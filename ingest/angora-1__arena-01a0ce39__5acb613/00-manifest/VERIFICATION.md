# Verification report - full-repo ingest

- source: `SimonSaga-202306/Angora-1` branch `arena/01a0ce39-angora` commit `5acb6132a6a6090bfc777c324cfea6bc8dfb877a`
- git-tracked files: **781**
- ingest artifacts: **781** (1:1, nothing merged)
- source bytes: **787,973,154**
- artifact bytes: **41,323,127**
- artifact characters: **40,290,238**
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
| 09 | every office/pdf file produced a text extraction | PASS | 176 extractions, statuses: ['ok'] |
| 10 | binary artifacts carry the exact sha256 + byte size of the original | PASS | 213 metadata artifacts |
| 11 | directory tree manifest lists every file basename | PASS | spot check on basenames without spaces |
| 12 | every directory level present in the tree manifest | PASS | 781 file lines vs 781 files; 57 directories, max depth 5 levels |

## File count reconciliation

| source | count |
|---|---|
| `git ls-files` on `arena/01a0ce39-angora` | 781 |
| manifest rows | 781 |
| artifacts on disk | 781 |
| verbatim text artifacts | 392 |
| text-extraction artifacts | 176 |
| binary metadata artifacts | 213 |
| files with no artifact | 0 |

