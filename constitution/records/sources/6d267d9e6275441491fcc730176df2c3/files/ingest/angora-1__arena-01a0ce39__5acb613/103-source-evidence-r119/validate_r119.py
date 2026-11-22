#!/usr/bin/env python3
"""Bounded byte/structure/link checks for the prelisted r119 deliverable set."""
from pathlib import Path
import csv
import hashlib
import json
import random
import re

D = Path(__file__).resolve().parent
ROOT = D.parents[2]
scope_path = D / 'final-validation-scope-v2-before-read.csv'
with scope_path.open(encoding='utf8', newline='') as f:
    scope = list(csv.DictReader(f))
assert len(scope) == len({x['path'] for x in scope})
inventory = []
json_count = csv_count = 0
emails = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}', re.I)
credentials = re.compile(r'''(?i)(?:authorization\s*:\s*bearer\s+\S+|(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|passwd)\s*[=:]\s*["']?[A-Za-z0-9_\-]{8,})''')
sensitive_url = re.compile(r'(?i)[?&](?:token|sig|signature|session|auth|x-amz-credential|x-amz-signature)=')
privacy_hits = []
for row in scope:
    p = ROOT / row['path']
    if p.is_symlink() or not p.is_file() or '.arena' in p.parts:
        raise ValueError(f'unsafe or missing path {p}')
    b = p.read_bytes()
    if len(b) != int(row['listed_bytes']):
        raise ValueError(f'file changed since pre-list: {p}')
    inventory.append({'path':row['path'],'bytes_read':len(b),'sha256':hashlib.sha256(b).hexdigest()})
    try:
        text = b.decode('utf8')
    except UnicodeDecodeError:
        text = None
    if p.suffix in {'.md','.py','.csv','.json','.txt'} and text is None:
        raise ValueError(f'expected UTF-8: {p}')
    if p.suffix == '.json':
        json.loads(text); json_count += 1
    elif p.suffix == '.csv':
        list(csv.reader(text.splitlines(), strict=True)); csv_count += 1
    if text is not None:
        e, c, u = emails.findall(text), credentials.findall(text), sensitive_url.findall(text)
        if e or c or u:
            privacy_hits.append({'path':row['path'],'email_like_count':len(e),
                                 'credential_pattern_count':len(c),'sensitive_url_count':len(u)})
if privacy_hits:
    raise ValueError('privacy heuristic hits (counts/paths only): '+json.dumps(privacy_hits,ensure_ascii=False))

with (D/'final-validation-inventory-after-read.csv').open('x',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes_read','sha256'],lineterminator='\n')
    w.writeheader();w.writerows(inventory)
sample = random.Random(1192026).sample(inventory, min(30, len(inventory)))
for row in sample:
    h = hashlib.sha256()
    with (ROOT/row['path']).open('rb') as f:
        for block in iter(lambda:f.read(4096),b''):
            h.update(block)
    if h.hexdigest() != row['sha256']:
        raise ValueError('streaming sample mismatch '+row['path'])

with (D/'request-outcomes.csv').open(encoding='utf8',newline='') as f:
    requests=list(csv.DictReader(f))
assert len(requests)==71 and len({x['id'] for x in requests})==71
assert sum(x['kind']=='web_search' for x in requests)==40
assert sum(x['kind']=='fetch_page' for x in requests)==25
assert sum(x['kind']=='fetch_page_archive_index' for x in requests)==5
assert sum(x['kind']=='fetch_page_time_reference' for x in requests)==1
assert sum(x['status']=='error' for x in requests)==4
for row in requests:
    manifest = json.loads((ROOT/row['manifest_path']).read_text(encoding='utf8'))
    assert manifest['id']==row['id'] and manifest['actual_request_time'] is None
    assert all((ROOT/x).is_file() for x in manifest['input_paths'])
with (D/'source-catalog.csv').open(encoding='utf8',newline='') as f:
    sources=list(csv.DictReader(f))
assert len(sources)==27 and len({x['source_id'] for x in sources})==27
assert all((ROOT/x['local_path']).is_file() for x in sources)
with (D/'evidence-traceability.csv').open(encoding='utf8',newline='') as f:
    claims=list(csv.DictReader(f))
source_ids={x['source_id'] for x in sources}
assert len(claims)==8 and all(set(x['source_ids'].split(';')) <= source_ids for x in claims)
comparison=json.loads((D/'claims-comparison-result.json').read_text(encoding='utf8'))
assert (comparison['shortlist_names_count'],comparison['solution_heading_count'],comparison['textual_matches_with_explicit_aliases'],comparison['alias_based_matches'])==(20,20,20,5)
assert comparison['angora_in_winner_paragraph'] is False and comparison['angora_in_solution_headings'] is True
assert comparison['sum_try']==4000000
with (D/'claims-comparison-inventory-after-read.csv').open(encoding='utf8',newline='') as f:
    compared=list(csv.DictReader(f))
assert len(compared)==15
for row in compared:
    b=(ROOT/row['path']).read_bytes()
    assert len(b)==int(row['bytes_read']) and hashlib.sha256(b).hexdigest()==row['sha256']
prior=json.loads((D/'prior-reading-sample-verification.json').read_text(encoding='utf8'))
assert (prior['listed_files'],prior['fully_read_files'],prior['fully_read_bytes'],prior['sample_count'])==(1081,1081,83394100,35)
old=json.loads((D/'r114-crosscheck-summary.json').read_text(encoding='utf8'))
assert (old['prelisted'],old['fully_read'],old['bytes'],old['streaming_sample'])==(22,22,186101,8)

I=ROOT/'ingest/angora-1__arena-01a0ce39__5acb613'
docs=[I/'01-text-verbatim/workstation/08-customer-pipeline/188-angora-registry-event-disambiguation-r119-2026-10-26.md',I/'01-text-verbatim/workstation/09-orders/120-angora-orders-dossier-2026-10-21.r119-appendix.md',I/'01-text-verbatim/workstation/09-orders/120-angora-orders-master-2026-10-21.mapping-r119.md',I/'104-followup-angora-r119/angora-networks.md',I/'105-audit-r119.md',D/'README.md',D/'issues-and-corrections.md',D/'2022-agenda-search-splice-observation.md',ROOT/'constitution/README.md',ROOT/'constitution/issues/r119-time-and-source-date-correction-v2.md',ROOT/'constitution/issues/r119-time-observations-and-scope.md',ROOT/'constitution/issues/r119-application-state-and-scope.md']
links=[]
for doc in docs:
    s=doc.read_text(encoding='utf8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',s):
        target=target.strip().split(' ',1)[0]
        if re.match(r'^[a-z][a-z0-9+.-]*:',target,re.I) or target.startswith('#'):
            continue
        path=target.split('#',1)[0].split('?',1)[0]
        if not path: continue
        links.append((doc,(doc.parent/path).resolve()))
# The summary is the output of this program and the ledger receipts are generated later.
deferred={str((D/'final-validation-summary.json').resolve()),str((D/'ledger-capture-receipts.jsonl').resolve())}
missing=[(str(a.relative_to(ROOT)),str(b)) for a,b in links if not b.exists() and str(b) not in deferred]
if missing:
    raise ValueError('broken local links: '+json.dumps(missing,ensure_ascii=False))
summary={'scope_listed':len(scope),'fully_read':len(inventory),'bytes':sum(x['bytes_read'] for x in inventory),
         'sample_seed':1192026,'streaming_sample_verified':len(sample),'sample_paths':[x['path'] for x in sample],
         'json_files_parsed':json_count,'csv_files_parsed':csv_count,'privacy_heuristic_hits':len(privacy_hits),
         'request_manifests_checked':len(requests),'curated_sources_checked':len(sources),'claim_rows_checked':len(claims),
         'compared_file_hashes_verified':len(compared),'markdown_local_links_checked':len(links),
         'deferred_generated_link_targets':[x for x in sorted(deferred) if not Path(x).exists()],
         'limitations':'Restricted prelisted versions only; later logs, ledger records, snapshots, final message and pushes excluded. Heuristic privacy scan and hashes do not prove completeness, source truth, legal identity or original-response fidelity.'}
with (D/'final-validation-summary.json').open('x',encoding='utf8') as f:
    json.dump(summary,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in summary.items() if k!='sample_paths'},ensure_ascii=False,indent=2))
