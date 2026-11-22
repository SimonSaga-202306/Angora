#!/usr/bin/env python3
"""Build one derivative manifest per known search/page request; no network or raw-byte claims."""
from pathlib import Path
import csv
import json
import re

D = Path(__file__).resolve().parent
ROOT = D.parents[2]
OUT = D / 'request-manifests'
OUT.mkdir(exist_ok=True)
rows = []


def rel(p):
    p = Path(p)
    if not p.is_absolute():
        p = D / p
    if not p.is_file():
        raise FileNotFoundError(p)
    return str(p.relative_to(ROOT))


def save(record):
    record['actual_request_time'] = None
    record['provenance'] = 'Derived manifest from retained manual/protected tool observations; not original protocol data.'
    out = OUT / (record['id'] + '.json')
    with out.open('x', encoding='utf8') as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
        f.write('\n')
    rows.append({'id': record['id'], 'kind': record['kind'], 'status': record['status'],
                 'query_or_url': record['query_or_url'], 'chunk_index': record.get('chunk_index', ''),
                 'retention': record['retention'], 'result_count_if_search': record.get('result_count', ''),
                 'manifest_path': str(out.relative_to(ROOT))})


plans = sorted(D.glob('search-plan-batch-*-before-search.csv'))
queries = {}
for plan in plans:
    with plan.open(encoding='utf8', newline='') as f:
        for row in csv.DictReader(f):
            if row['id'] in queries:
                raise ValueError('duplicate query id ' + row['id'])
            queries[row['id']] = (row['query'], plan)
assert set(queries) == {f'Q{i:02}' for i in range(1, 41)}
partial = {4,13,14,15,16,19,20,22,23,30,31,33,34,36,38,39,40}
for i in range(1, 41):
    q = f'Q{i:02}'
    files = [p for p in (D / 'search-responses').glob(q + '.*.json') if 'initial-version' not in p.name]
    if len(files) != 1:
        raise ValueError(f'{q} response files: {files}')
    response = json.loads(files[0].read_text(encoding='utf8'))
    variants = [files[0]]
    variants += sorted((D / 'search-responses').glob(q + '.*.initial-version.json'))
    note = ('protected partial manual transcript' if i in partial else
            'reconstruction copied from Q17, visually compared only' if i == 35 else
            'manual tool-visible transcript; transcription may be imperfect')
    if 13 <= i <= 27:
        note += '; prior parallel-response-to-query association not independently proven'
    query, plan = queries[q]
    save({'id': q, 'kind': 'web_search', 'status': response['status'],
          'query_or_url': query, 'result_count': len(response.get('results', [])),
          'depth': '2' if i >= 24 else 'not established from retained plan',
          'retention': note, 'input_paths': [rel(plan)] + [rel(x) for x in variants]})

# URLs and request-specific retained artefacts are taken from prior plans/observations;
# extra metadata is not evidence that source contents were preserved.
p = {
'P01': [(0,'pages/P01/response-metadata.json','pages/P01/www.ekonomim.com/ekonomi/enerji-ihtiyaclarina-iyi-cozum-getiren-3-proje-odullendirildi-haberi-927872/chunk-0.visible.manual.md'), (1,'pages/P01/response-metadata.json','pages/P01/www.ekonomim.com/ekonomi/enerji-ihtiyaclarina-iyi-cozum-getiren-3-proje-odullendirildi-haberi-927872/chunk-1.visible.manual.md')],
'P02': [(7,'pages/P02/protected-blocks-observations.json'),(6,'pages/P02/protected-blocks-observations.json'),(5,'pages/P02/protected-blocks-observations.json'),(0,'pages/P02/chunk-0-refetch-metadata.json','pages/P02/kirikkaletso.org.tr/ktso/basin/uyeler/4.GRUP.pdf/chunk-0-header.protected-partial.manual.md')],
'P03': [(0,'pages/P03/response-0.error.json')],
'P04': [(0,'pages/P04/response-metadata.json','pages/P04/kouteknopark.com/firmalarimiz/chunk-0.protected-partial.manual.md')],
'P05': [(0,'pages/P05/response-metadata.json')],
'P06': [(0,'pages/P06/response-metadata.json','pages/P06/kouteknopark.com/firma-detay/id-50/chunk-0.protected-partial.manual.md')],
'P07': [(0,'pages/P07/response-metadata.json','pages/P07/compatlas.com.tr/sehir/kocaeli/gomulu/chunk-0.protected-partial.manual.md')],
'P08': [(0,'pages/P08/response-metadata.json','pages/P08/compatlas.com.tr/sehir/kirikkale/gomulu/chunk-0.protected-partial.manual.md')],
'P09': [(0,'pages/P09/response-metadata.json','pages/P09/yesilhaber.net/enerjim-sensin-2026-uc-girisime-4-milyon-tl/chunk-0.protected-partial.manual.md'),(1,'pages/P09/response-metadata.json','pages/P09/yesilhaber.net/enerjim-sensin-2026-uc-girisime-4-milyon-tl/chunk-1.protected-partial.manual.md'),(2,'pages/P09/response-metadata.json')],
'P10': [(0,'pages/P10/response-0.error.json')],
'P11': [(0,'pages/P11/response-metadata.json','pages/P11/elder.org.tr/bilgi-bankasi/haberler/enerjim-sensin-2026/chunk-0.visible.manual.md')],
'P12': [(0,'pages/P12/response-metadata.json','pages/P12/www.ekonomim.com/ekonomi/enerji-ihtiyaclarina-iyi-cozum-getiren-3-proje-odullendirildi-haberi-927872/chunk-0.reconstructed.manual.md'),(1,'pages/P12/response-metadata.json','pages/P12/www.ekonomim.com/ekonomi/enerji-ihtiyaclarina-iyi-cozum-getiren-3-proje-odullendirildi-haberi-927872/chunk-1.reconstructed.manual.md')],
'P13': [(0,'pages/P13/response-metadata.json','pages/P13/ticaretsicil.gov.tr/index.protected-partial.manual.md')],
'P14': [(0,'pages/P14/response-0.error.json')],
'P15': [(0,'pages/P15/response-metadata.json','pages/P15/ticaretsicil.gov.tr/view/hizlierisim/girisyap.protected-partial.manual.md')],
'P16': [(0,'pages/P16/response-metadata.json','pages/P16/ticaretsicil.gov.tr/view/hizlierisim/girisyap.protected-partial.manual.md')],
'P17': [(0,'pages/P17/response-metadata.json','pages/P17/kamubib-bimy.org/2022/program/chunk-0.protected-partial.manual.md'),(1,'pages/P17/response-metadata.json','pages/P17/kamubib-bimy.org/2022/program/chunk-1.protected-partial.manual.md')],
}
for pid, items in p.items():
    for chunk, *files in items:
        meta = json.loads((D/files[0]).read_text(encoding='utf8'))
        url = meta.get('request_url') or meta.get('url')
        if not url:
            raise ValueError(pid + ' missing requested URL')
        status = meta['status']
        retention = ('error metadata only' if status == 'error' else
                     'observational metadata only; no complete response body retained' if len(files) == 1 else
                     'reconstructed from earlier transcription; not a byte-identical response' if pid == 'P12' else
                     'manual transcription or protected partial excerpt; not original HTTP body')
        save({'id': f'{pid}-c{chunk}', 'kind':'fetch_page', 'query_or_url':url,
              'chunk_index':chunk, 'status':status, 'retention':retention,
              'input_paths':[rel(x) for x in files]})

for i in range(1, 6):
    aid = f'A{i:02}'
    ad = D / 'archive-index' / aid
    matches = list(ad.glob('response*.json'))
    assert len(matches) == 1
    meta = json.loads(matches[0].read_text(encoding='utf8'))
    url = meta.get('request_url') or meta.get('url')
    content = sorted(ad.rglob('chunk-0.visible.manual.md'))
    save({'id':aid+'-c0','kind':'fetch_page_archive_index','query_or_url':url,
          'chunk_index':0,'status':meta['status'],
          'retention':'tool-visible archive index manually transcribed or error metadata, not original HTTP',
          'input_paths':[rel(matches[0])] + [rel(x) for x in content]})

meta = json.loads((D/'time-reference/time.is/Beijing/response-metadata.json').read_text(encoding='utf8'))
save({'id':'T01-c0','kind':'fetch_page_time_reference','query_or_url':meta['request_url'],
      'chunk_index':0,'status':meta['status'],
      'retention':'manual tool transcription, corrected initial variant retained; no calibrated message time or original HTML',
      'input_paths':[rel('time-reference/time.is/Beijing/response-metadata.json'),
                     rel('time-reference/time.is/Beijing/chunk-0.visible.manual.md'),
                     rel('time-reference/time.is/Beijing/chunk-0.visible.manual.initial-version.md')]})

assert len(rows) == 71, len(rows)
with (D/'request-outcomes.csv').open('x',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','kind','status','query_or_url','chunk_index','retention','result_count_if_search','manifest_path'],lineterminator='\n')
    w.writeheader();w.writerows(rows)
summary={'search_requests':40,'fetch_page_requests':sum(x['kind']=='fetch_page' for x in rows),
         'archive_index_requests':sum(x['kind']=='fetch_page_archive_index' for x in rows),
         'time_reference_requests':sum(x['kind']=='fetch_page_time_reference' for x in rows),
         'all_request_manifests':len(rows),
         'search_result_items_in_retained_structures':sum(int(x['result_count_if_search']) for x in rows if x['kind']=='web_search'),
         'zero_result_searches':sum(x['result_count_if_search']==0 for x in rows if x['kind']=='web_search'),
         'fetch_errors':sum(x['status']=='error' for x in rows),
         'limitations':'Counts of request records and retained result entries; not independent sources or complete original response bytes. Earlier parallel attribution uncertain. Some entries are entirely withheld.'}
with (D/'request-outcomes-summary.json').open('x',encoding='utf8') as f:
    json.dump(summary,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
