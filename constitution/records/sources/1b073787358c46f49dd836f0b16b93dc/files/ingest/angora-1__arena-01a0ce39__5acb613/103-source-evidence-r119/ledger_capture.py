#!/usr/bin/env python3
"""Copy each prelisted file separately and record each request as its own ledger event."""
from pathlib import Path
import csv
import hashlib
import json
import subprocess
import sys

D=Path(__file__).resolve().parent
ROOT=D.parents[2]
ledger=ROOT/'tools/constitution_ledger.py'
with (D/'ledger-input-scope-before-read.csv').open(encoding='utf8',newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==len({x['path'] for x in rows})
inventory=[]
for x in rows:
    p=ROOT/x['path']
    if not p.is_file() or p.is_symlink() or '.arena' in p.parts:
        raise ValueError('invalid input '+str(p))
    b=p.read_bytes()
    if len(b)!=int(x['listed_bytes']):
        raise ValueError('input changed since listing '+str(p))
    inventory.append({'path':x['path'],'bytes_read':len(b),'sha256':hashlib.sha256(b).hexdigest(),
                      'method':x['method'],'classification':x['classification']})
with (D/'ledger-input-inventory-after-read.csv').open('x',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes_read','sha256','method','classification'],lineterminator='\n')
    w.writeheader();w.writerows(inventory)

receipt_path=D/'ledger-capture-receipts.jsonl'
counts={'source':0,'request_event':0,'issue_event':0}
with receipt_path.open('x',encoding='utf8') as receipts:
    def run(kind,path,extra,note):
        args=[sys.executable,str(ledger),kind,'--file',str(ROOT/path),'--method',extra['method'],'--note',note]
        if kind=='source': args += ['--original-path',path]
        else: args += ['--event-kind',extra['event_kind']]
        r=subprocess.run(args,cwd=ROOT,capture_output=True,text=True)
        row={'kind':kind,'input_path':path,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
        if r.returncode==0:
            data=json.loads(r.stdout)
            if data.get('outcome')!='copied':
                raise ValueError('unexpected ledger result '+r.stdout)
            row['record_id']=data['id']
        receipts.write(json.dumps(row,ensure_ascii=False)+'\n');receipts.flush()
        if r.returncode:
            raise RuntimeError(f'ledger failed for {path}; see receipts')
    for x in inventory:
        note=('r119 separate file; '+x['classification']+'; local file copied byte-for-byte; '
              'not an assertion that the internet response was captured byte-for-byte. Event time unknown.')
        run('source',x['path'],{'method':x['method']},note)
        counts['source']+=1
    manifests=sorted((D/'request-manifests').glob('*.json'))
    assert len(manifests)==71
    for p in manifests:
        path=str(p.relative_to(ROOT))
        run('event',path,{'method':'supplied_file','event_kind':'tool_request_observation'},
            'One request per derived manifest; tool output may be partial/manual/reconstructed, as recorded. Actual request time unknown.')
        counts['request_event']+=1
    issues=[
      ROOT/'constitution/issues/r119-time-observations-and-scope.md',
      ROOT/'constitution/issues/r119-time-and-source-date-correction-v2.md',
      ROOT/'constitution/issues/r119-application-state-and-scope.md',
      D/'issues-and-corrections.md', D/'path-provenance-check.md',
      D/'r114-crosscheck-plan-before-list.md',D/'2022-agenda-search-splice-observation.md',
      D/'elapsed-observation.json', D/'P01-transcription-correction-and-P12.md',
    ]
    for p in issues:
        run('event',str(p.relative_to(ROOT)),{'method':'supplied_file','event_kind':'issue_or_verification'},
            'Separate r119 issue or verification; local generated record, not a fabricated event time.')
        counts['issue_event']+=1
summary={'scope':len(rows),'bytes':sum(x['bytes_read'] for x in inventory),
         'source_records':counts['source'],'request_events':counts['request_event'],
         'issue_or_check_events':counts['issue_event'],
         'receipt_lines':sum(counts.values()),
         'limits':'Receipts, resulting records, snapshots and later messages are generated after input scope; their consistency requires separate verification.'}
with (D/'ledger-capture-summary.json').open('x',encoding='utf8') as f:
    json.dump(summary,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
