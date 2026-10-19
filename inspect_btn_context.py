# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
pos = html.find('id="btnLec24"')
print("btnLec24 surrounding context:")
print(html[pos-150:pos+250])

pos22 = html.find('id="btnLec22"')
print("\nbtnLec22 surrounding context:")
print(html[pos22-150:pos22+250])

pos23 = html.find('id="btnLec23"')
print("\nbtnLec23 surrounding context:")
print(html[pos23-150:pos23+250])

pos4 = html.find('id="btnLec4"')
print("\nbtnLec4 surrounding context:")
print(html[pos4-150:pos4+250])
