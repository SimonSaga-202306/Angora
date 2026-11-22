#!/usr/bin/env python3
"""Compare only explicitly prelisted local transcriptions; no network or legal identity inference."""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

D = Path(__file__).resolve().parent
ROOT = D.parents[2]  # /home/user/Angora
rows = list(csv.DictReader((D / 'claims-comparison-scope-before-read.csv').open(encoding='utf-8', newline='')))
contents = {}
inventory = []
for row in rows:
    p = ROOT / row['path']
    b = p.read_bytes()
    if len(b) != int(row['listed_bytes']):
        raise ValueError(f'changed after listing: {p}')
    contents[row['path']] = b.decode('utf-8')
    inventory.append({'path': row['path'], 'bytes_read': len(b), 'sha256': hashlib.sha256(b).hexdigest()})

def by_fragment(fragment):
    hits = [v for k, v in contents.items() if fragment in k]
    if len(hits) != 1:
        raise ValueError(f'{fragment}: {len(hits)} matches')
    return hits[0]

preview = by_fragment('85-source-evidence-r115-2026-10-26/external-visible/www.enerjimagazin.com')
article = by_fragment('P01/www.ekonomim.com/ekonomi/enerji-ihtiyaclarina-iyi-cozum-getiren-3-proje-odullendirildi-haberi-927872/chunk-0')
elder = by_fragment('P11/elder.org.tr/bilgi-bankasi/haberler/enerjim-sensin-2026/chunk-0')
article_meta = json.loads(by_fragment('pages/P01/response-metadata.json'))
q06 = json.loads(by_fragment('search-responses/Q06.tool-visible.manual.json'))
match = re.search(r'şunlardan oluştu:.*?"([^"]+)"', preview, re.S)
if not match:
    raise ValueError('r115 shortlist marker not found')
shortlist = [x.strip().rstrip('.') for x in re.split(r',\s*|\s+ve\s+', match.group(1))]
if len(shortlist) != 20 or shortlist.count('Angora Networks') != 1:
    raise ValueError(f'unexpected shortlist parse: {shortlist!r}')
winner_text = article.split('## Ödüle değer bulunan 3 proje', 1)[1].split('## Hangi çözümleri sundular?', 1)[0]
solutions = article.split('## Hangi çözümleri sundular?', 1)[1].split('Henüz bu içeriğe yorum yapılmamış.', 1)[0]
solution_names = re.findall(r'^\*\*([^*]+):\*\*', solutions, re.M)
if len(solution_names) != 20 or solution_names.count('Angora Networks') != 1:
    raise ValueError(f'unexpected solution headings: {solution_names!r}')
expected = ('Pulse Systech', 'AT-AK', 'VoltGuard')
if any(x not in winner_text for x in expected) or 'Angora Networks' in winner_text:
    raise ValueError('unexpected future-dated article winner segment')
# Explicit name aliases are heuristic text comparisons, not corporate-identity mappings.
alias = {'pulsesystech': 'pulse systech', 'blue hybrid': 'blue hybrid solutions',
         'cyberweave ai oy': 'cyber weave ai', 'energywisepro': 'energy wisepro',
         'volt pil': 'volt pil batarya'}
normalized_solutions = {x.casefold(): x for x in solution_names}
matched, unmatched = [], []
for name in shortlist:
    canonical = alias.get(name.casefold(), name.casefold())
    (matched if canonical in normalized_solutions else unmatched).append(
        {'shortlist_text': name, 'article_text': normalized_solutions.get(canonical), 'used_alias': name.casefold() in alias}
    )
if unmatched:
    raise ValueError(f'unmatched candidate text: {unmatched}')
result = {
    'scope': 'Saved, potentially imperfect manual tool transcriptions only; NOT confirmation of future events or legal entities.',
    'shortlist_names_count': len(shortlist),
    'solution_heading_count': len(solution_names),
    'textual_matches_with_explicit_aliases': len(matched),
    'alias_based_matches': sum(x['used_alias'] for x in matched),
    'comparisons': matched,
    'article_winner_names_as_text': list(expected),
    'angora_in_winner_paragraph': 'Angora Networks' in winner_text,
    'angora_in_solution_headings': 'Angora Networks' in solution_names,
    'amounts_as_article_claim_try': [2000000, 1250000, 750000],
    'sum_try': sum([2000000, 1250000, 750000]),
    'elder_full_saved_text_angora_casefold_count': elder.casefold().count('angora'),
    'elder_self_date_literal': '25 Eylül 2026',
    'article_self_published_literal': article_meta['published_date_as_visible'],
    'article_search_pageAge_literal': q06['results'][1]['pageAge'],
    'future_date_caveat': 'Source asserts a final on 2026-10-28 and publication 2026-10-30; both are later than the session-provided 2026-10-26 UTC date. Merely a comparison of source claims, not a finding that the final occurred as of that date.',
}
assert result['elder_self_date_literal'] in elder
with (D / 'claims-comparison-inventory-after-read.csv').open('x', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['path', 'bytes_read', 'sha256'], lineterminator='\n')
    w.writeheader()
    w.writerows(inventory)
with (D / 'claims-comparison-result.json').open('x', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({k: v for k, v in result.items() if k != 'comparisons'}, ensure_ascii=False, indent=2))
print(f'Full byte read: {len(inventory)}/{len(rows)} files; {sum(x["bytes_read"] for x in inventory)} bytes')
