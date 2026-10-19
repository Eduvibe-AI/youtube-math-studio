# -*- coding: utf-8 -*-
"""
Script to inject Lecture 7 (Essence of Trigonometric Functions: Math Dealer / Essence of Math) into index.html
Preserving all existing Lectures 1, 2, 3, 4, 5, 6 without alteration.
"""

import os

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the lecture switcher bar
    old_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (6 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec6" onclick="setLecture(6)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #ef4444, #f59e0b); color: #fff;">🔥 파이널 특강</span>
          수능 기하 총정리 (수학딜러)
        </button>'''

    new_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (7 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec7" onclick="setLecture(7)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #8b5cf6, #3b82f6); color: #fff;">✨ 본질 특강</span>
          삼각비에서 삼각함수까지 (매쓰의 본질)
        </button>
        <button class="lecture-btn" id="btnLec6" onclick="setLecture(6)">
          수능 기하 총정리 (수학딜러)
        </button>'''

    if old_switcher_head not in content:
        print("ERROR: old_switcher_head not found in index.html!")
        return

    content = content.replace(old_switcher_head, new_switcher_head, 1)

    # Update captured_summary button from 1~6 to 1~7
    content = content.replace('📸 사진 1~6 핵심 전용 페이지', '📸 사진 1~7 핵심 전용 페이지', 1)

    # 2. Update lecture6View to start hidden:
    old_lec6_start = '<div id="lecture6View">'
    new_lec6_start = '<div id="lecture6View" style="display: none;">'
    if old_lec6_start not in content:
        print("ERROR: old_lec6_start not found!")
        return

    content = content.replace(old_lec6_start, new_lec6_start, 1)

    # 3. Read the Manim script to include in Tab 4
    with open('trig_functions_essence_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()
    manim_code_escaped = manim_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # 4. Lecture 7 Section HTML
    lecture7_html = r'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 7 (ESSENCE OF TRIG FUNCTIONS: MATHE OF ESSENCE) -->
    <!-- ============================================================== -->
    <div id="lecture7View">
      <header>
        <div class="badge-pill" style="border-color: rgba(139, 92, 246, 0.4); color: var(--accent-purple); box-shadow: 0 0 20px rgba(139, 92, 246, 0.3);">
          <span>📐 고등 수학 I · 미적분 · 삼각함수의 수학적 기원과 본질</span>
        </div>
        <h1 style="background: linear-gradient(135deg, #ffffff 30%, #c084fc 70%, #38bdf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          삼각비부터 삼각함수까지 — 수학적 일반화와 호도법의 본질
        </h1>
        <p class="subtitle">
          직각삼각형의 변의 비에서 단위원 위의 좌표 $P(\cos\theta, \sin\theta)$, 그리고 실수 전체를 정의역으로 하는 함수와 자연스러운 미분 $(\sin x)' = \cos x$까지의 <strong>위대한 수학적 추상화의 정수</strong>를 인터랙티브하게 체험합니다.
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>매쓰의 본질</strong></span>
          <span>•</span>
          <a href="https://youtu.be/DTKyrAyLWb8" target="_blank" rel="noopener">
            <span>YouTube 본 영상 보기 (16분 19초)</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
        </div>
      </header>

      <!-- Tab Bar for Lecture 7 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec7Tab('l7SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 삼각함수 스튜디오 (단위원 & 파형)
        </button>
        <button class="tab-btn" onclick="switchLec7Tab('l7CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 & 12단계 타임라인
        </button>
        <button class="tab-btn" onclick="switchLec7Tab('l7ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          수학교과서식 정형화 & 극한·미분 엄밀 증명
        </button>
        <button class="tab-btn" onclick="switchLec7Tab('l7ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 7) -->
      <div id="l7SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Dynamic Banner -->
          <div class="formula-banner" id="l7Banner" style="background: linear-gradient(135deg, rgba(192, 132, 252, 0.12), rgba(56, 189, 248, 0.08)); border-color: rgba(192, 132, 252, 0.35);">
            <div class="label" id="l7BannerLabel" style="color: var(--accent-purple);">🌟 삼각함수 핵심 불변 정의식</div>
            <div class="math-main" id="l7BannerMath">
              $$P(x, y) = (\cos\theta, \;\sin\theta) \quad\Big|\quad \theta = \frac{l}{r} \text{ (라디안)} \quad\Big|\quad \mathbf{\lim_{x \to 0}\frac{\sin x}{x} = 1 \implies (\sin x)' = \cos x}$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l7Canvas" width="560" height="520"></canvas>
              <div id="l7CanvasCaption" style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                단위원 위의 점 $P(\cos\theta, \sin\theta)$ 회전과 사인파($y = \sin x$) 실시간 생성 궤적
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Mode Selector -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎯 탐구 테마 선택</span>
                  <span class="badge-pill-sm" id="l7ActiveThemeBadge" style="background: var(--accent-purple); color: #fff;">1. 단위원 & 사인파</span>
                </div>
                <div class="preset-grid" style="grid-template-columns: 1fr 1fr;">
                  <button class="preset-btn active" id="l7BtnCircle" onclick="setL7Mode('circle')">
                    <span>1. 단위원 & 사인파 궤적</span>
                    <span class="p-sub">$P(\cos\theta, \sin\theta)$ & 파형 생성</span>
                  </button>
                  <button class="preset-btn" id="l7BtnRadian" onclick="setL7Mode('radian')">
                    <span>2. 호도법 (라디안) 언롤링</span>
                    <span class="p-sub">원호 길이 $\theta = l/r$ 실수화</span>
                  </button>
                  <button class="preset-btn" id="l7BtnCompare" onclick="setL7Mode('compare')">
                    <span>3. $\sin x$ vs $\sin x^\circ$</span>
                    <span class="p-sub">미적분과 도함수의 본질 차이</span>
                  </button>
                  <button class="preset-btn" id="l7BtnSigns" onclick="setL7Mode('signs')">
                    <span>4. 사분면 부호 (올사탄코)</span>
                    <span class="p-sub">좌표 $(x, y)$ 부호의 본질</span>
                  </button>
                </div>
              </div>

              <!-- Dynamic Sub-controls depending on mode -->
              <div class="control-card" id="l7SubControlCard">
                <!-- Injected via JavaScript based on mode -->
              </div>

              <!-- Live Numeric Analysis Card -->
              <div class="control-card" id="l7MetricCard">
                <!-- Injected via JavaScript based on mode -->
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: TIMELINE & CAPTURES (12 STEPS) -->
      <div id="l7CaptureTab" class="tab-panel">
        <div class="timeline-container">

          <!-- Step 1 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 1</span>
              <span class="timestamp">[00:01:10]</span>
              <span class="step-title">직각삼각형과 삼각비의 기원</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/01_trig_ratio_right_triangle.jpg" alt="직각삼각형과 삼각비의 기원">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"어떤 직각삼각형을 가져오더라도 빗변 분의 높이, 빗변 분의 밑변, 밑변 분의 높이라는 세 변 사이의 비율을 생각할 수 있습니다. 이것이 바로 우리가 중학교 때 처음 만나는 삼각비의 기원입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 삼각비의 기초 정의:</div>
                  <div class="math-highlight">$$\sin A = \frac{a}{c} = \frac{\text{높이}}{\text{빗변}}, \quad \cos A = \frac{b}{c} = \frac{\text{밑변}}{\text{빗변}}, \quad \tan A = \frac{a}{b} = \frac{\text{높이}}{\text{밑변}}$$</div>
                  <ul>
                    <li>고대 천문학과 측량술에서 거리를 직접 측정할 수 없을 때, 변의 비율을 통해 높이와 거리를 구하던 실용적 도구에서 출발했습니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 2 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 2</span>
              <span class="timestamp">[00:02:40]</span>
              <span class="step-title">닮음비와 각도-비율의 일대일 대응 (함수의 시작)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/02_angle_ratio_correspondence.jpg" alt="닮음비와 각도 비율 대응">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"직각삼각형의 크기가 아무리 커지거나 작아져도, 밑각의 크기 $x$가 정해지면 닮음에 의해 세 변 사이의 비율은 오직 하나로 유일하게 결정됩니다. 즉, 각도에서 비율로의 대응 관계가 생겨나는 것입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 기하학적 불변량:</div>
                  <ul>
                    <li>밑각 $x$가 같은 직각삼각형들은 모두 $AA$ 닮음입니다.</li>
                    <li>따라서 각도 $x$를 주면 그에 상응하는 비례값이 **단 하나로 결정**되므로, 수학자들은 이를 '함수(Function)'의 관점으로 바라보기 시작했습니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 3</span>
              <span class="timestamp">[00:04:30]</span>
              <span class="step-title">빗변의 길이가 1인 직각삼각형의 발견</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/03_unit_hypotenuse_triangle.jpg" alt="빗변의 길이가 1인 직각삼각형">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"직각삼각형의 빗변의 길이를 1로 고정해 봅시다. 그러면 $\sin x$의 값은 정의상 정확히 높이의 길이가 되고, $\cos x$의 값은 밑변의 길이가 됩니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 높이와 밑변의 직접 표기:</div>
                  <div class="math-highlight">$$\text{빗변 } = 1 \implies \text{높이 } = \sin x, \quad \text{밑변 } = \cos x$$</div>
                  <ul>
                    <li>분모를 1로 만드는 혁신적인 단순화를 통해, 삼각비는 복잡한 '분수 비율'에서 '선분의 길이' 그 자체로 승격됩니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 4 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 4</span>
              <span class="timestamp">[00:06:15]</span>
              <span class="step-title">각도의 확장과 직각삼각형의 한계(모순)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/04_angle_extension_dilemma.jpg" alt="각도의 확장과 직각삼각형 한계">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"수학이 발전하면서 $\sin 120^\circ, \sin 570^\circ, \sin(-30^\circ)$와 같은 각도에 대해서도 값을 정의하고 싶어졌습니다. 그런데 한 내각이 $120^\circ$이거나 음수인 직각삼각형은 세상에 존재할 수 없습니다. 여기서 거대한 모순과 장벽에 부딪히게 됩니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 삼각형 기하의 한계:</div>
                  <ul>
                    <li>직각삼각형의 두 예각의 합은 $90^\circ$이므로 $0^\circ < x < 90^\circ$를 벗어나는 순간 기하학적 정의가 붕괴합니다.</li>
                    <li>더 넓은 세계로 나아가기 위해선 '삼각형의 변'이라는 틀을 깨부수는 새로운 정의가 절실해졌습니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 5 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 5</span>
              <span class="timestamp">[00:07:45]</span>
              <span class="step-title">단위원(Unit Circle)과 동경의 회전을 통한 재정의</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/05_unit_circle_definition.jpg" alt="단위원과 동경 회전 재정의">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"수학자들은 삼각형이라는 껍질을 과감하게 깨부수었습니다. 원점 중심의 반지름 1인 원(단위원)에서 $x$축 양의 방향에서 반시계 방향으로 각도 $x$만큼 회전시킨 막대기가 원과 만나는 점의 $y$좌표와 $x$좌표를 각각 $\sin x, \cos x$로 아예 새롭게 정의해 버린 것입니다!"</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 현대 수학의 삼각함수 정의:</div>
                  <div class="math-highlight">$$\mathbf{P(x, y) = (\cos\theta, \;\sin\theta), \quad \tan\theta = \frac{y}{x} = \frac{\sin\theta}{\cos\theta}}$$</div>
                  <ul>
                    <li>회전각 $\theta$는 음수든 $360^\circ$ 이상이든 원주 위의 점 $P$로 항상 유일하게 대응됩니다!</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 6 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 6</span>
              <span class="timestamp">[00:08:45]</span>
              <span class="step-title">사분면 부호와 올-사-탄-코(All-Sin-Tan-Cos)의 본질</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/06_quadrant_signs_all_sin_tan_cos.jpg" alt="사분면 부호 올사탄코">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"길이는 음수가 될 수 없지만 좌표는 음수가 될 수 있습니다! 2사분면에서는 $x$좌표가 음수, $y$좌표가 양수이므로 $\cos$은 음수, $\sin$은 양수가 됩니다. 우리가 기계적으로 외우던 '올-사-탄-코'는 바로 좌표평면의 $(x, y)$ 부호 체계 그 자체입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 사분면 부호 불변 법칙:</div>
                  <ul>
                    <li>제1사분면 ($+, +$): $\text{All (+)}$</li>
                    <li>제2사분면 ($-, +$): $\sin\text{만 (+)}$</li>
                    <li>제3사분면 ($-, -$): $\tan = \frac{-}{-} = +\text{만 (+)}$</li>
                    <li>제4사분면 ($+, -$): $\cos\text{만 (+)}$</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 7 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 7</span>
              <span class="timestamp">[00:10:05]</span>
              <span class="step-title">육십분법(Degree)의 한계와 호도법(Radian)의 탄생</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/07_degree_vs_radian_origin.jpg" alt="육십분법 한계와 호도법 탄생">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"각도를 재는 고대 방식인 360도 법(육십분법)은 원 둘레를 임의로 360등분한 '단위'일 뿐입니다. 하지만 수학에서는 각도를 원의 반지름과 호의 길이의 비율로 정의하는 '호도법(Radian)'을 도입합니다. 반지름과 호의 길이가 같아질 때의 벌어진 각도를 1 라디안으로 정의합니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 호도법의 무차원 실수 정의:</div>
                  <div class="math-highlight">$$\theta = \frac{l}{r} \quad \left[\frac{\text{길이 [m]}}{\text{길이 [m]}} = \text{무차원 순수 실수}\right]$$</div>
                  <ul>
                    <li>단위원($r=1$)에서는 호의 길이 $l$이 곧 각도 $\theta$가 되어 기하학적 각이 수직선 위의 실수가 됩니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 8 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 8</span>
              <span class="timestamp">[00:10:50]</span>
              <span class="step-title">$180^\circ = \pi \text{ rad}$ 변환 공식과 특수각 일람</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/08_radian_conversion_formula.jpg" alt="180도는 파이 라디안 변환공식">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"원 전체의 중심각은 360도이고 원 둘레는 $2\pi r$이므로, $360^\circ = 2\pi \text{ rad}$, 즉 $180^\circ = \pi \text{ rad}$입니다. 여기서부터 $1^\circ = \frac{\pi}{180} \text{ rad}$, $1 \text{ rad} = \frac{180^\circ}{\pi} \approx 57.3^\circ$라는 변환식이 나옵니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 기본 특수각 변환:</div>
                  <div class="math-highlight">$$30^\circ = \frac{\pi}{6}, \quad 45^\circ = \frac{\pi}{4}, \quad 60^\circ = \frac{\pi}{3}, \quad 90^\circ = \frac{\pi}{2}, \quad 180^\circ = \pi$$</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 9 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 9</span>
              <span class="timestamp">[00:11:45]</span>
              <span class="step-title">각도 집합에서 실수 집합 $\mathbb{R}$로의 정의역 확장</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/09_real_number_domain_graph.jpg" alt="실수 집합 정의역 확장">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"삼각함수의 그래프를 그릴 때 $x$축은 '각도 축'이 아니라 '실수 축'입니다. 호도법을 통해 우리는 각도를 순수한 숫자(실수)로 다룰 수 있게 되었고, 비로소 삼각함수는 실수 전체 $\mathbb{R}$를 정의역으로 하는 진정한 함수의 형태를 갖추게 됩니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 해석학의 출발점:</div>
                  <ul>
                    <li>$x$축에 실수 $1, 2, \pi, \sqrt{2}$ 등을 대입할 수 있게 되면서, 삼각함수가 다항함수·지수함수·로그함수와 대등하게 실수 연산에 편입됩니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 10 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 10</span>
              <span class="timestamp">[00:13:30]</span>
              <span class="step-title">$y = \sin x$ vs $y = \sin x^\circ$ 의 결정적 차이</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/10_sinx_vs_sinx_deg_contrast.jpg" alt="sinx와 sinx도 차이 비교">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"많은 학생들이 $y = \sin x$와 $y = \sin x^\circ$를 혼동합니다. $y = \sin x^\circ$에 30을 넣으면 $\sin 30^\circ = \frac{1}{2}$이 나옵니다. 하지만 $y = \sin x$에 30을 넣으면 30 라디안($\approx 1718.8^\circ$)에 대한 사잇값이 나옵니다. $y = \sin x$에서 $\frac{1}{2}$이 나오려면 $x = \frac{\pi}{6}$이라는 실수값을 넣어야 합니다!"</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 수학교과서의 맹점 해소:</div>
                  <ul>
                    <li>"라디안 단위를 생략한다"는 설명 뒤에 감춰진 본질: $\sin x$의 $x$는 각도가 아니라 **순수한 실수**입니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 11 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 11</span>
              <span class="timestamp">[00:14:15]</span>
              <span class="step-title">호도법이 아니면 불가능한 자연스러운 미분 체계</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/11_calculus_natural_derivative.jpg" alt="호도법과 자연스러운 미분">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"왜 수학자들은 $y = \sin x^\circ$ 대신 $y = \sin x$를 쓸까요? 미분을 해보면 바로 알 수 있습니다. 호도법을 쓸 때만 $(\sin x)' = \cos x$라는 가장 자연스러운 도함수가 나옵니다. 만약 도($^\circ$)를 쓰면 $(\sin x^\circ)' = \frac{\pi}{180}\cos x^\circ$처럼 지저분한 상수 $\frac{\pi}{180}$가 꼬리표처럼 붙어버립니다!"</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 극한 계수의 불변성:</div>
                  <div class="math-highlight">$$\lim_{x \to 0}\frac{\sin x}{x} = 1 \iff \lim_{x \to 0}\frac{\sin x^\circ}{x} = \frac{\pi}{180}$$</div>
                  <ul>
                    <li>원점에서 접선의 기울기를 정확히 1로 만들어주는 유일무이한 각도 체계가 바로 호도법입니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 12 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 12</span>
              <span class="timestamp">[00:15:20]</span>
              <span class="step-title">수학적 일반화(Generalization)의 본질</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v7/12_mathematical_generalization.jpg" alt="수학적 일반화의 본질">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"삼각비에서 출발하여 단위원 위의 좌표로, 그리고 실수 전체를 정의역으로 하는 함수로 확장되는 이 과정은 수학 내에서 정의가 끊임없이 발전하고 일반화된다는 것을 보여줍니다. 일상 언어의 한계를 벗어나 새로운 개념을 창조해나가는 것이 바로 수학의 본질입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 수학의 본질적 통찰:</div>
                  <ul>
                    <li>음수 지수($2^{-3}$), 분수 나눗셈의 정의처럼 기존의 한계를 깨부수고 더 넓은 체계로 흡수해나가는 일반화의 여정입니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- TAB 3: MATH DEEP DIVE & CALCULUS PROOFS -->
      <div id="l7ProofTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; color: var(--accent-purple); margin-bottom: 20px;">
            📚 수학교과서식 엄밀한 증명 & 수능 기출 킬러 연계
          </h2>

          <!-- Proof 1 -->
          <div class="control-card" style="margin-bottom: 20px;">
            <h3 style="color: var(--accent-blue); margin-bottom: 12px;">
              [증명 1] 원점 극한 $\lim_{x \to 0} \frac{\sin x}{x} = 1$ 의 샌드위치 정리 증명
            </h3>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); line-height: 1.8; color: var(--text-main);">
              <strong>증명:</strong><br>
              1. 단위원 $x^2 + y^2 = 1$에서 중심각이 $x$ ($0 < x < \frac{\pi}{2}$)인 부채꼴 $OAP$와 접선에 의해 생기는 직각삼각형 $OAT$ ($T(1, \tan x)$)를 고려한다.<br>
              2. 세 도형의 면적 대소 관계:<br>
              &nbsp;&nbsp; $\triangle OAP \text{ 의 넓이} = \frac{1}{2}\cdot 1 \cdot 1 \cdot \sin x = \frac{1}{2}\sin x$<br>
              &nbsp;&nbsp; $\text{부채꼴 } OAP \text{ 의 넓이} = \frac{1}{2}\cdot 1^2 \cdot x = \frac{1}{2}x$<br>
              &nbsp;&nbsp; $\triangle OAT \text{ 의 넓이} = \frac{1}{2}\cdot 1 \cdot \tan x = \frac{1}{2}\tan x$<br>
              3. 따라서 $\frac{1}{2}\sin x < \frac{1}{2}x < \frac{1}{2}\tan x$ 가 성립한다.<br>
              4. $0 < x < \frac{\pi}{2}$에서 $\sin x > 0$이므로 $\frac{1}{2}\sin x$로 각 변을 나누면:<br>
              &nbsp;&nbsp; $1 < \frac{x}{\sin x} < \frac{1}{\cos x} \iff \cos x < \frac{\sin x}{x} < 1$<br>
              5. $x \to 0^+$일 때 $\lim_{x \to 0^+}\cos x = 1$이므로 조임정리(Squeeze Theorem)에 의해:<br>
              &nbsp;&nbsp; $\lim_{x \to 0^+}\frac{\sin x}{x} = 1$<br>
              6. 음수 방향 $x \to 0^-$ 역시 $x = -t$ 치환을 통해 $\lim_{t \to 0^+}\frac{\sin(-t)}{-t} = \lim_{t \to 0^+}\frac{\sin t}{t} = 1$로 일치한다.<br>
              $\therefore \mathbf{\lim_{x \to 0}\frac{\sin x}{x} = 1 \quad \blacksquare}$
            </div>
          </div>

          <!-- Proof 2 -->
          <div class="control-card" style="margin-bottom: 20px;">
            <h3 style="color: var(--accent-green); margin-bottom: 12px;">
              [증명 2] 도함수 정의에 의한 $(\sin x)' = \cos x$ 엄밀 유도
            </h3>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); line-height: 1.8; color: var(--text-main);">
              <strong>증명:</strong><br>
              미분의 정의에 따라:<br>
              $$(\sin x)' = \lim_{h \to 0}\frac{\sin(x+h) - \sin x}{h}$$
              삼각함수의 덧셈정리에 의해 $\sin(x+h) = \sin x\cos h + \cos x\sin h$ 이므로:<br>
              $$= \lim_{h \to 0}\left[ \cos x \cdot \frac{\sin h}{h} + \sin x \cdot \frac{\cos h - 1}{h} \right]$$
              여기서 $\lim_{h \to 0}\frac{\sin h}{h} = 1$이고,<br>
              $\lim_{h \to 0}\frac{\cos h - 1}{h} = \lim_{h \to 0}\frac{-\sin^2 h}{h(\cos h + 1)} = \lim_{h \to 0}\left(-\frac{\sin h}{h}\cdot \frac{\sin h}{\cos h + 1}\right) = -1 \cdot \frac{0}{2} = 0$ 이다.<br>
              $\therefore (\sin x)' = \cos x \cdot 1 + \sin x \cdot 0 = \mathbf{\cos x \quad \blacksquare}$
            </div>
          </div>

          <!-- CSAT Application -->
          <div class="control-card">
            <h3 style="color: var(--accent-gold); margin-bottom: 12px;">
              🎯 수능 수학I 삼각함수 그래프 킬러 문항 공략 3대 원칙
            </h3>
            <ul style="color: var(--text-muted); line-height: 2.0; padding-left: 20px;">
              <li><strong>1. 대칭성과 주기성의 활용:</strong> 삼각방정식 $\sin x = k$의 해를 직접 구하지 말고, 대칭축 $x = \frac{\pi}{2}$에 대해 두 실근의 합 $\alpha + \beta = \pi$임을 활용하라!</li>
              <li><strong>2. 단위원 동경 모델링:</strong> $\sin\theta, \cos\theta$가 복잡한 부등식으로 엮일 때는 수식 전개보다 단위원 $x^2 + y^2 = 1$ 위의 동경 영역으로 시각화하면 10초 만에 영역이 분할된다.</li>
              <li><strong>3. 호도법 비례 감각:</strong> 부채꼴 호의 길이 $l = r\theta$, 넓이 $S = \frac{1}{2}r^2\theta = \frac{1}{2}rl$에서 각도 $\theta$를 항상 무차원 실수로 취급하여 미적분 변수 변환과 일치시킨다.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 4: MANIM PYTHON SCRIPT -->
      <div id="l7ManimTab" class="tab-panel">
        <div class="glass-card">
          <div class="control-header" style="margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.35rem; color: #fff;">🎬 3Blue1Brown 스타일 Manim 스크립트</h2>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">매쓰의 본질: 직각삼각형 $\to$ 단위원 $\to$ 호도법 언롤링 $\to$ 사인 곡선 생성 시각화 코드</p>
            </div>
            <button class="preset-btn" onclick="copyL7ManimCode()" style="background: rgba(192, 132, 252, 0.2); color: var(--accent-purple); border-color: var(--accent-purple);">
              📋 코드 복사하기
            </button>
          </div>

          <div style="background: rgba(0, 0, 0, 0.4); padding: 12px 18px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); font-size: 0.82rem; color: var(--text-dim); margin-bottom: 16px;">
            💻 <strong>실행 명령어:</strong> <code style="color: var(--accent-gold);">manim -pql trig_functions_essence_manim.py TrigFunctionsEssenceScene</code>
          </div>

          <div class="code-container" style="background: #050811; border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 20px; overflow-x: auto; max-height: 600px;">
            <pre><code id="l7ManimCodeBlock" class="language-python" style="font-family: 'JetBrains Mono', monospace; font-size: 0.84rem; color: #e2e8f0; line-height: 1.6;">''' + manim_code_escaped + r'''</code></pre>
          </div>
        </div>
      </div>

    </div>
'''

    # Insert lecture7_html right before `<div id="lecture6View"`
    target_insert_point = '<div id="lecture6View"'
    if target_insert_point not in content:
        print("ERROR: target_insert_point not found!")
        return

    content = content.replace(target_insert_point, lecture7_html + '\n    ' + target_insert_point, 1)

    # 5. Update JavaScript logic:
    # Update setLecture(num) to support 7 lectures
    old_set_lecture = '''    function setLecture(num) {
      for (let i = 1; i <= 6; i++) {
        const btn = document.getElementById(`btnLec${i}`);
        const view = document.getElementById(`lecture${i}View`);
        if (btn) btn.classList.toggle('active', i === num);
        if (view) view.style.display = (i === num) ? 'block' : 'none';
      }

      if (num === 6) setTimeout(renderL6, 50);
      else if (num === 5) setTimeout(renderL5, 50);
      else if (num === 4) setTimeout(renderL4, 50);
      else if (num === 3) setTimeout(renderL3, 50);
      else if (num === 2) setTimeout(renderL2, 50);
      else if (num === 1) setTimeout(renderL1, 50);'''

    new_set_lecture = '''    function setLecture(num) {
      for (let i = 1; i <= 7; i++) {
        const btn = document.getElementById(`btnLec${i}`);
        const view = document.getElementById(`lecture${i}View`);
        if (btn) btn.classList.toggle('active', i === num);
        if (view) view.style.display = (i === num) ? 'block' : 'none';
      }

      if (num === 7) setTimeout(renderL7, 50);
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

    # Add switchLec7Tab and Lecture 7 logic right before `/* ========================================================= */\n    /* LECTURE 6`
    l7_js_logic = r'''    /* ========================================================= */
    /* LECTURE 7 (ESSENCE OF TRIG FUNCTIONS) LOGIC               */
    /* ========================================================= */
    function switchLec7Tab(tabId) {
      document.querySelectorAll('#lecture7View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture7View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l7SimTab') setTimeout(renderL7, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function copyL7ManimCode() {
      const code = document.getElementById('l7ManimCodeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('3Blue1Brown Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }

    const l7State = {
      mode: 'circle', // 'circle', 'radian', 'compare', 'signs'
      deg: 30,        // angle in degrees (0 to 360)
      r: 1.0,         // radius
      animating: false,
      timer: null
    };

    function setL7Mode(m) {
      l7State.mode = m;
      document.querySelectorAll('#lecture7View .preset-btn').forEach(b => b.classList.remove('active'));
      if (m === 'circle') document.getElementById('l7BtnCircle').classList.add('active');
      else if (m === 'radian') document.getElementById('l7BtnRadian').classList.add('active');
      else if (m === 'compare') document.getElementById('l7BtnCompare').classList.add('active');
      else if (m === 'signs') document.getElementById('l7BtnSigns').classList.add('active');

      syncL7UI();
      renderL7();
    }

    function setL7Angle(deg) {
      l7State.deg = deg;
      const slider = document.getElementById('l7AngleSlider');
      if (slider) slider.value = deg;
      syncL7UI();
      renderL7();
    }

    function toggleL7Anim() {
      l7State.animating = !l7State.animating;
      const btn = document.getElementById('l7AnimBtn');
      if (l7State.animating) {
        if (btn) btn.innerText = '⏸ 일시 정지';
        l7State.timer = setInterval(() => {
          l7State.deg = (l7State.deg + 1) % 360;
          const slider = document.getElementById('l7AngleSlider');
          if (slider) slider.value = l7State.deg;
          syncL7UI();
          renderL7();
        }, 30);
      } else {
        if (btn) btn.innerText = '▶ 회전 재생';
        clearInterval(l7State.timer);
      }
    }

    function syncL7UI() {
      const subCard = document.getElementById('l7SubControlCard');
      const metricCard = document.getElementById('l7MetricCard');
      const bannerLabel = document.getElementById('l7BannerLabel');
      const bannerMath = document.getElementById('l7BannerMath');
      const themeBadge = document.getElementById('l7ActiveThemeBadge');
      const caption = document.getElementById('l7CanvasCaption');

      const deg = l7State.deg;
      const rad = deg * Math.PI / 180;
      const cosVal = Math.cos(rad);
      const sinVal = Math.sin(rad);
      const tanVal = Math.abs(cosVal) < 1e-4 ? '∞' : Math.tan(rad).toFixed(3);

      let quadName = '제1사분면 (All +)';
      let quadClass = 'm3';
      if (deg > 90 && deg < 180) { quadName = '제2사분면 (Sin +)'; quadClass = 'm2'; }
      else if (deg > 180 && deg < 270) { quadName = '제3사분면 (Tan +)'; quadClass = 'm1'; }
      else if (deg > 270 && deg < 360) { quadName = '제4사분면 (Cos +)'; quadClass = 'm2'; }

      if (l7State.mode === 'circle') {
        themeBadge.innerText = '1. 단위원 & 사인파';
        bannerLabel.innerText = '🌟 단위원 위 점 P(cosθ, sinθ)와 실시간 사인파';
        bannerMath.innerHTML = `$$P(x, y) = (\\cos(${deg}^\\circ), \\;\\sin(${deg}^\\circ)) = (${cosVal.toFixed(3)}, \\;${sinVal.toFixed(3)}) \\quad\\Big|\\quad \\cos^2\\theta + \\sin^2\\theta = 1.000$$`;
        caption.innerText = '단위원 동경 회전에 따른 x=cosθ (청록), y=sinθ (골드) 및 우측 실수 좌표계 사인파 실시간 추적';

        subCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">🎛️ 회전각 $\\theta$ 조절 및 특수각 프리셋</span>
            <button class="preset-btn" id="l7AnimBtn" onclick="toggleL7Anim()" style="padding: 4px 10px; font-size: 0.78rem;">
              ${l7State.animating ? '⏸ 일시 정지' : '▶ 회전 재생'}
            </button>
          </div>
          <div class="slider-row">
            <label>동경 각도 $\\theta$: <strong id="l7DegLabel" style="color: var(--accent-purple);">${deg}° (${(rad/Math.PI).toFixed(2)}π)</strong></label>
            <input type="range" id="l7AngleSlider" min="0" max="360" step="1" value="${deg}" oninput="l7State.deg=parseInt(this.value); syncL7UI(); renderL7();">
          </div>
          <div class="preset-grid" style="grid-template-columns: repeat(4, 1fr); margin-top: 10px;">
            <button class="preset-btn ${deg===30?'active':''}" onclick="setL7Angle(30)">$30^\\circ (\\pi/6)$</button>
            <button class="preset-btn ${deg===45?'active':''}" onclick="setL7Angle(45)">$45^\\circ (\\pi/4)$</button>
            <button class="preset-btn ${deg===60?'active':''}" onclick="setL7Angle(60)">$60^\\circ (\\pi/3)$</button>
            <button class="preset-btn ${deg===90?'active':''}" onclick="setL7Angle(90)">$90^\\circ (\\pi/2)$</button>
            <button class="preset-btn ${deg===120?'active':''}" onclick="setL7Angle(120)">$120^\\circ (2\\pi/3)$</button>
            <button class="preset-btn ${deg===180?'active':''}" onclick="setL7Angle(180)">$180^\\circ (\\pi)$</button>
            <button class="preset-btn ${deg===240?'active':''}" onclick="setL7Angle(240)">$240^\\circ (4\\pi/3)$</button>
            <button class="preset-btn ${deg===315?'active':''}" onclick="setL7Angle(315)">$315^\\circ (7\\pi/4)$</button>
          </div>
        `;

        metricCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">📊 실시간 삼각함수 값 & 사분면 분석</span>
            <span class="badge-pill-sm" style="background: var(--accent-purple); color: #fff;">${quadName}</span>
          </div>
          <div class="metric-grid" style="grid-template-columns: repeat(3, 1fr);">
            <div class="metric-card m2">
              <div class="metric-label">밑변 $\\cos\\theta$ ($x$-좌표)</div>
              <div class="metric-val" style="color: var(--accent-blue);">${cosVal.toFixed(3)}</div>
            </div>
            <div class="metric-card m1">
              <div class="metric-label">높이 $\\sin\\theta$ ($y$-좌표)</div>
              <div class="metric-val" style="color: var(--accent-gold);">${sinVal.toFixed(3)}</div>
            </div>
            <div class="metric-card" style="border-top: 3px solid var(--accent-purple);">
              <div class="metric-label">기울기 $\\tan\\theta$ ($y/x$)</div>
              <div class="metric-val" style="color: var(--accent-purple);">${tanVal}</div>
            </div>
          </div>
          <div style="background: rgba(192, 132, 252, 0.08); padding: 10px; border-radius: var(--radius-sm); border: 1px solid rgba(192, 132, 252, 0.25); margin-top: 10px; text-align: center; font-size: 0.86rem;">
            피타고라스 항등식: $\\cos^2\\theta + \\sin^2\\theta = ${cosVal.toFixed(3)}^2 + ${sinVal.toFixed(3)}^2 = \\mathbf{1.000}$
          </div>
        `;
      } else if (l7State.mode === 'radian') {
        themeBadge.innerText = '2. 호도법 언롤링';
        bannerLabel.innerText = '🌟 호도법(Radian)의 정의: 원호 길이를 실수선에 펼치다';
        bannerMath.innerHTML = '$$\\mathbf{\\theta = \\frac{l}{r} \\quad (\\text{호의 길이} = l, \\text{반지름} = r) \\quad\\Big|\\quad r = 1 \\implies l = \\theta \\text{ (호의 길이가 곧 각도!)}}$$';
        caption.innerText = '반지름 r=1인 원에서 호의 길이 l을 똑바로 펼쳐 실수 수직선과 일대일 대응시키는 시각화';

        subCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">🎛️ 호의 길이 및 각도 조절</span>
          </div>
          <div class="slider-row">
            <label>중심각 $\\theta$: <strong style="color: var(--accent-purple);">${deg}° (${(rad/Math.PI).toFixed(2)}π rad)</strong></label>
            <input type="range" id="l7AngleSlider" min="10" max="360" step="5" value="${deg}" oninput="l7State.deg=parseInt(this.value); syncL7UI(); renderL7();">
          </div>
          <div style="background: rgba(255, 255, 255, 0.04); padding: 12px; border-radius: var(--radius-sm); font-size: 0.85rem; margin-top: 10px; line-height: 1.6;">
            💡 <strong>1 라디안(rad)의 크기:</strong> 호의 길이 $l$이 반지름 $r$과 같아지는 순간의 중심각!<br>
            $$1\\text{ rad} = \\frac{180^\\circ}{\\pi} \\approx \\mathbf{57.2958^\\circ}$$
          </div>
        `;

        metricCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">📊 각도 변환 대조표</span>
          </div>
          <div class="metric-grid" style="grid-template-columns: repeat(3, 1fr);">
            <div class="metric-card m1">
              <div class="metric-label">육십분법 (Degree)</div>
              <div class="metric-val">${deg}°</div>
            </div>
            <div class="metric-card m2">
              <div class="metric-label">호도법 (Radian)</div>
              <div class="metric-val">${rad.toFixed(3)} rad</div>
            </div>
            <div class="metric-card m3">
              <div class="metric-label">단위원 호의 길이 $l$</div>
              <div class="metric-val">${rad.toFixed(3)}</div>
            </div>
          </div>
        `;
      } else if (l7State.mode === 'compare') {
        themeBadge.innerText = '3. sin x vs sin x°';
        bannerLabel.innerText = '🌟 y = sin x (실수) vs y = sin x° (도)의 결정적 차이';
        bannerMath.innerHTML = '$$\\mathbf{(\\sin x)\' = \\cos x \\quad (\\text{호도법, 원점 접선 기울기 } 1) \\quad\\Big|\\quad (\\sin x^\\circ)\' = \\frac{\\pi}{180}\\cos x^\\circ}$$';
        caption.innerText = '호도법을 쓸 때만 원점에서 sin x / x = 1 (접선 기울기 1)이 되어 미적분이 아름답게 성립';

        subCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">💡 왜 수학자들은 라디안을 쓸까?</span>
          </div>
          <div style="background: rgba(139, 92, 246, 0.08); padding: 14px; border-radius: var(--radius-sm); border: 1px solid rgba(139, 92, 246, 0.3); font-size: 0.88rem; line-height: 1.8;">
            1. $y = \\sin x^\\circ$ : 주기가 360인 함수 ($x$축 단위: 도)<br>
            2. $y = \\sin x$ : 주기가 $2\\pi \\approx 6.28$인 함수 ($x$축 단위: 무차원 실수)<br>
            3. <strong>원점에서의 미분계수:</strong><br>
            $$\\lim_{x \\to 0}\\frac{\\sin x}{x} = \\mathbf{1} \\quad \\text{vs} \\quad \\lim_{x \\to 0}\\frac{\\sin x^\\circ}{x} = \\mathbf{\\frac{\\pi}{180} \\approx 0.0175}$$
            $\implies$ 호도법을 채택함으로써 미분 시 지저분한 상수 $\\frac{\\pi}{180}$가 전혀 붙지 않습니다!
          </div>
        `;

        metricCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">📊 입력값에 따른 출력값 대조</span>
          </div>
          <div class="metric-grid" style="grid-template-columns: 1fr 1fr;">
            <div class="metric-card m1">
              <div class="metric-label">$x = 30$ 입력 시</div>
              <div class="metric-val" style="font-size: 0.95rem;">
                $\\sin(30^\\circ) = 0.5$<br>
                $\\sin(30\\text{ rad}) = -0.988$
              </div>
            </div>
            <div class="metric-card m2">
              <div class="metric-label">$x = \\pi/6 \\approx 0.524$ 입력 시</div>
              <div class="metric-val" style="font-size: 0.95rem;">
                $\\sin(\\pi/6) = \\mathbf{0.5}$<br>
                $\\sin(0.524^\\circ) = 0.009$
              </div>
            </div>
          </div>
        `;
      } else if (l7State.mode === 'signs') {
        themeBadge.innerText = '4. 사분면 부호 (올사탄코)';
        bannerLabel.innerText = '🌟 사분면 부호의 본질: 동경 끝점의 좌표 (x, y) 부호';
        bannerMath.innerHTML = '$$\\text{All (+)} \\longrightarrow \\sin\\text{만 (+)} \\longrightarrow \\tan\\text{만 (+)} \\longrightarrow \\cos\\text{만 (+)}$$';
        caption.innerText = '단위원 위의 점 P(x, y)에서 x=cos, y=sin, y/x=tan 이므로 좌표의 부호가 곧 삼각함수의 부호';

        subCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">🎛️ 사분면 선택 및 각도 이동</span>
          </div>
          <div class="preset-grid" style="grid-template-columns: repeat(4, 1fr); margin-bottom: 10px;">
            <button class="preset-btn ${deg===45?'active':''}" onclick="setL7Angle(45)">1사분면 (45°)</button>
            <button class="preset-btn ${deg===135?'active':''}" onclick="setL7Angle(135)">2사분면 (135°)</button>
            <button class="preset-btn ${deg===225?'active':''}" onclick="setL7Angle(225)">3사분면 (225°)</button>
            <button class="preset-btn ${deg===315?'active':''}" onclick="setL7Angle(315)">4사분면 (315°)</button>
          </div>
          <div class="slider-row">
            <label>각도 $\\theta$: <strong style="color: var(--accent-purple);">${deg}°</strong></label>
            <input type="range" id="l7AngleSlider" min="0" max="360" step="1" value="${deg}" oninput="l7State.deg=parseInt(this.value); syncL7UI(); renderL7();">
          </div>
        `;

        metricCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">📊 현재 사분면 부호 판정: ${quadName}</span>
          </div>
          <div class="metric-grid" style="grid-template-columns: repeat(3, 1fr);">
            <div class="metric-card ${cosVal>0?'m3':'m1'}">
              <div class="metric-label">$\\cos\\theta$ ($x$-부호)</div>
              <div class="metric-val">${cosVal>0?'+ 양수':'- 음수'} (${cosVal.toFixed(2)})</div>
            </div>
            <div class="metric-card ${sinVal>0?'m3':'m1'}">
              <div class="metric-label">$\\sin\\theta$ ($y$-부호)</div>
              <div class="metric-val">${sinVal>0?'+ 양수':'- 음수'} (${sinVal.toFixed(2)})</div>
            </div>
            <div class="metric-card ${(cosVal*sinVal)>0?'m3':'m1'}">
              <div class="metric-label">$\\tan\\theta$ ($y/x$-부호)</div>
              <div class="metric-val">${(cosVal*sinVal)>0?'+ 양수':'- 음수'}</div>
            </div>
          </div>
        `;
      }

      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function renderL7() {
      const canvas = document.getElementById('l7Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      if (l7State.mode === 'circle') {
        renderL7CircleAndWave(ctx, w, h);
      } else if (l7State.mode === 'radian') {
        renderL7RadianUnroll(ctx, w, h);
      } else if (l7State.mode === 'compare') {
        renderL7CompareWave(ctx, w, h);
      } else if (l7State.mode === 'signs') {
        renderL7SignsCircle(ctx, w, h);
      }
    }

    /* 1. Circle & Wave Mode Render */
    function renderL7CircleAndWave(ctx, w, h) {
      const rad = l7State.deg * Math.PI / 180;
      const cCenter = { x: 160, y: 260 };
      const R = 110;

      // Coordinate axes for circle
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)'; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(cCenter.x - R - 30, cCenter.y); ctx.lineTo(cCenter.x + R + 30, cCenter.y); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cCenter.x, cCenter.y - R - 30); ctx.lineTo(cCenter.x, cCenter.y + R + 30); ctx.stroke();

      // Unit circle
      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(cCenter.x, cCenter.y, R, 0, Math.PI*2); ctx.stroke();
      ctx.fillStyle = 'rgba(56, 189, 248, 0.03)'; ctx.fill();

      // Arm OP
      const pP = {
        x: cCenter.x + R * Math.cos(rad),
        y: cCenter.y - R * Math.sin(rad) // Canvas Y inverted
      };

      // Shaded right triangle (projection)
      ctx.fillStyle = 'rgba(192, 132, 252, 0.15)';
      ctx.beginPath(); ctx.moveTo(cCenter.x, cCenter.y); ctx.lineTo(pP.x, cCenter.y); ctx.lineTo(pP.x, pP.y); ctx.closePath(); ctx.fill();

      // Cosine projection (horizontal cyan)
      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(cCenter.x, cCenter.y); ctx.lineTo(pP.x, cCenter.y); ctx.stroke();

      // Sine projection (vertical gold)
      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(pP.x, cCenter.y); ctx.lineTo(pP.x, pP.y); ctx.stroke();

      // Hypotenuse arm (purple)
      ctx.strokeStyle = '#c084fc'; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(cCenter.x, cCenter.y); ctx.lineTo(pP.x, pP.y); ctx.stroke();

      // Arc for angle theta
      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(cCenter.x, cCenter.y, 30, 0, -rad, true); ctx.stroke();

      // Point P
      drawDot(ctx, pP, '#ef4444', `P(${Math.cos(rad).toFixed(2)}, ${Math.sin(rad).toFixed(2)})`);

      // ----------------- RIGHT SIDE: SINE WAVE -----------------
      const waveXStart = 330;
      const waveW = 200;
      const waveYCenter = 260;

      // Axes for Sine wave
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)'; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(waveXStart, waveYCenter); ctx.lineTo(waveXStart + waveW + 20, waveYCenter); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(waveXStart, waveYCenter - R - 20); ctx.lineTo(waveXStart, waveYCenter + R + 20); ctx.stroke();

      // Plot Sine wave
      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= waveW; i++) {
        const curTh = (i / waveW) * (Math.PI * 2);
        const wy = waveYCenter - R * Math.sin(curTh);
        if (i === 0) ctx.moveTo(waveXStart + i, wy); else ctx.lineTo(waveXStart + i, wy);
      }
      ctx.stroke();

      // Dot on Sine wave
      const waveDotX = waveXStart + (rad / (Math.PI * 2)) * waveW;
      const waveDotY = waveYCenter - R * Math.sin(rad);

      // Connecting dash line from circle to wave
      ctx.strokeStyle = 'rgba(251, 191, 36, 0.5)'; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(pP.x, pP.y); ctx.lineTo(waveDotX, waveDotY); ctx.stroke();
      ctx.setLineDash([]);

      drawDot(ctx, { x: waveDotX, y: waveDotY }, '#fbbf24', `(${rad.toFixed(2)}, ${Math.sin(rad).toFixed(2)})`);

      // Axis labels
      ctx.fillStyle = '#94a3b8'; ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('0', waveXStart - 5, waveYCenter + 14);
      ctx.fillText('π', waveXStart + waveW/2 - 4, waveYCenter + 14);
      ctx.fillText('2π', waveXStart + waveW - 6, waveYCenter + 14);
      ctx.fillText('x (rad)', waveXStart + waveW + 8, waveYCenter + 14);
      ctx.fillText('+1', waveXStart - 18, waveYCenter - R + 4);
      ctx.fillText('-1', waveXStart - 18, waveYCenter + R + 4);
    }

    /* 2. Radian Unrolling Mode Render */
    function renderL7RadianUnroll(ctx, w, h) {
      const deg = l7State.deg;
      const rad = deg * Math.PI / 180;
      const cCenter = { x: 180, y: 220 };
      const R = 110;

      // Circle
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(cCenter.x, cCenter.y, R, 0, Math.PI*2); ctx.stroke();

      // Arm 1 (시초선)
      ctx.strokeStyle = '#fff'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(cCenter.x, cCenter.y); ctx.lineTo(cCenter.x + R, cCenter.y); ctx.stroke();

      // Arm 2 (동경)
      const pP = { x: cCenter.x + R * Math.cos(-rad), y: cCenter.y + R * Math.sin(-rad) };
      ctx.strokeStyle = '#c084fc'; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(cCenter.x, cCenter.y); ctx.lineTo(pP.x, pP.y); ctx.stroke();

      // Highlight circular arc in gold
      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 5;
      ctx.beginPath(); ctx.arc(cCenter.x, cCenter.y, R, 0, -rad, true); ctx.stroke();

      // Linear ruler at bottom (Unrolled straight arc)
      const rulerY = 410;
      const rulerStartX = 70;
      const scale = R; // 1 rad = R pixels

      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(rulerStartX, rulerY); ctx.lineTo(rulerStartX + scale * 3.5, rulerY); ctx.stroke();

      // Ruler ticks
      ctx.fillStyle = '#94a3b8'; ctx.font = 'bold 11px Inter, sans-serif';
      for (let i = 0; i <= 3; i++) {
        const tx = rulerStartX + i * scale;
        ctx.beginPath(); ctx.moveTo(tx, rulerY - 6); ctx.lineTo(tx, rulerY + 6); ctx.stroke();
        ctx.fillText(`${i} rad`, tx - 12, rulerY + 20);
      }
      // pi tick
      const piX = rulerStartX + Math.PI * scale;
      ctx.strokeStyle = '#38bdf8';
      ctx.beginPath(); ctx.moveTo(piX, rulerY - 10); ctx.lineTo(piX, rulerY + 10); ctx.stroke();
      ctx.fillStyle = '#38bdf8'; ctx.fillText('π rad', piX - 14, rulerY - 14);

      // Unrolled arc line
      const unrolledLen = rad * scale;
      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 5;
      ctx.beginPath(); ctx.moveTo(rulerStartX, rulerY); ctx.lineTo(rulerStartX + unrolledLen, rulerY); ctx.stroke();

      drawDot(ctx, { x: rulerStartX + unrolledLen, y: rulerY }, '#fbbf24', `길이 = ${rad.toFixed(2)}`);

      // Caption text
      ctx.fillStyle = '#fff'; ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText(`원의 호의 길이 l = rθ = ${rad.toFixed(3)}  (r=1이므로 호의 길이가 곧 라디안 각도)`, 70, 365);
    }

    /* 3. Compare Wave Mode Render */
    function renderL7CompareWave(ctx, w, h) {
      const cx = 80, cy = 260;
      const plotW = 440, plotH = 140;

      // Coordinate axes
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)'; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + plotW, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy - plotH - 30); ctx.lineTo(cx, cy + plotH + 30); ctx.stroke();

      // Radian wave: y = sin x (period 2pi ~ 6.28)
      // Scale: 2pi = 180px
      const scaleX = 180 / (Math.PI * 2);
      const scaleY = plotH * 0.8;

      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let px = 0; px <= plotW; px++) {
        const xReal = px / scaleX;
        const yVal = Math.sin(xReal);
        const py = cy - yVal * scaleY;
        if (px === 0) ctx.moveTo(cx + px, py); else ctx.lineTo(cx + px, py);
      }
      ctx.stroke();

      // Tangent line at origin y = x (slope 1)
      ctx.strokeStyle = '#34d399'; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(cx - 30, cy + 30 * (scaleY/scaleX)); ctx.lineTo(cx + 100, cy - 100 * (scaleY/scaleX)); ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#34d399'; ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('원점 접선: y = x (기울기 1)', cx + 40, cy - 110);

      // Degree wave y = sin(x°) squashed
      ctx.strokeStyle = '#c084fc'; ctx.lineWidth = 2; ctx.setLineDash([2, 2]);
      ctx.beginPath();
      for (let px = 0; px <= plotW; px++) {
        const xDeg = px; // 1px = 1 degree
        const yVal = Math.sin(xDeg * Math.PI / 180);
        const py = cy - yVal * scaleY;
        if (px === 0) ctx.moveTo(cx + px, py); else ctx.lineTo(cx + px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#fbbf24'; ctx.fillText('y = sin x (호도법: 주기 2π)', cx + 220, cy - 80);
      ctx.fillStyle = '#c084fc'; ctx.fillText('y = sin x° (육십분법: 주기 360, 기울기 π/180)', cx + 220, cy + 50);
    }

    /* 4. Signs Mode Render */
    function renderL7SignsCircle(ctx, w, h) {
      const cCenter = { x: 280, y: 260 };
      const R = 140;

      // 4 Quadrants background tint
      ctx.fillStyle = 'rgba(56, 189, 248, 0.06)'; ctx.fillRect(cCenter.x, cCenter.y - R, R, R); // Quad 1
      ctx.fillStyle = 'rgba(251, 191, 36, 0.06)'; ctx.fillRect(cCenter.x - R, cCenter.y - R, R, R); // Quad 2
      ctx.fillStyle = 'rgba(239, 68, 68, 0.06)';  ctx.fillRect(cCenter.x - R, cCenter.y, R, R); // Quad 3
      ctx.fillStyle = 'rgba(52, 211, 153, 0.06)'; ctx.fillRect(cCenter.x, cCenter.y, R, R); // Quad 4

      // Circle
      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.arc(cCenter.x, cCenter.y, R, 0, Math.PI*2); ctx.stroke();

      // Axes
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)'; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(cCenter.x - R - 30, cCenter.y); ctx.lineTo(cCenter.x + R + 30, cCenter.y); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cCenter.x, cCenter.y - R - 30); ctx.lineTo(cCenter.x, cCenter.y + R + 30); ctx.stroke();

      // Large quadrant tags
      ctx.font = 'bold 18px Inter, sans-serif';
      ctx.fillStyle = 'var(--accent-blue)';   ctx.fillText('All (+)', cCenter.x + 40, cCenter.y - 60);
      ctx.fillStyle = 'var(--accent-gold)';   ctx.fillText('Sin (+)', cCenter.x - 100, cCenter.y - 60);
      ctx.fillStyle = 'var(--accent-rose)';   ctx.fillText('Tan (+)', cCenter.x - 100, cCenter.y + 70);
      ctx.fillStyle = 'var(--accent-green)';  ctx.fillText('Cos (+)', cCenter.x + 40, cCenter.y + 70);

      // Rotating arm
      const rad = l7State.deg * Math.PI / 180;
      const pP = { x: cCenter.x + R * Math.cos(-rad), y: cCenter.y + R * Math.sin(-rad) };

      ctx.strokeStyle = '#fff'; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(cCenter.x, cCenter.y); ctx.lineTo(pP.x, pP.y); ctx.stroke();

      drawDot(ctx, pP, '#ef4444', `P(${Math.cos(rad).toFixed(2)}, ${Math.sin(rad).toFixed(2)})`);
    }

'''

    l6_marker = '    /* ========================================================= */\n    /* LECTURE 6 (CSAT GEOMETRY DEALER) LOGIC                    */'
    if l6_marker not in content:
        print("ERROR: l6_marker not found!")
        return

    content = content.replace(l6_marker, l7_js_logic + '\n' + l6_marker, 1)

    # 6. Update window load handler to initialize Lecture 7
    old_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      syncL6UI();
      renderL6();
    });'''

    new_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      syncL7UI();
      renderL7();
    });'''

    if old_load in content:
        content = content.replace(old_load, new_load, 1)

    # Write output to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: index.html updated successfully with Lecture 7!")

if __name__ == '__main__':
    main()
