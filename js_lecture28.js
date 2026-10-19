    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 28 (14 TEXTBOOK GRAPHS MASTER)   */
    /* ============================================================== */
    let l28Graph = 1; // 1 to 14

    const L28_INFO = [
      null,
      { name: "1. 일차함수 (직선)", formula: "y = kx + 1", sym: "점 (0,1) 점대칭", prop: "일정한 기울기, 전구간 미분가능" },
      { name: "2. 이차함수 (포물선)", formula: "y = kx² - 2", sym: "y축 선대칭 (x = 0)", prop: "꼭짓점 (0,-2), 볼록성" },
      { name: "3. 삼차함수 (N자 곡선)", formula: "y = k(x³ - 3x)", sym: "원점 (0,0) 변곡점 점대칭", prop: "극대/극소, 2:1 접선 비율, 8칸 박스법" },
      { name: "4. 사차함수 (W자 곡선)", formula: "y = k(x² - 2)² - 2", sym: "y축 선대칭 W형", prop: "이중접선, 1:√2 비율관계" },
      { name: "5. 유리함수 (직각쌍곡선)", formula: "y = k/x", sym: "원점 점대칭 및 y = ±x 선대칭", prop: "두 점근선 x = 0, y = 0" },
      { name: "6. 무리함수 (곡선)", formula: "y = k√(x + 2) - 1", sym: "대칭성 없음 (포물선 절반)", prop: "시작점 (-2,-1), 정의역 x ≥ -2" },
      { name: "7. 지수함수", formula: "y = (1.5^k)^x", sym: "로그함수와 y=x 역함수 대칭", prop: "수평 점근선 y = 0, 정점 (0,1)" },
      { name: "8. 로그함수", formula: "y = k · log₂(x)", sym: "지수함수와 y=x 역함수 대칭", prop: "수직 점근선 x = 0, 정점 (1,0)" },
      { name: "9. 삼각함수 (사인/코사인)", formula: "y = k sin(x)", sym: "원점 점대칭, 주기 2π", prop: "진폭 k, 8칸 박스 파동" },
      { name: "10. 삼각함수 (탄젠트)", formula: "y = k tan(0.8x)", sym: "원점 점대칭, 주기 π", prop: "무한 점근선 x = ±π/(2ω)" },
      { name: "11. 원의 방정식", formula: "x² + y² = (2k)²", sym: "원점 중심 완전 원대칭", prop: "반지름 r = 2k" },
      { name: "12. 포물선 (기하)", formula: "y² = 4(k)x", sym: "x축 선대칭", prop: "초점 F(k, 0), 준선 x = -k" },
      { name: "13. 타원의 방정식", formula: "x²/(3k)² + y²/(2k)² = 1", sym: "원점 점대칭 및 x,y축 선대칭", prop: "장축 6k, 단축 4k, 거리합 2a" },
      { name: "14. 쌍곡선 (기하)", formula: "x²/(2k)² - y²/(1.5k)² = 1", sym: "원점 점대칭 및 점근선 대칭", prop: "거리차 2a, 점근선 y = ±(b/a)x" }
    ];

    function setL28Graph(g) {
      l28Graph = g;
      for (let i = 1; i <= 14; i++) {
        const btn = document.getElementById(`btnL28_g${i}`);
        if (btn) btn.classList.toggle("active", i === g);
      }
      updateL28();
    }

    function switchL28Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL28_${i}`);
        const content = document.getElementById(`tabL28_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture28View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode28() {
      const codeEl = document.querySelector("#manimPre28 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제28강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL28() {
      updateL28();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture28View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL28() {
      const cvs = document.getElementById("cvsLec28");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const kEl = document.getElementById("slL28_k");
      const k = kEl ? parseFloat(kEl.value) : 1.0;
      const vk = document.getElementById("valL28_k");
      if (vk) vk.innerText = k.toFixed(1);

      ctx.clearRect(0, 0, W, H);

      const originX = W / 2;
      const originY = H / 2;
      const scaleX = 45;
      const scaleY = 45;

      // Grid
      ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
      ctx.lineWidth = 1;
      for (let x = 0; x < W; x += 30) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke();
      }
      for (let y = 0; y < H; y += 30) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
      }

      // Axes
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(0, originY); ctx.lineTo(W, originY); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(originX, 0); ctx.lineTo(originX, H); ctx.stroke();

      // Plot curve based on l28Graph
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.8;
      ctx.beginPath();

      if (l28Graph === 1) { // Linear: y = kx + 1
        const y1 = k * (-6) + 1;
        const y2 = k * (6) + 1;
        ctx.moveTo(originX - 6 * scaleX, originY - y1 * scaleY);
        ctx.lineTo(originX + 6 * scaleX, originY - y2 * scaleY);
        ctx.stroke();
      } else if (l28Graph === 2) { // Quadratic: y = k*x^2 - 2
        let st = false;
        for (let px = 0; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = k * x * x - 2;
          const py = originY - y * scaleY;
          if (py >= -100 && py <= H + 100) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
      } else if (l28Graph === 3) { // Cubic: y = k * (x^3 - 3x)
        let st = false;
        for (let px = 0; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = k * (x * x * x - 3 * x);
          const py = originY - y * scaleY;
          if (py >= -100 && py <= H + 100) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
      } else if (l28Graph === 4) { // Quartic: y = k * (x^2 - 2)^2 - 2
        let st = false;
        for (let px = 0; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = k * Math.pow(x * x - 2, 2) - 2;
          const py = originY - y * scaleY;
          if (py >= -100 && py <= H + 100) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
      } else if (l28Graph === 5) { // Rational: y = (2*k) / x
        ctx.beginPath();
        let st = false;
        for (let px = 0; px < originX - 2; px += 2) {
          const x = (px - originX) / scaleX;
          const y = (2 * k) / x;
          const py = originY - y * scaleY;
          if (py >= -100 && py <= H + 100) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
        ctx.beginPath();
        st = false;
        for (let px = originX + 2; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = (2 * k) / x;
          const py = originY - y * scaleY;
          if (py >= -100 && py <= H + 100) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
      } else if (l28Graph === 6) { // Irrational: y = k * sqrt(x + 2) - 1
        let st = false;
        for (let px = originX - 2 * scaleX; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = k * Math.sqrt(x + 2) - 1;
          const py = originY - y * scaleY;
          if (py >= -100 && py <= H + 100) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(originX - 2 * scaleX, originY + 1 * scaleY, 5, 0, Math.PI * 2);
        ctx.fillStyle = "#f43f5e"; ctx.fill();
      } else if (l28Graph === 7) { // Exponential: y = (1.5^k)^x
        const base = Math.pow(1.5, k);
        let st = false;
        for (let px = 0; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = Math.pow(base, x);
          const py = originY - y * scaleY;
          if (py >= -100 && py <= H + 100) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
      } else if (l28Graph === 8) { // Logarithmic: y = k * log2(x)
        let st = false;
        for (let px = originX + 2; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = Math.log2(x) * k;
          const py = originY - y * scaleY;
          if (py >= -100 && py <= H + 100) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
      } else if (l28Graph === 9) { // Sine: y = k * sin(x)
        let st = false;
        for (let px = 0; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = k * Math.sin(x);
          const py = originY - y * scaleY;
          if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
        }
        ctx.stroke();
      } else if (l28Graph === 10) { // Tangent: y = k * tan(0.8x)
        ctx.strokeStyle = "rgba(250, 204, 21, 0.4)";
        ctx.setLineDash([4, 4]);
        const wVal = 0.8;
        const asymX1 = originX - (Math.PI / (2 * wVal)) * scaleX;
        const asymX2 = originX + (Math.PI / (2 * wVal)) * scaleX;
        ctx.beginPath(); ctx.moveTo(asymX1, 0); ctx.lineTo(asymX1, H); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(asymX2, 0); ctx.lineTo(asymX2, H); ctx.stroke();
        ctx.setLineDash([]);

        ctx.strokeStyle = "#38bdf8";
        ctx.beginPath();
        let st = false;
        for (let px = asymX1 + 4; px < asymX2 - 4; px += 2) {
          const x = (px - originX) / scaleX;
          const y = k * Math.tan(wVal * x);
          const py = originY - y * scaleY;
          if (py >= -100 && py <= H + 100) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
      } else if (l28Graph === 11) { // Circle: x^2 + y^2 = (2k)^2
        const r = 2 * k * scaleX;
        ctx.beginPath();
        ctx.arc(originX, originY, r, 0, Math.PI * 2);
        ctx.stroke();
      } else if (l28Graph === 12) { // Parabola (conic): y^2 = 4kx
        ctx.beginPath();
        let st = false;
        for (let py = 0; py < H; py += 2) {
          const y = (originY - py) / scaleY;
          const x = (y * y) / (4 * k);
          const px = originX + x * scaleX;
          if (px <= W + 50) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(originX + k * scaleX, originY, 5, 0, Math.PI * 2);
        ctx.fillStyle = "#facc15"; ctx.fill();
        ctx.strokeStyle = "rgba(244, 63, 94, 0.6)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(originX - k * scaleX, 0); ctx.lineTo(originX - k * scaleX, H);
        ctx.stroke();
        ctx.setLineDash([]);
      } else if (l28Graph === 13) { // Ellipse: x^2/(3k)^2 + y^2/(2k)^2 = 1
        ctx.beginPath();
        ctx.ellipse(originX, originY, 3 * k * scaleX, 2 * k * scaleY, 0, 0, Math.PI * 2);
        ctx.stroke();
      } else if (l28Graph === 14) { // Hyperbola: x^2/(2k)^2 - y^2/(1.5k)^2 = 1
        const a = 2 * k, b = 1.5 * k;
        ctx.beginPath();
        let st = false;
        for (let py = 0; py < H; py += 2) {
          const y = (originY - py) / scaleY;
          const x = a * Math.sqrt(1 + (y * y) / (b * b));
          const px = originX + x * scaleX;
          if (px <= W + 50) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
        ctx.beginPath();
        st = false;
        for (let py = 0; py < H; py += 2) {
          const y = (originY - py) / scaleY;
          const x = -a * Math.sqrt(1 + (y * y) / (b * b));
          const px = originX + x * scaleX;
          if (px >= -50) {
            if (!st) { ctx.moveTo(px, py); st = true; } else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();
        ctx.strokeStyle = "rgba(250, 204, 21, 0.4)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(originX - 6 * scaleX, originY - (-6 * (b / a)) * scaleY);
        ctx.lineTo(originX + 6 * scaleX, originY - (6 * (b / a)) * scaleY);
        ctx.moveTo(originX - 6 * scaleX, originY - (6 * (b / a)) * scaleY);
        ctx.lineTo(originX + 6 * scaleX, originY - (-6 * (b / a)) * scaleY);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Title badge on canvas
      const curInfo = L28_INFO[l28Graph] || L28_INFO[1];
      ctx.fillStyle = "#facc15";
      ctx.font = "bold 14px sans-serif";
      ctx.textAlign = "left";
      ctx.fillText(`${curInfo.name} : ${curInfo.formula}`, 20, 30);

      // Update Audit Stats
      const statBox = document.getElementById("statL28_box");
      if (statBox) {
        statBox.innerHTML = `
          <div>• 선택 곡선: <strong style="color: #38bdf8;">${curInfo.name}</strong></div>
          <div>• 표준 수식: <strong style="color: #facc15;">${curInfo.formula}</strong></div>
          <div>• 대칭성: <strong style="color: #34d399;">${curInfo.sym}</strong></div>
          <div>• 주요 기하 특성: <strong style="color: #cbd5e1;">${curInfo.prop}</strong></div>
        `;
      }
    }
