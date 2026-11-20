#!/usr/bin/env python3
"""Prelist scopes, then independently read each listed path fully and hash it."""
import csv
import hashlib
import json
from pathlib import Path
import sys

R=Path(__file__).resolve().parent
I=R.parent
REPO=I.parent.parent
W=I/'01-text-verbatim/workstation'
HOUSEKEEPING={
    'round-readback-scope.csv','round-readback-inventory.csv','round-readback-summary.json',
    'final-deliverables-scope.csv','final-deliverables-inventory.csv','final-deliverables-summary.json',
    'verification-preflight-results.txt','verification-final-results.txt','completion-clock.json',
}


def relative(p):
    return str(p.relative_to(REPO))


def round_paths():
    return sorted(p for p in R.rglob('*') if p.is_file() and str(p.relative_to(R)) not in HOUSEKEEPING)


def write_csv(path, header, data):
    with path.open('w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f,lineterminator='\n');writer.writerow(header);writer.writerows(data)


def list_scope(scope, paths):
    assert len(set(p for p,_ in paths))==len(paths)
    records=[]
    for p,mode in paths:
        assert p.is_file() and not p.is_symlink(),p
        records.append((relative(p),p.stat().st_size,mode))
    write_csv(scope,('path','listed_bytes','mode'),records)
    print('PRELISTED',len(records),'paths;',sum(x[1] for x in records),'bytes; no contents read by list operation')


def do_read(scope, inventory, summary, enforce_round=False):
    with scope.open(encoding='utf-8',newline='') as f:
        plan=list(csv.DictReader(f))
    if enforce_round:
        self_set=[relative(p) for p in round_paths()]
        assert [r['path'] for r in plan]==self_set, 'round directory changed after listing'
    result=[];total=0;decoded=0
    for r in plan:
        p=REPO/r['path'];b=p.read_bytes()
        assert len(b)==int(r['listed_bytes']),(p,len(b),r['listed_bytes'])
        if r['mode']=='utf8':
            lines=len(b.decode('utf-8').splitlines());decoded+=1
        elif r['mode']=='bytes-only':
            lines='not decoded'
        else:
            raise ValueError(r['mode'])
        total+=len(b)
        result.append((r['path'],len(b),hashlib.sha256(b).hexdigest(),r['mode'],lines))
    write_csv(inventory,('path','bytes_read','sha256','mode','lines'),result)
    result_summary={
        'listed_paths':len(plan),'read_paths':len(result),'utf8_decoded_paths':decoded,
        'bytes_only_paths':len(result)-decoded,'total_bytes':total,
        'scope_file':relative(scope),'scope_sha256':hashlib.sha256(scope.read_bytes()).hexdigest(),
        'inventory_file':relative(inventory),'inventory_sha256':hashlib.sha256(inventory.read_bytes()).hexdigest(),
        'scope_limit':'only the paths prelisted in the scope; not an independent-source count',
        'not_proved':'byte read and SHA do not prove correctness of human transcription or external truth',
    }
    if enforce_round:
        result_summary['excluded_housekeeping_files']=sorted(HOUSEKEEPING)
    summary.write_text(json.dumps(result_summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('全量读取完成（预列限定范围）:',len(result),'/',len(plan),'paths;',total,'bytes;',decoded,'UTF-8 decoded;',len(result)-decoded,'bytes-only')


def main():
    op=sys.argv[1]
    if op=='round-list':
        list_scope(R/'round-readback-scope.csv',[(p,'utf8') for p in round_paths()])
    elif op=='round-read':
        do_read(R/'round-readback-scope.csv',R/'round-readback-inventory.csv',R/'round-readback-summary.json',True)
    elif op=='final-list':
        docs=[
            (W/'08-customer-pipeline/185-angora-historical-address-park-evidence-r116-2026-10-26.md','utf8'),
            (W/'09-orders/120-angora-orders-dossier-2026-10-21.r116-appendix.md','utf8'),
            (W/'09-orders/120-angora-orders-master-2026-10-21.mapping-r116.md','utf8'),
            (I/'89-followup-angora-r116-2026-10-26/angora-networks.md','utf8'),
            (I/'90-audit-r116-2026-10-26.md','utf8'),
            (W/'09-orders/120-angora-orders-dossier-2026-10-21.md','bytes-only'),
        ]
        list_scope(R/'final-deliverables-scope.csv',docs)
    elif op=='final-read':
        do_read(R/'final-deliverables-scope.csv',R/'final-deliverables-inventory.csv',R/'final-deliverables-summary.json')
    else:
        raise ValueError(op)


if __name__=='__main__':
    main()
