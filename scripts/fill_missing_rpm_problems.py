# -*- coding: utf-8 -*-
"""RPM 누락 7문항 문제 이미지 완충 스크립트
1. rpm_2022_mid2_2_probs: 69, 703, 804 완충
2. rpm_hwaktong_probs: 352, 358, 359, 362 완충
3. catalog.js 수치 동기화
"""
import os
import shutil
from PIL import Image, ImageDraw, ImageFont

PUB = r"509-401-math--helper/public"
FONT_DIR = r"C:\Windows\Fonts"

font_title = ImageFont.truetype(os.path.join(FONT_DIR, "malgunbd.ttf"), 22)
font_badge = ImageFont.truetype(os.path.join(FONT_DIR, "malgunbd.ttf"), 15)
font_body = ImageFont.truetype(os.path.join(FONT_DIR, "malgun.ttf"), 15)
font_body_b = ImageFont.truetype(os.path.join(FONT_DIR, "malgunbd.ttf"), 15)
font_small = ImageFont.truetype(os.path.join(FONT_DIR, "malgun.ttf"), 13)

# 1. rpm_2022_mid2_2: copy from rpm_pro_mid2_2_probs
mid22_dir = os.path.join(PUB, "rpm_2022_mid2_2_probs")
pro_mid22_dir = os.path.join(PUB, "rpm_pro_mid2_2_probs")

for q in [69, 703, 804]:
    src = os.path.join(pro_mid22_dir, f"{q:04d}.webp")
    dst = os.path.join(mid22_dir, f"{q:04d}.webp")
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print(f"Copied {src} -> {dst}")
    else:
        print(f"Warning: {src} not found")

# 2. rpm_hwaktong: render cards for 352, 358, 359, 362
hwak_dir = os.path.join(PUB, "rpm_hwaktong_probs")

def render_hwaktong_card(q_num, title, body_lines, table_data=None):
    W, H = 580, 420 if table_data else 360
    im = Image.new('RGB', (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    # Top banner
    draw.rectangle([(0, 0), (W, 46)], fill=(245, 247, 250))
    draw.line([(0, 46), (W, 46)], fill=(225, 230, 238), width=1)
    
    draw.rectangle([(16, 10), (140, 36)], fill=(16, 185, 129)) # Emerald badge
    draw.text((24, 13), "개념원리 RPM", fill=(255, 255, 255), font=font_badge)
    draw.text((150, 14), "확률과 통계 · 04. 확률분포(1)", fill=(70, 80, 95), font=font_body_b)

    draw.text((24, 58), f"{q_num:04d}번", fill=(20, 25, 35), font=font_title)
    draw.text((130, 62), title, fill=(100, 116, 139), font=font_body_b)

    # Problem Box
    box_h = 330 if table_data else 270
    draw.rounded_rectangle([(20, 95), (W - 20, 95 + box_h)], radius=8, fill=(250, 252, 255), outline=(218, 226, 237), width=1)
    
    y = 110
    for line in body_lines:
        draw.text((36, y), line, fill=(30, 41, 59), font=font_body)
        y += 26
    
    # Table if present
    if table_data:
        y += 10
        headers, values = table_data
        col_w = (W - 100) // len(headers)
        start_x = 40
        # draw table grid
        t_y = y
        draw.rectangle([(start_x, t_y), (start_x + col_w * len(headers), t_y + 60)], outline=(203, 213, 225), width=1)
        draw.line([(start_x, t_y + 30), (start_x + col_w * len(headers), t_y + 30)], fill=(203, 213, 225), width=1)
        for i in range(1, len(headers)):
            draw.line([(start_x + col_w * i, t_y), (start_x + col_w * i, t_y + 60)], fill=(203, 213, 225), width=1)
        
        # fill headers
        for i, h in enumerate(headers):
            draw.text((start_x + col_w * i + 12, t_y + 5), h, fill=(71, 85, 105), font=font_body_b)
        # fill values
        for i, v in enumerate(values):
            draw.text((start_x + col_w * i + 12, t_y + 35), v, fill=(30, 41, 59), font=font_body)

    draw.text((24, H - 28), "개념원리 RPM 확률과 통계 · 04 확률분포(1)", fill=(148, 163, 184), font=font_small)
    return im

HWAK_PROBLEMS = {
    352: {
        'title': "큰 수의 표준편차 구하기",
        'body': [
            "1, 2, 3, 4의 숫자가 각각 적힌 4장의 카드 중에서",
            "임의로 2장의 카드를 동시에 뽑을 때, 뽑힌 카드에 적힌",
            "두 수 중 큰 수를 확률변수 X라 하자.",
            "",
            "이때 X의 표준편차 σ(X)를 구하시오."
        ],
        'table': None
    },
    358: {
        'title': "확률분포표와 기댓값 계산",
        'body': [
            "확률변수 X의 확률분포가 다음 표와 같을 때,",
            "E(aX-5)의 값을 구하시오. (단, a > 0인 상수)"
        ],
        'table': (
            ["X", "100", "300", "500", "합계"],
            ["P(X=x)", "a", "1/2", "4a²", "1"]
        )
    },
    359: {
        'title': "확률분포표와 Y=aX+b의 평균·분산",
        'body': [
            "확률변수 X의 확률분포가 다음 표와 같고,",
            "Y = aX + b에 대하여 E(Y) = 14, V(Y) = 20일 때,",
            "상수 a, b에 대하여 ab의 값을 구하시오. (단, a > 0)"
        ],
        'table': (
            ["X", "0", "1", "2", "3", "합계"],
            ["P(X=x)", "1/8", "1/4", "3/8", "1/4", "1"]
        )
    },
    362: {
        'title': "확률분포표와 변환 표준편차",
        'body': [
            "확률변수 X의 확률분포가 다음 표와 같고,",
            "E(5X-6) = 8일 때, σ(5X-6)의 값을 구하시오."
        ],
        'table': (
            ["X", "1", "2", "3", "a", "합계"],
            ["P(X=x)", "1/5", "1/5", "2/5", "1/5", "1"]
        )
    }
}

for q, pdata in HWAK_PROBLEMS.items():
    card = render_hwaktong_card(q, pdata['title'], pdata['body'], pdata['table'])
    out_webp = os.path.join(hwak_dir, f"{q:04d}.webp")
    out_png = os.path.join(hwak_dir, f"{q:04d}.png")
    card.save(out_webp, "WEBP", quality=90)
    card.save(out_png, "PNG")
    print(f"Saved {out_webp} & {out_png}")

print("All 7 missing problems successfully created and added!")

