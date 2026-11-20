#!/usr/bin/env python3
"""Index each saved r117 source artifact without merging or equating witnesses."""
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
I = ROOT / 'ingest/angora-1__arena-01a0ce39__5acb613'
R = I / '92-source-evidence-r117-2026-10-26'
# Resolve independently of the current shell working directory.
if not I.is_dir():
    ROOT = next(p for p in Path(__file__).resolve().parents if (p / '.git').exists())
    I = ROOT / 'ingest/angora-1__arena-01a0ce39__5acb613'
    R = I / '92-source-evidence-r117-2026-10-26'

rows = []
def add(source_id, kind, source_url, path, time_field, fidelity, boundary):
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    data = p.read_bytes()
    rows.append({
        'source_id': source_id, 'kind': kind, 'source_url': source_url,
        'repo_relative_path': p.relative_to(ROOT).as_posix(), 'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest(), 'time_field': time_field,
        'fidelity': fidelity, 'boundary': boundary,
    })

# The per-snapshot plans were written before the associated GitHub requests.
snapshot_plans = [
    'github-pen-snapshot-plan-before-download.csv',
    'github-pen-snapshot-plan-extension-before-download.csv',
    'github-pen-snapshot-plan-early-before-download.csv',
    'github-pen-snapshot-plan-2021-before-download.csv',
    'github-pen-snapshot-plan-autumn-before-download.csv',
    'github-pen-snapshot-plan-september-before-download.csv',
    'github-pen-parent-plan-before-download.csv',
    'github-pen-snapshot-plan-ietf-october-before-download.csv',
    'github-pen-ietf-parent-child-plan-before-download.csv',
]
for filename in snapshot_plans:
    with (R / filename).open(encoding='utf8', newline='') as f:
        for item in csv.DictReader(f):
            meta = json.loads((R / 'github-api' / (item['id'] + '-raw.request.json')).read_text(encoding='utf8'))
            assert meta['exit_code'] == 0 and meta['blob_equal'] and meta['size_equal']
            url = f"https://github.com/{item['repo']}/blob/{item['commit']}/{item['path']}"
            add(item['id'], 'Git mirror full snapshot', url, meta['path'], item['commit_utc'],
                'full raw bytes; Git blob and size match contents API',
                'mirror timestamp and file header not the individual allocation date; copies can share one IANA dataset')

# API outputs are raw gh stdout, each query/commit preserved individually with separate stderr and request metadata.
for p in sorted((R / 'github-api').glob('G[0-9][0-9].body.json')):
    sid = p.name.split('.')[0]
    req = json.loads((p.parent / (sid + '.request.json')).read_text(encoding='utf8'))
    add(sid, 'GitHub API response', 'https://api.github.com/' + req['endpoint'], p,
        'request observation monotonic in companion metadata; no calibrated wall time',
        'complete gh stdout bytes; request/stderr alongside',
        'search results and commit patches require source interpretation; zero search is not absence')

with (R / 'archive-response-metadata.csv').open(encoding='utf8', newline='') as f:
    for a in csv.DictReader(f):
        add(a['id'], 'archive tool chunk', a['requested_url'], R / a['content_path_relative_to_r117'],
            a['requested_url'].split('/web/')[1].split('/')[0], a['provenance'],
            'same park directory; snapshots are not separate witnesses, membership proof or original HTML')

add('N01', 'government biography tool chunk', 'https://sincan.gov.tr/makam',
    R / 'external-visible/sincan.gov.tr/makam/chunk-0.visible.md', 'current page; capture time not independently calibrated',
    'manual transcription of 1/1 tool block; not original HTML', 'identity disambiguation only; no business or government relationship inferred')
add('V23', 'incomplete video tool chunk', 'https://www.youtube.com/watch?v=z0loF632E2s',
    R / 'incomplete-observations/www.youtube.com/watch/z0loF632E2s/chunk-0.visible.md', 'tool metadata self-reports 2023-05-24',
    'corrected manual first chunk of 177; JavaScript appears where transcript expected', 'no audio or complete transcript; cannot use for interview content claim')
add('V23-DRAFT', 'transcription draft', 'https://www.youtube.com/watch?v=z0loF632E2s',
    R / 'incomplete-observations/www.youtube.com/watch/z0loF632E2s/chunk-0.initial-transcription.md', 'same request as V23',
    'initial manual draft retained with correction record', 'not a separate request or independent witness')

for p in sorted((R / 'search-visible').glob('Q[0-9][0-9].json')):
    add(p.stem, 'search discovery response', '', p, 'no reliable page publication inference from search timestamp',
        'manual transcription; no automated comparison with tool original',
        'discovery only; duplicates and unrelated results; not page body')

prior = [
    ('OLD-INTERVIEW', I / '53-source-evidence-r107-2026-10-26/corrected-r106/ictmedia.com.tr/haber/yerli-bir-ureticiye-verilebilecek-en-buyuk-destek-onun-urunlerini-kullanmaktir/index.tr.extracted.md', '2023-06-08 page self-date', 'media summary of interview; park unnamed'),
    ('OLD-FOUNDER', I / '81-source-evidence-r114-2026-10-26/archive-replay/ortakakil.org.tr/ozgecmisler/levent-kilic/20210622052721/index.visible.md', '2021-06-22 archive capture', 'organization biography; named founder, not identity document'),
]
for sid, path, time_field, boundary in prior:
    add(sid, 'prior-round source', '', path, time_field, 'old manually transcribed tool-visible text', boundary)
B = I / '88-source-evidence-r116-2026-10-26/archive-chunks'
for date in ('20201205142413', '20240920103752', '20260120061616'):
    paths = sorted(B.glob('**/' + date + '/chunk-*.visible.md'))
    assert len(paths) == 4
    for p in paths:
        add('OLD-' + date + '-' + p.stem, 'prior park archive tool chunk', '', p, date,
            'old manual transcription; not original HTML', 'same park source; not entry/exit date')

out = R / 'source-catalog.csv'
with out.open('w', encoding='utf8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
print('Catalogued artifacts:', len(rows), '(not independent sources); bytes:', sum(r['bytes'] for r in rows))
