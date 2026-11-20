#!/usr/bin/env python3
"""Pre-list, fully read, hash r117 bounded artifacts; does not validate provenance."""
from pathlib import Path
import csv
import hashlib
import json
import time

ROOT = next(p for p in Path(__file__).resolve().parents if (p / '.git').exists())
I = ROOT / 'ingest/angora-1__arena-01a0ce39__5acb613'
R = I / '92-source-evidence-r117-2026-10-26'
S = I / '91-entry-safety-r117-2026-10-26'
EXCLUDE = {
    'round-readback-scope.csv', 'round-readback-inventory.csv', 'round-readback-summary.json',
    'final-deliverables-inventory.csv', 'final-deliverables-summary.json',
    'verify-r117.log', 'verify-r117-initial.log', 'verify-r117-result.json',
    'commit-verification.json',
}


def read_csv(path):
    with path.open(encoding='utf8', newline='') as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields):
    with path.open('w', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def kind(path):
    return 'binary' if path.name == 'initial-untracked-pathspec.nul' else 'utf8'


# Enumerate metadata and persist the scope before opening the listed data.
paths = sorted(p for base in (S, R) for p in base.rglob('*')
               if p.is_file() and not (base == R and p.name in EXCLUDE))
for row in read_csv(R / 'final-deliverables-scope-before-read.csv'):
    p = ROOT / row['path']
    if p not in paths:
        paths.append(p)
paths = sorted(paths, key=lambda x: x.relative_to(ROOT).as_posix())
assert len(paths) == len(set(paths))
scoped = [{'path': p.relative_to(ROOT).as_posix(), 'listed_bytes': p.stat().st_size,
           'read_kind': kind(p)} for p in paths]
write_csv(R / 'round-readback-scope.csv', scoped, ['path', 'listed_bytes', 'read_kind'])

inventory = []
for row in scoped:
    p = ROOT / row['path']
    data = p.read_bytes()
    if len(data) != row['listed_bytes']:
        raise RuntimeError(f'changed size during read: {p}')
    if row['read_kind'] == 'utf8':
        data.decode('utf8')
    inventory.append({'path': row['path'], 'bytes_read': len(data),
                      'sha256': hashlib.sha256(data).hexdigest(), 'read_kind': row['read_kind']})
write_csv(R / 'round-readback-inventory.csv', inventory, ['path', 'bytes_read', 'sha256', 'read_kind'])
summary = {'listed_files': len(scoped), 'fully_read_files': len(inventory),
           'listed_bytes': sum(r['listed_bytes'] for r in scoped),
           'fully_read_bytes': sum(r['bytes_read'] for r in inventory),
           'utf8_decoded_files': sum(r['read_kind'] == 'utf8' for r in inventory),
           'binary_read_files': sum(r['read_kind'] == 'binary' for r in inventory),
           'created_after_scope': sorted(EXCLUDE),
           'observed_monotonic_seconds': time.monotonic(),
           'limit': 'Only prelisted local artifacts; not original web HTML, full internet or independent witnesses.'}
(R / 'round-readback-summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf8')

final = []
for row in read_csv(R / 'final-deliverables-scope-before-read.csv'):
    p = ROOT / row['path']
    b = p.read_bytes()
    b.decode('utf8')
    final.append({'id': row['id'], 'path': row['path'], 'bytes_read': len(b), 'sha256': hashlib.sha256(b).hexdigest()})
write_csv(R / 'final-deliverables-inventory.csv', final, ['id', 'path', 'bytes_read', 'sha256'])
(R / 'final-deliverables-summary.json').write_text(json.dumps({'listed_files': len(final),
    'fully_read_files': len(final), 'fully_read_bytes': sum(x['bytes_read'] for x in final),
    'observed_monotonic_seconds': time.monotonic()}, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
print('全量读取完成（本轮预列产物）：', len(inventory), '/', len(scoped), '路径，',
      summary['fully_read_bytes'], 'bytes；最终交付：', len(final), '/', len(final),
      '路径，', sum(x['bytes_read'] for x in final), 'bytes。', sep='')
