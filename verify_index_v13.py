# -*- coding: utf-8 -*-
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("=== VERIFYING INDEX.HTML INTEGRITY FOR LECTURE 13 ===")
print("Total HTML length:", len(text))

# 1. Check buttons
for i in range(1, 14):
    btn_id = f'id="btnLec{i}"'
    assert btn_id in text, f"Missing {btn_id}"
print("✔ All buttons btnLec1 ~ btnLec13 present.")

# 2. Check views
for i in range(1, 14):
    view_id = f'id="lecture{i}View"'
    assert view_id in text, f"Missing {view_id}"
print("✔ All views lecture1View ~ lecture13View present.")

# 3. Check displays
for i in range(1, 13):
    assert f'id="lecture{i}View" style="display: none;"' in text, f"lecture{i}View not hidden"
assert '<div id="lecture13View">' in text, "lecture13View not visible by default"
print("✔ Display states verified: Views 1~12 hidden, View 13 visible.")

# 4. Check setLecture loop
assert 'for (let i = 1; i <= 13; i++)' in text, "setLecture loop not updated to 13"
assert 'if (num === 13) setTimeout(renderL13, 50);' in text, "renderL13 not in setLecture"
print("✔ setLecture(num) loop & handler verified.")

# 5. Check Lecture 13 Captures
for i in range(1, 11):
    match = re.search(rf'\./captures_v13/{i:02d}_[a-zA-Z0-9_]+\.jpg', text)
    assert match is not None, f"Capture {i:02d} not found in HTML"
    path = match.group(0).replace('./', '')
    assert os.path.exists(path), f"File {path} does not exist on disk"
print("✔ All 10 captures for Lecture 13 exist on disk and correctly linked in HTML.")

# 6. Check Canvas and JS functions
assert 'id="l13Canvas"' in text, "l13Canvas missing"
assert 'function renderL13()' in text, "renderL13 missing"
assert 'function switchLec13Tab' in text, "switchLec13Tab missing"
assert 'function copyL13ManimCode' in text, "copyL13ManimCode missing"
assert 'function setL13Mode' in text, "setL13Mode missing"
assert 'function setL13Func' in text, "setL13Func missing"
print("✔ Canvas and all JS functions for Lecture 13 verified.")

print("\n🎉 ALL 13 LECTURES VERIFIED AND FULLY INTACT!")
