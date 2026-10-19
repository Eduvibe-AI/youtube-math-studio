# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

groups = re.findall(r'<div class="lec-group[^"]*" id="([^"]+)">', c)
print('Groups:', groups)

tabs = re.findall(r'data-subject="([^"]+)"[^>]*>[\s\S]*?<span class="tab-badge">([^<]+)</span>', c)
print('Tabs and badges:', tabs)

buttons = re.findall(r'<button[^>]*id="(btnLec\d+)"[^>]*data-subj="([^"]+)"[\s\S]*?<span class="lec-title">([^<]+)</span>', c)
print(f'Total lecture buttons: {len(buttons)}')
for bid, s, t in buttons[:10]:
    print(f'  {bid} ({s}): {t}')
print('...')
for bid, s, t in buttons[-6:]:
    print(f'  {bid} ({s}): {t}')
