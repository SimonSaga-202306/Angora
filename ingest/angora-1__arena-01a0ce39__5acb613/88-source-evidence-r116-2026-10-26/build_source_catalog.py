#!/usr/bin/env python3
"""Create one row per saved evidence artifact; search metadata are not sources."""
import csv
from pathlib import Path

R = Path(__file__).resolve().parent
I = R.parent
REPO = I.parent.parent
rows = []

def add(id_, kind, url, anchor, path, fidelity, limit):
    path = Path(path).resolve()
    assert path.is_file(), path
    rows.append((id_, kind, url, anchor, str(path.relative_to(REPO)), fidelity, limit))

for ident, path, commit, metadata in [
    ('WS-PARENT', 'wireshark/wireshark', '95bf9f5e0acac09f35cd8e8467cb6d93fb5a0d78', 'parent snapshot'),
    ('WS-CHILD', 'wireshark/wireshark', '0fcf4b1de93f79cc7d24ecb9c57193a61f822329', '2019-02-24 commit'),
    ('G-2018', 'gentoo/hwids', '41e194e41bcb65e764c67562e2fba877b0b4408b', '2018-09-17 commit'),
    ('G-2019', 'gentoo/hwids', '2986daf9bf2626efe6ff1d62f9713dad6cb82dae', '2019-03-17 commit'),
    ('G-2020', 'gentoo/hwids', 'cad1d07b026dd2c04b6940cf9c72b4b8639ae55b', '2020-08-13 snapshot')]:
    filename = 'manuf' if path.startswith('wireshark/') else 'ma-small.txt'
    add(ident, 'historical Git versioned file', f'https://github.com/{path}/blob/{commit}/{filename}',
        metadata, R / 'github-raw' / 'github.com' / path / commit / filename,
        'full original bytes; API Git blob checked',
        'upstream registry mirrors may share data; not issue certificate, legal identity, shipment or sale')

for ident in ('GH01','GH02','GH03','GH04','GH07','GH08','GH11','GH12','GH13','GH14','GH15','GH16','GH17'):
    add(ident, 'GitHub API full response', 'https://api.github.com/', 'see prelisted API plan',
        R / 'github-api' / f'{ident}.body.json', 'full API response as captured by gh',
        'queries and commit metadata; search zero or commit absence is not registry nonexistence')

for ident, host, stamp in [('AR01','www.kirikkaleteknopark.com','20201205142413'),
                            ('AR04','kirikkaleteknopark.com','20240920103752'),
                            ('AR05','kirikkaleteknopark.com','20260120061616')]:
    for ix in range(4):
        add(f'{ident}-{ix}', 'technology park directory capture',
            f'https://web.archive.org/web/{stamp}/https://{host}/firma-rehberi/', stamp,
            R / 'archive-chunks' / host / 'firma-rehberi' / stamp / f'chunk-{ix}.visible.md',
            'one complete tool-visible chunk; human transcription, not original HTML',
            'four chunks one source and repeat captures one publisher; not enrollment start, procurement, or legal identity')

for ident, stamp in [('AR06','20201021095900'), ('AR07','20220123023037')]:
    add(ident, 'Advensis English archive capture',
        f'https://web.archive.org/web/{stamp}/https://advensis.com.tr/en/angora-en/', stamp,
        R / 'archive-replay/advensis.com.tr/en/angora-en' / stamp / 'chunk-0.visible.md',
        'one tool-visible chunk; human transcription; images not fetched',
        'same publisher as old Turkish page; no sales or partnership inferred from filenames')

for ident, rel, url in [
    ('CDX01','kirikkaleteknopark.com/firma-rehberi/cdx.visible.md','https://web.archive.org/cdx/search/cdx?url=kirikkaleteknopark.com/firma-rehberi/&output=json&filter=statuscode:200&collapse=digest&filter=timestamp:.*&to=2026'),
    ('CDX02','advensis.com.tr/en/angora-en/cdx.visible.md','https://web.archive.org/cdx/search/cdx?url=advensis.com.tr/en/angora-en/&output=json&filter=statuscode:200&collapse=digest&to=2026'),
    ('CDX03','kirikkaletso.org.tr/ktso/basin/uyeler/4.GRUP.pdf/cdx.visible.md','https://web.archive.org/cdx/search/cdx?url=kirikkaletso.org.tr/ktso/basin/uyeler/4.GRUP.pdf&output=json&filter=statuscode:200&collapse=digest&to=2026')]:
    add(ident,'Wayback CDX query',url,'filtered index; no original publication date', R/'archive-index'/rel,
        'tool-visible text manually transcribed','empty or filtered index does not establish source nonexistence')

for ident, rel, url, note in [
    ('P01-0','kirikkaleteknopark.com/firma-rehberi/current/chunk-0.visible.md','https://kirikkaleteknopark.com/firma-rehberi/','only chunk 0 of 3; dynamic'),
    ('P02-DRAFT','kirikkaletso.org.tr/ktso/basin/uyeler/4.GRUP.pdf/chunk-0.initial-transcription.md','https://www.kirikkaletso.org.tr/ktso/basin/uyeler/4.GRUP.pdf','inaccurate first transcription preserved for audit'),
    ('P02-0','kirikkaletso.org.tr/ktso/basin/uyeler/4.GRUP.pdf/chunk-0.visible.md','https://www.kirikkaletso.org.tr/ktso/basin/uyeler/4.GRUP.pdf','refetch chunk 0 of 9; self-dated after cutoff'),
    ('P05-0','uic.jp/mac/vendor/a/p=19/chunk-0.visible.md','https://uic.jp/mac/vendor/a?p=19','refetch chunk 0 of 2; returned URL differs')]:
    add(ident,'incomplete exploration',url,'actual response date not independently calibrated',
        R/'incomplete-observations'/rel,'partial tool-visible text; human transcription',note+'; no as-of subject conclusion')

add('P03-FAIL', 'failed current page request', 'https://advensis.com.tr/en/angora-en/',
    'one attempt; observed session time not independently calibrated',
    R/'fetch-failures/P03-Advensis-current.json', 'record of tool failure, not page content',
    'single failure does not prove permanent unavailability or no historical page')

for ident, rel, url, note in [
    ('OLD-IANA','81-source-evidence-r114-2026-10-26/external-visible/www.iana.org/assignments/enterprise-numbers/page-581/index.visible.md','https://www.iana.org/assignments/enterprise-numbers/?page=581','PEN is different namespace; registration date and legal identity unknown'),
    ('OLD-FIND','69-source-evidence-r111-2026-10-26/external-visible/www.find.com.tr/Company/angoranetworksbilisimteknolojiticaretsanayianonimsirketi/index.visible.md','https://www.find.com.tr/Company/angoranetworksbilisimteknolojiticaretsanayianonimsirketi','unverified third-party directory, hidden registry ID; street matches only'),
    ('OLD-ADV','81-source-evidence-r114-2026-10-26/archive-replay/advensis.com.tr/angoranetworks/20201124234344/index.visible.md','https://web.archive.org/web/20201124234344/https://advensis.com.tr/angoranetworks/','prior Turkish page; image URLs, not delivery'),
    ('OLD-CLI','81-source-evidence-r114-2026-10-26/archive-replay/support.angoranetworks.com/p/330/20240221043438/index.visible.md','https://web.archive.org/web/20240221043438/https://support.angoranetworks.com/?p=330','already in r114; no visible 2019 publication date')]:
    add(ident,'old-round selected evidence',url,'prior saved tool-visible text',I/rel,
        'old-round human transcription; not original HTML',note)

with (R/'source-catalog.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f,lineterminator='\n')
    w.writerow(('id','kind','url','time_anchor','repo_relative_path','fidelity','use_limit'))
    w.writerows(rows)
print('Saved',len(rows),'artifact rows; chunks and repeat captures are not independent source counts')
