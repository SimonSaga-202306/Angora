#!/usr/bin/env python3
"""Reconstruct two tool-visible replays from explicitly identified earlier templates.

These are not raw fetches or proof of byte equality. See the adjacent r110
transcription-reconstruction-plan.md and source inventory for limitations.
"""
from pathlib import Path

E = Path('ingest/angora-1__arena-01a0ce39__5acb613/65-source-evidence-r110-2026-10-26')
IN = E / 'archive-replay/support.angoranetworks.com/ht_kb'
OUT = E / 'archive-replay-reconstructed/support.angoranetworks.com/ht_kb'

def one(s: str, before: str, after: str) -> str:
    if s.count(before) != 1:
        raise AssertionError(f'expected exactly one occurrence: {before!r}')
    return s.replace(before, after, 1)

def reconstruct(slug, old_stamp, new_stamp, old_table, new_table, related, title=None):
    src = IN / slug / old_stamp / 'index.visible.md'
    dest = OUT / slug / new_stamp / 'index.visible.md'
    if dest.exists():
        raise FileExistsError(f'refusing to overwrite {dest}')
    text = src.read_text(encoding='utf-8')
    if text.count(old_stamp) < 8:
        raise AssertionError('unexpectedly few timestamp links')
    text = text.replace(old_stamp, new_stamp)
    text = one(text, old_table, new_table)
    if title:
        text = one(text, '# Knowledge Base\n', title + '\n\n# Knowledge Base\n')
    start = text.index('### Related Articles\n')
    end = text.index('### Leave A Comment?', start)
    text = text[:start] + related + '\n\n' + text[end:]
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding='utf-8', newline='')
    print(f'{src} -> {dest}: {len(text.encode("utf-8"))} bytes')

reconstruct(
    'tacacs-authentication-with-cisco-ise', '20210227205859', '20240530151345',
    '| Jan | FEB | Mar |\n|  | 27 |  |\n| 2020 | 2021 | 2022 |',
    '| Apr | MAY | Jun |\n|  | 30 |  |\n| 2023 | 2024 | 2025 |',
    '''### Related Articles

- [Software Upgrade (TFTP/USB) – Verge Switches](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "Software Upgrade (TFTP/USB) – Verge Switches")  - 0
  - 720
- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 3
  - 1388
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 1
  - 888
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 1313
- [Komut Satırı kullanımı](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - 0
  - 1672
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20240530151345/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 957''',
    'Tacacs+ Authentication (with Cisco ISE) – Angora Networks Support',
)
reconstruct(
    'stacking', '20220118063431', '20250211043846',
    '| Dec | JAN | Feb |\n|  | 18 |  |\n| 2021 | 2022 | 2023 |',
    '| Jan | FEB | Mar |\n|  | 11 |  |\n| 2024 | 2025 | 2026 |',
    '''### Related Articles

- [Software Upgrade (TFTP/USB) – Verge Switches](https://web.archive.org/web/20250211043846/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "Software Upgrade (TFTP/USB) – Verge Switches")  - 0
  - 687
- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20250211043846/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 3
  - 1236
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20250211043846/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 1
  - 842
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20250211043846/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 1207
- [Komut Satırı kullanımı](https://web.archive.org/web/20250211043846/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - 0
  - 1601
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20250211043846/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 927''',
)
