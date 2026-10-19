import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

index_path = r"c:\Users\Admin\Desktop\유튜브수학\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

errors = []

# Check switcher buttons
for i in range(1, 15):
    btn_id = f"btnLec{i}"
    if f'id="{btn_id}"' not in html:
        errors.append(f"Missing switcher button {btn_id}")

# Check lecture views
for i in range(1, 15):
    view_id = f"lecture{i}View"
    if f'id="{view_id}"' not in html:
        errors.append(f"Missing lecture view {view_id}")

# Check default display states
if 'id="lecture14View" style="display: block;"' not in html and 'id="lecture14View"' not in html:
    errors.append("lecture14View not found or styled improperly")

for i in range(1, 14):
    if f'id="lecture{i}View" style="display: none;"' not in html:
        errors.append(f"lecture{i}View is not set to display: none")

# Check captures
cap_dir = r"c:\Users\Admin\Desktop\유튜브수학\captures_v14"
for i in range(1, 11):
    found = False
    for fname in os.listdir(cap_dir):
        if fname.startswith(f"{i:02d}_"):
            found = True
            break
    if not found:
        errors.append(f"Capture {i:02d} missing in captures_v14")

# Check MathJax render in setLecture
if "num === 14" not in html:
    errors.append("Lecture 14 handler missing in setLecture")

if "for (let i = 1; i <= 14; i++)" not in html:
    errors.append("setLecture loop upper bound is not 14")

if errors:
    print("VERIFICATION FAILED:")
    for err in errors:
        print(" -", err)
else:
    print("ALL VERIFICATION CHECKS PASSED!")
    print(f"Total HTML file size: {len(html):,} bytes")
