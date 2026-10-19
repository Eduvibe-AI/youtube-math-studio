import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')
doc = pymupdf.open(r'C:\Users\Admin\Downloads\2022개정+RPM+중+2-2.pdf')

for p in range(40, 46):
    txt = doc[p].get_text()
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    header = lines[0] if lines else ''
    footer = lines[-1] if lines else ''
    print(f"PDF Page {p+1} | Header: {header} | Footer: {footer} | Lines: {len(lines)}")
