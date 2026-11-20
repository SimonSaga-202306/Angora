#!/usr/bin/env python3
"""Local integrity checks only; they do not authenticate sources or prove historical events."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import csv
import hashlib
import json
import re
import subprocess
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / '.git').exists())
I = ROOT / 'ingest/angora-1__arena-01a0ce39__5acb613'
R = I / '92-source-evidence-r117-2026-10-26'
A = R / 'github-api'
W = I / '01-text-verbatim/workstation'
S = I / '91-entry-safety-r117-2026-10-26'
REPORT = W / '08-customer-pipeline/186-angora-pen-park-identity-evidence-r117-2026-10-26.md'
APPENDIX = W / '09-orders/120-angora-orders-dossier-2026-10-21.r117-appendix.md'
MAPPING = W / '09-orders/120-angora-orders-master-2026-10-21.mapping-r117.md'
FOLLOW = I / '93-followup-angora-r117-2026-10-26/angora-networks.md'
AUDIT = I / '94-audit-r117-2026-10-26.md'
MASTER = W / '09-orders/120-angora-orders-dossier-2026-10-21.md'


def load(path):
    return json.loads(path.read_text(encoding='utf8'))


def csvrows(path):
    with path.open(encoding='utf8', newline='') as f:
        return list(csv.DictReader(f))


def git_blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def rawmeta(name):
    return load(A / (name + '-raw.request.json'))


class Integrity(unittest.TestCase):
    def test_01_sixteen_full_git_snapshots(self):
        meta = sorted(A.glob('*-raw.request.json'))
        self.assertEqual(len(meta), 16)
        total = 0
        for p in meta:
            m = load(p)
            b = (ROOT / m['path']).read_bytes()
            total += len(b)
            self.assertEqual(len(b), m['bytes'], p.name)
            self.assertEqual(hashlib.sha256(b).hexdigest(), m['sha256'], p.name)
            self.assertEqual(git_blob(b), m['api_git_blob_sha1'], p.name)
            self.assertTrue(m['blob_equal'] and m['size_equal'])
            b.decode('utf8')
        self.assertEqual(total, 70958756)

    def test_02_ietf_parent_child_and_patch(self):
        parent = rawmeta('IETFPARENT')
        child = rawmeta('IETFCHILD')
        before = (ROOT / parent['path']).read_text(encoding='utf8').splitlines()
        after = (ROOT / child['path']).read_text(encoding='utf8').splitlines()
        self.assertFalse(any(x.strip() in {'58029', 'Angora Networks'} for x in before))
        n = [i for i, line in enumerate(after) if line.strip() == '58029']
        self.assertEqual(len(n), 1)
        self.assertEqual(after[n[0] + 1].strip(), 'Angora Networks')
        self.assertEqual(n[0] + 1, 231668)
        c = load(A / 'G50.body.json')
        self.assertEqual(c['sha'], 'fe367b60547788ed755be66dbec17e819f63c77c')
        self.assertEqual(c['parents'][0]['sha'], 'ae9ceebec6bf7a4034e6c8d6768e13b7f4f95883')
        fileinfo = next(x for x in c['files'] if x['filename'] == 'enterprise-numbers/enterprise-numbers')
        self.assertEqual(fileinfo['sha'], child['api_git_blob_sha1'])
        diff = (R / 'pen-ietf-parent-child-local.diff').read_text(encoding='utf8')
        self.assertIn('+58029\n+  Angora Networks\n', diff)
        self.assertEqual(diff[diff.index('@@ '):].rstrip('\n'), fileinfo['patch'].rstrip('\n'))
        self.assertEqual(c['commit']['committer']['date'], '2021-10-20T16:45:45Z')

    def test_03_cross_repository_equal_bytes(self):
        for x, y in [('IETFPARENT', 'PEN21PARENT'), ('PENIETF1022', 'PEN21OCT')]:
            a = (ROOT / rawmeta(x)['path']).read_bytes()
            b = (ROOT / rawmeta(y)['path']).read_bytes()
            self.assertEqual(a, b)
        comparisons = load(R / 'pen-ietf-parent-child-comparison-result.json')['cross_repository_byte_comparisons']
        self.assertEqual(len(comparisons), 2)
        self.assertTrue(all(x['byte_equal'] for x in comparisons))

    def test_04_rfinnie_parent_child(self):
        o = load(A / 'G40.body.json')
        self.assertEqual(o['parents'][0]['sha'], 'c99419cac238e3960c1942506514dd2f87df202b')
        f = next(x for x in o['files'] if x['filename'] == 'www.iana.org/assignments/enterprise-numbers/enterprise-numbers')
        d = (R / 'pen-parent-child-local.diff').read_text(encoding='utf8')
        self.assertEqual(d[d.index('@@ '):].rstrip('\n'), f['patch'].rstrip('\n'))
        self.assertIn('+58029\n+  Angora Networks\n', d)

    def test_05_park_chunks_and_reconstruction_disclosure(self):
        inventory = load(R / 'park-new-full-scan-results.json')
        self.assertEqual(len(inventory), 8)
        self.assertEqual(sum(x['bytes_read'] for x in inventory), 55657)
        for item in inventory:
            b = (ROOT / item['path']).read_bytes()
            self.assertEqual(hashlib.sha256(b).hexdigest(), item['sha256'])
            self.assertNotIn('angora', b.decode('utf8').casefold())
        metadata = csvrows(R / 'archive-response-metadata.csv')
        self.assertEqual(len(metadata), 8)
        self.assertEqual(sum('constructed' in x['provenance'] for x in metadata), 3)
        self.assertIn('重构', REPORT.read_text(encoding='utf8'))

    def test_06_prior_positive_and_namesake_separate(self):
        for date in ('20240920103752', '20260120061616'):
            p = I / ('88-source-evidence-r116-2026-10-26/archive-chunks/kirikkaleteknopark.com/firma-rehberi/' + date + '/chunk-0.visible.md')
            s = p.read_text(encoding='utf8')
            self.assertIn('Angora Networks Bilişim', s)
            self.assertIn('angoranetworks.com', s)
        founder = (I / '81-source-evidence-r114-2026-10-26/archive-replay/ortakakil.org.tr/ozgecmisler/levent-kilic/20210622052721/index.visible.md').read_text(encoding='utf8')
        official = (R / 'external-visible/sincan.gov.tr/makam/chunk-0.visible.md').read_text(encoding='utf8')
        self.assertIn('1969', founder)
        self.assertIn('Angora Networks', founder)
        self.assertIn('1966', official)
        self.assertIn('Kamu Yönetimi', official)

    def test_07_search_outcomes_and_secret_guard(self):
        rows = csvrows(R / 'search-outcomes.csv')
        self.assertEqual(len(rows), 20)
        self.assertEqual(sum(int(x['manually_counted_results']) for x in rows), 44)
        yes = [x for x in rows if x['full_response_manually_transcribed'] == 'yes']
        self.assertEqual(len(yes), 16)
        self.assertEqual({x['id'] for x in rows if x['full_response_manually_transcribed'] == 'no'}, {'Q02', 'Q03', 'Q07', 'Q11'})
        for row in yes:
            p = ROOT / row['repo_relative_path']
            obj = load(p)
            self.assertIn('results', obj)
            raw = p.read_text(encoding='utf8')
            self.assertNotIn('AWSAccessKeyId=', raw)
            self.assertNotIn('Signature=', raw)

    def test_08_video_incomplete_and_draft_preserved(self):
        row = next(x for x in csvrows(R / 'fetch-outcomes.csv') if x['id'] == 'V23')
        self.assertEqual(row['reported_total_chunks'], '177')
        self.assertEqual(row['attempted_chunk_indexes'], '0')
        self.assertEqual(row['status'], 'incomplete')
        d = R / 'incomplete-observations/www.youtube.com/watch/z0loF632E2s'
        initial = (d / 'chunk-0.initial-transcription.md').read_text(encoding='utf8')
        corrected = (d / 'chunk-0.visible.md').read_text(encoding='utf8')
        self.assertEqual(initial.replace('&&message.indexOf("Polymer")<0', '', 1), corrected)
        result = load(d / 'chunk-0-correction-result.json')
        self.assertEqual(hashlib.sha256(initial.encode()).hexdigest(), result['initial_sha256'])
        self.assertEqual(hashlib.sha256(corrected.encode()).hexdigest(), result['corrected_sha256'])

    def test_09_q01_correction(self):
        d = R / 'search-visible'
        a = (d / 'Q01.initial-manual.json').read_bytes()
        b = (d / 'Q01.json').read_bytes()
        result = load(d / 'Q01-transcription-correction-result.json')
        self.assertEqual(hashlib.sha256(a).hexdigest(), result['initial_sha256'])
        self.assertEqual(hashlib.sha256(b).hexdigest(), result['corrected_sha256'])
        self.assertEqual(len(json.loads(b)['results']), 3)

    def test_10_named_corrections_and_date_scope(self):
        for p in (REPORT, APPENDIX, MAPPING):
            s = p.read_text(encoding='utf8')
            self.assertIn('修正／取代 r116', s, p.name)
            self.assertIn('r114', s, p.name)
            self.assertIn('不是用户', s, p.name)
        self.assertIn('2026-10-26', (R / 'date-scope-correction-r117.md').read_text(encoding='utf8'))
        self.assertIn('2026-11-20', (R / 'date-scope-correction-r117.md').read_text(encoding='utf8'))

    def test_11_entry_safety_and_stash(self):
        meta = load(S / 'stash-third-parent-verification.json')
        self.assertEqual(meta['listed_paths'], 868)
        self.assertEqual(meta['matching_blob_paths'], 868)
        self.assertTrue(meta['safety_directory_not_in_stash'])
        self.assertEqual(meta['matching_bytes_scope'], 46015150)
        corr = load(S / 'backup-correction-summary.json')
        self.assertTrue(corr)
        # This check is local to the current environment: stash refs may not survive another environment reset.
        raw = subprocess.check_output(['git', 'ls-tree', '-r', '-z', '--full-tree', meta['third_parent_untracked_commit']], cwd=ROOT)
        files = {}
        for entry in raw.split(b'\0'):
            if entry:
                left, path = entry.split(b'\t', 1)
                files[path.decode()] = left.decode().split()[2]
        initial = csvrows(S / 'initial-untracked-comparison.csv')
        self.assertEqual(len(files), len(initial))
        self.assertEqual(len(initial), 868)
        for row in initial:
            self.assertEqual(files[row['path']], row['git_blob_sha1'])

    def test_12_master_index_append_only(self):
        plan = load(R / 'master-index-append-plan-before-write.json')
        result = load(R / 'master-index-append-result.json')
        b = MASTER.read_bytes()
        payload = (R / 'master-index-append-payload.txt').read_bytes()
        self.assertEqual(hashlib.sha256(b[:plan['old_bytes']]).hexdigest(), plan['old_sha256'])
        self.assertEqual(b[plan['old_bytes']:], payload)
        self.assertEqual(hashlib.sha256(b).hexdigest(), result['new_sha256'])
        self.assertEqual(b.count(b'.r117-appendix.md'), 1)

    def test_13_source_catalogue_paths_sizes_hashes(self):
        rows = csvrows(R / 'source-catalog.csv')
        self.assertEqual(len(rows), 110)
        self.assertEqual(len({x['repo_relative_path'] for x in rows}), 110)
        for row in rows:
            p = ROOT / row['repo_relative_path']
            b = p.read_bytes()
            self.assertEqual(len(b), int(row['bytes']), row['source_id'])
            self.assertEqual(hashlib.sha256(b).hexdigest(), row['sha256'], row['source_id'])

    def test_14_round_readback_scope_and_hashes(self):
        scope = csvrows(R / 'round-readback-scope.csv')
        inv = csvrows(R / 'round-readback-inventory.csv')
        summary = load(R / 'round-readback-summary.json')
        self.assertEqual(len(scope), len(inv))
        self.assertEqual(summary['listed_files'], len(scope))
        self.assertEqual(summary['fully_read_files'], len(inv))
        for a, b in zip(scope, inv):
            self.assertEqual(a['path'], b['path'])
            data = (ROOT / b['path']).read_bytes()
            self.assertEqual(len(data), int(b['bytes_read']))
            self.assertEqual(hashlib.sha256(data).hexdigest(), b['sha256'])

    def test_15_deliverable_links_resolve(self):
        for p in (REPORT, APPENDIX, MAPPING, FOLLOW, AUDIT):
            text = p.read_text(encoding='utf8')
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if target.startswith(('http://', 'https://', 'mailto:', '#')):
                    continue
                part = unquote(urlsplit(target).path)
                if part:
                    self.assertTrue((p.parent / part).exists(), f'{p.name}: {target}')

    def test_16_clock_and_single_subject(self):
        t = load(R / 'completion-clock.json')
        self.assertGreaterEqual(t['elapsed_seconds'], 600)
        self.assertEqual(t['environment_boot_id_start'], t['environment_boot_id_finish'])
        f = FOLLOW.read_text(encoding='utf8')
        self.assertIn('主体未确认', f)
        self.assertIn('C 档不跟进', f)
        self.assertIn('未新增 Ewind', f)
        self.assertIn('1/177', AUDIT.read_text(encoding='utf8'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
