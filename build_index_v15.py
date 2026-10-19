# -*- coding: utf-8 -*-
"""
Script to build and inject Lecture 15 into index.html
Lecture: [Geometric Mean] Product of All Divisors! Formula and Principle
Instructor: Bae Sang-myeon (MathPresso / Chulbyuk Math)
YouTube Short: https://youtube.com/shorts/tyJUL6AKlmE
"""

import os
import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code for tab
    with open('product_of_divisors_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()

    # 1. Update Switcher Bar: Add btnLec15 as active, remove active from btnLec14
    if 'id="btnLec15"' not in html:
        old_btn14 = '<button class="lecture-btn active" id="btnLec14" onclick="setLecture(14)">'
        if old_btn14 in html:
            new_btn_block = '''<button class="lecture-btn active" id="btnLec15" onclick="setLecture(15)">
          약수의 총곱 &amp; 기하평균 (배상면)
        </button>
        <button class="lecture-btn" id="btnLec14" onclick="setLecture(14)">'''
            html = html.replace(old_btn14, new_btn_block, 1)
            print("Added btnLec15 to switcher bar.")
        else:
            old_btn14_alt = '<button class="lecture-btn" id="btnLec14" onclick="setLecture(14)">'
            if old_btn14_alt in html:
                new_btn_block = '''<button class="lecture-btn active" id="btnLec15" onclick="setLecture(15)">
          약수의 총곱 &amp; 기하평균 (배상면)
        </button>
        <button class="lecture-btn" id="btnLec14" onclick="setLecture(14)">'''
                html = html.replace(old_btn14_alt, new_btn_block, 1)
                print("Added btnLec15 to switcher bar (alt).")

    # Update captured_summary button label
    html = html.replace('📸 사진 1~14 핵심 전용 페이지', '📸 사진 1~15 핵심 전용 페이지')

    # 2. Hide lecture14View if active
    if '<div id="lecture14View">' in html:
        html = html.replace('<div id="lecture14View">', '<div id="lecture14View" style="display: none;">', 1)
        print("Set lecture14View to display: none.")

    # 3. Create Lecture 15 View HTML
    escaped_manim = (manim_code
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))

    lecture15_template = '''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 15 (PRODUCT OF ALL DIVISORS: MATHPRESSO)     -->
    <!-- ============================================================== -->
    <div id="lecture15View">
      <header>
        <div class="badge-pill" style="border-color: rgba(234, 179, 8, 0.4); color: #facc15; box-shadow: 0 0 20px rgba(234, 179, 8, 0.3);">
          ⚡ 제15강 · 매스프레소 MathPresso (배상면 선생님 / 철벽수학)
        </div>
        <h1 style="background: linear-gradient(135deg, #facc15 0%, #fb923c 50%, #38bdf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          [기하평균] 약수의 총 곱! $P(N) = (\\sqrt{N})^{d(N)}$
        </h1>
        <p class="subtitle" style="max-width: 900px; margin: 0 auto; line-height: 1.7; color: #cbd5e1;">
          "약수의 개수, 약수의 총합은 익숙하지만 약수의 곱은 생소하다!"<br>
          자연수 $N$의 모든 약수는 $d \\times \\frac{N}{d} = N$의 대칭 쌍(Pair)을 이루며,
          <strong>약수 1개의 곱셈 기대치(기하평균)는 정확히 $\\sqrt{N}$</strong>입니다.<br>
          약수의 개수가 짝수이든 홀수(완전제곱수)이든 모든 자연수에 예외 없이 성립하는 궁극의 공식을 완전 정복합니다.
        </p>
      </header>

      <!-- TOP FORMULA HIGHLIGHT BANNER -->
      <div style="background: linear-gradient(135deg, rgba(234, 179, 8, 0.15), rgba(251, 146, 60, 0.1), rgba(15, 23, 42, 0.9)); border: 2px solid rgba(234, 179, 8, 0.5); border-radius: 20px; padding: 28px; margin-bottom: 35px; box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5); text-align: center;">
        <div style="font-size: 0.95rem; font-weight: 700; color: #facc15; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px;">
          ⭐ 배상면 선생님의 약수 총곱 정리 (Product of All Positive Divisors)
        </div>
        <div style="font-size: 1.6rem; color: #ffffff; margin: 15px 0; font-family: 'Consolas', monospace; line-height: 1.8;">
          $$\\prod_{d \\mid N} d = \\left(\\sqrt{N}\\right)^{d(N)} = N^{\\frac{d(N)}{2}}$$
        </div>
        <p style="margin: 0; color: #e2e8f0; font-size: 1.05rem;">
          <strong style="color: #fde047;">핵심 원리:</strong> 모든 약수 1개의 <strong>기하평균(Geometric Mean)</strong>은 $\\sqrt{N}$이므로, 
          약수 $k$개를 모두 곱한 값은 <strong>$\\sqrt{N}$을 $k$번 곱한 $(\\sqrt{N})^k$</strong>와 완벽히 같습니다!
        </p>
      </div>

      <!-- MAIN INTERACTIVE LAB: DIVISOR PAIRING & GEOMETRIC MEAN VISUALIZER -->
      <div class="card" style="margin-bottom: 40px; border-color: rgba(234, 179, 8, 0.4); box-shadow: 0 10px 30px rgba(234, 179, 8, 0.15);">
        <h2 style="color: #facc15; display: flex; align-items: center; gap: 10px;">
          <span>🔬</span> 약수의 대칭 쌍 &amp; 기하평균 인터랙티브 비주얼라이저
        </h2>
        <p style="color: #94a3b8; margin-bottom: 20px;">
          자연수 $N$을 선택하거나 직접 입력하면, 모든 약수의 대칭 쌍(Pair) 아크와 중앙 기하평균 $\\sqrt{N}$의 완벽한 대칭 균형을 실시간 렌더링합니다.
        </p>

        <!-- CONTROLS -->
        <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; padding: 20px; margin-bottom: 24px;">
          <div style="display: flex; flex-wrap: wrap; gap: 12px; align-items: center; margin-bottom: 16px;">
            <span style="font-weight: 700; color: #e2e8f0; font-size: 0.95rem;">빠른 예제 선택:</span>
            <button class="nav-btn" onclick="setN15(12)" style="padding: 6px 14px; font-size: 0.85rem; border-color: rgba(56, 189, 248, 0.5);">N = 12 (영상 예제, 6개)</button>
            <button class="nav-btn" onclick="setN15(16)" style="padding: 6px 14px; font-size: 0.85rem; border-color: rgba(244, 63, 94, 0.5);">N = 16 (제곱수, 5개)</button>
            <button class="nav-btn" onclick="setN15(24)" style="padding: 6px 14px; font-size: 0.85rem; border-color: rgba(56, 189, 248, 0.5);">N = 24 (8개)</button>
            <button class="nav-btn" onclick="setN15(36)" style="padding: 6px 14px; font-size: 0.85rem; border-color: rgba(244, 63, 94, 0.5);">N = 36 (제곱수, 9개)</button>
            <button class="nav-btn" onclick="setN15(60)" style="padding: 6px 14px; font-size: 0.85rem; border-color: rgba(244, 63, 94, 0.5);">N = 60 (12개)</button>
            <button class="nav-btn" onclick="setN15(100)" style="padding: 6px 14px; font-size: 0.85rem; border-color: rgba(244, 63, 94, 0.5);">N = 100 (제곱수, 9개)</button>
          </div>

          <div style="display: flex; flex-wrap: wrap; gap: 16px; align-items: center;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <label for="inputN15" style="color: #facc15; font-weight: 700;">자연수 $N$ 직접 입력:</label>
              <input type="number" id="inputN15" value="12" min="1" max="10000" style="background: #1e293b; border: 1px solid #475569; color: #fff; padding: 8px 14px; border-radius: 8px; width: 110px; font-size: 1rem; font-family: monospace; font-weight: bold;" oninput="updateFromInput15()">
            </div>
            <div style="display: flex; align-items: center; gap: 10px; flex: 1; min-width: 200px;">
              <span style="color: #94a3b8; font-size: 0.85rem;">슬라이더 (1~120):</span>
              <input type="range" id="sliderN15" min="1" max="120" value="12" style="flex: 1; accent-color: #facc15;" oninput="updateFromSlider15(this.value)">
            </div>
          </div>
        </div>

        <!-- STATS CARDS -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 24px;">
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 12px; padding: 14px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 4px;">소인수분해 (Prime Factorization)</div>
            <div id="statFactor15" style="font-size: 1.15rem; font-weight: bold; color: #38bdf8;">12 = 2² × 3¹</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 12px; padding: 14px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 4px;">약수의 개수 $d(N)$</div>
            <div id="statCount15" style="font-size: 1.15rem; font-weight: bold; color: #facc15;">6개 (짝수)</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 12px; padding: 14px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 4px;">약수 1개의 기하평균 $\\sqrt{N}$</div>
            <div id="statGm15" style="font-size: 1.15rem; font-weight: bold; color: #4ade80;">√12 ≈ 3.464</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(244, 63, 94, 0.3); border-radius: 12px; padding: 14px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 4px;">약수의 총곱 $P(N)$</div>
            <div id="statProd15" style="font-size: 1.15rem; font-weight: bold; color: #f43f5e;">12³ = 1,728</div>
          </div>
        </div>

        <!-- CANVAS VISUALIZER -->
        <div style="background: #090d16; border: 1px solid rgba(148, 163, 184, 0.3); border-radius: 16px; padding: 15px; position: relative; overflow: hidden;">
          <canvas id="canvasDivisors15" width="1000" height="340" style="width: 100%; height: auto; display: block;"></canvas>
          <div id="canvasTooltip15" style="position: absolute; display: none; background: rgba(15, 23, 42, 0.95); border: 1px solid #facc15; border-radius: 8px; padding: 8px 12px; color: #fff; font-size: 0.85rem; pointer-events: none; box-shadow: 0 4px 12px rgba(0,0,0,0.5); z-index: 10;"></div>
        </div>
      </div>

      <!-- IN-DEPTH CONCEPT TABS -->
      <div class="card" style="margin-bottom: 40px;">
        <h2 style="color: #38bdf8; display: flex; align-items: center; gap: 10px;">
          <span>📚</span> 약수의 총곱 이론 및 증명 마스터 가이드
        </h2>

        <div style="display: flex; gap: 10px; margin-bottom: 24px; border-bottom: 1px solid #334155; padding-bottom: 12px; flex-wrap: wrap;">
          <button class="nav-btn active" id="tabBtnL15_1" onclick="switchL15Tab(1)">1. 대칭 쌍 증명 (가우스법)</button>
          <button class="nav-btn" id="tabBtnL15_2" onclick="switchL15Tab(2)">2. 기하평균 증명 (배상면의 통찰)</button>
          <button class="nav-btn" id="tabBtnL15_3" onclick="switchL15Tab(3)">3. 완전제곱수 검증 (홀수 개)</button>
          <button class="nav-btn" id="tabBtnL15_4" onclick="switchL15Tab(4)">4. 소인수분해 대수적 증명</button>
          <button class="nav-btn" id="tabBtnL15_5" onclick="switchL15Tab(5)">5. 실전 수능·내신 기출 예제</button>
          <button class="nav-btn" id="tabBtnL15_6" onclick="switchL15Tab(6)">6. Manim 애니메이션 코드</button>
        </div>

        <!-- TAB 1: PAIRING PROOF -->
        <div id="tabL15_1" class="tab-content" style="display: block;">
          <h3 style="color: #facc15;">증명 1: 약수의 대칭 쌍(Pairing)과 가우스 곱셈법</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            초등학생 가우스가 $1$부터 $100$까지의 합을 구할 때 양끝의 합 $1+100 = 2+99 = \\cdots = 101$로 대칭 쌍을 묶어 
            덧셈을 곱셈으로 전환한 것처럼, <strong>약수의 세계에서도 곱셈 대칭 쌍이 완벽하게 존재</strong>합니다.
          </p>
          <div style="background: rgba(15, 23, 42, 0.7); border-left: 4px solid #38bdf8; padding: 18px; border-radius: 0 12px 12px 0; margin: 20px 0;">
            <p style="color: #e2e8f0; margin: 0 0 10px 0;">
              $N$의 임의의 양의 약수를 $d$라 하면, $\\frac{N}{d}$ 역시 반드시 $N$의 양의 약수가 되며, 두 약수의 곱은 항상 $N$입니다:
            </p>
            <div style="text-align: center; font-size: 1.2rem; color: #38bdf8; font-family: monospace;">
              $$d \\times \\frac{N}{d} = N$$
            </div>
          </div>
          <p style="color: #cbd5e1; line-height: 1.8;">
            $N$의 모든 약수를 크기순으로 나열한 것을 $d_1, d_2, \\dots, d_k$라 할 때, 총곱 $P(N)$을 정방향과 역방향으로 적어 곱해봅니다:
          </p>
          <div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 12px; padding: 20px; margin: 15px 0;">
            $$\\begin{aligned}
            P(N) &= d_1 \\times d_2 \\times \\cdots \\times d_k \\\\
            P(N) &= \\frac{N}{d_1} \\times \\frac{N}{d_2} \\times \\cdots \\times \\frac{N}{d_k}
            \\end{aligned}$$
            <hr style="border: 0; border-top: 1px dashed #475569; margin: 15px 0;">
            $$\\begin{aligned}
            [P(N)]^2 &= \\left(d_1 \\times \\frac{N}{d_1}\\right) \\times \\left(d_2 \\times \\frac{N}{d_2}\\right) \\times \\cdots \\times \\left(d_k \\times \\frac{N}{d_k}\\right) \\\\
            &= \\underbrace{N \\times N \\times \\cdots \\times N}_{k\\text{개}} = N^k
            \\end{aligned}$$
          </div>
          <p style="color: #cbd5e1; line-height: 1.8;">
            양변에 제곱근을 취하면 (모든 약수는 양수이므로):
          </p>
          <div style="text-align: center; font-size: 1.3rem; color: #facc15; font-weight: bold; margin: 15px 0;">
            $$P(N) = \\sqrt{N^k} = \\left(\\sqrt{N}\\right)^k = N^{\\frac{k}{2}}$$
          </div>
        </div>

        <!-- TAB 2: GEOMETRIC MEAN PROOF -->
        <div id="tabL15_2" class="tab-content" style="display: none;">
          <h3 style="color: #facc15;">증명 2: 기하평균(Geometric Mean)과 곱셈 기대치 (배상면 선생님의 통찰)</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            배상면 선생님은 이 공식을 단순히 수식 조작으로 보지 않고, <strong>"기하평균(Geometric Mean) = 곱셈 세계에서의 1회당 기대치"</strong>라는
            본질적 통찰로 단번에 설명합니다.
          </p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 25px 0;">
            <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 14px; padding: 20px;">
              <h4 style="color: #38bdf8; margin-top: 0;">➕ 덧셈의 세계 (산술평균)</h4>
              <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                두 수 $A, B$를 더할 때 1회당 평균적으로 기여하는 크기는 <strong>산술평균 $\\frac{A+B}{2}$</strong>입니다.<br>
                따라서 $k$개의 평균이 $M$이면 총합은 $M \\times k$가 됩니다.
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 14px; padding: 20px;">
              <h4 style="color: #facc15; margin-top: 0;">✖️ 곱셈의 세계 (기하평균)</h4>
              <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                두 수 $A, B$를 곱할 때 1회당 평균적으로 기여하는 곱셈 크기는 <strong>기하평균 $\\sqrt{A \\times B}$</strong>입니다.<br>
                따라서 $k$개의 기하평균이 $G$이면 총곱은 $G^k$가 됩니다!
              </p>
            </div>
          </div>
          <div style="background: rgba(234, 179, 8, 0.1); border: 1px solid rgba(234, 179, 8, 0.4); border-radius: 14px; padding: 20px; margin: 20px 0;">
            <h4 style="color: #fde047; margin-top: 0;">💡 약수 1개의 기하평균 유도</h4>
            <p style="color: #e2e8f0; line-height: 1.8; margin-bottom: 10px;">
              임의의 약수 $d$와 그 짝꿍 $\\frac{N}{d}$의 곱은 $N = (\\sqrt{N})^2$이므로, 두 약수의 기하평균은:
            </p>
            <div style="text-align: center; font-size: 1.25rem; color: #facc15; margin: 15px 0;">
              $$\\text{G.M.} = \\sqrt{d \\times \\frac{N}{d}} = \\sqrt{N}$$
            </div>
            <p style="color: #e2e8f0; line-height: 1.8; margin: 0;">
              즉, <strong>"작은 약수와 큰 약수가 짝을 이루어 서로를 보완하므로, 약수 1개가 곱셈에서 차지하는 평균적 크기는 정확히 $\\sqrt{N}$"</strong>입니다!<br>
              약수가 총 $k$개 있으므로, 약수의 총곱은 <strong>$\\sqrt{N}$을 $k$번 거듭제곱한 $(\\sqrt{N})^k$</strong>가 됩니다!
            </p>
          </div>
        </div>

        <!-- TAB 3: SQUARE NUMBER VERIFICATION -->
        <div id="tabL15_3" class="tab-content" style="display: none;">
          <h3 style="color: #facc15;">완전제곱수(Square Number)에서도 공식이 성립하는가?</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            약수의 개수가 짝수일 때는 2개씩 짝이 깔끔하게 맞아떨어지지만, <strong>완전제곱수($N=m^2$)는 약수의 개수가 홀수 개</strong>입니다.<br>
            가운데 약수가 홀로 남는데도 과연 $(\\sqrt{N})^k$ 공식이 정확히 맞을까요?
          </p>

          <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(244, 63, 94, 0.4); border-radius: 14px; padding: 22px; margin: 20px 0;">
            <h4 style="color: #f43f5e; margin-top: 0;">반례 의심 검증: $N = 36$ (약수 9개)</h4>
            <p style="color: #e2e8f0; line-height: 1.7;">
              $36$의 모든 약수: {1, 2, 3, 4, <strong>6</strong>, 9, 12, 18, 36} (총 $k = 9$개, 홀수)<br>
              - 대칭 쌍: $(1, 36), (2, 18), (3, 12), (4, 9)$ $\\implies$ 4쌍, 각 곱은 $36$<br>
              - 가운데 홀로 남은 약수: <strong>$6 = \\sqrt{36}$</strong>
            </p>
            <div style="background: #0f172a; padding: 15px; border-radius: 10px; margin: 15px 0;">
              <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 6px;">[직접 나열 곱셈]:</p>
              $$\\begin{aligned}
              P(36) &= (1 \\times 36) \\times (2 \\times 18) \\times (3 \\times 12) \\times (4 \\times 9) \\times 6 \\\\
              &= 36^4 \\times 6 = (6^2)^4 \\times 6^1 = 6^8 \\times 6^1 = 6^9 = 10,077,696
              \\end{aligned}$$
              <p style="color: #94a3b8; font-size: 0.9rem; margin: 15px 0 6px 0;">[공식 적용]:</p>
              $$P(36) = (\\sqrt{36})^9 = 6^9 = 10,077,696$$
            </div>
            <p style="color: #4ade80; font-weight: bold; margin: 0;">
              🎉 완벽하게 일치합니다! 가운데 약수 $6$은 자기 자신과의 기하평균이 $\\sqrt{6 \\times 6} = 6 = \\sqrt{36}$이므로,
              홀수 개이든 짝수 개이든 공식에 단 하나의 오차도 없습니다.
            </p>
          </div>
        </div>

        <!-- TAB 4: ALGEBRAIC PROOF VIA PRIME FACTORIZATION -->
        <div id="tabL15_4" class="tab-content" style="display: none;">
          <h3 style="color: #facc15;">증명 3: 소인수분해를 이용한 대수적 증명</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            자연수 $N$을 소인수분해하여 각 소인수의 지수의 총합을 직접 계산하는 고전 정수론 방식의 엄밀한 증명입니다.
          </p>
          <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 12px; padding: 20px; margin: 15px 0;">
            <p style="color: #e2e8f0; line-height: 1.8;">
              $N = p_1^{a_1} p_2^{a_2} \\cdots p_r^{a_r}$ 이고, 약수의 개수를 $k = (a_1+1)(a_2+1)\\cdots(a_r+1)$이라 합시다.<br>
              임의의 약수 $d$는 $d = p_1^{x_1} p_2^{x_2} \\cdots p_r^{x_r}$ ($0 \\le x_i \\le a_i$)로 표현됩니다.
            </p>
            <p style="color: #e2e8f0; line-height: 1.8;">
              모든 약수를 곱할 때 소인수 $p_1$의 지수의 합 $S_1$을 구하면, $x_1$이 $0, 1, \\dots, a_1$일 때마다 나머지 지수 선택의 경우의 수가 $\\frac{k}{a_1+1}$가지이므로:
            </p>
            $$\\begin{aligned}
            S_1 &= \\left(\\sum_{x_1=0}^{a_1} x_1\\right) \\times \\frac{k}{a_1+1} = \\frac{a_1(a_1+1)}{2} \\times \\frac{k}{a_1+1} = a_1 \\times \\frac{k}{2}
            \\end{aligned}$$
            <p style="color: #e2e8f0; line-height: 1.8;">
              모든 소인수 $p_i$에 대해 지수의 합은 $a_i \\times \\frac{k}{2}$가 되므로, 모든 약수의 총곱 $P(N)$은:
            </p>
            $$P(N) = p_1^{a_1 \\frac{k}{2}} p_2^{a_2 \\frac{k}{2}} \\cdots p_r^{a_r \\frac{k}{2}} = \\left(p_1^{a_1} p_2^{a_2} \\cdots p_r^{a_r}\\right)^{\\frac{k}{2}} = N^{\\frac{k}{2}} = \\left(\\sqrt{N}\\right)^k$$
          </div>
        </div>

        <!-- TAB 5: EXAMPLES -->
        <div id="tabL15_5" class="tab-content" style="display: none;">
          <h3 style="color: #facc15;">실전 수능·내신 기출 대표 예제 풀이</h3>
          <div style="display: grid; gap: 16px;">
            <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 12px; padding: 18px;">
              <h4 style="color: #38bdf8; margin-top: 0;">예제 1: 12의 모든 양의 약수의 곱을 구하시오.</h4>
              <p style="color: #cbd5e1; margin: 0; line-height: 1.7;">
                $12 = 2^2 \\times 3^1$ $\\implies$ 약수 개수 $k = (2+1)(1+1) = 6$개.<br>
                공식 적용: $P(12) = (\\sqrt{12})^6 = 12^3 = \\mathbf{1,728}$.
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 12px; padding: 18px;">
              <h4 style="color: #facc15; margin-top: 0;">예제 2: 100의 모든 양의 약수의 곱을 구하시오.</h4>
              <p style="color: #cbd5e1; margin: 0; line-height: 1.7;">
                $100 = 10^2 = 2^2 \\times 5^2$ $\\implies$ 약수 개수 $k = (2+1)(2+1) = 9$개.<br>
                공식 적용: $P(100) = (\\sqrt{100})^9 = 10^9 = \\mathbf{1,000,000,000}$ ($10억$).
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 12px; padding: 18px;">
              <h4 style="color: #4ade80; margin-top: 0;">예제 3: 72의 모든 양의 약수의 곱을 $2^a \\cdot 3^b$ 형태로 나타내시오.</h4>
              <p style="color: #cbd5e1; margin: 0; line-height: 1.7;">
                $72 = 2^3 \\times 3^2$ $\\implies$ 약수 개수 $k = (3+1)(2+1) = 12$개.<br>
                공식 적용: $P(72) = 72^{12/2} = 72^6 = (2^3 \\times 3^2)^6 = \\mathbf{2^{18} \\times 3^{12}}$.
              </p>
            </div>
          </div>
        </div>

        <!-- TAB 6: MANIM CODE -->
        <div id="tabL15_6" class="tab-content" style="display: none;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <h3 style="color: #facc15; margin: 0;">3Blue1Brown 스타일 Manim Community 애니메이션 코드</h3>
            <button class="nav-btn" onclick="copyManimCode15()" style="padding: 6px 14px; font-size: 0.85rem; border-color: #facc15;">📋 코드 복사</button>
          </div>
          <p style="color: #94a3b8; font-size: 0.9rem;">
            약수들의 대칭 아크 연결선, 기하평균 수평 균형, 완전제곱수 $N=36$의 단독 약수 강조를 애니메이션으로 구현한 파이썬 스크립트입니다.
          </p>
          <pre id="manimPre15" style="background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 18px; color: #e2e8f0; font-family: 'Consolas', monospace; font-size: 0.85rem; max-height: 500px; overflow-y: auto; line-height: 1.5;"><code>__MANIM_CODE__</code></pre>
        </div>
      </div>

      <!-- TIMELINE CAPTURE CARDS -->
      <div class="card" style="margin-bottom: 40px;">
        <h2 style="color: #facc15; display: flex; align-items: center; gap: 10px;">
          <span>🎬</span> 타임라인별 핵심 판서 &amp; 화면 캡처 해설 (10장)
        </h2>
        <p style="color: #94a3b8; margin-bottom: 25px;">
          배상면 선생님의 33초 강의 흐름을 고화질(1080p) 프레임 10장으로 정밀 분석했습니다.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
          <!-- CARD 1 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/01_intro_question_product_of_divisors.jpg" alt="01 도입 질문" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:02</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">01. 문제 제기: 약수의 곱은 생소하다</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                약수의 개수와 약수의 총합은 중·고교에서 익숙하게 다루지만, 약수의 곱은 생소하게 다가옵니다.
              </p>
            </div>
          </div>

          <!-- CARD 2 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/02_formula_root_n_power_k.jpg" alt="02 공식 선언" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:06</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">02. 공식 선언: $(\\sqrt{N})^{k}$</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                자연수 $N$의 모든 (양의) 약수의 곱은 $\\sqrt{N}$의 '약수의 개수' 거듭제곱입니다.
              </p>
            </div>
          </div>

          <!-- CARD 3 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/03_question_why_proof_starts.jpg" alt="03 Why 질문" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:08</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">03. Why? 원리 탐구 시작</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                단순 암기가 아닌, 왜 이 공식이 항상 완벽하게 성립하는지 원리 증명에 착수합니다.
              </p>
            </div>
          </div>

          <!-- CARD 4 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/04_divisors_appear_in_pairs.jpg" alt="04 약수의 짝" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:10</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">04. 핵심 원리 1: 약수는 짝으로 존재</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                약수는 언제나 둘씩 짝(Pair)을 지어 나타난다는 정수론의 기본 원리를 제시합니다.
              </p>
            </div>
          </div>

          <!-- CARD 5 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/05_example_12_divisors_pairing.jpg" alt="05 12의 약수 예시" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:13</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">05. 구체적 예시: $3 \\times 4 = 12$</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $3 \\times 4 = 12$ 처럼 3과 4가 짝을 이루어 $12$의 약수가 되는 직관적 예시를 듭니다.
              </p>
            </div>
          </div>

          <!-- CARD 6 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/06_general_pairing_d_and_n_over_d.jpg" alt="06 일반화" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:16</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">06. 일반화: $d$와 $\\frac{N}{d}$의 짝</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $N$의 임의의 약수를 $d$라 하면, $d$와 $\\frac{N}{d}$은 반드시 짝으로 $N$의 약수가 됩니다.
              </p>
            </div>
          </div>

          <!-- CARD 7 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/07_product_of_pair_equals_n.jpg" alt="07 쌍의 곱" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:20</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">07. 두 약수의 곱 = $(\\sqrt{N})^2$</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $d \\times \\frac{N}{d} = N = (\\sqrt{N})^2$로 표현하여 기하평균의 징검다리를 놓습니다.
              </p>
            </div>
          </div>

          <!-- CARD 8 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/08_geometric_mean_is_root_n.jpg" alt="08 기하평균" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:23</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">08. 약수 하나의 기하평균 = $\\sqrt{N}$</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                "약수 하나의 기하평균 [곱셈의 회당 기대치] = $\\sqrt{N}$"이라는 최고의 직관적 표현이 등장합니다!
              </p>
            </div>
          </div>

          <!-- CARD 9 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/09_total_product_root_n_times_k.jpg" alt="09 총곱 계산" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:27</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">09. 총곱 = $\\sqrt{N}$을 개수만큼 곱함</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                기하평균이 $\\sqrt{N}$인 수를 약수의 개수만큼 곱하므로 $(\\sqrt{N})^{k}$가 유도됩니다.
              </p>
            </div>
          </div>

          <!-- CARD 10 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v15/10_final_conclusion_formula_box.jpg" alt="10 최종 결론" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #facc15; font-size: 0.75rem;">00:30</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">10. 최종 정리: 노란 원 공식 박스</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                "자연수 $N$의 모든 약수의 곱 = $\\sqrt{N}^{\\text{약수의 개수}}$"로 33초 강의가 명쾌하게 마무리됩니다.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
'''

    lecture15_html = lecture15_template.replace('__MANIM_CODE__', escaped_manim)

    # Insert lecture15View before lecture14View
    idx_lec14 = html.find('<div id="lecture14View"')
    if idx_lec14 != -1:
        html = html[:idx_lec14] + lecture15_html + '\n' + html[idx_lec14:]
        print("Inserted lecture15View before lecture14View.")

    # 4. Insert Lecture 15 JavaScript
    js_code_15 = '''
    // ==============================================================
    // JAVASCRIPT FOR LECTURE 15 (PRODUCT OF DIVISORS & GEOMETRIC MEAN)
    // ==============================================================
    let currentN15 = 12;
    let hoveredDivisorIdx15 = -1;

    function getDivisors(n) {
      const divs = [];
      for (let i = 1; i * i <= n; i++) {
        if (n % i === 0) {
          divs.push(i);
          if (i * i !== n) {
            divs.push(n / i);
          }
        }
      }
      divs.sort((a, b) => a - b);
      return divs;
    }

    function getPrimeFactors(n) {
      if (n === 1) return "1";
      let d = 2;
      let temp = n;
      const factors = {};
      while (d * d <= temp) {
        while (temp % d === 0) {
          factors[d] = (factors[d] || 0) + 1;
          temp /= d;
        }
        d++;
      }
      if (temp > 1) {
        factors[temp] = (factors[temp] || 0) + 1;
      }
      return Object.entries(factors)
        .map(([p, exp]) => exp === 1 ? `${p}¹` : `${p}<sup>${exp}</sup>`)
        .join(" × ");
    }

    function formatLargeProduct(n, k) {
      if (k % 2 === 0) {
        const pwr = k / 2;
        const val = Math.pow(n, pwr);
        if (val < 1e12) {
          return `${n}<sup>${pwr}</sup> = ${val.toLocaleString()}`;
        }
        return `${n}<sup>${pwr}</sup> ≈ ${val.toExponential(4)}`;
      } else {
        const sqrtN = Math.sqrt(n);
        const val = Math.pow(sqrtN, k);
        if (Number.isInteger(sqrtN)) {
          if (val < 1e12) {
            return `(${sqrtN})<sup>${k}</sup> = ${Math.round(val).toLocaleString()}`;
          }
          return `(${sqrtN})<sup>${k}</sup> ≈ ${val.toExponential(4)}`;
        }
        return `(√${n})<sup>${k}</sup> ≈ ${val.toExponential(4)}`;
      }
    }

    function setN15(val) {
      currentN15 = parseInt(val, 10);
      const inputEl = document.getElementById("inputN15");
      const sliderEl = document.getElementById("sliderN15");
      if (inputEl) inputEl.value = currentN15;
      if (sliderEl) sliderEl.value = Math.min(currentN15, 120);
      updateL15();
    }

    function updateFromInput15() {
      const val = parseInt(document.getElementById("inputN15").value, 10);
      if (!isNaN(val) && val >= 1 && val <= 100000) {
        currentN15 = val;
        const sliderEl = document.getElementById("sliderN15");
        if (sliderEl) sliderEl.value = Math.min(val, 120);
        updateL15();
      }
    }

    function updateFromSlider15(val) {
      currentN15 = parseInt(val, 10);
      const inputEl = document.getElementById("inputN15");
      if (inputEl) inputEl.value = currentN15;
      updateL15();
    }

    function updateL15() {
      const n = currentN15;
      const divs = getDivisors(n);
      const k = divs.length;
      const isSquare = Number.isInteger(Math.sqrt(n));

      // Update stat cards
      const factorEl = document.getElementById("statFactor15");
      const countEl = document.getElementById("statCount15");
      const gmEl = document.getElementById("statGm15");
      const prodEl = document.getElementById("statProd15");

      if (factorEl) factorEl.innerHTML = `${n} = ${getPrimeFactors(n)}`;
      if (countEl) countEl.innerHTML = `${k}개 (${isSquare ? "홀수, 완전제곱수" : "짝수"})`;
      if (gmEl) {
        const sqrtVal = Math.sqrt(n);
        gmEl.innerHTML = isSquare ? `√${n} = ${sqrtVal}` : `√${n} ≈ ${sqrtVal.toFixed(3)}`;
      }
      if (prodEl) prodEl.innerHTML = formatLargeProduct(n, k);

      renderCanvasL15();
    }

    function renderCanvasL15() {
      const canvas = document.getElementById("canvasDivisors15");
      if (!canvas) return;
      const ctx = canvas.getContext("2d");
      const w = canvas.width;
      const h = canvas.height;

      ctx.clearRect(0, 0, w, h);

      const n = currentN15;
      const divs = getDivisors(n);
      const k = divs.length;
      if (k === 0) return;

      const isSquare = Number.isInteger(Math.sqrt(n));
      const sqrtN = Math.sqrt(n);

      // Node layout
      const marginX = 80;
      const availW = w - 2 * marginX;
      const stepX = k > 1 ? availW / (k - 1) : 0;
      const baseY = h - 60;
      const nodeR = Math.max(12, Math.min(22, 400 / k));

      const nodes = [];
      for (let i = 0; i < k; i++) {
        const x = k === 1 ? w / 2 : marginX + i * stepX;
        nodes.push({ x: x, y: baseY, d: divs[i], idx: i });
      }

      // Draw horizontal baseline
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(marginX - 30, baseY);
      ctx.lineTo(w - marginX + 30, baseY);
      ctx.stroke();

      // Draw Center Geometric Mean marker line
      let gmX = w / 2;
      ctx.strokeStyle = "rgba(74, 222, 128, 0.6)";
      ctx.setLineDash([4, 4]);
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(gmX, 30);
      ctx.lineTo(gmX, baseY + 30);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#4ade80";
      ctx.font = "bold 13px 'Consolas', monospace";
      ctx.textAlign = "center";
      ctx.fillText(`기하평균 √${n} ≈ ${sqrtN.toFixed(2)}`, gmX, 22);

      // Colors for pairs
      const pairColors = [
        "#f43f5e", "#38bdf8", "#facc15", "#a855f7",
        "#ec4899", "#2dd4bf", "#fb923c", "#4ade80",
        "#60a5fa", "#e879f9", "#34d399", "#f87171"
      ];

      // Draw Pairing Arcs
      const numPairs = Math.floor(k / 2);
      for (let i = 0; i < numPairs; i++) {
        const leftNode = nodes[i];
        const rightNode = nodes[k - 1 - i];
        const col = pairColors[i % pairColors.length];
        const isHoveredPair = (hoveredDivisorIdx15 === i || hoveredDivisorIdx15 === (k - 1 - i));

        const midX = (leftNode.x + rightNode.x) / 2;
        const dist = rightNode.x - leftNode.x;
        // Arc peak height
        const arcH = Math.min(180, 40 + (numPairs - 1 - i) * (140 / Math.max(1, numPairs)));

        ctx.strokeStyle = isHoveredPair ? "#ffffff" : col;
        ctx.lineWidth = isHoveredPair ? 3.5 : 2;
        ctx.beginPath();
        ctx.moveTo(leftNode.x, baseY - nodeR);
        ctx.quadraticCurveTo(midX, baseY - nodeR - arcH * 1.5, rightNode.x, baseY - nodeR);
        ctx.stroke();

        // Label on top of arc
        const labelY = baseY - nodeR - arcH * 0.75;
        ctx.fillStyle = isHoveredPair ? "#ffffff" : col;
        ctx.font = isHoveredPair ? "bold 13px 'Consolas', monospace" : "11px 'Consolas', monospace";
        ctx.textAlign = "center";
        ctx.fillText(`${leftNode.d} × ${rightNode.d} = ${n}`, midX, Math.max(35, labelY));
      }

      // If square number, highlight center single node
      if (isSquare) {
        const midIdx = Math.floor(k / 2);
        const centerNode = nodes[midIdx];
        const isCenterHover = (hoveredDivisorIdx15 === midIdx);

        ctx.strokeStyle = "#facc15";
        ctx.lineWidth = isCenterHover ? 3 : 2;
        ctx.beginPath();
        ctx.arc(centerNode.x, centerNode.y - nodeR - 25, 20, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = "#facc15";
        ctx.font = "bold 11px sans-serif";
        ctx.fillText("단독 (√N)", centerNode.x, centerNode.y - nodeR - 50);
      }

      // Draw Nodes
      for (let i = 0; i < k; i++) {
        const node = nodes[i];
        const isCenter = isSquare && (i === Math.floor(k / 2));
        const isHover = (hoveredDivisorIdx15 === i || hoveredDivisorIdx15 === (k - 1 - i));

        // Outer glow on hover
        if (isHover) {
          ctx.beginPath();
          ctx.arc(node.x, node.y, nodeR + 6, 0, Math.PI * 2);
          ctx.fillStyle = "rgba(250, 204, 21, 0.4)";
          ctx.fill();
        }

        // Node circle
        ctx.beginPath();
        ctx.arc(node.x, node.y, nodeR, 0, Math.PI * 2);
        ctx.fillStyle = isCenter ? "#78350f" : (isHover ? "#1e293b" : "#0f172a");
        ctx.fill();
        ctx.strokeStyle = isCenter ? "#facc15" : (isHover ? "#ffffff" : "#38bdf8");
        ctx.lineWidth = isCenter ? 2.5 : 1.8;
        ctx.stroke();

        // Divisor number text
        ctx.fillStyle = isCenter ? "#fef08a" : (isHover ? "#ffffff" : "#f1f5f9");
        ctx.font = `bold ${Math.max(10, nodeR * 0.9)}px 'Consolas', monospace`;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(node.d, node.x, node.y);
      }
    }

    function switchL15Tab(tabIdx) {
      for (let i = 1; i <= 6; i++) {
        const btn = document.getElementById(`tabBtnL15_${i}`);
        const content = document.getElementById(`tabL15_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.MathJax) {
        MathJax.typesetPromise();
      }
    }

    function copyManimCode15() {
      const codeEl = document.querySelector("#manimPre15 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL15() {
      updateL15();
      if (window.MathJax) {
        MathJax.typesetPromise();
      }
    }
'''

    # Insert Lecture 15 JS before Lecture 14 JS
    idx_js14 = html.find('// ==============================================================')
    if idx_js14 != -1:
        html = html[:idx_js14] + js_code_15 + '\n' + html[idx_js14:]
        print("Inserted Lecture 15 JavaScript.")

    # 5. Update setLecture loop from 14 to 15
    html = html.replace('for (let i = 1; i <= 14; i++)', 'for (let i = 1; i <= 15; i++)')
    print("Updated setLecture loop to 15.")

    # Add num === 15 render handler
    old_l14_check = 'if (num === 14) setTimeout(renderL14, 50);'
    new_l15_check = 'if (num === 15) setTimeout(renderL15, 50);\n      else if (num === 14) setTimeout(renderL14, 50);'
    html = html.replace(old_l14_check, new_l15_check, 1)
    print("Added num === 15 render handler to setLecture.")

    # Update window load handler
    html = html.replace('setLecture(14);', 'setLecture(15);')
    html = html.replace('setTimeout(renderL14, 200);', 'setTimeout(renderL15, 200);')
    print("Updated window load handler to initialize Lecture 15.")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with Lecture 15!")

if __name__ == '__main__':
    main()
