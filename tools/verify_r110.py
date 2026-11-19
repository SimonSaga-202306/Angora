#!/usr/bin/env python3
"""Read-only checks for the r110 Angora research and safety artifacts.

No assertion here proves that a manual tool-visible transcription is faithful
to original HTML, that a vendor claim is true, or that recorded reads happened
in a given order.  Legacy PASS sections are hashed only, never displayed.
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
import re
from pathlib import Path
import subprocess
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
I = ROOT / 'ingest/angora-1__arena-01a0ce39__5acb613'
E = I / '65-source-evidence-r110-2026-10-26'
S = I / '64-entry-safety-r110-2026-10-26'
W = I / '01-text-verbatim/workstation'
R109 = '9df3405118c2e38ccc146d8447ab5bfddc787cc5'
STASH = '3e2d5571c79f113bdf8712561d42d32c9010395b'


def need(value, message):
    if not value:
        raise AssertionError(message)


def rel(path):
    return str(Path(path).relative_to(ROOT))


def local(path):
    candidate = (ROOT / path).resolve()
    need(candidate.is_relative_to(ROOT), f'outside workspace: {path}')
    return candidate


def read_csv(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def digest(data):
    return sha256(data).hexdigest()


def check_inventory(scope_name, inventory_name, path_key, expected_count, expected_bytes):
    scope = read_csv(E / scope_name)
    inv = read_csv(E / inventory_name)
    need(len(scope) == len(inv) == expected_count, f'count mismatch: {scope_name}')
    scoped = {r[path_key]: r for r in scope}
    observed = {r[path_key]: r for r in inv}
    need(len(scoped) == len(observed) == expected_count and scoped.keys() == observed.keys(),
         f'paths mismatch: {scope_name}')
    size = 0
    for name, row in observed.items():
        data = local(name).read_bytes()
        data.decode('utf-8')
        need(len(data) == int(scoped[name]['bytes_before_read']) == int(row['bytes_read']),
             f'byte count: {name}')
        need(digest(data) == row['sha256'], f'byte hash: {name}')
        size += len(data)
    need(size == expected_bytes, f'total bytes: {scope_name} {size}')
    return set(scoped), size


def verify_links(docs, allow_missing_summary):
    count = 0
    for doc in docs:
        text = doc.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
            target = target.split(' ', 1)[0]
            if not target or target.startswith(('#', 'http://', 'https://', 'mailto:')):
                continue
            target = unquote(target.split('#', 1)[0])
            candidate = (doc.parent / target).resolve()
            need(candidate.is_relative_to(ROOT), f'link outside repository: {doc} -> {target}')
            if allow_missing_summary and candidate == E / 'verification-summary.json':
                continue
            need(candidate.exists(), f'broken link: {rel(doc)} -> {target}')
            count += 1
    return count


def output_scope_paths():
    scope = read_csv(E / 'output-scope-before-hash.csv') + read_csv(E / 'output-scope-extension-before-hash.csv')
    paths = [r['repository_relative_path'] for r in scope]
    need(len(paths) == len(set(paths)), 'duplicate output scope path')
    return paths


def write_output_manifest():
    paths = output_scope_paths()
    self_path = rel(E / 'output-manifest-before-stage.csv')
    need(self_path in paths, 'manifest not listed in output scope')
    rows = []
    total = 0
    for path in sorted(paths):
        if path == self_path:
            rows.append({'repository_relative_path': path, 'byte_count': 'SELF', 'sha256': 'SELF',
                         'handling': 'self excluded to avoid circular hash'})
            continue
        data = local(path).read_bytes()
        total += len(data)
        rows.append({'repository_relative_path': path, 'byte_count': len(data), 'sha256': digest(data),
                     'handling': 'complete file bytes'})
    with (E / 'output-manifest-before-stage.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['repository_relative_path', 'byte_count', 'sha256', 'handling'], lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({'output_paths': len(rows), 'hashed_paths': len(rows) - 1, 'hashed_bytes': total}, indent=2))


def verify_output_manifest():
    scoped_paths = output_scope_paths()
    manifest = read_csv(E / 'output-manifest-before-stage.csv')
    rows = {r['repository_relative_path']: r for r in manifest}
    need(len(rows) == len(manifest) and set(rows) == set(scoped_paths), 'output manifest versus scope')
    self_path = rel(E / 'output-manifest-before-stage.csv')
    need(rows[self_path]['byte_count'] == rows[self_path]['sha256'] == 'SELF', 'manifest self-reference')
    total = 0
    for path, row in rows.items():
        if path == self_path:
            continue
        data = local(path).read_bytes()
        need(len(data) == int(row['byte_count']) and digest(data) == row['sha256'], f'output manifest changed: {path}')
        total += len(data)
    return len(rows), total


def negative_tests():
    def expect_failure(fn, name):
        try:
            fn()
        except AssertionError:
            return
        raise AssertionError(f'negative test unexpectedly passed: {name}')
    expect_failure(lambda: need(digest(b'changed') == digest(b'original'), 'hash changed'), 'hash')
    expect_failure(lambda: need('greater than 4.0' in '4.0 or above', 'version boundary changed'), 'boundary')
    expect_failure(lambda: need('target article visible' == 'toolbar and title only; article body absent', 'missing body'), 'body status')
    expect_failure(lambda: need(digest(b'bad prefix') == 'b15acbf6e543a6774c775ae2b48c7ce3ac9b45720b1ad0506ab39aa11085a40f', 'prefix altered'), 'prefix')
    return 4


def main(write_summary=False, check_output_manifest=False):
    need(not (write_summary and check_output_manifest), 'cannot write summary while checking its manifest hash')
    branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip()
    need(branch == 'arena/5da004bd-angora', 'unexpected branch')
    ancestor = subprocess.run(['git', 'merge-base', '--is-ancestor', R109, 'HEAD'], cwd=ROOT)
    need(ancestor.returncode == 0, 'r109 is not ancestor of current HEAD')

    scopes = [
        ('comparison-local-scope-before-read.csv', 'comparison-local-read-inventory.csv', 'repository_relative_path', 14, 100177),
        ('source-artifact-scope-before-read.csv', 'source-artifact-read-inventory.csv', 'repository_relative_path', 28, 130178),
        ('r109-inventory-comparison-scope-before-read.csv', 'r109-inventory-comparison-read.csv', 'path', 5, 12813),
        ('supplemental-cli-scope-before-read.csv', 'supplemental-cli-read-inventory.csv', 'repository_relative_path', 1, 15349),
    ]
    allpaths = set()
    groups = []
    for s, v, k, count, size in scopes:
        paths, actual = check_inventory(s, v, k, count, size)
        need(not (allpaths & paths), f'overlapping inventory groups: {s}')
        allpaths |= paths
        groups.append({'scope': s, 'count': len(paths), 'bytes': actual})
    need(len(allpaths) == 48 and sum(g['bytes'] for g in groups) == 258517, '48-path inventory total')
    source_paths = set(r['repository_relative_path'] for r in read_csv(E / 'source-artifact-read-inventory.csv'))
    source_paths |= set(r['repository_relative_path'] for r in read_csv(E / 'supplemental-cli-read-inventory.csv'))

    catalog = read_csv(E / 'source-catalog.csv')
    need(len(catalog) == 29, 'source catalog count')
    byid = {r['source_id']: r for r in catalog}
    need(len(byid) == len(catalog), 'duplicate source IDs')
    need({r['artifact_path'] for r in catalog} == source_paths, 'catalog versus source scopes')
    expected_types = {'direct_transcription': 7, 'reconstructed_from_AR01': 1,
                      'reconstructed_from_AR05': 1, 'quarantined': 2,
                      'quarantined_error_transcription': 5,
                      'cdx_index_transcription': 9, 'github_search_metadata': 4}
    need(Counter(r['record_type'] for r in catalog) == Counter(expected_types), 'artifact evidence grades')
    for r in catalog:
        data = local(r['artifact_path']).read_bytes()
        need(len(data) == int(r['bytes']) and digest(data) == r['sha256'], f'catalog hash {r["source_id"]}')

    replays = read_csv(E / 'archive-replay-results.csv')
    need(len(replays) == 11 and sum(int(r['tool_chunks']) for r in replays) == 20, 'replay block count')
    need(sum(r['record_type'] == 'direct_transcription' for r in replays) == 7, 'direct replay count')
    need(sum(r['record_type'].startswith('reconstructed') for r in replays) == 2, 'reconstructed replay count')
    need(sum(r['record_type'] == 'quarantined' for r in replays) == 2, 'quarantined replay count')
    plans = (read_csv(E / 'archive-replay-plan-before-fetch.csv')
             + read_csv(E / 'archive-replay-extension-plan-before-fetch.csv')
             + read_csv(E / 'archive-replay-cli-plan-before-fetch.csv'))
    plan_by_id = {r['source_id']: r for r in plans}
    need(len(plan_by_id) == 11 and set(plan_by_id) == {r['source_id'] for r in replays}, 'replay plan coverage')
    index_record_count = 0
    indexes = {}
    for r in catalog:
        if r['record_type'] != 'cdx_index_transcription':
            continue
        text = local(r['artifact_path']).read_text(encoding='utf-8')
        need(text.startswith('```json\n') and text.endswith('```'), f'CDX envelope {r["source_id"]}')
        table = json.loads(text[8:-3].strip())
        need(table[0] == ['timestamp', 'original', 'statuscode', 'digest', 'length'], 'CDX columns')
        query = parse_qs(urlsplit(r['retrieval_url']).query)
        original_url = urlsplit(r['original_or_query_url'])
        expected_query_url = original_url.netloc + original_url.path + ('?' + original_url.query if original_url.query else '')
        need(query.get('to') == ['20261026'] and query.get('url') == [expected_query_url], 'CDX cutoff or query URL')
        for row in table[1:]:
            need(row[0].isdigit() and len(row[0]) == 14 and row[0][:8] <= '20261026' and row[2] == '200', 'CDX filter')
            need(row[1] == r['original_or_query_url'], f'CDX original URL mismatch {r["source_id"]}')
            need((row[1], row[0]) not in indexes, 'duplicate CDX URL/timestamp')
            indexes[(row[1], row[0])] = (row[3], row[4])
            index_record_count += 1
    need(index_record_count == 35, 'CDX row count')
    need(len({r['source_id'] for r in replays}) == 11, 'duplicate replay IDs')
    for r in replays:
        p = plan_by_id[r['source_id']]
        catalog_row = byid[r['source_id']]
        for key in catalog_row:
            need(r[key] == catalog_row[key], f'replay/catalog mismatch {r["source_id"]}: {key}')
        need(r['capture_or_result'] == p['capture_timestamp_utc'], 'replay capture mismatch')
        need(r['original_or_query_url'] == p['original_url'] and r['retrieval_url'] == p['archive_replay_url'], 'replay URL mismatch')
        need((r['cdx_digest'], r['cdx_length_field']) == (p['cdx_digest'], p['cdx_length_field'])
             == indexes[(p['original_url'], p['capture_timestamp_utc'])], 'replay not listed in planned CDX')
        body = local(r['artifact_path']).read_text(encoding='utf-8')
        need(r['retrieval_url'] in body, f'replay URL absent from saved wrapper {r["source_id"]}')
        if r['record_type'] == 'direct_transcription':
            need('# Knowledge Base' in body and body.endswith('Save my name, email, and website in this browser for the next time I comment.'), f'incomplete visible wrapper {r["source_id"]}')
    need('# Knowledge Base' not in local(byid['AR04']['artifact_path']).read_text(encoding='utf-8'), 'AR04 body unexpectedly classified')
    need('BERLINAVTO.COM.UA' in local(byid['AR07']['artifact_path']).read_text(encoding='utf-8'), 'AR07 wrong-page marker missing')
    for i in range(1, 6):
        r = byid[f'KB{i:02}']
        need('522' in r['status'] and 'the web page can not be displayed' in local(r['artifact_path']).read_text(encoding='utf-8'), '522 classification')
    for i in range(1, 5):
        obj = json.loads(local(byid[f'GH{i:02}']['artifact_path']).read_text(encoding='utf-8'))
        need(obj['total_count'] == 0 and obj['incomplete_results'] is False, 'GitHub search result')

    traces = read_csv(E / 'evidence-traceability.csv')
    need(len(traces) == 45 and len({r['anchor_id'] for r in traces}) == 45, 'anchor count or uniqueness')
    anchors = {r['anchor_id']: r for r in traces}
    direct_ids = {r['source_id'] for r in catalog if r['record_type'] == 'direct_transcription'}
    used_ids = set()
    for r in traces:
        need(r['source_id'] in direct_ids and r['source_path'] == byid[r['source_id']]['artifact_path'], f'anchor source {r["anchor_id"]}')
        lines = local(r['source_path']).read_text(encoding='utf-8').splitlines()
        start, end = int(r['start_line_1based']), int(r['end_line_1based'])
        need(1 <= start <= end <= len(lines), 'anchor range')
        quote = '\n'.join(lines[start - 1:end])
        need(quote == r['quote_exact_from_saved_transcription'] and digest(quote.encode('utf-8')) == r['quote_sha256_utf8'], f'anchor changed {r["anchor_id"]}')
        used_ids.add(r['source_id'])
    need(used_ids == direct_ids, 'not all direct sources have anchors')
    for filename, expected_count in [('claim-boundaries.csv', 19), ('issues-and-corrections.csv', 12), ('cross-language-comparison.csv', 4)]:
        rows = read_csv(E / filename)
        need(len(rows) == expected_count, f'row count {filename}')
        for r in rows:
            for anchor in filter(None, r.get('anchor_ids', '').split(';')):
                need(anchor in anchors, f'unknown anchor {anchor} in {filename}')
    need('greater than 4.0' in anchors['AUTH-EN-V']['quote_exact_from_saved_transcription'], 'English version boundary')
    need('4.0 versiyonu ve üzerini' in anchors['AUTH-TR-V']['quote_exact_from_saved_transcription'], 'Turkish version boundary')
    need('/0/' in anchors['CLI-TEMPLATE']['quote_exact_from_saved_transcription'], 'CLI template')
    need('1/1/1' in anchors['CLI-EXAMPLE1']['quote_exact_from_saved_transcription'] and '1/2/1' in anchors['CLI-EXAMPLE2']['quote_exact_from_saved_transcription'], 'CLI examples')

    discovery_originals = {
        'discovery-metadata.csv': (32, '60ae4759f747f0f20739daf5b500fc815eed87241de7a3535be30e080bb4cb3a'),
        'upgrade-discovery-metadata.csv': (7, '6d285e57a05e37b9dc46c67240c61d3b19b22fc5bd2523817c81a40a9a91d7cd'),
        'archive-discovery-metadata.csv': (7, 'f32b1139b8f09ea1df222c322870cc899b9b44a8f5269388c069a08af6aed9b3'),
    }
    discovery_rows = 0
    for name, (expected, prior_hash) in discovery_originals.items():
        original = E / 'metadata-attribution-originals' / name
        need(digest(original.read_bytes()) == prior_hash, f'discovery original hash {name}')
        before = read_csv(original)
        after = read_csv(E / name)
        need(len(before) == len(after) == expected, f'discovery row count {name}')
        for old_row, new_row in zip(before, after):
            warning = new_row.pop('query_attribution_status', '')
            need(warning.startswith('UNVERIFIED') and old_row == new_row, f'discovery attribution warning or changed fields {name}')
        discovery_rows += len(after)
    need(discovery_rows == 46, 'discovery metadata row count')

    comparison = read_csv(E / 'r109-r110-local-path-comparison.csv')
    need(sum(r['in_r109_local_49'] == 'True' for r in comparison) == 49, 'r109 count')
    need(sum(r['in_r110_prior_14'] == 'True' for r in comparison) == 14, 'r110 prior count')
    need(sum(r['in_r109_local_49'] == r['in_r110_prior_14'] == 'True' for r in comparison) == 4, 'overlap count')

    variant_rows = read_csv(S / 'variant-protection-verification.csv')
    need(len(variant_rows) == 32, 'variant count')
    variant_bytes = 0
    for r in variant_rows:
        b = local(r['prior_r109_protected_path']).read_bytes()
        need(len(b) == int(r['bytes']) and digest(b) == r['sha256'], 'protected variant hash')
        need(r['exact_prior_r109_protection'] == 'True' and r['worktree_blob_sha1'] == r['prior_r109_protected_blob_sha1'], 'protected variant identity')
        variant_bytes += len(b)
    need(variant_bytes == 17473261, 'protected variant bytes')
    stash_rows = read_csv(S / 'stash-untracked-tree-verification.csv')
    need(len(stash_rows) == 868 and all(r['exact_blob_equal'] == 'True' and r['pre_stash_blob_sha1'] == r['stash_blob_sha1'] for r in stash_rows), 'stash verification records')
    have_stash = subprocess.run(['git', 'cat-file', '-e', STASH + '^3'], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    if have_stash:
        raw = subprocess.check_output(['git', 'ls-tree', '-r', '-z', STASH + '^3'], cwd=ROOT)
        actual = {}
        for e in raw.split(b'\0'):
            if e:
                metadata, name = e.split(b'\t', 1)
                actual[name.decode('utf-8')] = metadata.split()[2].decode('ascii')
        need(actual == {r['repository_relative_path']: r['stash_blob_sha1'] for r in stash_rows}, 'actual stash tree')

    append = read_csv(E / 'append-log.csv')
    need(len(append) == 1, 'append log count')
    a = append[0]
    old = local(a['repository_relative_path']).read_bytes()
    addition = local(a['append_source_path']).read_bytes()
    prefix_len = int(a['preappend_bytes'])
    need(prefix_len == 48365 and digest(old[:prefix_len]) == a['preappend_sha256'] == a['prefix_sha256_after'], 'legacy dossier prefix')
    need(old[prefix_len:] == addition and digest(addition) == a['append_sha256'], 'append contents')
    need(len(old) == int(a['postappend_bytes']) and digest(old) == a['postappend_sha256'], 'postappend hash')
    append_links = 0
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', addition.decode('utf-8')):
        candidate = (local(a['repository_relative_path']).parent / unquote(target)).resolve()
        need(candidate.is_relative_to(ROOT) and candidate.exists(), f'broken appended link: {target}')
        append_links += 1
    history = read_csv(S / 'historical-append-read-inventory.csv')
    need(len(history) == 9, 'historical chain count')
    for r in history:
        data = local(r['repository_relative_path']).read_bytes()
        if r['repository_relative_path'] == a['repository_relative_path']:
            data = data[:prefix_len]
        need(len(data) == int(r['bytes_read']) and digest(data) == r['sha256'], 'historical chain hash')

    baseline = json.loads((S / 'baseline.json').read_text(encoding='utf-8'))
    need(baseline['session_date_supplied_utc'] == '2026-10-26' and baseline['environment_initial_observed_utc'].startswith('2026-11-19'), 'date caveat')
    report = W / '08-customer-pipeline/179-angora-software-support-archive-r110-2026-10-26.md'
    appendix = W / '09-orders/120-angora-orders-dossier-2026-10-21.r110-appendix.md'
    mapping = W / '09-orders/120-angora-orders-master-2026-10-21.mapping-r110.md'
    follow = I / '66-followup-angora-r110-2026-10-26/angora-networks.md'
    docs = [report, appendix, mapping, follow, E / 'README.md', I / '67-audit-r110-2026-10-26.md',
            S / 'README.md', E / 'discovery-attribution-correction.md',
            E / 'local-scope-deviation-D04.md', E / 'local-scope-deviation-D05.md']
    for p in (report, appendix, mapping):
        text = p.read_text(encoding='utf-8')
        need('r105–r109' in text and '2026-10-26' in text and '2026-11-19' in text, f'date qualifier missing {p}')
        need('r109' in text and 'r101' in text and 'r105' in text, f'prior comparison missing {p}')
        need('local-scope-deviation-D05.md' in text, f'mixed old-report scope disclosure missing {p}')
        need('discovery-attribution-correction.md' in text, f'discovery attribution disclosure missing {p}')
    for p in (E / 'README.md', I / '67-audit-r110-2026-10-26.md'):
        text = p.read_text(encoding='utf-8')
        need('local-scope-deviation-D05.md' in text and '十二项具名' in text, f'final disclosure/count missing {p}')
        need('discovery-attribution-correction.md' in text, f'discovery attribution disclosure missing {p}')
    need(len(list(follow.parent.glob('*.md'))) == 1, 'follow-up contains multiple subjects')
    links = verify_links(docs, allow_missing_summary=write_summary) + append_links
    negatives = negative_tests()
    output_check = verify_output_manifest() if check_output_manifest else None

    result = {
        'status': 'PASS',
        'scope_groups': groups,
        'distinct_paths_fully_read': len(allpaths),
        'scoped_bytes': sum(g['bytes'] for g in groups),
        'catalog_artifacts': len(catalog),
        'archive_replays': len(replays),
        'archive_tool_blocks': 20,
        'direct_transcriptions': len(direct_ids),
        'reconstructed_replays': 2,
        'quarantined_replays': 2,
        'cdx_filtered_digest_records': index_record_count,
        'evidence_anchors': len(traces),
        'discovery_metadata_rows_with_unverified_query_attribution': discovery_rows,
        'discovery_original_metadata_copies_verified': len(discovery_originals),
        'issue_records': 12,
        'cdx_query_cutoff_utc': '2026-10-26',
        'r109_path_overlap': 4,
        'protected_variants': len(variant_rows),
        'protected_variant_bytes': variant_bytes,
        'stash_recorded_blobs': len(stash_rows),
        'stash_tree_checked_in_this_clone': have_stash,
        'legacy_prefix_bytes': prefix_len,
        'historical_append_chains_verified': len(history),
        'local_links_checked': links,
        'output_manifest_checked_this_run': check_output_manifest,
        'output_manifest_paths_and_bytes': output_check,
        'negative_tests': negatives,
        'environment_clock_observation_utc': datetime.now(timezone.utc).isoformat(),
        'session_date_supplied_utc': '2026-10-26',
        'verifier_sha256': digest(Path(__file__).read_bytes()),
        'limitations': 'Manual tool-visible transcriptions and reconstructions are not automatically byte-compared to tool responses or original HTML; parallel search query attribution remains unverified; no device test, temporal provenance, independent certification or service delivery is established.',
    }
    if write_summary:
        (E / 'verification-summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-summary', action='store_true')
    parser.add_argument('--check-output-manifest', action='store_true')
    parser.add_argument('--write-output-manifest', action='store_true')
    args = parser.parse_args()
    if args.write_output_manifest:
        need(not (args.write_summary or args.check_output_manifest), 'manifest writing is a separate phase')
        write_output_manifest()
    else:
        main(args.write_summary, args.check_output_manifest)
