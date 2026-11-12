# -*- coding: utf-8 -*-
"""RPM 잔여 이미지(대수 59+5, 중1-2 9+12, 기하 55) 전수 완충 스크립트"""

import os
import sys
import json
import re
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

PUB = r"509-401-math--helper/public"
WB_DATA = os.path.join(PUB, "workbook_data")
FONT_DIR = r"C:\Windows\Fonts"

font_title = ImageFont.truetype(os.path.join(FONT_DIR, "malgunbd.ttf"), 22)
font_badge = ImageFont.truetype(os.path.join(FONT_DIR, "malgunbd.ttf"), 15)
font_body = ImageFont.truetype(os.path.join(FONT_DIR, "malgun.ttf"), 15)
font_body_b = ImageFont.truetype(os.path.join(FONT_DIR, "malgunbd.ttf"), 15)
font_small = ImageFont.truetype(os.path.join(FONT_DIR, "malgun.ttf"), 13)

def wrap_text(text, font, max_width, draw):
    lines = []
    for paragraph in str(text).split('\n'):
        if not paragraph.strip():
            lines.append('')
            continue
        cur_line = ''
        for ch in paragraph:
            test_line = cur_line + ch
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if bbox[2] - bbox[0] > max_width and cur_line:
                lines.append(cur_line)
                cur_line = ch
            else:
                cur_line = test_line
        if cur_line:
            lines.append(cur_line)
    return lines

def render_prob_card(book_name, qn, goal, steps, out_path):
    W = 760
    temp_img = Image.new('RGB', (W, 100))
    draw = ImageDraw.Draw(temp_img)
    
    body_lines = wrap_text(goal or f"{book_name} {qn}번 핵심 문항입니다.", font_body_b, W - 60, draw)
    step1_lines = []
    if steps and len(steps) > 0 and len(steps[0]) > 1:
        step1_lines = wrap_text(f"【조건 및 문제 맥락】\n{steps[0][1]}", font_body, W - 70, draw)
        
    line_h = 24
    content_h = len(body_lines) * line_h + (len(step1_lines) * line_h + 30 if step1_lines else 0)
    H = max(260, 80 + content_h + 40)
    
    im = Image.new('RGB', (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    # Outer border
    draw.rectangle([(0, 0), (W - 1, H - 1)], outline=(220, 224, 230), width=2)
    # Header bar
    draw.rectangle([(0, 0), (W, 52)], fill=(245, 247, 250))
    draw.line([(0, 52), (W, 52)], fill=(218, 222, 229), width=2)
    
    # Badges
    draw.rounded_rectangle([(20, 10), (120, 42)], radius=6, fill=(44, 62, 80))
    draw.text((32, 16), f"문제 {qn:04d}", fill=(255, 255, 255), font=font_badge)
    draw.text((135, 17), book_name, fill=(100, 110, 125), font=font_body_b)
    
    # Body
    y = 75
    for l in body_lines:
        draw.text((30, y), l, fill=(20, 25, 35), font=font_body_b)
        y += line_h
        
    if step1_lines:
        y += 12
        box_top = y
        box_bottom = y + len(step1_lines) * line_h + 16
        draw.rounded_rectangle([(30, box_top), (W - 30, box_bottom)], radius=8, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
        sy = box_top + 8
        for l in step1_lines:
            draw.text((45, sy), l, fill=(71, 85, 105), font=font_body)
            sy += line_h
            
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    im.save(out_path, 'WEBP', quality=92)

def render_sol_card(book_name, qn, ans, steps, out_path):
    W = 760
    temp_img = Image.new('RGB', (W, 100))
    draw = ImageDraw.Draw(temp_img)
    
    rendered_steps = []
    line_h = 23
    total_step_lines = 0
    
    if steps:
        for s in steps:
            title = s[0] if len(s) > 0 else "풀이 단계"
            body = s[1] if len(s) > 1 else ""
            t_lines = wrap_text(f"▶ {title}", font_body_b, W - 70, draw)
            b_lines = wrap_text(body, font_body, W - 80, draw)
            rendered_steps.append((t_lines, b_lines))
            total_step_lines += len(t_lines) + len(b_lines) + 1
            
    ans_lines = wrap_text(f"정답: {ans}", font_title, W - 100, draw)
    H = max(320, 80 + total_step_lines * line_h + len(ans_lines) * 32 + 70)
    
    im = Image.new('RGB', (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    # Outer border
    draw.rectangle([(0, 0), (W - 1, H - 1)], outline=(220, 224, 230), width=2)
    # Header bar
    draw.rectangle([(0, 0), (W, 52)], fill=(238, 242, 246))
    draw.line([(0, 52), (W, 52)], fill=(218, 222, 229), width=2)
    
    # Badges
    draw.rounded_rectangle([(20, 10), (140, 42)], radius=6, fill=(30, 115, 190))
    draw.text((28, 16), f"해설 {qn:04d}", fill=(255, 255, 255), font=font_badge)
    draw.text((155, 17), f"{book_name} [정답 및 상세해설]", fill=(70, 80, 95), font=font_body_b)
    
    y = 75
    for t_lines, b_lines in rendered_steps:
        for l in t_lines:
            draw.text((35, y), l, fill=(30, 41, 59), font=font_body_b)
            y += line_h
        for l in b_lines:
            draw.text((45, y), l, fill=(51, 65, 85), font=font_body)
            y += line_h
        y += 10
        
    y += 10
    ans_h = len(ans_lines) * 32 + 20
    draw.rounded_rectangle([(30, y), (W - 30, y + ans_h)], radius=8, fill=(239, 246, 255), outline=(147, 197, 253), width=2)
    ay = y + 10
    for l in ans_lines:
        draw.text((50, ay), l, fill=(29, 78, 216), font=font_title)
        ay += 32
        
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    im.save(out_path, 'WEBP', quality=92)


def load_book_sol_data(bid):
    """Run node to extract pure JSON of WB_SOL[bid]"""
    import subprocess
    js_file = os.path.join(WB_DATA, f"sol_{bid}.js").replace('\\', '/')
    cmd = [
        'node', '-e',
        f"""
        const fs = require('fs');
        const vm = require('vm');
        const code = fs.readFileSync('{js_file}', 'utf8');
        const sandbox = {{ window: {{}} }};
        vm.createContext(sandbox);
        vm.runInContext(code, sandbox);
        const data = sandbox.window.WB_SOL['{bid}'];
        console.log(JSON.stringify(data));
        """
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
    if res.returncode != 0:
        raise RuntimeError(f"Failed to load sol data for {bid}: {res.stderr}")
    return json.loads(res.stdout)


# 1. RPM 2022 Daesu
print("=== 1. RPM 대수 (rpm_2022_daesu) 완충 ===")
daesu_data = load_book_sol_data('rpm_2022_daesu')
daesu_pdir = os.path.join(PUB, "rpm_2022_daesu_probs")
daesu_sdir = os.path.join(PUB, "rpm_2022_daesu_sols")

existing_p = set(int(f.split('.')[0]) for f in os.listdir(daesu_pdir) if f.endswith(('.webp', '.png', '.jpg')) and f.split('.')[0].isdigit())
existing_s = set(int(f.split('.')[0]) for f in os.listdir(daesu_sdir) if f.endswith(('.webp', '.png', '.jpg')) and f.split('.')[0].isdigit())

filled_p = 0
filled_s = 0

for k_str, v in daesu_data.items():
    qn = int(k_str)
    ans = v[0] if len(v) > 0 else ""
    goal = v[1] if len(v) > 1 else ""
    steps = v[2] if len(v) > 2 else []
    
    if qn not in existing_p:
        out_file = os.path.join(daesu_pdir, f"{qn:04d}.webp")
        render_prob_card("RPM 대수", qn, goal, steps, out_file)
        filled_p += 1
        
    if qn not in existing_s:
        out_file = os.path.join(daesu_sdir, f"{qn:04d}.webp")
        render_sol_card("RPM 대수", qn, ans, steps, out_file)
        filled_s += 1

print(f"RPM 대수: 문제 이미지 {filled_p}개 완충, 해설 이미지 {filled_s}개 완충 완료")


# 2. RPM 2022 Mid 1-2
print("\n=== 2. RPM 중학수학 1-2 (rpm_2022_mid1_2) 완충 ===")
mid12_data = load_book_sol_data('rpm_2022_mid1_2')
mid12_pdir = os.path.join(PUB, "rpm_2022_mid1_2_probs")
mid12_sdir = os.path.join(PUB, "rpm_2022_mid1_2_sols")

existing_p = set(int(f.split('.')[0]) for f in os.listdir(mid12_pdir) if f.endswith(('.webp', '.png', '.jpg')) and f.split('.')[0].isdigit())
existing_s = set(int(f.split('.')[0]) for f in os.listdir(mid12_sdir) if f.endswith(('.webp', '.png', '.jpg')) and f.split('.')[0].isdigit())

filled_p = 0
filled_s = 0

for k_str, v in mid12_data.items():
    qn = int(k_str)
    ans = v[0] if len(v) > 0 else ""
    goal = v[1] if len(v) > 1 else ""
    steps = v[2] if len(v) > 2 else []
    
    if qn not in existing_p:
        out_file = os.path.join(mid12_pdir, f"{qn:04d}.webp")
        render_prob_card("RPM 중학수학 1-2", qn, goal, steps, out_file)
        filled_p += 1
        
    if qn not in existing_s:
        out_file = os.path.join(mid12_sdir, f"{qn:04d}.webp")
        render_sol_card("RPM 중학수학 1-2", qn, ans, steps, out_file)
        filled_s += 1

print(f"RPM 중학수학 1-2: 문제 이미지 {filled_p}개 완충, 해설 이미지 {filled_s}개 완충 완료")


# 3. RPM Giha
print("\n=== 3. RPM 기하 (rpm_giha) 완충 ===")
giha_data = load_book_sol_data('rpm_giha')
giha_sdir = os.path.join(PUB, "rpm_giha_sols")

existing_s = set(int(f.split('.')[0]) for f in os.listdir(giha_sdir) if f.endswith(('.webp', '.png', '.jpg')) and f.split('.')[0].isdigit())

filled_s = 0
for k_str, v in giha_data.items():
    qn = int(k_str)
    ans = v[0] if len(v) > 0 else ""
    goal = v[1] if len(v) > 1 else ""
    steps = v[2] if len(v) > 2 else []
    
    if qn not in existing_s:
        out_file = os.path.join(giha_sdir, f"{qn:04d}.webp")
        render_sol_card("RPM 기하", qn, ans, steps, out_file)
        filled_s += 1

print(f"RPM 기하: 해설 이미지 {filled_s}개 완충 완료")
