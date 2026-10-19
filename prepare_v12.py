import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'function setLecture\(num\)\s*\{[\s\S]*?\n    \}', text)
if m:
    print(m.group(0))

m_onload = re.search(r'window\.addEventListener\(\'load\',[\s\S]*?\}\);', text)
if m_onload:
    print('\nOnload:')
    print(m_onload.group(0))
