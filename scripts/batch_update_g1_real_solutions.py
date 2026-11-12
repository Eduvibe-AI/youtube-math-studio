import os
import sys
import glob
import re
import json
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

# PUA Decode map
PUA_MAP = {
    # Digits
    0xE034: '1', 0xE035: '2', 0xE036: '3', 0xE037: '4', 0xE038: '5',
    0xE039: '6', 0xE03A: '7', 0xE03B: '8', 0xE03C: '9', 0xE03D: '0',
    # Lowercase
    0xE0E5: 'a', 0xE0E6: 'b', 0xE0E7: 'c', 0xE0E8: 'd', 0xE0E9: 'e',
    0xE0EA: 'f', 0xE0EB: 'g', 0xE0EC: 'h', 0xE0ED: 'i', 0xE0EE: 'j',
    0xE0EF: 'm', 0xE0F0: 'n', 0xE0F1: 't', 0xE0F2: 'k', 0xE0F3: 'l',
    0xE0F4: 'p', 0xE0F5: 'q', 0xE0F6: 'r', 0xE0F7: 's', 0xE0F8: 't',
    0xE0F9: 'u', 0xE0FA: 'v', 0xE0FB: 'w', 0xE0FC: 'x', 0xE0FD: 'y', 0xE0FE: 'z',
    # Uppercase
    0xE000: 'A', 0xE001: 'B', 0xE002: 'C', 0xE003: 'D', 0xE004: 'E',
    0xE005: 'F', 0xE006: 'G', 0xE007: 'H', 0xE008: 'I', 0xE009: 'J',
    0xE00A: 'K', 0xE00B: 'L', 0xE00C: 'M', 0xE00D: 'N', 0xE00E: 'O',
    0xE00F: 'P', 0xE010: 'Q', 0xE011: 'R', 0xE012: 'S', 0xE013: 'T',
    0xE014: 'U', 0xE015: 'V', 0xE016: 'W', 0xE017: 'X', 0xE018: 'Y', 0xE019: 'Z',
    # Operators
    0xE044: '(', 0xE045: ')', 0xE046: '-', 0xE047: '=', 0xE048: '+',
    0xE049: '*', 0xE04A: '/', 0xE04B: '{', 0xE04C: '}', 0xE04D: '|',
    0xE055: '<', 0xE056: '>', 0xE05C: '√', 0xE06D: '/',
    0xE101: '±', 0x2212: '-', 0x2264: '≤', 0x2265: '≥', 0x2260: '≠',
    0x221A: '√', 0x00B7: '·', 0x00D7: '×', 0x00F7: '÷'
}

def decode_pua(text):
    if not text: return ""
    res = []
    for c in text:
        code = ord(c)
        if code in PUA_MAP:
            res.append(PUA_MAP[code])
        elif 0xE034 <= code <= 0xE03D:
            res.append(str((code - 0xE034 + 1) % 10))
        elif 0xE0E5 <= code <= 0xE0FE:
            res.append(chr(ord('a') + (code - 0xE0E5)))
        elif 0xE000 <= code <= 0xE019:
            res.append(chr(ord('A') + (code - 0xE000)))
        elif 0xe000 <= code <= 0xf8ff:
            res.append(' ')
        else:
            res.append(c)
    return "".join(res)

def parse_sol_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text() + "\n"
        
    full_text = decode_pua(full_text)
    
    # Answers
    answers = {}
    ans_m = re.findall(r'(\b\d{1,2}\b)\s*[\n\r]+\s*([①②③④⑤]|\d{1,4})', full_text)
    for qn, ans in ans_m:
        qn_i = int(qn)
        if 1 <= qn_i <= 30 and qn_i not in answers:
            answers[qn_i] = ans
            
    # Explanations
    # Support multiple formats: [출제의도], 출제의도, 경북교육청(1. 계산 능력 ...)
    sols = {}
    pattern = r'(?:^|\n)\s*(\d{1,2})\.\s*(?:\[\s*출제의도\s*\]|출제의도|\w+\s*능력\s*-\s*[^ \n\r]+)(.*?)(?=(?:^|\n)\s*\d{1,2}\.\s*(?:\[\s*출제의도\s*\]|출제의도|\w+\s*능력\s*-\s*[^ \n\r]+)|\Z)'
    matches = re.findall(pattern, full_text, re.DOTALL)
    for qn, body in matches:
        qn_i = int(qn)
        if 1 <= qn_i <= 30 and qn_i not in sols:
            lines = [ln.strip() for ln in body.strip().split('\n') if ln.strip()]
            intent = lines[0] if lines else f"{qn_i}번 핵심 개념"
            explanation = "\n".join(lines[1:]) if len(lines) > 1 else ""
            sols[qn_i] = {
                'intent': intent.strip(),
                'text': explanation.strip()
            }
            
    return answers, sols

def split_into_steps(intent, sol_text, ans_str, qn):
    lines = [ln.strip() for ln in sol_text.split('\n') if ln.strip()]
    if len(lines) <= 2:
        step1_body = f"[{intent}]\n" + "\n".join(lines)
        step2_body = f"위의 식을 계산하여 정리하면 정답은 {ans_str}입니다."
        return [
            ["1단계: 문제 조건 분석 및 식 전개", step1_body],
            ["2단계: 정답 도출 및 계산 검증", step2_body]
        ]
        
    last_idx = -1
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].startswith('따라서') or lines[i].startswith('그러므로') or lines[i].startswith('즉,') or '정답' in lines[i]:
            last_idx = i
            break
            
    if last_idx != -1 and last_idx > 1:
        step1_lines = lines[:(last_idx // 2)]
        step2_lines = lines[(last_idx // 2):last_idx]
        step3_lines = lines[last_idx:]
    else:
        n = len(lines)
        p1 = max(1, n // 3)
        p2 = max(p1 + 1, (2 * n) // 3)
        step1_lines = lines[:p1]
        step2_lines = lines[p1:p2]
        step3_lines = lines[p2:]
        
    s1 = f"[{intent}]\n" + "\n".join(step1_lines)
    s2 = "\n".join(step2_lines)
    s3 = "\n".join(step3_lines)
    if not any(ans_str in ln for ln in step3_lines):
        s3 += f"\n따라서 최종 정답은 {ans_str}입니다."
        
    return [
        ["1단계: 핵심 조건 및 식 설정", s1],
        ["2단계: 논리적 식 전개 및 성질 적용", s2],
        ["3단계: 정답 도출 및 결론", s3]
    ]

# Mapping exams
EXAM_MAP = [
    # 2021
    ('mock_8103', '2021 3월 고1 전국연합학력평가 정답해설.pdf'),
    ('mock_8106', '2021 6월 고1 전국연합학력평가 수학 정답해설.pdf'),
    ('mock_8109', '2021 9월 고1 전국연합학력평가 수학 정답및해설.pdf'),
    ('mock_8111', '2021 11월 고1 전국연합학력평가 정답및해설.pdf'),
    # 2022
    ('mock_8203', '2022 3월 고1 전국연합학력평가 정답해설.pdf'),
    ('mock_8206', '2022년 6월 고1 전국연합학력평가 수학 정답해설.pdf'),
    ('mock_8209', '2022 9월 고1 전국연합학력평가 수학 정답및해설.pdf'),
    ('mock_8211', '2022 11월 고1 전국연합학력평가 정답해설.pdf'),
    # 2024
    ('mock_8403', '2024 3월 고1 전국연합학력평가 정답해설(전체).pdf'),
    ('mock_8406', '2024 6월 고1 전국연합학력평가 정답해설.pdf'),
    ('mock_8409', '2024학년도 9월 고1 전국연합학력평가 정답 및 해설.pdf'),
    ('mock_8410', '2024학년도 10월 고1 전국연합학력평가 수학 해설지.pdf'),
    # 2025
    ('mock_8506', '2025 6월 고1 전국연합학력평가 수학 해설지.pdf'),
    ('mock_8509', '2025 9월 고1 전국연합학력평가 수학 정답해설.pdf'),
    ('mock_8510', '2025학년도 10월 고1 전국연합학력평가 수학 정답 및 해설.pdf'),
    # 2026
    ('mock_8603', '2026 3월 고1 전국연합학력평가 수학 정답 및 해설.pdf'),
    ('mock_8606', '2026학년도 6월 고1 전국연합학력평가 수학 정답해설.pdf'),
    ('mock_8609', '2026학년도 9월 고1 전국연합학력평가 수학 정답해설.pdf'),
    ('mock_8610', '2026학년도 10월 고1 전국연합학력평가 수학 정답 및 해설.pdf'),
]

def run_all():
    dl_dir = os.path.expanduser('~/Downloads')
    base_data = '509-401-math--helper/public/workbook_data'
    
    total_exams = len(EXAM_MAP)
    success_exams = 0
    total_questions_updated = 0
    
    print(f"=== 고1 모의고사 실제 교육청 해설 일괄 전수 교체 시작 ({total_exams}개 회차) ===")
    
    for eid, pdf_name in EXAM_MAP:
        pdf_path = os.path.join(dl_dir, pdf_name)
        js_path = os.path.join(base_data, f"sol_{eid}.js")
        
        if not os.path.exists(pdf_path):
            print(f"⚠️ PDF 파일 없음: {pdf_name}")
            continue
        if not os.path.exists(js_path):
            print(f"⚠️ JS 파일 없음: sol_{eid}.js")
            continue
            
        try:
            ans_dict, sols_dict = parse_sol_pdf(pdf_path)
            with open(js_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            prefix_match = re.search(rf'window\.WB_SOL\[[\'\"]{eid}[\'\"]\]\s*=\s*window\.SOL_DATA\[[\'\"]{eid}[\'\"]\]\s*=\s*', content)
            if not prefix_match:
                prefix_match = re.search(rf'window\.WB_SOL\[[\'\"]{eid}[\'\"]\]\s*=\s*', content)
            if not prefix_match:
                print(f"❌ Prefix match 실패: {eid}")
                continue
                
            prefix = prefix_match.group(0)
            raw_json = content[content.find(prefix) + len(prefix):].strip().rstrip(';')
            data = json.loads(raw_json)
            
            q_updated = 0
            for qn_str, entry in data.items():
                qn = int(qn_str)
                if qn in sols_dict:
                    sol_info = sols_dict[qn]
                    intent = sol_info['intent'] or f"{qn}번 핵심 개념"
                    sol_text = sol_info['text']
                    ans_str = entry[0]
                    
                    # [1]: 요약 풀이
                    first_line = sol_text.split('\n')[0] if sol_text else intent
                    entry[1] = f"{intent} — {first_line[:60]}"
                    
                    # [2]: 수험생 풀이 단계별 배열 교체
                    entry[2] = split_into_steps(intent, sol_text, ans_str, qn)
                    
                    # [8] 학습 도움 및 [7] 선생님 풀이는 절대 손대지 않고 100% 보존
                    q_updated += 1
                    
            # 백업 후 저장
            bak_path = js_path + '.bak'
            if not os.path.exists(bak_path):
                with open(bak_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
            header = 'window.WB_SOL=window.WB_SOL||{};window.SOL_DATA=window.SOL_DATA||{};\n'
            new_content = f'{header}{prefix}' + json.dumps(data, ensure_ascii=False) + ';\n'
            with open(js_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            success_exams += 1
            total_questions_updated += q_updated
            print(f"✅ [{eid}] {pdf_name[:30]}... -> {q_updated}/30 문항 실제 해설 교체 완료")
            
        except Exception as e:
            print(f"❌ [{eid}] 오류 발생: {e}")
            
    print("\n" + "=" * 60)
    print(f"🎉 고1 모의고사 실제 해설 일괄 교체 완료!")
    print(f"총 성공 회차: {success_exams}/{total_exams}")
    print(f"총 교체 문항 수: {total_questions_updated}문항")
    print("=" * 60)

if __name__ == '__main__':
    run_all()

