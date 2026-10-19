# -*- coding: utf-8 -*-
"""
Script to build and inject Lecture 17 into index.html
Lecture: 유리함수 y=(ax+b)/(cx+d)의 그래프 d 변화 애니메이션 | Algeomath | 알지오매스
Instructor: 이동의 (Algeomath 공학도구 수학 수업)
YouTube Short: https://youtube.com/shorts/xDMt29XvFL0
"""

import os
import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code for tab
    with open('rational_function_d_variation_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()

    # 1. Update Switcher Bar: Add btnLec17 as active, remove active from btnLec16
    if 'id="btnLec17"' not in html:
        old_btn16 = '<button class="lecture-btn active" id="btnLec16" onclick="setLecture(16)">'
        if old_btn16 in html:
            new_btn_block = '''<button class="lecture-btn active" id="btnLec17" onclick="setLecture(17)">
          유리함수 d 변화 (알지오매스)
        </button>
        <button class="lecture-btn" id="btnLec16" onclick="setLecture(16)">'''
            html = html.replace(old_btn16, new_btn_block, 1)
            print("Added btnLec17 to switcher bar.")
        else:
            old_btn16_alt = '<button class="lecture-btn" id="btnLec16" onclick="setLecture(16)">'
            if old_btn16_alt in html:
                new_btn_block = '''<button class="lecture-btn active" id="btnLec17" onclick="setLecture(17)">
          유리함수 d 변화 (알지오매스)
        </button>
        <button class="lecture-btn" id="btnLec16" onclick="setLecture(16)">'''
                html = html.replace(old_btn16_alt, new_btn_block, 1)
                print("Added btnLec17 to switcher bar (alt).")

    # Update captured_summary button label
    html = html.replace('📸 사진 1~16 핵심 전용 페이지', '📸 사진 1~17 핵심 전용 페이지')

    # 2. Hide lecture16View if active
    if '<div id="lecture16View">' in html:
        html = html.replace('<div id="lecture16View">', '<div id="lecture16View" style="display: none;">', 1)
        print("Set lecture16View to display: none.")

    # 3. Create Lecture 17 View HTML
    escaped_manim = (manim_code
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))

    lecture17_template = '''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 17 (RATIONAL FUNCTION D VARIATION: ALGEOMATH) -->
    <!-- ============================================================== -->
    <div id="lecture17View">
      <header>
        <div class="badge-pill" style="border-color: rgba(245, 158, 11, 0.4); color: #fbbf24; box-shadow: 0 0 20px rgba(245, 158, 11, 0.3);">
          ⚡ 제17강 · 이동의 선생님 (Algeomath 알지오매스 공학수학)
        </div>
        <h1 style="background: linear-gradient(135deg, #fbbf24 0%, #38bdf8 50%, #f43f5e 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          유리함수 $y = \\frac{ax+b}{cx+d}$의 그래프와 매개변수 $d$의 동적 변화
        </h1>
        <p class="subtitle" style="max-width: 900px; margin: 0 auto; line-height: 1.7; color: #cbd5e1;">
          "분모의 상수항 $d$가 변하면 유리함수의 그래프는 어떻게 왜곡되고 이동할까?"<br>
          알지오매스(Algeomath) 공학도구로 시각화한 $y = \\frac{x+2}{x+d}$의 동적 궤적:<br>
          <strong>수직점근선의 이동 · 수평점근선 $y=1$의 불변성 · 고정 정점 $(-2, 0)$ · $d=2$ 축퇴(직선 붕괴) 및 사분면 대반전</strong>까지 완벽 해부합니다.
        </p>
      </header>

      <!-- TOP SUMMARY BANNER -->
      <div style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(56, 189, 248, 0.1), rgba(15, 23, 42, 0.95)); border: 2px solid rgba(245, 158, 11, 0.4); border-radius: 20px; padding: 26px; margin-bottom: 35px; box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5);">
        <div style="font-size: 0.95rem; font-weight: 700; color: #fbbf24; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; text-align: center;">
          ⭐ 알지오매스 모델 함수: $y = \\frac{x+2}{x+d} = 1 + \\frac{2-d}{x+d}$ ($a=1, b=2, c=1$)
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; text-align: center; margin-top: 15px;">
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(56, 189, 248, 0.3);">
            <div style="color: #38bdf8; font-weight: bold; font-size: 0.85rem;">1. 수평점근선 (고정)</div>
            <div style="color: #fff; font-size: 1.1rem; font-family: monospace; margin-top: 3px;">$y = 1$ (불변)</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(251, 191, 36, 0.3);">
            <div style="color: #fbbf24; font-weight: bold; font-size: 0.85rem;">2. 수직점근선 (이동)</div>
            <div style="color: #fff; font-size: 1.1rem; font-family: monospace; margin-top: 3px;">$x = -d$ (좌우 이동)</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(244, 63, 94, 0.3);">
            <div style="color: #f43f5e; font-weight: bold; font-size: 0.85rem;">3. 고정 정점 (Fixed Pt)</div>
            <div style="color: #fff; font-size: 1.1rem; font-family: monospace; margin-top: 3px;">$(-2, 0)$ 항상 통과</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(168, 85, 247, 0.3);">
            <div style="color: #c084fc; font-weight: bold; font-size: 0.85rem;">4. 임계점 $d = 2$ (축퇴)</div>
            <div style="color: #fff; font-size: 1.1rem; font-family: monospace; margin-top: 3px;">$ad - bc = 0 \\implies y=1$ 직선!</div>
          </div>
        </div>
      </div>

      <!-- MAIN INTERACTIVE LAB: ALGEOMATH RATIONAL FUNCTION SIMULATOR -->
      <div class="card" style="margin-bottom: 40px; border-color: rgba(245, 158, 11, 0.4); box-shadow: 0 10px 30px rgba(245, 158, 11, 0.15);">
        <h2 style="color: #fbbf24; display: flex; align-items: center; gap: 10px;">
          <span>🔬</span> 알지오매스 스타일 유리함수 $d$ 변화 인터랙티브 시뮬레이터
        </h2>
        <p style="color: #94a3b8; margin-bottom: 20px;">
          슬라이더를 드래그하거나 <strong>[▶ 자동 왕복 애니메이션]</strong>을 켜서 $d$의 변화에 따른 점근선의 궤적, 대칭 중심의 이동, 그리고 $d=2$에서의 쌍곡선 사분면 반전 현상을 실시간으로 체험해보세요.
        </p>

        <!-- CONTROLS -->
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; padding: 20px; margin-bottom: 22px;">
          <!-- BUTTONS ROW -->
          <div style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin-bottom: 16px;">
            <button class="nav-btn" id="btnAnimToggle17" onclick="toggleAnim17()" style="background: #fbbf24; color: #0f172a; font-weight: bold; border-color: #fbbf24;">▶ 자동 애니메이션 (왕복)</button>
            <span style="color: #64748b; margin: 0 4px;">|</span>
            <span style="font-weight: 700; color: #e2e8f0; font-size: 0.85rem;">주요 임계값 바로가기:</span>
            <button class="nav-btn" onclick="setD17(-8)" style="padding: 4px 10px; font-size: 0.8rem;">d = -8 (x = 8)</button>
            <button class="nav-btn" onclick="setD17(-2)" style="padding: 4px 10px; font-size: 0.8rem;">d = -2 (x = 2)</button>
            <button class="nav-btn" onclick="setD17(0)" style="padding: 4px 10px; font-size: 0.8rem;">d = 0 (x = 0, y축)</button>
            <button class="nav-btn" onclick="setD17(1.7)" style="padding: 4px 10px; font-size: 0.8rem; border-color: #fbbf24;">d = 1.7 (축퇴 직전)</button>
            <button class="nav-btn" onclick="setD17(2)" style="padding: 4px 10px; font-size: 0.8rem; border-color: #f43f5e; color: #f43f5e; font-weight: bold;">d = 2 (⚠️ 축퇴/직선)</button>
            <button class="nav-btn" onclick="setD17(2.3)" style="padding: 4px 10px; font-size: 0.8rem; border-color: #38bdf8;">d = 2.3 (반전 직후)</button>
            <button class="nav-btn" onclick="setD17(5)" style="padding: 4px 10px; font-size: 0.8rem;">d = 5 (x = -5)</button>
            <button class="nav-btn" onclick="setD17(8)" style="padding: 4px 10px; font-size: 0.8rem;">d = 8 (x = -8)</button>
          </div>

          <!-- SLIDER ROW -->
          <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center;">
            <div style="flex: 1; min-width: 280px; display: flex; align-items: center; gap: 12px;">
              <span style="color: #fbbf24; font-weight: bold; font-size: 0.95rem;">매개변수 $d$ 슬라이더:</span>
              <input type="range" id="sliderD17" min="-10" max="10" step="0.1" value="-2" style="flex: 1; accent-color: #fbbf24;" oninput="updateFromSlider17(this.value)">
              <span id="labelD17" style="color: #fbbf24; font-family: monospace; font-weight: bold; min-width: 55px; text-align: right; font-size: 1.1rem;">-2.0</span>
            </div>
            <div id="bannerDegeneracy17" style="display: none; background: rgba(244, 63, 94, 0.2); border: 1px solid #f43f5e; border-radius: 8px; padding: 4px 12px; color: #f43f5e; font-size: 0.85rem; font-weight: bold;">
              ⚠️ $d=2$ 축퇴 상태: $y=1$ 직선 (단, $x \ne -2$ 펑크)
            </div>
          </div>
        </div>

        <!-- REALTIME STATS -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 22px;">
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(251, 191, 36, 0.3); border-radius: 12px; padding: 12px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8;">함수식 표준형</div>
            <div id="statStdEq17" style="font-size: 1.05rem; font-weight: bold; color: #fbbf24; font-family: monospace;">y = 1 + 4/(x - 2)</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 12px; padding: 12px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8;">수직 / 수평점근선</div>
            <div id="statAsym17" style="font-size: 1.05rem; font-weight: bold; color: #38bdf8; font-family: monospace;">x = 2,  y = 1</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(244, 63, 94, 0.3); border-radius: 12px; padding: 12px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8;">대칭의 중심 &amp; 고정 정점</div>
            <div id="statPts17" style="font-size: 1.05rem; font-weight: bold; color: #f43f5e; font-family: monospace;">중심 (2, 1), 정점 (-2, 0)</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 12px; padding: 12px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8;">모양 계수 $k = 2-d$ &amp; 사분면</div>
            <div id="statQuad17" style="font-size: 1.05rem; font-weight: bold; color: #4ade80; font-family: monospace;">k = 4.0 > 0 (1, 3사분면)</div>
          </div>
        </div>

        <!-- CANVAS -->
        <div style="background: #060913; border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 16px; padding: 15px; position: relative; overflow: hidden;">
          <canvas id="canvasRational17" width="960" height="540" style="width: 100%; height: auto; display: block;"></canvas>
          <div style="margin-top: 10px; font-size: 0.85rem; color: #94a3b8; text-align: center;">
            💡 초록색 점선: <strong>수평점근선 $y=1$ (절대 고정)</strong> | 노란색 점선: <strong>수직점근선 $x=-d$ (좌우 이동)</strong> | 빨간 점: <strong>모든 곡선이 지나는 정점 $(-2, 0)$</strong>
          </div>
        </div>
      </div>

      <!-- IN-DEPTH CONCEPT TABS -->
      <div class="card" style="margin-bottom: 40px;">
        <h2 style="color: #fbbf24; display: flex; align-items: center; gap: 10px;">
          <span>📚</span> 유리함수 일반형과 $d$ 변화 심화 마스터 가이드
        </h2>

        <div style="display: flex; gap: 10px; margin-bottom: 24px; border-bottom: 1px solid #334155; padding-bottom: 12px; flex-wrap: wrap;">
          <button class="nav-btn active" id="tabBtnL17_1" onclick="switchL17Tab(1)">1. 일반형 $\\to$ 표준형 변환</button>
          <button class="nav-btn" id="tabBtnL17_2" onclick="switchL17Tab(2)">2. $d$의 변화와 점근선 거동</button>
          <button class="nav-btn" id="tabBtnL17_3" onclick="switchL17Tab(3)">3. $d=2$ 축퇴(직선 붕괴)</button>
          <button class="nav-btn" id="tabBtnL17_4" onclick="switchL17Tab(4)">4. 사분면 대반전(Flip)</button>
          <button class="nav-btn" id="tabBtnL17_5" onclick="switchL17Tab(5)">5. 고정 정점 $(-2, 0)$ 증명</button>
          <button class="nav-btn" id="tabBtnL17_6" onclick="switchL17Tab(6)">6. Manim 애니메이션 코드</button>
        </div>

        <!-- TAB 1 -->
        <div id="tabL17_1" class="tab-content" style="display: block;">
          <h3 style="color: #fbbf24;">1. 유리함수 일반형 $y = \\frac{ax+b}{cx+d}$의 표준화 공식</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            유리함수의 일반형을 분자 나누기 분모를 통해 표준형 $y = \\frac{k}{x-p} + q$로 변형하면, 기하학적 핵심 성질들이 즉시 드러납니다.
          </p>
          <div style="background: rgba(15, 23, 42, 0.8); border-left: 4px solid #fbbf24; padding: 18px; border-radius: 0 12px 12px 0; margin: 20px 0;">
            $$\\begin{aligned}
            y &= \\frac{ax+b}{cx+d} = \\frac{\\frac{a}{c}(cx+d) + \\left(b - \\frac{ad}{c}\\right)}{cx+d} \\\\
            &= \\frac{a}{c} + \\frac{\\frac{bc-ad}{c^2}}{x + \\frac{d}{c}} = q + \\frac{k}{x - p}
            \\end{aligned}$$
            <hr style="border: 0; border-top: 1px dashed #475569; margin: 15px 0;">
            <ul style="color: #e2e8f0; line-height: 1.8; margin: 0; padding-left: 20px;">
              <li><strong>수직점근선</strong>: 분모 $= 0 \\implies x = -\\frac{d}{c}$</li>
              <li><strong>수평점근선</strong>: 최고차항 계수비 $\\implies y = \\frac{a}{c}$</li>
              <li><strong>대칭의 중심</strong>: 점근선의 교점 $\\left(-\\frac{d}{c}, \\frac{a}{c}\\right)$</li>
              <li><strong>모양 결정 상수</strong>: $k = \\frac{bc-ad}{c^2} = -\\frac{ad-bc}{c^2}$</li>
            </ul>
          </div>
        </div>

        <!-- TAB 2 -->
        <div id="tabL17_2" class="tab-content" style="display: none;">
          <h3 style="color: #38bdf8;">2. 매개변수 $d$의 변화와 점근선의 동적 거동</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            모델 함수 $y = \\frac{x+2}{x+d} = 1 + \\frac{2-d}{x+d}$ 에서 매개변수 $d$가 변화할 때 점근선들은 어떻게 움직일까요?
          </p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
            <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 12px; padding: 18px;">
              <h4 style="color: #4ade80; margin-top: 0;">수평점근선: $y = 1$ (완전 고정!)</h4>
              <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                분모와 분자의 $x$ 계수비가 $\\frac{1}{1} = 1$로 고정되어 있으므로, <strong>$d$가 어떤 실수 값을 갖더라도 수평점근선 $y=1$은 절대 흔들리지 않습니다.</strong>
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(251, 191, 36, 0.3); border-radius: 12px; padding: 18px;">
              <h4 style="color: #fbbf24; margin-top: 0;">수직점근선: $x = -d$ (좌우 선형 이동)</h4>
              <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                $d$가 음수에서 양수로 증가함에 따라, 수직점근선 $x = -d$는 <strong>오른쪽($x=10$)에서 왼쪽($x=-10$)으로 일정하게 수평 이동</strong>합니다.
              </p>
            </div>
          </div>
          <p style="color: #e2e8f0; line-height: 1.8;">
            따라서 대칭의 중심 $(-d, 1)$의 자취(Locus)는 <strong>수평선 $y = 1$</strong>이 됩니다.
          </p>
        </div>

        <!-- TAB 3 -->
        <div id="tabL17_3" class="tab-content" style="display: none;">
          <h3 style="color: #f43f5e;">3. 임계점 $d = 2$에서의 축퇴(Degeneracy)와 직선 붕괴</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            $d = 2$가 되는 순간, 분수식의 분자와 분모가 일치하면서 쌍곡선이 순간적으로 붕괴하는 극적인 수학적 현상이 일어납니다.
          </p>
          <div style="background: rgba(15, 23, 42, 0.9); border: 2px solid #f43f5e; border-radius: 14px; padding: 20px; margin: 20px 0;">
            <div style="font-size: 1.15rem; color: #f43f5e; font-weight: bold; margin-bottom: 10px;">
              $$ad - bc = (1)(2) - (2)(1) = 0 \\iff k = 2 - d = 0$$
            </div>
            <p style="color: #e2e8f0; line-height: 1.8; margin-bottom: 12px;">
              함수식에 $d=2$를 대입하면:
              $$y = \\frac{x+2}{x+2} = 1 \\quad (\\text{단, } x \\ne -2)$$
            </p>
            <ul style="color: #cbd5e1; line-height: 1.8; margin: 0; padding-left: 20px;">
              <li>쌍곡선이 완전히 평평해져 <strong>수평 직선 $y = 1$</strong>로 축퇴(Degenerate)됩니다.</li>
              <li>단, $x = -2$에서는 분모가 $0$이 되므로 정의되지 않아, <strong>점 $(-2, 1)$에 펑크(구멍)가 뚫린 직선</strong>이 됩니다.</li>
            </ul>
          </div>
          <p style="color: #fbbf24; font-weight: bold;">
            💡 교과서에서 유리함수를 정의할 때 "$ad - bc \\ne 0$"이라는 제한 조건을 거는 이유가 바로 이 축퇴(직선화)를 방지하기 위함입니다.
          </p>
        </div>

        <!-- TAB 4 -->
        <div id="tabL17_4" class="tab-content" style="display: none;">
          <h3 style="color: #c084fc;">4. 사분면 대반전(Flip): $k = 2 - d$의 부호 전환</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            임계점 $d = 2$를 통과하기 전과 통과한 후, 쌍곡선의 위치가 정반대로 뒤집힙니다.
          </p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
            <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 12px; padding: 18px;">
              <h4 style="color: #38bdf8; margin-top: 0;">$d < 2$ 일 때 ($k > 0$)</h4>
              <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                $k = 2 - d > 0$ 이므로 점근선 교점을 기준으로 <strong>제1사분면과 제3사분면</strong>에 쌍곡선 위치.
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(244, 63, 94, 0.4); border-radius: 12px; padding: 18px;">
              <h4 style="color: #f43f5e; margin-top: 0;">$d > 2$ 일 때 ($k < 0$)</h4>
              <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                $k = 2 - d < 0$ 이므로 점근선 교점을 기준으로 <strong>제2사분면과 제4사분면</strong>으로 전격 위치 반전!
              </p>
            </div>
          </div>
        </div>

        <!-- TAB 5 -->
        <div id="tabL17_5" class="tab-content" style="display: none;">
          <h3 style="color: #4ade80;">5. 모든 곡선이 반드시 지나는 고정 정점 $(-2, 0)$ 증명</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            영상에서 $d$가 아무리 변해도 그래프가 $x$축 위의 한 점 $(-2, 0)$을 닻(Anchor)처럼 고정되어 지나갑니다.
          </p>
          <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 12px; padding: 20px; margin: 20px 0;">
            <p style="color: #e2e8f0; line-height: 1.8; margin-bottom: 10px;">
              함수식 $y = \\frac{x+2}{x+d}$의 양변에 $(x+d)$를 곱해 정리합니다:
              $$y(x+d) = x + 2 \\iff yx + yd = x + 2$$
              이를 $d$에 대한 항등식으로 묶으면:
              $$d \\cdot y + (yx - x - 2) = 0$$
            </p>
            <p style="color: #e2e8f0; line-height: 1.8; margin-bottom: 0;">
              이 식이 임의의 $d$에 대해 항상 성립하려면:
              $$y = 0 \\quad \\text{그리고} \\quad 0 \\cdot x - x - 2 = 0 \\implies x = -2$$
              $$\\therefore (x, y) = (-2, 0)$$
            </p>
          </div>
          <p style="color: #4ade80; font-weight: bold;">
            결론: $d$의 값과 상관없이 모든 유리함수 곡선은 $x$절편인 <strong>정점 $(-2, 0)$을 반드시 통과</strong>합니다!
          </p>
        </div>

        <!-- TAB 6: MANIM CODE -->
        <div id="tabL17_6" class="tab-content" style="display: none;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <h3 style="color: #fbbf24; margin: 0;">3Blue1Brown 스타일 Manim Community 애니메이션 코드</h3>
            <button class="nav-btn" onclick="copyManimCode17()" style="padding: 6px 14px; font-size: 0.85rem; border-color: #fbbf24;">📋 코드 복사</button>
          </div>
          <p style="color: #94a3b8; font-size: 0.9rem;">
            수직점근선의 이동, 대칭 중심의 궤적, 고정 정점 $(-2, 0)$, $d=2$ 축퇴 및 사분면 반전을 애니메이션으로 구현한 파이썬 스크립트입니다.
          </p>
          <pre id="manimPre17" style="background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 18px; color: #e2e8f0; font-family: 'Consolas', monospace; font-size: 0.85rem; max-height: 500px; overflow-y: auto; line-height: 1.5;"><code>__MANIM_CODE__</code></pre>
        </div>
      </div>

      <!-- TIMELINE CAPTURE CARDS -->
      <div class="card" style="margin-bottom: 40px;">
        <h2 style="color: #fbbf24; display: flex; align-items: center; gap: 10px;">
          <span>🎬</span> 타임라인별 핵심 화면 &amp; Algeomath 캡처 해설 (10장)
        </h2>
        <p style="color: #94a3b8; margin-bottom: 25px;">
          46초 애니메이션 영상을 10장의 고화질 프레임으로 세분화하여 분석했습니다.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
          <!-- CARD 1 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/01_algeomath_initial_setup.jpg" alt="01 초기 설정" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:02</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">01. Algeomath 인터페이스와 슬라이더</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $a=1, b=2, c=1$ 고정 후, $d$를 $[-10, 10]$ 범위에서 연속 제어하는 알지오매스 환경 세팅.
              </p>
            </div>
          </div>

          <!-- CARD 2 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/02_d_minus_10_extreme_negative.jpg" alt="02 d=-10" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:08</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">02. $d \approx -10$ (수직점근선 $x = 10$)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                수직점근선이 우측 끝 $x = 10$에 위치하며, $k = 12 > 0$으로 제1, 3사분면에 풍만한 곡선 형성.
              </p>
            </div>
          </div>

          <!-- CARD 3 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/03_d_minus_6_approaching_center.jpg" alt="03 d=-6" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:14</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">03. $d \approx -6$ (수직점근선 $x = 6$)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                점근선 교점이 수평선 $y=1$을 타고 좌측으로 점진 이동하며 곡선이 점근선 쪽으로 점차 수축.
              </p>
            </div>
          </div>

          <!-- CARD 4 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/04_d_minus_2_near_origin.jpg" alt="04 d=-2" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:18</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">04. $d \approx -2$ (수직점근선 $x = 2$)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                수직점근선이 원점 근방으로 접근하며 $y$절편이 음수 방향으로 가파르게 내려감.
              </p>
            </div>
          </div>

          <!-- CARD 5 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/05_d_zero_reciprocal_hyperbola.jpg" alt="05 d=0" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:22</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">05. $d = 0$ (수직점근선이 $y$축 일치)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $y = 1 + \frac{2}{x}$ 형태가 되어 수직점근선이 정확히 $y$축($x=0$)과 일치하는 순간.
              </p>
            </div>
          </div>

          <!-- CARD 6 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/06_d_approaching_2_critical_point.jpg" alt="06 d=1.7" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:24</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">06. $d \approx 1.7$ (임계점 $d=2$ 직전)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $k = 2 - d = 0.3$으로 0에 근접하며 쌍곡선이 점근선 교점 쪽으로 극도로 뾰족하게 수축.
              </p>
            </div>
          </div>

          <!-- CARD 7 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/07_d_flipped_quadrants_sign_change.jpg" alt="07 d=2.2" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:25</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">07. $d \approx 2.2$ (사분면 위치 대반전!)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $d=2$ 축퇴(직선화)를 통과하자마자 $k < 0$이 되어 제2, 4사분면으로 쌍곡선이 전격 뒤집힘!
              </p>
            </div>
          </div>

          <!-- CARD 8 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/08_d_plus_5_asymptote_moving_left.jpg" alt="08 d=5" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:27</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">08. $d \approx 5$ (수직점근선 $x = -5$)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $k = -3$이 되어 곡선이 다시 벌어지며, 정점 $(-2, 0)$을 확연히 지나는 모습 관측.
              </p>
            </div>
          </div>

          <!-- CARD 9 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/09_d_plus_8_asymptote_far_left.jpg" alt="09 d=8" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:33</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">09. $d \approx 8$ (수직점근선 $x = -8$)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                수직점근선이 좌측 깊숙이 이동하면서 대칭 중심 $(-8, 1)$과 완벽한 점대칭 곡선 유지.
              </p>
            </div>
          </div>

          <!-- CARD 10 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v17/10_d_plus_10_extreme_positive.jpg" alt="10 d=10" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #fbbf24; font-size: 0.75rem;">00:38</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">10. $d \approx 10$ (좌측 극단 도달 및 반전)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $x = -10$에 도달한 후 다시 왕복 운동을 시작하며 전체 애니메이션의 기하학적 대칭성 완성.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
'''

    lecture17_html = lecture17_template.replace('__MANIM_CODE__', escaped_manim)

    # Insert lecture17View before lecture16View
    idx_lec16 = html.find('<div id="lecture16View"')
    if idx_lec16 != -1:
        html = html[:idx_lec16] + lecture17_html + '\n' + html[idx_lec16:]
        print("Inserted lecture17View before lecture16View.")

    # 4. Insert Lecture 17 JavaScript
    js_code_17 = '''
    // ==============================================================
    // JAVASCRIPT FOR LECTURE 17 (RATIONAL FUNCTION D VARIATION: ALGEOMATH)
    // ==============================================================
    let currentD17 = -2.0;
    let animRunning17 = false;
    let animDirection17 = 1; // 1: increasing, -1: decreasing
    let animTimer17 = null;

    function setD17(val) {
      currentD17 = parseFloat(val);
      const slider = document.getElementById("sliderD17");
      if (slider) slider.value = currentD17;
      updateL17();
    }

    function updateFromSlider17(val) {
      currentD17 = parseFloat(val);
      updateL17();
    }

    function toggleAnim17() {
      animRunning17 = !animRunning17;
      const btn = document.getElementById("btnAnimToggle17");
      if (animRunning17) {
        if (btn) {
          btn.innerText = "⏸ 애니메이션 일시정지";
          btn.style.background = "#f43f5e";
          btn.style.color = "#fff";
        }
        runAnimLoop17();
      } else {
        if (btn) {
          btn.innerText = "▶ 자동 애니메이션 (왕복)";
          btn.style.background = "#fbbf24";
          btn.style.color = "#0f172a";
        }
        if (animTimer17) {
          cancelAnimationFrame(animTimer17);
          animTimer17 = null;
        }
      }
    }

    function runAnimLoop17() {
      if (!animRunning17) return;

      currentD17 += animDirection17 * 0.08;
      if (currentD17 >= 10.0) {
        currentD17 = 10.0;
        animDirection17 = -1;
      } else if (currentD17 <= -10.0) {
        currentD17 = -10.0;
        animDirection17 = 1;
      }

      const slider = document.getElementById("sliderD17");
      if (slider) slider.value = currentD17;
      updateL17();

      animTimer17 = requestAnimationFrame(runAnimLoop17);
    }

    function updateL17() {
      const d = currentD17;
      const k = 2 - d;
      const isDegenerate = Math.abs(k) < 0.05;

      const labelD = document.getElementById("labelD17");
      if (labelD) labelD.innerText = d.toFixed(1);

      const bannerDeg = document.getElementById("bannerDegeneracy17");
      if (bannerDeg) bannerDeg.style.display = isDegenerate ? "inline-block" : "none";

      const statStd = document.getElementById("statStdEq17");
      const statAsym = document.getElementById("statAsym17");
      const statPts = document.getElementById("statPts17");
      const statQuad = document.getElementById("statQuad17");

      if (statStd) {
        if (isDegenerate) {
          statStd.innerText = "y = 1 (x ≠ -2)";
        } else {
          const signStr = k >= 0 ? `+ ${k.toFixed(1)}` : `- ${Math.abs(k).toFixed(1)}`;
          const dStr = d >= 0 ? `+ ${d.toFixed(1)}` : `- ${Math.abs(d).toFixed(1)}`;
          statStd.innerText = `y = 1 ${signStr} / (x ${dStr})`;
        }
      }

      if (statAsym) {
        statAsym.innerText = `x = ${(-d).toFixed(1)},  y = 1.0 (고정)`;
      }

      if (statPts) {
        statPts.innerText = `중심 (${(-d).toFixed(1)}, 1), 정점 (-2, 0)`;
      }

      if (statQuad) {
        if (isDegenerate) {
          statQuad.innerText = "k = 0.0 (쌍곡선 축퇴 -> 직선!)";
          statQuad.style.color = "#f43f5e";
        } else if (k > 0) {
          statQuad.innerText = `k = ${k.toFixed(1)} > 0 (1, 3사분면)`;
          statQuad.style.color = "#38bdf8";
        } else {
          statQuad.innerText = `k = ${k.toFixed(1)} < 0 (2, 4사분면 반전!)`;
          statQuad.style.color = "#c084fc";
        }
      }

      renderCanvasL17();
    }

    function renderCanvasL17() {
      const canvas = document.getElementById("canvasRational17");
      if (!canvas) return;
      const ctx = canvas.getContext("2d");
      const w = canvas.width;
      const h = canvas.height;

      ctx.clearRect(0, 0, w, h);

      // Coordinate scaling
      const xMin = -15, xMax = 15;
      const yMin = -10, yMax = 10;

      function toScreenX(x) {
        return (x - xMin) / (xMax - xMin) * w;
      }
      function toScreenY(y) {
        return h - (y - yMin) / (yMax - yMin) * h;
      }

      const d = currentD17;
      const k = 2 - d;
      const asymX = -d;
      const asymY = 1.0;
      const isDegenerate = Math.abs(k) < 0.05;

      // Draw Grid lines
      ctx.strokeStyle = "rgba(148, 163, 184, 0.12)";
      ctx.lineWidth = 1;
      for (let x = -14; x <= 14; x += 2) {
        ctx.beginPath();
        ctx.moveTo(toScreenX(x), 0);
        ctx.lineTo(toScreenX(x), h);
        ctx.stroke();
      }
      for (let y = -8; y <= 8; y += 2) {
        ctx.beginPath();
        ctx.moveTo(0, toScreenY(y));
        ctx.lineTo(w, toScreenY(y));
        ctx.stroke();
      }

      // Draw Axes
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
      ctx.lineWidth = 1.8;

      // X axis (y = 0)
      ctx.beginPath();
      ctx.moveTo(0, toScreenY(0));
      ctx.lineTo(w, toScreenY(0));
      ctx.stroke();

      // Y axis (x = 0)
      ctx.beginPath();
      ctx.moveTo(toScreenX(0), 0);
      ctx.lineTo(toScreenX(0), h);
      ctx.stroke();

      // Axis Labels
      ctx.fillStyle = "#94a3b8";
      ctx.font = "bold 12px 'Consolas', monospace";
      ctx.fillText("x", w - 20, toScreenY(0) + 16);
      ctx.fillText("y", toScreenX(0) + 10, 20);
      ctx.fillText("O", toScreenX(0) - 15, toScreenY(0) + 16);

      // Draw Fixed Horizontal Asymptote: y = 1 (Green Dashed)
      ctx.strokeStyle = "#4ade80";
      ctx.setLineDash([5, 5]);
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(0, toScreenY(1));
      ctx.lineTo(w, toScreenY(1));
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#4ade80";
      ctx.font = "bold 12px 'Consolas', monospace";
      ctx.fillText("수평점근선 y = 1", w - 140, toScreenY(1) - 8);

      // Draw Dynamic Vertical Asymptote: x = -d (Yellow Dashed)
      if (asymX >= xMin && asymX <= xMax) {
        ctx.strokeStyle = "#fbbf24";
        ctx.setLineDash([5, 5]);
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(toScreenX(asymX), 0);
        ctx.lineTo(toScreenX(asymX), h);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#fbbf24";
        ctx.fillText(`수직점근선 x = ${asymX.toFixed(1)}`, toScreenX(asymX) + 8, 30);
      }

      // Draw Rational Function Curve
      ctx.strokeStyle = isDegenerate ? "#f43f5e" : (k > 0 ? "#38bdf8" : "#c084fc");
      ctx.lineWidth = 3;

      if (isDegenerate) {
        // Line y = 1 with puncture at (-2, 1)
        ctx.beginPath();
        ctx.moveTo(0, toScreenY(1));
        ctx.lineTo(w, toScreenY(1));
        ctx.stroke();

        // Puncture dot at (-2, 1)
        const puncX = toScreenX(-2);
        const puncY = toScreenY(1);
        ctx.fillStyle = "#060913";
        ctx.beginPath();
        ctx.arc(puncX, puncY, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#f43f5e";
        ctx.lineWidth = 2.5;
        ctx.stroke();

        ctx.fillStyle = "#f43f5e";
        ctx.font = "bold 12px 'Consolas', monospace";
        ctx.fillText("펑크 (-2, 1)", puncX - 35, puncY - 14);
      } else {
        // Left Branch: x < asymX
        ctx.beginPath();
        let started = false;
        const step = 0.05;
        for (let x = xMin; x < asymX - 0.08; x += step) {
          const y = 1 + k / (x + d);
          if (y >= yMin - 15 && y <= yMax + 15) {
            const sx = toScreenX(x);
            const sy = toScreenY(y);
            if (!started) {
              ctx.moveTo(sx, sy);
              started = true;
            } else {
              ctx.lineTo(sx, sy);
            }
          }
        }
        ctx.stroke();

        // Right Branch: x > asymX
        ctx.beginPath();
        started = false;
        for (let x = asymX + 0.08; x <= xMax; x += step) {
          const y = 1 + k / (x + d);
          if (y >= yMin - 15 && y <= yMax + 15) {
            const sx = toScreenX(x);
            const sy = toScreenY(y);
            if (!started) {
              ctx.moveTo(sx, sy);
              started = true;
            } else {
              ctx.lineTo(sx, sy);
            }
          }
        }
        ctx.stroke();
      }

      // Draw Center of Symmetry Dot: (-d, 1)
      if (asymX >= xMin && asymX <= xMax) {
        const cxScr = toScreenX(asymX);
        const cyScr = toScreenY(1);
        ctx.fillStyle = "#fbbf24";
        ctx.beginPath();
        ctx.arc(cxScr, cyScr, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = "#fbbf24";
        ctx.font = "bold 11px sans-serif";
        ctx.fillText(`대칭중심 (${asymX.toFixed(1)}, 1)`, cxScr + 8, cyScr + 18);
      }

      // Draw Fixed Point: (-2, 0)
      const fixX = toScreenX(-2);
      const fixY = toScreenY(0);
      ctx.fillStyle = "#f43f5e";
      ctx.beginPath();
      ctx.arc(fixX, fixY, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = "#f43f5e";
      ctx.font = "bold 12px 'Consolas', monospace";
      ctx.fillText("고정 정점 (-2, 0)", fixX - 45, fixY + 22);
    }

    function switchL17Tab(tabIdx) {
      for (let i = 1; i <= 6; i++) {
        const btn = document.getElementById(`tabBtnL17_${i}`);
        const content = document.getElementById(`tabL17_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise();
      }
    }

    function copyManimCode17() {
      const codeEl = document.querySelector("#manimPre17 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL17() {
      updateL17();
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise();
      }
    }
'''

    # Insert Lecture 17 JS before Lecture 16 JS
    idx_js16 = html.find('// ==============================================================')
    if idx_js16 != -1:
        html = html[:idx_js16] + js_code_17 + '\n' + html[idx_js16:]
        print("Inserted Lecture 17 JavaScript.")

    # 5. Update setLecture loop from 16 to 17
    html = html.replace('for (let i = 1; i <= 16; i++)', 'for (let i = 1; i <= 17; i++)')
    print("Updated setLecture loop to 17.")

    # Add num === 17 render handler
    old_l16_check = 'if (num === 16) setTimeout(renderL16, 50);'
    new_l17_check = 'if (num === 17) setTimeout(renderL17, 50);\n      else if (num === 16) setTimeout(renderL16, 50);'
    html = html.replace(old_l16_check, new_l17_check, 1)
    print("Added num === 17 render handler to setLecture.")

    # Update window load handler
    html = html.replace('setLecture(16);', 'setLecture(17);')
    html = html.replace('setTimeout(renderL16, 200);', 'setTimeout(renderL17, 200);')
    print("Updated window load handler to initialize Lecture 17.")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with Lecture 17!")

if __name__ == '__main__':
    main()
