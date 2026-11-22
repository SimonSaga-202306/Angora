#!/usr/bin/env python3
"""Prelist staged blobs, then fully compare index contents with working files."""
from pathlib import Path
import csv
import hashlib
import io
import json
import random
import re
import subprocess
import sys

D=Path(__file__).resolve().parent
ROOT=D.parents[2]
scope=D/'staged-scope-before-read.csv'

def git(*args, **kwargs):
    return subprocess.check_output(['git',*args],cwd=ROOT,**kwargs)

def list_scope():
    names=[x.decode('utf8') for x in git('diff','--cached','--name-only','-z').split(b'\0') if x]
    assert len(names)==len(set(names)) and all(not p.startswith('.arena/') for p in names)
    index={}
    for entry in git('ls-files','--stage','-z').split(b'\0'):
        if not entry: continue
        meta,path=entry.split(b'\t',1)
        mode,blob,stage=meta.decode('ascii').split(' ')
        name=path.decode('utf8')
        if name in names:
            if stage!='0' or name in index:raise ValueError('unmerged index '+name)
            index[name]=(mode,blob)
    assert set(index)==set(names)
    query=''.join(index[x][1]+'\n' for x in names).encode('ascii')
    result=subprocess.run(['git','cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)'],cwd=ROOT,input=query,capture_output=True,check=True).stdout.decode('ascii').splitlines()
    assert len(result)==len(names)
    with scope.open('x',encoding='utf8',newline='') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(['path','mode','git_blob','listed_bytes'])
        for name,line in zip(names,result):
            obj,typ,size=line.split();assert obj==index[name][1] and typ=='blob'
            w.writerow([name,index[name][0],obj,int(size)])
    print(json.dumps({'prelisted_staged_paths':len(names),'excluded_local_private':True},ensure_ascii=False))

def check_scope():
    with scope.open(encoding='utf8',newline='') as f: rows=list(csv.DictReader(f))
    assert git('rev-parse','--show-object-format').strip()==b'sha1'
    query=''.join(x['git_blob']+'\n' for x in rows).encode('ascii')
    raw=subprocess.run(['git','cat-file','--batch'],cwd=ROOT,input=query,capture_output=True,check=True).stdout
    stream=io.BytesIO(raw); inv=[];hits=[]
    email=re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}',re.I)
    cred=re.compile(r'''(?i)(?:authorization\s*:\s*bearer\s+\S+|(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|passwd)\s*[=:]\s*["']?[A-Za-z0-9_\-]{8,})''')
    url=re.compile(r'(?i)[?&](?:token|sig|signature|session|auth|x-amz-credential|x-amz-signature)=')
    for x in rows:
        header=stream.readline().decode('ascii').strip().split()
        if len(header)!=3:raise ValueError('bad cat-file header '+repr(header))
        obj,typ,size=header; size=int(size); data=stream.read(size); sep=stream.read(1)
        assert obj==x['git_blob'] and typ=='blob' and size==int(x['listed_bytes']) and len(data)==size and sep==b'\n'
        p=ROOT/x['path']; assert p.is_file() and not p.is_symlink() and p.read_bytes()==data
        blob_hash=hashlib.sha1(b'blob '+str(size).encode()+b'\0'+data).hexdigest();assert blob_hash==obj
        sha=hashlib.sha256(data).hexdigest();inv.append({'path':x['path'],'bytes_read':size,'sha256':sha,'git_blob':obj,'mode':x['mode']})
        try:t=data.decode('utf8')
        except UnicodeDecodeError:continue
        a,b,c=email.findall(t),cred.findall(t),url.findall(t)
        if a or b or c:hits.append({'path':x['path'],'email_like':len(a),'credential_like':len(b),'sensitive_query':len(c)})
    assert stream.read()==b''
    earlier={x['path']:x['sha256'] for x in csv.DictReader((D/'prestage-inventory-after-read.csv').open(encoding='utf8'))}
    actual={x['path']:x['sha256'] for x in inv}
    assert all(actual.get(k)==v for k,v in earlier.items())
    sample=random.Random(1191054).sample(inv,min(30,len(inv)))
    for x in sample:
        h=hashlib.sha256()
        with (ROOT/x['path']).open('rb') as f:
            for b in iter(lambda:f.read(4096),b''):h.update(b)
        assert h.hexdigest()==x['sha256']
    check=subprocess.run(['git','diff','--cached','--check'],cwd=ROOT,capture_output=True,text=True)
    assert check.returncode==0,check.stdout+check.stderr
    if hits: raise ValueError('privacy heuristic hits (counts and paths): '+json.dumps(hits,ensure_ascii=False))
    with (D/'staged-inventory-after-read.csv').open('x',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['path','bytes_read','sha256','git_blob','mode'],lineterminator='\n');w.writeheader();w.writerows(inv)
    out={'prelisted_staged_paths':len(rows),'fully_read_index_blobs':len(inv),'bytes':sum(x['bytes_read'] for x in inv),
         'working_tree_equal':len(inv),'sha1_git_blobs_verified':len(inv),'prior_prestage_files_matching':len(earlier),
         'streaming_sample_verified':len(sample),'sample_seed':1191054,'privacy_pattern_hit_files':hits,'git_diff_check_exit':check.returncode,
         'limits':'Only index entries listed in staged-scope-before-read.csv; subsequently generated verification and Git-observation files are separate. Hashes do not prove source truth or complete privacy screening.'}
    with (D/'staged-summary.json').open('x',encoding='utf8') as f:json.dump(out,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':
    if sys.argv[1:] == ['list']:list_scope()
    elif sys.argv[1:] == ['check']:check_scope()
    else:raise SystemExit('usage: stage_verify.py list|check')
