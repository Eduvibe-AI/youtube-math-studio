# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    ('btnLec24', 'id="btnLec24"' in text),
    ('view24', 'id="lecture24View"' in text),
    ('meta24', "24: { subj: 'math1'" in text),
    ('setLecture(24)', 'setLecture(24)' in text),
    ('badge24', 'data-subject="all"' in text and '>24<' in text),
    ('math1_7', 'data-subject="math1"' in text and '>7<' in text),
]

all_passed = True
for name, res in checks:
    print(f'{name}: {res}')
    if not res:
        all_passed = False

if all_passed:
    print('ALL VERIFICATIONS FOR V24 PASSED!')
else:
    print('SOME CHECKS FAILED!')
