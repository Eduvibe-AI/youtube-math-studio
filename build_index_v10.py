# -*- coding: utf-8 -*-
"""
Script to inject Lecture 10 (Rational Function Shift & 3-Sec Rule: Cha Gil-young) into index.html
Preserving all existing Lectures 1, 2, 3, 4, 5, 6, 7, 8, 9 without alteration.
"""

import os

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the lecture switcher bar
    old_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (9 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec9" onclick="setLecture(9)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #f59e0b, #ef4444); color: #fff;">🔥 적분과 넓이</span>
          정적분과 넓이 & 차함수의 마법 (사오수학)
        </button>
        <button class="lecture-btn" id="btnLec8" onclick="setLecture(8)">
          삼각함수 그래프 8칸 박스법 (사오수학)
        </button>'''

    new_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (10 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec10" onclick="setLecture(10)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #ec4899, #8b5cf6); color: #fff;">⚡ 3초 풀이법</span>
          유리함수 평행이동 3초 공식 (차길영)
        </button>
        <button class="lecture-btn" id="btnLec9" onclick="setLecture(9)">
          정적분과 넓이 & 차함수의 마법 (사오수학)
        </button>
        <button class="lecture-btn" id="btnLec8" onclick="setLecture(8)">
          삼각함수 그래프 8칸 박스법 (사오수학)
        </button>'''

    if old_switcher_head not in content:
        print("ERROR: old_switcher_head not found in index.html!")
        return

    content = content.replace(old_switcher_head, new_switcher_head, 1)

    # Update captured_summary button from 1~9 to 1~10
    content = content.replace('📸 사진 1~9 핵심 전용 페이지', '📸 사진 1~10 핵심 전용 페이지', 1)

    # 2. Update lecture9View to start hidden:
    old_lec9_start = '<div id="lecture9View">'
    new_lec9_start = '<div id="lecture9View" style="display: none;">'
    if old_lec9_start not in content:
        print("ERROR: old_lec9_start not found!")
        return

    content = content.replace(old_lec9_start, new_lec9_start, 1)

    # 3. Read the Manim script to include in Tab 4
    with open('rational_function_3sec_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()
    manim_code_escaped = manim_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # 4. Lecture 10 Section HTML
    lecture10_html = r'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 10 (RATIONAL FUNCTION 3-SEC RULE: CHA GIL-YOUNG) -->
    <!-- ============================================================== -->
    <div id="lecture10View">
      <header>
        <div class="badge-pill" style="border-color: rgba(236, 72, 153, 0.4); color: #f472b6; box-shadow: 0 0 20px rgba(236, 72, 153, 0.3);">
          <span>📐 고1 수학 (하) · 유리함수 1탄 · 내신 1등급 3초 킬러 공식</span>
        </div>
        <h1 style="background: linear-gradient(135deg, #ffffff 30%, #f472b6 70%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          유리함수 평행이동과 나머지 정리 3초 풀이법
        </h1>
        <p class="subtitle">
          평행이동하여 겹쳐지는 유리함수는 오직 출생 함수 $y = \frac{k}{x}$의 분자 상수 $k$에 의해서만 결정됩니다! 분모가 0 되는 $x$를 분자에 대입하는 <strong>나머지 정리 3초 스피드런 스튜디오</strong>입니다.
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>차길영의 세븐에듀</strong></span>
          <span>•</span>
          <a href="https://youtube.com/shorts/vYo2lh83hu0" target="_blank" rel="noopener noreferrer" style="color: var(--accent-blue); text-decoration: none; display: inline-flex; align-items: center; gap: 4px;">
            <span>[고1] 2학기 기말고사 수학🌟유리함수 1탄🌟 3초 풀이법 (0:56)</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
          <span>•</span>
          <span>강의 고화질 10단계 캡처 &amp; Manim 코드 탑재</span>
        </div>
      </header>

      <!-- Tab Bar for Lecture 10 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec10Tab('l10SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 3초 판정기 &amp; 유리함수 기하학 스튜디오
        </button>
        <button class="tab-btn" onclick="switchLec10Tab('l10CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 &amp; 10단계 타임라인
        </button>
        <button class="tab-btn" onclick="switchLec10Tab('l10ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          수학교과서식 정형화 &amp; 유리함수 5대 치트키
        </button>
        <button class="tab-btn" onclick="switchLec10Tab('l10ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 10) -->
      <div id="l10SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Dynamic Banner -->
          <div class="formula-banner" id="l10Banner" style="background: linear-gradient(135deg, rgba(236, 72, 153, 0.12), rgba(168, 85, 247, 0.08)); border-color: rgba(236, 72, 153, 0.35);">
            <div class="label" id="l10BannerLabel" style="color: #f472b6;">🌟 유리함수 평행이동 3초 불변 공식 (The Remainder Invariance Theorem)</div>
            <div class="math-main" id="l10BannerMath">
              $$y = \frac{ax + b}{x + d} \implies \text{분모 } x + d = 0 \text{ 대입 } \implies \mathbf{k = a(-d) + b} \quad \left(\text{평행이동 겹침 } \iff k_1 = k_2\right)$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l10Canvas" width="560" height="520"></canvas>
              <div id="l10CanvasCaption" style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                곡선: $y = \frac{ax+b}{cx+d}$ (실선) | 점근선: $x=p, y=q$ (황금색 점선) | 출생 기본형: $y=\frac{k}{x}$ (회색 점선)
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Problem Options Speedrun -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">⚡ 3초 풀이법: 시험 5개 선지 즉시 검증</span>
                  <span style="font-size: 0.8rem; color: #f472b6; font-weight: bold;">기준 $y = \frac{2x-1}{x+1} \to k = -3$</span>
                </div>
                <div class="preset-grid" style="grid-template-columns: 1fr;">
                  <button class="preset-btn" id="l10Opt1" onclick="setL10Option(1)" style="display: flex; justify-content: space-between; align-items: center;">
                    <span>① $y = \frac{2 - x}{x + 1}$</span>
                    <span class="p-sub" style="color: #ef4444; font-weight: bold;">$k = 3$ [탈락 ❌]</span>
                  </button>
                  <button class="preset-btn" id="l10Opt2" onclick="setL10Option(2)" style="display: flex; justify-content: space-between; align-items: center;">
                    <span>② $y = \frac{x + 4}{x + 1}$</span>
                    <span class="p-sub" style="color: #ef4444; font-weight: bold;">$k = 3$ [탈락 ❌]</span>
                  </button>
                  <button class="preset-btn active" id="l10Opt3" onclick="setL10Option(3)" style="display: flex; justify-content: space-between; align-items: center; border-color: #34d399; background: rgba(52, 211, 153, 0.12);">
                    <span style="color: #34d399; font-weight: bold;">③ $y = \frac{-2x - 5}{x + 1}$</span>
                    <span class="p-sub" style="color: #34d399; font-weight: bold;">$k = -3$ [★ 정답 일치! 🎯]</span>
                  </button>
                  <button class="preset-btn" id="l10Opt4" onclick="setL10Option(4)" style="display: flex; justify-content: space-between; align-items: center;">
                    <span>④ $y = \frac{x + 3}{x + 1}$</span>
                    <span class="p-sub" style="color: #ef4444; font-weight: bold;">$k = 2$ [탈락 ❌]</span>
                  </button>
                  <button class="preset-btn" id="l10Opt5" onclick="setL10Option(5)" style="display: flex; justify-content: space-between; align-items: center;">
                    <span>⑤ $y = \frac{2x + 1}{x + 1}$</span>
                    <span class="p-sub" style="color: #ef4444; font-weight: bold;">$k = -1$ [탈락 ❌]</span>
                  </button>
                </div>
              </div>

              <!-- Parameter Sliders -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎛️ $y = \frac{ax + b}{cx + d}$ 파라미터 조절</span>
                </div>

                <div class="slider-row">
                  <label>분자 $a$: <strong id="l10aVal" style="color: #f472b6;">-2.0</strong></label>
                  <input type="range" id="l10SliderA" min="-5.0" max="5.0" step="0.5" value="-2.0" oninput="updateL10Sliders()">
                </div>

                <div class="slider-row">
                  <label>분자 $b$: <strong id="l10bVal" style="color: var(--accent-blue);">-5.0</strong></label>
                  <input type="range" id="l10SliderB" min="-10.0" max="10.0" step="1.0" value="-5.0" oninput="updateL10Sliders()">
                </div>

                <div class="slider-row">
                  <label>분모 $d$: <strong id="l10dVal" style="color: var(--accent-green);">1.0</strong></label>
                  <input type="range" id="l10SliderD" min="-5.0" max="5.0" step="0.5" value="1.0" oninput="updateL10Sliders()">
                </div>
              </div>

              <!-- Live Geometry Card -->
              <div class="control-card" style="background: rgba(236, 72, 153, 0.05); border-color: rgba(236, 72, 153, 0.25);">
                <div class="control-header">
                  <span class="control-title" style="color: #f472b6;">📊 실시간 기하학적 요소 &amp; 일치성 검증</span>
                </div>

                <div class="metric-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 12px;">
                  <div class="metric-card m1">
                    <div class="metric-label">출생 분자 상수 ($k$)</div>
                    <div class="metric-val" id="l10ValK" style="color: var(--accent-gold); font-size: 1.35rem;">-3.00</div>
                    <div class="metric-sub">나머지 정리 값</div>
                  </div>
                  <div class="metric-card m2">
                    <div class="metric-label">점근선 교점 $(p, q)$</div>
                    <div class="metric-val" id="l10ValCenter" style="color: #38bdf8;">(-1.0, -2.0)</div>
                    <div class="metric-sub">대칭의 중심점</div>
                  </div>
                </div>

                <div class="metric-grid" style="grid-template-columns: 1fr 1fr;">
                  <div class="metric-card m3">
                    <div class="metric-label">평행이동 겹침 판정</div>
                    <div class="metric-val" id="l10ValMatch" style="color: #34d399; font-size: 1.15rem;">★ 100% 겹침!</div>
                    <div class="metric-sub">$k = -3$ 완벽 일치</div>
                  </div>
                  <div class="metric-card">
                    <div class="metric-label">선대칭 2대 직선</div>
                    <div class="metric-val" id="l10ValSymm" style="color: #c084fc; font-size: 0.95rem;">y = ±(x+1) - 2</div>
                    <div class="metric-sub">기울기 ±1 대칭축</div>
                  </div>
                </div>

                <div id="l10LiveFormula" style="margin-top: 14px; padding: 10px; background: rgba(0,0,0,0.3); border-radius: 8px; font-size: 0.88rem; color: #cbd5e1; text-align: center;">
                  표준형: $y = \frac{-3}{x + 1} - 2$ $\iff$ 기본형 $y = \frac{-3}{x}$을 $x$축 $-1$, $y$축 $-2$ 평행이동
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: TIMELINE CAPTURES (LECTURE 10) -->
      <div id="l10CaptureTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; margin-bottom: 8px; color: var(--accent-gold);">
            📸 차길영 선생님 강의 10단계 판서 타임라인 &amp; 교재 해설
          </h2>
          <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 24px;">
            유튜브 쇼츠(0:56) 원본 영상의 3초 풀이법 전 과정을 1080p 고화질 캡처와 함께 완벽히 분석했습니다.
          </p>

          <div class="timeline-container">
            <!-- Card 1 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">1단계 [00:00:03]</span>
                <span class="timeline-title">시험 출제 문제 세팅 &amp; 3초 풀이 선언</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/01_intro_problem_screen.jpg" alt="01_intro_problem_screen">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "이 문제가 시험에 나오면 어? 무조건 3초 풀이야! 자 답부터 얘기해 줄게."
              </div>
              <div class="timeline-desc">
                <strong>문제 분석:</strong> 함수 $y = \frac{2x - 1}{x + 1}$의 그래프를 평행이동하여 겹쳐지는 것을 보기 ①~⑤에서 고르는 전형적인 내신 킬러 빈출 문제입니다.
              </div>
            </div>

            <!-- Card 2 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">2단계 [00:00:08]</span>
                <span class="timeline-title">평행이동 겹침의 본질: 분자의 그 숫자($k$)를 찾아라!</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/02_target_numerator_rule.jpg" alt="02_target_numerator_rule">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "겹쳐지는 걸 찾잖아? 그러면 그걸 찾아야 돼. 그 분자에 있는 그 숫자를 찾아야 돼!"
              </div>
              <div class="timeline-desc">
                <strong>수학적 배경:</strong> 평행이동은 그래프의 위치만 바꿀 뿐, 곡선의 휨 정도(곡률)를 결정하는 상수 $k$는 절대 변하지 않습니다.
              </div>
            </div>

            <!-- Card 3 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">3단계 [00:00:13]</span>
                <span class="timeline-title">분모가 0 되는 $x = -1$의 분자 대입</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/03_denominator_zero_substitution.jpg" alt="03_denominator_zero_substitution">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "그럼 분모가 0이 되는 $x$값 얼마야? $-1$이지. $-1$을 분자에 넣어 봐. 얼마야? $-3$!"
              </div>
              <div class="timeline-desc">
                <strong>초고속 연산:</strong> 분모 $x + 1 = 0 \implies x = -1$. 분자 $2(-1) - 1 = \mathbf{-3}$. 단 1초 만에 분자 상수가 도출됩니다.
              </div>
            </div>

            <!-- Card 4 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">4단계 [00:00:18]</span>
                <span class="timeline-title">출생 함수(태어났을 때의 식): $y = \frac{-3}{x}$</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/04_birth_function_k_minus_3.jpg" alt="04_birth_function_k_minus_3">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "그러니까 얘는 태어났을 때 응애응애 하고 태어났을 때 식이 뭐라는 거야? $y = \frac{-3}{x}$이라는 거야!"
              </div>
              <div class="timeline-desc">
                <strong>해설:</strong> $y = \frac{2x - 1}{x + 1} = \frac{-3}{x + 1} + 2$. 즉 기본형 $y = \frac{-3}{x}$을 평행이동한 것입니다.
              </div>
            </div>

            <!-- Card 5 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">5단계 [00:00:25]</span>
                <span class="timeline-title">선지 탐색 전략: 분자 대입 결과가 $-3$인 것 찾기</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/05_search_strategy_k_minus_3.jpg" alt="05_search_strategy_k_minus_3">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "그럼 이제 $-3$ 나오는 것만 찾으면 돼!"
              </div>
              <div class="timeline-desc">
                <strong>실전 팁:</strong> 5개 선지 모두를 표준형으로 바꿀 필요 없이, 분모가 0 되는 $x=-1$을 분자에 대입해 $-3$이 나오는 선지만 픽업합니다.
              </div>
            </div>

            <!-- Card 6 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">6단계 [00:00:31]</span>
                <span class="timeline-title">①번 선지 검증: 탈락</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/06_option1_test_fail.jpg" alt="06_option1_test_fail">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "1번 봐봐. 분모가 0 되는 거 뭐야? $-1$. 분자에 넣어 봐. 얼마야? $3$. 그러니까 얘는 태어났을 때 $3$이었다는 거야. 아니지!"
              </div>
              <div class="timeline-desc">
                <strong>검산:</strong> ① $y = \frac{2-x}{x+1} \implies 2 - (-1) = 3 \ne -3$ (불일치).
              </div>
            </div>

            <!-- Card 7 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">7단계 [00:00:36]</span>
                <span class="timeline-title">②번 선지 검증: 탈락</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/07_option2_test_fail.jpg" alt="07_option2_test_fail">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "2번도 $-1$ 넣어봐. 얼마야? $3$ 나오니까 아니지!"
              </div>
              <div class="timeline-desc">
                <strong>검산:</strong> ② $y = \frac{x+4}{x+1} \implies (-1) + 4 = 3 \ne -3$ (불일치).
              </div>
            </div>

            <!-- Card 8 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">8단계 [00:00:42]</span>
                <span class="timeline-title">③번 선지 검증: 정확히 $-3$ 일치!</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/08_option3_test_match.jpg" alt="08_option3_test_match">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "3번 봐봐. $-1$ 넣어 봐. $-2(-1) - 5 = 2 - 5 = -3$! 똑같네! 답은 3번이야!"
              </div>
              <div class="timeline-desc">
                <strong>검산:</strong> ③ $y = \frac{-2x-5}{x+1} \implies -2(-1) - 5 = \mathbf{-3}$ (완벽 일치! 출생 함수 $y = \frac{-3}{x}$).
              </div>
            </div>

            <!-- Card 9 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">9단계 [00:00:48]</span>
                <span class="timeline-title">④, ⑤번 선지 확인</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/09_option4_option5_test.jpg" alt="09_option4_option5_test">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "4번은 $-1$ 넣으면 $2$, 5번은 $-1$ 넣으면 $-1$. 아니야!"
              </div>
              <div class="timeline-desc">
                <strong>검산:</strong> ④ $k = 2$, ⑤ $k = -1$로 모두 탈락.
              </div>
            </div>

            <!-- Card 10 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">10단계 [00:00:54]</span>
                <span class="timeline-title">3초 풀이 완결: 정답 ③번!</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v10/10_final_answer_3_seconds.jpg" alt="10_final_answer_3_seconds">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "답 몇 번이야? 답은 3번이야! 3초 만에 끝!"
              </div>
              <div class="timeline-desc">
                <strong>결론:</strong> 나머지 정리를 활용하면 직접 나눗셈 없이 3초 만에 평행이동 일치 문제를 정복할 수 있습니다.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: PROOF & CSAT LINK (LECTURE 10) -->
      <div id="l10ProofTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px; color: var(--accent-gold);">
            📐 수학교과서식 정형화 &amp; 유리함수 5대 치트키
          </h2>

          <div style="margin-bottom: 24px;">
            <h3 style="color: var(--accent-blue); font-size: 1.15rem; margin-bottom: 8px;">1. 나머지 정리에 의한 분자 상수 $k$ 도출 증명</h3>
            <p style="color: var(--text-muted); font-size: 0.94rem; line-height: 1.7;">
              유리함수 $y = \frac{ax + b}{cx + d}$ ($c \ne 0$)에서 분자를 분모로 나누면 몫은 $\frac{a}{c}$, 나머지는 상수 $R$이 됩니다:
              $$ax + b = \frac{a}{c}(cx + d) + R$$
              양변에 $cx + d = 0 \iff x = -\frac{d}{c}$를 대입하면 항등식 성질에 의해:
              $$R = a\left(-\frac{d}{c}\right) + b = \frac{bc - ad}{c}$$
              따라서 유리함수의 표준형은 다음과 같이 전개됩니다:
              $$y = \frac{\frac{a}{c}(cx + d) + R}{cx + d} = \frac{R}{c(x + \frac{d}{c})} + \frac{a}{c} = \frac{\frac{bc - ad}{c^2}}{x + \frac{d}{c}} + \frac{a}{c}$$
              즉, 분자 상수 $k$는 분모가 $0$이 되는 $x$를 분자에 대입한 뒤 $x$의 계수 $c$로 나눈 값 $\mathbf{k = \frac{bc - ad}{c^2}}$와 완전히 일치합니다.
            </p>
          </div>

          <div style="margin-bottom: 24px;">
            <h3 style="color: var(--accent-green); font-size: 1.15rem; margin-bottom: 8px;">2. 수능/내신 실전 유리함수 5대 치트키 총정리</h3>
            <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-color); border-radius: 12px; padding: 18px;">
              <ul style="list-style: none; padding-left: 0; display: flex; flex-direction: column; gap: 12px; font-size: 0.94rem;">
                <li>
                  <strong style="color: var(--accent-gold);">① 점근선 1초 도출:</strong>
                  세로 점근선 $x = -\frac{d}{c}$ (분모 $=0$), 가로 점근선 $y = \frac{a}{c}$ ($x$의 계수비).
                </li>
                <li>
                  <strong style="color: var(--accent-blue);">② 점근선의 교점 대칭:</strong>
                  유리함수는 점근선의 교점 $(p, q) = \left(-\frac{d}{c}, \frac{a}{c}\right)$에 대하여 점대칭입니다.
                </li>
                <li>
                  <strong style="color: var(--accent-purple);">③ 선대칭 2대 직선:</strong>
                  점근선의 교점을 지나고 기울기가 $\pm 1$인 두 직선 $y - q = \pm(x - p)$에 대하여 선대칭입니다.
                </li>
                <li>
                  <strong style="color: #34d399;">④ 역함수 1초 공식:</strong>
                  $f(x) = \frac{ax+b}{cx+d} \iff f^{-1}(x) = \frac{-dx+b}{cx-a}$ (주대각선 $a, d$ 자리와 부호 동시 반전).
                </li>
                <li>
                  <strong style="color: #f472b6;">⑤ 점근선 교점에서 곡선 위 점까지의 최소거리:</strong>
                  곡선 위의 임의의 점에서 점근선 교점까지의 최단거리는 $d_{\min} = \sqrt{2|k|}$ (산술·기하 평균에 의해 유도).
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 4: MANIM SCRIPT (LECTURE 10) -->
      <div id="l10ManimTab" class="tab-panel">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.4rem; color: var(--accent-purple);">🎬 3Blue1Brown 스타일 Manim 파이썬 코드</h2>
              <p style="color: var(--text-dim); font-size: 0.85rem;">유리함수 평행이동과 나머지 정리 3초 풀이법 애니메이션 (Python Manim Community v0.18+)</p>
            </div>
            <button class="tab-btn active" onclick="copyL10ManimCode()" style="padding: 8px 16px; font-size: 0.82rem;">
              📋 코드 복사
            </button>
          </div>

          <div style="background: #080d17; border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; overflow-x: auto;">
            <pre><code id="l10ManimCodeBlock" style="font-family: 'JetBrains Mono', monospace; font-size: 0.84rem; color: #e2e8f0; line-height: 1.6;">''' + manim_code_escaped + r'''</code></pre>
          </div>
        </div>
      </div>
    </div>
    <!-- END LECTURE 10 VIEW -->

'''

    # Insert lecture10_html right before <div id="lecture9View"
    target_insert_point = '<div id="lecture9View"'
    if target_insert_point not in content:
        print("ERROR: target_insert_point not found!")
        return

    content = content.replace(target_insert_point, lecture10_html + '\n    ' + target_insert_point, 1)

    # 5. Update JavaScript logic:
    # Update setLecture(num) to support 10 lectures
    old_set_lecture = '''    function setLecture(num) {
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

    new_set_lecture = '''    function setLecture(num) {
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

    if old_set_lecture not in content:
        print("ERROR: old_set_lecture not found!")
        return

    content = content.replace(old_set_lecture, new_set_lecture, 1)

    # 6. Add switchLec10Tab and Lecture 10 JavaScript logic right before Lecture 9 logic
    l10_js_logic = r'''    /* ========================================================= */
    /* LECTURE 10 (RATIONAL FUNCTION 3-SEC RULE) LOGIC           */
    /* ========================================================= */
    function switchLec10Tab(tabId) {
      document.querySelectorAll('#lecture10View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture10View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l10SimTab') setTimeout(renderL10, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function copyL10ManimCode() {
      const code = document.getElementById('l10ManimCodeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('3Blue1Brown Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }

    const l10State = {
      opt: 3, // 1, 2, 3, 4, 5
      a: -2.0,
      b: -5.0,
      c: 1.0,
      d: 1.0
    };

    function setL10Option(optNum) {
      l10State.opt = optNum;
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`l10Opt${i}`);
        if (btn) btn.classList.toggle('active', i === optNum);
      }

      if (optNum === 1) { // y = (2 - x)/(x + 1) = (-x + 2)/(x + 1)
        l10State.a = -1.0; l10State.b = 2.0; l10State.c = 1.0; l10State.d = 1.0;
      } else if (optNum === 2) { // y = (x + 4)/(x + 1)
        l10State.a = 1.0; l10State.b = 4.0; l10State.c = 1.0; l10State.d = 1.0;
      } else if (optNum === 3) { // y = (-2x - 5)/(x + 1) [CORRECT]
        l10State.a = -2.0; l10State.b = -5.0; l10State.c = 1.0; l10State.d = 1.0;
      } else if (optNum === 4) { // y = (x + 3)/(x + 1)
        l10State.a = 1.0; l10State.b = 3.0; l10State.c = 1.0; l10State.d = 1.0;
      } else if (optNum === 5) { // y = (2x + 1)/(x + 1)
        l10State.a = 2.0; l10State.b = 1.0; l10State.c = 1.0; l10State.d = 1.0;
      }

      document.getElementById('l10SliderA').value = l10State.a;
      document.getElementById('l10SliderB').value = l10State.b;
      document.getElementById('l10SliderD').value = l10State.d;

      updateL10Sliders();
    }

    function updateL10Sliders() {
      l10State.a = parseFloat(document.getElementById('l10SliderA').value);
      l10State.b = parseFloat(document.getElementById('l10SliderB').value);
      l10State.d = parseFloat(document.getElementById('l10SliderD').value);
      l10State.c = 1.0;

      document.getElementById('l10aVal').innerText = l10State.a.toFixed(1);
      document.getElementById('l10bVal').innerText = l10State.b.toFixed(1);
      document.getElementById('l10dVal').innerText = l10State.d.toFixed(1);

      // Remainder Theorem calculation:
      // Denominator cx + d = 0 => x0 = -d/c
      const x0 = -l10State.d / l10State.c;
      // Remainder R = a(x0) + b
      const R = l10State.a * x0 + l10State.b;
      // k = R / c
      const k = R / l10State.c;
      const p = -l10State.d / l10State.c;
      const q = l10State.a / l10State.c;

      document.getElementById('l10ValK').innerText = k.toFixed(2);
      document.getElementById('l10ValCenter').innerText = `(${p.toFixed(1)}, ${q.toFixed(1)})`;

      const isMatch = Math.abs(k - (-3.0)) < 0.05;
      const matchEl = document.getElementById('l10ValMatch');
      if (isMatch) {
        matchEl.innerText = '★ 100% 겹침! (정답)';
        matchEl.style.color = '#34d399';
      } else {
        matchEl.innerText = `불일치 (k=${k.toFixed(1)} ≠ -3)`;
        matchEl.style.color = '#ef4444';
      }

      document.getElementById('l10ValSymm').innerText = `y = ±(x - ${p.toFixed(1)}) + ${q.toFixed(1)}`;

      const formulaEl = document.getElementById('l10LiveFormula');
      if (formulaEl) {
        formulaEl.innerHTML = `표준형: $y = \\frac{${k.toFixed(1)}}{x - (${p.toFixed(1)})} + (${q.toFixed(1)})$ $\\implies$ 기본형 $y = \\frac{${k.toFixed(1)}}{x}$ 평행이동`;
        if (window.renderMathInElement) {
          renderMathInElement(formulaEl, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
        }
      }

      renderL10();
    }

    function renderL10() {
      const canvas = document.getElementById('l10Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const a = l10State.a, b = l10State.b, c = l10State.c, d = l10State.d;
      const x0 = -d / c;
      const k = (a * x0 + b) / c;
      const p = -d / c;
      const q = a / c;

      // Coordinate boundaries: X in [-7, 5], Y in [-7, 7]
      const margin = 40;
      const plotW = w - margin * 2;
      const plotH = h - margin * 2;
      const xMin = -6.5, xMax = 5.0;
      const yMin = -6.5, yMax = 6.5;

      function toX(rx) { return margin + ((rx - xMin) / (xMax - xMin)) * plotW; }
      function toY(ry) { return margin + ((yMax - ry) / (yMax - yMin)) * plotH; }

      // 1. Grid & Background
      ctx.fillStyle = '#080d1a';
      ctx.fillRect(0, 0, w, h);

      ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
      ctx.lineWidth = 1;
      for (let gx = Math.ceil(xMin); gx <= xMax; gx++) {
        ctx.beginPath(); ctx.moveTo(toX(gx), margin); ctx.lineTo(toX(gx), h - margin); ctx.stroke();
      }
      for (let gy = Math.ceil(yMin); gy <= yMax; gy++) {
        ctx.beginPath(); ctx.moveTo(margin, toY(gy)); ctx.lineTo(w - margin, toY(gy)); ctx.stroke();
      }

      // Axes (x-axis, y-axis)
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
      ctx.lineWidth = 1.5;
      const sx0 = toX(0), sy0 = toY(0);
      ctx.beginPath(); ctx.moveTo(margin, sy0); ctx.lineTo(w - margin, sy0); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(sx0, margin); ctx.lineTo(sx0, h - margin); ctx.stroke();

      // Axis labels
      ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.font = '11px JetBrains Mono, sans-serif';
      ctx.fillText('x', w - margin + 6, sy0 + 4);
      ctx.fillText('y', sx0 - 6, margin - 8);

      // 2. Base Function y = -3/x (Reference dashed curve)
      ctx.strokeStyle = 'rgba(148, 163, 184, 0.35)';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);

      // Left branch of base
      ctx.beginPath();
      for (let rx = xMin; rx <= -0.15; rx += 0.05) {
        const ry = -3.0 / rx;
        if (ry >= yMin && ry <= yMax) {
          const px = toX(rx), py = toY(ry);
          if (rx === xMin) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();

      // Right branch of base
      ctx.beginPath();
      for (let rx = 0.15; rx <= xMax; rx += 0.05) {
        const ry = -3.0 / rx;
        if (ry >= yMin && ry <= yMax) {
          const px = toX(rx), py = toY(ry);
          if (rx === 0.15) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // 3. Asymptotes (x = p, y = q)
      const spx = toX(p), sqy = toY(q);
      ctx.strokeStyle = '#fbbf24';
      ctx.lineWidth = 1.8;
      ctx.setLineDash([5, 5]);

      // Vertical asymptote x = p
      ctx.beginPath(); ctx.moveTo(spx, margin); ctx.lineTo(spx, h - margin); ctx.stroke();
      // Horizontal asymptote y = q
      ctx.beginPath(); ctx.moveTo(margin, sqy); ctx.lineTo(w - margin, sqy); ctx.stroke();
      ctx.setLineDash([]);

      // Asymptote labels
      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText(`x = ${p.toFixed(1)}`, spx + 6, margin + 16);
      ctx.fillText(`y = ${q.toFixed(1)}`, margin + 8, sqy - 8);

      // 4. Center Dot (p, q)
      ctx.fillStyle = '#fbbf24';
      ctx.beginPath(); ctx.arc(spx, sqy, 6, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = '#000'; ctx.lineWidth = 2; ctx.stroke();
      ctx.fillText(`(${p.toFixed(1)}, ${q.toFixed(1)})`, spx + 8, sqy + 16);

      // 5. Symmetric Axes Lines: y = (x - p) + q, y = -(x - p) + q
      ctx.strokeStyle = 'rgba(192, 132, 252, 0.35)';
      ctx.lineWidth = 1.2;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(toX(xMin), toY((xMin - p) + q));
      ctx.lineTo(toX(xMax), toY((xMax - p) + q));
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(toX(xMin), toY(-(xMin - p) + q));
      ctx.lineTo(toX(xMax), toY(-(xMax - p) + q));
      ctx.stroke();
      ctx.setLineDash([]);

      // 6. Plot Current Rational Function y = (ax + b)/(cx + d)
      const isMatch = Math.abs(k - (-3.0)) < 0.05;
      ctx.strokeStyle = isMatch ? '#34d399' : '#f472b6';
      ctx.lineWidth = 3;

      // Branch 1: Left of asymptote (x < p)
      ctx.beginPath();
      let started = false;
      for (let rx = xMin; rx <= p - 0.08; rx += 0.03) {
        const ry = (a * rx + b) / (c * rx + d);
        if (ry >= yMin - 2 && ry <= yMax + 2) {
          const px = toX(rx), py = toY(ry);
          if (!started) { ctx.moveTo(px, py); started = true; }
          else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();

      // Branch 2: Right of asymptote (x > p)
      ctx.beginPath();
      started = false;
      for (let rx = p + 0.08; rx <= xMax; rx += 0.03) {
        const ry = (a * rx + b) / (c * rx + d);
        if (ry >= yMin - 2 && ry <= yMax + 2) {
          const px = toX(rx), py = toY(ry);
          if (!started) { ctx.moveTo(px, py); started = true; }
          else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();

      // 7. Legend & Callout
      ctx.fillStyle = isMatch ? '#34d399' : '#f472b6';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText(`현재 곡선: y = (${a.toFixed(1)}x + ${b.toFixed(1)}) / (x + ${d.toFixed(1)})`, margin + 10, margin + 20);

      ctx.fillStyle = 'rgba(148, 163, 184, 0.7)';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('회색 점선: 원본 출생 기본형 y = -3/x', margin + 10, margin + 38);
    }

'''

    l9_marker = '    /* ========================================================= */\n    /* LECTURE 9 (DEFINITE INTEGRAL & AREA: DIFF FUNCTION) LOGIC */'
    if l9_marker not in content:
        print("ERROR: l9_marker not found!")
        return

    content = content.replace(l9_marker, l10_js_logic + '\n' + l9_marker, 1)

    # 7. Update window load handler to initialize Lecture 10
    old_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      updateL9Sliders();
      renderL9();
    });'''

    new_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      updateL10Sliders();
      renderL10();
    });'''

    if old_load in content:
        content = content.replace(old_load, new_load, 1)

    # Write output to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: index.html updated successfully with Lecture 10!")

if __name__ == '__main__':
    main()
