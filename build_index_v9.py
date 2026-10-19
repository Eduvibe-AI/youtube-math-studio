# -*- coding: utf-8 -*-
"""
Script to inject Lecture 9 (Definite Integral & Area, The Diff-Function: Sao Math) into index.html
Preserving all existing Lectures 1, 2, 3, 4, 5, 6, 7, 8 without alteration.
"""

import os

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the lecture switcher bar
    old_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (8 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec8" onclick="setLecture(8)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #10b981, #06b6d4); color: #fff;">📊 그래프 특강</span>
          삼각함수 그래프 8칸 박스법 (사오수학)
        </button>
        <button class="lecture-btn" id="btnLec7" onclick="setLecture(7)">
          삼각비에서 삼각함수까지 (매쓰의 본질)
        </button>'''

    new_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (9 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec9" onclick="setLecture(9)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #f59e0b, #ef4444); color: #fff;">🔥 적분과 넓이</span>
          정적분과 넓이 & 차함수의 마법 (사오수학)
        </button>
        <button class="lecture-btn" id="btnLec8" onclick="setLecture(8)">
          삼각함수 그래프 8칸 박스법 (사오수학)
        </button>
        <button class="lecture-btn" id="btnLec7" onclick="setLecture(7)">
          삼각비에서 삼각함수까지 (매쓰의 본질)
        </button>'''

    if old_switcher_head not in content:
        print("ERROR: old_switcher_head not found in index.html!")
        return

    content = content.replace(old_switcher_head, new_switcher_head, 1)

    # Update captured_summary button from 1~8 to 1~9
    content = content.replace('📸 사진 1~8 핵심 전용 페이지', '📸 사진 1~9 핵심 전용 페이지', 1)

    # 2. Update lecture8View to start hidden:
    old_lec8_start = '<div id="lecture8View">'
    new_lec8_start = '<div id="lecture8View" style="display: none;">'
    if old_lec8_start not in content:
        print("ERROR: old_lec8_start not found!")
        return

    content = content.replace(old_lec8_start, new_lec8_start, 1)

    # 3. Read the Manim script to include in Tab 4
    with open('integral_area_diff_function_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()
    manim_code_escaped = manim_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # 4. Lecture 9 Section HTML
    lecture9_html = r'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 9 (DEFINITE INTEGRAL & AREA: SAO MATH)        -->
    <!-- ============================================================== -->
    <div id="lecture9View">
      <header>
        <div class="badge-pill" style="border-color: rgba(245, 158, 11, 0.4); color: #f59e0b; box-shadow: 0 0 20px rgba(245, 158, 11, 0.3);">
          <span>📐 고등 수학 II · 정적분과 넓이 완전 정복 · 내신/수능 1등급 필수</span>
        </div>
        <h1 style="background: linear-gradient(135deg, #ffffff 30%, #f59e0b 70%, #ef4444 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          정적분과 넓이 & 차함수 $h(x) = f(x) - g(x)$의 마법
        </h1>
        <p class="subtitle">
          정적분의 부호 면적과 기하학적 넓이의 본질! 두 곡선 사이의 넓이를 단 하나의 차함수로 $x$축 평탄화하여 10초 만에 완벽 정복하는 <strong>인터랙티브 듀얼 스튜디오</strong>입니다.
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>사오수학</strong></span>
          <span>•</span>
          <a href="https://youtu.be/iIEeqxjQIBM" target="_blank" rel="noopener noreferrer" style="color: var(--accent-blue); text-decoration: none; display: inline-flex; align-items: center; gap: 4px;">
            <span>[수Ⅱ][LV 1] 30강. 정적분과 넓이_그래프의 넓이 (10:36)</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
          <span>•</span>
          <span>강의 고화질 12단계 캡처 &amp; Manim 코드 탑재</span>
        </div>
      </header>

      <!-- Tab Bar for Lecture 9 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec9Tab('l9SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 차함수 & 넓이 스튜디오 (실시간 듀얼 변환)
        </button>
        <button class="tab-btn" onclick="switchLec9Tab('l9CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 & 12단계 타임라인
        </button>
        <button class="tab-btn" onclick="switchLec9Tab('l9ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          수학교과서식 정형화 & 수능 기출 킬러 연계
        </button>
        <button class="tab-btn" onclick="switchLec9Tab('l9ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 9) -->
      <div id="l9SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Dynamic Banner -->
          <div class="formula-banner" id="l9Banner" style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(239, 68, 68, 0.08)); border-color: rgba(245, 158, 11, 0.35);">
            <div class="label" id="l9BannerLabel" style="color: #f59e0b;">🌟 정적분과 넓이 & 차함수 불변 정리 (The Diff-Function Theorem)</div>
            <div class="math-main" id="l9BannerMath">
              $$S = \int_a^b |f(x) - g(x)|dx = \int_a^b |h(x)|dx \implies \text{기울어진 직선이 } x\text{축으로 평탄화되어 면적 } 100\% \text{ 완벽 보존!}$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l9Canvas" width="560" height="520"></canvas>
              <div id="l9CanvasCaption" style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                상단: 두 곡선 $y=f(x)$와 $y=g(x)$ 사이 영역 | 하단: 차함수 $y=f(x)-g(x)$의 $x$축 사이 영역 (면적 완벽 일치)
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Presets -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎯 사오수학 4대 필수 예제 프리셋</span>
                </div>
                <div class="preset-grid" style="grid-template-columns: 1fr 1fr;">
                  <button class="preset-btn active" id="l9PreCubicLine" onclick="setL9Preset('cubicLine')">
                    <span>1. 3차곡선 & 직선 (메인)</span>
                    <span class="p-sub">$f=x(x-2)^2, g=x \to S = \frac{37}{12}$</span>
                  </button>
                  <button class="preset-btn" id="l9PreQuadLine" onclick="setL9Preset('quadLine')">
                    <span>2. 포물선 & 직선 (예제 4)</span>
                    <span class="p-sub">$f=x^2-3x-2, g=-x+1 \to S = \frac{32}{3}$</span>
                  </button>
                  <button class="preset-btn" id="l9PreSingleParabola" onclick="setL9Preset('singleParabola')">
                    <span>3. 단일 포물선과 $x$축 (예제 1)</span>
                    <span class="p-sub">$y=x^2-5x \to S = -\int_0^5 = \frac{125}{6}$</span>
                  </button>
                  <button class="preset-btn" id="l9PreSymmetricCubic" onclick="setL9Preset('symmetricCubic')">
                    <span>4. 3차 대칭형 (예제 2)</span>
                    <span class="p-sub">$y=x^3-x \to S_1=1/4, S_2=1/4, S=1/2$</span>
                  </button>
                </div>
              </div>

              <!-- Parameter Sliders -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎛️ 동적 파라미터 조절 &amp; 카발리에리 단면 탐침</span>
                </div>

                <div class="slider-row">
                  <label>직선 기울기 $m$: <strong id="l9mVal" style="color: #f59e0b;">1.0</strong></label>
                  <input type="range" id="l9SliderM" min="-2.0" max="3.0" step="0.2" value="1.0" oninput="updateL9Sliders()">
                </div>

                <div class="slider-row">
                  <label>직선 $y$절편 $k$: <strong id="l9kVal" style="color: var(--accent-blue);">0.0</strong></label>
                  <input type="range" id="l9SliderK" min="-4.0" max="4.0" step="0.5" value="0.0" oninput="updateL9Sliders()">
                </div>

                <div class="slider-row">
                  <label>단면 검증기 탐침 $x_0$: <strong id="l9probeVal" style="color: var(--accent-gold);">0.50</strong></label>
                  <input type="range" id="l9SliderProbe" min="0.0" max="3.0" step="0.05" value="0.5" oninput="updateL9Sliders()">
                </div>
              </div>

              <!-- Live Math Box -->
              <div class="control-card" style="background: rgba(245, 158, 11, 0.05); border-color: rgba(245, 158, 11, 0.25);">
                <div class="control-header">
                  <span class="control-title" style="color: #f59e0b;">📊 실시간 정적분 vs 기하학적 넓이 대조</span>
                </div>

                <div class="metric-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 12px;">
                  <div class="metric-card m1">
                    <div class="metric-label">영역 $S_1$ (윗구간)</div>
                    <div class="metric-val" id="l9ValS1" style="color: #34d399;">5/12 (0.42)</div>
                    <div class="metric-sub">양수 적분 구간</div>
                  </div>
                  <div class="metric-card m2">
                    <div class="metric-label">영역 $S_2$ (아랫구간)</div>
                    <div class="metric-val" id="l9ValS2" style="color: #f59e0b;">8/3 (2.67)</div>
                    <div class="metric-sub">음수 $\to -$부호 반전</div>
                  </div>
                </div>

                <div class="metric-grid" style="grid-template-columns: 1fr 1fr;">
                  <div class="metric-card m3">
                    <div class="metric-label">기하학적 총 넓이 ($S$)</div>
                    <div class="metric-val" id="l9ValTotalS" style="color: var(--accent-gold); font-size: 1.3rem;">37/12 (3.08)</div>
                    <div class="metric-sub">$S = S_1 + S_2$ (항상 $\ge 0$)</div>
                  </div>
                  <div class="metric-card" style="border-color: rgba(239, 68, 68, 0.4);">
                    <div class="metric-label">단면 세로 높이 $|f - g|$</div>
                    <div class="metric-val" id="l9ValHeight" style="color: #ef4444;">0.625</div>
                    <div class="metric-sub">카발리에리 불변 높이</div>
                  </div>
                </div>

                <div id="l9LiveEquation" style="margin-top: 14px; padding: 10px; background: rgba(0,0,0,0.3); border-radius: 8px; font-size: 0.88rem; color: #cbd5e1; text-align: center;">
                  차함수: $h(x) = x(x-1)(x-3) = x^3 - 4x^2 + 3x$ (교점: $0, 1, 3$)
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: TIMELINE CAPTURES (LECTURE 9) -->
      <div id="l9CaptureTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; margin-bottom: 8px; color: var(--accent-gold);">
            📸 사오수학 강의 12단계 판서 타임라인 &amp; 교재 해설
          </h2>
          <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 24px;">
            유튜브 원본 영상(10:36)의 핵심 개념과 문제 풀이 전 과정을 1080p 고화질 캡처와 함께 완벽히 분석했습니다.
          </p>

          <div class="timeline-container">
            <!-- Card 1 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">1단계 [00:00:17]</span>
                <span class="timeline-title">$y = x^2 - 5x$와 $x$축으로 둘러싸인 도형 넓이 문제 세팅</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/01_parabola_x_axis_problem.jpg" alt="01_parabola_x_axis_problem">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "0과 5를 근으로 갖는 2차식이 그려져 있죠. 이 그래프와 $x$축으로 둘러싸인 도형의 넓이를 $S$라고 할 때, $S$를 구하는 과정이 어떻게 되는지 지금부터 설명해 드리겠습니다."
              </div>
              <div class="timeline-desc">
                <strong>해설:</strong> $y = x(x-5)$는 아래로 볼록한 포물선이며, $0 \le x \le 5$ 구간 전체가 $x$축 아래에 위치합니다.
              </div>
            </div>

            <!-- Card 2 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">2단계 [00:00:55]</span>
                <span class="timeline-title">정적분과 음수 넓이: 마이너스 붙이기의 필연성</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/02_integral_negative_area.jpg" alt="02_integral_negative_area">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "0부터 5까지 적분하면 $S$가 나오긴 하는데 문제는 정적분은 플러스 마이너스가 있어요. $x$축 밑의 넓이는 다 마이너스가 붙어 나옵니다. 그래서 $S$를 구하려면 양변에 마이너스를 붙여줘야 합니다."
              </div>
              <div class="timeline-desc">
                <strong>수식 전개:</strong> $\int_0^5 (x^2 - 5x)dx = -\frac{125}{6} \implies S = -\int_0^5 (x^2 - 5x)dx = \mathbf{\frac{125}{6}}$.
              </div>
            </div>

            <!-- Card 3 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">3단계 [00:01:40]</span>
                <span class="timeline-title">일반 함수 $f(x)$의 부호 분할 (별 $\star$과 세모 $\blacktriangle$)</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/03_concept_general_split.jpg" alt="03_concept_general_split">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "함수가 $x$축과 두 군데에서 영역을 만들 때, 하나를 별($\star$), 하나를 세모($\blacktriangle$)라고 해봅시다. 넓이를 구하라고 하면 별과 세모를 더해야 합니다. 별은 $x$축 윗부분이고, 세모는 아랫부분입니다."
              </div>
              <div class="timeline-desc">
                <strong>해설:</strong> $[a, b]$ 구간은 $f(x) \ge 0$이므로 순수 정적분이 곧 넓이($\star$)입니다. $[b, c]$ 구간은 $f(x) \le 0$이므로 순수 정적분 결과는 음수($-\blacktriangle$)입니다.
              </div>
            </div>

            <!-- Card 4 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">4단계 [00:02:20]</span>
                <span class="timeline-title">넓이 공식 정형화: $\text{넓이} = \int_a^b f(x)dx - \int_b^c f(x)dx$</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/04_formula_summary_split.jpg" alt="04_formula_summary_split">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "세모는 음수로 나오기 때문에 그냥 적분해버리면 안 되고 앞에 마이너스를 붙여야 양수가 됩니다. 그래서 전체 넓이는 $\int_a^b f(x)dx - \int_b^c f(x)dx$가 됩니다. 넓이는 항상 양수입니다!"
              </div>
              <div class="timeline-desc">
                <strong>핵심 정리:</strong> 기하학적 넓이는 항상 $S \ge 0$이어야 하므로, 음의 영역에 $-$ 부호를 취하여 상쇄합니다.
              </div>
            </div>

            <!-- Card 5 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">5단계 [00:03:25]</span>
                <span class="timeline-title">예제 2: 3차함수와 $x$축 사이 양·음 구간 공존</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/05_example2_cubic_both_sides.jpg" alt="05_example2_cubic_both_sides">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "$-1$부터 $0$까지는 $x$축보다 윗부분 넓이니까 그냥 플러스로 나오고, $0$부터 $1$까지는 $x$축 아래에 있으니까 음수로 나와서 다시 앞에 마이너스를 곱해줘야 플러스가 됩니다."
              </div>
              <div class="timeline-desc">
                <strong>구간 분할:</strong> $S = S_1 + S_2 = \int_{-1}^0 f(x)dx + \left( -\int_0^1 f(x)dx \right)$.
              </div>
            </div>

            <!-- Card 6 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">6단계 [00:04:15]</span>
                <span class="timeline-title">예제 2 계산 완결: 넓이 $S = 2$</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/06_example2_solution.jpg" alt="06_example2_solution">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "안에 있는 함수들의 부정적분을 구해서 대입 계산을 해 주면 각각 1이 나와서 최종 정답은 2가 됩니다."
              </div>
              <div class="timeline-desc">
                <strong>계산 결과:</strong> $S_1 = 1, S_2 = 1 \implies S = S_1 + S_2 = \mathbf{2}$.
              </div>
            </div>

            <!-- Card 7 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">7단계 [00:05:05]</span>
                <span class="timeline-title">두 곡선 사이의 넓이 등장 ($y = x(x-2)^2$과 $y = x$)</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/07_two_curves_intersection.jpg" alt="07_two_curves_intersection">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "이번에는 3차식과 $y = x$라는 두 곡선으로 둘러싸인 도형의 넓이입니다. 어떤 함수와 $x$축이 아니라 두 함수 사이의 넓이를 구하라고 할 때 어떻게 푸는지 잘 보세요."
              </div>
              <div class="timeline-desc">
                <strong>문제 상황:</strong> 3차 곡선 $f(x) = x(x-2)^2$과 직선 $g(x) = x$가 교점들을 형성하며 두 개의 둘러싸인 영역을 만듭니다.
              </div>
            </div>

            <!-- Card 8 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">8단계 [00:06:00]</span>
                <span class="timeline-title">차함수 $h(x) = f(x) - g(x)$의 마법</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/08_diff_function_concept.jpg" alt="08_diff_function_concept">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "두 그래프 사이의 넓이를 구할 때 가장 먼저 해야 할 것은 두 함수를 빼는 것입니다. $f(x) - g(x)$를 만들어주면 교점 $a, b, c$는 함숫값이 같으므로 빼면 무조건 0이 됩니다!"
              </div>
              <div class="timeline-desc">
                <strong>차함수의 본질:</strong> 교점 $x = a, b, c \iff f(x) = g(x) \iff f(x) - g(x) = 0$. 즉 교점은 차함수 $h(x)$의 $x$절편이 됩니다.
              </div>
            </div>

            <!-- Card 9 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">9단계 [00:06:50]</span>
                <span class="timeline-title">기하학적 넓이 불변성의 원리 (Area Invariance)</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/09_diff_function_area_invariance.jpg" alt="09_diff_function_area_invariance">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "여기서 생긴 두 개의 넓이가 그대로 $S_1$이랑 $S_2$로 내려옵니다! 위에 있던 $g(x)$가 $x$축이 되었다고 생각하시면 됩니다. 넓이는 그대로 내려옵니다."
              </div>
              <div class="timeline-desc">
                <strong>카발리에리의 원리:</strong> 모든 $x$에서 세로 높이 $|f(x) - g(x)|$가 하단의 $|h(x)|$와 같으므로 적분 넓이는 100% 동일합니다.
              </div>
            </div>

            <!-- Card 10 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">10단계 [00:08:25]</span>
                <span class="timeline-title">3차 차함수의 인수분해와 교점 도출</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/10_example3_diff_factorization.jpg" alt="10_example3_diff_factorization">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "각각의 그래프를 굳이 그릴 필요가 없습니다! 둘을 뺀 함수를 구하면 $x^3 - 4x^2 + 3x$가 되고, 인수분해하면 근이 0, 1, 3이 나옵니다. 0, 1, 3을 지나는 3차 함수만 그리면 끝납니다."
              </div>
              <div class="timeline-desc">
                <strong>수식 전개:</strong> $h(x) = x(x-2)^2 - x = x^3 - 4x^2 + 3x = x(x-1)(x-3) = 0 \implies x = 0, 1, 3$.
              </div>
            </div>

            <!-- Card 11 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">11단계 [00:09:15]</span>
                <span class="timeline-title">3차 차함수 넓이 계산 완결 ($S = \frac{37}{12}$)</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/11_example3_area_calculation.jpg" alt="11_example3_area_calculation">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "0부터 1까지는 $x$축 위에 있으니까 플러스, 1부터 3까지는 $x$축 아래니까 마이너스. 각각 정적분하면 12분의 5와 3분의 8이 나와서 둘을 더하면 12분의 37이 됩니다."
              </div>
              <div class="timeline-desc">
                <strong>적분 계산:</strong> $S_1 = \frac{5}{12}, S_2 = \frac{8}{3} = \frac{32}{12} \implies \mathbf{S = \frac{37}{12}}$.
              </div>
            </div>

            <!-- Card 12 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">12단계 [00:10:10]</span>
                <span class="timeline-title">예제 4: 2차곡선과 직선의 넓이 & 차수 팁</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v9/12_example4_parabola_line.jpg" alt="12_example4_parabola_line">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "뺄 때 차수가 높은 것에서 낮은 것을 빼는 게 좋습니다. 그래야 최고차항 부호가 양수로 유지되어 그래프가 뒤집히지 않습니다. $(x+1)(x-3)$이므로 근은 -1과 3입니다. 적분하면 3분의 32가 나옵니다."
              </div>
              <div class="timeline-desc">
                <strong>공식 검산:</strong> $S = \frac{|a|}{6}(\beta - \alpha)^3 = \frac{1}{6}(3 - (-1))^3 = \frac{64}{6} = \mathbf{\frac{32}{3}}$ (완벽 일치!).
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: PROOF & CSAT LINK (LECTURE 9) -->
      <div id="l9ProofTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px; color: var(--accent-gold);">
            📐 수학교과서식 정형화 &amp; 수능 기출 킬러 연계 분석
          </h2>

          <div style="margin-bottom: 24px;">
            <h3 style="color: var(--accent-blue); font-size: 1.15rem; margin-bottom: 8px;">1. 정적분의 정의와 카발리에리 원리에 의한 차함수 면적 불변성</h3>
            <p style="color: var(--text-muted); font-size: 0.94rem; line-height: 1.7;">
              두 연속함수 $f(x)$와 $g(x)$로 둘러싸인 도형의 넓이 $S$는 리만 합(Riemann Sum)에 의해 다음과 같이 정의됩니다:
              $$S = \lim_{n \to \infty} \sum_{k=1}^n |f(x_k^*) - g(x_k^*)| \Delta x = \int_a^b |f(x) - g(x)| dx$$
              여기서 새로운 함수 $h(x) \equiv f(x) - g(x)$로 치환하면, $x$축($y = 0$)과의 차이는 $|h(x) - 0| = |h(x)|$가 됩니다.
              즉, 임의의 $x$에서 두 곡선 사이의 수직 선분 길이와 차함수와 $x$축 사이의 수직 선분 길이가 완전히 동일하므로,
              기울어진 임의의 기준선 $y = g(x)$를 수평의 $x$축으로 전단(Shear) 변환해도 적분 면적은 엄밀하게 보존됩니다.
            </p>
          </div>

          <div style="margin-bottom: 24px;">
            <h3 style="color: var(--accent-green); font-size: 1.15rem; margin-bottom: 8px;">2. 수능 실전 4대 다항함수 넓이 초고속 공식집</h3>
            <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-color); border-radius: 12px; padding: 18px;">
              <ul style="list-style: none; padding-left: 0; display: flex; flex-direction: column; gap: 12px; font-size: 0.94rem;">
                <li>
                  <strong style="color: var(--accent-gold);">① 포물선과 직선 (두 교점 $\alpha, \beta$):</strong>
                  $$S = \frac{|a|}{6}(\beta - \alpha)^3$$
                  $\to$ 예제 4 검산: $\frac{1}{6}(3 - (-1))^3 = \frac{64}{6} = \frac{32}{3}$ (1초 컷!)
                </li>
                <li>
                  <strong style="color: var(--accent-blue);">② 3차함수와 접선 (접점 $\alpha$, 교점 $\beta$):</strong>
                  $$S = \frac{|a|}{12}(\beta - \alpha)^4$$
                </li>
                <li>
                  <strong style="color: var(--accent-purple);">③ 4차함수와 이중접선 (두 접점 $\alpha, \beta$):</strong>
                  $$S = \frac{|a|}{30}(\beta - \alpha)^5$$
                </li>
                <li>
                  <strong style="color: #34d399;">④ 3차함수의 변곡점 대칭 정적분 상쇄:</strong>
                  $$\int_{\text{변곡점}-p}^{\text{변곡점}+p} h(x)dx = 0 \iff S_1 = S_2$$
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 4: MANIM SCRIPT (LECTURE 9) -->
      <div id="l9ManimTab" class="tab-panel">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.4rem; color: var(--accent-purple);">🎬 3Blue1Brown 스타일 Manim 파이썬 코드</h2>
              <p style="color: var(--text-dim); font-size: 0.85rem;">정적분과 넓이 & 차함수 불변 변환 애니메이션 (Python Manim Community v0.18+)</p>
            </div>
            <button class="tab-btn active" onclick="copyL9ManimCode()" style="padding: 8px 16px; font-size: 0.82rem;">
              📋 코드 복사
            </button>
          </div>

          <div style="background: #080d17; border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; overflow-x: auto;">
            <pre><code id="l9ManimCodeBlock" style="font-family: 'JetBrains Mono', monospace; font-size: 0.84rem; color: #e2e8f0; line-height: 1.6;">''' + manim_code_escaped + r'''</code></pre>
          </div>
        </div>
      </div>
    </div>
    <!-- END LECTURE 9 VIEW -->

'''

    # Insert lecture9_html right before <div id="lecture8View"
    target_insert_point = '<div id="lecture8View"'
    if target_insert_point not in content:
        print("ERROR: target_insert_point not found!")
        return

    content = content.replace(target_insert_point, lecture9_html + '\n    ' + target_insert_point, 1)

    # 5. Update JavaScript logic:
    # Update setLecture(num) to support 9 lectures
    old_set_lecture = '''    function setLecture(num) {
      for (let i = 1; i <= 8; i++) {
        const btn = document.getElementById(`btnLec${i}`);
        const view = document.getElementById(`lecture${i}View`);
        if (btn) btn.classList.toggle('active', i === num);
        if (view) view.style.display = (i === num) ? 'block' : 'none';
      }

      if (num === 8) setTimeout(renderL8, 50);
      else if (num === 7) setTimeout(renderL7, 50);
      else if (num === 6) setTimeout(renderL6, 50);
      else if (num === 5) setTimeout(renderL5, 50);
      else if (num === 4) setTimeout(renderL4, 50);
      else if (num === 3) setTimeout(renderL3, 50);
      else if (num === 2) setTimeout(renderL2, 50);
      else if (num === 1) setTimeout(renderL1, 50);'''

    new_set_lecture = '''    function setLecture(num) {
      for (let i = 1; i <= 9; i++) {
        const btn = document.getElementById(`btnLec${i}`);
        const view = document.getElementById(`lecture${i}View`);
        if (btn) btn.classList.toggle('active', i === num);
        if (view) view.style.display = (i === num) ? 'block' : 'none';
      }

      if (num === 9) setTimeout(renderL9, 50);
      else if (num === 8) setTimeout(renderL8, 50);
      else if (num === 7) setTimeout(renderL7, 50);
      else if (num === 6) setTimeout(renderL6, 50);
      else if (num === 5) setTimeout(renderL5, 50);
      else if (num === 4) setTimeout(renderL4, 50);
      else if (num === 3) setTimeout(renderL3, 50);
      else if (num === 2) setTimeout(renderL2, 50);
      else if (num === 1) setTimeout(renderL1, 50);'''

    if old_set_lecture not in content:
        print("ERROR: old_set_lecture not found!")
        return

    content = content.replace(old_set_lecture, new_set_lecture, 1)

    # 6. Add switchLec9Tab and Lecture 9 JavaScript logic right before Lecture 8 logic
    l9_js_logic = r'''    /* ========================================================= */
    /* LECTURE 9 (DEFINITE INTEGRAL & AREA: DIFF FUNCTION) LOGIC */
    /* ========================================================= */
    function switchLec9Tab(tabId) {
      document.querySelectorAll('#lecture9View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture9View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l9SimTab') setTimeout(renderL9, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function copyL9ManimCode() {
      const code = document.getElementById('l9ManimCodeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('3Blue1Brown Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }

    const l9State = {
      preset: 'cubicLine', // 'cubicLine', 'quadLine', 'singleParabola', 'symmetricCubic'
      m: 1.0,
      k: 0.0,
      probeX: 0.5
    };

    function setL9Preset(pre) {
      l9State.preset = pre;
      document.querySelectorAll('#lecture9View .preset-grid .preset-btn').forEach(b => b.classList.remove('active'));
      if (pre === 'cubicLine') {
        document.getElementById('l9PreCubicLine').classList.add('active');
        l9State.m = 1.0; l9State.k = 0.0; l9State.probeX = 0.5;
      } else if (pre === 'quadLine') {
        document.getElementById('l9PreQuadLine').classList.add('active');
        l9State.m = -1.0; l9State.k = 1.0; l9State.probeX = 1.0;
      } else if (pre === 'singleParabola') {
        document.getElementById('l9PreSingleParabola').classList.add('active');
        l9State.m = 0.0; l9State.k = 0.0; l9State.probeX = 2.5;
      } else if (pre === 'symmetricCubic') {
        document.getElementById('l9PreSymmetricCubic').classList.add('active');
        l9State.m = 0.0; l9State.k = 0.0; l9State.probeX = -0.5;
      }

      document.getElementById('l9SliderM').value = l9State.m;
      document.getElementById('l9SliderK').value = l9State.k;
      document.getElementById('l9SliderProbe').value = l9State.probeX;
      updateL9Sliders();
    }

    function updateL9Sliders() {
      l9State.m = parseFloat(document.getElementById('l9SliderM').value);
      l9State.k = parseFloat(document.getElementById('l9SliderK').value);
      l9State.probeX = parseFloat(document.getElementById('l9SliderProbe').value);

      document.getElementById('l9mVal').innerText = l9State.m.toFixed(1);
      document.getElementById('l9kVal').innerText = l9State.k.toFixed(1);
      document.getElementById('l9probeVal').innerText = l9State.probeX.toFixed(2);

      renderL9();
    }

    function renderL9() {
      const canvas = document.getElementById('l9Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const pre = l9State.preset;
      const m = l9State.m;
      const k = l9State.k;
      const probeX = l9State.probeX;

      // Mathematical definitions:
      // f(x), g(x), h(x) = f(x) - g(x)
      let f, g, h_diff, xMin, xMax, yMinTop, yMaxTop, yMinBot, yMaxBot;
      let r1, r2, r3, eqDesc, s1_val, s2_val, totalS;

      if (pre === 'cubicLine') {
        // f(x) = x(x-2)^2, g(x) = m*x + k (Default: g(x) = x)
        f = (x) => x * Math.pow(x - 2, 2);
        g = (x) => m * x + k;
        h_diff = (x) => f(x) - g(x);
        xMin = -0.6; xMax = 3.6;
        yMinTop = -1.5; yMaxTop = 5.2;
        yMinBot = -3.2; yMaxBot = 2.2;
        r1 = 0; r2 = 1; r3 = 3; // for default
        s1_val = 5/12; s2_val = 8/3; totalS = 37/12;
        eqDesc = `3차곡선 $f(x)=x(x-2)^2$ vs 직선 $g(x)=x$ $\\to$ 차함수 $h(x)=x(x-1)(x-3)$`;
      } else if (pre === 'quadLine') {
        // f(x) = x^2 - 3x - 2, g(x) = m*x + k (Default: -x + 1)
        f = (x) => x*x - 3*x - 2;
        g = (x) => m*x + k;
        h_diff = (x) => f(x) - g(x);
        xMin = -2.2; xMax = 4.2;
        yMinTop = -5.0; yMaxTop = 4.0;
        yMinBot = -5.0; yMaxBot = 2.0;
        r1 = -1; r2 = 3; r3 = null;
        s1_val = 32/3; s2_val = 0; totalS = 32/3;
        eqDesc = `포물선 $f(x)=x^2-3x-2$ vs 직선 $g(x)=-x+1$ $\\to$ 차함수 $h(x)=(x+1)(x-3)$`;
      } else if (pre === 'singleParabola') {
        f = (x) => x*x - 5*x;
        g = (x) => 0;
        h_diff = (x) => f(x);
        xMin = -1.0; xMax = 6.0;
        yMinTop = -7.5; yMaxTop = 4.0;
        yMinBot = -7.5; yMaxBot = 4.0;
        r1 = 0; r2 = 5; r3 = null;
        s1_val = 125/6; s2_val = 0; totalS = 125/6;
        eqDesc = `포물선 $f(x)=x^2-5x$와 $x$축 $\\to S = -\\int_0^5 (x^2-5x)dx = 125/6$`;
      } else { // symmetricCubic
        f = (x) => x*x*x - x;
        g = (x) => 0;
        h_diff = (x) => f(x);
        xMin = -1.6; xMax = 1.6;
        yMinTop = -1.5; yMaxTop = 1.5;
        yMinBot = -1.5; yMaxBot = 1.5;
        r1 = -1; r2 = 0; r3 = 1;
        s1_val = 0.25; s2_val = 0.25; totalS = 0.5;
        eqDesc = `3차 대칭형 $f(x)=x^3-x$ $\\to S_1 = \\int_{-1}^0 f dx = 0.25, S_2 = -\\int_0^1 f dx = 0.25$`;
      }

      // Update text in UI
      const eqEl = document.getElementById('l9LiveEquation');
      if (eqEl) {
        eqEl.innerHTML = eqDesc;
        if (window.renderMathInElement) {
          renderMathInElement(eqEl, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
        }
      }

      // Height probe calc
      const curProbeF = f(probeX);
      const curProbeG = g(probeX);
      const curProbeH = Math.abs(curProbeF - curProbeG);
      document.getElementById('l9ValHeight').innerText = curProbeH.toFixed(3);

      // Split Canvas: Top Panel (0 to h/2 - 10), Bottom Panel (h/2 + 10 to h)
      const padX = 40;
      const topH = h * 0.48;
      const botH = h * 0.48;
      const botY0 = h * 0.52;

      // Coordinate helper functions
      function toTopX(rx) { return padX + ((rx - xMin) / (xMax - xMin)) * (w - padX * 2); }
      function toTopY(ry) { return 25 + ((yMaxTop - ry) / (yMaxTop - yMinTop)) * (topH - 35); }
      function toBotX(rx) { return padX + ((rx - xMin) / (xMax - xMin)) * (w - padX * 2); }
      function toBotY(ry) { return botY0 + 25 + ((yMaxBot - ry) / (yMaxBot - yMinBot)) * (botH - 35); }

      // 1. TOP PANEL: Background & Grid
      ctx.fillStyle = '#0b1120';
      ctx.fillRect(0, 0, w, topH);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
      ctx.lineWidth = 1;
      ctx.strokeRect(0, 0, w, topH);

      // Title Top Panel
      ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('TOP: 곡선 y = f(x) vs 기준선 y = g(x)', padX, 20);

      // Top Axes (x-axis & y-axis)
      const topAxisY = toTopY(0);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(padX, topAxisY); ctx.lineTo(w - padX, topAxisY);
      ctx.stroke();

      // Top Shading between curves
      const steps = 300;
      for (let i = 0; i < steps; i++) {
        const x1 = xMin + (i / steps) * (xMax - xMin);
        const x2 = xMin + ((i + 1) / steps) * (xMax - xMin);
        const y1_f = f(x1), y1_g = g(x1);
        const y2_f = f(x2), y2_g = g(x2);

        // Check region
        let inRegion = false, color = 'rgba(52, 211, 153, 0.35)'; // green
        if (pre === 'cubicLine') {
          if (x1 >= 0 && x2 <= 1) { inRegion = true; color = 'rgba(52, 211, 153, 0.4)'; }
          else if (x1 >= 1 && x2 <= 3) { inRegion = true; color = 'rgba(245, 158, 11, 0.4)'; }
        } else if (pre === 'quadLine') {
          if (x1 >= -1 && x2 <= 3) { inRegion = true; color = 'rgba(245, 158, 11, 0.4)'; }
        } else if (pre === 'singleParabola') {
          if (x1 >= 0 && x2 <= 5) { inRegion = true; color = 'rgba(239, 68, 68, 0.4)'; }
        } else {
          if (x1 >= -1 && x2 <= 0) { inRegion = true; color = 'rgba(52, 211, 153, 0.4)'; }
          else if (x1 >= 0 && x2 <= 1) { inRegion = true; color = 'rgba(239, 68, 68, 0.4)'; }
        }

        if (inRegion) {
          ctx.fillStyle = color;
          ctx.beginPath();
          ctx.moveTo(toTopX(x1), toTopY(y1_f));
          ctx.lineTo(toTopX(x2), toTopY(y2_f));
          ctx.lineTo(toTopX(x2), toTopY(y2_g));
          ctx.lineTo(toTopX(x1), toTopY(y1_g));
          ctx.closePath();
          ctx.fill();
        }
      }

      // Plot f(x) curve (Blue)
      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let px = 0; px <= w - padX * 2; px++) {
        const curX = xMin + (px / (w - padX * 2)) * (xMax - xMin);
        const curY = f(curX);
        const sx = padX + px, sy = toTopY(curY);
        if (px === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Plot g(x) curve (Red/Orange)
      ctx.strokeStyle = '#f87171'; ctx.lineWidth = 2; ctx.beginPath();
      for (let px = 0; px <= w - padX * 2; px++) {
        const curX = xMin + (px / (w - padX * 2)) * (xMax - xMin);
        const curY = g(curX);
        const sx = padX + px, sy = toTopY(curY);
        if (px === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // 2. BOTTOM PANEL: Diff-Function h(x) = f(x) - g(x)
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, botY0, w, botH);
      ctx.strokeStyle = 'rgba(245, 158, 11, 0.15)';
      ctx.lineWidth = 1;
      ctx.strokeRect(0, botY0, w, botH);

      // Title Bottom Panel
      ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('BOTTOM: 차함수 y = f(x) - g(x) (x축 평탄화 및 면적 보존)', padX, botY0 + 20);

      // Bottom x-axis
      const botAxisY = toBotY(0);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)'; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padX, botAxisY); ctx.lineTo(w - padX, botAxisY);
      ctx.stroke();

      // Bottom Shading between h(x) and x-axis
      for (let i = 0; i < steps; i++) {
        const x1 = xMin + (i / steps) * (xMax - xMin);
        const x2 = xMin + ((i + 1) / steps) * (xMax - xMin);
        const y1_h = h_diff(x1), y2_h = h_diff(x2);

        let inRegion = false, color = 'rgba(52, 211, 153, 0.4)';
        if (pre === 'cubicLine') {
          if (x1 >= 0 && x2 <= 1) { inRegion = true; color = 'rgba(52, 211, 153, 0.4)'; }
          else if (x1 >= 1 && x2 <= 3) { inRegion = true; color = 'rgba(245, 158, 11, 0.4)'; }
        } else if (pre === 'quadLine') {
          if (x1 >= -1 && x2 <= 3) { inRegion = true; color = 'rgba(245, 158, 11, 0.4)'; }
        } else if (pre === 'singleParabola') {
          if (x1 >= 0 && x2 <= 5) { inRegion = true; color = 'rgba(239, 68, 68, 0.4)'; }
        } else {
          if (x1 >= -1 && x2 <= 0) { inRegion = true; color = 'rgba(52, 211, 153, 0.4)'; }
          else if (x1 >= 0 && x2 <= 1) { inRegion = true; color = 'rgba(239, 68, 68, 0.4)'; }
        }

        if (inRegion) {
          ctx.fillStyle = color;
          ctx.beginPath();
          ctx.moveTo(toBotX(x1), toBotY(y1_h));
          ctx.lineTo(toBotX(x2), toBotY(y2_h));
          ctx.lineTo(toBotX(x2), botAxisY);
          ctx.lineTo(toBotX(x1), botAxisY);
          ctx.closePath();
          ctx.fill();
        }
      }

      // Plot h(x) curve (Yellow/Gold)
      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let px = 0; px <= w - padX * 2; px++) {
        const curX = xMin + (px / (w - padX * 2)) * (xMax - xMin);
        const curY = h_diff(curX);
        const sx = padX + px, sy = toBotY(curY);
        if (px === 0) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // 3. Connect Intersection Roots with Vertical Dashed Lines
      const roots = [r1, r2, r3].filter(r => r !== null);
      roots.forEach(rx => {
        const topPx = toTopX(rx);
        ctx.strokeStyle = 'rgba(251, 191, 36, 0.5)';
        ctx.lineWidth = 1.2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(topPx, toTopY(g(rx)));
        ctx.lineTo(topPx, toBotY(0));
        ctx.stroke();
        ctx.setLineDash([]);

        // Root label
        ctx.fillStyle = '#fbbf24'; ctx.font = 'bold 11px JetBrains Mono, sans-serif';
        ctx.fillText(`x=${rx}`, topPx - 10, botAxisY + 16);
      });

      // 4. Cavalieri Height Probe Bar at probeX
      const pTopX = toTopX(probeX);
      const pTopY1 = toTopY(f(probeX));
      const pTopY2 = toTopY(g(probeX));

      // Upper probe line
      ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(pTopX, pTopY1); ctx.lineTo(pTopX, pTopY2); ctx.stroke();
      ctx.fillStyle = '#ef4444';
      ctx.beginPath(); ctx.arc(pTopX, pTopY1, 4, 0, Math.PI*2); ctx.fill();
      ctx.beginPath(); ctx.arc(pTopX, pTopY2, 4, 0, Math.PI*2); ctx.fill();

      // Lower probe line
      const pBotY1 = toBotY(h_diff(probeX));
      const pBotY2 = botAxisY;
      ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(pTopX, pBotY1); ctx.lineTo(pTopX, pBotY2); ctx.stroke();
      ctx.fillStyle = '#ef4444';
      ctx.beginPath(); ctx.arc(pTopX, pBotY1, 4, 0, Math.PI*2); ctx.fill();
      ctx.beginPath(); ctx.arc(pTopX, pBotY2, 4, 0, Math.PI*2); ctx.fill();

      // Probe connecting guide
      ctx.strokeStyle = 'rgba(239, 68, 68, 0.35)'; ctx.lineWidth = 1; ctx.setLineDash([2, 3]);
      ctx.beginPath(); ctx.moveTo(pTopX, Math.max(pTopY1, pTopY2)); ctx.lineTo(pTopX, Math.min(pBotY1, pBotY2)); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#fff'; ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText(`높이=${curProbeH.toFixed(2)}`, pTopX + 6, (pTopY1 + pTopY2) / 2);
      ctx.fillText(`높이=${curProbeH.toFixed(2)}`, pTopX + 6, (pBotY1 + pBotY2) / 2);
    }

'''

    l8_marker = '    /* ========================================================= */\n    /* LECTURE 8 (TRIG GRAPHS & 8-BOX METHOD) LOGIC              */'
    if l8_marker not in content:
        print("ERROR: l8_marker not found!")
        return

    content = content.replace(l8_marker, l9_js_logic + '\n' + l8_marker, 1)

    # 7. Update window load handler to initialize Lecture 9
    old_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      updateL8Sliders();
      renderL8();
    });'''

    new_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      updateL9Sliders();
      renderL9();
    });'''

    if old_load in content:
        content = content.replace(old_load, new_load, 1)

    # Write output to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: index.html updated successfully with Lecture 9!")

if __name__ == '__main__':
    main()
