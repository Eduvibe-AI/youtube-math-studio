# -*- coding: utf-8 -*-
"""
Verification script for index.html (Lectures 1 to 28)
"""

import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

def verify():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    print("=== 1. Checking Lecture Buttons ===")
    missing_btns = []
    for i in range(1, 29):
        if f'id="btnLec{i}"' not in html:
            missing_btns.append(i)
    if missing_btns:
        print(f"❌ Missing buttons: {missing_btns}")
    else:
        print("✅ All 28 lecture buttons (btnLec1 ~ btnLec28) found!")

    print("\n=== 2. Checking Lecture Views ===")
    missing_views = []
    for i in range(1, 29):
        if f'id="lecture{i}View"' not in html:
            missing_views.append(i)
    if missing_views:
        print(f"❌ Missing views: {missing_views}")
    else:
        print("✅ All 28 lecture views (lecture1View ~ lecture28View) found!")

    print("\n=== 3. Checking Badges ===")
    tabs = re.findall(r'data-subject="([^"]+)"[^>]*>[\s\S]*?<span class="tab-badge">([^<]+)</span>', html)
    expected_badges = {'all': '28', 'math-ha': '8', 'math1': '8', 'math2': '7', 'geom': '5'}
    badge_dict = dict(tabs)
    for subj, exp in expected_badges.items():
        actual = badge_dict.get(subj)
        if actual == exp:
            print(f"✅ Badge [{subj}]: {actual}")
        else:
            print(f"❌ Badge [{subj}]: expected {exp}, got {actual}")

    print("\n=== 4. Checking LECTURE_META ===")
    meta_keys = re.findall(r'(\d+):\s*\{\s*subj:', html)
    meta_set = set(int(k) for k in meta_keys)
    missing_meta = [i for i in range(1, 29) if i not in meta_set]
    if missing_meta:
        print(f"❌ Missing meta: {missing_meta}")
    else:
        print("✅ All 28 lecture metadata entries present!")

    print("\n=== 5. Checking Keyframes on Disk ===")
    dirs = [
        ('captures_v25', 10),
        ('captures_v26', 8),
        ('captures_v27', 10),
        ('captures_v28', 10),
    ]
    for d, expected_cnt in dirs:
        if os.path.exists(d):
            files = [f for f in os.listdir(d) if f.endswith('.jpg')]
            print(f"✅ Directory {d}: {len(files)} / {expected_cnt} files")
        else:
            print(f"❌ Directory {d} does not exist!")

    print("\n=== 6. Checking Video Files on Disk ===")
    vids = ['lecture_video25.mp4', 'lecture_video26.mp4', 'lecture_video27.mp4', 'lecture_video28.mp4']
    for v in vids:
        if os.path.exists(v):
            size_mb = os.path.getsize(v) / (1024 * 1024)
            print(f"✅ Video {v}: {size_mb:.1f} MB")
        else:
            print(f"❌ Video {v} missing!")

    print("\nVerification complete!")

if __name__ == '__main__':
    verify()
