#!/usr/bin/env python3
"""Local provenance/integrity tests for r116; these do not certify external truth."""
import base64
import csv
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unittest
from urllib.parse import unquote

R = Path(__file__).resolve().parent
I = R.parent
REPO = I.parent.parent
W = I / '01-text-verbatim/workstation'
REPORT = W / '08-customer-pipeline/185-angora-historical-address-park-evidence-r116-2026-10-26.md'
APPENDIX = W / '09-orders/120-angora-orders-dossier-2026-10-21.r116-appendix.md'
MAPPING = W / '09-orders/120-angora-orders-master-2026-10-21.mapping-r116.md'
FOLLOW = I / '89-followup-angora-r116-2026-10-26/angora-networks.md'
AUDIT = I / '90-audit-r116-2026-10-26.md'
MASTER = W / '09-orders/120-angora-orders-dossier-2026-10-21.md'
BASE = '4624b8f52bd5d527a9b91c6e9661d3bdc682e433'


def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def rows(name):
    with (R / name).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


class R116Integrity(unittest.TestCase):
    def test_01_five_historical_git_blobs(self):
        files = [
            ('GH07','wireshark/wireshark/95bf9f5e0acac09f35cd8e8467cb6d93fb5a0d78/manuf'),
            ('GH08','wireshark/wireshark/0fcf4b1de93f79cc7d24ecb9c57193a61f822329/manuf'),
            ('GH16','gentoo/hwids/41e194e41bcb65e764c67562e2fba877b0b4408b/ma-small.txt'),
            ('GH17','gentoo/hwids/2986daf9bf2626efe6ff1d62f9713dad6cb82dae/ma-small.txt'),
            ('GH11','gentoo/hwids/cad1d07b026dd2c04b6940cf9c72b4b8639ae55b/ma-small.txt'),
        ]
        for api, relative in files:
            with self.subTest(api=api):
                meta = json.loads((R/'github-api'/f'{api}.body.json').read_text(encoding='utf-8'))
                data = (R/'github-raw/github.com'/relative).read_bytes()
                self.assertEqual(len(data), meta['size'])
                self.assertEqual(blob_sha(data), meta['sha'])
                if api in ('GH11','GH16','GH17'):
                    self.assertEqual(base64.b64decode(meta['content']), data)
                data.decode('utf-8')

    def test_02_wireshark_commit_parent_patch_and_time(self):
        obj=json.loads((R/'github-api/GH02.body.json').read_text(encoding='utf-8'))
        self.assertEqual(obj['sha'],'0fcf4b1de93f79cc7d24ecb9c57193a61f822329')
        self.assertEqual(obj['parents'][0]['sha'],'95bf9f5e0acac09f35cd8e8467cb6d93fb5a0d78')
        self.assertEqual(obj['commit']['committer']['date'],'2019-02-24T08:32:11Z')
        changes=[f for f in obj['files'] if f['filename']=='manuf']
        self.assertEqual(len(changes),1)
        self.assertIn('+70:B3:D5:82:20:00/36\tAngoraNe\tAngora Networks',changes[0]['patch'])

    def test_03_full_file_scans_and_target_lines(self):
        scans={r['id']:r for r in json.loads((R/'scan-full-file-exact-results.json').read_text(encoding='utf-8'))}
        self.assertEqual(set(scans),{'WS-PARENT','WS-CHILD','G-2018','G-2019','G-2020'})
        self.assertFalse(scans['WS-PARENT']['matches'])
        self.assertFalse(scans['G-2018']['matches'])
        self.assertEqual(scans['WS-CHILD']['matches'][0]['line'],26100)
        self.assertEqual([v['line'] for v in scans['G-2019']['matches']],[11069,11070])
        self.assertEqual([v['line'] for v in scans['G-2020']['matches']],[266,267])
        for item in scans.values():
            raw=(R/item['path']).read_bytes()
            self.assertEqual(item['bytes_read'],len(raw))
            self.assertEqual(item['sha256'],hashlib.sha256(raw).hexdigest())
            lines=raw.decode('utf-8').splitlines()
            found=[]
            for n,line in enumerate(lines,1):
                needles=[q for q in item['needles'] if q.casefold() in line.casefold()]
                if needles:
                    found.append({'line':n,'needles':needles,'text':line})
            self.assertEqual(item['matches'],found)

    def test_04_gentoo_snapshot_dates_and_address(self):
        for api,sha,date in [('GH12','41e194e41bcb65e764c67562e2fba877b0b4408b','2018-09-17T14:51:59Z'),
                             ('GH13','41e194e41bcb65e764c67562e2fba877b0b4408b','2018-09-17T14:51:59Z'),
                             ('GH14','2986daf9bf2626efe6ff1d62f9713dad6cb82dae','2019-03-17T01:37:12Z')]:
            obj=json.loads((R/'github-api'/f'{api}.body.json').read_text(encoding='utf-8'))
            self.assertEqual(obj[0]['sha'],sha)
            self.assertEqual(obj[0]['commit']['committer']['date'],date)
        text=(R/'github-raw/github.com/gentoo/hwids/2986daf9bf2626efe6ff1d62f9713dad6cb82dae/ma-small.txt').read_text(encoding='utf-8')
        self.assertIn('822000-822FFF     (base 16)\t\tAngora Networks',text)
        self.assertIn('Alacaatli Mah. Park Cad 47/31, Cayyolu',text)

    def test_05_cidr_arithmetic_and_nonexclusive_prefix(self):
        start=int('70b3d5822000',16)
        last=start+(1<<(48-36))-1
        self.assertEqual(last,int('70b3d5822fff',16))
        self.assertEqual(last-start+1,4096)
        text=(R/'github-raw/github.com/gentoo/hwids/2986daf9bf2626efe6ff1d62f9713dad6cb82dae/ma-small.txt').read_text(encoding='utf-8')
        self.assertIn('70-B3-D5   (hex)\t\tShenzhen Riitek Technology Co.,Ltd',text)

    def test_06_three_park_captures_are_separate_chunks(self):
        groups=[('www.kirikkaleteknopark.com','20201205142413'),
                ('kirikkaleteknopark.com','20240920103752'),
                ('kirikkaleteknopark.com','20260120061616')]
        for host,stamp in groups:
            d=R/'archive-chunks'/host/'firma-rehberi'/stamp
            paths=[d/f'chunk-{i}.visible.md' for i in range(4)]
            self.assertTrue(all(p.is_file() for p in paths))
            self.assertEqual([len(p.read_text(encoding='utf-8')) for p in paths[:3]],[8000]*3)
            self.assertGreater(len(paths[3].read_text(encoding='utf-8')),0)
            if stamp=='20201205142413':
                self.assertTrue(all('angora' not in p.read_text(encoding='utf-8').casefold() for p in paths))
            else:
                s=paths[0].read_text(encoding='utf-8')
                self.assertIn('##### Angora Networks Bilişim',s)
                self.assertIn('angoranetworks.com',s)

    def test_07_advensis_images_and_prior_sources_are_not_overclaimed(self):
        for date in ('20201021095900','20220123023037'):
            s=(R/'archive-replay/advensis.com.tr/en/angora-en'/date/'chunk-0.visible.md').read_text(encoding='utf-8')
            self.assertIn('angora3.jpg',s)
        s=(I/'81-source-evidence-r114-2026-10-26/archive-replay/support.angoranetworks.com/p/330/20240221043438/index.visible.md').read_text(encoding='utf-8')
        self.assertIn('Verge CLI guides are published',s)
        self.assertNotIn('2019-09-29',s)
        old=(I/'73-source-evidence-r112-2026-10-26/archive-index/support.angoranetworks.com/ht_kb/quick-start-guide/cdx.visible.md').read_text(encoding='utf-8')
        self.assertIn('[]',old)

    def test_08_future_chamber_header_and_retained_draft(self):
        d=R/'incomplete-observations/kirikkaletso.org.tr/ktso/basin/uyeler/4.GRUP.pdf'
        draft=(d/'chunk-0.initial-transcription.md').read_bytes()
        corrected=(d/'chunk-0.visible.md').read_bytes()
        self.assertNotEqual(draft,corrected)
        self.assertEqual(hashlib.sha256(draft).hexdigest(),'78d0fa501306d5e302cc82b46c0f78421ec7c7efec5868e368348ca7d48cfa99')
        self.assertEqual(len(corrected.decode('utf-8')),8000)
        self.assertIn('31.10.2026',corrected.decode('utf-8'))
        self.assertGreater(datetime.date(2026,10,31),datetime.date(2026,10,26))

    def test_09_eighty_four_search_metadata_not_claimed_full(self):
        search=list((R/'search-discovery').glob('Q*.json'))
        self.assertEqual(len(search),84)
        for p in search:
            obj=json.loads(p.read_text(encoding='utf-8'))
            self.assertEqual(obj['id'],p.stem)
            self.assertIn('NOT full search response',obj['fidelity'])
        self.assertIn('未完整持久化',(R/'README.md').read_text(encoding='utf-8'))

    def test_10_catalog_artifact_paths_and_unique_ids(self):
        catalog=rows('source-catalog.csv')
        self.assertEqual(len(catalog),44)
        self.assertEqual(len({r['id'] for r in catalog}),len(catalog))
        self.assertEqual(len({r['repo_relative_path'] for r in catalog}),len(catalog))
        for row in catalog:
            self.assertTrue((REPO/row['repo_relative_path']).is_file(),row['id'])
        for row in rows('evidence-traceability.csv'):
            self.assertTrue((REPO/row['repo_relative_path']).is_file(),row['claim_id'])

    def test_11_old_scoped_reads_and_sizes(self):
        summary=json.loads((R/'prior-round-read-summary.json').read_text(encoding='utf-8'))
        self.assertIn('102536',json.dumps(summary,ensure_ascii=False))
        ext=json.loads((R/'prior-sources-extension-read-inventory.json').read_text(encoding='utf-8'))
        dedup=json.loads((R/'support-dedup-read-inventory.json').read_text(encoding='utf-8'))
        self.assertEqual((len(ext),sum(x['bytes_read'] for x in ext)),(3,22974))
        self.assertEqual((len(dedup),sum(x['bytes_read'] for x in dedup)),(5,12307))
        for item in ext+dedup:
            b=(REPO/item['path']).read_bytes()
            self.assertEqual(hashlib.sha256(b).hexdigest(),item['sha256'])

    def test_12_master_prefix_is_byte_identical_without_decoding(self):
        rel=str(MASTER.relative_to(REPO))
        old=subprocess.check_output(['git','show',f'{BASE}:{rel}'],cwd=REPO)
        new=MASTER.read_bytes()
        meta=json.loads((R/'master-index-append-verification.json').read_text(encoding='utf-8'))
        self.assertEqual(len(old),52516)
        self.assertEqual(hashlib.sha256(old).hexdigest(),'bd9c0646f3f3571819623d92f9df7c693852e0c977218a931ddbe94b25697afc')
        self.assertTrue(new.startswith(old))
        self.assertEqual(len(new)-len(old),meta['appended_bytes'])
        self.assertEqual(hashlib.sha256(new).hexdigest(),meta['new_sha256'])

    def test_13_round_readback_scope_and_checksums(self):
        scope=rows('round-readback-scope.csv')
        inv=rows('round-readback-inventory.csv')
        self.assertEqual([r['path'] for r in scope],[r['path'] for r in inv])
        self.assertEqual(len({r['path'] for r in scope}),len(scope))
        total=0
        for listed,record in zip(scope,inv):
            p=REPO/listed['path']
            data=p.read_bytes()
            self.assertEqual(len(data),int(listed['listed_bytes']))
            self.assertEqual(len(data),int(record['bytes_read']))
            self.assertEqual(hashlib.sha256(data).hexdigest(),record['sha256'])
            data.decode('utf-8')
            total+=len(data)
        summary=json.loads((R/'round-readback-summary.json').read_text(encoding='utf-8'))
        self.assertEqual(summary['listed_paths'],len(scope))
        self.assertEqual(summary['read_paths'],len(scope))
        self.assertEqual(summary['total_bytes'],total)

    def test_14_deliverable_links_resolve(self):
        documents=[REPORT,APPENDIX,MAPPING,FOLLOW,AUDIT,R/'README.md']
        pattern=re.compile(r'(?<!!)\[[^\]]+\]\(([^\s)]+)\)')
        count=0
        for p in documents:
            self.assertTrue(p.is_file(),p)
            for target in pattern.findall(p.read_text(encoding='utf-8')):
                if target.startswith(('https://','http://','mailto:','#')):
                    continue
                local=unquote(target.split('#',1)[0])
                with self.subTest(document=p.name,target=target):
                    self.assertTrue((p.parent/local).exists(),target)
                    count+=1
        self.assertGreater(count,30)

    def test_15_entity_boundary_and_no_forced_identity(self):
        for path in (REPORT,APPENDIX,MAPPING,FOLLOW):
            text=path.read_text(encoding='utf-8')
            self.assertIn('主体未确认',text)
        self.assertIn('C 档不跟进',FOLLOW.read_text(encoding='utf-8'))
        self.assertIn('不是两份独立',APPENDIX.read_text(encoding='utf-8'))


if __name__=='__main__':
    unittest.main(verbosity=2)
