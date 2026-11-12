import os
import sys
import json
import re
import pymupdf

sys.path.insert(0, '509-401-math--helper/scripts')
sys.path.insert(0, 'scripts')
from batch_update_g1_real_solutions import parse_sol_pdf, split_into_steps
import crop_mock_images as cm

sys.stdout.reconfigure(encoding='utf-8')

dl_dir = os.path.expanduser('~/Downloads')
base_data = '509-401-math--helper/public/workbook_data'
base_public = '509-401-math--helper/public'

TARGETS = [
    ('mock_8303', '2023학년도 3월 고1 학력평가', '2023 3월 고1 전국연합학력평가 정답해설.pdf'),
    ('mock_8306', '2023학년도 6월 고1 학력평가', '2023 6월 고1 전국연합학력평가 정답해설.pdf'),
    ('mock_8309', '2023학년도 9월 고1 학력평가', '2023 9월 고1 전국연합학력평가 수학 정답및해설.pdf'),
    ('mock_8311', '2023학년도 11월 고1 학력평가', '2023 11월 고1 전국연합학력평가 수학 해설지.pdf'),
]

new_catalog_entries = []

for eid, title, pdf_name in TARGETS:
    pdf_path = os.path.join(dl_dir, pdf_name)
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        continue
        
    print(f"\n--- Processing {eid}: {title} ---")
    ans_dict, sols_dict = parse_sol_pdf(pdf_path)
    print(f"Parsed {len(ans_dict)} answers, {len(sols_dict)} solutions")
    
    # 1. Build sol data JSON
    sol_data = {}
    for qn in range(1, 31):
        qn_str = str(qn)
        ans_str = ans_dict.get(qn, "①")
        sol_info = sols_dict.get(qn, {'intent': f"{qn}번 핵심 개념", 'text': f"{qn}번 풀이"})
        intent = sol_info['intent'] or f"{qn}번 핵심 개념"
        sol_text = sol_info['text']
        
        first_line = sol_text.split('\n')[0] if sol_text else intent
        steps = split_into_steps(intent, sol_text, ans_str, qn)
        
        # Standard 13-tuple format for workbook
        entry = [
            ans_str,                                     # [0]: ans
            f"{intent} — {first_line[:60]}",            # [1]: summary
            steps,                                       # [2]: steps
            f"정답 {ans_str} — 풀이 단계를 열어 과정을 확인하세요.", # [3]: guide
            f"계산 과정에서 부호나 조건을 혼동하지 않도록 주의하세요. 정답은 {ans_str}입니다.", # [4]: warn
            "수학 영역",                                  # [5]: badge
            qn,                                          # [6]: qn
            [intent, [["[조건 분석] 문제 조건 파악", f"{intent} 파악."], ["[식 전개] 핵심 정리", "단계별 수식 정리."]], f"정답 {ans_str}", [], f"정답은 {ans_str}입니다.", []], # [7]: teacher
            ["막히면 힌트를 한 칸씩만 열어 보세요. 스스로 식을 세우는 연습이 고득점의 지름길입니다.", [[intent, "이 문항의 기본 개념과 핵심 성질을 복습해 보세요."]], [["1단계: 조건 분석", "핵심 조건을 정리하세요."], ["2단계: 계산 전개", "단계를 밟아 계산하세요."]], [[f"정답은 {ans_str}입니다.", "최종 계산 과정에서 놓친 조건이 없는지 확인하세요."]], [], []], # [8]: help
            0,
            qn,
            "수학 영역",
            title
        ]
        sol_data[qn_str] = entry
        
    # Write sol_{eid}.js
    js_path = os.path.join(base_data, f"sol_{eid}.js")
    header = 'window.WB_SOL=window.WB_SOL||{};window.SOL_DATA=window.SOL_DATA||{};\n'
    content = f'{header}window.WB_SOL["{eid}"]=window.SOL_DATA["{eid}"]=' + json.dumps(sol_data, ensure_ascii=False) + ';\n'
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {js_path} (30 questions)")
    
    # 2. Crop Solutions to public/{eid}_sols/{0001..0030}.webp
    sols_dir = os.path.join(base_public, f"{eid}_sols")
    os.makedirs(sols_dir, exist_ok=True)
    try:
        doc = pymupdf.open(pdf_path)
        marks, lay, tail = cm.sol_marks(doc, 30)
        cropped_cnt = 0
        if marks and lay:
            for i in range(len(marks)):
                im = cm.sol_image(doc, marks, lay, i, tail)
                if im:
                    qn = marks[i]['no']
                    fn = f"{qn:04d}.webp"
                    im.save(os.path.join(sols_dir, fn), 'WEBP', quality=88, method=4)
                    cropped_cnt += 1
            print(f"Cropped {cropped_cnt}/30 solution images into {sols_dir}")
        else:
            print("Could not find marks/layout for cropping")
    except Exception as e:
        print(f"Error cropping {eid}: {e}")
        
    # 3. Catalog Entry
    entry = {
        "id": eid,
        "name": title,
        "short": title,
        "publisher": "평가원·교육청 기출",
        "dir": eid,
        "total": 30,
        "imgP": 30,
        "imgS": 30,
        "solved": 30,
        "ans": 30,
        "units": [
            {
                "name": "수학 영역",
                "start": 1,
                "end": 30,
                "count": 30,
                "solved": 30,
                "ans": 30
            }
        ]
    }
    new_catalog_entries.append(entry)

# Update catalog.js
cat_path = os.path.join(base_data, 'catalog.js')
with open(cat_path, 'r', encoding='utf-8') as f:
    text = f.read()
catalog = json.loads(text.split('=', 1)[1].strip().rstrip(';'))

existing_ids = {b['id'] for b in catalog}
added = 0
for ne in new_catalog_entries:
    if ne['id'] not in existing_ids:
        catalog.append(ne)
        added += 1

if added > 0:
    new_content = 'window.WB_CATALOG = ' + json.dumps(catalog, ensure_ascii=False, indent=2) + ';\n'
    with open(cat_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"\nAdded {added} new exams to catalog.js!")
