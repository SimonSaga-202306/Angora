#!/usr/bin/env python3
"""Verify bounded r104 records without network, old verifiers, or archive extraction.

This checks saved representations, not the truth of vendor claims, PDF/HTML origin
bytes, independent tests, customer deployment, or the actual wall-clock date.
Quarantined PDF-derived files are read only as bytes for integrity accounting.
"""
from __future__ import annotations

import csv
import hashlib
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
INGEST = ROOT / 'ingest/angora-1__arena-01a0ce39__5acb613'
SOURCE = INGEST / '41-source-evidence-r104-2026-10-26'
SAFETY = INGEST / '40-entry-safety-r104-2026-10-26'
W = INGEST / '01-text-verbatim/workstation'


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def absolute(path: str) -> Path:
    result = (ROOT / path).resolve()
    require(result.is_relative_to(ROOT), 'path outside repository')
    return result


def check_inventory(name: str, prefix: bool = False) -> int:
    inventory = rows(SOURCE / name)
    for record in inventory:
        path = absolute(record['repository_relative_path'])
        data = path.read_bytes()
        length = int(record['bytes'])
        saved = data[:length] if prefix else data
        require(len(saved) == length, f'{name}: byte length')
        require(prefix or len(data) == length, f'{name}: entire length')
        require(sha(saved) == record['sha256'], f'{name}: SHA-256')
    return len(inventory)


def valid_chunks(segments: list[dict[str, str]], total: int) -> bool:
    try:
        segments = sorted(segments, key=lambda r: int(r['chunk']))
        cursor = 0
        for number, r in enumerate(segments):
            if int(r['chunk']) != number or int(r['saved_start_byte']) != cursor:
                return False
            end = int(r['saved_end_byte_exclusive'])
            if end <= cursor or int(r['bytes']) != end - cursor:
                return False
            cursor = end
        return bool(segments) and cursor == total
    except (KeyError, TypeError, ValueError):
        return False


def valid_web_policy(records: list[dict[str, str]]) -> bool:
    if len(records) != 14 or len({r['url'] for r in records}) != 14:
        return False
    for r in records:
        pdf = '/download/' in r['url']
        if pdf != r['eligibility'].startswith('excluded: PDF PASS'):
            return False
        if not pdf and r['eligibility'] != 'manufacturer webpage (claim only)':
            return False
    return True


def parse_tsv(path: Path) -> dict[str, tuple[int, list[str], str]]:
    result = {}
    for number, line in enumerate(path.read_text(encoding='utf-8').split('\n'), 1):
        if not line or line.startswith('#') or line.startswith('id\t'):
            continue
        cells = line.split('\t')
        require(len(cells) >= 4 and cells[0].isdigit(), 'invalid saved TSV row')
        require(cells[0] not in result, 'duplicate saved TSV ID')
        result[cells[0]] = (number, cells, line)
    return result


def git_attributes(paths: list[Path], attribute: str, expected: str) -> None:
    rel = [str(p.relative_to(ROOT)) for p in paths]
    data = subprocess.check_output(
        ['git', 'check-attr', '-z', attribute, '--', *rel], cwd=ROOT
    ).split(b'\0')
    require(data[-1] == b'', 'git check-attr framing')
    values = data[:-1]
    require(len(values) == 3 * len(paths), 'git check-attr count')
    for index in range(len(paths)):
        name, attr, value = values[3 * index:3 * index + 3]
        require(name.decode() == rel[index], 'git check-attr path')
        require(attr.decode() == attribute and value.decode() == expected,
                f'git attribute {attribute} not {expected}')


def local_links(paths: list[Path]) -> int:
    count = 0
    for path in paths:
        content = path.read_text(encoding='utf-8')
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', content):
            target = target.strip()
            if target.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            name = unquote(urlsplit(target).path)
            if not name:
                continue
            resolved = (path.parent / name).resolve()
            require(resolved.is_relative_to(ROOT) and resolved.exists(),
                    f'broken local link in {path.name}: {target}')
            count += 1
    return count


def main() -> None:
    # Entry ledger: no output of historical file contents or sensitive paths.
    before = rows(SAFETY / 'entry-scope-before-comparison.csv')
    compared = rows(SAFETY / 'entry-comparison.csv')
    require(len(before) == len(compared) == 868, 'entry ledger size')
    require(Counter(r['comparison_to_remote'] for r in compared)
            == {'same': 837, 'different': 31}, 'entry ledger classes')
    require(sum(int(r['size_bytes']) for r in before) == 46_015_150,
            'entry scope byte total')
    for a, b in zip(before, compared):
        require(a['seq'] == b['seq'] and a['path_from_repo_root'] == b['path_from_repo_root'],
                'entry ledger ordering')
        require(a['size_bytes'] == b['bytes'], 'entry ledger lengths')
        if b['comparison_to_remote'] == 'different':
            protected = absolute(b['existing_protected_variant_path']).read_bytes()
            require(len(protected) == int(b['bytes']) and sha(protected) == b['incoming_sha256'],
                    'protected entry variant')
    require(sum(int(r['bytes']) for r in compared if r['comparison_to_remote'] == 'different')
            == 17_455_599, 'protected-variant byte total')
    print('entry ledger: 868 rows; 837 same; 31/31 protected variants (17,455,599 bytes) verified')

    inventories = [
        ('local-product-read-inventory.csv', 10, False),
        ('local-method-read-inventory.csv', 2, False),
        ('date-audit-read-inventory.csv', 9, False),
        ('context-prefix-read-inventory.csv', 7, True),
    ]
    for name, count, prefix in inventories:
        require(check_inventory(name, prefix) == count, f'{name}: row count')
    scope_pairs = [
        ('local-product-scope-before-read.csv', 'local-product-read-inventory.csv'),
        ('local-method-scope-before-read.csv', 'local-method-read-inventory.csv'),
        ('date-audit-scope-before-read.csv', 'date-audit-read-inventory.csv'),
        ('context-scope-before-read.csv', 'context-prefix-read-inventory.csv'),
    ]
    for scope_name, inventory_name in scope_pairs:
        listed, read = rows(SOURCE / scope_name), rows(SOURCE / inventory_name)
        require([(r['repository_relative_path'], r['bytes']) for r in listed]
                == [(r['repository_relative_path'], r['bytes']) for r in read],
                f'{scope_name}: scope/inventory mismatch')
    all_paths = [r['repository_relative_path'] for name, _, _ in inventories
                 for r in rows(SOURCE / name)]
    require(len(set(all_paths)) == 28, 'local groups must be distinct')
    require(sum(int(r['bytes']) for name, _, _ in inventories for r in rows(SOURCE / name))
            == 304_511, 'local byte total')
    additional = rows(SOURCE / 'overlap-check-inputs-after-first-read.csv')
    require(check_inventory('overlap-check-inputs-after-first-read.csv') == 7
            and sum(int(r['bytes']) for r in additional) == 12_932, 'overlap-inputs inventory')
    require(all('preceded this ledger' in r['read_order'] for r in additional),
            'overlap-input ordering disclosure')
    require(len(set(all_paths + [r['repository_relative_path'] for r in additional])) == 35,
            'all local paths must be distinct')
    date_scope = rows(SOURCE / 'date-audit-scope-before-read.csv')
    require(len(date_scope) == 9 and all('read before' in r['read_order'] for r in date_scope[:3])
            and all(r['read_order'] == 'listed before reading' for r in date_scope[3:]),
            'date-scope ordering disclosure')
    for r in rows(SOURCE / 'date-claims-index.csv'):
        line = absolute(r['path']).read_text(encoding='utf-8').split('\n')[int(r['line']) - 1]
        require(line == r['text'] and sha(line.encode()) == r['line_sha256'], 'date line')
    for r in rows(SOURCE / 'append-log.csv'):
        data = absolute(r['repository_relative_path']).read_bytes()
        n = int(r['prefix_bytes'])
        require(sha(data[:n]) == r['prefix_sha256'] and len(data[n:]) == int(r['appended_bytes'])
                and sha(data[n:]) == r['appended_sha256'] and len(data) == int(r['new_bytes'])
                and sha(data) == r['new_sha256'], 'append-only log')
    require(len(rows(SOURCE / 'append-log.csv')) == 6, 'append-only log count')
    ingest_rel = INGEST.relative_to(ROOT)
    local = {str(Path(r['repository_relative_path']).relative_to(ingest_rel))
             for r in rows(SOURCE / 'local-product-read-inventory.csv')}
    old103 = {r['path_from_ingest_root'] for name in ('source-read-inventory.csv',
               'supplement-read-inventory.csv') for r in rows(INGEST / '37-source-evidence-r103-2026-10-26' / name)}
    old102 = {r['path_from_ingest_root'] for p in (INGEST / '33-source-evidence-r102-2026-10-26').glob('*read-inventory.csv')
              if not p.name.startswith('context-') for r in rows(p) if 'path_from_ingest_root' in r}
    overlap = rows(SOURCE / 'overlap-r102-r103-by-path.csv')
    require(len(local) == 10 and len(old103) == 16 and len(old102) == 29
            and not (local & old103) and not (local & old102), 'historical path-set overlap')
    require({r['path_from_ingest_root'] for r in overlap} == local and len(overlap) == 10,
            'overlap index path set')
    for r in overlap:
        path = r['path_from_ingest_root']
        require(r['in_r103_16'] == str(path in old103) and r['in_r102_29'] == str(path in old102),
                'overlap index flags')
    print('local: 35/35 paths (317,443 bytes); 7 intact prefixes; 6 append logs; 10/10 overlaps checked')

    # Each URL remains a distinct artifact; PDF-derived artifacts remain quarantined.
    scopes = [rows(SOURCE / name) for name in (
        'web-initial-scope-before-fetch.csv', 'web-supplement-scope-before-fetch.csv',
        'web-second-supplement-scope-before-fetch.csv')]
    require([len(s) for s in scopes] == [3, 8, 3], 'URL scope counts')
    web = rows(SOURCE / 'web-visible-inventory.csv')
    require(valid_web_policy(web), 'web scope or PDF quarantine')
    require({r['url'] for r in web} == {r['url'] for scope in scopes for r in scope},
            'URL scope mismatch')
    planned = {r['url']: str((SOURCE / r['planned_path_from_r104_source_dir']).relative_to(ROOT))
               for scope in scopes for r in scope}
    require(all(r['repository_relative_path'] == planned[r['url']] and r['fetch_status'] == 'success'
                and r['returned_chunk_ids'] == ','.join(map(str, range(int(r['total_chunks']))))
                for r in web), 'web planned paths or returned chunks')
    require(sum(int(r['bytes']) for r in web) == 89_981, 'web byte total')
    chunks = rows(SOURCE / 'web-chunk-inventory.csv')
    by_url = defaultdict(list)
    for chunk in chunks:
        by_url[chunk['url']].append(chunk)
    require(len(chunks) == 16 and set(by_url) == {r['url'] for r in web}, 'chunk scope')
    for r in web:
        data = absolute(r['repository_relative_path']).read_bytes()
        require(len(data) == int(r['bytes']) and sha(data) == r['sha256'], 'web local hash')
        group = by_url[r['url']]
        require(valid_chunks(group, len(data)) and len(group) == int(r['total_chunks']),
                'chunk coverage')
        for chunk in group:
            a, b = int(chunk['saved_start_byte']), int(chunk['saved_end_byte_exclusive'])
            require(sha(data[a:b]) == chunk['sha256_saved_slice'], 'chunk hash')
    allowed = [r for r in web if not r['eligibility'].startswith('excluded:')]
    excluded = [r for r in web if r['eligibility'].startswith('excluded:')]
    require((len(allowed), sum(int(r['total_chunks']) for r in allowed),
             sum(int(r['bytes']) for r in allowed)) == (10, 11, 65_130), 'eligible web counts')
    require((len(excluded), sum(int(r['total_chunks']) for r in excluded),
             sum(int(r['bytes']) for r in excluded)) == (4, 5, 24_851), 'quarantine counts')
    for r in rows(SOURCE / 'search-result-inventory.csv'):
        data = absolute(r['repository_relative_path']).read_bytes()
        require(len(data) == int(r['bytes']) and sha(data) == r['sha256'], 'search snippet hash')
    print('web: 14 URL artifacts / 16 chunks; 10 HTML eligible, 4 PDF artifacts quarantined')

    anchors = rows(SOURCE / 'evidence-traceability.csv')
    require(len(anchors) == 44 and len({r['claim_id'] for r in anchors}) == 44, 'anchor count')
    require(not ({r['repository_relative_path'] for r in anchors}
                 & {r['repository_relative_path'] for r in excluded}), 'quarantined PDF in evidence anchors')
    for r in anchors:
        data = absolute(r['repository_relative_path']).read_bytes()[:int(r['bytes_bound'])]
        require(len(data) == int(r['bytes_bound']) and sha(data) == r['sha256'], 'anchor hash')
        line = data.decode('utf-8').split('\n')[int(r['line']) - 1]
        require(r['anchor'] in line, f"anchor {r['claim_id']}")
    known = {r['claim_id'] for r in anchors}
    for table, column, expected in [('protocol-capability-matrix.csv', 'anchors', 11),
                                    ('publication-dates.csv', 'anchors', 4)]:
        table_rows = rows(SOURCE / table)
        require(len(table_rows) == expected, f'{table} count')
        for r in table_rows:
            require(all(key in known for key in r[column].split('|')), f'{table} references')
    corrections = rows(SOURCE / 'issues-and-corrections.csv')
    require(len(corrections) == 10, 'corrections count')
    for r in corrections:
        for key in r['basis'].split('|'):
            require(key in known or (SOURCE / key).is_file(), 'correction basis')
    print('traceability: 44/44 anchored observations, 11 protocol rows, 4 date rows, 10 corrections')

    # Compare only stored historical TSV values, not live CMS state.
    p1 = INGEST / '06-web-crawl-2026-10-27/angora/api/wp-api-posts.tsv'
    p2 = INGEST / '07-web-crawl-2026-11-01/angora/api/wp-api-posts-2026-11-01.tsv'
    q1 = INGEST / '06-web-crawl-2026-10-27/angora/api/wp-api-pages.tsv'
    q2 = INGEST / '07-web-crawl-2026-11-01/angora/api/wp-api-pages-2026-11-01.tsv'
    A, B, C, E = [parse_tsv(p) for p in (p1, p2, q1, q2)]
    require(len(A) == len(B) == 10 and set(A) == set(B), 'old post rows')
    require(len(C) == len(E) == 25 and set(C) == set(E), 'old page rows')
    require(all(A[i][1][1:3] == B[i][1][1:3] for i in A), 'post datetime comparison')
    require({i for i in A if A[i][1][3] != B[i][1][3]} == {'777', '803'}, 'post slug comparison')
    require(all(C[i][1][1:3] == E[i][1][1:3] and C[i][1][-1] == E[i][1][-1] for i in C),
            'page field comparison')
    post_index = rows(SOURCE / 'wordpress-posts-compare.csv')
    page_index = rows(SOURCE / 'wordpress-pages-compare.csv')
    require(len(post_index) == len(A) and {r['id'] for r in post_index} == set(A)
            and len(page_index) == len(C) and {r['id'] for r in page_index} == set(C),
            'comparison ID set or duplicates')
    for r in post_index:
        i = r['id']; a, b = A[i], B[i]
        require(int(r['old_1027_row']) == a[0] and int(r['old_1101_row']) == b[0], 'post positions')
        require(r['old_1027_date'] == a[1][1] and r['old_1101_date'] == b[1][1]
                and r['old_1027_modified'] == a[1][2] and r['old_1101_modified'] == b[1][2]
                and r['old_1027_slug'] == a[1][3] and r['old_1101_slug'] == b[1][3], 'post fields')
        require(r['same_datetime_fields'] == str(a[1][1:3] == b[1][1:3])
                and r['same_slug'] == str(a[1][3] == b[1][3]), 'post flags')
        require(r['old_1027_row_sha256'] == sha(a[2].encode())
                and r['old_1101_row_sha256'] == sha(b[2].encode()), 'post row hash')
    for r in page_index:
        i = r['id']; a, b = C[i], E[i]
        require(int(r['old_1027_row']) == a[0] and int(r['old_1101_row']) == b[0], 'page positions')
        require(r['same_date_modified'] == str(a[1][1:3] == b[1][1:3])
                and r['same_url'] == str(a[1][-1] == b[1][-1]), 'page flags')
        require(r['old_1027_row_sha256'] == sha(a[2].encode())
                and r['old_1101_row_sha256'] == sha(b[2].encode()), 'page row hash')
    require(len(rows(SOURCE / 'wordpress-posts-compare.csv')) == 10
            and len(rows(SOURCE / 'wordpress-pages-compare.csv')) == 25, 'comparison row counts')
    print('historical TSV: 25/25 pages; 10/10 posts; 10 date pairs match and 2 slugs differ')

    # Existing source blobs and all new records should retain exact stored bytes.
    for p in (p1, p2, q1, q2):
        git_bytes = subprocess.check_output(['git', 'show', 'HEAD:' + str(p.relative_to(ROOT))], cwd=ROOT)
        require(git_bytes == p.read_bytes(), 'historical TSV differs from HEAD blob')
    recorded = sorted(p for root in (SOURCE, SAFETY) for p in root.rglob('*') if p.is_file())
    git_attributes(recorded + [p1, p2, q1, q2], 'text', 'unset')
    git_attributes([absolute(r['repository_relative_path']) for r in excluded], 'diff', 'unset')
    print(f'Git bytes/attributes: 4/4 old TSV blobs equal; {len(recorded)} records and 4 TSV -text; 4 PDF -diff')

    report = W / '08-customer-pipeline/173-angora-security-products-protocols-r104-2026-10-26.md'
    mapping = W / '09-orders/120-angora-orders-master-2026-10-21.mapping-r104.md'
    internal = INGEST / '42-followup-angora-r104-2026-10-26/angora-networks.md'
    audit = INGEST / '43-audit-r104-2026-10-26.md'
    link_count = local_links([report, mapping, internal, SOURCE / 'README.md', SAFETY / 'README.md', audit])
    print(f'local links: {link_count} resolve')

    # Memory-only negative checks; do not change sources or run prior verifiers.
    sample = b'check'
    require(sha(sample + b'!') != sha(sample), 'negative: changed bytes')
    require(not valid_chunks([], 5), 'negative: empty chunk list')
    require(not valid_chunks([{'chunk':'0', 'saved_start_byte':'1',
                              'saved_end_byte_exclusive':'5', 'bytes':'4'}], 5), 'negative: gap')
    require(not valid_chunks([{'chunk':'0', 'saved_start_byte':'0',
                              'saved_end_byte_exclusive':'6', 'bytes':'6'}], 5), 'negative: overflow')
    bad = [dict(r) for r in web]; bad[0]['url'] = bad[1]['url']
    require(not valid_web_policy(bad), 'negative: duplicate URL')
    bad = [dict(r) for r in web]
    next(r for r in bad if '/download/' in r['url'])['eligibility'] = 'manufacturer webpage (claim only)'
    require(not valid_web_policy(bad), 'negative: PDF quarantine removed')
    require('nonexistent-claim' not in known, 'negative: missing anchor')
    print('negative checks: 7/7 in memory')
    print('PASS: r104 integrity checks only; no inference of product tests, deployments or original PDF/HTML')


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, OSError, UnicodeError, subprocess.CalledProcessError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        raise SystemExit(1)
