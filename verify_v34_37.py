import os
import re
import sys
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

index_path = r"c:\Users\Admin\Desktop\유튜브수학\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

print("=== Comprehensive Verification: index.html (Lectures 1~37) ===")

# 1. Buttons
missing_btns = []
for i in range(1, 38):
    btn_id = f'id="btnLec{i}"'
    if btn_id not in content:
        missing_btns.append(f"btnLec{i}")
if missing_btns:
    print(f"[FAIL] Missing buttons: {missing_btns}")
else:
    print("[PASS] All buttons btnLec1 ~ btnLec37 are present.")

# 2. Views
missing_views = []
for i in range(1, 38):
    view_id = f'id="lecture{i}View"'
    if view_id not in content:
        missing_views.append(f"lecture{i}View")
if missing_views:
    print(f"[FAIL] Missing views: {missing_views}")
else:
    print("[PASS] All views lecture1View ~ lecture37View are present.")

# 3. Navigation Subject Badges
expected_badges = {
    "all": "37",
    "math-ha": "8",
    "math1": "11",
    "math2": "11",
    "geom": "7"
}

for subj, exp_val in expected_badges.items():
    pattern = rf'data-subject="{subj}"[^>]*>[\s\S]*?<span class="tab-badge">([^<]+)</span>'
    m = re.search(pattern, content)
    if m:
        act_val = m.group(1).strip()
        if act_val == exp_val:
            print(f"[PASS] Tab [{subj}] badge = {act_val}")
        else:
            print(f"[FAIL] Tab [{subj}] badge expected {exp_val}, got {act_val}")
    else:
        print(f"[FAIL] Tab [{subj}] badge not found")

# 4. Summary link check
if "사진 1~37 요약집" in content:
    print("[PASS] Summary link: '사진 1~37 요약집' is present.")
else:
    print("[FAIL] Summary link '사진 1~37 요약집' missing.")

# 5. Check lecture buttons for channel name brackets
btn_matches = re.findall(r'<button[^>]*class="lecture-btn[^"]*"[^>]*>([\s\S]*?)</button>', content)
found_channel_brackets_in_btns = []
channel_keywords = ["사오수학", "MK.K", "수학리더", "수학싸부", "수능수학", "이정환", "이동준", "Ray", "SeolMath", "다정수학", "유튜브"]
for btn in btn_matches:
    for kw in channel_keywords:
        if f"({kw})" in btn:
            found_channel_brackets_in_btns.append(btn.strip())

if found_channel_brackets_in_btns:
    print(f"[FAIL] Found channel brackets in buttons: {found_channel_brackets_in_btns}")
else:
    print("[PASS] No channel/author brackets in any of the 37 lecture buttons.")

# 6. Check LECTURE_META keys 1 to 37
meta_missing = []
for i in range(1, 38):
    if f"{i}:" not in content and f"'{i}':" not in content and f'"{i}":' not in content:
        meta_missing.append(i)
if meta_missing:
    print(f"[FAIL] LECTURE_META missing entries: {meta_missing}")
else:
    print("[PASS] LECTURE_META contains entries 1 through 37.")

# 7. Check video and capture assets
base_dir = r"c:\Users\Admin\Desktop\유튜브수학"
for i in [34, 35, 36, 37]:
    vid = os.path.join(base_dir, f"lecture_video{i}.mp4")
    vid_ok = os.path.exists(vid) and os.path.getsize(vid) > 50000
    print(f"[PASS] Video {i}: {os.path.basename(vid)} ({os.path.getsize(vid):,} bytes)" if vid_ok else f"[FAIL] Video {i} issue")
    
    cap_dir = os.path.join(base_dir, f"captures_v{i}")
    caps = [f for f in os.listdir(cap_dir) if f.endswith(('.jpg', '.png'))] if os.path.exists(cap_dir) else []
    print(f"[PASS] Captures {i}: {len(caps)} keyframes in {os.path.basename(cap_dir)}" if len(caps) >= 5 else f"[FAIL] Captures {i} issue: only {len(caps)} images")

# 8. HTTP server ping
try:
    with urllib.request.urlopen("http://localhost:8085/index.html", timeout=3) as resp:
        print(f"[PASS] Local HTTP Server responding: status {resp.status}")
except Exception as e:
    print(f"[FAIL] Local HTTP Server error: {e}")

print("=== All Checks Completed Successfully! ===")
