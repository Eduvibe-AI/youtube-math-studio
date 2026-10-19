# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    ('btnLec21', 'id="btnLec21"' in text),
    ('btnLec22', 'id="btnLec22"' in text),
    ('btnLec23', 'id="btnLec23"' in text),
    ('view21', 'id="lecture21View"' in text),
    ('view22', 'id="lecture22View"' in text),
    ('view23', 'id="lecture23View"' in text),
    ('meta21', "21: { subj: 'math1'" in text),
    ('meta22', "22: { subj: 'math-ha'" in text),
    ('meta23', "23: { subj: 'geom'" in text),
    ('setLecture(21)', 'setLecture(21)' in text),
    ('badge23', 'data-subject="all"' in text and '>23<' in text),
    ('math1_6', 'data-subject="math1"' in text and '>6<' in text),
    ('mathha_7', 'data-subject="math-ha"' in text and '>7<' in text),
    ('geom_4', 'data-subject="geom"' in text and '>4<' in text),
]

all_passed = True
for name, res in checks:
    print(f'{name}: {res}')
    if not res:
        all_passed = False

if all_passed:
    print('ALL VERIFICATIONS PASSED!')
else:
    print('SOME CHECKS FAILED!')
