#!/usr/bin/env python3
"""Read only prelisted public vendor mirror files; record exact casefold matches."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
with (ROOT / 'scan-plan-before-read.csv').open(encoding='utf-8', newline='') as f:
    plan = list(csv.DictReader(f))
assert len(plan) == 5
result = []
for row in plan:
    path = ROOT / row['relative_path']
    raw = path.read_bytes()
    text = raw.decode('utf-8')
    lines = text.splitlines()
    needles = row['needles'].split(';')
    matches = []
    for n, line in enumerate(lines, 1):
        hit = [q for q in needles if q.casefold() in line.casefold()]
        if hit:
            matches.append({'line': n, 'needles': hit, 'text': line})
    result.append({
        'id': row['id'], 'path': row['relative_path'], 'bytes_read': len(raw),
        'sha256': hashlib.sha256(raw).hexdigest(), 'line_count': len(lines),
        'needles': needles, 'matches': matches,
    })
(ROOT / 'scan-full-file-exact-results.json').write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for row in result:
    print(row['id'], row['bytes_read'], 'bytes;', len(row['matches']), 'matching lines')
