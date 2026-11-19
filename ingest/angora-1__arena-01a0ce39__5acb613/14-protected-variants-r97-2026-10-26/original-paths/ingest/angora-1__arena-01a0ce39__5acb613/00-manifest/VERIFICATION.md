# Verification report - full-repo ingest

- source: `SimonSaga-202306/Angora-1` branch `arena/01a0ce39-angora` commit `5acb6132a6a6090bfc777c324cfea6bc8dfb877a`
- git-tracked files: **781**
- ingest artifacts: **781** (1:1, nothing merged)
- source bytes: **787,973,154**
- artifact bytes: **41,513,083**
- artifact characters: **40,465,473**
- archive-member artifacts (layer 04): **72**
- total artifacts: **853** (781 primary + 72 archive members)
- result: **PASS**

| # | check | result | detail |
|---|---|---|---|
| 01 | tracked files in git == ingested files | PASS | 781 vs 781 |
| 02 | path sets identical (no skipped file, no invented file) | PASS | lists compared element-wise in sorted order |
| 03 | reading order == manifest order (no duplicates) | PASS | seq 1..N contiguous |
| 04 | every source file has an artifact on disk | PASS | 781/781 |
| 05 | artifact paths unique (nothing merged / overwritten) | PASS | 781 unique artifact paths |
| 06 | verbatim text copies are byte-identical to source (sha256 re-check) | PASS | 392 copies re-hashed, mismatches: none |
| 07 | source byte total matches manifest | PASS | 787973154 bytes |
| 08 | no empty artifact (nothing truncated to zero) | PASS | empty: none |
| 09 | every office/pdf file produced a text extraction | PASS | 178 extractions, statuses: ['ok'] |
| 10 | binary artifacts carry the exact sha256 + byte size of the original | PASS | 211 metadata artifacts |
| 11 | directory tree manifest lists every file basename | PASS | spot check on basenames without spaces |
| 12 | every directory level present in the tree manifest | PASS | 781 file lines vs 781 files; 57 directories, max depth 5 levels |
| 13 | archive members: every member has its own artifact (or a verified loose copy) | PASS | 86 members across 7 archives; unresolved: none |
| 14 | every member of every container is accounted for (recursively) | PASS | 7 containers reconciled |
| 15 | archive member totals consistent (nested members included) | PASS | 85 indexed member rows cover 62 direct container members + expanded nested members |
| 16 | legacy .doc decoded to real body text (>=100 CJK chars each) | PASS | 6 docs; bad: none |
| 17 | no document extraction collapsed to a stub (<300 chars) | PASS | stubs: none |
| 18 | total artifacts = 781 primary + archive-member layer | PASS | 781 + 72 = 853 |

## File count reconciliation

| source | count |
|---|---|
| `git ls-files` on `arena/01a0ce39-angora` | 781 |
| manifest rows | 781 |
| artifacts on disk | 781 |
| verbatim text artifacts | 392 |
| text-extraction artifacts | 178 |
| binary metadata artifacts | 211 |
| files with no artifact | 0 |
| archive-member artifacts (layer 04) | 72 |
| **total artifacts** | **853** |

