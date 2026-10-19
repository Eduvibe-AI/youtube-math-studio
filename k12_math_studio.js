/**
 * K-12 MATH GEOMETRY & GRAPH INTERACTIVE STUDIO
 * 중1부터 고3까지 과목별, 단원별 16대 개념·심화 인터랙티브 그래프 & 도형 엔진
 */

const K12Studio = (function () {
  let activeTrack = 'all';

  function init() {
    renderStudioHtml();
    initCanvases();
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('k12StudioSection'), {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ]
      });
    }
  }

  function setTrack(track) {
    activeTrack = track;
    document.querySelectorAll('.k12-track-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-track') === track);
    });

    document.querySelectorAll('.k12-card').forEach(card => {
      const cardTrack = card.getAttribute('data-track');
      if (track === 'all' || cardTrack === track) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  function renderStudioHtml() {
    const container = document.getElementById('k12StudioContent');
    if (!container) return;

    container.innerHTML = `
      <!-- Track Selector Bar -->
      <div class="k12-track-bar">
        <button class="k12-track-btn active" data-track="all" onclick="K12Studio.setTrack('all')">
          <span>🌟 전체 모아보기</span>
          <span class="badge-count">16</span>
        </button>
        <button class="k12-track-btn" data-track="middle-geom" onclick="K12Studio.setTrack('middle-geom')">
          <span>📐 중등 기하·도형</span>
          <span class="badge-count">4</span>
        </button>
        <button class="k12-track-btn" data-track="high1" onclick="K12Studio.setTrack('high1')">
          <span>📘 고1 공통수학 핵심</span>
          <span class="badge-count">4</span>
        </button>
        <button class="k12-track-btn" data-track="high2" onclick="K12Studio.setTrack('high2')">
          <span>📙 고2 일반선택 (수1·수2)</span>
          <span class="badge-count">4</span>
        </button>
        <button class="k12-track-btn" data-track="high3" onclick="K12Studio.setTrack('high3')">
          <span>🚀 고3 수능심화 (미적·기하)</span>
          <span class="badge-count">4</span>
        </button>
      </div>

      <!-- Studio Cards Grid (16 Interactive Modules) -->
      <div class="k12-cards-grid">

        <!-- ======================================================== -->
        <!-- [중등 1] 삼각형의 오심 (외심·내심·무게중심) 동적 궤적기       -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="middle-geom">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">중2 기하</span>
                <span class="k12-tag tag-unit">삼각형의 성질</span>
                <span class="k12-tag tag-concept">개념</span>
              </div>
              <h3 class="k12-card-title">1. 삼각형의 오심 동적 작도기 (외심 · 내심 · 무게중심)</h3>
              <p class="k12-card-desc">꼭짓점 A, B, C를 마우스로 직접 드래그하여 외접원, 내접원, 중선 2:1 분할비를 실시간 관찰합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_m1_triangle" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_m1_triangle">드래그하여 삼각형 변경</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">🎯 중심 모드:</span>
              <div class="k12-btn-group">
                <button class="k12-opt-btn active" onclick="K12Studio.setM1Mode('centroid')">무게중심 (2:1)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setM1Mode('circum')">외심 (외접원)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setM1Mode('incenter')">내심 (내접원)</button>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              $G = \\left(\\frac{x_1+x_2+x_3}{3}, \\frac{y_1+y_2+y_3}{3}\\right) \\quad \\text{중선 비 } AG:GM = 2:1$
            </div>
            <ul class="k12-points-list">
              <li><strong>무게중심:</strong> 세 중선의 교점이며, 삼각형의 넓이를 정확히 $6$등분합니다.</li>
              <li><strong>외심:</strong> 세 변의 수직이등분선의 교점. 둔각삼각형에서는 외심이 삼각형 외부에 위치합니다!</li>
              <li><strong>내심:</strong> 세 내각의 이등분선의 교점. 넓이 공식 $S = \\frac{1}{2}r(a+b+c)$와 직결됩니다.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [중등 2] 피타고라스 정리 유클리드·바스카라 변환기             -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="middle-geom">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">중2·3 기하</span>
                <span class="k12-tag tag-unit">피타고라스 정리</span>
                <span class="k12-tag tag-killer">심화 증명</span>
              </div>
              <h3 class="k12-card-title">2. 피타고라스 정리 유클리드 &amp; 바스카라 증명기</h3>
              <p class="k12-card-desc">직각삼각형의 두 변 $a, b$를 조절하여 빗변 $c^2 = a^2 + b^2$ 면적 보존을 기하학적으로 증명합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_m2_pythagoras" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_m2_pythagoras">$a^2+b^2=c^2$</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">밑변 $a$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_m2_a" min="30" max="110" value="60" oninput="K12Studio.drawM2()">
                <span class="k12-val-badge" id="val_m2_a">6</span>
              </div>
            </div>
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">높이 $b$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_m2_b" min="30" max="110" value="80" oninput="K12Studio.drawM2()">
                <span class="k12-val-badge" id="val_m2_b">8</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              $a^2 + b^2 = c^2 \\iff c = \\sqrt{a^2 + b^2}$
            </div>
            <ul class="k12-points-list">
              <li><strong>유클리드 증명:</strong> $a^2$ 정사각형과 빗변 위의 직사각형이 밑변과 높이가 같은 평행사변형을 거쳐 면적이 완전히 같습니다.</li>
              <li><strong>바스카라 퍼즐:</strong> 4개의 직각삼각형 넓이 $4 \\times (\\frac{1}{2}ab) + (b-a)^2 = a^2+b^2 = c^2$ 증명.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [중등 3] 원주각과 중심각 2:1 & 접현각 시뮬레이터             -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="middle-geom">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">중3 기하</span>
                <span class="k12-tag tag-unit">원의 성질</span>
                <span class="k12-tag tag-concept">개념</span>
              </div>
              <h3 class="k12-card-title">3. 원주각과 중심각 2:1 불변 원리 &amp; 접현각</h3>
              <p class="k12-card-desc">원주 위의 점 $P$를 드래그해도 같은 호에 대한 원주각 $\\theta$가 절반으로 항상 일정함을 체감합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_m3_circle" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_m3_circle">원주각 = 중심각 / 2</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">호 크기 $2\\theta$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_m3_arc" min="40" max="160" value="100" oninput="K12Studio.drawM3()">
                <span class="k12-val-badge" id="val_m3_arc">100°</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              $\\angle APB = \\frac{1}{2}\\angle AOB = \\text{일정(Constant)}$
            </div>
            <ul class="k12-points-list">
              <li><strong>원주각의 불변성:</strong> 호 $AB$가 고정되어 있으면 점 $P$가 원주 어디로 이동하든 원주각은 변하지 않습니다.</li>
              <li><strong>반원의 원주각:</strong> 지름에 대한 원주각은 언제나 $90^\\circ$ 직각입니다.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [중등 4] 닮음비와 넓이비·부피비 배율기                        -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="middle-geom">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">중2 기하</span>
                <span class="k12-tag tag-unit">도형의 닮음</span>
                <span class="k12-tag tag-killer">심화 원리</span>
              </div>
              <h3 class="k12-card-title">4. 닮음비와 넓이비 · 부피비 확장 스케일러</h3>
              <p class="k12-card-desc">길이의 비가 $1:k$일 때 넓이는 $1:k^2$, 입체 부피는 $1:k^3$으로 폭발적으로 증가하는 기하학적 원리입니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_m4_similarity" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_m4_similarity">길이 1:k → 넓이 1:k²</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">닮음 배율 $k$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_m4_k" min="1" max="3" step="0.1" value="2" oninput="K12Studio.drawM4()">
                <span class="k12-val-badge" id="val_m4_k">2.0배</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              \\text{닮음비 } m:n \\implies \\text{넓이비 } m^2:n^2, \\quad \\text{부피비 } m^3:n^3
            </div>
            <ul class="k12-points-list">
              <li><strong>차원의 법칙:</strong> 1차원(길이 $k$) $\\to$ 2차원(격자 타일 $k^2$) $\\to$ 3차원(정육면체 블록 $k^3$).</li>
              <li><strong>수능 기하 급수:</strong> 프랙탈 등비급수 문항의 공비($r$)를 구할 때 넓이비 $k^2$를 직접 적용하는 핵심 기초입니다.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고1-1] 점과 직선 사이의 거리 공식 동적 작도기               -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high1">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고1 공통수학</span>
                <span class="k12-tag tag-unit">도형의 방정식</span>
                <span class="k12-tag tag-concept">개념 공식</span>
              </div>
              <h3 class="k12-card-title">5. 점과 직선 사이의 거리 공식 동적 작도기</h3>
              <p class="k12-card-desc">점 $P(x_1, y_1)$을 마우스로 끌어 직선 $ax+by+c=0$에 내린 수선의 발 $H$와 최단거리를 실시간 계산합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h1_dist" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h1_dist">d = 계산중</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">기울기 $m$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_h1_m" min="-2" max="2" step="0.2" value="0.6" oninput="K12Studio.drawH1()">
                <span class="k12-val-badge" id="val_h1_m">0.6</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              $d = \\frac{|ax_1 + by_1 + c|}{\\sqrt{a^2 + b^2}}$
            </div>
            <ul class="k12-points-list">
              <li><strong>직각삼각형의 닮음:</strong> 수선의 발 $H$에서 $x$축, $y$축 평행선을 그어 생기는 직각삼각형들의 닮음비로 공식을 유도합니다.</li>
              <li><strong>기하학적 본질:</strong> 점과 직선 사이의 '거리'는 수많은 선분 중 가장 짧은 '수선의 길이'입니다.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고1-2] 원과 직선의 위치관계 판별기 ($d$ vs $r$)             -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high1">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고1 공통수학</span>
                <span class="k12-tag tag-unit">원과 직선</span>
                <span class="k12-tag tag-killer">킬러 공식</span>
              </div>
              <h3 class="k12-card-title">6. 원과 직선의 위치관계 ($d$ vs $r$) &amp; 현의 길이</h3>
              <p class="k12-card-desc">중심과 직선의 거리 $d$와 반지름 $r$을 비교하여 두 점($d<r$), 접함($d=r$), 만나지 않음($d>r$)을 판별합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h2_circle_line" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h2_circle_line">위치관계 분석중</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">직선 이동:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_h2_c" min="-120" max="120" value="40" oninput="K12Studio.drawH2()">
                <span class="k12-val-badge" id="val_h2_c">+40</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              d &lt; r \\iff \\text{두 점 (현의 길이 } 2\\sqrt{r^2-d^2}), \\quad d=r \\iff \\text{접선}
            </div>
            <ul class="k12-points-list">
              <li><strong>판별식 $D$보다 $d$ 공식이 5배 빠름:</strong> 복잡한 $2$차방정식 대입 대신 $d=\\frac{|ax_0+by_0+c|}{\\sqrt{a^2+b^2}}$로 암산!</li>
              <li><strong>원 위의 점까지의 거리:</strong> 직선에서 원 위의 점까지 최단거리 $d-r$, 최장거리 $d+r$.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고1-3] 유리함수 점근선 박스와 평행이동 3초 공식             -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high1">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고1 공통수학</span>
                <span class="k12-tag tag-unit">유리함수</span>
                <span class="k12-tag tag-killer">3초 풀이법</span>
              </div>
              <h3 class="k12-card-title">7. 유리함수 점근선 교점과 파라미터 분해기</h3>
              <p class="k12-card-desc">일반형 $y=\\frac{ax+b}{cx+d}$에서 점근선 $x=-d/c, y=a/c$와 분자 상수 $k$를 초고속 도출합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h3_rational" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h3_rational">점근선 분석중</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">분자 상수 $k$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_h3_k" min="-8" max="8" step="0.5" value="3" oninput="K12Studio.drawH3()">
                <span class="k12-val-badge" id="val_h3_k">3.0</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              y = \\frac{k}{x-p} + q \\iff \\text{점근선 } x=p, y=q, \\quad \\text{대칭점 } (p, q)
            </div>
            <ul class="k12-points-list">
              <li><strong>대칭축 2개:</strong> 점근선 교점 $(p, q)$를 지나고 기울기가 $\\pm 1$인 두 직선 $y-q = \\pm(x-p)$에 대해 완벽한 선대칭!</li>
              <li><strong>사분면 판별:</strong> $k>0$이면 $1, 3$사분면 위치, $k<0$이면 $2, 4$사분면 위치.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고1-4] 무리함수 4대 사분면 시동점과 역함수 교점              -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high1">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고1 공통수학</span>
                <span class="k12-tag tag-unit">무리함수</span>
                <span class="k12-tag tag-killer">3초 풀이법</span>
              </div>
              <h3 class="k12-card-title">8. 무리함수 4방향 분기와 $y=x$ 역함수 교점</h3>
              <p class="k12-card-desc">시점 $(p, q)$와 부호 조합 $(\\pm, \\pm)$에 따른 4대 사분면 날개 곡선 및 $y=x$와의 교점 개수를 판별합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h4_irrational" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h4_irrational">시점 및 교점 계산중</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">방향 분기:</span>
              <div class="k12-btn-group">
                <button class="k12-opt-btn active" onclick="K12Studio.setH4Dir(1, 1)">제1사 (+,+)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setH4Dir(-1, 1)">제2사 (-,+)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setH4Dir(-1, -1)">제3사 (-,-)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setH4Dir(1, -1)">제4사 (+,-)</button>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              y = \\pm\\sqrt{a(x-p)} + q \\iff \\text{이차 포물선의 누운 절반(Inverse)}
            </div>
            <ul class="k12-points-list">
              <li><strong>역함수 교점 3초 법칙:</strong> 증가함수일 때 무리함수와 역함수의 교점은 무조건 $y=x$ 선상에서만 발생합니다!</li>
              <li><strong>판별식 주의점:</strong> 제곱하여 푸는 $D=0$은 가짜 근(무연근)을 포함하므로 시작점 $(p, q)$의 위치 체크가 필수입니다.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고2-1] 삼각함수 단위원 & 8칸 박스법 연동기                  -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high2">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고2 수학 I</span>
                <span class="k12-tag tag-unit">삼각함수</span>
                <span class="k12-tag tag-concept">개념</span>
              </div>
              <h3 class="k12-card-title">9. 단위원 회전각 &amp; 삼각함수 8칸 박스법 연동</h3>
              <p class="k12-card-desc">단위원의 회전각 $\\theta$에 따른 높이($\\sin$)와 밑변($\\cos$)이 우측 8칸 격자 그래프에 실시간 동기화됩니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h2_trig" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h2_trig">θ 동기화중</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">각도 $\\theta$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_h2_theta" min="0" max="360" value="45" oninput="K12Studio.drawH2Trig()">
                <span class="k12-val-badge" id="val_h2_theta">45°</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              P(\\cos\\theta, \\sin\\theta) \\iff \\text{단위원 위의 동점 좌표}
            </div>
            <ul class="k12-points-list">
              <li><strong>8칸 박스법:</strong> 주기를 4등분($\\frac{\\pi}{2}, \\pi, \\frac{3\\pi}{2}, 2\\pi$), 진폭을 2등분($\\pm A$)하여 8칸 상자 안에 곡선을 스케치!</li>
              <li><strong>기함수/우함수 대칭:</strong> $\\sin(-\\theta) = -\\sin\\theta$ (원점대칭), $\\cos(-\\theta) = \\cos\\theta$ ($y$축대칭).</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고2-2] 지수함수 & 로그함수 역함수 대칭축 ($y=x$)             -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high2">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고2 수학 I</span>
                <span class="k12-tag tag-unit">지수·로그함수</span>
                <span class="k12-tag tag-killer">심화</span>
              </div>
              <h3 class="k12-card-title">10. 지수·로그함수의 역함수 대칭축 ($y=x$) 및 교점</h3>
              <p class="k12-card-desc">밑 $a$ 조절에 따라 $y=a^x$와 $y=\\log_a x$의 점근선과 $y=x$와의 교점 개수($0, 1, 2$)를 실시간 추적합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h2_explog" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h2_explog">접점 a ≈ 1.444</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">밑 $a$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_h2_a" min="0.2" max="3" step="0.05" value="2.0" oninput="K12Studio.drawH2ExpLog()">
                <span class="k12-val-badge" id="val_h2_a">2.00</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              y = a^x \\iff x = \\log_a y \\iff y = \\log_a x \\quad (y=x \\text{ 대칭})
            </div>
            <ul class="k12-points-list">
              <li><strong>수능 단골 임계 밑:</strong> $a = e^{1/e} \\approx 1.4447$일 때 $y=a^x$와 $y=x$가 접하며 교점이 정확히 $1$개 발생합니다!</li>
              <li><strong>점근선 교차:</strong> 지수함수는 가로 점근선($y=0$), 로그함수는 세로 점근선($x=0$)을 가집니다.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고2-3] 3차함수 극대·극소와 4대 비율관계 만능 분석기          -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high2">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고2 수학 II</span>
                <span class="k12-tag tag-unit">도함수의 활용</span>
                <span class="k12-tag tag-killer">수능 킬러</span>
              </div>
              <h3 class="k12-card-title">11. 3차함수 극값과 4대 비율관계 ($2:1, 1:\\sqrt{3}, 1:1:1$)</h3>
              <p class="k12-card-desc">변곡점, 극댓값, 극솟값 접선 박스 안에서 일어나는 $1:1:1$ 및 $2:1$ 분할비를 3초 만에 암산합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h2_cubic" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h2_cubic">2:1 비율 격자 활성</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">극값 거리 $d$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_h2_cd" min="20" max="80" value="45" oninput="K12Studio.drawH2Cubic()">
                <span class="k12-val-badge" id="val_h2_cd">45</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              \\text{극점~변곡점~교점 비 } 1 : 1 : 1, \\quad \\text{극값 차 } |f(x_1)-f(x_2)| = \\frac{|a|}{2}(\\beta-\\alpha)^3
            </div>
            <ul class="k12-points-list">
              <li><strong>극대점 접선과의 교점:</strong> 극댓점 $\\to$ 변곡점 $\\to$ 극솟점 $\\to$ 교점의 $x$좌표 간격이 모두 같습니다 ($1:1:1$).</li>
              <li><strong>변곡점 지나는 직선:</strong> 중심 변곡점을 지나는 수평선과의 교점 거리는 $1:\\sqrt{3}$ 비율을 이룹니다.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고2-4] 4차함수 4대 개형과 삼중근 접선 비율 ($3:1$)           -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high2">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고2 수학 II</span>
                <span class="k12-tag tag-unit">도함수의 활용</span>
                <span class="k12-tag tag-killer">수능 킬러</span>
              </div>
              <h3 class="k12-card-title">12. 4차함수 4대 개형과 삼중근 접선 비율 ($3:1$)</h3>
              <p class="k12-card-desc">대칭 W자, 비대칭 W자, 변곡 삼중근 튕김형 등 4차함수의 4대 수능 킬러 개형을 한 번에 정복합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h2_quartic" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h2_quartic">3:1 내분점 활성</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">개형 선택:</span>
              <div class="k12-btn-group">
                <button class="k12-opt-btn active" onclick="K12Studio.setQuarticMode('triple')">삼중근형 (3:1)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setQuarticMode('sym')">대칭 W자형</button>
                <button class="k12-opt-btn" onclick="K12Studio.setQuarticMode('asym')">비대칭 W자형</button>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              \\text{삼중근 접점과 다른 교점 사이의 비 } 3 : 1
            </div>
            <ul class="k12-points-list">
              <li><strong>3:1 내분 공식:</strong> $f(x)-g(x) = a(x-\\alpha)^3(x-\\beta)$ 꼴일 때 도함수 극솟점은 $3:1$ 내분점에 정확히 위치합니다!</li>
              <li><strong>이중접선 면적:</strong> 대칭 W자 4차함수의 이중접선 사이 넓이는 $S = \\frac{|a|}{30}(\\beta-\\alpha)^5$.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고3-1] 초월함수 수능 킬러 3대 개형 ($xe^{-x}, \\ln x/x$)     -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high3">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고3 미적분</span>
                <span class="k12-tag tag-unit">도함수의 활용</span>
                <span class="k12-tag tag-killer">수능 킬러</span>
              </div>
              <h3 class="k12-card-title">13. 초월함수 수능 킬러 3대 개형 ($xe^{-x}, \\frac{\\ln x}{x}, \\frac{x}{x^2+1}$)</h3>
              <p class="k12-card-desc">수능 22번·30번에 단골 출제되는 지수·로그·분수 초월함수의 점근선, 극값, 변곡점을 정밀 렌더링합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h3_transcendental" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h3_transcendental">초월함수 분석중</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">함수 선택:</span>
              <div class="k12-btn-group">
                <button class="k12-opt-btn active" onclick="K12Studio.setTransMode('xe')">y = x e⁻ˣ</button>
                <button class="k12-opt-btn" onclick="K12Studio.setTransMode('lnx')">y = ln(x)/x</button>
                <button class="k12-opt-btn" onclick="K12Studio.setTransMode('frac')">y = x/(x²+1)</button>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              \\lim_{x\\to\\infty} xe^{-x} = 0, \\quad \\text{극댓값 } f(1) = \\frac{1}{e}, \\quad \\text{변곡점 } x=2
            </div>
            <ul class="k12-points-list">
              <li><strong>지수함수의 지배력:</strong> 다항함수 $x$보다 지수함수 $e^{-x}$의 감쇠 속도가 압도적이므로 $x\\to\\infty$에서 $0$으로 수렴합니다.</li>
              <li><strong>$y = \\frac{\\ln x}{x}$의 극대:</strong> $x=e$에서 극댓값 $\\frac{1}{e}$를 가지며, 자연상수 $e$ 판별 문제의 근원입니다.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고3-2] 정적분과 넓이 만능 공식 6종 계산기 & 시각화          -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high3">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고3 미적분·수2</span>
                <span class="k12-tag tag-unit">정적분과 넓이</span>
                <span class="k12-tag tag-killer">초고속 공식</span>
              </div>
              <h3 class="k12-card-title">14. 정적분 넓이 만능 공식 6종 계산기 &amp; 차함수</h3>
              <p class="k12-card-desc">$\\frac{|a|}{6}L^3, \\frac{|a|}{12}L^4, \\frac{|a|}{30}L^5$ 등 적분 계산 노가다 없이 3초 만에 면적을 도출합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h3_integrals" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h3_integrals">면적 자동 적분중</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">공식 모드:</span>
              <div class="k12-btn-group">
                <button class="k12-opt-btn active" onclick="K12Studio.setIntegMode(2)">2차 (1/6)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setIntegMode(3)">3차 접선 (1/12)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setIntegMode(4)">4차 이중접선 (1/30)</button>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              S = \\frac{|a|}{(m+n+1)!} m! n! (\\beta-\\alpha)^{m+n+1}
            </div>
            <ul class="k12-points-list">
              <li><strong>베타 함수 일반화:</strong> 2차함수 두 실근 사이 넓이는 $S = \\frac{|a|}{6}(\\beta-\\alpha)^3$.</li>
              <li><strong>3차 접선 넓이:</strong> 접점과 교점 사이 넓이는 $S = \\frac{|a|}{12}(\\beta-\\alpha)^4$. 적분 구간 대입이 필요 없습니다!</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고3-3] 이차곡선 초점·준선 동적 궤적기 (포물선·타원·쌍곡선)  -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high3">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고3 기하</span>
                <span class="k12-tag tag-unit">이차곡선</span>
                <span class="k12-tag tag-concept">개념</span>
              </div>
              <h3 class="k12-card-title">15. 이차곡선 초점·준선 정의 궤적기 (포물선 · 타원 · 쌍곡선)</h3>
              <p class="k12-card-desc">이심률 $e$와 초점 거리를 조절하여 거리의 합 일정(타원), 거리의 차 일정(쌍곡선), 초점-준선 거리 일치(포물선)를 증명합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h3_conic" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h3_conic">이차곡선 생성중</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">곡선 유형:</span>
              <div class="k12-btn-group">
                <button class="k12-opt-btn active" onclick="K12Studio.setConicMode('ellipse')">타원 (거리합 일정)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setConicMode('parabola')">포물선 (초점=준선)</button>
                <button class="k12-opt-btn" onclick="K12Studio.setConicMode('hyperbola')">쌍곡선 (거리차 일정)</button>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              \\text{타원: } PF + PF' = 2a, \\quad \\text{쌍곡선: } |PF - PF'| = 2a, \\quad \\text{포물선: } PF = PH
            </div>
            <ul class="k12-points-list">
              <li><strong>정의의 절대성:</strong> 수능 기하 킬러 문제의 90%는 복잡한 방정식이 아닌 '초점과 준선까지의 거리 정의'로 풀립니다.</li>
              <li><strong>빛의 반사 성질:</strong> 포물선 축에 평행하게 들어온 빛은 초점으로 모이고, 타원의 한 초점에서 나온 빛은 다른 초점으로 모입니다.</li>
            </ul>
          </div>
        </div>

        <!-- ======================================================== -->
        <!-- [고3-4] 공간도형 삼수선의 정리와 정사영 ($S'=S\\cos\\theta$)    -->
        <!-- ======================================================== -->
        <div class="k12-card" data-track="high3">
          <div class="k12-card-header">
            <div>
              <div class="k12-card-tags">
                <span class="k12-tag tag-grade">고3 기하</span>
                <span class="k12-tag tag-unit">공간도형</span>
                <span class="k12-tag tag-killer">공간 킬러</span>
              </div>
              <h3 class="k12-card-title">16. 삼수선의 정리와 정사영 넓이 ($S' = S\\cos\\theta$)</h3>
              <p class="k12-card-desc">3차원 공간 좌표계에서 평면 $\\alpha$와 직선 $l$, 수선의 발 3개의 직각 관계 및 그림자 넓이 투영을 시각화합니다.</p>
            </div>
          </div>
          <div class="k12-canvas-box">
            <canvas id="cvs_h3_projection" width="600" height="280"></canvas>
            <div class="k12-canvas-overlay" id="info_h3_projection">삼수선 직각 검증중</div>
          </div>
          <div class="k12-controls">
            <div class="k12-ctrl-row">
              <span class="k12-ctrl-label">이면각 $\\theta$:</span>
              <div class="k12-ctrl-slider-wrap">
                <input type="range" class="k12-slider" id="sld_h3_angle" min="15" max="75" value="45" oninput="K12Studio.drawH3Proj()">
                <span class="k12-val-badge" id="val_h3_angle">45°</span>
              </div>
            </div>
          </div>
          <div class="k12-card-body">
            <div class="k12-formula-box">
              S' = S \\cos\\theta \\iff \\cos\\theta = \\frac{S'}{S} \\quad (\\text{정사영 공식})
            </div>
            <ul class="k12-points-list">
              <li><strong>삼수선 제1정리:</strong> $PO \\perp \\alpha$이고 $OH \\perp l$이면 $\\implies PH \\perp l$. 공간의 높이를 잴 때 항상 직각삼각형 $POH$를 탐색합니다.</li>
              <li><strong>이면각의 크기:</b> 두 평면의 교선에 내린 두 수선이 이루는 각 $\\angle PHO = \\theta$가 이면각의 크기입니다.</li>
            </ul>
          </div>
        </div>

      </div>
    `;
  }

  // =========================================================================
  // Canvas Engines Implementation
  // =========================================================================
  let m1Mode = 'centroid';
  let m1Pts = { A: { x: 300, y: 40 }, B: { x: 120, y: 230 }, C: { x: 480, y: 230 } };
  let m1Dragging = null;

  function initCanvases() {
    initM1();
    drawM2();
    drawM3();
    drawM4();
    initH1();
    drawH2();
    drawH3();
    drawH4();
    drawH2Trig();
    drawH2ExpLog();
    drawH2Cubic();
    drawH2Quartic();
    drawH3Trans();
    drawH3Integ();
    drawH3Conic();
    drawH3Proj();
  }

  // [M1] Triangle Centers
  function initM1() {
    const cvs = document.getElementById('cvs_m1_triangle');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');

    function getMousePos(evt) {
      const rect = cvs.getBoundingClientRect();
      const scaleX = cvs.width / rect.width;
      const scaleY = cvs.height / rect.height;
      return {
        x: (evt.clientX - rect.left) * scaleX,
        y: (evt.clientY - rect.top) * scaleY
      };
    }

    cvs.onmousedown = (e) => {
      const pos = getMousePos(e);
      for (const k of ['A', 'B', 'C']) {
        const d = Math.hypot(m1Pts[k].x - pos.x, m1Pts[k].y - pos.y);
        if (d < 18) { m1Dragging = k; break; }
      }
    };
    window.addEventListener('mouseup', () => { m1Dragging = null; });
    cvs.onmousemove = (e) => {
      if (!m1Dragging) return;
      const pos = getMousePos(e);
      m1Pts[m1Dragging].x = Math.max(30, Math.min(570, pos.x));
      m1Pts[m1Dragging].y = Math.max(20, Math.min(260, pos.y));
      drawM1();
    };
    drawM1();
  }

  function setM1Mode(mode) {
    m1Mode = mode;
    const btns = document.querySelectorAll('#group-m1-btns button, .k12-card:nth-child(1) .k12-opt-btn');
    btns.forEach(b => b.classList.remove('active'));
    event.currentTarget.classList.add('active');
    drawM1();
  }

  function drawM1() {
    const cvs = document.getElementById('cvs_m1_triangle');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const { A, B, C } = m1Pts;

    // Background Grid
    drawGrid(ctx, cvs.width, cvs.height);

    // Draw Triangle
    ctx.beginPath();
    ctx.moveTo(A.x, A.y);
    ctx.lineTo(B.x, B.y);
    ctx.lineTo(C.x, C.y);
    ctx.closePath();
    ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.stroke();

    const info = document.getElementById('info_m1_triangle');

    if (m1Mode === 'centroid') {
      // Midpoints
      const mBC = { x: (B.x + C.x) / 2, y: (B.y + C.y) / 2 };
      const mAC = { x: (A.x + C.x) / 2, y: (A.y + C.y) / 2 };
      const mAB = { x: (A.x + B.x) / 2, y: (A.y + B.y) / 2 };
      const G = { x: (A.x + B.x + C.x) / 3, y: (A.y + B.y + C.y) / 3 };

      // Medians
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = 'rgba(251, 191, 36, 0.6)';
      ctx.lineWidth = 1.5;
      [[A, mBC], [B, mAC], [C, mAB]].forEach(([p1, p2]) => {
        ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
      });
      ctx.setLineDash([]);

      // Point G
      drawPoint(ctx, G.x, G.y, '#f59e0b', 'G (2:1)', 7);
      if (info) info.innerHTML = `무게중심 G: <b>(${Math.round(G.x)}, ${Math.round(G.y)})</b> | 중선 2:1 분할`;
    } else if (m1Mode === 'circum') {
      // Circumcenter
      const D = 2 * (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y));
      const Ux = ((A.x*A.x + A.y*A.y)*(B.y - C.y) + (B.x*B.x + B.y*B.y)*(C.y - A.y) + (C.x*C.x + C.y*C.y)*(A.y - B.y)) / D;
      const Uy = ((A.x*A.x + A.y*A.y)*(C.x - B.x) + (B.x*B.x + B.y*B.y)*(A.x - C.x) + (C.x*C.x + C.y*C.y)*(B.x - A.x)) / D;
      const R = Math.hypot(A.x - Ux, A.y - Uy);

      // Circumcircle
      ctx.beginPath();
      ctx.arc(Ux, Uy, R, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(168, 85, 247, 0.7)';
      ctx.lineWidth = 2;
      ctx.stroke();

      drawPoint(ctx, Ux, Uy, '#a855f7', 'O (외심)', 7);
      if (info) info.innerHTML = `외심 O (반지름 R = <b>${Math.round(R)}px</b>)`;
    } else if (m1Mode === 'incenter') {
      // Incenter
      const a = Math.hypot(B.x - C.x, B.y - C.y);
      const b = Math.hypot(A.x - C.x, A.y - C.y);
      const c = Math.hypot(A.x - B.x, A.y - B.y);
      const p = a + b + c;
      const Ix = (a * A.x + b * B.x + c * C.x) / p;
      const Iy = (a * A.y + b * B.y + c * C.y) / p;
      const s = p / 2;
      const area = Math.sqrt(Math.max(0, s * (s - a) * (s - b) * (s - c)));
      const r = area / s;

      // Incircle
      ctx.beginPath();
      ctx.arc(Ix, Iy, r, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(52, 211, 153, 0.85)';
      ctx.lineWidth = 2;
      ctx.stroke();

      drawPoint(ctx, Ix, Iy, '#34d399', 'I (내심)', 7);
      if (info) info.innerHTML = `내심 I (내접원 반지름 r = <b>${Math.round(r)}px</b>)`;
    }

    // Vertices
    drawPoint(ctx, A.x, A.y, '#38bdf8', 'A', 6);
    drawPoint(ctx, B.x, B.y, '#38bdf8', 'B', 6);
    drawPoint(ctx, C.x, C.y, '#38bdf8', 'C', 6);
  }

  // [M2] Pythagoras
  function drawM2() {
    const cvs = document.getElementById('cvs_m2_pythagoras');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const aVal = parseInt(document.getElementById('sld_m2_a')?.value || '60');
    const bVal = parseInt(document.getElementById('sld_m2_b')?.value || '80');
    const cVal = Math.sqrt(aVal * aVal + bVal * bVal);

    document.getElementById('val_m2_a').textContent = (aVal / 10).toFixed(1);
    document.getElementById('val_m2_b').textContent = (bVal / 10).toFixed(1);

    const ox = 260, oy = 210;

    drawGrid(ctx, cvs.width, cvs.height);

    // Triangle ABC
    ctx.beginPath();
    ctx.moveTo(ox, oy);
    ctx.lineTo(ox + aVal, oy);
    ctx.lineTo(ox, oy - bVal);
    ctx.closePath();
    ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Right angle mark
    ctx.strokeStyle = '#fff';
    ctx.strokeRect(ox, oy - 12, 12, 12);

    // Square on a (bottom)
    ctx.fillStyle = 'rgba(236, 72, 153, 0.2)';
    ctx.strokeStyle = '#ec4899';
    ctx.strokeRect(ox, oy, aVal, aVal);
    ctx.fillRect(ox, oy, aVal, aVal);
    ctx.fillStyle = '#f472b6';
    ctx.font = '12px sans-serif';
    ctx.fillText(`a² = ${(aVal*aVal/100).toFixed(0)}`, ox + aVal/3, oy + aVal/2 + 5);

    // Square on b (left)
    ctx.fillStyle = 'rgba(251, 191, 36, 0.2)';
    ctx.strokeStyle = '#fbbf24';
    ctx.strokeRect(ox - bVal, oy - bVal, bVal, bVal);
    ctx.fillRect(ox - bVal, oy - bVal, bVal, bVal);
    ctx.fillStyle = '#fbbf24';
    ctx.fillText(`b² = ${(bVal*bVal/100).toFixed(0)}`, ox - bVal/1.5, oy - bVal/2);

    // Hypotenuse c line
    ctx.fillStyle = '#34d399';
    ctx.fillText(`c = ${(cVal/10).toFixed(1)} (c² = ${(cVal*cVal/100).toFixed(0)})`, ox + aVal/2 - 20, oy - bVal/2 - 10);

    const info = document.getElementById('info_m2_pythagoras');
    if (info) info.innerHTML = `a²(${(aVal*aVal/100).toFixed(0)}) + b²(${(bVal*bVal/100).toFixed(0)}) = c²(<b>${(cVal*cVal/100).toFixed(0)}</b>)`;
  }

  // [M3] Circle Inscribed Angle
  function drawM3() {
    const cvs = document.getElementById('cvs_m3_circle');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const arcDeg = parseInt(document.getElementById('sld_m3_arc')?.value || '100');
    document.getElementById('val_m3_arc').textContent = arcDeg + '°';

    const ox = 300, oy = 140, r = 100;
    drawGrid(ctx, cvs.width, cvs.height);

    // Circle
    ctx.beginPath();
    ctx.arc(ox, oy, r, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
    ctx.lineWidth = 1.8;
    ctx.stroke();

    // Center O
    drawPoint(ctx, ox, oy, '#94a3b8', 'O', 4);

    // Points A, B on circle
    const radA = -arcDeg * Math.PI / 360;
    const radB = arcDeg * Math.PI / 360;
    const Ax = ox + r * Math.cos(radA), Ay = oy - r * Math.sin(radA);
    const Bx = ox + r * Math.cos(radB), By = oy - r * Math.sin(radB);

    // Point P on top arc
    const Px = ox - r * 0.7, Py = oy - r * 0.714;

    // Lines OA, OB
    ctx.beginPath();
    ctx.moveTo(ox, oy); ctx.lineTo(Ax, Ay);
    ctx.moveTo(ox, oy); ctx.lineTo(Bx, By);
    ctx.strokeStyle = 'rgba(251, 146, 60, 0.7)';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Lines PA, PB
    ctx.beginPath();
    ctx.moveTo(Px, Py); ctx.lineTo(Ax, Ay);
    ctx.lineTo(Bx, By); ctx.closePath();
    ctx.fillStyle = 'rgba(56, 189, 248, 0.1)';
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.stroke();

    drawPoint(ctx, Ax, Ay, '#fb923c', 'A', 5);
    drawPoint(ctx, Bx, By, '#fb923c', 'B', 5);
    drawPoint(ctx, Px, Py, '#38bdf8', `P (θ=${(arcDeg/2).toFixed(1)}°)`, 6);

    const info = document.getElementById('info_m3_circle');
    if (info) info.innerHTML = `중심각 <b>${arcDeg}°</b> ➔ 원주각 <b>${(arcDeg/2).toFixed(1)}°</b> (정확히 2:1)`;
  }

  // [M4] Similarity Ratio
  function drawM4() {
    const cvs = document.getElementById('cvs_m4_similarity');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const k = parseFloat(document.getElementById('sld_m4_k')?.value || '2');
    document.getElementById('val_m4_k').textContent = k.toFixed(1) + '배';

    drawGrid(ctx, cvs.width, cvs.height);

    // Base square (1 x 1)
    const baseS = 40;
    ctx.fillStyle = 'rgba(56, 189, 248, 0.2)';
    ctx.strokeStyle = '#38bdf8';
    ctx.strokeRect(80, 160, baseS, baseS);
    ctx.fillRect(80, 160, baseS, baseS);

    ctx.fillStyle = '#fff';
    ctx.font = '12px sans-serif';
    ctx.fillText('기준 1×1', 75, 220);
    ctx.fillText('S = 1', 85, 185);

    // Scaled square (k x k)
    const scaledS = baseS * k;
    ctx.fillStyle = 'rgba(251, 146, 60, 0.2)';
    ctx.strokeStyle = '#fb923c';
    ctx.lineWidth = 2;
    ctx.strokeRect(260, 200 - scaledS, scaledS, scaledS);
    ctx.fillRect(260, 200 - scaledS, scaledS, scaledS);

    // Grid tiles inside scaled
    ctx.setLineDash([2, 3]);
    ctx.strokeStyle = 'rgba(251, 146, 60, 0.5)';
    for (let i = 1; i < k; i++) {
      ctx.beginPath();
      ctx.moveTo(260 + i * baseS, 200 - scaledS);
      ctx.lineTo(260 + i * baseS, 200);
      ctx.moveTo(260, 200 - scaledS + i * baseS);
      ctx.lineTo(260 + scaledS, 200 - scaledS + i * baseS);
      ctx.stroke();
    }
    ctx.setLineDash([]);

    ctx.fillStyle = '#fb923c';
    ctx.font = '13px sans-serif';
    ctx.fillText(`확대 k=${k.toFixed(1)}배`, 260, 220);
    ctx.fillText(`넓이 = k² = ${(k*k).toFixed(2)}배`, 260 + scaledS/4, 200 - scaledS/2);

    const info = document.getElementById('info_m4_similarity');
    if (info) info.innerHTML = `길이비 <b>1 : ${k.toFixed(1)}</b> ➔ 넓이비 <b>1 : ${(k*k).toFixed(2)}</b> (부피비 1 : ${(k*k*k).toFixed(2)})`;
  }

  // [H1] Point-Line Distance
  let h1Pt = { x: 220, y: 70 };
  let h1Dragging = false;

  function initH1() {
    const cvs = document.getElementById('cvs_h1_dist');
    if (!cvs) return;
    cvs.onmousedown = (e) => {
      const rect = cvs.getBoundingClientRect();
      const mx = (e.clientX - rect.left) * (cvs.width / rect.width);
      const my = (e.clientY - rect.top) * (cvs.height / rect.height);
      if (Math.hypot(h1Pt.x - mx, h1Pt.y - my) < 20) h1Dragging = true;
    };
    window.addEventListener('mouseup', () => { h1Dragging = false; });
    cvs.onmousemove = (e) => {
      if (!h1Dragging) return;
      const rect = cvs.getBoundingClientRect();
      h1Pt.x = (e.clientX - rect.left) * (cvs.width / rect.width);
      h1Pt.y = (e.clientY - rect.top) * (cvs.height / rect.height);
      drawH1();
    };
    drawH1();
  }

  function drawH1() {
    const cvs = document.getElementById('cvs_h1_dist');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const m = parseFloat(document.getElementById('sld_h1_m')?.value || '0.6');
    document.getElementById('val_h1_m').textContent = m.toFixed(1);

    drawGrid(ctx, cvs.width, cvs.height);

    // Line ax + by + c = 0 -> y - y0 = m(x - x0)
    const lineX0 = 300, lineY0 = 170;
    // Line: m*x - y + (lineY0 - m*lineX0) = 0 -> a = m, b = -1, c = lineY0 - m*lineX0
    const a = m, b = -1, c = lineY0 - m * lineX0;

    // Draw Line
    ctx.beginPath();
    ctx.moveTo(0, lineY0 - m * (0 - lineX0));
    ctx.lineTo(cvs.width, lineY0 - m * (cvs.width - lineX0));
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.stroke();

    // Foot of perpendicular H
    const dist = (a * h1Pt.x + b * h1Pt.y + c) / (a * a + b * b);
    const Hx = h1Pt.x - a * dist;
    const Hy = h1Pt.y - b * dist;

    // Draw Perpendicular Segment PH
    ctx.beginPath();
    ctx.moveTo(h1Pt.x, h1Pt.y);
    ctx.lineTo(Hx, Hy);
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.setLineDash([]);

    // Right angle mark at H
    const len = Math.hypot(h1Pt.x - Hx, h1Pt.y - Hy);

    drawPoint(ctx, h1Pt.x, h1Pt.y, '#f43f5e', `P (${Math.round(h1Pt.x)}, ${Math.round(h1Pt.y)})`, 7);
    drawPoint(ctx, Hx, Hy, '#38bdf8', 'H', 5);

    const info = document.getElementById('info_h1_dist');
    if (info) info.innerHTML = `최단거리 d = <b>${Math.round(len)}px</b> | 점 P 드래그 가능`;
  }

  // [H2] Circle & Line
  function drawH2() {
    const cvs = document.getElementById('cvs_h2_circle_line');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const offset = parseInt(document.getElementById('sld_h2_c')?.value || '40');
    document.getElementById('val_h2_c').textContent = (offset > 0 ? '+' : '') + offset;

    const ox = 300, oy = 140, r = 70;
    drawGrid(ctx, cvs.width, cvs.height);

    // Circle
    ctx.beginPath();
    ctx.arc(ox, oy, r, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.8)';
    ctx.lineWidth = 2.5;
    ctx.stroke();
    drawPoint(ctx, ox, oy, '#38bdf8', 'O(중심)', 5);

    // Horizontal Line at oy + offset
    const ly = oy + offset;
    ctx.beginPath();
    ctx.moveTo(50, ly);
    ctx.lineTo(550, ly);
    ctx.strokeStyle = '#fbbf24';
    ctx.lineWidth = 2;
    ctx.stroke();

    const d = Math.abs(offset);
    const info = document.getElementById('info_h2_circle_line');

    if (d < r) {
      const halfChord = Math.sqrt(r * r - d * d);
      drawPoint(ctx, ox - halfChord, ly, '#f43f5e', '', 5);
      drawPoint(ctx, ox + halfChord, ly, '#f43f5e', '', 5);
      if (info) info.innerHTML = `<span style="color:#34d399">d &lt; r (두 점에서 만남)</span> : 현의 길이 = <b>${(halfChord*2).toFixed(1)}px</b>`;
    } else if (d === r) {
      drawPoint(ctx, ox, ly, '#f43f5e', '접점', 6);
      if (info) info.innerHTML = `<span style="color:#fbbf24">d = r (접함 / 접선)</span> : 1개의 실근`;
    } else {
      if (info) info.innerHTML = `<span style="color:#f43f5e">d &gt; r (만나지 않음)</span> : 최단거리 = <b>${d - r}px</b>`;
    }
  }

  // [H3] Rational Asymptotes
  function drawH3() {
    const cvs = document.getElementById('cvs_h3_rational');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const k = parseFloat(document.getElementById('sld_h3_k')?.value || '3');
    document.getElementById('val_h3_k').textContent = k.toFixed(1);

    const ox = 300, oy = 140, scale = 25;
    drawGrid(ctx, cvs.width, cvs.height);

    // Asymptotes x = 0, y = 0
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = 'rgba(251, 146, 60, 0.7)';
    ctx.beginPath();
    ctx.moveTo(ox, 20); ctx.lineTo(ox, cvs.height - 20);
    ctx.moveTo(20, oy); ctx.lineTo(cvs.width - 20, oy);
    ctx.stroke();
    ctx.setLineDash([]);

    // Curve y = k / x
    ctx.beginPath();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;

    // Right branch
    let first = true;
    for (let px = 1; px < 250; px += 2) {
      const x = px / scale;
      const y = k / x;
      const py = oy - y * scale;
      if (py >= 10 && py <= cvs.height - 10) {
        if (first) { ctx.moveTo(ox + px, py); first = false; }
        else ctx.lineTo(ox + px, py);
      }
    }
    ctx.stroke();

    // Left branch
    ctx.beginPath();
    first = true;
    for (let px = -250; px < -1; px += 2) {
      const x = px / scale;
      const y = k / x;
      const py = oy - y * scale;
      if (py >= 10 && py <= cvs.height - 10) {
        if (first) { ctx.moveTo(ox + px, py); first = false; }
        else ctx.lineTo(ox + px, py);
      }
    }
    ctx.stroke();

    const info = document.getElementById('info_h3_rational');
    if (info) info.innerHTML = `k = <b>${k}</b> (${k > 0 ? '제 1, 3사분면' : '제 2, 4사분면'}) | 대칭중심 (0, 0)`;
  }

  // [H4] Irrational Function
  let h4SignX = 1, h4SignY = 1;
  function setH4Dir(sx, sy) {
    h4SignX = sx; h4SignY = sy;
    document.querySelectorAll('.k12-card:nth-child(8) .k12-opt-btn').forEach(b => b.classList.remove('active'));
    event.currentTarget.classList.add('active');
    drawH4();
  }

  function drawH4() {
    const cvs = document.getElementById('cvs_h4_irrational');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const ox = 300, oy = 140, scale = 25;
    drawGrid(ctx, cvs.width, cvs.height);

    // Line y = x
    ctx.setLineDash([3, 4]);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
    ctx.beginPath();
    ctx.moveTo(ox - 120, oy + 120);
    ctx.lineTo(ox + 120, oy - 120);
    ctx.stroke();
    ctx.setLineDash([]);

    // Curve y = h4SignY * sqrt(h4SignX * x)
    ctx.beginPath();
    ctx.strokeStyle = '#ec4899';
    ctx.lineWidth = 2.5;
    let first = true;
    for (let px = 0; px <= 240; px += 2) {
      const realX = (px / scale) * h4SignX;
      const rad = h4SignX * realX;
      if (rad < 0) continue;
      const realY = h4SignY * Math.sqrt(rad);
      const canvasX = ox + realX * scale;
      const canvasY = oy - realY * scale;

      if (first) { ctx.moveTo(canvasX, canvasY); first = false; }
      else ctx.lineTo(canvasX, canvasY);
    }
    ctx.stroke();

    drawPoint(ctx, ox, oy, '#facc15', '시점(0,0)', 6);

    const info = document.getElementById('info_h4_irrational');
    const qName = (h4SignX > 0 && h4SignY > 0) ? '제1사분면 (+,+)' :
                  (h4SignX < 0 && h4SignY > 0) ? '제2사분면 (-,+)' :
                  (h4SignX < 0 && h4SignY < 0) ? '제3사분면 (-,-)' : '제4사분면 (+,-)';
    if (info) info.innerHTML = `방향: <b>${qName}</b> | 시점 (0, 0)`;
  }

  // [H2 Trig]
  function drawH2Trig() {
    const cvs = document.getElementById('cvs_h2_trig');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const thetaDeg = parseInt(document.getElementById('sld_h2_theta')?.value || '45');
    document.getElementById('val_h2_theta').textContent = thetaDeg + '°';
    const rad = thetaDeg * Math.PI / 180;

    // Left Unit circle: center 120, 140, R=65
    const cx = 120, cy = 140, R = 65;
    ctx.beginPath();
    ctx.arc(cx, cy, R, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
    ctx.stroke();

    const px = cx + R * Math.cos(rad);
    const py = cy - R * Math.sin(rad);

    ctx.beginPath();
    ctx.moveTo(cx, cy); ctx.lineTo(px, py);
    ctx.strokeStyle = '#fbbf24';
    ctx.lineWidth = 2;
    ctx.stroke();
    drawPoint(ctx, px, py, '#38bdf8', `P`, 5);

    // Height bar
    ctx.beginPath();
    ctx.moveTo(px, py); ctx.lineTo(px, cy);
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Right 8-box grid: from x=240 to 560
    const gx = 240, gy = 140, gW = 320;
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.strokeRect(gx, gy - R, gW, R * 2);
    ctx.beginPath();
    ctx.moveTo(gx, gy); ctx.lineTo(gx + gW, gy);
    for (let i = 1; i <= 4; i++) {
      ctx.moveTo(gx + (gW / 4) * i, gy - R);
      ctx.lineTo(gx + (gW / 4) * i, gy + R);
    }
    ctx.stroke();

    // Draw Sine curve
    ctx.beginPath();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    for (let x = 0; x <= gW; x++) {
      const th = (x / gW) * Math.PI * 2;
      const y = gy - R * Math.sin(th);
      if (x === 0) ctx.moveTo(gx + x, y);
      else ctx.lineTo(gx + x, y);
    }
    ctx.stroke();

    // Current point on sine curve
    const curX = gx + (thetaDeg / 360) * gW;
    const curY = gy - R * Math.sin(rad);
    drawPoint(ctx, curX, curY, '#f43f5e', `sin(${thetaDeg}°) = ${Math.sin(rad).toFixed(2)}`, 6);

    const info = document.getElementById('info_h2_trig');
    if (info) info.innerHTML = `θ = <b>${thetaDeg}°</b> | sinθ = <b>${Math.sin(rad).toFixed(3)}</b>, cosθ = <b>${Math.cos(rad).toFixed(3)}</b>`;
  }

  // [H2 ExpLog]
  function drawH2ExpLog() {
    const cvs = document.getElementById('cvs_h2_explog');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const a = parseFloat(document.getElementById('sld_h2_a')?.value || '2.0');
    document.getElementById('val_h2_a').textContent = a.toFixed(2);

    const ox = 300, oy = 160, scale = 30;
    drawGrid(ctx, cvs.width, cvs.height);

    // y = x
    ctx.setLineDash([3, 4]);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
    ctx.beginPath(); ctx.moveTo(80, oy + 220); ctx.lineTo(520, oy - 220); ctx.stroke();
    ctx.setLineDash([]);

    // y = a^x (Cyan)
    ctx.beginPath();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    let first = true;
    for (let px = -180; px <= 180; px += 2) {
      const x = px / scale;
      const y = Math.pow(a, x);
      const py = oy - y * scale;
      if (py >= 10 && py <= cvs.height - 10) {
        if (first) { ctx.moveTo(ox + px, py); first = false; }
        else ctx.lineTo(ox + px, py);
      }
    }
    ctx.stroke();

    // y = log_a(x) (Orange)
    ctx.beginPath();
    ctx.strokeStyle = '#fb923c';
    ctx.lineWidth = 2.5;
    first = true;
    for (let py = -180; py <= 180; py += 2) {
      const y = py / scale;
      const x = Math.pow(a, y);
      const canvasX = ox + x * scale;
      const canvasY = oy - y * scale;
      if (canvasX >= 10 && canvasX <= cvs.width - 10) {
        if (first) { ctx.moveTo(canvasX, canvasY); first = false; }
        else ctx.lineTo(canvasX, canvasY);
      }
    }
    ctx.stroke();

    const info = document.getElementById('info_h2_explog');
    const touchStatus = (a < 1.444) ? '2개 교점 발생' : (Math.abs(a - 1.444) < 0.05) ? '접함 (a ≈ e^(1/e))' : '교점 없음';
    if (info) info.innerHTML = `밑 a = <b>${a.toFixed(2)}</b> (y=x와 <b>${touchStatus}</b>)`;
  }

  // [H2 Cubic Ratio]
  function drawH2Cubic() {
    const cvs = document.getElementById('cvs_h2_cubic');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const d = parseInt(document.getElementById('sld_h2_cd')?.value || '45');
    document.getElementById('val_h2_cd').textContent = d;

    const ox = 300, oy = 140;
    drawGrid(ctx, cvs.width, cvs.height);

    // Inflection point at (ox, oy)
    // Local max at ox - d, Local min at ox + d
    // Function y = a*(x^3 - 3*d^2*x)
    ctx.beginPath();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    for (let px = -160; px <= 160; px += 2) {
      const normX = px / d;
      const normY = normX * normX * normX - 3 * normX;
      const canvasY = oy + normY * 25;
      if (px === -160) ctx.moveTo(ox + px, canvasY);
      else ctx.lineTo(ox + px, canvasY);
    }
    ctx.stroke();

    // Horizontal Tangent at Max: y = oy - 2 * 25 = oy - 50
    const maxY = oy - 50;
    ctx.setLineDash([3, 4]);
    ctx.strokeStyle = 'rgba(251, 191, 36, 0.7)';
    ctx.beginPath(); ctx.moveTo(80, maxY); ctx.lineTo(520, maxY); ctx.stroke();

    // Ratio Grid vertical lines: x = -d, x = 0, x = +d, x = +2d
    ctx.strokeStyle = 'rgba(168, 85, 247, 0.5)';
    [-d, 0, d, 2 * d].forEach(val => {
      ctx.beginPath(); ctx.moveTo(ox + val, 20); ctx.lineTo(ox + val, cvs.height - 20); ctx.stroke();
    });
    ctx.setLineDash([]);

    drawPoint(ctx, ox - d, maxY, '#fbbf24', '극대(-d)', 5);
    drawPoint(ctx, ox, oy, '#c084fc', '변곡점(0)', 5);
    drawPoint(ctx, ox + d, oy + 50, '#fbbf24', '극소(+d)', 5);
    drawPoint(ctx, ox + 2 * d, maxY, '#34d399', '교점(+2d)', 5);

    const info = document.getElementById('info_h2_cubic');
    if (info) info.innerHTML = `비율 <b>1 : 1 : 1</b> 완벽 일치 (극점~변곡점~교점 간격 = <b>${d}px</b>)`;
  }

  // [H2 Quartic Ratio]
  let quarticMode = 'triple';
  function setQuarticMode(m) {
    quarticMode = m;
    document.querySelectorAll('.k12-card:nth-child(12) .k12-opt-btn').forEach(b => b.classList.remove('active'));
    event.currentTarget.classList.add('active');
    drawH2Quartic();
  }

  function drawH2Quartic() {
    const cvs = document.getElementById('cvs_h2_quartic');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const ox = 300, oy = 170;
    drawGrid(ctx, cvs.width, cvs.height);

    ctx.beginPath();
    ctx.strokeStyle = '#ec4899';
    ctx.lineWidth = 2.5;

    if (quarticMode === 'triple') {
      // f(x) = (x + 60)^3 * (x - 60)
      for (let px = -130; px <= 110; px += 2) {
        const x = px / 50;
        const y = Math.pow(x + 1, 3) * (x - 1.5) * 18;
        const canvasY = oy + y;
        if (px === -130) ctx.moveTo(ox + px, canvasY);
        else ctx.lineTo(ox + px, canvasY);
      }
      ctx.stroke();

      // Triple root at x = -50, root at +75 -> Ratio 3:1
      ctx.setLineDash([3, 4]);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.beginPath(); ctx.moveTo(100, oy); ctx.lineTo(500, oy); ctx.stroke();
      ctx.setLineDash([]);

      drawPoint(ctx, ox - 50, oy, '#facc15', '삼중근 접점', 6);
      drawPoint(ctx, ox + 75, oy, '#38bdf8', '교점', 5);
      drawPoint(ctx, ox + 43.75, oy + 42, '#f43f5e', '극솟점 (3:1 분할)', 6);

      const info = document.getElementById('info_h2_quartic');
      if (info) info.innerHTML = `삼중근 접선 비율 <b>3 : 1</b> 분할 (극솟점 도출)`;
    } else {
      // Symmetric W
      for (let px = -140; px <= 140; px += 2) {
        const x = px / 60;
        const y = (x * x - 1) * (x * x - 1) * -40 + 40;
        const canvasY = oy - y;
        if (px === -140) ctx.moveTo(ox + px, canvasY);
        else ctx.lineTo(ox + px, canvasY);
      }
      ctx.stroke();

      const info = document.getElementById('info_h2_quartic');
      if (info) info.innerHTML = `대칭 W자 4차함수 (이중접선 면적 = <b>|a|/30 L⁵</b>)`;
    }
  }

  // [H3 Transcendental]
  let transMode = 'xe';
  function setTransMode(m) {
    transMode = m;
    document.querySelectorAll('.k12-card:nth-child(13) .k12-opt-btn').forEach(b => b.classList.remove('active'));
    event.currentTarget.classList.add('active');
    drawH3Trans();
  }

  function drawH3Trans() {
    const cvs = document.getElementById('cvs_h3_transcendental');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const ox = 260, oy = 180, scale = 45;
    drawGrid(ctx, cvs.width, cvs.height);

    ctx.beginPath();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;

    const info = document.getElementById('info_h3_transcendental');

    if (transMode === 'xe') {
      // y = x * exp(-x)
      for (let px = -80; px <= 260; px += 2) {
        const x = px / scale;
        const y = x * Math.exp(-x);
        const py = oy - y * scale * 2.2;
        if (px === -80) ctx.moveTo(ox + px, py);
        else ctx.lineTo(ox + px, py);
      }
      ctx.stroke();

      // Peak at x = 1 (1/e)
      const peakX = ox + 1 * scale;
      const peakY = oy - (1 / Math.E) * scale * 2.2;
      drawPoint(ctx, peakX, peakY, '#facc15', '극대 (1, 1/e)', 6);

      // Inflection at x = 2
      const infX = ox + 2 * scale;
      const infY = oy - (2 * Math.exp(-2)) * scale * 2.2;
      drawPoint(ctx, infX, infY, '#c084fc', '변곡점 (2, 2/e²)', 5);

      if (info) info.innerHTML = `y = x e⁻ˣ ➔ 극댓값 (1, 1/e ≈ <b>0.368</b>), 점근선 y = 0`;
    } else if (transMode === 'lnx') {
      // y = ln(x) / x
      for (let px = 10; px <= 280; px += 2) {
        const x = px / scale;
        const y = Math.log(x) / x;
        const py = oy - y * scale * 2.5;
        if (px === 10) ctx.moveTo(ox + px, py);
        else ctx.lineTo(ox + px, py);
      }
      ctx.stroke();

      const eX = ox + Math.E * scale;
      const eY = oy - (1 / Math.E) * scale * 2.5;
      drawPoint(ctx, eX, eY, '#facc15', '극대 (e, 1/e)', 6);

      if (info) info.innerHTML = `y = ln(x)/x ➔ 최대치 x = <b>e</b> (≈2.718), y = 1/e`;
    } else {
      // y = x / (x^2 + 1)
      for (let px = -200; px <= 200; px += 2) {
        const x = px / scale;
        const y = x / (x * x + 1);
        const py = oy - y * scale * 2.5;
        if (px === -200) ctx.moveTo(ox + px, py);
        else ctx.lineTo(ox + px, py);
      }
      ctx.stroke();

      drawPoint(ctx, ox + scale, oy - 0.5 * scale * 2.5, '#facc15', '극대 (1, 1/2)', 6);
      drawPoint(ctx, ox - scale, oy + 0.5 * scale * 2.5, '#f43f5e', '극소 (-1, -1/2)', 6);

      if (info) info.innerHTML = `y = x/(x²+1) ➔ 원점대칭 기함수, 극댓값 = <b>1/2</b>`;
    }
  }

  // [H3 Integrals]
  let integMode = 2;
  function setIntegMode(m) {
    integMode = m;
    document.querySelectorAll('.k12-card:nth-child(14) .k12-opt-btn').forEach(b => b.classList.remove('active'));
    event.currentTarget.classList.add('active');
    drawH3Integ();
  }

  function drawH3Integ() {
    const cvs = document.getElementById('cvs_h3_integrals');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const ox = 300, oy = 170;
    drawGrid(ctx, cvs.width, cvs.height);

    const info = document.getElementById('info_h3_integrals');

    if (integMode === 2) {
      // Parabola y = -(x-a)(x-b)
      const L = 120;
      ctx.beginPath();
      for (let px = -L/2; px <= L/2; px++) {
        const y = (1 - (px / (L/2)) * (px / (L/2))) * 60;
        if (px === -L/2) ctx.moveTo(ox + px, oy);
        ctx.lineTo(ox + px, oy - y);
      }
      ctx.lineTo(ox + L/2, oy);
      ctx.closePath();
      ctx.fillStyle = 'rgba(56, 189, 248, 0.2)';
      ctx.fill();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      drawPoint(ctx, ox - L/2, oy, '#facc15', 'α', 5);
      drawPoint(ctx, ox + L/2, oy, '#facc15', 'β', 5);

      if (info) info.innerHTML = `2차 만능 공식: S = <b>|a|/6 (β - α)³</b>`;
    } else if (integMode === 3) {
      // 3rd degree tangent
      const L = 140;
      ctx.beginPath();
      for (let px = 0; px <= L; px++) {
        const norm = px / L;
        const y = norm * norm * (1 - norm) * 90;
        if (px === 0) ctx.moveTo(ox - L/2 + px, oy);
        ctx.lineTo(ox - L/2 + px, oy - y);
      }
      ctx.lineTo(ox + L/2, oy);
      ctx.closePath();
      ctx.fillStyle = 'rgba(251, 146, 60, 0.2)';
      ctx.fill();
      ctx.strokeStyle = '#fb923c';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      if (info) info.innerHTML = `3차 접선 공식: S = <b>|a|/12 (β - α)⁴</b>`;
    } else {
      // 4th degree double tangent
      const L = 160;
      ctx.beginPath();
      for (let px = -L/2; px <= L/2; px++) {
        const norm = px / (L/2);
        const y = (1 - norm * norm) * (1 - norm * norm) * 60;
        if (px === -L/2) ctx.moveTo(ox + px, oy);
        ctx.lineTo(ox + px, oy - y);
      }
      ctx.lineTo(ox + L/2, oy);
      ctx.closePath();
      ctx.fillStyle = 'rgba(168, 85, 247, 0.2)';
      ctx.fill();
      ctx.strokeStyle = '#c084fc';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      if (info) info.innerHTML = `4차 이중접선 공식: S = <b>|a|/30 (β - α)⁵</b>`;
    }
  }

  // [H3 Conic]
  let conicMode = 'ellipse';
  function setConicMode(m) {
    conicMode = m;
    document.querySelectorAll('.k12-card:nth-child(15) .k12-opt-btn').forEach(b => b.classList.remove('active'));
    event.currentTarget.classList.add('active');
    drawH3Conic();
  }

  function drawH3Conic() {
    const cvs = document.getElementById('cvs_h3_conic');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const ox = 300, oy = 140;
    drawGrid(ctx, cvs.width, cvs.height);

    const info = document.getElementById('info_h3_conic');

    if (conicMode === 'ellipse') {
      const a = 110, b = 70;
      const c = Math.sqrt(a * a - b * b);

      ctx.beginPath();
      ctx.ellipse(ox, oy, a, b, 0, 0, Math.PI * 2);
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      drawPoint(ctx, ox - c, oy, '#facc15', 'F(-c, 0)', 5);
      drawPoint(ctx, ox + c, oy, '#facc15', "F'(c, 0)", 5);

      // Random point P
      const Px = ox + a * Math.cos(0.9), Py = oy - b * Math.sin(0.9);
      ctx.beginPath();
      ctx.moveTo(ox - c, oy); ctx.lineTo(Px, Py); ctx.lineTo(ox + c, oy);
      ctx.strokeStyle = 'rgba(236, 72, 153, 0.7)';
      ctx.lineWidth = 1.8;
      ctx.stroke();
      drawPoint(ctx, Px, Py, '#ec4899', 'P', 5);

      if (info) info.innerHTML = `타원: PF + PF' = <b>2a (장축 길이)</b> = ${2*a}px`;
    } else if (conicMode === 'parabola') {
      // Parabola y^2 = 4px
      const p = 35;
      ctx.beginPath();
      ctx.strokeStyle = '#34d399';
      ctx.lineWidth = 2.5;
      for (let y = -110; y <= 110; y += 2) {
        const x = (y * y) / (4 * p);
        if (y === -110) ctx.moveTo(ox + x, oy + y);
        else ctx.lineTo(ox + x, oy + y);
      }
      ctx.stroke();

      // Focus F(p, 0), Directrix x = -p
      drawPoint(ctx, ox + p, oy, '#facc15', 'F(p,0)', 5);
      ctx.setLineDash([3, 4]);
      ctx.strokeStyle = '#f43f5e';
      ctx.beginPath(); ctx.moveTo(ox - p, 20); ctx.lineTo(ox - p, cvs.height - 20); ctx.stroke();
      ctx.setLineDash([]);

      if (info) info.innerHTML = `포물선: 초점까지 거리 PF = 준선까지 거리 PH (e = 1)`;
    } else {
      // Hyperbola x^2/a^2 - y^2/b^2 = 1
      const a = 50, b = 45;
      const c = Math.sqrt(a * a + b * b);

      ctx.beginPath();
      ctx.strokeStyle = '#c084fc';
      ctx.lineWidth = 2.5;
      // Right branch
      for (let py = -100; py <= 100; py += 2) {
        const px = a * Math.sqrt(1 + (py*py)/(b*b));
        if (py === -100) ctx.moveTo(ox + px, oy + py);
        else ctx.lineTo(ox + px, oy + py);
      }
      // Left branch
      for (let py = -100; py <= 100; py += 2) {
        const px = -a * Math.sqrt(1 + (py*py)/(b*b));
        if (py === -100) ctx.moveTo(ox + px, oy + py);
        else ctx.lineTo(ox + px, oy + py);
      }
      ctx.stroke();

      drawPoint(ctx, ox - c, oy, '#facc15', 'F', 5);
      drawPoint(ctx, ox + c, oy, '#facc15', "F'", 5);

      if (info) info.innerHTML = `쌍곡선: |PF - PF'| = <b>2a (주축 길이)</b> = ${2*a}px`;
    }
  }

  // [H3 Projection]
  function drawH3Proj() {
    const cvs = document.getElementById('cvs_h3_projection');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    ctx.clearRect(0, 0, cvs.width, cvs.height);

    const deg = parseInt(document.getElementById('sld_h3_angle')?.value || '45');
    document.getElementById('val_h3_angle').textContent = deg + '°';
    const rad = deg * Math.PI / 180;

    const ox = 280, oy = 180;
    drawGrid(ctx, cvs.width, cvs.height);

    // Bottom Plane (alpha)
    ctx.fillStyle = 'rgba(255, 255, 255, 0.04)';
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
    ctx.beginPath();
    ctx.moveTo(ox - 160, oy - 20);
    ctx.lineTo(ox + 80, oy - 20);
    ctx.lineTo(ox + 160, oy + 40);
    ctx.lineTo(ox - 80, oy + 40);
    ctx.closePath();
    ctx.fill(); ctx.stroke();
    ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
    ctx.fillText('평면 α', ox - 140, oy + 30);

    // Tilted Triangle Plane
    const L = 100;
    const Px = ox - 20;
    const Py = oy - L * Math.sin(rad);
    const Hx = ox - 20;
    const Hy = oy;

    // Draw Triangles: P, O, H
    ctx.beginPath();
    ctx.moveTo(Px, Py);
    ctx.lineTo(Hx, Hy);
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 2.5;
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(Px, Py);
    ctx.lineTo(ox + 60, oy);
    ctx.lineTo(Hx, Hy);
    ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.stroke();

    drawPoint(ctx, Px, Py, '#f43f5e', 'P (공간점)', 5);
    drawPoint(ctx, Hx, Hy, '#38bdf8', 'H (수선의 발)', 5);
    drawPoint(ctx, ox + 60, oy, '#facc15', '교선 l 위 점', 5);

    const info = document.getElementById('info_h3_projection');
    if (info) info.innerHTML = `이면각 θ = <b>${deg}°</b> ➔ 정사영 면적 S' = S × <b>${Math.cos(rad).toFixed(3)}</b>`;
  }

  // Utility Helper
  function drawGrid(ctx, w, h) {
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.035)';
    ctx.lineWidth = 1;
    for (let x = 0; x < w; x += 30) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
    }
    for (let y = 0; y < h; y += 30) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
    }
  }

  function drawPoint(ctx, x, y, color, label, r = 5) {
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    if (label) {
      ctx.fillStyle = '#f8fafc';
      ctx.font = '11px sans-serif';
      ctx.fillText(label, x + 8, y - 6);
    }
  }

  return {
    init,
    setTrack,
    setM1Mode,
    drawM2,
    drawM3,
    drawM4,
    drawH1,
    drawH2,
    drawH3,
    setH4Dir,
    drawH2Trig,
    drawH2ExpLog,
    drawH2Cubic,
    setQuarticMode,
    setTransMode,
    setIntegMode,
    setConicMode,
    drawH3Proj
  };
})();

// Auto-run on load
window.addEventListener('DOMContentLoaded', () => {
  K12Studio.init();
});
