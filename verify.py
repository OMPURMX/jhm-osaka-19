#!/usr/bin/env python3
"""Validate the exported static website using Python 3 standard library only."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
root=Path(__file__).resolve().parent
class Parser(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=set();self.refs=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        for attr in ('href','src'):
            if a.get(attr):self.refs.append(a[attr])
docs={}
for f in (root/'dist').glob('*.html'):
    p=Parser();p.feed(f.read_text(encoding='utf-8'));docs[f.resolve()]=p
errors=[]
for f,p in docs.items():
    for ref in p.refs:
        q=urlsplit(ref)
        if q.scheme or q.netloc:continue
        dest=(f.parent/unquote(q.path)).resolve() if q.path else f
        if not dest.is_file():errors.append(f'{f.name}: missing {ref}')
        elif q.fragment and dest in docs and q.fragment not in docs[dest].ids:errors.append(f'{f.name}: missing anchor {ref}')
for line in (root/'CHECKSUMS.sha256').read_text().splitlines():
    expected,name=line.split('  ',1);file=root/name
    if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest()!=expected:errors.append(f'checksum mismatch: {name}')
if errors:
    print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: {len(docs)} HTML pages; internal links, images, and SHA-256 verified.')
