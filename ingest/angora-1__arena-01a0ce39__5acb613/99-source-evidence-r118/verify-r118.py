#!/usr/bin/env python3
"""Validate the explicitly listed r118 local artifacts, not upstream truth."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv
import hashlib
import json
import re
import sys
from urllib.parse import urlsplit, unquote

D = Path('ingest/angora-1__arena-01a0ce39__5acb613/99-source-evidence-r118')
I = D.parent
W = I / '01-text-verbatim/workstation'


def strict_json(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=unique)


rows = list(csv.DictReader((D / 'local-verification-scope-before-read.csv').open(encoding='utf8', newline='')))
assert rows and len({r['path'] for r in rows}) == len(rows)
files = {}
inventory = []
for row in rows:
    path = Path(row['path'])
    data = path.read_bytes()
    assert len(data) == int(row['listed_bytes']), path
    files[path] = data
    inventory.append({'path': str(path), 'bytes_read': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
with (D / 'local-verification-inventory-after-read.csv').open('x', encoding='utf8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(inventory[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(inventory)

checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def text(path):
    return files[Path(path)].decode('utf8')


index_path = D / 'search-outcomes-v2.csv'
idx = list(csv.DictReader(text(index_path).splitlines()))
summary = strict_json(text(D / 'search-outcomes-v2-summary.json'))
check('48 unique indexed queries', len(idx) == 48 and len({x['id'] for x in idx}) == 48 and {x['id'] for x in idx} == {f'Q{x:02}' for x in range(1, 49)})
for row in idx:
    data = files[Path(row['response_file'])]
    obj = strict_json(data)
    assert hashlib.sha256(data).hexdigest() == row['sha256']
    assert len(data) == int(row['response_bytes'])
    assert len(obj['results']) == int(row['reported_results']) and obj['query'] == row['query'] and obj['status'] == 'success'
check('indexed bytes hashes queries statuses and item counts agree', True)
check('reported index aggregate counts', summary['result_items_including_repeated_and_irrelevant'] == sum(int(r['reported_results']) for r in idx) == 104 and summary['partially_redacted_responses'] == sum(r['capture'] == 'protected-partial' for r in idx) == 19 and summary['zero_result_responses'] == sum(int(r['reported_results']) == 0 for r in idx) == 5)

branch = D / 'institutional-pages/P05/www.find.com.tr/Company/angoranetworksbilisimteknolojiticaretsanayianonimsirketikirikkalesubesi/chunk-0.visible.manual.md'
bt = text(branch)
check('candidate fields and unverified disclaimer', all(x in bt for x in ['KIRIKKALE ŞUBESİ', '24 Mart 2023', '18.09.2023 06:44:00', 'Bilgiler Doğrulanmadı', 'angoranetworks.com', 'Üyeler Görebilir!', 'resmi hiçbir geçerliliği yoktur']))
p05 = strict_json(text(D / 'institutional-pages/P05/response-metadata.json'))
check('branch 2 of 2 separately transcribed', p05['reported_total_chunks'] == 2 and p05['manually_transcribed_chunks'] == [0, 1])

p06dir = D / 'park-archive/P06/www.kirikkaleteknopark.com/firma-rehberi/20230921184425'
chunks = [text(p06dir / f'chunk-{i}.visible.manual.md') for i in range(4)]
check('2023 park four local chunks no literal angora', sum(x.casefold().count('angora') for x in chunks) == 0)
check('park 8000 character boundaries plausible', all(len(x) == 8000 for x in chunks[:3]) and chunks[0].endswith('Cloudpeer Globa') and chunks[1].startswith('l Teknoloji]') and chunks[1].endswith('tarafından yazıla') and chunks[2].startswith('n yazılar') and chunks[2].endswith('[![]') and chunks[3].startswith('(https://'))
park2024 = text(I / '88-source-evidence-r116-2026-10-26/archive-chunks/kirikkaleteknopark.com/firma-rehberi/20240920103752/chunk-0.visible.md')
check('2024 park name and domain line', 'Angora Networks Bilişim' in park2024 and 'angoranetworks.com' in park2024)
interview = text(I / '53-source-evidence-r107-2026-10-26/corrected-r106/ictmedia.com.tr/haber/yerli-bir-ureticiye-verilebilecek-en-buyuk-destek-onun-urunlerini-kullanmaktir/index.tr.extracted.md')
check('interview generic technopark quote', 'Teknokente geçtik' in interview)
check('2023 archive UTC to Beijing conversion', datetime.fromisoformat('2023-09-21T18:44:25+00:00').astimezone(timezone(timedelta(hours=8))).isoformat() == '2023-09-22T02:44:25+08:00')
check('2024 archive UTC to Beijing conversion', datetime.fromisoformat('2024-09-20T10:37:52+00:00').astimezone(timezone(timedelta(hours=8))).isoformat() == '2024-09-20T18:37:52+08:00')

p04dir = D / 'institutional-pages/P04/www.find.com.tr/List/iletisim-cihazlari-ve-aksesuarlari-uretim/query-Page37-Grid'
p04 = [text(p04dir / f'chunk-{i}.visible.manual.md') for i in range(3)]
check('P04 recorded response boundary drift', p04[0].endswith('https://www.find.com') and p04[1].startswith('im-cihazlari') and p04[1].endswith('iletisim-cihazlari-ve') and p04[2].startswith('ler İthalat'))
for n in (1, 2, 3, 7):
    failure = strict_json(text(D / f'institutional-pages/P{n:02}/response-0.error.json'))
    assert failure['tool_visible_result']['status'] == 'error'
check('P01 P02 P03 P07 failed requests recorded separately', True)
search47 = strict_json(text(D / 'search-responses/Q47.protected-partial.json'))
p08 = text(D / 'institutional-pages/P08/kirikkaleteknopark.com/haberler/chunk-0.visible.manual.md')
check('Q47 address absent from P08 tool text', 'Ulubatlı' in search47['results'][0]['description'] and 'Ulubatlı' not in p08 and 'BİZE ULAŞIN' not in p08)

for n, rev in ((16, 'r1'), (19, 'r2'), (31, 'r1'), (48, 'r1')):
    old = strict_json(text(D / f'search-responses/Q{n:02}.tool-visible.manual.json'))
    new = strict_json(text(D / f'search-responses/Q{n:02}.tool-visible.manual.revision-{rev}.json'))
    assert 'status' not in old and new.pop('status') == 'success' and new == old
initial19 = strict_json(text(D / 'search-responses/Q19.tool-visible.manual.initial-version.json'))
check('four explicit JSON status repairs and Q19 earlier version had one valid status', initial19['status'] == 'success')

main = W / '09-orders/120-angora-orders-dossier-2026-10-21.md'
backup = D / 'dossier-before-r118/01-text-verbatim/workstation/09-orders/120-angora-orders-dossier-2026-10-21.md'
check('dossier byte-identical preserved prefix and one r118 index', files[main].startswith(files[backup]) and len(files[main]) - len(files[backup]) == 268 and files[main].count(b'120-angora-orders-dossier-2026-10-21.r118-appendix.md') == 1)

markdown_paths = [
    W / '08-customer-pipeline/187-angora-kirikkale-branch-candidate-r118-2026-10-26.md',
    W / '09-orders/120-angora-orders-dossier-2026-10-21.r118-appendix.md',
    W / '09-orders/120-angora-orders-master-2026-10-21.mapping-r118.md',
    I / '100-followup-angora-r118-2026-10-26/angora-networks.md',
    I / '101-audit-r118-2026-10-26.md',
    D / 'README.md', D / 'issues-and-corrections.md',
]
missing = []
link_count = 0
for path in markdown_paths:
    body = text(path)
    for match in re.finditer(r'(?<!!)\]\(([^)\s]+)', body):
        dest = match.group(1)
        parsed = urlsplit(dest)
        if parsed.scheme or dest.startswith('#'):
            continue
        rel = unquote(parsed.path)
        if not rel:
            continue
        target = path.parent / rel
        link_count += 1
        if not target.exists():
            missing.append({'source': str(path), 'destination': dest})
check('local Markdown links exist', not missing)
check('source evidence CSV paths resolve', all((D / r['source_path']).exists() for r in csv.DictReader(text(D / 'evidence-traceability.csv').splitlines())))

result = {
    'outcome': 'ok',
    'scope_files_listed': len(rows),
    'scope_files_fully_read': len(inventory),
    'bytes_read': sum(x['bytes_read'] for x in inventory),
    'checks_passed': len(checks),
    'checks': checks,
    'relative_markdown_links_checked': link_count,
    'missing_local_links': missing,
    'limitation': 'Only listed local bytes and structural assertions; not proof of source authenticity, independent evidence, complete external data, or exact manual transcription.',
}
with (D / 'local-verification-result.json').open('x', encoding='utf8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
