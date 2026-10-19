# -*- coding: utf-8 -*-
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("=== VERIFYING INDEX.HTML INTEGRITY ===")
print("Total HTML length:", len(text))

# 1. Check buttons
for i in range(1, 13):
    btn_id = f'id="btnLec{i}"'
    assert btn_id in text, f"Missing {btn_id}"
print("✔ All buttons btnLec1 ~ btnLec12 present.")

# 2. Check views
for i in range(1, 13):
    view_id = f'id="lecture{i}View"'
    assert view_id in text, f"Missing {view_id}"
print("✔ All views lecture1View ~ lecture12View present.")

# 3. Check displays
for i in range(1, 11):
    assert f'id="lecture{i}View" style="display: none;"' in text, f"lecture{i}View not hidden"
assert 'id="lecture11View" style="display: none;"' in text, "lecture11View not hidden"
assert '<div id="lecture12View">' in text, "lecture12View not visible by default"
print("✔ Display states verified: Views 1~11 hidden, View 12 visible.")

# 4. Check setLecture loop
assert 'for (let i = 1; i <= 12; i++)' in text, "setLecture loop not updated to 12"
assert 'if (num === 12) setTimeout(renderL12, 50);' in text, "renderL12 not in setLecture"
print("✔ setLecture(num) loop & handler verified.")

# 5. Check Lecture 12 Captures
for i in range(1, 11):
    match = re.search(rf'\./captures_v12/{i:02d}_[a-zA-Z0-9_]+\.jpg', text)
    assert match is not None, f"Capture {i:02d} not found in HTML"
    path = match.group(0).replace('./', '')
    assert os.path.exists(path), f"File {path} does not exist on disk"
print("✔ All 10 captures for Lecture 12 exist on disk and correctly linked in HTML.")

# 6. Check Canvas and JS functions
assert 'id="l12Canvas"' in text, "l12Canvas missing"
assert 'function renderL12()' in text, "renderL12 missing"
assert 'function switchLec12Tab' in text, "switchLec12Tab missing"
assert 'function copyL12ManimCode' in text, "copyL12ManimCode missing"
print("✔ Canvas and all JS functions for Lecture 12 verified.")

print("\n🎉 ALL VERIFICATIONS PASSED PERFECTLY!")
