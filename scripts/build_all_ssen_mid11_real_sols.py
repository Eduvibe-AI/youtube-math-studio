# -*- coding: utf-8 -*-
"""쎈 중학수학 1-1 (22개정) 실제 정답 및 해설 전수 크롭 및 WebP 생성
- 입력: scratch/_mid11_pages/page_*.png (106쪽, 90도 정방향 회전 완료)
- OCR: scratch/ssen11_ocr_results.json (Windows Media OCR 106쪽 전수)
- 출력: 509-401-math--helper/public/ssen_2022_mid1_1_sols/{0001..1199}.webp
"""
import os
import re
import json
import cv2
import numpy as np
from PIL import Image

OCR_JSON = r"scratch/ssen11_ocr_results.json"
PAGES_DIR = r"scratch/_mid11_pages"
OUT_DIR = r"509-401-math--helper/public/ssen_2022_mid1_1_sols"
os.makedirs(OUT_DIR, exist_ok=True)

CHAR_MAP = str.maketrans({
    'O': '0', 'o': '0', 'D': '0', 'Q': '0',
    'l': '1', 'I': '1', '|': '1', 'i': '1',
    'Z': '2', 'z': '2',
    'S': '5', 's': '5',
    'B': '8',
    'q': '9', 'g': '9'
})

print("Loading OCR results...")
with open(OCR_JSON, 'r', encoding='utf-8-sig') as f:
    ocr_pages = json.load(f)

# Step 1: Detect 4-col vs 2-col per page
page_is_4col = {}
for pno_idx, pdata in enumerate(ocr_pages):
    pno = pno_idx + 1
    has_sub = False
    for line in pdata['lines']:
        for w in line['words']:
            t = w['t'].strip().translate(CHAR_MAP)
            if re.match(r'^(0\d{3}|1[01]\d{2})$', t):
                if 320 <= w['x'] <= 520 or 880 <= w['x'] <= 1100:
                    has_sub = True
                    break
        if has_sub:
            break
    page_is_4col[pno] = has_sub

def get_col_and_bounds(pno, x):
    if page_is_4col[pno]:
        if x < 350: return 0, (70, 360)
        elif x < 640: return 1, (360, 638)
        elif x < 920: return 2, (642, 925)
        else: return 3, (925, 1210)
    else:
        if x < 640: return 0, (70, 638)
        else: return 1, (642, 1210)

# Step 2: Extract all detected badges
detected = []
for pno_idx, pdata in enumerate(ocr_pages):
    pno = pno_idx + 1
    for line in pdata['lines']:
        for w in line['words']:
            wt = w['t'].strip()
            norm = wt.translate(CHAR_MAP)
            m = re.match(r'^0?([0-1]?\d{3})$', norm)
            if m:
                qnum = int(m.group(1))
                if 1 <= qnum <= 1199:
                    col, bounds = get_col_and_bounds(pno, w['x'])
                    detected.append({
                        'q': qnum, 'pno': pno, 'col': col,
                        'x': w['x'], 'y': w['y'], 'w': w['w'], 'h': w['h'],
                        'bounds': bounds
                    })
            # Shared range: 0006 ~ 0008, 0426~0430, etc.
            m_range = re.search(r'0?(\d{3,4})\s*[~∼-]\s*0?(\d{3,4})', norm)
            if m_range:
                q1 = int(m_range.group(1))
                q2 = int(m_range.group(2))
                if 1 <= q1 <= q2 <= 1199 and (q2 - q1) <= 15:
                    col, bounds = get_col_and_bounds(pno, w['x'])
                    for qnum in range(q1, q2 + 1):
                        detected.append({
                            'q': qnum, 'pno': pno, 'col': col,
                            'x': w['x'], 'y': w['y'], 'w': w['w'], 'h': w['h'],
                            'bounds': bounds, 'is_shared': True
                        })

# Sort badges chronologically
detected.sort(key=lambda d: (d['pno'], d['col'], d['y']))

q_map = {}
last_pno = 1
for d in detected:
    q = d['q']
    if q not in q_map:
        if d['pno'] >= last_pno - 1:
            q_map[q] = d
            last_pno = d['pno']

print(f"Directly mapped from OCR: {len(q_map)} / 1199")

# Step 3: Interpolate missing questions
missing_qs = [q for q in range(1, 1200) if q not in q_map]
print(f"Interpolating {len(missing_qs)} questions...")

for q in missing_qs:
    prev_q = q - 1
    while prev_q >= 1 and prev_q not in q_map:
        prev_q -= 1
    next_q = q + 1
    while next_q <= 1199 and next_q not in q_map:
        next_q += 1
    
    if prev_q in q_map and next_q in q_map:
        p_prev = q_map[prev_q]
        p_next = q_map[next_q]
        if p_prev['pno'] == p_next['pno'] and p_prev['col'] == p_next['col']:
            y_interp = (p_prev['y'] + p_next['y']) / 2.0
            q_map[q] = {
                'q': q, 'pno': p_prev['pno'], 'col': p_prev['col'],
                'x': p_prev['x'], 'y': y_interp, 'w': p_prev['w'], 'h': p_prev['h'],
                'bounds': p_prev['bounds'], 'interpolated': True
            }
        elif p_prev['pno'] == p_next['pno']:
            q_map[q] = {
                'q': q, 'pno': p_prev['pno'], 'col': p_prev['col'],
                'x': p_prev['x'], 'y': min(1600.0, p_prev['y'] + 100),
                'w': p_prev['w'], 'h': p_prev['h'],
                'bounds': p_prev['bounds'], 'interpolated': True
            }
        else:
            q_map[q] = {
                'q': q, 'pno': p_prev['pno'], 'col': p_prev['col'],
                'x': p_prev['x'], 'y': min(1600.0, p_prev['y'] + 80),
                'w': p_prev['w'], 'h': p_prev['h'],
                'bounds': p_prev['bounds'], 'interpolated': True
            }
    elif prev_q in q_map:
        p_prev = q_map[prev_q]
        q_map[q] = {
            'q': q, 'pno': p_prev['pno'], 'col': p_prev['col'],
            'x': p_prev['x'], 'y': min(1600.0, p_prev['y'] + 80),
            'w': p_prev['w'], 'h': p_prev['h'],
            'bounds': p_prev['bounds'], 'interpolated': True
        }

print(f"Total questions mapped after interpolation: {len(q_map)} / 1199")

# Step 4: Group by (pno, col) and crop
items_by_pcol = {}
for q in range(1, 1200):
    item = q_map[q]
    key = (item['pno'], item['col'])
    items_by_pcol.setdefault(key, []).append(item)

for key in items_by_pcol:
    items_by_pcol[key].sort(key=lambda it: it['y'])

print(f"Cropping {len(q_map)} solution images from {len(items_by_pcol)} columns...")
crop_count = 0
for (pno, col), q_list in items_by_pcol.items():
    page_path = os.path.join(PAGES_DIR, f"page_{pno:03d}.png")
    if not os.path.exists(page_path):
        continue
    page_img = cv2.imread(page_path)
    if page_img is None:
        continue
    
    H, W, _ = page_img.shape
    x1, x2 = q_list[0]['bounds']
    x1 = max(0, min(W - 10, x1))
    x2 = max(x1 + 50, min(W, x2))
    
    for i, it in enumerate(q_list):
        q = it['q']
        y_top = max(70, int(it['y']) - 10)
        
        if i + 1 < len(q_list):
            next_it = q_list[i + 1]
            y_bottom = max(y_top + 40, int(next_it['y']) - 10)
        else:
            if y_top < 1620:
                col_strip = page_img[y_top:1660, x1:x2]
                if col_strip.size > 0:
                    gray = cv2.cvtColor(col_strip, cv2.COLOR_BGR2GRAY)
                    dark_mask = gray < 235
                    dark_y = np.where(dark_mask.any(axis=1))[0]
                    if len(dark_y) > 0:
                        y_bottom = min(1660, y_top + int(dark_y[-1]) + 20)
                    else:
                        y_bottom = min(1660, y_top + 160)
                else:
                    y_bottom = min(1660, y_top + 160)
            else:
                y_bottom = min(H - 20, y_top + 80)
        
        y_bottom = max(y_top + 40, min(H, y_bottom))
        crop = page_img[y_top:y_bottom, x1:x2]
        
        if crop.size > 0:
            out_path = os.path.join(OUT_DIR, f"{q:04d}.webp")
            # Convert BGR to RGB
            crop_rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
            Image.fromarray(crop_rgb).save(out_path, "WEBP", quality=90)
            crop_count += 1

print(f"Successfully cropped {crop_count} / 1199 solution webp files into {OUT_DIR}!")

