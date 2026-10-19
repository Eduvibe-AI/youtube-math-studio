import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('captured_summary.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*>', text)
print('Sections count:', len(sections))
print('First 5 sections:', sections[:5])

# Find where lecture 11 section is
m = re.search(r'<section[^>]*11[^>]*>[\s\S]*?</section>', text)
if m:
    print('Lecture 11 section found, length:', len(m.group(0)))
    print(m.group(0)[:300])
