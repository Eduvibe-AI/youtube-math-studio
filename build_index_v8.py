# -*- coding: utf-8 -*-
"""
Script to inject Lecture 8 (Trig Function Graphs & 8-Box Method: Sao Math) into index.html
Preserving all existing Lectures 1, 2, 3, 4, 5, 6, 7 without alteration.
"""

import os

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the lecture switcher bar
    old_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (7 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec7" onclick="setLecture(7)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #8b5cf6, #3b82f6); color: #fff;">✨ 본질 특강</span>
          삼각비에서 삼각함수까지 (매쓰의 본질)
        </button>'''

    new_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (8 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec8" onclick="setLecture(8)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #10b981, #06b6d4); color: #fff;">📊 그래프 특강</span>
          삼각함수 그래프 8칸 박스법 (사오수학)
        </button>
        <button class="lecture-btn" id="btnLec7" onclick="setLecture(7)">
          삼각비에서 삼각함수까지 (매쓰의 본질)
        </button>'''

    if old_switcher_head not in content:
        print("ERROR: old_switcher_head not found in index.html!")
        return

    content = content.replace(old_switcher_head, new_switcher_head, 1)

    # Update captured_summary button from 1~7 to 1~8
    content = content.replace('📸 사진 1~7 핵심 전용 페이지', '📸 사진 1~8 핵심 전용 페이지', 1)

    # 2. Update lecture7View to start hidden:
    old_lec7_start = '<div id="lecture7View">'
    new_lec7_start = '<div id="lecture7View" style="display: none;">'
    if old_lec7_start not in content:
        print("ERROR: old_lec7_start not found!")
        return

    content = content.replace(old_lec7_start, new_lec7_start, 1)

    # 3. Read the Manim script to include in Tab 4
    with open('trig_graphs_box_method_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()
    manim_code_escaped = manim_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # 4. Lecture 8 Section HTML
    lecture8_html = r'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 8 (TRIG GRAPHS & 8-BOX METHOD: SAO MATH)     -->
    <!-- ============================================================== -->
    <div id="lecture8View">
      <header>
        <div class="badge-pill" style="border-color: rgba(16, 185, 129, 0.4); color: var(--accent-green); box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);">
          <span>📐 고등 수학 I · 삼각함수 그래프 완벽 정복 · 내신/수능 1등급 필수</span>
        </div>
        <h1 style="background: linear-gradient(135deg, #ffffff 30%, #34d399 70%, #38bdf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          삼각함수 그래프 & 8칸 박스 작도법 마스터
        </h1>
        <p class="subtitle">
          주기 4등분과 최대·최소 중심선의 완벽한 시각화! $y = a\sin(bx + c) + d$와 $y = a\cos(bx + c) + d$의 모든 파라미터 변환을 <strong>인터랙티브 8칸 박스 스튜디오</strong>로 단 10초 만에 완벽 정복합니다.
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>사오수학</strong></span>
          <span>•</span>
          <a href="https://youtu.be/OErYVKR10Tw" target="_blank" rel="noopener">
            <span>YouTube 본 영상 보기 (14분 17초)</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
        </div>
      </header>

      <!-- Tab Bar for Lecture 8 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec8Tab('l8SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 8칸 박스 스튜디오 (실시간 변환)
        </button>
        <button class="tab-btn" onclick="switchLec8Tab('l8CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 & 12단계 타임라인
        </button>
        <button class="tab-btn" onclick="switchLec8Tab('l8ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          수학교과서식 정형화 & 수능 기출 킬러 연계
        </button>
        <button class="tab-btn" onclick="switchLec8Tab('l8ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 8) -->
      <div id="l8SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Dynamic Banner -->
          <div class="formula-banner" id="l8Banner" style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(56, 189, 248, 0.08)); border-color: rgba(16, 185, 129, 0.35);">
            <div class="label" id="l8BannerLabel" style="color: var(--accent-green);">🌟 삼각함수 일반형 4대 핵심 불변 공식</div>
            <div class="math-main" id="l8BannerMath">
              $$y = a\sin(b(x - p)) + d \implies \mathbf{M = |a| + d, \quad m = -|a| + d, \quad T = \frac{2\pi}{|b|}, \quad \text{박스 1칸} = \frac{T}{4}}$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l8Canvas" width="560" height="520"></canvas>
              <div id="l8CanvasCaption" style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                주기 $T$를 4등분한 가로 4칸 $\times$ 진폭 $|a|$ 상하 2단으로 형성된 8칸 박스 격자 위의 삼각함수 작도
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Type & Presets -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎯 함수 형태 및 필수 예제 프리셋</span>
                  <div style="display: flex; gap: 6px;">
                    <button class="preset-btn active" id="l8TypeSin" onclick="setL8Type('sin')" style="padding: 4px 10px; font-size: 0.8rem;">Sine</button>
                    <button class="preset-btn" id="l8TypeCos" onclick="setL8Type('cos')" style="padding: 4px 10px; font-size: 0.8rem;">Cosine</button>
                  </div>
                </div>
                <div class="preset-grid" style="grid-template-columns: 1fr 1fr;">
                  <button class="preset-btn active" id="l8PreDefault" onclick="setL8Preset('default')">
                    <span>1. 기본형 $y = \sin x$</span>
                    <span class="p-sub">$T = 2\pi, M=1, m=-1$</span>
                  </button>
                  <button class="preset-btn" id="l8PreAmp3" onclick="setL8Preset('amp3')">
                    <span>2. 진폭 3배 $y = 3\sin x$</span>
                    <span class="p-sub">$M=3, m=-3$ (치역 $[-3, 3]$)</span>
                  </button>
                  <button class="preset-btn" id="l8PreShiftCos" onclick="setL8Preset('shiftCos')">
                    <span>3. $y = 2\cos(x - \pi/2)$</span>
                    <span class="p-sub">위상 평행이동 $\to$ 사인 일치</span>
                  </button>
                  <button class="preset-btn" id="l8PreCompress3x" onclick="setL8Preset('compress3x')">
                    <span>4. $y = 2\sin(3x) + 1$</span>
                    <span class="p-sub">주기 단축 $T=2\pi/3, M=3, m=-1$</span>
                  </button>
                </div>
              </div>

              <!-- Parameter Sliders -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎛️ 4대 파라미터 ($a, b, p, d$) 실시간 튜닝</span>
                </div>

                <div class="slider-row">
                  <label>진폭 $a$ (상하 확대): <strong id="l8aVal" style="color: var(--accent-green);">1.0</strong></label>
                  <input type="range" id="l8SliderA" min="-3" max="3" step="0.5" value="1" oninput="updateL8Sliders()">
                </div>

                <div class="slider-row">
                  <label>계수 $b$ (주기 압축): <strong id="l8bVal" style="color: var(--accent-blue);">1.0</strong></label>
                  <input type="range" id="l8SliderB" min="0.5" max="3" step="0.5" value="1" oninput="updateL8Sliders()">
                </div>

                <div class="slider-row">
                  <label>$x$축 평행이동 $p$: <strong id="l8pVal" style="color: var(--accent-purple);">0.00π</strong></label>
                  <input type="range" id="l8SliderP" min="-2" max="2" step="0.25" value="0" oninput="updateL8Sliders()">
                </div>

                <div class="slider-row">
                  <label>$y$축 평행이동 $d$ (중심선): <strong id="l8dVal" style="color: var(--accent-gold);">0.0</strong></label>
                  <input type="range" id="l8SliderD" min="-2" max="2" step="0.5" value="0" oninput="updateL8Sliders()">
                </div>
              </div>

              <!-- Live Numeric Analysis Card -->
              <div class="control-card" id="l8MetricCard">
                <div class="control-header">
                  <span class="control-title">📊 8칸 박스 기하 요소 실시간 계산</span>
                </div>
                <div class="metric-grid" style="grid-template-columns: repeat(4, 1fr);">
                  <div class="metric-card m3">
                    <div class="metric-label">최댓값 ($M$)</div>
                    <div class="metric-val" id="l8ValM">1.00</div>
                  </div>
                  <div class="metric-card m1">
                    <div class="metric-label">최솟값 ($m$)</div>
                    <div class="metric-val" id="l8ValMin">-1.00</div>
                  </div>
                  <div class="metric-card m2">
                    <div class="metric-label">주기 ($T$)</div>
                    <div class="metric-val" id="l8ValT">2.00π</div>
                  </div>
                  <div class="metric-card" style="border-top: 3px solid var(--accent-gold);">
                    <div class="metric-label">박스 1칸 ($T/4$)</div>
                    <div class="metric-val" id="l8ValStep">0.50π</div>
                  </div>
                </div>
                <div style="background: rgba(16, 185, 129, 0.08); padding: 10px; border-radius: var(--radius-sm); border: 1px solid rgba(16, 185, 129, 0.25); margin-top: 10px; text-align: center; font-size: 0.86rem;">
                  중심선: $y = d = \mathbf{0.00}$ &nbsp;|&nbsp; 진폭: $|a| = \frac{M - m}{2} = \mathbf{1.00}$ &nbsp;|&nbsp; 8칸 박스 격자점 완벽 일치!
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: TIMELINE & CAPTURES (12 STEPS) -->
      <div id="l8CaptureTab" class="tab-panel">
        <div class="timeline-container">

          <!-- Step 1 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 1</span>
              <span class="timestamp">[00:01:10]</span>
              <span class="step-title">사인 함수 그래프의 기본 작도와 4등분 박스법</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/01_sine_graph_4division.jpg" alt="사인 함수 그래프 기본 작도와 4등분">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"사인 그래프를 그릴 때는 $2\pi$를 먼저 찍고, 무조건 반의 반, 즉 4등분을 하고 시작하는 것입니다. $\frac{\pi}{2}, \pi, \frac{3\pi}{2}, 2\pi$를 찍어두고 맨 앞부분($0 \sim \frac{\pi}{2}$)만 잘 그려주면 나머지는 대칭으로 끝납니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 4등분 박스의 핵심:</div>
                  <ul>
                    <li>한 주기 $2\pi$를 4등분하면 각 사분면에 해당하는 핵심 5개 점이 격자선 위에 정확하게 배치됩니다.</li>
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
              <span class="timestamp">[00:01:45]</span>
              <span class="step-title">원점 접선 기울기 1과 극댓점의 기울기 0</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/02_sine_slope_and_peak.jpg" alt="원점 접선 기울기와 극댓점 기울기">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"원점에서는 접선의 기울기가 1이 되도록 비스듬하게 올라가게 그려주시고, $x = \frac{\pi}{2}$ 꼭대기에서는 기울기가 0이 되도록 완만하게 둥글려 주셔야 합니다. 그 다음은 선대칭, 점대칭, 선대칭으로 이어주면 한 주기가 완성됩니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 곡선의 곡률 디테일:</div>
                  <ul>
                    <li>직선처럼 그리지 않고 원점에서 기울기 1, 극대에서 기울기 0인 부드러운 위로 볼록 곡선을 그리는 것이 핵심입니다.</li>
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
              <span class="timestamp">[00:03:50]</span>
              <span class="step-title">코사인 함수 그래프의 작도: $(0, 1)$에서 하강 출발</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/03_cosine_graph_offset.jpg" alt="코사인 함수 그래프 작도">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"코사인 그래프는 사인 그래프를 옆으로 대칭 이동한 것입니다. $(0, 0)$에서 시작하는 게 아니라 $(0, 1)$ 꼭대기에서 출발하여 아래로 떨어지게 그려주시면 됩니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 코사인의 5대 포인트:</div>
                  <div class="math-highlight">$$(0, 1) \longrightarrow (\pi/2, 0) \longrightarrow (\pi, -1) \longrightarrow (3\pi/2, 0) \longrightarrow (2\pi, 1)$$</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 4 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 4</span>
              <span class="timestamp">[00:04:40]</span>
              <span class="step-title">코사인 함수의 대칭성과 치역 $[-1, 1]$</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/04_cosine_symmetry_range.jpg" alt="코사인 함수 대칭성과 치역">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"코사인의 $y$값도 역시 $-1$과 $+1$ 사이에 갇혀 있습니다. 그래서 최댓값은 $+1$, 최솟값은 $-1$이고, $y$축에 대하여 완벽하게 좌우 대칭(우함수)입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 대칭성 공식:</div>
                  <ul>
                    <li>$\cos(-x) = \cos x$ ($y$축 선대칭, 우함수)</li>
                    <li>$\sin(-x) = -\sin x$ (원점 점대칭, 기함수)</li>
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
              <span class="timestamp">[00:06:05]</span>
              <span class="step-title">계수 $a$의 역할: 진폭과 상하 확대 ($y$값 $a$배)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/05_amplitude_a_effect.jpg" alt="계수 a의 역할 진폭과 상하확대">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"함수 전체에 $a$가 곱해져 있으면 위아래로 $a$배 늘려주시면 됩니다. 단, $a$가 음수일 수도 있으므로 최댓값은 $|a|$, 최솟값은 $-|a|$가 됩니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 치역 결정 공식:</div>
                  <div class="math-highlight">$$y \in [-|a|, \; |a|], \quad \text{진폭 } = |a|$$</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 6 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 6</span>
              <span class="timestamp">[00:06:55]</span>
              <span class="step-title">계수 $b$의 역할: $x$축 압축과 주기 $T = \frac{2\pi}{|b|}$</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/06_period_b_compression.jpg" alt="계수 b의 역할 주기 압축">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"$x$ 앞에 $b$가 곱해져 있으면 그래프는 좌우로 $\frac{1}{|b|}$배 압축됩니다. 원래 한 바퀴 도는 데 $2\pi$가 걸렸는데, $b$배 빠르게 달리니까 주기는 $\frac{2\pi}{|b|}$로 줄어드는 것입니다!"</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 주기 공식:</div>
                  <div class="math-highlight">$$\mathbf{T = \frac{2\pi}{|b|}}$$</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 7 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 7</span>
              <span class="timestamp">[00:07:45]</span>
              <span class="step-title">일반형 $y = a\sin(bx + c) + d$의 8칸 박스 설계법</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/07_general_form_box_method.jpg" alt="일반형 8칸 박스 설계법">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"복잡한 삼각함수 식을 만나면 3가지만 먼저 뽑아내세요: 1번 최댓값과 최솟값, 2번 주기, 3번 평행이동! 이 세 가지로 박스를 만들면 어떤 문제든 풀립니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 8칸 박스 구성 요소:</div>
                  <ul>
                    <li>가로 4칸: $T/4$ 간격</li>
                    <li>세로 2단: 중심선 $y = d$ 기준 위아래 $|a|$</li>
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
              <span class="timestamp">[00:08:45]</span>
              <span class="step-title">예제 1: $y = 3\sin x$ 의 작도와 치역 $[-3, 3]$</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/08_example1_3sinx.jpg" alt="예제 1 y=3sinx 작도">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"$y = 3\sin x$는 $2\pi$를 4등분하고 위아래를 3과 $-3$으로 잡은 뒤, 0에서 3으로 볼록하게 올라갔다가 내려오면 끝입니다. 치역은 $[-3, 3]$이고 주기는 변함없이 $2\pi$입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 예제 분석:</div>
                  <ul>
                    <li>$a = 3, b = 1, d = 0 \implies M = 3, m = -3, T = 2\pi$.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 9 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 9</span>
              <span class="timestamp">[00:10:15]</span>
              <span class="step-title">예제 2: $y = 2\cos(x - \frac{\pi}{2})$ 의 평행이동 작도</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/09_example2_cosine_shift.jpg" alt="예제 2 코사인 평행이동 작도">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"평행이동이 섞여 있을 때는 기본형 $y = 2\cos x$를 먼저 박스에 그리고, 모든 점을 $x$축 방향으로 $\frac{\pi}{2}$만큼 오른쪽으로 툭 밀어주면 됩니다. 그러면 정확하게 사인 그래프와 일치하게 됩니다!"</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 각변환과의 일치:</div>
                  <div class="math-highlight">$$\cos(x - \pi/2) = \sin x \implies y = 2\sin x$$</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 10 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 10</span>
              <span class="timestamp">[00:12:40]</span>
              <span class="step-title">예제 3: $y = 2\sin(3x) + 1$ 의 주기 단축 ($T = \frac{2\pi}{3}$)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/10_example3_bx_compression.jpg" alt="예제 3 bx 주기 압축">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"$x$ 앞에 3이 곱해져 있으니 주기는 $\frac{2\pi}{3}$입니다. 4등분하면 한 칸의 길이가 $\frac{\pi}{6}$가 됩니다. 중심선 $y = 1$을 기준으로 위로 2칸($y=3$), 아래로 2칸($y=-1$)을 잡아 박스를 치면 10초 만에 그려집니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 예제 분석:</div>
                  <ul>
                    <li>최댓값: $M = 2 + 1 = 3$</li>
                    <li>최솟값: $m = -2 + 1 = -1$</li>
                    <li>주기: $T = \frac{2\pi}{3}$</li>
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
              <span class="timestamp">[00:13:40]</span>
              <span class="step-title">수능 스피드 해법: 식에서 $M, m, T$ 즉시 추출</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/11_rapid_period_formula.jpg" alt="수능 스피드 해법 주기 공식">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"수능 시험장에서는 언제나 그래프를 다 그리고 있을 시간이 없습니다. 식을 보자마자 $x$ 앞의 계수로 주기를 나누고, 앞뒤 숫자로 최대최소를 구해서 5초 만에 답을 내는 기계적 훈련이 되어 있어야 합니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 5초 컷 공식:</div>
                  <div class="math-highlight">$$T = \frac{2\pi}{|b|}, \quad M = |a| + d, \quad m = -|a| + d$$</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 12 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 12</span>
              <span class="timestamp">[00:14:10]</span>
              <span class="step-title">최종 요약: 8칸 박스법의 절대 규칙</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v8/12_summary_box_rule.jpg" alt="8칸 박스법 최종 요약">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"삼각함수 그래프는 8칸 박스법 하나로 모든 내신과 수능 문제가 종결됩니다. 주기를 4등분하고 최대최소 중심선을 그어 박스를 채우는 이 감각을 꼭 체화하시기 바랍니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 실전 마인드셋:</div>
                  <ul>
                    <li>축을 먼저 그리지 말고 박스를 먼저 그린 뒤 축을 나중에 기입하는 역발상 작도법이 오차를 제로로 만듭니다.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- TAB 3: MATH DEEP DIVE & CSAT PROOFS -->
      <div id="l8ProofTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; color: var(--accent-green); margin-bottom: 20px;">
            📚 수학교과서식 엄밀한 증명 & 수능 기출 킬러 연계
          </h2>

          <!-- Proof 1 -->
          <div class="control-card" style="margin-bottom: 20px;">
            <h3 style="color: var(--accent-blue); margin-bottom: 12px;">
              [증명] 삼각함수의 주기 공식 $T = \frac{2\pi}{|b|}$ 대수적 증명
            </h3>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); line-height: 1.8; color: var(--text-main);">
              <strong>증명:</strong><br>
              1. 함수 $f(x) = \sin(bx)$가 주기 $T > 0$를 갖는다는 것은 모든 실수 $x$에 대해 $\sin(b(x + T)) = \sin(bx)$가 성립함을 의미한다.<br>
              2. 전개하면 $\sin(bx + bT) = \sin(bx)$이다.<br>
              3. 사인함수의 기본 주기는 $2\pi$이므로, $bT$의 절댓값은 $2\pi$의 최소 양의 주기 $2\pi$와 같아야 한다:<br>
              &nbsp;&nbsp; $|b|T = 2\pi \iff \mathbf{T = \frac{2\pi}{|b|}}$<br>
              4. 코사인함수 $g(x) = \cos(bx)$ 역시 기본 주기가 $2\pi$이므로 동일하게 $T = \frac{2\pi}{|b|}$가 성립한다. $\blacksquare$
            </div>
          </div>

          <!-- CSAT Application -->
          <div class="control-card">
            <h3 style="color: var(--accent-gold); margin-bottom: 12px;">
              🎯 수능 삼각함수 그래프 빈출 킬러 3대 역추적 알고리즘
            </h3>
            <ul style="color: var(--text-muted); line-height: 2.0; padding-left: 20px;">
              <li><strong>1. 진폭 $|a|$ 및 중심선 $d$ 역추적:</strong> 그래프의 최고점 $M$과 최저점 $m$이 주어지면 즉시 $|a| = \frac{M - m}{2}$, $d = \frac{M + m}{2}$를 확정한다!</li>
              <li><strong>2. 주기 $b$ 역추적:</strong> 인접한 두 마루(최고점) 사이의 거리는 1주기 $T$, 마루와 골(최저점) 사이의 가로 거리는 반주기 $\frac{T}{2}$이다. 이를 통해 $T$를 구하고 $|b| = \frac{2\pi}{T}$를 즉시 구한다!</li>
              <li><strong>3. 대칭축 실근의 합 킬러:</strong> $\sin(bx) = k$의 해를 구할 때, 4등분 박스의 대칭축 선 $x = \alpha$를 기준으로 항상 두 실근의 합 $= 2\alpha$가 됨을 활용하여 5초 만에 계산을 끝낸다.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 4: MANIM PYTHON SCRIPT -->
      <div id="l8ManimTab" class="tab-panel">
        <div class="glass-card">
          <div class="control-header" style="margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.35rem; color: #fff;">🎬 3Blue1Brown 스타일 Manim 스크립트</h2>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">사오수학: 8칸 박스 격자 작도 및 파라미터(a, b, c, d) 동적 변환 시각화 코드</p>
            </div>
            <button class="preset-btn" onclick="copyL8ManimCode()" style="background: rgba(16, 185, 129, 0.2); color: var(--accent-green); border-color: var(--accent-green);">
              📋 코드 복사하기
            </button>
          </div>

          <div style="background: rgba(0, 0, 0, 0.4); padding: 12px 18px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); font-size: 0.82rem; color: var(--text-dim); margin-bottom: 16px;">
            💻 <strong>실행 명령어:</strong> <code style="color: var(--accent-gold);">manim -pql trig_graphs_box_method_manim.py TrigGraphsBoxMethodScene</code>
          </div>

          <div class="code-container" style="background: #050811; border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 20px; overflow-x: auto; max-height: 600px;">
            <pre><code id="l8ManimCodeBlock" class="language-python" style="font-family: 'JetBrains Mono', monospace; font-size: 0.84rem; color: #e2e8f0; line-height: 1.6;">''' + manim_code_escaped + r'''</code></pre>
          </div>
        </div>
      </div>

    </div>
'''

    # Insert lecture8_html right before `<div id="lecture7View"`
    target_insert_point = '<div id="lecture7View"'
    if target_insert_point not in content:
        print("ERROR: target_insert_point not found!")
        return

    content = content.replace(target_insert_point, lecture8_html + '\n    ' + target_insert_point, 1)

    # 5. Update JavaScript logic:
    # Update setLecture(num) to support 8 lectures
    old_set_lecture = '''    function setLecture(num) {
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

    new_set_lecture = '''    function setLecture(num) {
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

    if old_set_lecture not in content:
        print("ERROR: old_set_lecture not found!")
        return

    content = content.replace(old_set_lecture, new_set_lecture, 1)

    # Add switchLec8Tab and Lecture 8 logic right before `/* ========================================================= */\n    /* LECTURE 7`
    l8_js_logic = r'''    /* ========================================================= */
    /* LECTURE 8 (TRIG GRAPHS & 8-BOX METHOD) LOGIC              */
    /* ========================================================= */
    function switchLec8Tab(tabId) {
      document.querySelectorAll('#lecture8View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture8View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l8SimTab') setTimeout(renderL8, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function copyL8ManimCode() {
      const code = document.getElementById('l8ManimCodeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('3Blue1Brown Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }

    const l8State = {
      type: 'sin', // 'sin' or 'cos'
      a: 1.0,
      b: 1.0,
      p: 0.0, // x shift in multiples of pi
      d: 0.0  // y shift
    };

    function setL8Type(t) {
      l8State.type = t;
      document.getElementById('l8TypeSin').classList.toggle('active', t === 'sin');
      document.getElementById('l8TypeCos').classList.toggle('active', t === 'cos');
      renderL8();
    }

    function setL8Preset(pre) {
      document.querySelectorAll('#lecture8View .preset-grid .preset-btn').forEach(b => b.classList.remove('active'));
      if (pre === 'default') {
        document.getElementById('l8PreDefault').classList.add('active');
        l8State.type = 'sin'; l8State.a = 1.0; l8State.b = 1.0; l8State.p = 0.0; l8State.d = 0.0;
      } else if (pre === 'amp3') {
        document.getElementById('l8PreAmp3').classList.add('active');
        l8State.type = 'sin'; l8State.a = 3.0; l8State.b = 1.0; l8State.p = 0.0; l8State.d = 0.0;
      } else if (pre === 'shiftCos') {
        document.getElementById('l8PreShiftCos').classList.add('active');
        l8State.type = 'cos'; l8State.a = 2.0; l8State.b = 1.0; l8State.p = 0.5; l8State.d = 0.0;
      } else if (pre === 'compress3x') {
        document.getElementById('l8PreCompress3x').classList.add('active');
        l8State.type = 'sin'; l8State.a = 2.0; l8State.b = 3.0; l8State.p = 0.0; l8State.d = 1.0;
      }

      setL8Type(l8State.type);
      document.getElementById('l8SliderA').value = l8State.a;
      document.getElementById('l8SliderB').value = l8State.b;
      document.getElementById('l8SliderP').value = l8State.p;
      document.getElementById('l8SliderD').value = l8State.d;
      updateL8Sliders();
    }

    function updateL8Sliders() {
      l8State.a = parseFloat(document.getElementById('l8SliderA').value);
      l8State.b = parseFloat(document.getElementById('l8SliderB').value);
      l8State.p = parseFloat(document.getElementById('l8SliderP').value);
      l8State.d = parseFloat(document.getElementById('l8SliderD').value);

      document.getElementById('l8aVal').innerText = l8State.a.toFixed(1);
      document.getElementById('l8bVal').innerText = l8State.b.toFixed(1);
      document.getElementById('l8pVal').innerText = (l8State.p === 0 ? '0.00' : l8State.p.toFixed(2)) + 'π';
      document.getElementById('l8dVal').innerText = l8State.d.toFixed(1);

      const absA = Math.abs(l8State.a);
      const absB = Math.abs(l8State.b);
      const maxVal = absA + l8State.d;
      const minVal = -absA + l8State.d;
      const periodVal = 2.0 / absB;
      const stepVal = periodVal / 4.0;

      document.getElementById('l8ValM').innerText = maxVal.toFixed(2);
      document.getElementById('l8ValMin').innerText = minVal.toFixed(2);
      document.getElementById('l8ValT').innerText = periodVal.toFixed(2) + 'π';
      document.getElementById('l8ValStep').innerText = stepVal.toFixed(2) + 'π';

      renderL8();
    }

    function renderL8() {
      const canvas = document.getElementById('l8Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const a = l8State.a;
      const b = l8State.b;
      const p = l8State.p * Math.PI; // in radians
      const d = l8State.d;
      const type = l8State.type;

      const absA = Math.abs(a);
      const absB = Math.abs(b);
      const T = (2 * Math.PI) / absB; // period in radians
      const stepX = T / 4; // quarter period

      // Coordinate Transform
      // X range: [-0.5*PI, 3.5*PI], Y range: [-4.2, 4.2]
      const margin = 45;
      const plotW = w - margin * 2;
      const plotH = h - margin * 2;
      const xMin = -0.5 * Math.PI, xMax = 3.2 * Math.PI;
      const yMin = -4.2, yMax = 4.2;

      function toX(x) { return margin + ((x - xMin) / (xMax - xMin)) * plotW; }
      function toY(y) { return margin + plotH - ((y - yMin) / (yMax - yMin)) * plotH; }

      // 1. Draw Grid Axes
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)'; ctx.lineWidth = 1;
      // X axis (y = 0)
      ctx.beginPath(); ctx.moveTo(toX(xMin), toY(0)); ctx.lineTo(toX(xMax), toY(0)); ctx.stroke();
      // Y axis (x = 0)
      ctx.beginPath(); ctx.moveTo(toX(0), toY(yMin)); ctx.lineTo(toX(0), toY(yMax)); ctx.stroke();

      // Axis ticks
      ctx.fillStyle = '#64748b'; ctx.font = '11px Inter, sans-serif';
      for (let mul = 0; mul <= 3; mul++) {
        const valX = mul * Math.PI;
        ctx.fillText(mul === 0 ? '0' : (mul === 1 ? 'π' : `${mul}π`), toX(valX) - 5, toY(0) + 16);
      }
      ctx.fillText('+2', toX(0) - 20, toY(2) + 4);
      ctx.fillText('-2', toX(0) - 22, toY(-2) + 4);

      // 2. DRAW 8-BOX GRID
      // Box horizontal bounds: [p, p + T]
      // Box vertical bounds: [d - absA, d + absA]
      const boxLeft = toX(p);
      const boxRight = toX(p + T);
      const boxTop = toY(d + absA);
      const boxMid = toY(d);
      const boxBot = toY(d - absA);

      // Box background tint
      ctx.fillStyle = 'rgba(16, 185, 129, 0.06)';
      ctx.fillRect(boxLeft, boxTop, boxRight - boxLeft, boxBot - boxTop);

      // Box outer border
      ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2;
      ctx.strokeRect(boxLeft, boxTop, boxRight - boxLeft, boxBot - boxTop);

      // Horizontal lines (Upper M, Midline d, Lower m)
      ctx.strokeStyle = 'rgba(16, 185, 129, 0.4)'; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(toX(xMin), boxTop); ctx.lineTo(toX(xMax), boxTop); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(toX(xMin), boxBot); ctx.lineTo(toX(xMax), boxBot); ctx.stroke();
      ctx.setLineDash([]);

      // Midline (Teal solid)
      ctx.strokeStyle = '#06b6d4'; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(toX(xMin), boxMid); ctx.lineTo(toX(xMax), boxMid); ctx.stroke();

      // Vertical 4-division lines: 5 lines at p + k*stepX
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.35)'; ctx.setLineDash([3, 3]);
      for (let k = 0; k <= 4; k++) {
        const curX = toX(p + k * stepX);
        ctx.beginPath(); ctx.moveTo(curX, boxTop - 15); ctx.lineTo(curX, boxBot + 15); ctx.stroke();
      }
      ctx.setLineDash([]);

      // 3. DRAW FULL SINE / COSINE CURVE
      ctx.strokeStyle = type === 'sin' ? '#34d399' : '#38bdf8';
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      for (let px = 0; px <= plotW; px++) {
        const curRealX = xMin + (px / plotW) * (xMax - xMin);
        let curY;
        if (type === 'sin') {
          curY = a * Math.sin(b * (curRealX - p)) + d;
        } else {
          curY = a * Math.cos(b * (curRealX - p)) + d;
        }
        const py = toY(curY);
        if (px === 0) ctx.moveTo(margin + px, py); else ctx.lineTo(margin + px, py);
      }
      ctx.stroke();

      // 4. PLOT 5 KEY MILESTONE POINTS
      // Sine 5 points: (p, d), (p+T/4, d+a), (p+T/2, d), (p+3T/4, d-a), (p+T, d)
      // Cosine 5 points: (p, d+a), (p+T/4, d), (p+T/2, d-a), (p+3T/4, d), (p+T, d+a)
      let pts = [];
      if (type === 'sin') {
        pts = [
          { x: p, y: d, label: '중심' },
          { x: p + stepX, y: d + a, label: a >= 0 ? '최대' : '최소' },
          { x: p + 2*stepX, y: d, label: '중심' },
          { x: p + 3*stepX, y: d - a, label: a >= 0 ? '최소' : '최대' },
          { x: p + 4*stepX, y: d, label: '중심' }
        ];
      } else {
        pts = [
          { x: p, y: d + a, label: a >= 0 ? '최대' : '최소' },
          { x: p + stepX, y: d, label: '중심' },
          { x: p + 2*stepX, y: d - a, label: a >= 0 ? '최소' : '최대' },
          { x: p + 3*stepX, y: d, label: '중심' },
          { x: p + 4*stepX, y: d + a, label: a >= 0 ? '최대' : '최소' }
        ];
      }

      pts.forEach(pt => {
        const sx = toX(pt.x), sy = toY(pt.y);
        ctx.fillStyle = '#fbbf24';
        ctx.beginPath(); ctx.arc(sx, sy, 6, 0, Math.PI * 2); ctx.fill();
        ctx.strokeStyle = '#000'; ctx.lineWidth = 2; ctx.stroke();

        ctx.fillStyle = '#fff'; ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillText(pt.label, sx - 10, sy - 10);
      });

      // 5. Box Dimensions & Legend
      ctx.fillStyle = '#10b981'; ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(`M = ${(d + absA).toFixed(2)} (최대)`, boxRight + 8, boxTop + 4);
      ctx.fillStyle = '#06b6d4';
      ctx.fillText(`d = ${d.toFixed(2)} (중심선)`, boxRight + 8, boxMid + 4);
      ctx.fillStyle = '#ef4444';
      ctx.fillText(`m = ${(d - absA).toFixed(2)} (최소)`, boxRight + 8, boxBot + 4);

      // Period bracket
      ctx.fillStyle = '#fbbf24'; ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText(`주기 T = ${(T/Math.PI).toFixed(2)}π (4등분: 한 칸 = ${(stepX/Math.PI).toFixed(2)}π)`, boxLeft, boxTop - 24);
    }

'''

    l7_marker = '    /* ========================================================= */\n    /* LECTURE 7 (ESSENCE OF TRIG FUNCTIONS) LOGIC               */'
    if l7_marker not in content:
        print("ERROR: l7_marker not found!")
        return

    content = content.replace(l7_marker, l8_js_logic + '\n' + l7_marker, 1)

    # 6. Update window load handler to initialize Lecture 8
    old_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      syncL7UI();
      renderL7();
    });'''

    new_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      updateL8Sliders();
      renderL8();
    });'''

    if old_load in content:
        content = content.replace(old_load, new_load, 1)

    # Write output to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: index.html updated successfully with Lecture 8!")

if __name__ == '__main__':
    main()
