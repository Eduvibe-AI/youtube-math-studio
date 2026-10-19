# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos_render = html.find('if (num === 24)')
print(html[pos_render:pos_render+400])

pos_select = html.find('function selectSubject(subj)')
print("\nselectSubject context:")
print(html[pos_select:pos_select+400])
