#!/usr/bin/env python3
"""Copy each prelisted r120/v3 file separately and record each request & issue event."""
from pathlib import Path
import csv
import hashlib
import json
import subprocess
import sys

D = Path(__file__).resolve().parent
ROOT = D.parents[2]
ledger = ROOT / 'tools/constitution_ledger.py'

with (D / 'ledger-input-scope-before-read.csv').open(encoding='utf8', newline='') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == len({x['path'] for x in rows})

inventory = []
for x in rows:
    p = ROOT / x['path']
    if not p.is_file() or p.is_symlink() or '.arena' in p.parts:
        raise ValueError('invalid input ' + str(p))
    b = p.read_bytes()
    if len(b) != int(x['listed_bytes']):
        raise ValueError('input changed since listing ' + str(p))
    inventory.append({
        'path': x['path'],
        'bytes_read': len(b),
        'sha256': hashlib.sha256(b).hexdigest(),
        'method': x['method'],
        'classification': x['classification'],
    })

with (D / 'ledger-input-inventory-after-read.csv').open('w', encoding='utf8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['path', 'bytes_read', 'sha256', 'method', 'classification'], lineterminator='\n')
    w.writeheader()
    w.writerows(inventory)

receipt_path = D / 'ledger-capture-receipts.jsonl'
counts = {'source': 0, 'request_event': 0, 'issue_event': 0}
with receipt_path.open('w', encoding='utf8') as receipts:
    def run(kind, path, extra, note, supersedes=None):
        args = [sys.executable, str(ledger), kind, '--file', str(ROOT / path), '--method', extra['method'], '--note', note]
        if kind == 'source':
            args += ['--original-path', path]
        else:
            args += ['--event-kind', extra['event_kind']]
        if supersedes:
            args += ['--supersedes', supersedes]
        r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
        row = {'kind': kind, 'input_path': path, 'exit_code': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr}
        if r.returncode == 0:
            data = json.loads(r.stdout)
            if data.get('outcome') != 'copied':
                raise ValueError('unexpected ledger result ' + r.stdout)
            row['record_id'] = data['id']
        receipts.write(json.dumps(row, ensure_ascii=False) + '\n')
        receipts.flush()
        if r.returncode:
            raise RuntimeError(f'ledger failed for {path}; see receipts')

    for x in inventory:
        note = ('r120/v3 separate file; ' + x['classification'] + '; local file copied byte-for-byte; '
                'not an assertion that an upstream web response was captured byte-for-byte. Event time unknown.')
        run('source', x['path'], {'method': x['method']}, note)
        counts['source'] += 1

    manifests = sorted((D / 'request-manifests').glob('*.json'))
    assert len(manifests) == 48
    for p in manifests:
        path = str(p.relative_to(ROOT))
        run('event', path, {'method': 'supplied_file', 'event_kind': 'tool_request_observation'},
            'One r120 request per derived manifest; tool output is manual protected excerpt or tool-visible transcription. Actual request time unknown.')
        counts['request_event'] += 1

    issues = [
        (ROOT / 'constitution/issues/r119-r120-date-correction-v3.md', 'date_correction_v3', '3d38b1e37ed14ae6b266a9c4785bc61e',
         'v3 date correction establishing 2026-11-22 UTC session date; supersedes r120 clarification 3d38b1e37ed14ae6b266a9c4785bc61e and covers v1/v2.'),
        (D / 'date-scope-correction-v3.md', 'date_correction_v3', None,
         'r120 plan and CDX filter date scope correction under v3; preserves original plan files unchanged.'),
        (D / 'crosscheck-plan-before-reread.md', 'reading_order_remediation', None,
         'r120 supplementary reread remediation plan; does not retroactively validate initial inspection order.'),
        (D / 'issues-and-corrections.md', 'issue_or_verification', None,
         'r120 named issues, corrections and limits.'),
        (D / 'crosscheck-result.json', 'issue_or_verification', None,
         'r120 12/12 prelisted reread and 4/4 streaming hash verification result.'),
        (D / 'final-validation-summary.json', 'issue_or_verification', None,
         'r120 bounded validation summary across 175 prelisted files.'),
    ]
    for p, ekind, sup, note in issues:
        run('event', str(p.relative_to(ROOT)), {'method': 'supplied_file', 'event_kind': ekind}, note, supersedes=sup)
        counts['issue_event'] += 1

summary = {
    'scope': len(rows),
    'bytes': sum(x['bytes_read'] for x in inventory),
    'source_records': counts['source'],
    'request_events': counts['request_event'],
    'issue_or_check_events': counts['issue_event'],
    'receipt_lines': sum(counts.values()),
    'limits': 'Receipts, resulting records, snapshots and later messages are generated after input scope; their consistency requires separate verification.'
}
with (D / 'ledger-capture-summary.json').open('w', encoding='utf8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))
PY