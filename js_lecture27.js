    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 27 (POLYNOMIAL ROOTS & SYMMETRY)  */
    /* ============================================================== */
    let l27Mode = 1; // 1: 8-box cubic, 2: root contacts, 3: quartic W

    function setL27Mode(m) {
      l27Mode = m;
      for (let i = 1; i <= 3; i++) {
        const btn = document.getElementById(`btnL27_mode${i}`);
        if (btn) btn.classList.toggle("active", i === m);
      }
      updateL27();
    }

    function switchL27Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL27_${i}`);
        const content = document.getElementById(`tabL27_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture27View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode27() {
      const codeEl = document.querySelector("#manimPre27 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제27강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL27() {
      updateL27();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture27View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL27() {
      const cvs = document.getElementById("cvsLec27");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const lEl = document.getElementById("slL27_L");
      const aEl = document.getElementById("slL27_a");
      const L = lEl ? parseFloat(lEl.value) : 1.0;
      const a = aEl ? parseFloat(aEl.value) : 1.0;

      const vL = document.getElementById("valL27_L");
      const va = document.getElementById("valL27_a");
      if (vL) vL.innerText = L.toFixed(1);
      if (va) va.innerText = a.toFixed(1);

      ctx.clearRect(0, 0, W, H);

      const originX = W / 2;
      const originY = H / 2;
      const scaleX = 75 / L; // adapt scale to L
      const scaleY = 40 / (a * Math.pow(L, 3));

      // Grid
      ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
      ctx.lineWidth = 1;
      for (let x = 0; x < W; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke();
      }
      for (let y = 0; y < H; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
      }

      // Axes
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(0, originY); ctx.lineTo(W, originY); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(originX, 0); ctx.lineTo(originX, H); ctx.stroke();

      if (l27Mode === 1) { // 8-box cubic method
        // f(x) = a * x * (x^2 - 3 * L^2)
        // Local max at x = -L, y = 2 * a * L^3
        // Local min at x = L, y = -2 * a * L^3
        // Tangent max y = 2 * a * L^3 crosses at x = 2L
        const yMax = 2 * a * Math.pow(L, 3);
        const yMin = -yMax;

        // Draw 8-box rectangle grid: x in [-2L, 2L], y in [yMin, yMax]
        ctx.strokeStyle = "rgba(56, 189, 248, 0.25)";
        ctx.lineWidth = 1;
        const boxX0 = originX - 2 * L * scaleX;
        const boxX1 = originX + 2 * L * scaleX;
        const boxY0 = originY - yMax * scaleY;
        const boxY1 = originY - yMin * scaleY;

        ctx.strokeRect(boxX0, boxY0, boxX1 - boxX0, boxY1 - boxY0);

        // Vertical lines at -2L, -L, 0, L, 2L
        [-2, -1, 1, 2].forEach(k => {
          const vx = originX + k * L * scaleX;
          ctx.beginPath(); ctx.moveTo(vx, boxY0); ctx.lineTo(vx, boxY1); ctx.stroke();
        });

        // Horizontal tangent lines
        ctx.strokeStyle = "rgba(250, 204, 21, 0.7)";
        ctx.lineWidth = 1.5;
        ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(boxX0 - 20, boxY0); ctx.lineTo(boxX1 + 20, boxY0); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(boxX0 - 20, boxY1); ctx.lineTo(boxX1 + 20, boxY1); ctx.stroke();
        ctx.setLineDash([]);

        // Ratio labels (1:1:1:1)
        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold 11px sans-serif";
        ctx.textAlign = "center";
        [-1.5, -0.5, 0.5, 1.5].forEach(k => {
          ctx.fillText("1", originX + k * L * scaleX, boxY0 - 8);
        });

        // 2:1 highlight bracket
        ctx.fillStyle = "#facc15";
        ctx.font = "bold 12px sans-serif";
        ctx.fillText("←──── 2 ────→←── 1 ──→ (2:1 접선 분할)", originX + 0.5 * L * scaleX, boxY0 - 24);

        // Plot cubic curve
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 3;
        ctx.beginPath();
        let started = false;
        for (let px = 0; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = a * x * (x * x - 3 * L * L);
          const py = originY - y * scaleY;
          if (py >= -200 && py <= H + 200) {
            if (!started) { ctx.moveTo(px, py); started = true; }
            else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();

        // Highlight Key Points
        const pts = [
          { x: -2 * L, y: yMin, color: "#34d399", label: "하단 교점 (-2L)" },
          { x: -L, y: yMax, color: "#f43f5e", label: "극대 접점 (-L)" },
          { x: 0, y: 0, color: "#ffffff", label: "변곡점 (0,0)" },
          { x: L, y: yMin, color: "#38bdf8", label: "극소 접점 (L)" },
          { x: 2 * L, y: yMax, color: "#34d399", label: "상단 교점 (2L)" }
        ];

        pts.forEach(p => {
          const px = originX + p.x * scaleX;
          const py = originY - p.y * scaleY;
          ctx.beginPath();
          ctx.arc(px, py, 5.5, 0, Math.PI * 2);
          ctx.fillStyle = p.color;
          ctx.fill();
          ctx.strokeStyle = "#fff";
          ctx.lineWidth = 1.5;
          ctx.stroke();

          ctx.fillStyle = p.color;
          ctx.font = "11px sans-serif";
          ctx.textAlign = p.x < 0 ? "right" : (p.x === 0 ? "left" : "left");
          ctx.fillText(p.label, px + (p.x < 0 ? -8 : 8), py - 6);
        });

      } else if (l27Mode === 2) { // Contact Orders (1st, 2nd, 3rd)
        // Draw 3 graphs illustrating (x-a)^1, (x-a)^2, (x-a)^3
        ctx.lineWidth = 2.5;

        // 1st order: linear cross (cyan)
        ctx.strokeStyle = "#38bdf8";
        ctx.beginPath();
        ctx.moveTo(originX - 120, originY + 80);
        ctx.lineTo(originX + 120, originY - 80);
        ctx.stroke();

        // 2nd order: bounce parabola (yellow)
        ctx.strokeStyle = "#facc15";
        ctx.beginPath();
        for (let px = originX - 120; px <= originX + 120; px += 4) {
          const dx = (px - originX) / 40;
          const py = originY - dx * dx * 25;
          if (px === originX - 120) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // 3rd order: inflection tangent (rose)
        ctx.strokeStyle = "#f43f5e";
        ctx.beginPath();
        for (let px = originX - 120; px <= originX + 120; px += 4) {
          const dx = (px - originX) / 40;
          const py = originY - dx * dx * dx * 10;
          if (px === originX - 120) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Center dot
        ctx.beginPath();
        ctx.arc(originX, originY, 6, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff";
        ctx.fill();

        // Labels
        ctx.font = "bold 12px sans-serif";
        ctx.fillStyle = "#38bdf8"; ctx.fillText("(x - α)¹ : 단순 관통 (Cross)", 30, 40);
        ctx.fillStyle = "#facc15"; ctx.fillText("(x - α)² : 포물선 접함 (Bounce)", 30, 65);
        ctx.fillStyle = "#f43f5e"; ctx.fillText("(x - α)³ : 변곡 관통 접선 (Inflection)", 30, 90);

      } else { // Quartic W-shape
        // f(x) = a * (x^2 - L^2)^2 = a * (x - L)^2 * (x + L)^2
        ctx.strokeStyle = "#c084fc";
        ctx.lineWidth = 3;
        ctx.beginPath();
        let started = false;
        for (let px = 0; px < W; px += 2) {
          const x = (px - originX) / scaleX;
          const y = a * Math.pow(x * x - L * L, 2);
          const py = originY + 70 - y * (scaleY * 0.7);
          if (py >= -200 && py <= H + 200) {
            if (!started) { ctx.moveTo(px, py); started = true; }
            else ctx.lineTo(px, py);
          }
        }
        ctx.stroke();

        // Double tangent at bottom
        const btmY = originY + 70;
        ctx.strokeStyle = "rgba(250, 204, 21, 0.7)";
        ctx.lineWidth = 1.5;
        ctx.setLineDash([6, 4]);
        ctx.beginPath(); ctx.moveTo(40, btmY); ctx.lineTo(W - 40, btmY); ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#facc15";
        ctx.font = "bold 12px sans-serif";
        ctx.fillText("이중접선 y = k (x = -L, x = L 접함)", originX, btmY + 22);
      }

      // Update Audit Stats
      const statBox = document.getElementById("statL27_box");
      if (statBox) {
        const deltaY = 4 * a * Math.pow(L, 3);
        statBox.innerHTML = `
          <div>• 극값 간격: <strong style="color: #38bdf8;">2L = ${(2 * L).toFixed(2)}</strong> (변곡점 기준 대칭)</div>
          <div>• 극값 높이차: <strong style="color: #facc15;">Δy = 4aL³ = ${deltaY.toFixed(2)}</strong></div>
          <div>• 접선 비율: <strong style="color: #34d399;">2 : 1 내분 분할 보존</strong></div>
        `;
      }
    }
