# -*- coding: utf-8 -*-
"""
Script to build and inject Lecture 13 into index.html
Lecture: The Difference Between y and f(x): Territory vs Resident & 4 Absolute Value Graphs
Instructor: Bae Sang-myeon (MathPresso / Chulbyuk Math)
YouTube Short: https://youtube.com/shorts/-Kcc-4UwVCg
"""

import os
import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code for tab
    with open('y_vs_fx_absolute_value_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()

    # 1. Update Switcher Bar: Add btnLec13 as active, remove active from btnLec12
    if 'id="btnLec13"' not in html:
        old_btn12 = '<button class="lecture-btn active" id="btnLec12" onclick="setLecture(12)">'
        if old_btn12 in html:
            new_btn_block = '''<button class="lecture-btn active" id="btnLec13" onclick="setLecture(13)">
          $y$와 $f(x)$ 차이 &amp; 절댓값 (배상면)
        </button>
        <button class="lecture-btn" id="btnLec12" onclick="setLecture(12)">'''
            html = html.replace(old_btn12, new_btn_block, 1)
            print("Added btnLec13 to switcher bar.")
        else:
            old_btn12_alt = '<button class="lecture-btn" id="btnLec12" onclick="setLecture(12)">'
            if old_btn12_alt in html:
                new_btn_block = '''<button class="lecture-btn active" id="btnLec13" onclick="setLecture(13)">
          $y$와 $f(x)$ 차이 &amp; 절댓값 (배상면)
        </button>
        <button class="lecture-btn" id="btnLec12" onclick="setLecture(12)">'''
                html = html.replace(old_btn12_alt, new_btn_block, 1)
                print("Added btnLec13 to switcher bar (alt).")

    # Update captured_summary button label
    html = html.replace('📸 사진 1~12 핵심 전용 페이지', '📸 사진 1~13 핵심 전용 페이지')

    # 2. Hide lecture12View if active
    if '<div id="lecture12View">' in html:
        html = html.replace('<div id="lecture12View">', '<div id="lecture12View" style="display: none;">', 1)
        print("Set lecture12View to display: none.")

    # 3. Create Lecture 13 View HTML
    escaped_manim = (manim_code
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))

    lecture13_html = f'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 13 (Y VS F(X): TERRITORY VS RESIDENT: MATHPRESSO) -->
    <!-- ============================================================== -->
    <div id="lecture13View">
      <header>
        <div class="badge-pill" style="border-color: rgba(245, 158, 11, 0.4); color: #fbbf24; box-shadow: 0 0 20px rgba(245, 158, 11, 0.3);">
          <span>📐 고1 수학 · 함수 &amp; 도형의 이동 · 4대 절댓값 그래프 완전 정복</span>
        </div>
        <h1 style="background: linear-gradient(135deg, #ffffff 30%, #fbbf24 70%, #f97316 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          $y$와 $f(x)$의 본질적 차이: 영역(영토) vs 그래프(사람)
        </h1>
        <p class="subtitle">
          "지구가 스케치북이면 $x$축은 적도! $y$는 영토이고, $f(x)$는 사람이다!" $|y| = f(x)$의 상하 대칭 영토 복사와 $y = |f(x)|$의 남쪽 사람 꺾어 올리기를 통해 <strong>함수와 대칭의 본질을 꿰뚫는 인터랙티브 스튜디오</strong>입니다.
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>매스프레소 MathPresso (배상면 선생님)</strong></span>
          <span>•</span>
          <a href="https://youtube.com/shorts/-Kcc-4UwVCg" target="_blank" rel="noopener noreferrer" style="color: var(--accent-blue); text-decoration: none; display: inline-flex; align-items: center; gap: 4px;">
            <span>"y와 f(x) 차이" 솔직히 모르지?! (0:52)</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
          <span>•</span>
          <span>강의 고화질 10단계 캡처 &amp; Manim 코드 탑재</span>
        </div>
      </header>

      <!-- Tab Bar for Lecture 13 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec13Tab('l13SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 영토 vs 사람 절댓값 스튜디오
        </button>
        <button class="tab-btn" onclick="switchLec13Tab('l13CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 &amp; 10단계 타임라인
        </button>
        <button class="tab-btn" onclick="switchLec13Tab('l13ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          4대 절댓값 함수 교과서식 정형화 &amp; 킬러 치트키
        </button>
        <button class="tab-btn" onclick="switchLec13Tab('l13ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 13) -->
      <div id="l13SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Dynamic Banner -->
          <div class="formula-banner" id="l13Banner" style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(239, 68, 68, 0.08)); border-color: rgba(245, 158, 11, 0.35);">
            <div class="label" id="l13BannerLabel" style="color: #fbbf24;">🌟 배상면 선생님의 본질적 명제 : $y$는 영토(Territory), $f(x)$는 사람(Resident)</div>
            <div class="math-main" id="l13BannerMath">
              $$|y| = f(x) \\iff \\text{{남반구 영토 대칭 복사 (상하 대칭)}} \\quad \\longleftrightarrow \\quad y = |f(x)| \\iff \\text{{남쪽 사람 북반구 이주 (꺾어 올리기)}}$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l13Canvas" width="580" height="520"></canvas>
              <div id="l13CanvasCaption" style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                북반구 영토 $y \\ge 0$ (연노랑) | 남반구 영토 $y < 0$ (청록) | 적도 $x$축 (실선) | 변환 결과 곡선 (선명한 네온)
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Mode Selection -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎯 4대 절댓값 변환 모드 선택</span>
                </div>
                <div class="preset-grid" style="grid-template-columns: 1fr 1fr;">
                  <button class="preset-btn" id="l13ModeOrig" onclick="setL13Mode('orig')">
                    <span>0. 오리지널 $y = f(x)$</span>
                    <span class="p-sub" style="color: #94a3b8;">원형 곡선 그대로</span>
                  </button>
                  <button class="preset-btn active" id="l13ModeAbsY" onclick="setL13Mode('absY')">
                    <span>1. $|y| = f(x)$ (영토) 🎯</span>
                    <span class="p-sub" style="color: #38bdf8; font-weight: bold;">상하 대칭 복사 (남반구)</span>
                  </button>
                  <button class="preset-btn" id="l13ModeAbsFx" onclick="setL13Mode('absFx')">
                    <span>2. $y = |f(x)|$ (사람) 🚀</span>
                    <span class="p-sub" style="color: #fbbf24; font-weight: bold;">꺾어 올리기 (V-Fold)</span>
                  </button>
                  <button class="preset-btn" id="l13ModeAbsX" onclick="setL13Mode('absX')">
                    <span>3. $y = f(|x|)$ (우함수)</span>
                    <span class="p-sub" style="color: #a78bfa;">$x \\ge 0$ 남기고 $y$축 대칭</span>
                  </button>
                  <button class="preset-btn" id="l13ModeAbsBoth" onclick="setL13Mode('absBoth')" style="grid-column: span 2;">
                    <span>4. $|y| = f(|x|)$ (4방향 대칭) 💎</span>
                    <span class="p-sub" style="color: #34d399;">제1사분면만 남기고 $x, y,$ 원점 3중 복사</span>
                  </button>
                </div>
              </div>

              <!-- Base Function Selector -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">📈 기본 함수 $f(x)$ 프리셋 선택</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <button class="preset-btn active" id="l13FuncCubic" onclick="setL13Func('cubic')">
                    <span>삼차함수 (영상 원본)</span>
                    <span class="p-sub">$0.25x(x+2.3)(x-2.1)$</span>
                  </button>
                  <button class="preset-btn" id="l13FuncQuad" onclick="setL13Func('quad')">
                    <span>이차함수 (포물선)</span>
                    <span class="p-sub">$x^2 - 3.5$</span>
                  </button>
                  <button class="preset-btn" id="l13FuncLine" onclick="setL13Func('line')">
                    <span>일차함수 (직선)</span>
                    <span class="p-sub">$1.2x - 1.0$</span>
                  </button>
                  <button class="preset-btn" id="l13FuncSin" onclick="setL13Func('sin')">
                    <span>삼각함수 (사인파)</span>
                    <span class="p-sub">$2.0 \\sin(x)$</span>
                  </button>
                </div>
              </div>

              <!-- Visual Layer Toggles -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">👁️ 지구-적도 시각화 레이어 On/Off</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.85rem;">
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                    <input type="checkbox" id="l13ToggleEquator" checked onchange="updateL13Toggles()">
                    <span>적도($x$축) &amp; 영토 틴트</span>
                  </label>
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                    <input type="checkbox" id="l13ToggleGhost" checked onchange="updateL13Toggles()">
                    <span>오리지널 잔상 고스트</span>
                  </label>
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer; grid-column: span 2;">
                    <input type="checkbox" id="l13ToggleResidents" checked onchange="updateL13Toggles()">
                    <span>사람(곡선 상의 주요 점들) 동적 표시</span>
                  </label>
                </div>
              </div>

              <!-- Live Analysis Card -->
              <div class="control-card" style="background: rgba(15, 23, 42, 0.95); border-color: rgba(245, 158, 11, 0.4);">
                <div class="control-header">
                  <span class="control-title" style="color: #fbbf24;">🔍 수학적 정의 &amp; 함수성 판정</span>
                  <span class="badge-pill-sm" id="l13FuncBadge" style="background: #ef4444; color: #fff;">함수 아님 (관계식 ❌)</span>
                </div>

                <div id="l13LiveDefText" style="margin-top: 10px; padding: 12px; background: rgba(0,0,0,0.35); border-radius: 8px; font-size: 0.84rem; color: #cbd5e1; line-height: 1.7;">
                  • <strong>식의 의미:</strong> $y \\ge 0 \\implies y = f(x)$, $y < 0 \\implies y = -f(x)$<br>
                  • <strong>기하학적 조작:</strong> $x$축 위($y \\ge 0$)를 남기고 $x$축 대칭 복사!<br>
                  • <strong>배티의 비유:</strong> 남반구 영토에 북반구 지도를 데칼코마니로 찍어냄<br>
                  • <strong>수직선 판정:</strong> 하나의 $x$에 $y$가 2개 대응되므로 함수가 아닙니다.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: TIMELINE CAPTURES (LECTURE 13) -->
      <div id="l13CaptureTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; margin-bottom: 8px; color: var(--accent-gold);">
            📸 배상면 선생님 강의 10단계 판서 타임라인 &amp; 교재 해설
          </h2>
          <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 24px;">
            유튜브 쇼츠(0:52) 원본 영상의 $y$와 $f(x)$ 개념 판서 전 과정을 1080p 고화질 캡처와 함께 완벽히 분석했습니다.
          </p>

          <div class="timeline-container">
            <!-- Card 1 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">1단계 [00:00:02]</span>
                <span class="timeline-title">인트로: "y와 f(x) 차이 솔직히 모른다에 한 표!"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/01_intro_y_vs_fx_question.jpg" alt="01_intro_y_vs_fx_question">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "y, f(x) 차이 솔직히 모른다! 절댓값 그래프를 접수하면 y와 f(x)의 차이는 덤이다."
              </div>
              <div class="timeline-desc">
                <strong>출제 의도:</strong> 중학교 때부터 $y = f(x)$로 써왔기 때문에 둘을 무의식적으로 동일시하는 수험생들의 맹점을 날카롭게 찌릅니다.
              </div>
            </div>

            <!-- Card 2 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">2단계 [00:00:07]</span>
                <span class="timeline-title">오리지널 함수 $y = f(x)$ 그래프 세팅</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/02_original_curve_setup.jpg" alt="02_original_curve_setup">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "$y = f(x)$ 오리지널 그래프가 요래 생겼을 때..."
              </div>
              <div class="timeline-desc">
                <strong>곡선 세팅:</strong> 원점을 지나며 $x$축 위($f(x) > 0$)와 $x$축 아래($f(x) < 0$)를 모두 드나드는 기준 곡선 $y = f(x)$를 제시합니다.
              </div>
            </div>

            <!-- Card 3 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">3단계 [00:00:11]</span>
                <span class="timeline-title">$|y| = f(x)$ 식 제시 및 $y$ 영역 분할</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/03_abs_y_equals_fx_definition.jpg" alt="03_abs_y_equals_fx_definition">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "y의 절댓값 씌운 그래프는 $y$가 0 이상일 때는 오리지널 유지..."
              </div>
              <div class="timeline-desc">
                <strong>정의 분석:</strong> 절댓값의 성질에 따라 $y \\ge 0$에서는 $|y| = y$이므로 $y = f(x)$를 그대로 그립니다.
              </div>
            </div>

            <!-- Card 4 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">4단계 [00:00:17]</span>
                <span class="timeline-title">$|y| = f(x)$ 상하 대칭형 그래프 완성</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/04_abs_y_symmetric_graph.jpg" alt="04_abs_y_symmetric_graph">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "...y가 0보다 작을 때는 오리지널을 x축 대칭 이동하면 상하 대칭형이 되고..."
              </div>
              <div class="timeline-desc">
                <strong>상하 대칭 복사:</strong> $y < 0$에서는 $-y = f(x) \\iff y = -f(x)$가 되어 $x$축 아래로 데칼코마니 복사됩니다. 단, $f(x) < 0$인 구간은 실수가 존재하지 않아 빈 공간이 됩니다!
              </div>
            </div>

            <!-- Card 5 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">5단계 [00:00:22]</span>
                <span class="timeline-title">$y = |f(x)|$ 식 제시 및 $f(x)$ 부호 분할</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/05_y_equals_abs_fx_definition.jpg" alt="05_y_equals_abs_fx_definition">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "f(x)의 절댓값 씌운 그래프는 f(x)가 0 이상일 때 오리지널 유지..."
              </div>
              <div class="timeline-desc">
                <strong>수식 대비:</strong> 이번에는 $y$가 아닌 함수값 전체 $f(x)$에 절댓값을 씌웁니다. $f(x) \\ge 0$인 점들은 원래 자리를 지킵니다.
              </div>
            </div>

            <!-- Card 6 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">6단계 [00:00:27]</span>
                <span class="timeline-title">$y = |f(x)|$ $x$축 아래 꺾어 올리기 (V-Fold)</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/06_y_equals_abs_fx_fold_up.jpg" alt="06_y_equals_abs_fx_fold_up">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "...f(x)가 0보다 작을 때 오리지널을 꺾어 올리기가 된다."
              </div>
              <div class="timeline-desc">
                <strong>접어 올리기:</strong> $f(x) < 0$인 점들은 $y = -f(x)$가 되어 $x$축 위로 접혀 올라옵니다. 수능 미적분의 뾰족점(첨점)이 만들어지는 순간입니다.
              </div>
            </div>

            <!-- Card 7 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">7단계 [00:00:29]</span>
                <span class="timeline-title">학생들의 단골 의문: "아니, 식으로는 같은 거 아닌가요?"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/07_common_doubt_same_equation.jpg" alt="07_common_doubt_same_equation">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "아니, 식으로는 같은 거 아닌가요?"
              </div>
              <div class="timeline-desc">
                <strong>학생 심리 대변:</strong> "$y = f(x)$니까 $|y| = f(x)$나 $y = |f(x)|$나 양변에 절댓값 씌운 거니 같지 않나?"라는 전국의 수포자들이 하는 질문입니다.
              </div>
            </div>

            <!-- Card 8 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">8단계 [00:00:34]</span>
                <span class="timeline-title">$y$는 영역(영토), $f(x)$는 그래프(사람)의 본질</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/08_territory_vs_resident_concept.jpg" alt="08_territory_vs_resident_concept">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "y가 음인 건 x축 아래 영역을 뜻하고, f(x)가 음인 건 x축 아래에 있는 그래프를 뜻한다."
              </div>
              <div class="timeline-desc">
                <strong>명쾌한 개념 분리:</strong> $y$는 '공간/좌표 구역' 자체이고, $f(x)$는 그 공간 속을 지나가는 '곡선 위의 점들의 모임'입니다.
              </div>
            </div>

            <!-- Card 9 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">9단계 [00:00:41]</span>
                <span class="timeline-title">지구 스케치북 &amp; 적도 대칭 비유 (Earth Analogy)</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/09_earth_equator_analogy.jpg" alt="09_earth_equator_analogy">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "즉 지구가 스케치북이면 x축은 적도! 남반구 영토에는 오리지널을 적도에 대칭 이동시키고, 남쪽 사람은 적도 반대편 위로 이주시킨다."
              </div>
              <div class="timeline-desc">
                <strong>환상적인 직관:</strong> $|y| = f(x)$는 남반구 영토에 북반구 지도를 복사한 것이고, $y = |f(x)|$는 남쪽에 사는 사람만 북쪽으로 피난 이주시킨 것입니다!
              </div>
            </div>

            <!-- Card 10 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">10단계 [00:00:47]</span>
                <span class="timeline-title">최종 결론: "$y$는 영토, $f(x)$는 사람이다!"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v13/10_final_epiphany_y_is_territory.jpg" alt="10_final_epiphany_y_is_territory">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "y는 영토, f(x)는 사람이다!"
              </div>
              <div class="timeline-desc">
                <strong>개념 완결:</strong> 이제 $x, y, f(x)$ 어디에 절댓값이 붙더라도 이 원리 하나로 4대 절댓값 함수 그래프를 1초 만에 스케치할 수 있습니다!
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: MATHEMATICAL PROOF & 4 TYPES (LECTURE 13) -->
      <div id="l13ProofTab" class="tab-panel">
        <div class="glass-card" style="line-height: 1.8;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px; color: #fbbf24;">
            📐 고1 수학(하) 4대 절댓값 함수의 교과서식 정형화 &amp; 킬러 치트키
          </h2>
          
          <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 12px; border-left: 4px solid #fbbf24; margin-bottom: 24px;">
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">1. $y$와 $f(x)$의 수학적 정의 차이</h3>
            <p>
              $y = f(x)$라는 기호에서:
            </p>
            <ul style="padding-left: 20px; margin-top: 8px; color: #cbd5e1;">
              <li><strong>$x, y$ (변수, 좌표평면의 축):</strong> 평면 $\\mathbb{{R}}^2$ 위의 위치를 나타내는 독립변수와 종속변수입니다. 부등식 $y \\ge 0$, $y < 0$은 각각 $x$축 위쪽, 아래쪽의 **2차원 반평면 영역(영토, Territory)**을 규정합니다.</li>
              <li><strong>$f(x)$ (함숫값, 대응 규칙):</strong> 각 $x$에 대하여 $f$라는 규칙에 의해 계산된 결과값(스칼라)입니다. 부등식 $f(x) < 0$은 곡선 위의 점들 중 **함숫값이 음수인 특정 점들(사람, Resident)**을 지칭합니다.</li>
            </ul>
          </div>

          <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 12px; border-left: 4px solid #38bdf8; margin-bottom: 24px;">
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">2. 시험에 100% 출제되는 4대 절댓값 그래프 총정리</h3>
            <table style="width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 0.88rem; color: #cbd5e1;">
              <thead>
                <tr style="background: rgba(255,255,255,0.06); text-align: left;">
                  <th style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">형태</th>
                  <th style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">그리는 원리</th>
                  <th style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">대칭성 &amp; 특징</th>
                  <th style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">함수 여부</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); font-weight: bold; color: #fbbf24;">① $y = |f(x)|$</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">$f(x) < 0$인 곡선(남쪽 사람)을 $x$축 위로 꺾어 올림</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">치역 $y \\ge 0$, 접촉점에서 뾰족점(첨점) 발생</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); color: #34d399;">함수 O</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); font-weight: bold; color: #38bdf8;">② $|y| = f(x)$</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">$y \\ge 0$ 영토만 남기고 $x$축 대칭 복사</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">$x$축 상하 대칭형, $f(x) < 0$ 구간은 그래프 소멸</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); color: #ef4444;">함수 X (관계식)</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); font-weight: bold; color: #a78bfa;">③ $y = f(|x|)$</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">$x \\ge 0$ 영토만 남기고 $y$축 대칭 복사</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">$y$축 좌우 대칭 (우함수/짝함수화: $f(-x) = f(x)$)</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); color: #34d399;">함수 O</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); font-weight: bold; color: #f472b6;">④ $|y| = f(|x|)$</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">제1사분면($x\\ge 0, y\\ge 0$)만 남기고 $x, y,$ 원점 3중 복사</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">4방향 대칭 (마름모형 닫힌 곡선 형성)</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); color: #ef4444;">함수 X (관계식)</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 12px; border-left: 4px solid #34d399;">
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">3. 수능 수학Ⅱ 킬러 문항과의 직결성</h3>
            <ul style="padding-left: 20px; color: #cbd5e1;">
              <li><strong>$g(x) = |f(x) - t|$ 미분가능성:</strong> 함수 $y = f(x)$와 상수함수 $y = t$가 만나는 점에서 $y = t$를 새로운 기준선(새로운 적도!)으로 삼아 아래쪽을 접어 올립니다. 접선 기울기가 0이 아닌 곳에서 꺾이면 반드시 미분불가능한 첨점이 됩니다!</li>
              <li><strong>넓이 2배 테크닉:</strong> $|y| = f(x)$ 꼴로 둘러싸인 도형의 넓이를 구할 때는 상하 대칭이므로, $y \\ge 0$인 위쪽 영역의 정적분 $\\int f(x) dx$를 구한 뒤 **정확히 2배**를 곱해주면 계산이 순식간에 끝납니다.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 4: MANIM PYTHON SCRIPT (LECTURE 13) -->
      <div id="l13ManimTab" class="tab-panel">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.4rem; color: #fbbf24;">3Blue1Brown 스타일 Manim 파이썬 애니메이션 코드</h2>
              <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">
                `y_vs_fx_absolute_value_manim.py` - 수학교육용 수학 애니메이션 풀스크립트
              </p>
            </div>
            <button class="preset-btn" onclick="copyL13ManimCode()" style="padding: 8px 18px; border-color: #fbbf24; color: #fbbf24;">
              📋 파이썬 코드 복사하기
            </button>
          </div>

          <pre id="l13ManimCodeBlock" style="background: #020617; padding: 20px; border-radius: 10px; border: 1px solid var(--border-color); font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: #e2e8f0; overflow-x: auto; max-height: 600px; line-height: 1.5;"><code>{escaped_manim}</code></pre>
        </div>
      </div>
    </div>

'''

    # Insert lecture13_html right before lecture12View
    if 'id="lecture13View"' not in html:
        idx_lec12 = html.find('id="lecture12View"')
        if idx_lec12 != -1:
            target_str = '    <!-- ============================================================== -->\n    <!-- SECTION FOR LECTURE 12'
            if target_str in html:
                html = html.replace(target_str, lecture13_html + target_str, 1)
                print("Inserted lecture13View before lecture12View.")
            else:
                html = html.replace('<div id="lecture12View"', lecture13_html + '<div id="lecture12View"', 1)
                print("Inserted lecture13View before lecture12View (fallback).")

    # 4. Add JavaScript for Lecture 13
    js_lecture13 = '''
    /* ========================================================= */
    /* LECTURE 13 (Y VS F(X): TERRITORY VS RESIDENT) LOGIC       */
    /* ========================================================= */
    function switchLec13Tab(tabId) {
      document.querySelectorAll('#lecture13View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture13View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l13SimTab') setTimeout(renderL13, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function copyL13ManimCode() {
      const code = document.getElementById('l13ManimCodeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('3Blue1Brown Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }

    const l13State = {
      mode: 'absY', // 'orig', 'absY', 'absFx', 'absX', 'absBoth'
      funcType: 'cubic', // 'cubic', 'quad', 'line', 'sin'
      showEquator: true,
      showGhost: true,
      showResidents: true
    };

    function setL13Mode(mode) {
      document.querySelectorAll('#lecture13View .preset-grid .preset-btn').forEach(b => b.classList.remove('active'));
      l13State.mode = mode;
      if (mode === 'orig') document.getElementById('l13ModeOrig').classList.add('active');
      else if (mode === 'absY') document.getElementById('l13ModeAbsY').classList.add('active');
      else if (mode === 'absFx') document.getElementById('l13ModeAbsFx').classList.add('active');
      else if (mode === 'absX') document.getElementById('l13ModeAbsX').classList.add('active');
      else if (mode === 'absBoth') document.getElementById('l13ModeAbsBoth').classList.add('active');

      updateL13InfoCard();
      renderL13();
    }

    function setL13Func(funcType) {
      document.querySelectorAll('#lecture13View #l13SimTab .control-card:nth-child(2) .preset-btn').forEach(b => b.classList.remove('active'));
      l13State.funcType = funcType;
      if (funcType === 'cubic') document.getElementById('l13FuncCubic').classList.add('active');
      else if (funcType === 'quad') document.getElementById('l13FuncQuad').classList.add('active');
      else if (funcType === 'line') document.getElementById('l13FuncLine').classList.add('active');
      else if (funcType === 'sin') document.getElementById('l13FuncSin').classList.add('active');

      renderL13();
    }

    function updateL13Toggles() {
      l13State.showEquator = document.getElementById('l13ToggleEquator').checked;
      l13State.showGhost = document.getElementById('l13ToggleGhost').checked;
      l13State.showResidents = document.getElementById('l13ToggleResidents').checked;
      renderL13();
    }

    function updateL13InfoCard() {
      const badge = document.getElementById('l13FuncBadge');
      const text = document.getElementById('l13LiveDefText');
      if (!badge || !text) return;

      if (l13State.mode === 'orig') {
        badge.innerText = '엄연한 함수 (1:1 또는 n:1 대응 ✔)';
        badge.style.background = '#10b981';
        text.innerHTML = `
          • <strong>오리지널 $y = f(x)$:</strong> 원본 함수 곡선 자체입니다.<br>
          • <strong>상태:</strong> 북반구($y \\ge 0$)와 남반구($y < 0$)를 자연스럽게 관통합니다.<br>
          • <strong>배티의 비유:</strong> 아무런 이동이나 영토 복사가 없는 평화로운 원형 상태.
        `;
      } else if (l13State.mode === 'absY') {
        badge.innerText = '함수 아님 (관계식 ❌)';
        badge.style.background = '#ef4444';
        text.innerHTML = `
          • <strong>식의 의미:</strong> $y \\ge 0 \\implies y = f(x)$, $y < 0 \\implies y = -f(x)$<br>
          • <strong>기하학적 조작:</strong> $x$축 위($y \\ge 0$) 영토를 남기고 $x$축 대칭 복사!<br>
          • <strong>배티의 비유:</strong> 남반구 영토에 북반구 지도를 데칼코마니로 복사 ($y$는 영토)<br>
          • <strong>수직선 판정:</strong> 하나의 $x$에 $y$가 2개 대응되므로 함수가 아닙니다.
        `;
      } else if (l13State.mode === 'absFx') {
        badge.innerText = '엄연한 함수 (치역 y ≥ 0 ✔)';
        badge.style.background = '#10b981';
        text.innerHTML = `
          • <strong>식의 의미:</strong> $f(x) \\ge 0 \\implies y = f(x)$, $f(x) < 0 \\implies y = -f(x)$<br>
          • <strong>기하학적 조작:</strong> $x$축 아래($f(x) < 0$) 사람만 $x$축 위로 꺾어 올림 (V-Fold)!<br>
          • <strong>배티의 비유:</strong> 남쪽에 살던 사람만 북반구로 강제 이주 ($f(x)$는 사람)<br>
          • <strong>수직선 판정:</strong> 하나의 $x$에 $y$가 1개 대응되므로 훌륭한 함수입니다.
        `;
      } else if (l13State.mode === 'absX') {
        badge.innerText = '엄연한 함수 (우함수 y축 대칭 ✔)';
        badge.style.background = '#10b981';
        text.innerHTML = `
          • <strong>식의 의미:</strong> $x \\ge 0 \\implies y = f(x)$, $x < 0 \\implies y = f(-x)$<br>
          • <strong>기하학적 조작:</strong> $y$축 오른쪽($x \\ge 0$, 동반구)만 남기고 $y$축 대칭 복사!<br>
          • <strong>성질:</strong> $f(-x) = f(x)$가 되어 완벽한 $y$축 대칭(우함수/짝함수)이 됩니다.
        `;
      } else if (l13State.mode === 'absBoth') {
        badge.innerText = '함수 아님 (4방향 대칭 관계식 ❌)';
        badge.style.background = '#ef4444';
        text.innerHTML = `
          • <strong>식의 의미:</strong> 제1사분면($x \\ge 0, y \\ge 0$)만 남기고 $x$축, $y$축, 원점 3중 복사!<br>
          • <strong>기하학적 형상:</strong> 마름모형 닫힌 대칭 도형을 형성합니다.<br>
          • <strong>배티의 비유:</strong> 동북반구(제1사분면)의 영토와 사람을 전 세계 4대륙에 복사!
        `;
      }

      if (window.renderMathInElement) {
        renderMathInElement(text, {delimiters: [{left: '$', right: '$', display: false}]});
      }
    }

    function evalL13Base(x) {
      if (l13State.funcType === 'cubic') {
        return 0.28 * (x + 2.3) * x * (x - 2.1);
      } else if (l13State.funcType === 'quad') {
        return 0.8 * (x * x - 3.2);
      } else if (l13State.funcType === 'line') {
        return 1.1 * x - 0.6;
      } else if (l13State.funcType === 'sin') {
        return 2.0 * Math.sin(x);
      }
      return 0;
    }

    function renderL13() {
      const canvas = document.getElementById('l13Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      // Coordinate mapping: X in [-3.8, 3.8], Y in [-3.4, 3.4]
      const margin = 45;
      const plotW = w - margin * 2;
      const plotH = h - margin * 2;
      const xMin = -3.8, xMax = 3.8;
      const yMin = -3.4, yMax = 3.4;

      function toX(x) { return margin + ((x - xMin) / (xMax - xMin)) * plotW; }
      function toY(y) { return (h - margin) - ((y - yMin) / (yMax - yMin)) * plotH; }

      // 1. Equator & Hemisphere Territorials
      if (l13State.showEquator) {
        // North Hemisphere (y >= 0): Soft warm yellow tint
        ctx.fillStyle = 'rgba(251, 191, 36, 0.08)';
        ctx.fillRect(toX(xMin), toY(yMax), toX(xMax) - toX(xMin), toY(0) - toY(yMax));

        // South Hemisphere (y < 0): Soft cool teal tint
        ctx.fillStyle = 'rgba(6, 182, 212, 0.08)';
        ctx.fillRect(toX(xMin), toY(0), toX(xMax) - toX(xMin), toY(yMin) - toY(0));

        // Labels for Northern & Southern Territorials
        ctx.fillStyle = 'rgba(251, 191, 36, 0.6)';
        ctx.font = 'bold 12px Inter, sans-serif';
        ctx.fillText('북반구 영토 (y ≥ 0)', toX(xMin) + 12, toY(2.8));

        ctx.fillStyle = 'rgba(6, 182, 212, 0.6)';
        ctx.fillText('남반구 영토 (y < 0)', toX(xMin) + 12, toY(-2.8));
      }

      // 2. Grid lines
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
      ctx.lineWidth = 1;
      for (let x = -3; x <= 3; x++) {
        ctx.beginPath();
        ctx.moveTo(toX(x), toY(yMin));
        ctx.lineTo(toX(x), toY(yMax));
        ctx.stroke();
      }
      for (let y = -3; y <= 3; y++) {
        ctx.beginPath();
        ctx.moveTo(toX(xMin), toY(y));
        ctx.lineTo(toX(xMax), toY(y));
        ctx.stroke();
      }

      // 3. Axes
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      // Equator X axis
      ctx.moveTo(toX(xMin), toY(0));
      ctx.lineTo(toX(xMax), toY(0));
      // Y axis
      ctx.moveTo(toX(0), toY(yMin));
      ctx.lineTo(toX(0), toY(yMax));
      ctx.stroke();

      // Equator Badge
      if (l13State.showEquator) {
        ctx.fillStyle = '#f59e0b';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillText('적도 (x축)', toX(xMax) - 60, toY(0) - 10);
      }

      // Axis labels
      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('x', toX(xMax) - 12, toY(0) + 18);
      ctx.fillText('y', toX(0) - 16, toY(yMax) + 12);
      ctx.fillText('O', toX(0) - 16, toY(0) + 16);

      // 4. Ghost Line of Original Curve
      if (l13State.showGhost && l13State.mode !== 'orig') {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        let started = false;
        for (let x = xMin; x <= xMax; x += 0.05) {
          const y = evalL13Base(x);
          if (y >= yMin - 1 && y <= yMax + 1) {
            if (!started) { ctx.moveTo(toX(x), toY(y)); started = true; }
            else ctx.lineTo(toX(x), toY(y));
          } else started = false;
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // 5. Draw Transformed Curves based on Mode
      const mode = l13State.mode;

      if (mode === 'orig') {
        // Original curve
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 3.0;
        ctx.beginPath();
        let started = false;
        for (let x = xMin; x <= xMax; x += 0.05) {
          const y = evalL13Base(x);
          if (y >= yMin && y <= yMax) {
            if (!started) { ctx.moveTo(toX(x), toY(y)); started = true; }
            else ctx.lineTo(toX(x), toY(y));
          } else started = false;
        }
        ctx.stroke();

      } else if (mode === 'absY') {
        // |y| = f(x): exists only where f(x) >= 0. Curves are y = f(x) and y = -f(x)
        // Upper branch (y >= 0)
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 3.0;
        ctx.beginPath();
        let started = false;
        for (let x = xMin; x <= xMax; x += 0.05) {
          const fVal = evalL13Base(x);
          if (fVal >= 0 && fVal <= yMax) {
            if (!started) { ctx.moveTo(toX(x), toY(fVal)); started = true; }
            else ctx.lineTo(toX(x), toY(fVal));
          } else started = false;
        }
        ctx.stroke();

        // Lower branch (reflected into y < 0)
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3.0;
        ctx.beginPath();
        started = false;
        for (let x = xMin; x <= xMax; x += 0.05) {
          const fVal = evalL13Base(x);
          if (fVal >= 0 && -fVal >= yMin) {
            if (!started) { ctx.moveTo(toX(x), toY(-fVal)); started = true; }
            else ctx.lineTo(toX(x), toY(-fVal));
          } else started = false;
        }
        ctx.stroke();

        // Label on canvas
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 14px Inter, sans-serif';
        ctx.fillText('|y| = f(x) : 상하 대칭 복사', toX(-1.5), toY(-2.5));

      } else if (mode === 'absFx') {
        // y = |f(x)|: curve is y = |f(x)|
        ctx.strokeStyle = '#ec4899';
        ctx.lineWidth = 3.0;
        ctx.beginPath();
        let started = false;
        for (let x = xMin; x <= xMax; x += 0.05) {
          const y = Math.abs(evalL13Base(x));
          if (y <= yMax) {
            if (!started) { ctx.moveTo(toX(x), toY(y)); started = true; }
            else ctx.lineTo(toX(x), toY(y));
          } else started = false;
        }
        ctx.stroke();

        // Folded indicators
        ctx.fillStyle = '#ec4899';
        ctx.font = 'bold 14px Inter, sans-serif';
        ctx.fillText('y = |f(x)| : 꺾어 올리기 (V-Fold)', toX(-1.5), toY(2.8));

      } else if (mode === 'absX') {
        // y = f(|x|): right side x >= 0 reflected to left
        ctx.strokeStyle = '#a78bfa';
        ctx.lineWidth = 3.0;
        ctx.beginPath();
        let started = false;
        for (let x = xMin; x <= xMax; x += 0.05) {
          const y = evalL13Base(Math.abs(x));
          if (y >= yMin && y <= yMax) {
            if (!started) { ctx.moveTo(toX(x), toY(y)); started = true; }
            else ctx.lineTo(toX(x), toY(y));
          } else started = false;
        }
        ctx.stroke();

        ctx.fillStyle = '#a78bfa';
        ctx.font = 'bold 14px Inter, sans-serif';
        ctx.fillText('y = f(|x|) : 좌우 대칭 (우함수)', toX(-1.5), toY(2.8));

      } else if (mode === 'absBoth') {
        // |y| = f(|x|): takes quadrant 1 (x >= 0, f(x) >= 0) and reflects across x and y
        ctx.strokeStyle = '#34d399';
        ctx.lineWidth = 3.0;

        function drawBothBranches(signX) {
          // upper
          ctx.beginPath();
          let started = false;
          for (let x = 0; x <= xMax; x += 0.05) {
            const fVal = evalL13Base(x);
            if (fVal >= 0 && fVal <= yMax) {
              if (!started) { ctx.moveTo(toX(signX * x), toY(fVal)); started = true; }
              else ctx.lineTo(toX(signX * x), toY(fVal));
            } else started = false;
          }
          ctx.stroke();

          // lower
          ctx.beginPath();
          started = false;
          for (let x = 0; x <= xMax; x += 0.05) {
            const fVal = evalL13Base(x);
            if (fVal >= 0 && -fVal >= yMin) {
              if (!started) { ctx.moveTo(toX(signX * x), toY(-fVal)); started = true; }
              else ctx.lineTo(toX(signX * x), toY(-fVal));
            } else started = false;
          }
          ctx.stroke();
        }

        drawBothBranches(1);
        drawBothBranches(-1);

        ctx.fillStyle = '#34d399';
        ctx.font = 'bold 14px Inter, sans-serif';
        ctx.fillText('|y| = f(|x|) : 4방향 3중 복사', toX(-1.5), toY(-2.5));
      }

      // 6. Dynamic Resident Dots (People on graph)
      if (l13State.showResidents) {
        const sampleXs = [-1.8, -0.9, 0.0, 1.1, 2.0];
        sampleXs.forEach(sx => {
          let origY = evalL13Base(sx);
          if (origY >= yMin && origY <= yMax) {
            if (mode === 'orig') {
              drawDot(sx, origY, '#fbbf24', 'P');
            } else if (mode === 'absY' && origY >= 0) {
              drawDot(sx, origY, '#fbbf24', 'P_N');
              drawDot(sx, -origY, '#38bdf8', 'P_S');
            } else if (mode === 'absFx') {
              drawDot(sx, Math.abs(origY), '#ec4899', 'P\'');
            }
          }
        });
      }

      function drawDot(x, y, color, tag) {
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(toX(x), toY(y), 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1.2;
        ctx.stroke();
      }
    }
'''

    # Insert js_lecture13 before switchLec12Tab
    if 'function switchLec13Tab' not in html:
        idx_js12 = html.find('/* LECTURE 12 (RECTANGULAR HYPERBOLA S = T) LOGIC')
        if idx_js12 != -1:
            html = html[:idx_js12] + js_lecture13 + '\n' + html[idx_js12:]
            print("Inserted Lecture 13 JavaScript before Lecture 12 JS.")
        else:
            idx_script = html.rfind('</script>')
            html = html[:idx_script] + js_lecture13 + '\n' + html[idx_script:]
            print("Inserted Lecture 13 JavaScript before closing script tag.")

    # 5. Update setLecture(num) loop and handlers
    # Change for (let i = 1; i <= 12; i++) to for (let i = 1; i <= 13; i++)
    old_loop = 'for (let i = 1; i <= 12; i++) {'
    new_loop = 'for (let i = 1; i <= 13; i++) {'
    if old_loop in html:
        html = html.replace(old_loop, new_loop)
        print("Updated setLecture loop to 13.")

    # Add num === 13 handler
    old_handler = 'if (num === 12) setTimeout(renderL12, 50);'
    new_handler = 'if (num === 13) setTimeout(renderL13, 50);\n      else if (num === 12) setTimeout(renderL12, 50);'
    if old_handler in html and 'if (num === 13) setTimeout(renderL13, 50);' not in html:
        html = html.replace(old_handler, new_handler)
        print("Added num === 13 render handler to setLecture.")

    # 6. Update window load handler to default to lecture 13
    old_onload = """window.addEventListener('load', () => {
      updateL12Sliders();
      renderL12();
    });"""
    new_onload = """window.addEventListener('load', () => {
      renderL13();
    });"""
    if old_onload in html:
        html = html.replace(old_onload, new_onload)
        print("Updated window load handler to initialize Lecture 13.")

    # Write back to index.html
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with Lecture 13!")

if __name__ == '__main__':
    main()
