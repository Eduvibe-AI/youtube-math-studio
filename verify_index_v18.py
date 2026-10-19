# -*- coding: utf-8 -*-
"""
Verification script for Lecture 18 in index.html
"""

import os
import re

def verify():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    errors = []

    # 1. Check buttons 1 to 18
    for i in range(1, 19):
        btn_id = f'id="btnLec{i}"'
        if btn_id not in html:
            errors.append(f"Missing button: {btn_id}")
        else:
            print(f"[OK] Found button {btn_id}")

    # Check active button is btnLec18
    if 'id="btnLec18"' in html and 'active' in html[html.find('id="btnLec18"') - 30 : html.find('id="btnLec18"') + 30]:
        print("[OK] btnLec18 is active")
    else:
        errors.append("btnLec18 is not active")

    # 2. Check views 1 to 18
    for i in range(1, 19):
        view_id = f'id="lecture{i}View"'
        if view_id not in html:
            errors.append(f"Missing view: {view_id}")
        else:
            print(f"[OK] Found view {view_id}")

    # Check lecture18View is visible (no display:none)
    lec18_pos = html.find('id="lecture18View"')
    lec18_tag = html[lec18_pos - 10 : lec18_pos + 40]
    if 'display: none' in lec18_tag:
        errors.append("lecture18View has display: none!")
    else:
        print("[OK] lecture18View is visible")

    # 3. Check captures in captures_v18
    if not os.path.isdir('captures_v18'):
        errors.append("Directory captures_v18 does not exist!")
    else:
        files = os.listdir('captures_v18')
        if len(files) < 10:
            errors.append(f"Expected 10 files in captures_v18, found {len(files)}")
        else:
            print(f"[OK] captures_v18 contains {len(files)} files")

    # 4. Check JS functions
    required_js = [
        'applyPreset18', 'setSign18', 'updateFromSliders18',
        'toggleAnimation18', 'updateL18', 'drawCanvasL18',
        'switchL18Tab', 'copyManimCode18', 'renderL18'
    ]
    for fn in required_js:
        if f'function {fn}' not in html:
            errors.append(f"Missing JS function: {fn}")
        else:
            print(f"[OK] Found JS function {fn}")

    # 5. Check setLecture loop
    if 'for (let i = 1; i <= 18; i++)' in html:
        print("[OK] setLecture loops up to 18")
    else:
        errors.append("setLecture loop does not loop up to 18")

    # 6. Check window onload or setLecture(18)
    if 'setLecture(18);' in html:
        print("[OK] Initial lecture set to 18")
    else:
        errors.append("Initial lecture is not set to 18")

    if errors:
        print("\n--- VERIFICATION FAILED ---")
        for err in errors:
            print(f"[ERROR] {err}")
        return False
    else:
        print("\n=== ALL VERIFICATIONS PASSED SUCCESSFULLY! ===")
        return True

if __name__ == '__main__':
    verify()
