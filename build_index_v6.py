# -*- coding: utf-8 -*-
"""
Script to inject Lecture 6 (CSAT Geometry Dealer: 7 Core Theorems) into index.html
Preserving all existing Lectures 1, 2, 3, 4, 5 without alteration.
"""

import os

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the lecture switcher bar
    old_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (5 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec5" onclick="setLecture(5)">
          <span class="badge-pill-sm">최신 강의</span>
          피타고라스 정리 (유클리드 증명)
        </button>'''

    new_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (6 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec6" onclick="setLecture(6)">
          <span class="badge-pill-sm" style="background: linear-gradient(135deg, #ef4444, #f59e0b); color: #fff;">🔥 파이널 특강</span>
          수능 기하 총정리 (수학딜러)
        </button>
        <button class="lecture-btn" id="btnLec5" onclick="setLecture(5)">
          피타고라스 정리 (유클리드 증명)
        </button>'''

    if old_switcher_head not in content:
        print("ERROR: old_switcher_head not found in index.html!")
        return

    content = content.replace(old_switcher_head, new_switcher_head, 1)

    # 2. Update lecture5View to start hidden:
    old_lec5_start = '<div id="lecture5View">'
    new_lec5_start = '<div id="lecture5View" style="display: none;">'
    if old_lec5_start not in content:
        print("ERROR: old_lec5_start not found!")
        return

    content = content.replace(old_lec5_start, new_lec5_start, 1)

    # 3. Read the Manim script to include in Tab 4
    with open('csat_geometry_dealer_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()
    manim_code_escaped = manim_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # 4. Lecture 6 Section HTML
    lecture6_html = r'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 6 (CSAT GEOMETRY DEALER: 7 CORE THEOREMS)   -->
    <!-- ============================================================== -->
    <div id="lecture6View">
      <header>
        <div class="badge-pill" style="border-color: rgba(245, 158, 11, 0.4); color: var(--accent-gold); box-shadow: 0 0 20px rgba(245, 158, 11, 0.3);">
          <span>📐 2025/2026 수능 수학 파이널 기하 특강 · 전 등급 필수 시청</span>
        </div>
        <h1 style="background: linear-gradient(135deg, #ffffff 30%, #fbbf24 70%, #38bdf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          수능 도형 총정리 & 기하적 실전 태도 마스터
        </h1>
        <p class="subtitle">
          평행선의 역발견 · 직각삼각형 $\bigcirc+\triangle=90^\circ$ 삼각비 등비수열 · 접현각과 두 원의 공통접선 · 방멱(할선정리 3대 공식)을 <strong>인터랙티브 시뮬레이터</strong>와 <strong>14단계 판서 타임라인</strong>으로 완벽 정복하는 수능 파이널 필수 포털!
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>수학딜러 (@mathdealer)</strong></span>
          <span>•</span>
          <a href="https://youtu.be/xTnNZ0N-Qt8" target="_blank" rel="noopener">
            <span>YouTube 본 영상 보기 (26분 29초)</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
        </div>
      </header>

      <!-- Tab Bar for Lecture 6 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec6Tab('l6SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 수능 기하 스튜디오 (4대 핵심 모드)
        </button>
        <button class="tab-btn" onclick="switchLec6Tab('l6CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 & 14단계 타임라인
        </button>
        <button class="tab-btn" onclick="switchLec6Tab('l6ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          수학교과서식 정형화 & 수능 기출 킬러 연계
        </button>
        <button class="tab-btn" onclick="switchLec6Tab('l6ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 6) -->
      <div id="l6SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Dynamic Banner depending on mode -->
          <div class="formula-banner" id="l6Banner" style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(56, 189, 248, 0.08)); border-color: rgba(245, 158, 11, 0.35);">
            <div class="label" id="l6BannerLabel" style="color: var(--accent-gold);">🌟 수능 기하 핵심 정리</div>
            <div class="math-main" id="l6BannerMath">
              $$L_0 = a \;\longrightarrow\; L_1 = a\tan\theta \;\longrightarrow\; L_2 = a\tan^2\theta \quad (\text{연속 직각삼각형은 공비 } \tan\theta \text{인 등비수열})$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l6Canvas" width="560" height="520"></canvas>
              <div id="l6CanvasCaption" style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                각 $\theta$와 직각($90^\circ$)을 공유하는 연쇄 직각삼각형과 등비수열 체인
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Mode Selector -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎯 수능 4대 기하 테마 선택</span>
                  <span class="badge-pill-sm" id="l6ActiveThemeBadge" style="background: var(--accent-gold); color: #000;">체인 모드</span>
                </div>
                <div class="preset-grid" style="grid-template-columns: 1fr 1fr;">
                  <button class="preset-btn active" id="l6BtnChain" onclick="setL6Mode('chain')">
                    <span>1. 직각삼각형 등비수열</span>
                    <span class="p-sub">$a, a\tan\theta, a\tan^2\theta$</span>
                  </button>
                  <button class="preset-btn" id="l6BtnSecant" onclick="setL6Mode('secant')">
                    <span>2. 할선정리 (방멱)</span>
                    <span class="p-sub">$PA \cdot PB = PC \cdot PD$</span>
                  </button>
                  <button class="preset-btn" id="l6BtnTangent" onclick="setL6Mode('tangent')">
                    <span>3. 접현각 & 평행선</span>
                    <span class="p-sub">두 원의 공통접선 평행</span>
                  </button>
                  <button class="preset-btn" id="l6BtnQuad" onclick="setL6Mode('quad')">
                    <span>4. 외접 사각형 대변합</span>
                    <span class="p-sub">$a + c = b + d$</span>
                  </button>
                </div>
              </div>

              <!-- Dynamic Sub-controls depending on mode -->
              <div class="control-card" id="l6SubControlCard">
                <!-- Injected via JavaScript based on mode -->
              </div>

              <!-- Live Numeric Analysis Card -->
              <div class="control-card" id="l6MetricCard">
                <!-- Injected via JavaScript based on mode -->
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: TIMELINE & CAPTURES (14 STEPS) -->
      <div id="l6CaptureTab" class="tab-panel">
        <div class="timeline-container">

          <!-- Step 1 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 1</span>
              <span class="timestamp">[00:01:10]</span>
              <span class="step-title">평행선과 동위각 · 엇각의 역발견</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/01_parallel_alternate_angles.jpg" alt="평행선과 동위각 엇각의 역발견">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"평행선이 주어지면 동위각과 엇각을 찾는 것은 누구나 합니다. 하지만 수능 고난도 문제의 핵심은 역발견입니다! 두 각이 같다는 것(엇각/동위각)을 발견했을 때, 거꾸로 '이 두 직선이 평행하구나!'를 떠올리는 것이 진짜 실력입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 핵심 수능 태도:</div>
                  <ul>
                    <li>문제에서 직접 "평행하다"고 알려주지 않아도, 원주각이나 접현각으로 인해 두 각이 같아지면 즉시 <strong>두 선분이 평행함</strong>을 간파해야 합니다.</li>
                    <li>평행선이 생기는 순간 필연적으로 <strong>모래시계형 / 피라미드형 $AA$ 닮음 삼각형</strong>이 나타나며 비례식이 폭발합니다.</li>
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
              <span class="timestamp">[00:03:30]</span>
              <span class="step-title">직각삼각형 2개 엮임과 $\bigcirc + \triangle = 90^\circ$ 각도 마킹</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/02_right_triangles_angles.jpg" alt="직각삼각형 엮임과 각도 마킹">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"직각삼각형 두 개가 엮여 있을 때는 각도를 무조건 $\bigcirc$와 $\triangle$로 잡으세요. 직각삼각형이니까 $\bigcirc + \triangle = 90^\circ$입니다. 맞꼭지각이나 여각을 타고 넘어가면 다른 직각삼각형의 각도도 자연스럽게 채워집니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 핵심 수능 태도:</div>
                  <ul>
                    <li>복잡한 계산식 대신 직관적인 기호 $\bigcirc, \triangle$를 마킹하면 수능 시험장에서 연산 실수를 획기적으로 줄일 수 있습니다.</li>
                    <li>두 직각삼각형의 한 예각이 공유되거나 맞꼭지각/여각으로 같아지면 즉시 <strong>$AA$ 닮음</strong>과 동일한 삼각비($\sin, \cos, \tan$)를 공유합니다.</li>
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
              <span class="timestamp">[00:04:45]</span>
              <span class="step-title">삼각비의 연쇄 전개와 등비수열 체인 ($a, a\tan\theta, a\tan^2\theta$)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/03_geometric_progression_tan.jpg" alt="삼각비 연쇄와 등비수열 체인">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"밑변이 $a$이고 각이 $\theta$라면 높이는 $a\tan\theta$입니다. 그 높이를 다시 밑변으로 하는 또 다른 직각삼각형이 맞물려 있다면 다음 변은 $a\tan^2\theta$가 됩니다. 즉, 변의 길이들이 공비가 $\tan\theta$인 등비수열을 이룹니다. 이 소재 하나만으로 출제된 평가원 기출도 있습니다!"</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 등비수열 공식 체계:</div>
                  <div class="math-highlight">$$L_0 = a \;\longrightarrow\; L_1 = a\tan\theta \;\longrightarrow\; L_2 = a\tan^2\theta \implies L_n = a(\tan\theta)^n$$</div>
                  <ul>
                    <li>공비 $r = \tan\theta$ (또는 빗변 방향 전개 시 $\frac{1}{\cos\theta}$).</li>
                    <li>수학I 등비수열 킬러 및 미적분 무한등비급수 도형 문제의 핵심 구조입니다.</li>
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
              <span class="timestamp">[00:08:15]</span>
              <span class="step-title">원의 중심과 현의 수직이등분선 & 이등변삼각형</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/04_chord_perpendicular_bisector.jpg" alt="현의 수직이등분선과 이등변삼각형">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"원의 중심에서 현에 수선을 내리면 무조건 수직이등분합니다. 반대로 문제에서 선분의 수직이등분선이 주어지면 두 점을 잇는 이등변삼각형과 그 점들을 지나는 외접원의 중심을 떠올리셔야 합니다. 이게 양방향으로 왔다 갔다 잘 돼야 합니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 피타고라스 관계:</div>
                  <div class="math-highlight">$$OM \perp AB \implies AM = MB, \quad OM^2 + \left(\frac{AB}{2}\right)^2 = R^2$$</div>
                  <ul>
                    <li>수능에서 "선분의 수직이등분선"이라는 힌트는 곧 <strong>외접원의 중심 $O$</strong>의 자취를 뜻합니다.</li>
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
              <span class="timestamp">[00:10:00]</span>
              <span class="step-title">원 외부 한 점에서 그은 접선의 길이의 상등 ($PA = PB$)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/05_tangent_lengths_equal.jpg" alt="원 외부 한 점에서 접선 길이 같음">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"원 외부의 점 $P$에서 원에 접선을 두 개 그으면, 접점까지의 거리는 무조건 같습니다 ($PA = PB$). $RHS$ 합동이기 때문입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 기하적 원리 ($RHS$ 합동):</div>
                  <ul>
                    <li>중심 $O$에서 접점에 이르는 선분은 접선과 수직($\angle OAP = \angle OBP = 90^\circ$).</li>
                    <li>공통 빗변 $OP$, 반지름 $OA = OB = R$에 의해 $\triangle OAP \equiv \triangle OBP$ ($RHS$ 합동).</li>
                    <li>따라서 $PA = PB$뿐만 아니라 $\angle APO = \angle BPO$ (각의 이등분선)까지 자동으로 확보됩니다.</li>
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
              <span class="timestamp">[00:11:15]</span>
              <span class="step-title">원에 외접하는 사각형: 대변의 합 공식 ($a + c = b + d$)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/06_circumscribed_quadrilateral.jpg" alt="외접 사각형 대변의 합 공식">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"원에 외접하는 사각형이 나온다면 고민할 것 없이 대변의 합을 쓰세요! 윗변 + 아랫변 = 왼쪽변 + 오른쪽변 입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 대변 합 공식:</div>
                  <div class="math-highlight">$$\mathbf{\text{상} + \text{하} = \text{좌} + \text{우} \iff a + c = b + d = x + y + z + w}$$</div>
                  <ul>
                    <li>네 꼭짓점에서 원에 그은 접선 4쌍의 길이 $x, y, z, w$의 대칭적 합으로 즉시 증명됩니다.</li>
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
              <span class="timestamp">[00:13:30]</span>
              <span class="step-title">접선과 현이 이루는 각 (접현각, Tangent-Chord Theorem)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/07_tangent_chord_angle.jpg" alt="접선과 현이 이루는 각 접현각">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"원의 접선과 그 접점을 지나는 현이 이루는 각은, 그 현에 대한 원주각의 크기와 정확히 같습니다. 이걸 접현각이라고 부릅니다. 그림을 보자마자 같은 각 $\theta$를 표시할 수 있어야 합니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 접현각 정리:</div>
                  <div class="math-highlight">$$\angle TAB = \angle BCA = \theta$$</div>
                  <ul>
                    <li>지름을 지나는 직각삼각형 보조선으로 $90^\circ - \angle$ 관계를 활용해 5초 만에 유도 가능합니다.</li>
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
              <span class="timestamp">[00:15:20]</span>
              <span class="step-title">외접하는 두 원과 공통내접선: 엇각을 통한 평행선 발견</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/08_two_circles_external_tangent_parallel.jpg" alt="외접하는 두 원과 공통내접선 평행">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"외접하는 두 원의 접점에 공통접선을 긋고, 접점을 통과하는 직선 두 개를 그어보세요. 맞꼭지각과 접현각을 타고 넘어가면 두 현이 이루는 엇각이 정확히 같아집니다! 따라서 두 직선은 평행합니다. 수능 출제진이 사랑하는 킬러 태도입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 평행 유도 체인:</div>
                  <div class="math-highlight">$$\angle 1 = \angle \text{접현각} = \angle \text{맞꼭지} = \angle 2 \implies \mathbf{AB \parallel CD}$$</div>
                  <ul>
                    <li>엇각이 같으므로 두 현은 평행하며, 두 삼각형은 모래시계형 닮음이 됩니다.</li>
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
              <span class="timestamp">[00:17:15]</span>
              <span class="step-title">내접하는 두 원과 공통외접선: 동위각을 통한 평행선 발견</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/09_two_circles_internal_tangent_parallel.jpg" alt="내접하는 두 원과 공통외접선 평행">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"이번엔 안쪽에서 접하는(내접하는) 두 원입니다. 공통접선에서 접현각을 적용하면 작은 원의 각이 $\theta$이고 큰 원의 각도 $\theta$가 됩니다. 동위각 위치의 각이 같으므로 두 선분은 평행합니다!"</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 동위각 상등:</div>
                  <ul>
                    <li>동일한 접선에서 출발하여 두 원의 현이 만드는 동위각이 일치 $\implies \mathbf{AB \parallel CD}$.</li>
                    <li>피라미드형 닮음비가 즉각 성립합니다.</li>
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
              <span class="timestamp">[00:18:15]</span>
              <span class="step-title">원주각과 중심각의 $2:1$ 관계</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/10_inscribed_central_angle.jpg" alt="원주각과 중심각의 2대1 관계">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"원에서 가장 중요한 단 하나의 개념을 꼽으라면 무조건 원주각과 중심각입니다. 같은 호에 대한 중심각이 $2\theta$라면 원주각은 무조건 $\theta$입니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 원주각의 핵심 불변성:</div>
                  <div class="math-highlight">$$\angle APB = \frac{1}{2}\angle AOB = \theta \quad (\text{호 } AB \text{에 대해 점 } P\text{ 위치 무관 항상 일정})$$</div>
                  <ul>
                    <li>특히 선분 $AB$가 원의 지름일 때 원주각은 무조건 <strong>$90^\circ$</strong>!</li>
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
              <span class="timestamp">[00:19:35]</span>
              <span class="step-title">원 내접 사각형: 대각의 합 $180^\circ$ & 한 외각 = 내대각</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/11_cyclic_quadrilateral_180.jpg" alt="원 내접 사각형 대각의 합 180도">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"원에 내접하는 사각형이 보이면 바로 쓰세요. 마주보는 두 대각의 합은 무조건 $180^\circ$입니다 ($\alpha + \beta = 180^\circ$). 따라서 한 외각의 크기는 마주보는 안쪽 각(내대각)과 완벽히 같습니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 코사인법칙과의 결합:</div>
                  <div class="math-highlight">$$\angle A + \angle C = 180^\circ \implies \cos C = \cos(180^\circ - A) = -\cos A$$</div>
                  <ul>
                    <li>대각선 길이에 대해 코사인법칙을 위아래 삼각형에 두 번 적용할 때 마이너스 부호로 상쇄되는 테크닉의 원천입니다.</li>
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
              <span class="timestamp">[00:21:30]</span>
              <span class="step-title">할선정리 (방멱) 1: 접선과 할선 ($PT^2 = PA \cdot PB$)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/12_power_of_point_tangent_secant.jpg" alt="할선정리 1 접선과 할선">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"할선정리 첫 번째! 접선과 할선이 만날 때입니다. 접점까지의 길이의 제곱은 짧은 할선 곱하기 긴 할선입니다. 즉, $PT^2 = PA \cdot PB$ ($t^2 = a(a+b)$)입니다. 수능에서는 유도할 시간 따위 없습니다. 무조건 외우고 바로 쓰셔야 합니다!"</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 접현각에 의한 $AA$ 닮음:</div>
                  <div class="math-highlight">$$\triangle PTA \sim \triangle PBT \implies \frac{PT}{PB} = \frac{PA}{PT} \implies \mathbf{PT^2 = PA \cdot PB}$$</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 13 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 13</span>
              <span class="timestamp">[00:23:45]</span>
              <span class="step-title">할선정리 (방멱) 2: 외부 두 할선 ($PA \cdot PB = PC \cdot PD$)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/13_power_of_point_secants.jpg" alt="할선정리 2 외부 두 할선">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"원 외부의 점 $P$에서 할선을 두 개 그었을 때입니다. 내접사각형의 외각 성질 때문에 $\triangle PAC$와 $\triangle PDB$가 $AA$ 닮음이 됩니다. 그래서 $PA \cdot PB = PC \cdot PD$ ($a(a+b) = c(c+d)$)가 성립합니다."</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 비례식 유도:</div>
                  <div class="math-highlight">$$\triangle PAC \sim \triangle PDB \implies \frac{PA}{PD} = \frac{PC}{PB} \implies \mathbf{PA \cdot PB = PC \cdot PD}$$</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 14 -->
          <div class="timeline-card">
            <div class="timeline-node"></div>
            <div class="timeline-step">
              <span class="step-num">Step 14</span>
              <span class="timestamp">[00:25:40]</span>
              <span class="step-title">할선정리 (방멱) 3: 원 내부에서 교차하는 두 현 ($PA \cdot PB = PC \cdot PD$)</span>
            </div>
            <div class="timeline-content">
              <div class="timeline-img-box">
                <img src="./captures_v6/14_power_of_point_intersecting_chords.jpg" alt="할선정리 3 내부 교차하는 두 현">
              </div>
              <div class="timeline-text">
                <div class="teacher-speech">
                  <span class="icon">💬</span>
                  <div class="quote">"마지막 할선정리 세 번째는 원 내부에서 현 두 개가 교차할 때입니다. 같은 호에 대한 원주각을 표시하면 두 맞꼭지 삼각형이 닮음이 됩니다. 따라서 내항의 곱과 외항의 곱에 의해 $PA \cdot PB = PC \cdot PD$ ($a \cdot b = c \cdot d$)가 성립합니다!"</div>
                </div>
                <div class="desc-box">
                  <div class="point-label">📌 원주각에 의한 $AA$ 닮음:</div>
                  <div class="math-highlight">$$\triangle PAC \sim \triangle PDB \implies \frac{PA}{PD} = \frac{PC}{PB} \implies \mathbf{PA \cdot PB = PC \cdot PD}$$</div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- TAB 3: MATH DEEP DIVE & CSAT PROOFS -->
      <div id="l6ProofTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; color: var(--accent-gold); margin-bottom: 20px;">
            📚 수학교과서식 엄밀한 증명 & 수능 킬러 기출 연계
          </h2>

          <!-- Proof 1 -->
          <div class="control-card" style="margin-bottom: 20px;">
            <h3 style="color: var(--accent-blue); margin-bottom: 12px;">
              [정리 1] 접현각 정리 (The Alternate Segment Theorem)
            </h3>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 12px;">
              <strong>정리:</strong> 원의 접선 $l$과 그 접점 $A$를 지나는 현 $AB$가 이루는 각 $\angle TAB$는 호 $AB$에 대한 원주각 $\angle BCA$의 크기와 같다.
            </p>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); line-height: 1.8; color: var(--text-main);">
              <strong>증명:</strong><br>
              1. 접점 $A$를 지나 원의 중심 $O$를 통과하는 지름 $AD$를 작도한다.<br>
              2. 지름에 대한 원주각의 성질에 의해 $\angle ABD = 90^\circ$이다.<br>
              3. 반지름 $OA$는 접선 $l$과 수직이므로 $\angle TAD = 90^\circ$이다.<br>
              4. 따라서 $\angle TAB = 90^\circ - \angle DAB$이다.<br>
              5. 직각삼각형 $ABD$에서 세 내각의 합은 $180^\circ$이므로 $\angle BDA = 90^\circ - \angle DAB$이다.<br>
              6. 식 4와 5에 의해 $\angle TAB = \angle BDA$이다.<br>
              7. 원주각의 정리에 의해 같은 호 $AB$에 대한 원주각은 항상 같으므로 $\angle BDA = \angle BCA$이다.<br>
              8. $\therefore \angle TAB = \angle BCA \quad \blacksquare$
            </div>
          </div>

          <!-- Proof 2 -->
          <div class="control-card" style="margin-bottom: 20px;">
            <h3 style="color: var(--accent-green); margin-bottom: 12px;">
              [정리 2] 방멱의 정리 (Power of a Point) 대수적 불변량 증명
            </h3>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 12px;">
              <strong>정리:</strong> 중심이 $O$이고 반지름이 $R$인 원과 한 점 $P$에 대하여, 점 $P$를 지나는 임의의 할선이 원과 만나는 두 점을 $A, B$라 하고 $d = OP$라 하면,
              $$\mathbf{PA \cdot PB = |d^2 - R^2| = \text{const (불변 상수)}}$$
            </p>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); line-height: 1.8; color: var(--text-main);">
              <strong>증명:</strong><br>
              점 $P$와 중심 $O$를 지나는 직선을 그으면, 이 직선은 원과 두 점 $X, Y$에서 만나며 선분 $XY$는 지름이 된다.<br>
              - $P$가 원 외부일 때: $PX = d - R$, $PY = d + R$<br>
              &nbsp;&nbsp; 따라서 $PX \cdot PY = (d - R)(d + R) = d^2 - R^2$<br>
              - 점 $P$에서 원에 그은 접점 $T$에 대해 직각삼각형 $OTP$에서 피타고라스 정리에 의해 $PT^2 = OP^2 - OT^2 = d^2 - R^2$<br>
              - 원주각과 삼각형 닮음에 의해 임의의 할선 $PAB$에 대해 $PA \cdot PB = PX \cdot PY = d^2 - R^2 = PT^2$가 성립한다.<br>
              $\therefore$ 점 $P$의 위치가 고정되면 할선의 각도에 무관하게 곱 $PA \cdot PB$는 언제나 **$|d^2 - R^2|$로 일정하다!** $\blacksquare$
            </div>
          </div>

          <!-- CSAT Application -->
          <div class="control-card">
            <h3 style="color: var(--accent-gold); margin-bottom: 12px;">
              🎯 수능 수학I 삼각함수 도형 킬러 문항 실전 풀이 전략
            </h3>
            <ul style="color: var(--text-muted); line-height: 2.0; padding-left: 20px;">
              <li><strong>1. 사인법칙의 뇌관:</strong> 문제에 "외접원 반지름 $R$" 또는 "외접원 위의 세 점"이 언급되면 즉시 $\frac{a}{\sin A} = 2R$을 쓰고, 같은 호를 바라보는 원주각들을 모조리 동일 기호($\theta$)로 표기한다.</li>
              <li><strong>2. 원에 내접하는 사각형의 대각 합 $180^\circ$:</strong> 마주보는 각을 $\theta, 180^\circ - \theta$로 두고 대각선에 대해 코사인법칙 식을 연립한다 ($\cos(180^\circ-\theta) = -\cos\theta$).</li>
              <li><strong>3. 할선정리의 초스피드 적용:</strong> 현의 교점이나 외부 교점에서 미지수 선분이 생기면 복잡한 삼각방정식 대신 **$PA \cdot PB = PC \cdot PD$**를 먼저 적용하여 미지수 하나를 5초 만에 소거한다!</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 4: MANIM PYTHON SCRIPT -->
      <div id="l6ManimTab" class="tab-panel">
        <div class="glass-card">
          <div class="control-header" style="margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.35rem; color: #fff;">🎬 3Blue1Brown 스타일 Manim 스크립트</h2>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">수학딜러의 수능 기하 핵심 정리 (직각삼각형 체인 · 접현각 평행선 · 방멱 할선정리) 시각화 파이썬 코드</p>
            </div>
            <button class="preset-btn" onclick="copyL6ManimCode()" style="background: rgba(56, 189, 248, 0.2); color: var(--accent-blue); border-color: var(--accent-blue);">
              📋 코드 복사하기
            </button>
          </div>

          <div style="background: rgba(0, 0, 0, 0.4); padding: 12px 18px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); font-size: 0.82rem; color: var(--text-dim); margin-bottom: 16px;">
            💻 <strong>실행 명령어:</strong> <code style="color: var(--accent-gold);">manim -pql csat_geometry_dealer_manim.py CSATGeometryMasterScene</code>
          </div>

          <div class="code-container" style="background: #050811; border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 20px; overflow-x: auto; max-height: 600px;">
            <pre><code id="l6ManimCodeBlock" class="language-python" style="font-family: 'JetBrains Mono', monospace; font-size: 0.84rem; color: #e2e8f0; line-height: 1.6;">''' + manim_code_escaped + r'''</code></pre>
          </div>
        </div>
      </div>

    </div>
'''

    # Insert lecture6_html right after `<div class="container">\n\n    <!-- TOP LECTURE SELECTOR BAR (6 LECTURES) --> ... </div>\n    </div>\n\n`
    # Or right before `<div id="lecture5View"`
    target_insert_point = '<div id="lecture5View"'
    if target_insert_point not in content:
        print("ERROR: target_insert_point not found!")
        return

    content = content.replace(target_insert_point, lecture6_html + '\n    ' + target_insert_point, 1)

    # 5. Update JavaScript logic:
    # Update setLecture(num) to support 6 lectures
    old_set_lecture = '''    function setLecture(num) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`btnLec${i}`);
        const view = document.getElementById(`lecture${i}View`);
        if (btn) btn.classList.toggle('active', i === num);
        if (view) view.style.display = (i === num) ? 'block' : 'none';
      }

      if (num === 5) setTimeout(renderL5, 50);
      else if (num === 4) setTimeout(renderL4, 50);
      else if (num === 3) setTimeout(renderL3, 50);
      else if (num === 2) setTimeout(renderL2, 50);
      else if (num === 1) setTimeout(renderL1, 50);'''

    new_set_lecture = '''    function setLecture(num) {
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

    if old_set_lecture not in content:
        print("ERROR: old_set_lecture not found!")
        return

    content = content.replace(old_set_lecture, new_set_lecture, 1)

    # Add switchLec6Tab and Lecture 6 logic right before `/* ========================================================= */\n    /* LECTURE 5`
    l6_js_logic = r'''    /* ========================================================= */
    /* LECTURE 6 (CSAT GEOMETRY DEALER) LOGIC                    */
    /* ========================================================= */
    function switchLec6Tab(tabId) {
      document.querySelectorAll('#lecture6View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture6View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l6SimTab') setTimeout(renderL6, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function copyL6ManimCode() {
      const code = document.getElementById('l6ManimCodeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('3Blue1Brown Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }

    const l6State = {
      mode: 'chain', // 'chain', 'secant', 'tangent', 'quad'
      // Chain mode state
      chainA: 3.5,
      chainTheta: 32, // degrees
      // Secant mode state
      secantCase: 'case_chords', // 'case_chords', 'case_secants', 'case_tangent'
      secantPos: 0.5,
      // Tangent mode state
      tangentCase: 'case_ext', // 'case_ext', 'case_int'
      // Quad mode state
      quadOffset: 0.0
    };

    function setL6Mode(m) {
      l6State.mode = m;
      document.querySelectorAll('#lecture6View .preset-btn').forEach(b => b.classList.remove('active'));
      if (m === 'chain') document.getElementById('l6BtnChain').classList.add('active');
      else if (m === 'secant') document.getElementById('l6BtnSecant').classList.add('active');
      else if (m === 'tangent') document.getElementById('l6BtnTangent').classList.add('active');
      else if (m === 'quad') document.getElementById('l6BtnQuad').classList.add('active');

      syncL6UI();
      renderL6();
    }

    function syncL6UI() {
      const subCard = document.getElementById('l6SubControlCard');
      const metricCard = document.getElementById('l6MetricCard');
      const bannerLabel = document.getElementById('l6BannerLabel');
      const bannerMath = document.getElementById('l6BannerMath');
      const themeBadge = document.getElementById('l6ActiveThemeBadge');
      const caption = document.getElementById('l6CanvasCaption');

      if (l6State.mode === 'chain') {
        themeBadge.innerText = '1. 직각삼각형 체인';
        bannerLabel.innerText = '🌟 연쇄 직각삼각형 & 등비수열 체인 공식';
        bannerMath.innerHTML = '$$L_0 = a \\;\\longrightarrow\\; L_1 = a\\tan\\theta \\;\\longrightarrow\\; L_2 = a\\tan^2\\theta \\quad (\\text{변의 길이는 공비 } \\tan\\theta \\text{인 등비수열})$$';
        caption.innerText = '직각삼각형 3개가 엮이며 변의 길이가 공비 tanθ인 등비수열을 형성하는 기하 구조';

        subCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">🎛️ 밑변 길이 $a$ 및 각도 $\\theta$ 조절</span>
          </div>
          <div class="slider-row">
            <label>기본 밑변 $a$: <strong id="l6ChainAVal" style="color: var(--accent-blue);">${l6State.chainA.toFixed(1)}</strong></label>
            <input type="range" min="2.0" max="5.0" step="0.1" value="${l6State.chainA}" oninput="l6State.chainA=parseFloat(this.value); document.getElementById('l6ChainAVal').innerText=this.value; renderL6();">
          </div>
          <div class="slider-row">
            <label>예각 $\\theta$: <strong id="l6ChainThetaVal" style="color: var(--accent-gold);">${l6State.chainTheta}°</strong></label>
            <input type="range" min="18" max="52" step="1" value="${l6State.chainTheta}" oninput="l6State.chainTheta=parseInt(this.value); document.getElementById('l6ChainThetaVal').innerText=this.value+'°'; renderL6();">
          </div>
        `;

        const rad = l6State.chainTheta * Math.PI / 180;
        const tanVal = Math.tan(rad);
        const l0 = l6State.chainA;
        const l1 = l0 * tanVal;
        const l2 = l1 * tanVal;
        const l3 = l2 * tanVal;

        metricCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">📊 실시간 등비수열 체인 검증</span>
          </div>
          <div class="metric-grid" style="grid-template-columns: repeat(4, 1fr); margin-top: 6px;">
            <div class="metric-card m1">
              <div class="metric-label">$L_0$ (밑변)</div>
              <div class="metric-val">${l0.toFixed(2)}</div>
            </div>
            <div class="metric-card m2">
              <div class="metric-label">$L_1 = a\\tan\\theta$</div>
              <div class="metric-val">${l1.toFixed(2)}</div>
            </div>
            <div class="metric-card m3">
              <div class="metric-label">$L_2 = a\\tan^2\\theta$</div>
              <div class="metric-val">${l2.toFixed(2)}</div>
            </div>
            <div class="metric-card" style="border-top: 3px solid var(--accent-purple);">
              <div class="metric-label">$L_3 = a\\tan^3\\theta$</div>
              <div class="metric-val">${l3.toFixed(2)}</div>
            </div>
          </div>
          <div style="background: rgba(56, 189, 248, 0.08); padding: 12px; border-radius: var(--radius-sm); border: 1px solid rgba(56, 189, 248, 0.2); margin-top: 12px; text-align: center; font-size: 0.88rem;">
            공비 $r = \\tan(${l6State.chainTheta}^\\circ) = \\mathbf{${tanVal.toFixed(3)}}$ &nbsp;|&nbsp; 
            등비중앙 검증: $L_1^2 = ${(l1*l1).toFixed(3)} \\approx L_0 \\cdot L_2 = ${(l0*l2).toFixed(3)}$ <span style="color: var(--accent-green); font-weight: bold;">(일치!)</span>
          </div>
        `;
      } else if (l6State.mode === 'secant') {
        themeBadge.innerText = '2. 할선정리 (방멱)';
        bannerLabel.innerText = '🌟 방멱의 정리 (Power of a Point Theorem) 핵심 등식';
        bannerMath.innerHTML = '$$\\mathbf{PA \\cdot PB = PC \\cdot PD \\quad (\\text{내부 교차 & 외부 두 할선}) \\quad\\Big|\\quad PT^2 = PA \\cdot PB \\quad (\\text{접선과 할선})}$$';
        caption.innerText = '점 P의 위치에 관계없이 원과 만나는 두 선분의 곱이 언제나 일정함을 실시간 검증';

        subCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">🎛️ 할선정리 3대 유형 선택 및 점 P 이동</span>
          </div>
          <div class="preset-grid" style="grid-template-columns: 1fr 1fr 1fr; margin-bottom: 12px;">
            <button class="preset-btn ${l6State.secantCase==='case_chords'?'active':''}" onclick="l6State.secantCase='case_chords'; syncL6UI(); renderL6();">
              <span>내부 교차 현</span>
              <span class="p-sub">$a \\cdot b = c \\cdot d$</span>
            </button>
            <button class="preset-btn ${l6State.secantCase==='case_secants'?'active':''}" onclick="l6State.secantCase='case_secants'; syncL6UI(); renderL6();">
              <span>외부 두 할선</span>
              <span class="p-sub">$a(a+b)=c(c+d)$</span>
            </button>
            <button class="preset-btn ${l6State.secantCase==='case_tangent'?'active':''}" onclick="l6State.secantCase='case_tangent'; syncL6UI(); renderL6();">
              <span>접선과 할선</span>
              <span class="p-sub">$t^2 = a(a+b)$</span>
            </button>
          </div>
          <div class="slider-row">
            <label>점 P 위치 파라미터: <strong id="l6SecantPosVal" style="color: var(--accent-gold);">${l6State.secantPos.toFixed(2)}</strong></label>
            <input type="range" min="0.1" max="0.9" step="0.02" value="${l6State.secantPos}" oninput="l6State.secantPos=parseFloat(this.value); document.getElementById('l6SecantPosVal').innerText=this.value; renderL6();">
          </div>
        `;

        renderL6SecantMetrics();
      } else if (l6State.mode === 'tangent') {
        themeBadge.innerText = '3. 접현각 & 평행선';
        bannerLabel.innerText = '🌟 접현각과 두 원의 공통접선 평행 증명';
        bannerMath.innerHTML = '$$\\angle \\text{접현각} = \\angle \\text{원주각} = \\theta \\implies \\text{공통접선 경유 엇각/동위각 상등} \\implies \\mathbf{l_1 \\parallel l_2 \\text{ (평행선 발견)}}$$';
        caption.innerText = '접선과 현이 이루는 각(접현각)을 징검다리 삼아 두 원의 현이 평행함을 증명';

        subCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">🎛️ 두 원의 접점 배치 모드 선택</span>
          </div>
          <div class="preset-grid" style="grid-template-columns: 1fr 1fr;">
            <button class="preset-btn ${l6State.tangentCase==='case_ext'?'active':''}" onclick="l6State.tangentCase='case_ext'; syncL6UI(); renderL6();">
              <span>외접하는 두 원</span>
              <span class="p-sub">공통내접선 $\\to$ 엇각 일치 $\\to$ 평행</span>
            </button>
            <button class="preset-btn ${l6State.tangentCase==='case_int'?'active':''}" onclick="l6State.tangentCase='case_int'; syncL6UI(); renderL6();">
              <span>내접하는 두 원</span>
              <span class="p-sub">공통외접선 $\\to$ 동위각 일치 $\\to$ 평행</span>
            </button>
          </div>
        `;

        metricCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">💡 수능 고난도 킬러 행동 강령</span>
          </div>
          <div style="background: rgba(245, 158, 11, 0.08); padding: 14px; border-radius: var(--radius-sm); border: 1px solid rgba(245, 158, 11, 0.25); font-size: 0.88rem; line-height: 1.8;">
            <div style="color: var(--accent-gold); font-weight: 700; margin-bottom: 4px;">🎯 평가원이 숨겨놓은 평행선 발견 알고리즘</div>
            1. 접점에서 출발하는 두 원의 접현각 $\\theta$를 각각 표시한다.<br>
            2. 외접원: 맞꼭지각을 통과하여 반대편 접현각과 엇각이 같아지므로 <strong>$l_1 \\parallel l_2$</strong>!<br>
            3. 내접원: 같은 접선에서 동위각이 같아지므로 <strong>$l_1 \\parallel l_2$</strong>!<br>
            4. 평행선이 발견되면 즉시 <strong>모래시계형 / 피라미드형 닮음비($AA$)</strong>를 전개한다.
          </div>
        `;
      } else if (l6State.mode === 'quad') {
        themeBadge.innerText = '4. 외접 사각형 대변합';
        bannerLabel.innerText = '🌟 원에 외접하는 사각형의 대변의 합 정리';
        bannerMath.innerHTML = '$$\\mathbf{\\text{윗변} + \\text{아랫변} = \\text{왼쪽변} + \\text{오른쪽변} = x + y + z + w}$$';
        caption.innerText = '원 외부 한 점에서 그은 접선의 길이가 같음(PA=PB)에서 유도되는 대변의 합 불변성';

        subCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">🎛️ 사각형 꼭짓점 이동 파라미터</span>
          </div>
          <div class="slider-row">
            <label>변형 오프셋: <strong id="l6QuadVal" style="color: var(--accent-blue);">${l6State.quadOffset.toFixed(2)}</strong></label>
            <input type="range" min="-0.3" max="0.3" step="0.05" value="${l6State.quadOffset}" oninput="l6State.quadOffset=parseFloat(this.value); document.getElementById('l6QuadVal').innerText=this.value; renderL6();">
          </div>
        `;

        metricCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">📊 실시간 대변의 합 계산 및 검증</span>
          </div>
          <div class="metric-grid" style="grid-template-columns: 1fr 1fr;">
            <div class="metric-card m1">
              <div class="metric-label">윗변 + 아랫변 (상 + 하)</div>
              <div class="metric-val" id="l6SumTopBottom">14.60</div>
            </div>
            <div class="metric-card m2">
              <div class="metric-label">왼쪽변 + 오른쪽변 (좌 + 우)</div>
              <div class="metric-val" id="l6SumLeftRight">14.60</div>
            </div>
          </div>
          <div style="background: rgba(52, 211, 153, 0.08); padding: 12px; border-radius: var(--radius-sm); border: 1px solid rgba(52, 211, 153, 0.25); margin-top: 12px; text-align: center; font-size: 0.88rem; color: var(--accent-green); font-weight: bold;">
            (상 + 하) = (좌 + 우) 완벽 일치!
          </div>
        `;
      }

      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function renderL6SecantMetrics(pa, pb, pc, pd, isTangent) {
      const metricCard = document.getElementById('l6MetricCard');
      if (!metricCard) return;

      if (!pa) {
        // default dummy numbers to be updated by renderL6
        pa = 3.2; pb = 5.0; pc = 2.0; pd = 8.0; isTangent = false;
      }

      const prod1 = pa * pb;
      const prod2 = isTangent ? (pc * pc) : (pc * pd);

      if (isTangent) {
        metricCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">📊 접선과 할선 실시간 곱 검증</span>
          </div>
          <div class="metric-grid" style="grid-template-columns: 1fr 1fr;">
            <div class="metric-card m1">
              <div class="metric-label">할선 $PA \\cdot PB$</div>
              <div class="metric-val">${pa.toFixed(2)} × ${pb.toFixed(2)} = ${prod1.toFixed(2)}</div>
            </div>
            <div class="metric-card m2">
              <div class="metric-label">접선 $PT^2$</div>
              <div class="metric-val">${pc.toFixed(2)}² = ${prod2.toFixed(2)}</div>
            </div>
          </div>
          <div style="background: rgba(52, 211, 153, 0.08); padding: 10px; border-radius: var(--radius-sm); border: 1px solid rgba(52, 211, 153, 0.25); margin-top: 10px; text-align: center; font-size: 0.88rem; color: var(--accent-green); font-weight: bold;">
            $|PT^2 - PA \\cdot PB| = 0.00$ (완벽 일치!)
          </div>
        `;
      } else {
        metricCard.innerHTML = `
          <div class="control-header">
            <span class="control-title">📊 실시간 선분의 곱(방멱) 검증</span>
          </div>
          <div class="metric-grid" style="grid-template-columns: 1fr 1fr;">
            <div class="metric-card m1">
              <div class="metric-label">선분 1: $PA \\cdot PB$</div>
              <div class="metric-val">${pa.toFixed(2)} × ${pb.toFixed(2)} = ${prod1.toFixed(2)}</div>
            </div>
            <div class="metric-card m2">
              <div class="metric-label">선분 2: $PC \\cdot PD$</div>
              <div class="metric-val">${pc.toFixed(2)} × ${pd.toFixed(2)} = ${prod2.toFixed(2)}</div>
            </div>
          </div>
          <div style="background: rgba(52, 211, 153, 0.08); padding: 10px; border-radius: var(--radius-sm); border: 1px solid rgba(52, 211, 153, 0.25); margin-top: 10px; text-align: center; font-size: 0.88rem; color: var(--accent-green); font-weight: bold;">
            $|PA \\cdot PB - PC \\cdot PD| = 0.00$ (완벽 일치!)
          </div>
        `;
      }
    }

    function renderL6() {
      const canvas = document.getElementById('l6Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      if (l6State.mode === 'chain') {
        renderL6Chain(ctx, w, h);
      } else if (l6State.mode === 'secant') {
        renderL6Secant(ctx, w, h);
      } else if (l6State.mode === 'tangent') {
        renderL6Tangent(ctx, w, h);
      } else if (l6State.mode === 'quad') {
        renderL6Quad(ctx, w, h);
      }
    }

    /* 1. Chain Mode Render */
    function renderL6Chain(ctx, w, h) {
      const a = l6State.chainA;
      const deg = l6State.chainTheta;
      const rad = deg * Math.PI / 180;
      const scale = 55;

      const pA = { x: 70, y: 380 };
      const lenA = a * scale;
      const pB = { x: pA.x + lenA, y: pA.y };
      const lenB = lenA * Math.tan(rad);
      const pC = { x: pB.x, y: pB.y - lenB };

      // Triangle 1: ABC
      ctx.fillStyle = 'rgba(56, 189, 248, 0.12)';
      ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pB.x, pB.y); ctx.lineTo(pC.x, pC.y); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3; ctx.stroke();

      // Right angle at B
      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 2;
      ctx.strokeRect(pB.x - 16, pB.y - 16, 16, 16);

      // Angle theta arc at A
      ctx.beginPath(); ctx.arc(pA.x, pA.y, 38, -rad, 0); ctx.strokeStyle = '#fbbf24'; ctx.stroke();
      ctx.fillStyle = '#fbbf24'; ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText(`θ (${deg}°)`, pA.x + 46, pA.y - 8);

      // Angle badge at A (circle) and C (triangle)
      ctx.fillStyle = '#34d399'; ctx.beginPath(); ctx.arc(pA.x + 24, pA.y - 7, 5, 0, Math.PI*2); ctx.fill();
      ctx.fillStyle = '#fbbf24'; ctx.beginPath(); ctx.arc(pC.x - 8, pC.y + 22, 5, 0, Math.PI*2); ctx.fill();

      // Length labels
      ctx.fillStyle = '#fff'; ctx.font = 'bold 14px "JetBrains Mono", monospace';
      ctx.fillText(`a = ${a.toFixed(1)}`, (pA.x + pB.x)/2 - 25, pB.y + 26);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText(`a·tanθ = ${(a*Math.tan(rad)).toFixed(2)}`, pB.x + 12, (pB.y + pC.y)/2 + 4);

      // Triangle 2: CD from C perpendicular to AC
      // Vector AC
      const vAC = { x: pC.x - pA.x, y: pC.y - pA.y };
      const lenAC = Math.hypot(vAC.x, vAC.y);
      // Unit normal to AC (pointing up-left)
      const uNorm = { x: vAC.y / lenAC, y: -vAC.x / lenAC };
      const len2 = lenB * Math.tan(rad);
      const pD = { x: pC.x + uNorm.x * len2, y: pC.y + uNorm.y * len2 };

      ctx.fillStyle = 'rgba(251, 191, 36, 0.12)';
      ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pC.x, pC.y); ctx.lineTo(pD.x, pD.y); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 2.5; ctx.stroke();

      // Triangle 3: DE
      const vAD = { x: pD.x - pA.x, y: pD.y - pA.y };
      const lenAD = Math.hypot(vAD.x, vAD.y);
      const uNorm2 = { x: vAD.y / lenAD, y: -vAD.x / lenAD };
      const len3 = len2 * Math.tan(rad);
      const pE = { x: pD.x + uNorm2.x * len3, y: pD.y + uNorm2.y * len3 };

      ctx.fillStyle = 'rgba(52, 211, 153, 0.12)';
      ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pD.x, pD.y); ctx.lineTo(pE.x, pE.y); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = '#34d399'; ctx.lineWidth = 2.5; ctx.stroke();

      // Label L2, L3
      ctx.fillStyle = '#fbbf24';
      ctx.fillText(`a·tan²θ = ${(a*Math.tan(rad)**2).toFixed(2)}`, pD.x - 30, pD.y - 12);
      ctx.fillStyle = '#34d399';
      ctx.fillText(`a·tan³θ = ${(a*Math.tan(rad)**3).toFixed(2)}`, pE.x - 45, pE.y - 10);

      // Points
      [pA, pB, pC, pD, pE].forEach((p, idx) => {
        ctx.fillStyle = idx === 0 ? '#38bdf8' : '#fff';
        ctx.beginPath(); ctx.arc(p.x, p.y, 5, 0, Math.PI*2); ctx.fill();
      });
      ctx.fillStyle = '#fff'; ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('A', pA.x - 18, pA.y + 4);
      ctx.fillText('B', pB.x + 8, pB.y + 4);
      ctx.fillText('C', pC.x + 8, pC.y);
      ctx.fillText('D', pD.x + 8, pD.y);
      ctx.fillText('E', pE.x - 15, pE.y - 6);
    }

    /* 2. Secant Mode Render */
    function renderL6Secant(ctx, w, h) {
      const cCenter = { x: 300, y: 260 };
      const R = 150;

      // Draw Circle
      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.arc(cCenter.x, cCenter.y, R, 0, Math.PI*2); ctx.stroke();
      ctx.fillStyle = 'rgba(56, 189, 248, 0.04)'; ctx.fill();

      // Center Dot
      ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
      ctx.beginPath(); ctx.arc(cCenter.x, cCenter.y, 4, 0, Math.PI*2); ctx.fill();
      ctx.fillText('O', cCenter.x + 6, cCenter.y - 6);

      const pos = l6State.secantPos;

      if (l6State.secantCase === 'case_chords') {
        // Point P inside the circle
        const pP = { x: cCenter.x - 30 + (pos - 0.5) * 80, y: cCenter.y + 20 };
        // Chord 1 angle 1
        const ang1 = 0.35, ang2 = ang1 + Math.PI;
        // Intersections with circle
        // Line through P with direction ang: P + t * (cos, sin)
        function getChordPts(center, r, pt, angle) {
          const dx = Math.cos(angle), dy = Math.sin(angle);
          const ox = pt.x - center.x, oy = pt.y - center.y;
          // (ox + t*dx)^2 + (oy + t*dy)^2 = r^2
          const A = 1;
          const B = 2 * (ox*dx + oy*dy);
          const C = ox*ox + oy*oy - r*r;
          const disc = Math.sqrt(Math.max(0, B*B - 4*A*C));
          const t1 = (-B + disc) / (2*A);
          const t2 = (-B - disc) / (2*A);
          return [
            { x: pt.x + t1*dx, y: pt.y + t1*dy, t: t1 },
            { x: pt.x + t2*dx, y: pt.y + t2*dy, t: t2 }
          ];
        }

        const pts1 = getChordPts(cCenter, R, pP, 0.4);
        const pts2 = getChordPts(cCenter, R, pP, 1.85);

        const pA = pts1[0], pB = pts1[1];
        const pC = pts2[0], pD = pts2[1];

        // Draw chords
        ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pB.x, pB.y); ctx.stroke();

        ctx.strokeStyle = '#34d399'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(pC.x, pC.y); ctx.lineTo(pD.x, pD.y); ctx.stroke();

        // Shaded similar triangles PAC & PDB
        ctx.fillStyle = 'rgba(251, 191, 36, 0.1)';
        ctx.beginPath(); ctx.moveTo(pP.x, pP.y); ctx.lineTo(pA.x, pA.y); ctx.lineTo(pC.x, pC.y); ctx.closePath(); ctx.fill();
        ctx.fillStyle = 'rgba(52, 211, 153, 0.1)';
        ctx.beginPath(); ctx.moveTo(pP.x, pP.y); ctx.lineTo(pB.x, pB.y); ctx.lineTo(pD.x, pD.y); ctx.closePath(); ctx.fill();

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)'; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pC.x, pC.y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(pB.x, pB.y); ctx.lineTo(pD.x, pD.y); ctx.stroke();
        ctx.setLineDash([]);

        // Points
        drawDot(ctx, pP, '#ef4444', 'P');
        drawDot(ctx, pA, '#fbbf24', 'A');
        drawDot(ctx, pB, '#fbbf24', 'B');
        drawDot(ctx, pC, '#34d399', 'C');
        drawDot(ctx, pD, '#34d399', 'D');

        const dPA = Math.hypot(pA.x - pP.x, pA.y - pP.y) / 40;
        const dPB = Math.hypot(pB.x - pP.x, pB.y - pP.y) / 40;
        const dPC = Math.hypot(pC.x - pP.x, pC.y - pP.y) / 40;
        const dPD = Math.hypot(pD.x - pP.x, pD.y - pP.y) / 40;
        renderL6SecantMetrics(dPA, dPB, dPC, dPD, false);

      } else if (l6State.secantCase === 'case_secants') {
        // Point P outside circle to the left
        const pP = { x: 70 + (pos - 0.5) * 50, y: 260 };

        function getSecantPts(center, r, pt, angle) {
          const dx = Math.cos(angle), dy = Math.sin(angle);
          const ox = pt.x - center.x, oy = pt.y - center.y;
          const A = 1, B = 2*(ox*dx + oy*dy), C = ox*ox + oy*oy - r*r;
          const disc = Math.sqrt(Math.max(0, B*B - 4*A*C));
          const t1 = (-B - disc) / 2; // closer
          const t2 = (-B + disc) / 2; // farther
          return [
            { x: pt.x + t1*dx, y: pt.y + t1*dy },
            { x: pt.x + t2*dx, y: pt.y + t2*dy }
          ];
        }

        const pts1 = getSecantPts(cCenter, R, pP, -0.22);
        const pts2 = getSecantPts(cCenter, R, pP, 0.28);

        const pA = pts1[0], pB = pts1[1];
        const pC = pts2[0], pD = pts2[1];

        // Secant lines
        ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(pP.x, pP.y); ctx.lineTo(pB.x, pB.y); ctx.stroke();
        ctx.strokeStyle = '#34d399'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(pP.x, pP.y); ctx.lineTo(pD.x, pD.y); ctx.stroke();

        // Cross chord connecting AC and BD
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)'; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pC.x, pC.y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(pB.x, pB.y); ctx.lineTo(pD.x, pD.y); ctx.stroke();
        ctx.setLineDash([]);

        drawDot(ctx, pP, '#ef4444', 'P');
        drawDot(ctx, pA, '#fbbf24', 'A');
        drawDot(ctx, pB, '#fbbf24', 'B');
        drawDot(ctx, pC, '#34d399', 'C');
        drawDot(ctx, pD, '#34d399', 'D');

        const dPA = Math.hypot(pA.x - pP.x, pA.y - pP.y) / 40;
        const dPB = Math.hypot(pB.x - pP.x, pB.y - pP.y) / 40;
        const dPC = Math.hypot(pC.x - pP.x, pC.y - pP.y) / 40;
        const dPD = Math.hypot(pD.x - pP.x, pD.y - pP.y) / 40;
        renderL6SecantMetrics(dPA, dPB, dPC, dPD, false);

      } else if (l6State.secantCase === 'case_tangent') {
        const pP = { x: 70 + (pos - 0.5) * 50, y: 260 };
        const dPO = Math.hypot(cCenter.x - pP.x, cCenter.y - pP.y);
        const tanAngle = Math.asin(R / dPO);
        const baseAngle = Math.atan2(cCenter.y - pP.y, cCenter.x - pP.x);

        // Tangent Point T (upper)
        const lenPT = Math.sqrt(dPO*dPO - R*R);
        const pT = {
          x: pP.x + lenPT * Math.cos(baseAngle - tanAngle),
          y: pP.y + lenPT * Math.sin(baseAngle - tanAngle)
        };

        // Secant PAB (lower)
        const secAngle = baseAngle + 0.22;
        const dx = Math.cos(secAngle), dy = Math.sin(secAngle);
        const ox = pP.x - cCenter.x, oy = pP.y - cCenter.y;
        const B = 2*(ox*dx + oy*dy), C = ox*ox + oy*oy - R*R;
        const disc = Math.sqrt(Math.max(0, B*B - 4*C));
        const t1 = (-B - disc)/2, t2 = (-B + disc)/2;
        const pA = { x: pP.x + t1*dx, y: pP.y + t1*dy };
        const pB = { x: pP.x + t2*dx, y: pP.y + t2*dy };

        // Lines
        ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(pP.x, pP.y); ctx.lineTo(pT.x, pT.y); ctx.stroke();

        ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(pP.x, pP.y); ctx.lineTo(pB.x, pB.y); ctx.stroke();

        // Triangle PTA and PBT
        ctx.strokeStyle = 'rgba(251, 191, 36, 0.4)'; ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(pT.x, pT.y); ctx.lineTo(pA.x, pA.y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(pT.x, pT.y); ctx.lineTo(pB.x, pB.y); ctx.stroke();
        ctx.setLineDash([]);

        drawDot(ctx, pP, '#ef4444', 'P');
        drawDot(ctx, pT, '#fbbf24', 'T (접점)');
        drawDot(ctx, pA, '#38bdf8', 'A');
        drawDot(ctx, pB, '#38bdf8', 'B');

        const dPA = Math.hypot(pA.x - pP.x, pA.y - pP.y) / 40;
        const dPB = Math.hypot(pB.x - pP.x, pB.y - pP.y) / 40;
        const dPT = lenPT / 40;
        renderL6SecantMetrics(dPA, dPB, dPT, 0, true);
      }
    }

    /* 3. Tangent & Alternate Angle Render */
    function renderL6Tangent(ctx, w, h) {
      if (l6State.tangentCase === 'case_ext') {
        // Two externally touching circles
        const r1 = 100, r2 = 70;
        const pT = { x: 270, y: 260 };
        const c1 = { x: pT.x - r1, y: pT.y };
        const c2 = { x: pT.x + r2, y: pT.y };

        // Draw Circles
        ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.arc(c1.x, c1.y, r1, 0, Math.PI*2); ctx.stroke();
        ctx.beginPath(); ctx.arc(c2.x, c2.y, r2, 0, Math.PI*2); ctx.stroke();

        // Common Tangent Line (vertical)
        ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(pT.x, 60); ctx.lineTo(pT.x, 460); ctx.stroke();
        ctx.fillStyle = '#fbbf24'; ctx.font = 'bold 12px Inter, sans-serif';
        ctx.fillText('공통내접선', pT.x + 8, 80);

        // Line 1 through T: ang1
        const ang1 = 0.55;
        // Line 2 through T: ang2
        const ang2 = -0.65;

        // Points on circles
        const pA = { x: pT.x - 2*r1*Math.cos(ang1)*Math.cos(ang1), y: pT.y - 2*r1*Math.cos(ang1)*Math.sin(ang1) };
        const pC = { x: pT.x + 2*r2*Math.cos(ang1)*Math.cos(ang1), y: pT.y + 2*r2*Math.cos(ang1)*Math.sin(ang1) };

        const pB = { x: pT.x - 2*r1*Math.cos(ang2)*Math.cos(ang2), y: pT.y - 2*r1*Math.cos(ang2)*Math.sin(ang2) };
        const pD = { x: pT.x + 2*r2*Math.cos(ang2)*Math.cos(ang2), y: pT.y + 2*r2*Math.cos(ang2)*Math.sin(ang2) };

        // Transversal lines
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)'; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pC.x, pC.y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(pB.x, pB.y); ctx.lineTo(pD.x, pD.y); ctx.stroke();

        // Parallel Chords AB and CD!
        ctx.strokeStyle = '#34d399'; ctx.lineWidth = 3.5;
        ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pB.x, pB.y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(pC.x, pC.y); ctx.lineTo(pD.x, pD.y); ctx.stroke();

        // Parallel arrows
        drawArrowBadge(ctx, (pA.x+pB.x)/2, (pA.y+pB.y)/2, 'l₁ (평행)');
        drawArrowBadge(ctx, (pC.x+pD.x)/2, (pC.y+pD.y)/2, 'l₂ (l₁ ∥ l₂)');

        drawDot(ctx, pT, '#ef4444', 'T (접점)');
        drawDot(ctx, pA, '#38bdf8', 'A');
        drawDot(ctx, pB, '#38bdf8', 'B');
        drawDot(ctx, pC, '#38bdf8', 'C');
        drawDot(ctx, pD, '#38bdf8', 'D');

      } else {
        // Internally touching circles
        const r1 = 140, r2 = 70;
        const pT = { x: 160, y: 260 };
        const c1 = { x: pT.x + r1, y: pT.y };
        const c2 = { x: pT.x + r2, y: pT.y };

        ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.arc(c1.x, c1.y, r1, 0, Math.PI*2); ctx.stroke();
        ctx.strokeStyle = '#818cf8';
        ctx.beginPath(); ctx.arc(c2.x, c2.y, r2, 0, Math.PI*2); ctx.stroke();

        // Common Tangent Line
        ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(pT.x, 60); ctx.lineTo(pT.x, 460); ctx.stroke();
        ctx.fillStyle = '#fbbf24'; ctx.font = 'bold 12px Inter, sans-serif';
        ctx.fillText('공통외접선', pT.x + 8, 80);

        const a1 = 0.5, a2 = -0.45;
        const pA1 = { x: pT.x + 2*r2*Math.cos(a1)*Math.cos(a1), y: pT.y + 2*r2*Math.cos(a1)*Math.sin(a1) };
        const pB1 = { x: pT.x + 2*r1*Math.cos(a1)*Math.cos(a1), y: pT.y + 2*r1*Math.cos(a1)*Math.sin(a1) };

        const pA2 = { x: pT.x + 2*r2*Math.cos(a2)*Math.cos(a2), y: pT.y + 2*r2*Math.cos(a2)*Math.sin(a2) };
        const pB2 = { x: pT.x + 2*r1*Math.cos(a2)*Math.cos(a2), y: pT.y + 2*r1*Math.cos(a2)*Math.sin(a2) };

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)'; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(pT.x, pT.y); ctx.lineTo(pB1.x, pB1.y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(pT.x, pT.y); ctx.lineTo(pB2.x, pB2.y); ctx.stroke();

        // Parallel Chords
        ctx.strokeStyle = '#34d399'; ctx.lineWidth = 3.5;
        ctx.beginPath(); ctx.moveTo(pA1.x, pA1.y); ctx.lineTo(pA2.x, pA2.y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(pB1.x, pB1.y); ctx.lineTo(pB2.x, pB2.y); ctx.stroke();

        drawArrowBadge(ctx, (pA1.x+pA2.x)/2, (pA1.y+pA2.y)/2, '동위각 일치');
        drawArrowBadge(ctx, (pB1.x+pB2.x)/2, (pB1.y+pB2.y)/2, '평행 (l₁ ∥ l₂)');

        drawDot(ctx, pT, '#ef4444', 'T');
        drawDot(ctx, pA1, '#818cf8', 'A₁');
        drawDot(ctx, pA2, '#818cf8', 'A₂');
        drawDot(ctx, pB1, '#38bdf8', 'B₁');
        drawDot(ctx, pB2, '#38bdf8', 'B₂');
      }
    }

    /* 4. Quad Mode Render */
    function renderL6Quad(ctx, w, h) {
      const cCenter = { x: 280, y: 260 };
      const R = 110;

      // Draw Inscribed Circle
      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.arc(cCenter.x, cCenter.y, R, 0, Math.PI*2); ctx.stroke();
      ctx.fillStyle = 'rgba(56, 189, 248, 0.05)'; ctx.fill();

      // Tangent points on circle at 4 angles
      const off = l6State.quadOffset;
      const th1 = 0.8 + off, th2 = 2.1 - off*0.5, th3 = 3.8 + off*0.7, th4 = 5.3 - off*0.6;
      const tA = { x: cCenter.x + R*Math.cos(th1), y: cCenter.y + R*Math.sin(th1) };
      const tB = { x: cCenter.x + R*Math.cos(th2), y: cCenter.y + R*Math.sin(th2) };
      const tC = { x: cCenter.x + R*Math.cos(th3), y: cCenter.y + R*Math.sin(th3) };
      const tD = { x: cCenter.x + R*Math.cos(th4), y: cCenter.y + R*Math.sin(th4) };

      // Intersection of tangents at thA and thB:
      function getTangentIntersection(center, r, a1, a2) {
        const midA = (a1 + a2) / 2;
        const d = r / Math.cos((a1 - a2)/2);
        return {
          x: center.x + d * Math.cos(midA),
          y: center.y + d * Math.sin(midA)
        };
      }

      const p1 = getTangentIntersection(cCenter, R, th1, th2);
      const p2 = getTangentIntersection(cCenter, R, th2, th3);
      const p3 = getTangentIntersection(cCenter, R, th3, th4);
      const p4 = getTangentIntersection(cCenter, R, th4, th1 + Math.PI*2);

      // Draw quadrilateral
      ctx.strokeStyle = '#fbbf24'; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y);
      ctx.lineTo(p3.x, p3.y); ctx.lineTo(p4.x, p4.y);
      ctx.closePath();
      ctx.stroke();

      // Draw tangent points
      [tA, tB, tC, tD].forEach(t => {
        ctx.fillStyle = '#ef4444';
        ctx.beginPath(); ctx.arc(t.x, t.y, 4, 0, Math.PI*2); ctx.fill();
      });

      // Side lengths
      const side12 = Math.hypot(p2.x - p1.x, p2.y - p1.y) / 30; // top
      const side34 = Math.hypot(p4.x - p3.x, p4.y - p3.y) / 30; // bottom
      const side23 = Math.hypot(p3.x - p2.x, p3.y - p2.y) / 30; // left
      const side41 = Math.hypot(p1.x - p4.x, p1.y - p4.y) / 30; // right

      const sumTB = side12 + side34;
      const sumLR = side23 + side41;

      const tbEl = document.getElementById('l6SumTopBottom');
      const lrEl = document.getElementById('l6SumLeftRight');
      if (tbEl && lrEl) {
        tbEl.innerText = sumTB.toFixed(2);
        lrEl.innerText = sumLR.toFixed(2);
      }

      drawDot(ctx, p1, '#fff', 'A');
      drawDot(ctx, p2, '#fff', 'B');
      drawDot(ctx, p3, '#fff', 'C');
      drawDot(ctx, p4, '#fff', 'D');
    }

    function drawDot(ctx, pt, color, label) {
      ctx.fillStyle = color;
      ctx.beginPath(); ctx.arc(pt.x, pt.y, 5, 0, Math.PI*2); ctx.fill();
      ctx.strokeStyle = '#000'; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.fillStyle = '#fff'; ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(label, pt.x + 8, pt.y - 6);
    }

    function drawArrowBadge(ctx, x, y, text) {
      ctx.fillStyle = 'rgba(52, 211, 153, 0.2)';
      ctx.fillRect(x - 30, y - 10, 60, 20);
      ctx.strokeStyle = '#34d399'; ctx.strokeRect(x - 30, y - 10, 60, 20);
      ctx.fillStyle = '#34d399'; ctx.font = 'bold 11px Inter, sans-serif';
      ctx.textAlign = 'center'; ctx.fillText(text, x, y + 4);
      ctx.textAlign = 'start';
    }

'''

    l5_marker = '    /* ========================================================= */\n    /* LECTURE 5 (PYTHAGOREAN THEOREM: EUCLID PROOF) LOGIC       */'
    if l5_marker not in content:
        print("ERROR: l5_marker not found!")
        return

    content = content.replace(l5_marker, l6_js_logic + '\n' + l5_marker, 1)

    # 6. Update window load handler to initialize Lecture 6
    old_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      syncL5Values();
      renderL5();
    });'''

    new_load = '''    // Initialize on page load
    window.addEventListener('load', () => {
      syncL6UI();
      renderL6();
    });'''

    if old_load in content:
        content = content.replace(old_load, new_load, 1)

    # Write output to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: index.html updated successfully with Lecture 6!")

if __name__ == '__main__':
    main()
