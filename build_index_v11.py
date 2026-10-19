# -*- coding: utf-8 -*-
"""
Script to inject Lecture 11 (Irrational Function & Inverse Intersection: Cha Gil-young) into index.html
Preserving all existing Lectures 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 without alteration.
"""

import os

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the lecture switcher bar
    old_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (10 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec10" onclick="setLecture(10)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #ec4899, #8b5cf6); color: #fff;">⚡ 3초 풀이법</span>
          유리함수 평행이동 3초 공식 (차길영)
        </button>
        <button class="lecture-btn" id="btnLec9" onclick="setLecture(9)">
          정적분과 넓이 & 차함수의 마법 (사오수학)
        </button>'''

    new_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (11 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec11" onclick="setLecture(11)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #06b6d4, #3b82f6); color: #fff;">⚡ 3초 풀이법</span>
          무리함수와 역함수 교점 3초 공식 (차길영)
        </button>
        <button class="lecture-btn" id="btnLec10" onclick="setLecture(10)">
          유리함수 평행이동 3초 공식 (차길영)
        </button>
        <button class="lecture-btn" id="btnLec9" onclick="setLecture(9)">
          정적분과 넓이 & 차함수의 마법 (사오수학)
        </button>'''

    if old_switcher_head not in content:
        print("ERROR: old_switcher_head not found in index.html!")
        return

    content = content.replace(old_switcher_head, new_switcher_head, 1)

    # Update captured_summary button from 1~10 to 1~11
    content = content.replace('📸 사진 1~10 핵심 전용 페이지', '📸 사진 1~11 핵심 전용 페이지', 1)

    # 2. Update lecture10View to start hidden:
    old_lec10_start = '<div id="lecture10View">'
    new_lec10_start = '<div id="lecture10View" style="display: none;">'
    if old_lec10_start not in content:
        print("ERROR: old_lec10_start not found!")
        return

    content = content.replace(old_lec10_start, new_lec10_start, 1)

    # 3. Read the Manim script to include in Tab 4
    with open('irrational_function_3sec_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()
    manim_code_escaped = manim_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # 4. Lecture 11 Section HTML
    lecture11_html = r'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 11 (IRRATIONAL FUNCTION & INVERSE: CHA GIL-YOUNG) -->
    <!-- ============================================================== -->
    <div id="lecture11View">
      <header>
        <div class="badge-pill" style="border-color: rgba(6, 182, 212, 0.4); color: #22d3ee; box-shadow: 0 0 20px rgba(6, 182, 212, 0.3);">
          <span>📐 고1 수학 (하) · 무리함수 2탄 · 내신 1등급 3초 킬러 공식</span>
        </div>
        <h1 style="background: linear-gradient(135deg, #ffffff 30%, #22d3ee 70%, #3b82f6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          무리함수와 역함수 교점 &amp; 시작점 $y=x$ 3초 풀이법
        </h1>
        <p class="subtitle">
          역함수와의 교점은 대칭축 $y = x$ 위에서만 존재합니다! 두 점에서 만나기 위한 $k$의 최댓값은 시작점 $(p, k)$가 $y = x$ 위에 안착하는 순간($k = p$)에 결정되는 <strong>인터랙티브 기하학 스튜디오</strong>입니다.
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>차길영의 세븐에듀</strong></span>
          <span>•</span>
          <a href="https://youtube.com/shorts/R2khenQ29ug" target="_blank" rel="noopener noreferrer" style="color: var(--accent-blue); text-decoration: none; display: inline-flex; align-items: center; gap: 4px;">
            <span>고1 '3초 풀이법' 무리함수 2탄 (1:00)</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
          <span>•</span>
          <span>강의 고화질 10단계 캡처 &amp; Manim 코드 탑재</span>
        </div>
      </header>

      <!-- Tab Bar for Lecture 11 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec11Tab('l11SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 3초 판정기 &amp; 무리함수 기하학 스튜디오
        </button>
        <button class="tab-btn" onclick="switchLec11Tab('l11CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 &amp; 10단계 타임라인
        </button>
        <button class="tab-btn" onclick="switchLec11Tab('l11ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          수학교과서식 정형화 &amp; 무리함수 5대 치트키
        </button>
        <button class="tab-btn" onclick="switchLec11Tab('l11ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 11) -->
      <div id="l11SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Dynamic Banner -->
          <div class="formula-banner" id="l11Banner" style="background: linear-gradient(135deg, rgba(6, 182, 212, 0.12), rgba(59, 130, 246, 0.08)); border-color: rgba(6, 182, 212, 0.35);">
            <div class="label" id="l11BannerLabel" style="color: #22d3ee;">🌟 무리함수와 역함수 교점 3초 불변 정리 (The Starting Point Theorem)</div>
            <div class="math-main" id="l11BannerMath">
              $$f(x) = \sqrt{x - p} + k \implies f(x) \cap f^{-1}(x) \iff f(x) \cap (y = x) \implies \mathbf{k_{\max} = p \quad (\text{시작점이 } y = x \text{ 위})}$$$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l11Canvas" width="560" height="520"></canvas>
              <div id="l11CanvasCaption" style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                무리함수 $f(x)$ (청록색) | 역함수 $f^{-1}(x)$ (핑크 점선) | 대칭축 $y = x$ (황금색 점선) | 시작점 $(p, k)$ (동적 구슬)
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Presets -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎯 4대 대표 기하학 상태 프리셋</span>
                </div>
                <div class="preset-grid" style="grid-template-columns: 1fr 1fr;">
                  <button class="preset-btn active" id="l11PreMax" onclick="setL11Preset('max')">
                    <span>1. 최댓값 $k = 3.0$ 🎯</span>
                    <span class="p-sub" style="color: #34d399; font-weight: bold;">두 점 $(3,3), (4,4)$ 정답!</span>
                  </button>
                  <button class="preset-btn" id="l11PreTan" onclick="setL11Preset('tan')">
                    <span>2. 접선 하한 $k = 2.75$</span>
                    <span class="p-sub">$D = 0$ (접점 1개)</span>
                  </button>
                  <button class="preset-btn" id="l11PreHigh" onclick="setL11Preset('high')">
                    <span>3. 너무 높은 $k = 3.6$</span>
                    <span class="p-sub" style="color: #ef4444;">교점 1개 (실패 ❌)</span>
                  </button>
                  <button class="preset-btn" id="l11PreLow" onclick="setL11Preset('low')">
                    <span>4. 너무 낮은 $k = 2.2$</span>
                    <span class="p-sub" style="color: #ef4444;">교점 0개 (안 만남 ❌)</span>
                  </button>
                </div>
              </div>

              <!-- Parameter Sliders -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎛️ $f(x) = \sqrt{x - p} + k$ 실시간 튜닝</span>
                </div>

                <div class="slider-row">
                  <label>상하 평행이동 $k$: <strong id="l11kVal" style="color: #22d3ee;">3.00</strong></label>
                  <input type="range" id="l11SliderK" min="2.0" max="4.2" step="0.05" value="3.0" oninput="updateL11Sliders()">
                </div>

                <div class="slider-row">
                  <label>시작점 $x$좌표 $p$: <strong id="l11pVal" style="color: var(--accent-gold);">3.0</strong></label>
                  <input type="range" id="l11SliderP" min="1.0" max="5.0" step="0.5" value="3.0" oninput="updateL11Sliders()">
                </div>
              </div>

              <!-- Live Status Card -->
              <div class="control-card" style="background: rgba(6, 182, 212, 0.05); border-color: rgba(6, 182, 212, 0.25);">
                <div class="control-header">
                  <span class="control-title" style="color: #22d3ee;">📊 실시간 교점 개수 &amp; 기하학적 판정</span>
                </div>

                <div class="metric-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 12px;">
                  <div class="metric-card m1">
                    <div class="metric-label">시작점 $(p, k)$</div>
                    <div class="metric-val" id="l11ValStart" style="color: var(--accent-gold); font-size: 1.25rem;">(3.0, 3.0)</div>
                    <div class="metric-sub">$y = x$ 접촉 상태</div>
                  </div>
                  <div class="metric-card m2">
                    <div class="metric-label">교점 개수 (정답 조건)</div>
                    <div class="metric-val" id="l11ValCount" style="color: #34d399; font-size: 1.25rem;">★ 서로 다른 2개</div>
                    <div class="metric-sub" id="l11ValCountSub">조건 완벽 충족</div>
                  </div>
                </div>

                <div class="metric-grid" style="grid-template-columns: 1fr 1fr;">
                  <div class="metric-card m3">
                    <div class="metric-label">$k$의 최댓값 ($k_{\max}$)</div>
                    <div class="metric-val" id="l11ValMax" style="color: #22d3ee; font-size: 1.3rem;">3.00</div>
                    <div class="metric-sub">$k = p$ (3초 암산 공식)</div>
                  </div>
                  <div class="metric-card">
                    <div class="metric-label">두 점 유효 범위</div>
                    <div class="metric-val" id="l11ValRange" style="color: #c084fc; font-size: 0.95rem;">[2.75, 3.00]</div>
                    <div class="metric-sub">접할 때 $\le k \le$ 시작점</div>
                  </div>
                </div>

                <div id="l11LiveFormula" style="margin-top: 14px; padding: 10px; background: rgba(0,0,0,0.3); border-radius: 8px; font-size: 0.88rem; color: #cbd5e1; text-align: center;">
                  함수: $f(x) = \sqrt{x - 3} + 3$ $\implies$ $y = x$와 교점: $(3, 3), (4, 4)$
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: TIMELINE CAPTURES (LECTURE 11) -->
      <div id="l11CaptureTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; margin-bottom: 8px; color: var(--accent-gold);">
            📸 차길영 선생님 강의 10단계 판서 타임라인 &amp; 교재 해설
          </h2>
          <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 24px;">
            유튜브 쇼츠(1:00) 원본 영상의 3초 풀이법 전 과정을 1080p 고화질 캡처와 함께 완벽히 분석했습니다.
          </p>

          <div class="timeline-container">
            <!-- Card 1 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">1단계 [00:00:03]</span>
                <span class="timeline-title">시험 출제 문제 세팅 &amp; 역함수 $y=x$ 연상</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/01_intro_problem_statement.jpg" alt="01_intro_problem_statement">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "우리는 $f^{-1}(x)$ 그러면 $y = x$ 대칭이 생각나잖아? 근데 $y = x$는 뭔가 $x$랑 $y$랑 같다! 이거를 잘 연상을 해 보란 말이야!"
              </div>
              <div class="timeline-desc">
                <strong>문제 분석:</strong> 무리함수 $f(x) = \sqrt{x - 3} + k$와 그 역함수가 서로 다른 두 점에서 만날 때, 상수 $k$의 최댓값을 구하는 고1 2학기 기말고사 단골 킬러 문제입니다.
              </div>
            </div>

            <!-- Card 2 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">2단계 [00:00:06]</span>
                <span class="timeline-title">$y = x$의 본질: $x$좌표와 $y$좌표의 일치</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/02_y_equals_x_symmetry.jpg" alt="02_y_equals_x_symmetry">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "$y = x$ 대칭이라는 건 $x$와 $y$가 같다는 거야. 이걸 잘 기억해!"
              </div>
              <div class="timeline-desc">
                <strong>핵심 통찰:</strong> $y = x$ 위의 모든 점은 $(t, t)$ 꼴이며, 시작점이 이 위에 닿으면 $x$좌표와 $y$좌표가 같아집니다.
              </div>
            </div>

            <!-- Card 3 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">3단계 [00:00:10]</span>
                <span class="timeline-title">무리함수의 출발점(시작점): $(3, k)$</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/03_starting_point_3_k.jpg" alt="03_starting_point_3_k">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "지금 이 $f(x)$를 보면 시작점이 $(3, k)$지? 눈치 챘어?"
              </div>
              <div class="timeline-desc">
                <strong>해설:</strong> $x - 3 = 0 \implies x = 3$. 따라서 시작점은 $(3, k)$입니다.
              </div>
            </div>

            <!-- Card 4 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">4단계 [00:00:14]</span>
                <span class="timeline-title">3초 예고: $k = 3$일 수밖에 없는 이유</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/04_k_equals_3_preview.jpg" alt="04_k_equals_3_preview">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "$k$ 얼마여야 돼? 3이어야 돼!"
              </div>
              <div class="timeline-desc">
                <strong>직관적 결론:</strong> 시작점 $(3, k)$의 $x$좌표가 $3$이므로, $y=x$ 위에 닿으려면 $y$좌표인 $k$도 $3$이어야 합니다.
              </div>
            </div>

            <!-- Card 5 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">5단계 [00:00:20]</span>
                <span class="timeline-title">$f(x)$와 $f^{-1}(x)$ 곡선의 기하학적 스케치</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/05_inverse_curve_sketch.jpg" alt="05_inverse_curve_sketch">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "시작점이 $(3, k)$라 그래프를 그려 보니까 뭐 이렇게 되나 봐. 이제 얘를 $y = x$ 대칭하면 요게 이제 $f^{-1}(x)$일 거 아니야."
              </div>
              <div class="timeline-desc">
                <strong>작도 원리:</strong> 무리함수와 역함수(이차함수의 반쪽)는 대칭축 $y = x$를 사이에 두고 마주봅니다.
              </div>
            </div>

            <!-- Card 6 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">6단계 [00:00:28]</span>
                <span class="timeline-title">역함수를 지우고 $y = x$로 대체하기</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/06_replace_inverse_with_y_x.jpg" alt="06_replace_inverse_with_y_x">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "근데 $f(x)$와 $f^{-1}(x)$의 교점은 이 $f(x)$와 $y = x$의 교점이랑 똑같은 거잖아! 그러니까 이 $f^{-1}(x)$는 없애버리고 $y = x$로 대체하겠다는 거지!"
              </div>
              <div class="timeline-desc">
                <strong>치환 공식:</strong> $f(x) = f^{-1}(x) \iff f(x) = x$로 교점 방정식을 1차 방정식 수준으로 경량화합니다.
              </div>
            </div>

            <!-- Card 7 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">7단계 [00:00:35]</span>
                <span class="timeline-title">한 점에서 만나는 경우의 실패 (조건 불만족)</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/07_single_intersection_fail.jpg" alt="07_single_intersection_fail">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "서로 다른 두 점에서 만나라고 했는데 지금 내가 그린 그림은 안 되잖아. 왜? 한 점에서 만나니까!"
              </div>
              <div class="timeline-desc">
                <strong>실패 분석:</strong> 시작점 $(3, k)$가 $y = x$보다 위쪽($k > 3$)에 있으면 $y = x$를 한 번만 관통하여 교점이 1개뿐입니다.
              </div>
            </div>

            <!-- Card 8 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">8단계 [00:00:42]</span>
                <span class="timeline-title">곡선이 아래로 내려와 시작점이 $y = x$ 위에 도달!</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/08_slide_down_to_y_x.jpg" alt="08_slide_down_to_y_x">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "그러면 확 내려와 가지고 얘가 $y = x$ 위에 있을 때 쭉 그려 보니까 어머 되네!"
              </div>
              <div class="timeline-desc">
                <strong>핵심 판정:</strong> 시작점 $(3, 3)$이 첫 번째 교점이 되고, $(4, 4)$에서 두 번째 교점이 생겨 완벽한 2개 교점이 형성됩니다!
              </div>
            </div>

            <!-- Card 9 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">9단계 [00:00:48]</span>
                <span class="timeline-title">더 내려와도 두 점에서 만나는 유효 구간</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/09_two_intersections_valid.jpg" alt="09_two_intersections_valid">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "조금만 더 내려와도 두 점에서 만나니까 된단 말이야. 하지만 우리가 원하는 거는 $k$의 최댓값이기 때문에!"
              </div>
              <div class="timeline-desc">
                <strong>유효 범위:</strong> 접할 때인 $k = \frac{11}{4} = 2.75$부터 시작점이 닿는 $k = 3$까지가 두 점에서 만나는 범위입니다.
              </div>
            </div>

            <!-- Card 10 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">10단계 [00:00:55]</span>
                <span class="timeline-title">$k$의 최댓값 완결: $k_{\max} = 3$!</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v11/10_maximum_k_equals_3.jpg" alt="10_maximum_k_equals_3">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "$k$가 여기 왔을 때, $y = x$ 위에 왔을 때, $y$랑 $x$가 같을 때! 그래서 $k$는 3일 수밖에 없다는 거야!"
              </div>
              <div class="timeline-desc">
                <strong>결론:</strong> 시작점 $(p, k)$에서 $k_{\max} = p = 3$으로 3초 만에 문제를 해결합니다.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: PROOF & CSAT LINK (LECTURE 11) -->
      <div id="l11ProofTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px; color: var(--accent-gold);">
            📐 수학교과서식 정형화 &amp; 무리함수 5대 치트키
          </h2>

          <div style="margin-bottom: 24px;">
            <h3 style="color: var(--accent-blue); font-size: 1.15rem; margin-bottom: 8px;">1. 대수적 판별식과 기하학적 시작점의 엄밀한 결합 증명</h3>
            <p style="color: var(--text-muted); font-size: 0.94rem; line-height: 1.7;">
              무리함수 $f(x) = \sqrt{x - 3} + k$와 $y = x$의 연립방정식:
              $$\sqrt{x - 3} = x - k \implies x - 3 = (x - k)^2 = x^2 - 2kx + k^2 \iff x^2 - (2k + 1)x + k^2 + 3 = 0$$
              이차방정식의 판별식 $D$:
              $$D = (2k + 1)^2 - 4(k^2 + 3) = 4k^2 + 4k + 1 - 4k^2 - 12 = 4k - 11$$
              * $D = 0 \iff k = \frac{11}{4} = 2.75$ (접할 때)
              * 그러나 무리함수는 정의역 $x \ge 3$ 및 치역 $y \ge k$의 제한이 있으므로, 무조건 $D > 0$이라고 해서 실근이 2개가 되는 것이 아닙니다!
              * 시작점 $(3, k)$가 $y = x$보다 아래에 있으면 곡선이 $x$축 우측으로 뻗으며 $y=x$를 1번만 만나게 되고,
              * 오직 **시작점이 $y = x$ 위에 놓이거나 그 아래로 접선까지의 구간에 있을 때만 서로 다른 두 실근**을 갖습니다:
              $$\mathbf{\frac{11}{4} \le k \le 3} \implies k_{\max} = \mathbf{3}$$
            </p>
          </div>

          <div style="margin-bottom: 24px;">
            <h3 style="color: var(--accent-green); font-size: 1.15rem; margin-bottom: 8px;">2. 수능/내신 실전 무리함수 5대 치트키</h3>
            <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-color); border-radius: 12px; padding: 18px;">
              <ul style="list-style: none; padding-left: 0; display: flex; flex-direction: column; gap: 12px; font-size: 0.94rem;">
                <li>
                  <strong style="color: var(--accent-gold);">① 두 교점 존재 일반 공식:</strong>
                  $f(x) = \sqrt{a(x - p)} + k$와 $y = x$가 두 점에서 만날 조건 $\implies \mathbf{\frac{4p - a}{4} \le k \le p}$
                  $\to$ 최댓값은 언제나 $k_{\max} = p$!
                </li>
                <li>
                  <strong style="color: var(--accent-blue);">② 역함수 교점의 $y = x$ 환원 원칙:</strong>
                  증가함수 $f(x)$와 $f^{-1}(x)$의 교점은 반드시 $y = x$ 위에만 존재하므로 역함수 식을 절대 직접 구하지 않는다.
                </li>
                <li>
                  <strong style="color: var(--accent-purple);">③ 무리함수 시작점 좌표 1초 파악:</strong>
                  $y = \sqrt{ax + b} + c \implies \text{시작점 } \left(-\frac{b}{a}, c\right)$.
                </li>
                <li>
                  <strong style="color: #34d399;">④ 두 교점 사이의 거리:</strong>
                  교점 $x$좌표 $\alpha, \beta$에 대해 $l = \sqrt{2}|\beta - \alpha|$.
                </li>
                <li>
                  <strong style="color: #22d3ee;">⑤ 무리함수와 역함수로 둘러싸인 넓이:</strong>
                  $S_{\text{전체}} = 2 \times \int_{\alpha}^{\beta} (f(x) - x)dx$ (대칭축 $y=x$ 기준으로 2배).
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 4: MANIM SCRIPT (LECTURE 11) -->
      <div id="l11ManimTab" class="tab-panel">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.4rem; color: var(--accent-purple);">🎬 3Blue1Brown 스타일 Manim 파이썬 코드</h2>
              <p style="color: var(--text-dim); font-size: 0.85rem;">무리함수와 역함수의 교점 &amp; 3초 풀이법 애니메이션 (Python Manim Community v0.18+)</p>
            </div>
            <button class="tab-btn active" onclick="copyL11ManimCode()" style="padding: 8px 16px; font-size: 0.82rem;">
              📋 코드 복사
            </button>
          </div>

          <div style="background: #080d17; border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; overflow-x: auto;">
            <pre><code id="l11ManimCodeBlock" style="font-family: 'JetBrains Mono', monospace; font-size: 0.84rem; color: #e2e8f0; line-height: 1.6;">''' + manim_code_escaped + r'''</code></pre>
          </div>
        </div>
      </div>
    </div>
    <!-- END LECTURE 11 VIEW -->

'''

    # Insert lecture11_html right before <div id="lecture10View"
    target_insert_point = '<div id="lecture10View"'
    if target_insert_point not in content:
        print("ERROR: target_insert_point not found!")
        return

    content = content.replace(target_insert_point, lecture11_html + '\n    ' + target_insert_point, 1)

    # 5. Update JavaScript logic:
    # Update setLecture(num) to support 11 lectures
    old_set_lecture = '''    function setLecture(num) {
      for (let i = 1; i <= 10; i++) {
        const btn = document.getElementById(`btnLec${i}`);
        const view = document.getElementById(`lecture${i}View`);
        if (btn) btn.classList.toggle('active', i === num);
        if (view) view.style.display = (i === num) ? 'block' : 'none';
      }

      if (num === 10) setTimeout(renderL10, 50);
      else if (num === 9) setTimeout(renderL9, 50);
      else if (num === 8) setTimeout(renderL8, 50);
      else if (num === 7) setTimeout(renderL7, 50);
      else if (num === 6) setTimeout(renderL6, 50);
      else if (num === 5) setTimeout(renderL5, 50);
      else if (num === 4) setTimeout(renderL4, 50);
      else if (num === 3) setTimeout(renderL3, 50);
      else if (num === 2) setTimeout(renderL2, 50);
      else if (num === 1) setTimeout(renderL1, 50);'''

    new_set_lecture = '''    function setLecture(num) {
      for (let i = 1; i <= 11; i++) {
        const btn = document.getElementById(`btnLec${i}`);
        const view = document.getElementById(`lecture${i}View`);
        if (btn) btn.classList.toggle('active', i === num);
        if (view) view.style.display = (i === num) ? 'block' : 'none';
      }

      if (num === 11) setTimeout(renderL11, 50);
      else if (num === 10) setTimeout(renderL10, 50);
      else if (num === 9) setTimeout(renderL9, 50);
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

    # 6. Add switchLec11Tab and Lecture 11 JavaScript logic right before Lecture 10 logic
    l11_js_logic = r'''    /* ========================================================= */
    /* LECTURE 11 (IRRATIONAL FUNCTION 3-SEC RULE) LOGIC         */
    /* ========================================================= */
    function switchLec11Tab(tabId) {
      document.querySelectorAll('#lecture11View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture11View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l11SimTab') setTimeout(renderL11, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function copyL11ManimCode() {
      const code = document.getElementById('l11ManimCodeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('3Blue1Brown Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }

    const l11State = {
      k: 3.0,
      p: 3.0,
      a: 1.0
    };

    function setL11Preset(mode) {
      document.querySelectorAll('#lecture11View .preset-grid .preset-btn').forEach(b => b.classList.remove('active'));
      if (mode === 'max') {
        document.getElementById('l11PreMax').classList.add('active');
        l11State.k = 3.0; l11State.p = 3.0;
      } else if (mode === 'tan') {
        document.getElementById('l11PreTan').classList.add('active');
        l11State.k = 2.75; l11State.p = 3.0;
      } else if (mode === 'high') {
        document.getElementById('l11PreHigh').classList.add('active');
        l11State.k = 3.6; l11State.p = 3.0;
      } else if (mode === 'low') {
        document.getElementById('l11PreLow').classList.add('active');
        l11State.k = 2.2; l11State.p = 3.0;
      }

      document.getElementById('l11SliderK').value = l11State.k;
      document.getElementById('l11SliderP').value = l11State.p;
      updateL11Sliders();
    }

    function updateL11Sliders() {
      l11State.k = parseFloat(document.getElementById('l11SliderK').value);
      l11State.p = parseFloat(document.getElementById('l11SliderP').value);
      l11State.a = 1.0;

      document.getElementById('l11kVal').innerText = l11State.k.toFixed(2);
      document.getElementById('l11pVal').innerText = l11State.p.toFixed(1);
      document.getElementById('l11ValStart').innerText = `(${l11State.p.toFixed(1)}, ${l11State.k.toFixed(2)})`;
      document.getElementById('l11ValMax').innerText = l11State.p.toFixed(2);

      const k_tan = (4 * l11State.p - 1.0) / 4.0;
      document.getElementById('l11ValRange').innerText = `[${k_tan.toFixed(2)}, ${l11State.p.toFixed(2)}]`;

      // Solve for intersection with y = x:
      // sqrt(x - p) + k = x => x - p = (x - k)^2 = x^2 - 2kx + k^2
      // x^2 - (2k + 1)x + k^2 + p = 0
      const A = 1.0, B = -(2 * l11State.k + 1), C = l11State.k * l11State.k + l11State.p;
      const D = B * B - 4 * A * C;

      let countStr = '0개 (안 만남)';
      let countSub = 'D < 0 상태';
      let countColor = '#ef4444';

      if (D < -0.001) {
        countStr = '0개 (안 만남)';
        countSub = '그래프가 떨어져 있음';
        countColor = '#ef4444';
      } else if (Math.abs(D) <= 0.001) {
        countStr = '1개 (접함)';
        countSub = `D = 0 경계 (k = ${k_tan.toFixed(2)})`;
        countColor = '#38bdf8';
      } else {
        const x1 = (-B - Math.sqrt(D)) / 2;
        const x2 = (-B + Math.sqrt(D)) / 2;

        let valid1 = (x1 >= l11State.p && x1 >= l11State.k);
        let valid2 = (x2 >= l11State.p && x2 >= l11State.k);

        if (valid1 && valid2) {
          countStr = '★ 서로 다른 2개';
          countSub = (Math.abs(l11State.k - l11State.p) < 0.02) ? '🎯 k의 최댓값 달성!' : '유효 구간 내부';
          countColor = '#34d399';
        } else if (valid1 || valid2) {
          countStr = '1개 (외톨이 교점)';
          countSub = '시작점이 y=x 위쪽에 위치';
          countColor = '#f59e0b';
        } else {
          countStr = '0개 (무연근)';
          countSub = '정의역 밖';
          countColor = '#ef4444';
        }
      }

      const countEl = document.getElementById('l11ValCount');
      countEl.innerText = countStr;
      countEl.style.color = countColor;
      document.getElementById('l11ValCountSub').innerText = countSub;

      const formulaEl = document.getElementById('l11LiveFormula');
      if (formulaEl) {
        formulaEl.innerHTML = `함수: $f(x) = \\sqrt{x - ${l11State.p.toFixed(1)}} + ${l11State.k.toFixed(2)}$ $\\implies$ 시작점: $(${l11State.p.toFixed(1)}, ${l11State.k.toFixed(2)})$`;
        if (window.renderMathInElement) {
          renderMathInElement(formulaEl, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
        }
      }

      renderL11();
    }

    function renderL11() {
      const canvas = document.getElementById('l11Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const k = l11State.k, p = l11State.p;

      // Coordinate mapping: X in [0, 8], Y in [0, 8]
      const margin = 45;
      const plotW = w - margin * 2;
      const plotH = h - margin * 2;
      const xMin = 0.0, xMax = 7.5;
      const yMin = 0.0, yMax = 7.5;

      function toX(rx) { return margin + ((rx - xMin) / (xMax - xMin)) * plotW; }
      function toY(ry) { return margin + ((yMax - ry) / (yMax - yMin)) * plotH; }

      // 1. Grid & Background
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
      ctx.lineWidth = 1;
      for (let gx = 0; gx <= 7; gx++) {
        ctx.beginPath(); ctx.moveTo(toX(gx), margin); ctx.lineTo(toX(gx), h - margin); ctx.stroke();
      }
      for (let gy = 0; gy <= 7; gy++) {
        ctx.beginPath(); ctx.moveTo(margin, toY(gy)); ctx.lineTo(w - margin, toY(gy)); ctx.stroke();
      }

      // Axes (x-axis, y-axis)
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
      ctx.lineWidth = 1.5;
      const sx0 = toX(0), sy0 = toY(0);
      ctx.beginPath(); ctx.moveTo(margin, sy0); ctx.lineTo(w - margin, sy0); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(sx0, margin); ctx.lineTo(sx0, h - margin); ctx.stroke();

      ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
      ctx.font = '11px JetBrains Mono, sans-serif';
      ctx.fillText('x', w - margin + 6, sy0 + 4);
      ctx.fillText('y', sx0 - 6, margin - 8);

      // 2. Line y = x
      ctx.strokeStyle = '#fbbf24';
      ctx.lineWidth = 2.0;
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(toX(0), toY(0));
      ctx.lineTo(toX(7.2), toY(7.2));
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('y = x (대칭축)', toX(6.2), toY(6.4));

      // 3. Inverse Function f^-1(x) = (x - k)^2 + p for x >= k (Pink/Purple)
      ctx.strokeStyle = 'rgba(244, 114, 182, 0.5)';
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      let invStarted = false;
      for (let rx = k; rx <= xMax; rx += 0.05) {
        const ry = Math.pow(rx - k, 2) + p;
        if (ry <= yMax + 2) {
          const px = toX(rx), py = toY(ry);
          if (!invStarted) { ctx.moveTo(px, py); invStarted = true; }
          else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // 4. Plot Irrational Function f(x) = sqrt(x - p) + k (Cyan/Emerald)
      ctx.strokeStyle = '#22d3ee';
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      let fStarted = false;
      for (let rx = p; rx <= xMax; rx += 0.04) {
        const ry = Math.sqrt(rx - p) + k;
        if (ry <= yMax + 2) {
          const px = toX(rx), py = toY(ry);
          if (!fStarted) { ctx.moveTo(px, py); fStarted = true; }
          else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();

      // 5. Starting Point (p, k)
      const spX = toX(p), spY = toY(k);
      const isTouch = Math.abs(k - p) < 0.03;

      if (isTouch) {
        ctx.fillStyle = 'rgba(52, 211, 153, 0.3)';
        ctx.beginPath(); ctx.arc(spX, spY, 14, 0, Math.PI * 2); ctx.fill();
      }

      ctx.fillStyle = isTouch ? '#34d399' : '#fbbf24';
      ctx.beginPath(); ctx.arc(spX, spY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = '#000'; ctx.lineWidth = 2; ctx.stroke();

      ctx.fillStyle = '#fff'; ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(`시작점 (${p.toFixed(1)}, ${k.toFixed(2)})`, spX + 10, spY - 6);

      // 6. Draw Intersections with y = x
      const A = 1.0, B = -(2 * k + 1), C = k * k + p;
      const D = B * B - 4 * A * C;
      if (D >= 0) {
        const rRoots = [(-B - Math.sqrt(D)) / 2, (-B + Math.sqrt(D)) / 2];
        rRoots.forEach(rx => {
          if (rx >= p - 0.001 && rx >= k - 0.001) {
            const ix = toX(rx), iy = toY(rx);
            ctx.fillStyle = '#ef4444';
            ctx.beginPath(); ctx.arc(ix, iy, 6, 0, Math.PI * 2); ctx.fill();
            ctx.strokeStyle = '#fff'; ctx.lineWidth = 2; ctx.stroke();
            ctx.fillStyle = '#fca5a5'; ctx.font = 'bold 11px Inter, sans-serif';
            ctx.fillText(`(${rx.toFixed(1)}, ${rx.toFixed(1)})`, ix + 8, iy + 14);
          }
        });
      }

      // Legend
      ctx.fillStyle = '#22d3ee'; ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(`f(x) = √(x - ${p.toFixed(1)}) + ${k.toFixed(2)}`, margin + 10, margin + 22);

      ctx.fillStyle = 'rgba(244, 114, 182, 0.8)';
      ctx.fillText(`f⁻¹(x) = (x - ${k.toFixed(2)})² + ${p.toFixed(1)}`, margin + 10, margin + 40);
    }

'''

    l10_marker = '    /* ========================================================= */\n    /* LECTURE 10 (RATIONAL FUNCTION 3-SEC RULE) LOGIC           */'
    if l10_marker not in content:
        print("ERROR: l10_marker not found!")
        return

    content = content.replace(l10_marker, l11_js_logic + '\n' + l10_marker, 1)

    # 7. Update window load handler to initialize Lecture 11
    old_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      updateL10Sliders();
      renderL10();
    });'''

    new_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      updateL11Sliders();
      renderL11();
    });'''

    if old_load in content:
        content = content.replace(old_load, new_load, 1)

    # Write output to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: index.html updated successfully with Lecture 11!")

if __name__ == '__main__':
    main()
