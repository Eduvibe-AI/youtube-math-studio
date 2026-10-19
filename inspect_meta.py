# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos_meta = html.find('const LECTURE_META = {')
print("LECTURE_META context:")
print(html[pos_meta:pos_meta+500])

pos_set = html.find('function setLecture(num)')
print("\nsetLecture context:")
print(html[pos_set:pos_set+600])

pos_view = html.find('<div id="lecture24View"')
print("\nlecture24View position:", pos_view)
