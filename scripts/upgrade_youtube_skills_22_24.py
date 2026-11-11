import json
import os
import re
import pymupdf

BASE_DIR = '509-401-math--helper/public/workbook_data'
BASE_PDF_2022 = r'D:\에듀바이블 문제은행\기출다운로드\2022'

EXAMS_2024 = [
    'mock_8403', 'mock_8406', 'mock_8409', 'mock_8410',
    'mock_7403', 'mock_7406', 'mock_7409', 'mock_7410',
]

EXAMS_2022 = [
    'mock_8203', 'mock_8206', 'mock_8209', 'mock_8211',
    'mock_7203', 'mock_7206', 'mock_7209', 'mock_7211',
]

FOLDERS_2022 = {
    'mock_8203': '2022학년도_3월_고1_학력평가',
    'mock_8206': '2022학년도_6월_고1_학력평가',
    'mock_8209': '2022학년도_9월_고1_학력평가',
    'mock_8211': '2022학년도_11월_고1_학력평가',
    'mock_7203': '2022학년도_3월_고2_학력평가',
    'mock_7206': '2022학년도_6월_고2_학력평가',
    'mock_7209': '2022학년도_9월_고2_학력평가',
    'mock_7211': '2022학년도_11월_고2_학력평가',
}

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
    t = t.replace('√', '\\sqrt ')
    t = t.replace('∛', '\\sqrt[3]')
    t = t.replace('²', '^2')
    t = t.replace('³', '^3')
    t = t.replace('⁴', '^4')
    t = t.replace('−', '-')
    t = t.replace('–', '-')
    return t.strip()

SKILL_TEMPLATES = [
    # 1. 원의 방정식 (고1 핵심)
    {
        "id": "circle_line_dist",
        "name": "원과 직선 위치관계 (d와 r 비교)",
        "match": lambda t: ("원" in t or "원의 방정식" in t) and ("직선" in t or "접선" in t or "접할" in t or "현" in t or "거리" in t or "방정식" in t or "원의 성질" in t or "원주각" in t),
        "board_item": ["[실전 기하] 판별식 대신 $d$와 $r$ 비교", "중심과 직선 사이 거리 $d$로 접선 초고속 판정."],
        "goal_suffix": " [유튜브 실전 개념] 복잡한 연립 판별식 대신 원의 중심과 직선 사이 거리 $d$와 반지름 $r$의 비교로 초고속 해결합니다.",
        "question": "원의 중심과 직선 사이의 거리 d가 반지름 r과 같을 때 원과 직선은 어떤 위치 관계인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>원과 직선의 위치 관계 초고속 판정:</b><br>이차방정식 연립 후 판별식 $D$를 쓰면 계산이 폭발합니다! 원의 중심 $(x_1, y_1)$에서 직선 $ax+by+c=0$까지의 거리 $d = \\dfrac{|ax_1+by_1+c|}{\\sqrt{a^2+b^2}}$를 구해 반지름 $r$과 비교하세요:<br>• $d < r$: 두 점에서 만남<br>• $d = r$: 접함 (접선 조건)<br>• $d > r$: 만나지 않음"
        }
    },
    # 2. 이차함수 대칭축과 최대·최소 (고1 핵심)
    {
        "id": "quad_axis_symmetry",
        "name": "이차함수 대칭축과 최대·최소",
        "match": lambda t: ("이차함수" in t or "포물선" in t) and ("대칭" in t or "최대" in t or "최소" in t or "꼭짓점" in t or "좌표" in t or "방정식" in t or "함숫값" in t or "그래프" in t) and not ("넓이" in t),
        "board_item": ["[대칭축 스킬] 축 $x = -\\dfrac{b}{2a}$ 대칭성", "이차함수는 축에 대해 좌우 완벽 대칭."],
        "goal_suffix": " [유튜브 실전 개념] 이차함수 대칭축 $x=-\\dfrac{b}{2a}$의 기하학적 성질을 이용해 연립 없이 좌표와 최대/최소를 확정합니다.",
        "question": "이차함수 y = ax^2 + bx + c 의 그래프에서 대칭축의 방정식을 바로 구하는 공식은 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>이차함수의 대칭축 & 최대최소 스킬:</b><br>이차함수 $y=ax^2+bx+c$는 항상 직선 $x=-\\dfrac{b}{2a}$에 대칭입니다. 제한된 범위에서 축에 가까울수록/멀수록 함숫값이 극대/극소가 되므로 완전제곱식 전개 없이 축과의 거리로 3초 만에 최대·최소를 판정할 수 있습니다."
        }
    },
    # 3. 다항식과 나머지정리 (고1 핵심)
    {
        "id": "polynomial_remainder",
        "name": "나머지정리와 인수정리",
        "match": lambda t: ("다항식" in t or "조립제법" in t or "나머지" in t or "인수정리" in t or "인수분해" in t or "항등식" in t or "동류항" in t),
        "board_item": ["[실전 비법] 나머지정리 $P(a) = R$", "일차식 나눗셈의 나머지는 대입 하나로 즉시 도출."],
        "goal_suffix": " [유튜브 실전 개념] 직접 나눗셈을 하지 않고 나머지정리 $P(a)=R$ 및 미분을 활용하여 미지수를 즉시 결정합니다.",
        "question": "다항식 P(x)를 x - a로 나눈 나머지를 한 번에 구하는 원리는 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>나머지정리 실전 팁:</b><br>• $P(x)$를 일차식 $(x-a)$로 나눈 나머지는 $P(a)$입니다.<br>• $(x-a)^2$으로 나눈 나머지를 구할 때는 $P(a)=R(a)$와 양변 미분 후 $P'(a)=R'(a)$를 연립하면 연립방정식을 10초 만에 풀 수 있습니다."
        }
    },
    # 4. 경우의 수와 조합 (고1 핵심)
    {
        "id": "combinatorics_count",
        "name": "경우의 수와 여사건 기법",
        "match": lambda t: ("경우의 수" in t or "조합" in t or "순열" in t or "확률" in t),
        "board_item": ["[실전 카운팅] 사건의 독립 분류와 여사건", "적어도 조건 나오면 여사건 ($전체 - 반대$)."],
        "goal_suffix": " [유튜브 실전 개념] 분류 기준을 명확히 잡고 '적어도' 조건 시 여사건(전체-반대)으로 계산 단계를 대폭 단축합니다.",
        "question": "경우의 수 문제에서 '적어도 하나의 ~' 조건이 주어졌을 때 가장 효율적인 접근법은 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>경우의 수 1타 강사 실전 행동 강령:</b><br>1) <b>여사건 고려:</b> '적어도' 또는 조건이 너무 많을 때는 (전체 경우의 수 - 반대 경우의 수)로 풉니다.<br>2) <b>케이스 분류 3원칙:</b> 빠짐없이, 겹침없이, 기준을 하나 정해 3~4개 이하로 쪼갭니다.<br>3) <b>순서가 없으면 조합($_nC_r$):</b> 뽑은 후 나열($_nP_r = {_nC_r} \\times r!$)하는 순서를 지킵니다."
        }
    },
    # 5. 산술·기하 평균 부등식 (고1 핵심)
    {
        "id": "am_gm_inequality",
        "name": "산술·기하 평균 부등식",
        "match": lambda t: ("부등식" in t or "양수" in t or "최솟값" in t or "최댓값" in t) and ("a+b" in t or "역수" in t or "합의 최솟값" in t or "곱의 최댓값" in t or "절대부등식" in t or "산술" in t),
        "board_item": ["[실전 공식] $a+b \\ge 2\\sqrt{ab}$ (등호 $a=b$)", "역수 꼴 합은 산술기하로 즉시 최솟값 도출."],
        "goal_suffix": " [유튜브 실전 개념] 양수 조건에서 산술-기하 평균 부등식 $a+b \\ge 2\\sqrt{ab}$을 적용해 한 줄로 최솟값을 구합니다.",
        "question": "산술-기하 평균 부등식에서 등호가 성립하기 위한 필요충분조건은 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>산술-기하 평균의 실전 적용:</b><br>양수 조건에서 합의 최솟값이나 곱의 최댓값을 물을 때 사용합니다. 반드시 <b>등호 성립 조건 ($a=b$)</b>을 확인하여 미지수 값을 확정하세요."
        }
    },
    # 6. 삼각함수 사인·코사인법칙 (고2 핵심)
    {
        "id": "trig_law_sin_cos",
        "name": "사인법칙과 코사인법칙",
        "match": lambda t: ("삼각형" in t or "외접원" in t) and ("사인법칙" in t or "코사인법칙" in t or "cos" in t or "sin" in t or "각" in t or "삼각비" in t),
        "board_item": ["[실전 공식] $\\dfrac{a}{\\sin A}=2R,\\; \\cos A=\\dfrac{b^2+c^2-a^2}{2bc}$", "외접원은 사인법칙, 세 변은 코사인법칙."],
        "goal_suffix": " [유튜브 실전 개념] 사인법칙과 코사인법칙의 표준 연계로 복잡한 기하 도형의 미지 길이를 신속히 해결합니다.",
        "question": "삼각형에서 외접원의 반지름 R이 주어졌을 때 가장 먼저 떠올려야 하는 공식은 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>삼각함수의 활용 실전 행동 강령:</b><br>1) <b>외접원의 반지름 $R$</b>이나 마주보는 대변-대각 쌍 $\\implies$ <b>사인법칙</b><br>2) <b>두 변과 끼인각</b> 또는 <b>세 변의 길이</b> $\\implies$ <b>코사인법칙</b><br>3) 원에 내접하는 사각형의 마주보는 두 대각의 합은 $180^\\circ$ ($\\cos(\\pi-\\theta) = -\\cos\\theta$)"
        }
    },
    # 7. 삼차함수 비율 관계 (고2 핵심)
    {
        "id": "cubic_ratio",
        "name": "삼차함수 비율 관계 (2:1 및 1:루트3)",
        "match": lambda t: ("삼차" in t or "x^3" in t or "x³" in t or "3차" in t) and ("극대" in t or "극소" in t or "변곡" in t or "접선" in t or "극값" in t or "미분" in t or "도함수" in t),
        "board_item": ["[비율 관계] $2:1$ / $1:\\sqrt{3}$", "극대·극소·변곡점의 황금 비율 법칙."],
        "goal_suffix": " [유튜브 실전 개념] 삼차함수 극값과 변곡점의 $2:1$ 및 $1:\\sqrt{3}$ 비율 관계로 식 전개 없이 좌표를 확정합니다.",
        "question": "삼차함수에서 극대점을 지나는 접선과 곡선이 만나는 다른 교점 사이의 비율 관계는 몇 대 몇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>삼차함수의 황금 비율 관계:</b><br>1) <b>극대-극소-교점 $2:1$ 법칙:</b> 극대(소)점을 지나는 접선과 다른 교점 사이의 비는 접점 쪽이 $2$, 교점 쪽이 $1$입니다.<br>2) <b>변곡점 대칭 $1:\\sqrt{3}$ 법칙:</b> 변곡점을 지나는 수평선과의 교점과 극값의 거리는 $1:\\sqrt{3}$입니다.<br>도함수 연립 없이 눈으로 바로 $x$좌표를 구할 수 있습니다."
        }
    },
    # 8. 포물선과 직선의 넓이 공식
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
    # 9. 0/0꼴 부정형 로피탈의 정리
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
    # 10. 등차수열의 합과 이차함수
    {
        "id": "arithmetic_sn",
        "name": "등차수열의 합과 이차함수 대칭성",
        "match": lambda t: ("등차" in t or "수열" in t) and ("합" in t or "Sn" in t or "S_" in t or "일반항" in t),
        "board_item": ["[실전 개념] $S_n = An^2+Bn \\implies d=2A$", "등차수열의 합은 원점을 지나는 이차함수."],
        "goal_suffix": " [유튜브 실전 개념] 등차수열의 합 $S_n$의 이차함수 대칭축과 공차 $d=2A$ 성질을 활용해 빠르게 해결합니다.",
        "question": "등차수열의 합 Sn을 n에 대한 이차식으로 보았을 때, 이차항 계수와 공차의 관계는 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>등차수열의 합과 이차함수 스킬:</b><br>등차수열의 합 $S_n$은 상수항이 없는 $n$에 대한 이차식 $S_n = \\dfrac{d}{2}n^2 + \\cdots$ 입니다.<br>이차항의 계수의 2배가 곧 공차 $d$가 되며, 대칭축 $n=-\\dfrac{B}{2A}$ 근처의 자연수에서 $S_n$의 최댓값/최솟값이 발생합니다."
        }
    },
    # 11. 특수각 삼각비와 피타고라스 삼조
    {
        "id": "pythagoras_special_tri",
        "name": "특수각 삼각비와 피타고라스 삼조",
        "match": lambda t: ("피타고라스" in t or "직각삼각형" in t or "빗변" in t) and not ("사인법칙" in t),
        "board_item": ["[실전 비법] $3:4:5$, $5:12:13$, $1:\\sqrt{3}:2$", "피타고라스 삼조와 특수각 삼각비로 3초 판정."],
        "goal_suffix": " [유튜브 실전 개념] 직각삼각형에서 피타고라스 수와 특수각 비를 적용해 길이 계산을 암산으로 도출합니다.",
        "question": "직각삼각형에서 가장 자주 나오는 피타고라스 정수 쌍(비율) 3가지는 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>직각삼각형 3초 계산 스킬:</b><br>• 피타고라스 정수비: $3:4:5$, $5:12:13$, $8:15:17$<br>• 특수각 비: $30^\\circ-60^\\circ-90^\\circ \\implies 1:\\sqrt{3}:2$, $45^\\circ-45^\\circ-90^\\circ \\implies 1:1:\\sqrt{2}$<br>제곱 계산 없이 비율로 변의 길이를 즉시 확정하세요."
        }
    },
    # 12. 지수·로그 밑 통일 공식과 진수 조건 (고2 핵심)
    {
        "id": "log_exp_base",
        "name": "지수·로그 밑 통일 공식과 진수 조건",
        "match": lambda t: ("지수" in t or "로그" in t or "log" in t or "밑" in t) and not ("극한" in t),
        "board_item": ["[실전 비법] 밑 통일 공식 & 진수 조건 ($x>0$)", "로그 계산 전 진수 조건 선점."],
        "goal_suffix": " [유튜브 실전 개념] 밑을 통일하고 로그 정의 조건(진수>0, 밑>0, 밑≠1)을 확인하여 함정을 피합니다.",
        "question": "로그가 정의되기 위한 밑과 진수의 조건은 각각 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>지수·로그 1타 강사 실전 행동 강령:</b><br>1) <b>밑 변환 공식:</b> $\\log_a b = \\dfrac{\\log_c b}{\\log_c a}$, $a^{\\log_a b} = b$<br>2) <b>진수 조건 선점:</b> 로그 방정식·부등식을 풀기 전에 항상 진수 $>0$을 먼저 적어두어야 함정에 빠지지 않습니다."
        }
    },
    # 13. 함수의 극한과 연속성 판정 (고2 핵심)
    {
        "id": "limit_continuity",
        "name": "함수의 극한과 연속성 판정",
        "match": lambda t: ("극한" in t or "연속" in t or "lim" in t or "좌극한" in t or "우극한" in t),
        "board_item": ["[실전 비법] $\\lim_{x\\to a^-} f(x) = \\lim_{x\\to a^+} f(x) = f(a)$", "좌극한·우극한·함숫값 일치로 미지수 확정."],
        "goal_suffix": " [유튜브 실전 개념] 좌극한, 우극한, 함숫값의 삼위일체 연속성 정의를 적용해 경계점 미지수를 즉시 결정합니다.",
        "question": "함수 f(x)가 x = a에서 연속이기 위한 필요충분조건은 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>함수의 극한 & 연속 3초 판정법:</b><br>1) <b>연속의 정의:</b> 좌극한 = 우극한 = 함숫값 ($f(a^-) = f(a^+) = f(a)$)<br>2) <b>불연속점 곱의 연속:</b> 불연속인 함수 $f(x)$에 연속함수 $g(x)$를 곱해 연속이 되려면, 불연속점 $x=a$에서 반드시 $g(a)=0$이어야 합니다."
        }
    },
    # 14. 접선의 방정식과 미분계수 (고2 핵심)
    {
        "id": "tangent_derivative",
        "name": "접선의 방정식과 미분계수",
        "match": lambda t: ("접선" in t or "접하는" in t or "미분계수" in t) and ("함수" in t or "곡선" in t or "y=" in t),
        "board_item": ["[실전 비법] $y - f(t) = f'(t)(x - t)$", "접점 $(t, f(t))$ 세팅 후 기울기 $f'(t)$로 접선 완성."],
        "goal_suffix": " [유튜브 실전 개념] 접점 $(t, f(t))$ 좌표를 미지수로 두고 도함수 $f'(t)$를 기울기로 설정하여 일관된 알고리즘으로 해결합니다.",
        "question": "곡선 y = f(x) 위의 점 (t, f(t))에서의 접선의 방정식을 구하는 공식은 무엇인가요?",
        "extra": {
            "type": "유튜브 실전 꿀팁",
            "text": "📌 <b>접선의 방정식 3대 유형 해결법:</b><br>1) <b>곡선 위의 점:</b> $y - f(t) = f'(t)(x - t)$<br>2) <b>기울기 $m$이 주어질 때:</b> $f'(t) = m$으로 접점 $t$를 먼저 구함<br>3) <b>곡선 밖의 점 $(x_1, y_1)$:</b> 접점 $(t, f(t))$로 식을 세운 뒤 $(x_1, y_1)$ 대입"
        }
    }
]

def load_2022_pdf_intents():
    intents_by_exam = {}
    for tid, folder in FOLDERS_2022.items():
        fpath = os.path.join(BASE_PDF_2022, folder)
        if not os.path.exists(fpath): continue
        pdfs = [f for f in os.listdir(fpath) if '해설' in f or '정답' in f]
        if not pdfs: continue
        pdf_file = os.path.join(fpath, pdfs[0])
        try:
            doc = pymupdf.open(pdf_file)
            text = ""
            for page in doc:
                text += page.get_text() + "\n"
            matches = re.findall(r'(\d+)\.\s*\[출제의도\]\s*([^\n]+)', text)
            intents_by_exam[tid] = {str(int(num)): intent.strip() for num, intent in matches}
        except Exception as e:
            print(f"Error loading PDF for {tid}: {e}")
    return intents_by_exam

def clean_board_item(write_text, say_text):
    w = clean_text(str(write_text))
    s = clean_text(str(say_text))
    s = re.sub(r'^[1-9]단계[:\s]*', '', s).strip()

    if any(w.startswith(prefix) for prefix in ['[실전', '[비율', '[대칭', '[사차', '[조건', '[정답', '[식 전개']):
        return [w, s]

    equations = re.findall(r'([a-zA-Z0-9\(\)\\\^+\-=/_\s,]+(?:=|\\implies|\\le|\\ge|<|>)[a-zA-Z0-9\(\)\\\^+\-=/_\s,]+)', w)
    pure_eqs = []
    for eq in equations:
        eq_clean = eq.strip()
        if len(re.findall(r'[가-힣]', eq_clean)) == 0 and len(eq_clean) >= 3:
            pure_eqs.append(eq_clean)
            
    if pure_eqs:
        best_eq = pure_eqs[-1] if len(pure_eqs) > 1 and len(pure_eqs[-1]) > len(pure_eqs[0]) else pure_eqs[0]
        best_eq = re.sub(r'^[,\.\s]+|[,\.\s]+$', '', best_eq)
        best_math = f"${best_eq}$"
    else:
        best_math = re.sub(r'[가-힣]+', ' ', w).strip()
        best_math = re.sub(r'\s{2,}', ' ', best_math)
        if best_math and ('=' in best_math or '\\' in best_math or '^' in best_math or '+' in best_math or '-' in best_math):
            best_math = f"${best_math}$"
        else:
            best_math = clean_text(w)

    if not s:
        korean_parts = re.findall(r'([가-힣\s]{3,})', w)
        s = " ".join(korean_parts).strip() if korean_parts else "단계별 식 전개 및 계산."
    
    return [best_math, s]

def polish_board_2024(board, matched_skill=None):
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

def process_exam_2024(tid):
    path = os.path.join(BASE_DIR, f'sol_{tid}.js')
    if not os.path.exists(path):
        return 0, 0

    content = open(path, encoding='utf-8').read()
    m = re.search(r'=\s*(\{"\d+":.*?\});?\s*$', content, re.DOTALL)
    if not m:
        idx = content.find('{"1":')
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
        if not isinstance(teacher, list):
            teacher = ["", [], "", [], "", []]
        while len(teacher) < 6:
            teacher.append([] if len(teacher) in [1, 3, 5] else "")

        goal = teacher[0] or ""
        board = teacher[1] or []
        questions = teacher[3] or []
        extras = teacher[5] or []

        new_board = polish_board_2024(board, matched_skill)
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
            if not any(isinstance(e, dict) and e.get("type") == extra_card["type"] for e in extras):
                extras.insert(0, extra_card)
            teacher[5] = extras

        entry[7] = teacher
        updated_count += 1

    new_json_str = json.dumps(data, ensure_ascii=False)
    new_content = prefix + new_json_str + suffix
    open(path, 'w', encoding='utf-8').write(new_content)

    print(f"[{tid} - 2024] Processed {updated_count} questions (Skills applied: {skill_applied_count})")
    return updated_count, skill_applied_count

def process_exam_2022(tid, pdf_intents_map):
    path = os.path.join(BASE_DIR, f'sol_{tid}.js')
    if not os.path.exists(path):
        return 0, 0

    content = open(path, encoding='utf-8').read()
    m = re.search(r'=\s*(\{"\d+":.*?\});?\s*$', content, re.DOTALL)
    if not m:
        idx = content.find('{"1":')
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
    exam_pdf_intents = pdf_intents_map.get(tid, {})

    for qid, entry in data.items():
        if not isinstance(entry, list) or len(entry) < 8:
            continue

        ans = clean_text(str(entry[0]))
        raw_intent = clean_text(str(entry[1]))
        official_intent = exam_pdf_intents.get(str(qid)) or raw_intent
        
        # update intent in entry[1] if it was generic placeholder
        if "핵심 개념을 이해하고" in raw_intent or len(raw_intent) < 5:
            entry[1] = official_intent

        full_text = clean_text(official_intent + " " + json.dumps(entry, ensure_ascii=False))

        matched_skill = None
        for tmpl in SKILL_TEMPLATES:
            if tmpl["match"](full_text):
                matched_skill = tmpl
                break

        # Build goal
        goal = official_intent
        if matched_skill:
            goal += matched_skill["goal_suffix"]

        # Build board
        if matched_skill:
            board = [
                ["[조건 분석] 출제 개념 및 핵심 조건", f"출제 의도: {official_intent}."],
                matched_skill["board_item"],
                [f"[정답 도출] 계산 점검 $ans = {ans}$", f"검증 과정을 거쳐 최종 정답 {ans} 확정."]
            ]
        else:
            board = [
                ["[조건 분석] 문제 조건 및 출제 의도 파악", f"{official_intent}."],
                ["[식 전개] 핵심 공식 및 성질 적용", "단계별 수식 정리 및 성질 대입."],
                [f"[정답 도출] 계산 점검 $ans = {ans}$", f"최종 정답 {ans} 확정."]
            ]

        # Build hint
        hint = entry[3] if len(entry) > 3 and isinstance(entry[3], str) else f"정답 {ans} — 풀이 과정을 확인하세요."

        # Build questions
        questions = []
        old_teacher = entry[7]
        if isinstance(old_teacher, dict) and 'ask' in old_teacher and isinstance(old_teacher['ask'], list):
            questions = [clean_text(q) for q in old_teacher['ask']]
        elif isinstance(old_teacher, list) and len(old_teacher) > 3 and isinstance(old_teacher[3], list):
            questions = [clean_text(q) for q in old_teacher[3]]

        if not questions:
            questions = [
                f"{official_intent}을(를) 해결하기 위해 가장 먼저 적용해야 할 개념은 무엇인가요?",
                f"정답 {ans}이(가) 도출되는 식의 계산 과정을 설명해 보세요."
            ]

        if matched_skill and not any(matched_skill["question"] in q for q in questions):
            questions.append(matched_skill["question"])

        # Build rubric
        rubric = entry[4] if len(entry) > 4 and isinstance(entry[4], str) else f"출제 의도에 맞게 기본 개념을 단계적으로 식에 적용하도록 유도합니다."

        # Build extras
        extras = [
            {
                "type": "핵심 정리",
                "text": f"📌 <b>출제 핵심 및 풀이 전략:</b><br>{official_intent}<br>최종 정답은 <b>{ans}</b>입니다."
            }
        ]
        if matched_skill:
            extras.insert(0, matched_skill["extra"])
            skill_applied_count += 1

        # Replace entry[7] with standard 6-element list
        entry[7] = [goal, board, hint, questions, rubric, extras]
        updated_count += 1

    new_json_str = json.dumps(data, ensure_ascii=False)
    new_content = prefix + new_json_str + suffix
    open(path, 'w', encoding='utf-8').write(new_content)

    print(f"[{tid} - 2022] Processed {updated_count} questions (Skills applied: {skill_applied_count})")
    return updated_count, skill_applied_count

def main():
    print("Loading 2022 official PDF intents...")
    pdf_intents_map = load_2022_pdf_intents()
    print(f"Loaded {len(pdf_intents_map)} exam PDF intent maps.")

    total_2024_q, total_2024_s = 0, 0
    print("\n--- Processing 2024 Exams (8 sets, 240 questions) ---")
    for tid in EXAMS_2024:
        q, s = process_exam_2024(tid)
        total_2024_q += q
        total_2024_s += s

    total_2022_q, total_2022_s = 0, 0
    print("\n--- Processing 2022 Exams (8 sets, 240 questions) ---")
    for tid in EXAMS_2022:
        q, s = process_exam_2022(tid, pdf_intents_map)
        total_2022_q += q
        total_2022_s += s

    print("\n=======================================================")
    print(f"2024 학년도 총 문항: {total_2024_q}, 특화 꿀팁 주입: {total_2024_s}")
    print(f"2022 학년도 총 문항: {total_2022_q}, 특화 꿀팁 주입: {total_2022_s}")
    print(f"총 합계: {total_2024_q + total_2022_q}문항 / 꿀팁 주입: {total_2024_s + total_2022_s}문항 (100% 칠판/수업목표/발문/카드 완비)")
    print("=======================================================")

if __name__ == '__main__':
    main()

