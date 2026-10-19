# -*- coding: utf-8 -*-
"""
Script to build and inject Lecture 18 into index.html
Lecture: [GSP5 무작정 따라하기] #27. 무리함수의 그래프
Instructor: 수학귀신 (GSP5 공학수학)
YouTube Video: https://youtu.be/GBCDXfQ8rIo
"""

import os
import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code for tab
    with open('square_root_function_gsp_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()

    # 1. Update Switcher Bar: Add btnLec18 as active, remove active from btnLec17
    if 'id="btnLec18"' not in html:
        old_btn17 = '<button class="lecture-btn active" id="btnLec17" onclick="setLecture(17)">'
        if old_btn17 in html:
            new_btn_block = '''<button class="lecture-btn active" id="btnLec18" onclick="setLecture(18)">
          무리함수 GSP5 (수학귀신)
        </button>
        <button class="lecture-btn" id="btnLec17" onclick="setLecture(17)">'''
            html = html.replace(old_btn17, new_btn_block, 1)
            print("Added btnLec18 to switcher bar.")
        else:
            old_btn17_alt = '<button class="lecture-btn" id="btnLec17" onclick="setLecture(17)">'
            if old_btn17_alt in html:
                new_btn_block = '''<button class="lecture-btn active" id="btnLec18" onclick="setLecture(18)">
          무리함수 GSP5 (수학귀신)
        </button>
        <button class="lecture-btn" id="btnLec17" onclick="setLecture(17)">'''
                html = html.replace(old_btn17_alt, new_btn_block, 1)
                print("Added btnLec18 to switcher bar (alt).")

    # Update captured_summary button label
    html = html.replace('📸 사진 1~17 핵심 전용 페이지', '📸 사진 1~18 핵심 전용 페이지')

    # 2. Hide lecture17View if active
    if '<div id="lecture17View">' in html:
        html = html.replace('<div id="lecture17View">', '<div id="lecture17View" style="display: none;">', 1)
        print("Set lecture17View to display: none.")

    # 3. Create Lecture 18 View HTML
    escaped_manim = (manim_code
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))

    lecture18_template = '''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 18 (SQUARE ROOT FUNCTION GSP5: MATH GHOST) -->
    <!-- ============================================================== -->
    <div id="lecture18View">
      <header>
        <div class="badge-pill" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8; box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);">
          ⚡ 제18강 · 수학귀신 선생님 (GSP5 무작정 따라하기 #27)
        </div>
        <h1 style="background: linear-gradient(135deg, #38bdf8 0%, #ec4899 50%, #facc15 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          무리함수 $y = \\sqrt{a(x-p)} + q$의 그래프와 기하학적 성질
        </h1>
        <p class="subtitle" style="max-width: 900px; margin: 0 auto; line-height: 1.7; color: #cbd5e1;">
          "무리함수의 곡선은 왜 2차 포물선($y=x^2$)의 누운 반쪽일까?"<br>
          GSP5(The Geometer's Sketchpad) 공학도구로 직접 작도하고 탐구하는 무리함수의 모든 것:<br>
          <strong>매개변수 $a$의 부호와 폭(Dilation) · 시작점(꼭짓점 $(p, q)$)의 평행이동 · 4개 사분면 분기 · 역함수($y=x$ 대칭)</strong>을 완벽 시각화합니다.
        </p>
      </header>

      <!-- TOP SUMMARY BANNER -->
      <div style="background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(236, 72, 153, 0.1), rgba(15, 23, 42, 0.95)); border: 2px solid rgba(56, 189, 248, 0.4); border-radius: 20px; padding: 26px; margin-bottom: 35px; box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5);">
        <div style="font-size: 0.95rem; font-weight: 700; color: #38bdf8; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; text-align: center;">
          ⭐ 무리함수 표준형 핵심 기하 공식: $y = \\pm\\sqrt{a(x-p)} + q$
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; text-align: center; margin-top: 15px;">
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(236, 72, 153, 0.3);">
            <div style="color: #ec4899; font-weight: bold; font-size: 0.85rem;">1. 시작점 (Vertex / 시점)</div>
            <div style="color: #fff; font-size: 1.1rem; font-family: monospace; margin-top: 3px;">$(p, q)$에서 출발</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(56, 189, 248, 0.3);">
            <div style="color: #38bdf8; font-weight: bold; font-size: 0.85rem;">2. 매개변수 $a$의 부호</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$a>0$(우상향) / $a<0$(좌상향)</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(250, 204, 21, 0.3);">
            <div style="color: #facc15; font-weight: bold; font-size: 0.85rem;">3. 곡선의 폭 (벌어짐)</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$|a|$ 커질수록 폭(증가량) 확대</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(168, 85, 247, 0.3);">
            <div style="color: #c084fc; font-weight: bold; font-size: 0.85rem;">4. 기하학적 본질 (역함수)</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">포물선 $x=y^2$의 $y=x$ 대칭 반쪽</div>
          </div>
        </div>
      </div>

      <!-- MAIN INTERACTIVE LAB: GSP5 SQUARE ROOT FUNCTION SIMULATOR -->
      <div class="card" style="margin-bottom: 40px; border-color: rgba(56, 189, 248, 0.4); box-shadow: 0 10px 30px rgba(56, 189, 248, 0.15);">
        <h2 style="color: #38bdf8; display: flex; align-items: center; gap: 10px;">
          <span>📐</span> GSP5 스타일 무리함수 실시간 동적 실험실
        </h2>
        <p style="color: #94a3b8; line-height: 1.6; margin-bottom: 20px;">
          영상 속 GSP5 작도 원리를 그대로 웹 캔버스에 구현했습니다. 매개변수 $a, p, q$ 슬라이더를 조작하여 시작점 이동과 곡선 개형의 변화를 실시간으로 확인해보세요.
        </p>

        <!-- PRESET BUTTONS -->
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;">
          <span style="font-size: 0.85rem; color: #94a3b8; align-self: center; margin-right: 4px;">🎯 프리셋:</span>
          <button class="btn btn-secondary" onclick="applyPreset18(1, 0, 0, 1)" style="font-size: 0.8rem; padding: 6px 12px;">기본형: y = √x</button>
          <button class="btn btn-secondary" onclick="applyPreset18(1, 0, 3, 1)" style="font-size: 0.8rem; padding: 6px 12px;">y축 이동: y = √x + 3</button>
          <button class="btn btn-secondary" onclick="applyPreset18(1, 3, 0, 1)" style="font-size: 0.8rem; padding: 6px 12px;">x축 이동: y = √(x-3)</button>
          <button class="btn btn-secondary" onclick="applyPreset18(-2, 0, 0, 1)" style="font-size: 0.8rem; padding: 6px 12px;">음수 a: y = √(-2x)</button>
          <button class="btn btn-secondary" onclick="applyPreset18(2, 2, 1, 1)" style="font-size: 0.8rem; padding: 6px 12px;">표준형: y = √(2(x-2)) + 1</button>
          <button class="btn btn-secondary" onclick="applyPreset18(1, -2, 2, -1)" style="font-size: 0.8rem; padding: 6px 12px;">하반부: y = -√(x+2) + 2</button>
          <button class="btn btn-primary" id="btnAnim18" onclick="toggleAnimation18()" style="font-size: 0.8rem; padding: 6px 14px; background: #38bdf8; color: #0f172a; font-weight: bold;">
            ▶ a 동적 스위프 애니메이션
          </button>
        </div>

        <div style="display: grid; grid-template-columns: 320px 1fr; gap: 24px; align-items: start;">
          <!-- CONTROLS COLUMN -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px;">
            <!-- Formula Display -->
            <div style="background: #030712; border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 8px; padding: 12px; margin-bottom: 16px; text-align: center;">
              <div style="color: #94a3b8; font-size: 0.75rem; letter-spacing: 1px;">현재 함수식</div>
              <div id="dispFormula18" style="font-size: 1.15rem; font-weight: bold; color: #38bdf8; margin: 4px 0; font-family: monospace;">
                y = √(1.0(x - 0.0)) + 0.0
              </div>
            </div>

            <!-- a Slider -->
            <div style="margin-bottom: 16px;">
              <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                <span style="color: #38bdf8; font-weight: bold;">매개변수 a (폭/방향):</span>
                <span id="valA18" style="color: #38bdf8; font-family: monospace; font-weight: bold;">1.0</span>
              </div>
              <input type="range" id="sliderA18" min="-5.0" max="5.0" step="0.1" value="1.0"
                     oninput="updateFromSliders18()" style="width: 100%; accent-color: #38bdf8;">
              <div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748b;">
                <span>-5 (좌상향)</span>
                <span>0 (수평선)</span>
                <span>+5 (우상향)</span>
              </div>
            </div>

            <!-- p Slider -->
            <div style="margin-bottom: 16px;">
              <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                <span style="color: #ec4899; font-weight: bold;">매개변수 p (x축 평행이동):</span>
                <span id="valP18" style="color: #ec4899; font-family: monospace; font-weight: bold;">0.0</span>
              </div>
              <input type="range" id="sliderP18" min="-6.0" max="6.0" step="0.1" value="0.0"
                     oninput="updateFromSliders18()" style="width: 100%; accent-color: #ec4899;">
              <div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748b;">
                <span>-6 (좌측 이동)</span>
                <span>0</span>
                <span>+6 (우측 이동)</span>
              </div>
            </div>

            <!-- q Slider -->
            <div style="margin-bottom: 16px;">
              <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                <span style="color: #facc15; font-weight: bold;">매개변수 q (y축 평행이동):</span>
                <span id="valQ18" style="color: #facc15; font-family: monospace; font-weight: bold;">0.0</span>
              </div>
              <input type="range" id="sliderQ18" min="-4.0" max="4.0" step="0.1" value="0.0"
                     oninput="updateFromSliders18()" style="width: 100%; accent-color: #facc15;">
              <div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748b;">
                <span>-4 (하단 이동)</span>
                <span>0</span>
                <span>+4 (상단 이동)</span>
              </div>
            </div>

            <!-- Sign Toggle (Upper / Lower branch) -->
            <div style="margin-bottom: 16px;">
              <div style="font-size: 0.85rem; color: #cbd5e1; margin-bottom: 6px; font-weight: bold;">근호 앞 부호 (상/하 분기):</div>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
                <button id="btnSignPos18" class="btn btn-secondary active" onclick="setSign18(1)" style="font-size: 0.8rem; padding: 6px;">
                  +√... (상반부)
                </button>
                <button id="btnSignNeg18" class="btn btn-secondary" onclick="setSign18(-1)" style="font-size: 0.8rem; padding: 6px;">
                  -√... (하반부)
                </button>
              </div>
            </div>

            <!-- Visual Guides Checkboxes -->
            <div style="border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 12px; margin-top: 12px;">
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.8rem; color: #cbd5e1; margin-bottom: 8px; cursor: pointer;">
                <input type="checkbox" id="chkInverse18" onchange="updateL18()" checked>
                <span>포물선 역함수 원형 ($x=y^2$ 및 $y=x$) 표시</span>
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.8rem; color: #cbd5e1; margin-bottom: 8px; cursor: pointer;">
                <input type="checkbox" id="chkVertexGuide18" onchange="updateL18()" checked>
                <span>시작점 $(p, q)$ 안내 점선 표시</span>
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.8rem; color: #cbd5e1; cursor: pointer;">
                <input type="checkbox" id="chkDomainRange18" onchange="updateL18()" checked>
                <span>정의역 및 치역 영역 음영 표시</span>
              </label>
            </div>
          </div>

          <!-- CANVAS & READOUT COLUMN -->
          <div>
            <div style="position: relative; background: #030712; border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 12px; overflow: hidden; box-shadow: inset 0 0 40px rgba(0,0,0,0.8);">
              <canvas id="canvasL18" width="720" height="480" style="display: block; width: 100%; height: auto;"></canvas>
            </div>

            <!-- Real-time Status Badges -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 14px;">
              <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(236, 72, 153, 0.3); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 0.75rem; color: #ec4899;">시작점 (꼭짓점)</div>
                <div id="statVertex18" style="font-size: 0.95rem; font-weight: bold; color: #fff; margin-top: 2px;">(0.0, 0.0)</div>
              </div>
              <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 0.75rem; color: #38bdf8;">정의역 (Domain)</div>
                <div id="statDomain18" style="font-size: 0.95rem; font-weight: bold; color: #fff; margin-top: 2px;">x ≥ 0.0</div>
              </div>
              <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(250, 204, 21, 0.3); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 0.75rem; color: #facc15;">치역 (Range)</div>
                <div id="statRange18" style="font-size: 0.95rem; font-weight: bold; color: #fff; margin-top: 2px;">y ≥ 0.0</div>
              </div>
              <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 0.75rem; color: #c084fc;">진행 사분면</div>
                <div id="statQuad18" style="font-size: 0.95rem; font-weight: bold; color: #fff; margin-top: 2px;">제1사분면 (우상향)</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- SIX CONCEPT TABS -->
      <div class="card" style="margin-bottom: 40px;">
        <h2 style="color: #38bdf8; display: flex; align-items: center; gap: 10px;">
          <span>📚</span> 무리함수 핵심 개념 완벽 마스터 (6대 테마)
        </h2>

        <div class="tabs" style="margin: 20px 0;">
          <button class="tab-btn active" id="tabBtnL18_1" onclick="switchL18Tab(1)">1. 포물선 역함수 원리</button>
          <button class="tab-btn" id="tabBtnL18_2" onclick="switchL18Tab(2)">2. 평행이동의 기초</button>
          <button class="tab-btn" id="tabBtnL18_3" onclick="switchL18Tab(3)">3. GSP5 동적 작도법</button>
          <button class="tab-btn" id="tabBtnL18_4" onclick="switchL18Tab(4)">4. 매개변수 a, p, q 역할</button>
          <button class="tab-btn" id="tabBtnL18_5" onclick="switchL18Tab(5)">5. 4개 사분면 분기표</button>
          <button class="tab-btn" id="tabBtnL18_6" onclick="switchL18Tab(6)">6. 수능/내신 실전 킬러</button>
        </div>

        <!-- TAB 1 -->
        <div id="tabL18_1" class="tab-content" style="display: block;">
          <h3 style="color: #38bdf8;">1. 무리함수의 기하학적 정체: 포물선의 반쪽 ($y=x$ 대칭 역함수)</h3>
          <p style="line-height: 1.7; color: #cbd5e1;">
            영상 01:10에서 강사가 강조하듯, $y = \\sqrt{x}$의 그래프는 전혀 새로운 곡선이 아니라 <strong>2차 포물선 $y = x^2$ ($x \\ge 0$)을 직선 $y = x$에 대해 대칭이동시킨 곡선</strong>입니다.
          </p>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 18px; border-left: 4px solid #38bdf8; border-radius: 8px; margin: 16px 0;">
            <div style="font-weight: bold; color: #38bdf8; margin-bottom: 8px;">대수적 증명:</div>
            $$y = \\sqrt{x} \\quad (x \\ge 0, \\; y \\ge 0) \\iff y^2 = x \\iff x = y^2$$
            이차함수 $y = x^2$의 역함수를 구하면 $x = y^2$가 되는데, 이는 하나의 $x$에 대해 $y = \\pm\\sqrt{x}$ 두 개가 대응하므로 함수가 되지 못합니다.<br>
            따라서 **함수의 정의(수직선 판정법, Vertical Line Test)**를 만족하기 위해 상반부($y \\ge 0$)인 $y = +\\sqrt{x}$만을 취한 것이 바로 무리함수의 본질입니다.
          </div>
        </div>

        <!-- TAB 2 -->
        <div id="tabL18_2" class="tab-content" style="display: none;">
          <h3 style="color: #38bdf8;">2. 기본형의 평행이동: $y = \\sqrt{x} + 3$ 및 $y = \\sqrt{x - 3}$</h3>
          <p style="line-height: 1.7; color: #cbd5e1;">
            강의 전반부에서 다루는 직관적인 평행이동 예시입니다:
          </p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0;">
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: 10px; border: 1px solid rgba(250, 204, 21, 0.3);">
              <h4 style="color: #facc15; margin-top: 0;">① y축 평행이동: $y = \\sqrt{x} + 3$</h4>
              <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                • 식 바깥에 $+3$을 더함<br>
                • 모든 점의 $y$좌표가 $+3$만큼 수직 상승<br>
                • 시작점: $(0, 0) \\to (0, 3)$<br>
                • 치역: $y \\ge 3$
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: 10px; border: 1px solid rgba(236, 72, 153, 0.3);">
              <h4 style="color: #ec4899; margin-top: 0;">② x축 평행이동: $y = \\sqrt{x - 3}$</h4>
              <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                • $x$ 대신 $x - 3$을 대입<br>
                • 근호 내부 $\\ge 0$이므로 $x - 3 \\ge 0 \\implies x \\ge 3$<br>
                • 시작점: $(0, 0) \\to (3, 0)$<br>
                • 정의역: $x \\ge 3$
              </p>
            </div>
          </div>
        </div>

        <!-- TAB 3 -->
        <div id="tabL18_3" class="tab-content" style="display: none;">
          <h3 style="color: #38bdf8;">3. GSP5 동적 기하 작도법 (수학귀신 비법 노하우)</h3>
          <p style="line-height: 1.7; color: #cbd5e1;">
            영상 03:00~05:40에서 시연된 GSP5 고유의 매개변수 생성 메커니즘 5단계입니다:
          </p>
          <ol style="line-height: 1.8; color: #cbd5e1; padding-left: 20px;">
            <li><strong>x축 위에 세 점 생성</strong>: 매개변수 세 개($a, p, q$)를 위해 적당한 간격으로 점을 배치합니다.</li>
            <li><strong>수선 작도</strong>: Construct $\\to$ Perpendicular Lines로 각 점을 지나는 수선을 세웁니다.</li>
            <li><strong>수선 위의 점 지정</strong>: Construct $\\to$ Point On Perpendicular Line으로 점을 올리고 위아래로 움직이게 만듭니다.</li>
            <li><strong>y좌표 측정 및 변수 라벨링</strong>: Measure $\\to$ Y-Coordinate로 값을 측정하고 이름을 각각 $a, p, q$로 수정합니다.</li>
            <li><strong>함수 입력창</strong>: Graph $\\to$ Plot New Function에서 `sqrt(a * (x - p)) + q`를 입력합니다. (단, $+q$가 근호 밖으로 빠져나오도록 괄호와 커서 위치를 확인하는 것이 결정적입니다!)</li>
          </ol>
        </div>

        <!-- TAB 4 -->
        <div id="tabL18_4" class="tab-content" style="display: none;">
          <h3 style="color: #38bdf8;">4. 표준형 $y = \\sqrt{a(x-p)} + q$ 매개변수 역할 총정리</h3>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 16px;">
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: 10px; border-top: 4px solid #38bdf8;">
              <h4 style="color: #38bdf8; margin-top: 0;">매개변수 a (방향 & 폭)</h4>
              <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
                • $a > 0$: 오른쪽 방향 (우상향, $x \\ge p$)<br>
                • $a < 0$: 왼쪽 방향 (좌상향, $x \\le p$)<br>
                • $|a|$ 확대: $y$축 방향으로 급격히 솟구치며 곡선의 폭(증가량) 확대
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: 10px; border-top: 4px solid #ec4899;">
              <h4 style="color: #ec4899; margin-top: 0;">매개변수 p (좌우 이동)</h4>
              <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
                • 시작점(꼭짓점)의 $x$좌표 결정<br>
                • $x$축 방향으로 $p$만큼 평행이동<br>
                • 정의역의 경계값 결정 ($x=p$)
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: 10px; border-top: 4px solid #facc15;">
              <h4 style="color: #facc15; margin-top: 0;">매개변수 q (상하 이동)</h4>
              <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
                • 시작점(꼭짓점)의 $y$좌표 결정<br>
                • $y$축 방향으로 $q$만큼 평행이동<br>
                • 치역의 경계값 결정 ($y=q$)
              </p>
            </div>
          </div>
        </div>

        <!-- TAB 5 -->
        <div id="tabL18_5" class="tab-content" style="display: none;">
          <h3 style="color: #38bdf8;">5. 무리함수 4가지 사분면 분기표 (4 Quadrant Branches)</h3>
          <div style="overflow-x: auto; margin-top: 14px;">
            <table style="width: 100%; border-collapse: collapse; text-align: center; font-size: 0.9rem;">
              <thead>
                <tr style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; border-bottom: 2px solid rgba(56, 189, 248, 0.4);">
                  <th style="padding: 10px;">함수식</th>
                  <th>정의역 ($x$)</th>
                  <th>치역 ($y$)</th>
                  <th>시작점</th>
                  <th>진행 방향</th>
                  <th>증감</th>
                  <th>대칭 관계 ($y=\\sqrt{x}$ 기준)</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
                  <td style="padding: 10px; font-weight: bold; color: #38bdf8;">$y = +\\sqrt{+x}$</td>
                  <td>$x \\ge 0$</td>
                  <td>$y \\ge 0$</td>
                  <td>$(0, 0)$</td>
                  <td>제1사분면 (우상향)</td>
                  <td>증가</td>
                  <td>기본형 (기준)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
                  <td style="padding: 10px; font-weight: bold; color: #ec4899;">$y = +\\sqrt{-x}$</td>
                  <td>$x \\le 0$</td>
                  <td>$y \\ge 0$</td>
                  <td>$(0, 0)$</td>
                  <td>제2사분면 (좌상향)</td>
                  <td>감소</td>
                  <td>$y$축 대칭 ($x \\to -x$)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
                  <td style="padding: 10px; font-weight: bold; color: #a855f7;">$y = -\\sqrt{-x}$</td>
                  <td>$x \\le 0$</td>
                  <td>$y \\le 0$</td>
                  <td>$(0, 0)$</td>
                  <td>제3사분면 (좌하향)</td>
                  <td>증가</td>
                  <td>원점 대칭 ($x \\to -x, y \\to -y$)</td>
                </tr>
                <tr>
                  <td style="padding: 10px; font-weight: bold; color: #facc15;">$y = -\\sqrt{+x}$</td>
                  <td>$x \\ge 0$</td>
                  <td>$y \\le 0$</td>
                  <td>$(0, 0)$</td>
                  <td>제4사분면 (우하향)</td>
                  <td>감소</td>
                  <td>$x$축 대칭 ($y \\to -y$)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- TAB 6 -->
        <div id="tabL18_6" class="tab-content" style="display: none;">
          <h3 style="color: #38bdf8;">6. 수능/내신 실전 킬러: 무리함수와 직선의 위치 관계</h3>
          <div style="background: rgba(244, 63, 94, 0.1); border: 1px solid rgba(244, 63, 94, 0.4); border-radius: 10px; padding: 18px; margin: 16px 0;">
            <div style="color: #f43f5e; font-weight: bold; font-size: 1rem; margin-bottom: 8px;">
              ⚠️ 수능 단골 함정: 판별식 $D=0$만 쓰면 무조건 틀린다! (무연근의 함정)
            </div>
            <p style="color: #cbd5e1; line-height: 1.7; font-size: 0.92rem; margin: 0;">
              무리함수 $\\sqrt{x}$와 직선 $mx+n$을 연립하여 제곱하면 $x = (mx+n)^2$이 되어 <strong>존재하지 않는 가상의 반쪽 포물선($y<0$)과의 가짜 교점(무연근)</strong>까지 모두 계산됩니다.<br>
              따라서 교점의 개수는 반드시 **1) 판별식 $D=0$ 접선**과 **2) 시작점 $(p, q)$ 통과선**이라는 두 개의 경계선을 그래프로 분할하여 판정해야 합니다.
            </p>
          </div>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 14px; text-align: center;">
            <div style="background: rgba(15, 23, 42, 0.7); padding: 12px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.1);">
              <div style="color: #38bdf8; font-weight: bold; font-size: 0.85rem;">서로 다른 2점 만남</div>
              <div style="color: #fff; font-size: 0.95rem; margin-top: 4px;">시작점 $\\le n <$ 접할 때</div>
            </div>
            <div style="background: rgba(15, 23, 42, 0.7); padding: 12px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.1);">
              <div style="color: #facc15; font-weight: bold; font-size: 0.85rem;">한 점 만남 (2가지)</div>
              <div style="color: #fff; font-size: 0.95rem; margin-top: 4px;">접할 때 ($D=0$) OR 시작점 아래</div>
            </div>
            <div style="background: rgba(15, 23, 42, 0.7); padding: 12px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.1);">
              <div style="color: #f43f5e; font-weight: bold; font-size: 0.85rem;">만나지 않음</div>
              <div style="color: #fff; font-size: 0.95rem; margin-top: 4px;">접선 위쪽 ($D < 0$)</div>
            </div>
          </div>
        </div>
      </div>

      <!-- MANIM PYTHON SCRIPT TAB -->
      <div class="card" style="margin-bottom: 40px; border-color: rgba(56, 189, 248, 0.3);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
          <h2 style="color: #38bdf8; margin: 0; display: flex; align-items: center; gap: 10px;">
            <span>🎬</span> 3Blue1Brown 스타일 Manim 애니메이션 코드
          </h2>
          <button class="btn btn-secondary" onclick="copyManimCode18()" style="font-size: 0.85rem; padding: 6px 14px;">
            📋 파이썬 코드 복사
          </button>
        </div>
        <p style="color: #94a3b8; font-size: 0.9rem; line-height: 1.6; margin-bottom: 14px;">
          포물선 $y=x^2$의 $y=x$ 대칭 변환 과정과 $a, p, q$ 매개변수 동적 추적을 3Blue1Brown 스타일로 연출한 Manim 파이썬 스크립트입니다:
        </p>
        <div style="background: #030712; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 16px; overflow-x: auto;">
          <pre id="manimPre18" style="margin: 0; font-family: 'Consolas', monospace; font-size: 0.85rem; color: #cbd5e1; line-height: 1.5;"><code>__MANIM_CODE__</code></pre>
        </div>
        <div style="margin-top: 12px; font-size: 0.8rem; color: #64748b;">
          💡 실행 명령어: <code style="color: #38bdf8; background: #0f172a; padding: 2px 6px; border-radius: 4px;">manim -pql square_root_function_gsp_manim.py SquareRootFunctionGSPScene</code>
        </div>
      </div>

      <!-- 10 TIMELINE CARDS WITH CAPTURES -->
      <div class="card" style="margin-bottom: 40px;">
        <h2 style="color: #38bdf8; display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
          <span>📸</span> 강의 타임라인 10대 핵심 장면 고화질 캡처 (수학귀신 GSP5)
        </h2>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
          <!-- Card 1 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_01_015s.jpg" alt="01 sqrt x basic" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">00:15</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">1. GSP5 시작 및 무리함수 $y = \sqrt{x}$ 작도</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                새 좌표계를 생성하고 Graph 메뉴의 Plot New Function에서 `sqrt(x)`를 입력하여 가장 기본적인 무리함수를 그립니다.
              </p>
            </div>
          </div>

          <!-- Card 2 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_02_075s.jpg" alt="02 parabola half insight" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">01:15</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">2. 포물선의 반쪽 ($y=x^2$ 역함수 대칭) 핵심 통찰</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $y = \sqrt{x}$ 곡선이 2차 포물선 $y=x^2$을 $y=x$ 대칭시켜 회전시킨 반쪽 포물선이라는 기하학적 본질을 짚어냅니다.
              </p>
            </div>
          </div>

          <!-- Card 3 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_03_140s.jpg" alt="03 vertical shift" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">02:20</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">3. y축 평행이동: $g(x) = \sqrt{x} + 3$ 수직 이동</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                식 바깥에 $+3$을 더하여 원래 그래프가 정확히 $y$축 방향으로 $3$만큼 수직 상승하는 평행이동의 원리를 확인합니다.
              </p>
            </div>
          </div>

          <!-- Card 4 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_04_200s.jpg" alt="04 horizontal shift" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">03:20</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">4. x축 평행이동: $h(x) = \sqrt{x-3}$ 수평 이동</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                괄호 안에 $x-3$을 대입하여 원래 그래프가 $x$축 양의 방향으로 $+3$만큼 수평 이동함을 보여줍니다.
              </p>
            </div>
          </div>

          <!-- Card 5 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_05_260s.jpg" alt="05 gsp param setup" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">04:20</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">5. GSP5 동적 파라미터 $a, p, q$ 작도 및 측정</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $x$축 위의 세 점과 수선을 세우고, 각 수선 위에 점을 잡아 $y$좌표를 측정한 뒤 $a, p, q$ 슬라이더로 변환합니다.
              </p>
            </div>
          </div>

          <!-- Card 6 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_06_320s.jpg" alt="06 gsp function input" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">05:20</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">6. 수식 편집기: $f(x) = \sqrt{a(x-p)} + q$ 입력</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                루트 안에 $a \cdot (x-p)$를 넣고, 커서를 괄호 바깥으로 이동시켜 $+q$를 더하는 실전 수식 입력 팁을 설명합니다.
              </p>
            </div>
          </div>

          <!-- Card 7 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_07_365s.jpg" alt="07 general form initial" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">06:05</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">7. 일반형 무리함수의 완성 ($a=1, p=0, q=0$)</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                빨간색 굵은 곡선으로 함수 그래프를 설정하고 원점 $(0, 0)$을 시점으로 하는 표준 무리함수를 준비합니다.
              </p>
            </div>
          </div>

          <!-- Card 8 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_08_380s.jpg" alt="08 param a dilation" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">06:20</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">8. 매개변수 $a$의 변화: $|a|$ 증가에 따른 폭 확대</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $a$가 커질수록 2차 포물선의 폭이 변하듯 무리함수의 벌어지는 폭과 증가 속도가 급격히 확장됨을 관찰합니다.
              </p>
            </div>
          </div>

          <!-- Card 9 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_09_395s.jpg" alt="09 param a negative flip" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">06:35</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">9. 매개변수 $a < 0$: 제2사분면 방향 대반전</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $a$가 음수가 되면 근호 안의 조건 $ax \ge 0 \implies x \le 0$이 되어 곡선이 제2사분면(좌상향)으로 반전됩니다.
              </p>
            </div>
          </div>

          <!-- Card 10 -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
            <img src="captures_v18/frame_10_415s.jpg" alt="10 param pq translation" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">06:55</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">10. 시작점 $(p, q)$ 주행 및 최종 핵심 요약</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $p$는 $x$축 평행이동, $q$는 $y$축 평행이동을 담당하여 꼭짓점 $(p, q)$가 평면 위를 이동하며 강의가 마무리됩니다.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
'''

    lecture18_html = lecture18_template.replace('__MANIM_CODE__', escaped_manim)

    # Insert lecture18View before lecture17View
    idx_lec17 = html.find('<div id="lecture17View"')
    if idx_lec17 != -1:
        html = html[:idx_lec17] + lecture18_html + '\n' + html[idx_lec17:]
        print("Inserted lecture18View before lecture17View.")

    # 4. Insert Lecture 18 JavaScript
    js_code_18 = '''
    // ==============================================================
    // JAVASCRIPT FOR LECTURE 18 (SQUARE ROOT FUNCTION GSP5: MATH GHOST)
    // ==============================================================
    let currentA18 = 1.0;
    let currentP18 = 0.0;
    let currentQ18 = 0.0;
    let currentSign18 = 1; // +1: upper branch, -1: lower branch

    let animRunning18 = false;
    let animTimer18 = null;
    let animDirA18 = 1;

    function applyPreset18(a, p, q, sign) {
      currentA18 = parseFloat(a);
      currentP18 = parseFloat(p);
      currentQ18 = parseFloat(q);
      currentSign18 = parseInt(sign);

      const sliderA = document.getElementById("sliderA18");
      const sliderP = document.getElementById("sliderP18");
      const sliderQ = document.getElementById("sliderQ18");
      if (sliderA) sliderA.value = currentA18;
      if (sliderP) sliderP.value = currentP18;
      if (sliderQ) sliderQ.value = currentQ18;

      updateSignButtons18();
      updateL18();
    }

    function setSign18(sign) {
      currentSign18 = sign;
      updateSignButtons18();
      updateL18();
    }

    function updateSignButtons18() {
      const btnPos = document.getElementById("btnSignPos18");
      const btnNeg = document.getElementById("btnSignNeg18");
      if (btnPos && btnNeg) {
        if (currentSign18 === 1) {
          btnPos.classList.add("active");
          btnNeg.classList.remove("active");
        } else {
          btnPos.classList.remove("active");
          btnNeg.classList.add("active");
        }
      }
    }

    function updateFromSliders18() {
      const sliderA = document.getElementById("sliderA18");
      const sliderP = document.getElementById("sliderP18");
      const sliderQ = document.getElementById("sliderQ18");
      if (sliderA) currentA18 = parseFloat(sliderA.value);
      if (sliderP) currentP18 = parseFloat(sliderP.value);
      if (sliderQ) currentQ18 = parseFloat(sliderQ.value);
      updateL18();
    }

    function toggleAnimation18() {
      animRunning18 = !animRunning18;
      const btn = document.getElementById("btnAnim18");
      if (animRunning18) {
        if (btn) {
          btn.innerText = "⏸ 애니메이션 일시정지";
          btn.style.background = "#ec4899";
          btn.style.color = "#fff";
        }
        runAnimLoop18();
      } else {
        if (btn) {
          btn.innerText = "▶ a 동적 스위프 애니메이션";
          btn.style.background = "#38bdf8";
          btn.style.color = "#0f172a";
        }
        if (animTimer18) {
          cancelAnimationFrame(animTimer18);
          animTimer18 = null;
        }
      }
    }

    function runAnimLoop18() {
      if (!animRunning18) return;

      currentA18 += animDirA18 * 0.04;
      if (currentA18 >= 4.0) {
        currentA18 = 4.0;
        animDirA18 = -1;
      } else if (currentA18 <= -4.0) {
        currentA18 = -4.0;
        animDirA18 = 1;
      }

      // Skip 0 smoothly
      if (Math.abs(currentA18) < 0.15) {
        currentA18 += animDirA18 * 0.2;
      }

      const sliderA = document.getElementById("sliderA18");
      if (sliderA) sliderA.value = currentA18.toFixed(1);

      updateL18();
      animTimer18 = requestAnimationFrame(runAnimLoop18);
    }

    function updateL18() {
      const a = currentA18;
      const p = currentP18;
      const q = currentQ18;
      const sign = currentSign18;

      // Update Slider Label Texts
      const elA = document.getElementById("valA18");
      const elP = document.getElementById("valP18");
      const elQ = document.getElementById("valQ18");
      if (elA) elA.innerText = a.toFixed(1);
      if (elP) elP.innerText = p.toFixed(1);
      if (elQ) elQ.innerText = q.toFixed(1);

      // Formula String
      const signStr = sign === 1 ? "" : "-";
      const aStr = a >= 0 ? `${a.toFixed(1)}` : `(${a.toFixed(1)})`;
      const pStr = p >= 0 ? `(x - ${p.toFixed(1)})` : `(x + ${Math.abs(p).toFixed(1)})`;
      const qStr = q >= 0 ? `+ ${q.toFixed(1)}` : `- ${Math.abs(q).toFixed(1)}`;
      const formulaStr = `y = ${signStr}√[${aStr}${pStr}] ${qStr}`;

      const dispFormula = document.getElementById("dispFormula18");
      if (dispFormula) dispFormula.innerText = formulaStr;

      // Status Badges
      const statVertex = document.getElementById("statVertex18");
      const statDomain = document.getElementById("statDomain18");
      const statRange = document.getElementById("statRange18");
      const statQuad = document.getElementById("statQuad18");

      if (statVertex) statVertex.innerText = `(${p.toFixed(1)}, ${q.toFixed(1)})`;
      if (statDomain) {
        if (a > 0) statDomain.innerText = `x ≥ ${p.toFixed(1)}`;
        else if (a < 0) statDomain.innerText = `x ≤ ${p.toFixed(1)}`;
        else statDomain.innerText = "전체 실수 (a=0)";
      }
      if (statRange) {
        if (sign === 1) statRange.innerText = `y ≥ ${q.toFixed(1)}`;
        else statRange.innerText = `y ≤ ${q.toFixed(1)}`;
      }
      if (statQuad) {
        if (a > 0 && sign === 1) statQuad.innerText = "제1사분면 (우상향 ↗)";
        else if (a < 0 && sign === 1) statQuad.innerText = "제2사분면 (좌상향 ↖)";
        else if (a < 0 && sign === -1) statQuad.innerText = "제3사분면 (좌하향 ↙)";
        else if (a > 0 && sign === -1) statQuad.innerText = "제4사분면 (우하향 ↘)";
        else statQuad.innerText = "수평선 y = q";
      }

      // Draw Canvas
      drawCanvasL18();
    }

    function drawCanvasL18() {
      const canvas = document.getElementById("canvasL18");
      if (!canvas) return;
      const ctx = canvas.getContext("2d");
      const W = canvas.width;
      const H = canvas.height;

      ctx.clearRect(0, 0, W, H);

      // Coordinate System
      const xMin = -7, xMax = 7;
      const yMin = -5, yMax = 5;

      function toScreenX(x) {
        return (x - xMin) / (xMax - xMin) * W;
      }
      function toScreenY(y) {
        return H - (y - yMin) / (yMax - yMin) * H;
      }

      const origX = toScreenX(0);
      const origY = toScreenY(0);

      // 1. Grid lines
      ctx.lineWidth = 1;
      ctx.strokeStyle = "rgba(255, 255, 255, 0.06)";
      for (let x = Math.ceil(xMin); x <= Math.floor(xMax); x++) {
        const sx = toScreenX(x);
        ctx.beginPath();
        ctx.moveTo(sx, 0);
        ctx.lineTo(sx, H);
        ctx.stroke();
      }
      for (let y = Math.ceil(yMin); y <= Math.floor(yMax); y++) {
        const sy = toScreenY(y);
        ctx.beginPath();
        ctx.moveTo(0, sy);
        ctx.lineTo(W, sy);
        ctx.stroke();
      }

      // 2. Axes
      ctx.lineWidth = 1.8;
      ctx.strokeStyle = "rgba(255, 255, 255, 0.35)";
      // X axis
      ctx.beginPath();
      ctx.moveTo(0, origY);
      ctx.lineTo(W, origY);
      ctx.stroke();
      // Y axis
      ctx.beginPath();
      ctx.moveTo(origX, 0);
      ctx.lineTo(origX, H);
      ctx.stroke();

      // Axis Ticks & Numbers
      ctx.fillStyle = "rgba(255, 255, 255, 0.4)";
      ctx.font = "11px 'Consolas', monospace";
      for (let x = -6; x <= 6; x += 2) {
        if (x === 0) continue;
        const sx = toScreenX(x);
        ctx.fillText(x.toString(), sx - 4, origY + 15);
      }
      for (let y = -4; y <= 4; y += 2) {
        if (y === 0) continue;
        const sy = toScreenY(y);
        ctx.fillText(y.toString(), origX + 6, sy + 4);
      }
      ctx.fillText("0", origX - 12, origY + 14);
      ctx.fillText("x", W - 15, origY - 6);
      ctx.fillText("y", origX + 8, 16);

      const a = currentA18;
      const p = currentP18;
      const q = currentQ18;
      const sign = currentSign18;

      const chkInverse = document.getElementById("chkInverse18")?.checked;
      const chkVertexGuide = document.getElementById("chkVertexGuide18")?.checked;
      const chkDomainRange = document.getElementById("chkDomainRange18")?.checked;

      // 3. Domain & Range Shading
      if (chkDomainRange && Math.abs(a) > 0.05) {
        ctx.fillStyle = "rgba(56, 189, 248, 0.06)";
        const pScr = toScreenX(p);
        const qScr = toScreenY(q);
        if (a > 0) {
          if (sign === 1) {
            ctx.fillRect(pScr, 0, W - pScr, qScr);
          } else {
            ctx.fillRect(pScr, qScr, W - pScr, H - qScr);
          }
        } else {
          if (sign === 1) {
            ctx.fillRect(0, 0, pScr, qScr);
          } else {
            ctx.fillRect(0, qScr, pScr, H - qScr);
          }
        }
      }

      // 4. Parabola & y=x Inverse overlay
      if (chkInverse) {
        // Line y = x
        ctx.strokeStyle = "rgba(148, 163, 184, 0.35)";
        ctx.lineWidth = 1.2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(toScreenX(xMin), toScreenY(xMin));
        ctx.lineTo(toScreenX(xMax), toScreenY(xMax));
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "rgba(148, 163, 184, 0.5)";
        ctx.font = "italic 11px sans-serif";
        ctx.fillText("y = x", toScreenX(4.2), toScreenY(4.5));

        // Parabola inverse: (y-q)^2 = a*(x-p)  =>  x = ((y-q)^2)/a + p
        if (Math.abs(a) > 0.1) {
          ctx.strokeStyle = "rgba(168, 85, 247, 0.35)";
          ctx.lineWidth = 1.5;
          ctx.setLineDash([3, 4]);
          ctx.beginPath();
          let started = false;
          for (let y = yMin; y <= yMax; y += 0.05) {
            const x = Math.pow(y - q, 2) / a + p;
            if (x >= xMin - 1 && x <= xMax + 1) {
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
          ctx.setLineDash([]);
        }
      }

      // 5. Vertex (p, q) Guide dashed lines
      if (chkVertexGuide) {
        const vx = toScreenX(p);
        const vy = toScreenY(q);
        ctx.strokeStyle = "rgba(236, 72, 153, 0.4)";
        ctx.lineWidth = 1.2;
        ctx.setLineDash([4, 4]);
        // Vertical guide to x-axis
        ctx.beginPath();
        ctx.moveTo(vx, origY);
        ctx.lineTo(vx, vy);
        ctx.stroke();
        // Horizontal guide to y-axis
        ctx.beginPath();
        ctx.moveTo(origX, vy);
        ctx.lineTo(vx, vy);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // 6. Draw Square Root Curve
      ctx.lineWidth = 3.5;
      ctx.strokeStyle = (a > 0) ? "#38bdf8" : "#fb923c";
      if (sign === -1) ctx.strokeStyle = "#facc15";

      ctx.beginPath();
      let curveStarted = false;

      if (Math.abs(a) < 0.05) {
        // Degenerate horizontal line y = q
        ctx.moveTo(toScreenX(xMin), toScreenY(q));
        ctx.lineTo(toScreenX(xMax), toScreenY(q));
      } else if (a > 0) {
        // Domain x >= p
        const startX = Math.max(p, xMin);
        const endX = xMax;
        for (let x = startX; x <= endX; x += 0.02) {
          const inner = a * (x - p);
          if (inner >= 0) {
            const y = sign * Math.sqrt(inner) + q;
            const sx = toScreenX(x);
            const sy = toScreenY(y);
            if (!curveStarted) {
              ctx.moveTo(sx, sy);
              curveStarted = true;
            } else {
              ctx.lineTo(sx, sy);
            }
          }
        }
      } else {
        // Domain x <= p
        const startX = Math.min(p, xMax);
        const endX = xMin;
        for (let x = startX; x >= endX; x -= 0.02) {
          const inner = a * (x - p);
          if (inner >= 0) {
            const y = sign * Math.sqrt(inner) + q;
            const sx = toScreenX(x);
            const sy = toScreenY(y);
            if (!curveStarted) {
              ctx.moveTo(sx, sy);
              curveStarted = true;
            } else {
              ctx.lineTo(sx, sy);
            }
          }
        }
      }
      ctx.stroke();

      // 7. Vertex (p, q) Glow Point
      const vx = toScreenX(p);
      const vy = toScreenY(q);

      // Glow halo
      const grad = ctx.createRadialGradient(vx, vy, 2, vx, vy, 14);
      grad.addColorStop(0, "rgba(236, 72, 153, 0.8)");
      grad.addColorStop(1, "rgba(236, 72, 153, 0)");
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(vx, vy, 14, 0, Math.PI * 2);
      ctx.fill();

      // Core dot
      ctx.fillStyle = "#ec4899";
      ctx.beginPath();
      ctx.arc(vx, vy, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
      ctx.stroke();

      // Vertex Label
      ctx.fillStyle = "#ec4899";
      ctx.font = "bold 12px 'Consolas', monospace";
      const offsetX = (a > 0) ? -65 : 12;
      const offsetY = (sign === 1) ? 18 : -10;
      ctx.fillText(`시점 (${p.toFixed(1)}, ${q.toFixed(1)})`, vx + offsetX, vy + offsetY);
    }

    function switchL18Tab(tabIdx) {
      for (let i = 1; i <= 6; i++) {
        const btn = document.getElementById(`tabBtnL18_${i}`);
        const content = document.getElementById(`tabL18_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise();
      }
    }

    function copyManimCode18() {
      const codeEl = document.querySelector("#manimPre18 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL18() {
      updateL18();
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise();
      }
    }
'''

    # Insert Lecture 18 JS before Lecture 17 JS
    idx_js17 = html.find('// JAVASCRIPT FOR LECTURE 17')
    if idx_js17 != -1:
        # find the beginning of the comment block
        idx_block = html.rfind('// ==============================================================', 0, idx_js17)
        if idx_block != -1:
            html = html[:idx_block] + js_code_18 + '\n' + html[idx_block:]
            print("Inserted Lecture 18 JavaScript before Lecture 17 JS.")
        else:
            html = html[:idx_js17] + js_code_18 + '\n' + html[idx_js17:]
            print("Inserted Lecture 18 JavaScript.")
    else:
        # fallback
        idx_js16 = html.find('// ==============================================================')
        html = html[:idx_js16] + js_code_18 + '\n' + html[idx_js16:]
        print("Inserted Lecture 18 JavaScript (fallback).")

    # 5. Update setLecture loop from 17 to 18
    html = html.replace('for (let i = 1; i <= 17; i++)', 'for (let i = 1; i <= 18; i++)')
    print("Updated setLecture loop to 18.")

    # Add num === 18 render handler
    old_l17_check = 'if (num === 17) setTimeout(renderL17, 50);'
    new_l18_check = 'if (num === 18) setTimeout(renderL18, 50);\n      else if (num === 17) setTimeout(renderL17, 50);'
    html = html.replace(old_l17_check, new_l18_check, 1)
    print("Added num === 18 render handler to setLecture.")

    # Update window load handler
    html = html.replace('setLecture(17);', 'setLecture(18);')
    html = html.replace('setTimeout(renderL17, 200);', 'setTimeout(renderL18, 200);')
    print("Updated window load handler to initialize Lecture 18.")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with Lecture 18!")

if __name__ == '__main__':
    main()
