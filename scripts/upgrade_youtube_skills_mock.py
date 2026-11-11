import json
import os
import re

BASE_DIR = '509-401-math--helper/public/workbook_data'
TARGET_EXAMS = [
    'mock_y2025',  # 2025 수능
    'mock_2506',    # 2025 6모
    'mock_2509',    # 2025 9모
    'mock_2603',    # 2026 3월 학평
    'mock_2605',    # 2026 5월 학평
    'mock_2606',    # 2026 6모
    'mock_2607',    # 2026 7월 학평
    'mock_2609',    # 2026 9모
    'mock_2610'     # 2026 10월 학평
]

def clean_text(t):
    if not t: return ""
    t = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\1', str(t))
    t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', t)
    t = t.replace('⟹', ' \\implies ')
    t = t.replace('→', ' \\to ')
    t = t.replace('·', ' \\cdot ')
    t = t.replace('×', ' \\times ')
    t = t.replace('≤', ' \\le ')
    t = t.replace('≥', ' \\ge ')
    t = t.replace('≠', ' \\ne ')
    t = t.replace('√', '\\sqrt')
    t = t.replace('²', '^2')
    t = t.replace('³', '^3')
    t = t.replace('⁴', '^4')
    return t.strip()

SKILL_TEMPLATES = [
    {
        "id": "parabola_line_area",
        "name": "포물선과 직선의 넓이 공식",
        "match": lambda t: ("넓이" in t or "적분" in t or "둘러싸인" in t) and ("이차" in t or "포물선" in t or "x^2" in t or "x²" in t or "ax^2" in t),
        "board_item": ["[실전 공식] $S = \\dfrac{|a|}{6}(\\beta-\\alpha)^3$", "포물선과 직선이 둘러싼 넓이 초고속 계산."],
        "goal_suffix": " [유튜브 실전 개념] 포물선-직선 넓이 공식 $S=\\dfrac{|a|}{6}(\\beta-\\alpha)^3$으로 적분 계산 없이 초고속으로 해결할 수 있습니다.",
        "question": "포물선과 직선이 이루는 넓이 공식 $S=\\dfrac{|a|}{6}(\\beta-\\alpha)^3$에서 $\\alpha, \\beta$는 어떤 값인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>포물선과 직선이 이루는 넓이 공식:</b><br>이차함수 $y=ax^2+\\cdots$과 직선의 두 교점이 $\\alpha, \\beta$일 때 둘러싸인 넓이는 항상 $S=\\dfrac{|a|}{6}(\\beta-\\alpha)^3$ 입니다.<br>복잡한 정적분 전개 없이 두 근의 차이만으로 초고속 계산이 가능합니다."
        }
    },
    {
        "id": "parabola_two_tangents",
        "name": "포물선과 두 접선의 넓이 공식",
        "match": lambda t: ("넓이" in t or "둘러싸인" in t) and ("두 접선" in t or ("접선" in t and ("대칭" in t or "y축" in t))),
        "board_item": ["[실전 공식] $S = \\dfrac{|a|}{12}(\\beta-\\alpha)^3$", "포물선과 두 접선 사이의 넓이 공식."],
        "goal_suffix": " [유튜브 실전 개념] 포물선-두 접선 넓이 공식 $S=\\dfrac{|a|}{12}(\\beta-\\alpha)^3$을 적용해 단 3초 만에 답을 도출합니다.",
        "question": "포물선과 두 접선 사이의 넓이 공식의 분모는 6이 아닌 12인 이유를 설명할 수 있나요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>이차함수와 접선의 넓이 공식:</b><br>포물선 $y=ax^2+\\cdots$과 두 접선으로 둘러싸인 넓이는 항상 $S=\\dfrac{|a|}{12}(\\beta-\\alpha)^3$ 입니다.<br>두 접점의 $x$좌표 $\\alpha, \\beta$만 알면 적분 없이 즉시 해결됩니다."
        }
    },
    {
        "id": "cubic_tangent_area",
        "name": "삼차함수와 접선의 넓이 공식",
        "match": lambda t: ("삼차" in t or "x^3" in t or "x³" in t) and ("접선" in t) and ("넓이" in t or "둘러싸인" in t),
        "board_item": ["[실전 공식] $S = \\dfrac{|a|}{12}(\\beta-\\alpha)^4$", "삼차함수와 접선 사이의 넓이 공식."],
        "goal_suffix": " [유튜브 실전 개념] 삼차함수-접선 넓이 공식 $S=\\dfrac{|a|}{12}(\\beta-\\alpha)^4$로 적분 계산을 한 번에 생략합니다.",
        "question": "삼차함수와 접선이 둘러싼 넓이를 구할 때 공식 $S=\\dfrac{|a|}{12}(\\beta-\\alpha)^4$의 차수는 왜 4제곱일까요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>삼차함수와 접선의 넓이 공식:</b><br>삼차함수 $y=ax^3+\\cdots$과 접점 $\\alpha$, 다른 한 교점 $\\beta$ 사이의 둘러싸인 넓이는 $S=\\dfrac{|a|}{12}(\\beta-\\alpha)^4$ 입니다.<br>전개 및 부정적분 계산을 단숨에 줄여줍니다."
        }
    },
    {
        "id": "cubic_ratio",
        "name": "삼차함수 비율 관계 (2:1 및 1:루트3)",
        "match": lambda t: ("삼차" in t or "x^3" in t or "x³" in t or "3차" in t) and ("극대" in t or "극소" in t or "변곡" in t or "극값" in t or "접선" in t),
        "board_item": ["[비율 관계] $2:1$ / $1:\\sqrt{3}$", "극대·극소·변곡점의 황금 비율 법칙."],
        "goal_suffix": " [유튜브 실전 개념] 삼차함수 극값과 변곡점의 $2:1$ 및 $1:\\sqrt{3}$ 비율 관계로 식 전개 없이 좌표를 확정합니다.",
        "question": "삼차함수에서 극대점을 지나는 접선과 곡선이 만나는 다른 교점 사이의 비율 관계는 몇 대 몇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>삼차함수의 황금 비율 관계:</b><br>1) <b>극대-극소-교점 $2:1$ 법칙:</b> 극대(소)점을 지나는 접선과 다른 교점 사이의 비는 접점 쪽이 $2$, 교점 쪽이 $1$입니다.<br>2) <b>변곡점 대칭 $1:\\sqrt{3}$ 법칙:</b> 변곡점을 지나는 수평선과의 교점과 극값의 거리는 $1:\\sqrt{3}$입니다.<br>도함수 연립 없이 눈으로 바로 $x$좌표를 구할 수 있습니다."
        }
    },
    {
        "id": "quartic_ratio",
        "name": "사차함수 비율 관계 (3:1 및 1:루트2)",
        "match": lambda t: ("사차" in t or "x^4" in t or "x⁴" in t or "4차" in t) and ("극대" in t or "극소" in t or "접선" in t or "극값" in t),
        "board_item": ["[사차함수 비율] $3:1$ / $1:\\sqrt{2}$", "극대·극소 대칭 분할 비율 법칙."],
        "goal_suffix": " [유튜브 실전 개념] 사차함수의 $3:1$ 접선 비율 관계를 활용하여 미지수를 즉시 결정합니다.",
        "question": "사차함수에서 삼중근을 갖는 접선과 다른 교점 사이의 분할 비율은 어떻게 되나요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>사차함수의 실전 비율 관계:</b><br>• 삼중근 접선과 다른 교점의 분할비는 $3:1$입니다.<br>• 좌우 대칭인 W자형 사차함수에서 극대와 극소 사이 거리와 극대-교점 거리 비는 $1:\\sqrt{2}$입니다."
        }
    },
    {
        "id": "lhopital",
        "name": "0/0꼴 부정형 로피탈의 정리",
        "match": lambda t: ("lim" in t or "극한" in t or "x\\to" in t or "h\\to" in t or "x→" in t) and ("0/0" in t or "할선" in t or "미분계수" in t or "분수" in t),
        "board_item": ["[실전 팁] $\\lim \\dfrac{f(x)}{g(x)} = \\lim \\dfrac{f'(x)}{g'(x)}$", "0/0 꼴 극한에서 로피탈 미분 적용."],
        "goal_suffix": " [유튜브 실전 개념] 0/0 꼴 극한에서 로피탈의 정리를 적용해 복잡한 유리화/인수분해 없이 5초 만에 답을 구합니다.",
        "question": "0/0 꼴 극한에서 분모와 분자를 각각 미분하여 계산할 수 있는 정리의 이름은 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>0/0 꼴 극한 초고속 해결 (로피탈의 정리):</b><br>분모와 분자가 모두 $0$으로 갈 때, 인수분해나 복잡한 유리화 대신 분모와 분자를 각각 미분하여 $\\lim_{x\\to a}\\dfrac{f'(x)}{g'(x)}$로 계산하면 5초 만에 답이 나옵니다."
        }
    },
    {
        "id": "trig_approx",
        "name": "삼각함수/초월함수 테일러 근사",
        "match": lambda t: ("sin" in t or "tan" in t or "cos" in t) and ("lim" in t or "극한" in t or "\\to 0" in t),
        "board_item": ["[실전 근사] $\\sin\\theta \\approx \\theta,\\; 1-\\cos\\theta \\approx \\dfrac{1}{2}\\theta^2$", "x→0 극한에서 다항식 근사 치환."],
        "goal_suffix": " [유튜브 실전 개념] $\\sin x \\approx x$, $1-\\cos x \\approx \\dfrac{1}{2}x^2$ 실전 근사로 삼각함수 도형의 극한을 3초 만에 풉니다.",
        "question": "x가 0으로 갈 때 1-cos(x)는 다항식 몇 차식으로 근사할 수 있나요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>삼각함수 도형 극한의 실전 근사 공식:</b><br>$\\theta \\to 0$일 때:<br>• $\\sin\\theta \\approx \\theta$<br>• $\\tan\\theta \\approx \\theta$<br>• $1 - \\cos\\theta \\approx \\dfrac{1}{2}\\theta^2$<br>복잡한 덧셈정리 변형 없이 다항식 차수와 계수만 비교하여 즉시 정답을 구할 수 있습니다."
        }
    },
    {
        "id": "arithmetic_sn",
        "name": "등차수열의 합과 이차함수 대칭성",
        "match": lambda t: ("등차" in t) and ("합" in t or "Sn" in t or "S_" in t),
        "board_item": ["[실전 개념] $S_n = An^2+Bn \\implies d=2A$", "등차수열의 합은 원점을 지나는 이차함수."],
        "goal_suffix": " [유튜브 실전 개념] 등차수열의 합 $S_n$의 이차함수 대칭축과 공차 $d=2A$ 성질을 활용해 빠르게 해결합니다.",
        "question": "등차수열의 합 Sn을 n에 대한 이차식으로 보았을 때, 이차항 계수와 공차의 관계는 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>등차수열의 합과 이차함수 스킬:</b><br>등차수열의 합 $S_n$은 상수항이 없는 $n$에 대한 이차식 $S_n = \\dfrac{d}{2}n^2 + \\cdots$ 입니다.<br>이차항의 계수의 2배가 곧 공차 $d$가 되며, 대칭축 $n=-\\dfrac{B}{2A}$ 근처의 자연수에서 $S_n$의 최댓값/최솟값이 발생합니다."
        }
    },
    {
        "id": "symmetry_integral",
        "name": "우함수/기함수 대칭 정적분 소거법",
        "match": lambda t: ("대칭" in t or "기함수" in t or "우함수" in t or "f(-x)" in t) and ("적분" in t or "넓이" in t),
        "board_item": ["[실전 대칭] $\\int_{-a}^a f_{odd}(x)dx = 0$", "대칭 구간 적분에서 홀수차항 즉시 소거."],
        "goal_suffix": " [유튜브 실전 개념] 대칭 구간 적분에서 기함수 항을 선제 소거하고 우함수만 $2\\int_0^a$로 계산량을 절반으로 줄입니다.",
        "question": "[-a, a] 구간의 정적분에서 기함수 항의 적분값이 0이 되는 원리는 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>우함수·기함수 대칭 정적분 스킬:</b><br>대칭 구간 $[-a, a]$ 적분에서:<br>• 홀수차 다항식(기함수)은 적분값이 무조건 $0$이므로 계산 전 먼저 지웁니다.<br>• 짝수차 다항식(우함수)은 $2\\int_0^a$로 바꾸어 $0$을 대입해 계산 시간을 반으로 줄입니다."
        }
    }
]

def clean_board_item(write_text, say_text):
    w = clean_text(str(write_text))
    s = clean_text(str(say_text))
    s = re.sub(r'^[1-9]단계[:\s]*', '', s).strip()

    # If write_text is already an injected clean skill item, keep it
    if w.startswith('[실전') or w.startswith('[비율') or w.startswith('[사차'):
        return [w, s]

    # Split lines
    raw_lines = [l.strip() for l in w.split('\n') if l.strip()]
    if not raw_lines:
        return [w, s]

    # If first line has lots of Korean text + formula at the end
    # e.g., "f(1) = f(2) = 0 이고 최고차항의 계수가 1 이므로 다음과 같이 놓는다.f(x) = (x − 1)(x − 2)(x − c)"
    # Extract the purest formula line
    best_math = None
    best_note = None

    for line in raw_lines:
        # Check if line contains inline Korean text glued with math
        # Try to find formula block
        match_eq = re.search(r'([a-zA-Z0-9\(\)\\\^+\-=/_\s]+(?:=|\\implies|\\le|\\ge)[a-zA-Z0-9\(\)\\\^+\-=/_\s]+)', line)
        if match_eq:
            cand = match_eq.group(1).strip()
            if len(cand) >= 4 and len(re.findall(r'[가-힣]', cand)) == 0:
                best_math = cand
                # The text before cand can be note
                prefix_text = line[:match_eq.start()].strip()
                if prefix_text and len(re.findall(r'[가-힣]', prefix_text)) >= 2:
                    best_note = prefix_text
                break

    if not best_math:
        # Just use the cleanest line
        best_math = raw_lines[-1] if len(raw_lines) > 1 else raw_lines[0]

    # Strip Korean words from best_math if any
    best_math = re.sub(r'[가-힣]+', ' ', best_math).strip()
    best_math = re.sub(r'\s{2,}', ' ', best_math)

    if not s:
        s = best_note if best_note else "단계별 식 전개 및 계산."

    # If best_math is purely formula, wrap in $...$
    if best_math and not best_math.startswith('$') and ('=' in best_math or '\\' in best_math or '^' in best_math or '+' in best_math or '-' in best_math):
        best_math = f"${best_math}$"

    if not best_math:
        best_math = clean_text(raw_lines[0])

    return [best_math, s]

def polish_board(board, matched_skill=None):
    new_board = []
    for item in board:
        if not isinstance(item, (list, tuple)) or len(item) < 1:
            continue
        cleaned = clean_board_item(item[0], item[1] if len(item) > 1 else "")
        new_board.append(cleaned)

    if matched_skill:
        skill_item = matched_skill["board_item"]
        already_has = any(skill_item[0] in b[0] for b in new_board)
        if not already_has:
            if len(new_board) > 1:
                new_board.insert(-1, skill_item)
            else:
                new_board.append(skill_item)

    return new_board

def process_exam(tid):
    path = os.path.join(BASE_DIR, f'sol_{tid}.js')
    if not os.path.exists(path):
        return 0, 0

    content = open(path, encoding='utf-8').read()

    m = re.search(r'=\s*(\{"\d+":.*?\});?\s*$', content, re.DOTALL)
    if not m:
        idx = content.find('{"1":')
        if idx == -1: idx = content.find('{"0001":')
        if idx == -1: return 0, 0
        json_str = content[idx:].rstrip().rstrip(';')
        prefix = content[:idx]
        suffix = ';\n'
    else:
        json_str = m.group(1)
        prefix = content[:m.start(1)]
        suffix = content[m.end(1):]

    data = json.loads(json_str)

    updated_count = 0
    skill_applied_count = 0

    for qid, entry in data.items():
        if not isinstance(entry, list) or len(entry) < 8:
            continue

        full_text = clean_text(json.dumps(entry, ensure_ascii=False))

        matched_skill = None
        for tmpl in SKILL_TEMPLATES:
            if tmpl["match"](full_text):
                matched_skill = tmpl
                break

        teacher = entry[7]
        if not isinstance(teacher, list) or len(teacher) < 2:
            continue

        goal = teacher[0] if len(teacher) > 0 else ""
        board = teacher[1] if len(teacher) > 1 else []
        questions = teacher[3] if len(teacher) > 3 else []
        extras = teacher[5] if len(teacher) > 5 else []

        new_board = polish_board(board, matched_skill)
        teacher[1] = new_board

        if matched_skill:
            skill_applied_count += 1
            if matched_skill["goal_suffix"] not in goal:
                teacher[0] = clean_text(goal) + matched_skill["goal_suffix"]

            q_text = matched_skill["question"]
            if not isinstance(questions, list): questions = []
            if not any(q_text in q for q in questions):
                questions.append(q_text)
            teacher[3] = questions

            if not isinstance(extras, list): extras = []
            extra_card = matched_skill["extra"]
            if not any(e.get("type") == extra_card["type"] for e in extras if isinstance(e, dict)):
                extras.insert(0, extra_card)
            teacher[5] = extras

        entry[7] = teacher
        updated_count += 1

    new_json_str = json.dumps(data, ensure_ascii=False)
    new_content = prefix + new_json_str + suffix
    open(path, 'w', encoding='utf-8').write(new_content)

    print(f"[{tid}] Processed {updated_count} questions (Skills applied: {skill_applied_count})")
    return updated_count, skill_applied_count

def main():
    total_q = 0
    total_skills = 0
    print(f"Executing clean YouTube skill expansion across {len(TARGET_EXAMS)} exams...")
    for tid in TARGET_EXAMS:
        q, s = process_exam(tid)
        total_q += q
        total_skills += s
    print(f"\nFinal Complete! Total questions: {total_q}, Total YouTube skills: {total_skills}")

if __name__ == '__main__':
    main()
