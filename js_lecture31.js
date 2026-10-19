    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 31 (EXP & LOG DUAL LAB)           */
    /* ============================================================== */
    let l31Base = 2.0;

    function setL31Base(b) {
      l31Base = b;
      [2.0, 3.0, 0.5, 0.33].forEach((val, idx) => {
        const btn = document.getElementById(`btnL31_b${idx + 1}`);
        if (btn) btn.classList.toggle("active", Math.abs(val - b) < 0.05);
      });
      updateL31();
    }

    function switchL31Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL31_${i}`);
        const content = document.getElementById(`tabL31_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture31View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode31() {
      const codeEl = document.querySelector("#manimPre31 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제31강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL31() {
      updateL31();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture31View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL31() {
      const cvs = document.getElementById("cvsLec31");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const xEl = document.getElementById("slL31_x");
      const trackX = xEl ? parseFloat(xEl.value) : 1.5;
      const vx = document.getElementById("valL31_x");
      if (vx) vx.innerText = trackX.toFixed(1);

      ctx.clearRect(0, 0, W, H);

      const originX = W / 2 - 20;
      const originY = H / 2 + 20;
      const scale = 50;

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

      // y = x dashed line
      ctx.strokeStyle = "rgba(148, 163, 184, 0.35)";
      ctx.setLineDash([5, 5]);
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(originX - 4 * scale, originY + 4 * scale);
      ctx.lineTo(originX + 4 * scale, originY - 4 * scale);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px sans-serif";
      ctx.fillText("y = x", originX + 3.2 * scale, originY - 3.4 * scale);

      // Plot y = a^x (Cyan)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      let started = false;
      for (let px = 0; px < W; px += 2) {
        const x = (px - originX) / scale;
        const y = Math.pow(l31Base, x);
        const py = originY - y * scale;
        if (py >= -100 && py <= H + 100) {
          if (!started) { ctx.moveTo(px, py); started = true; }
          else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();

      // Plot y = log_a(x) (Gold)
      ctx.strokeStyle = "#fbbf24";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      started = false;
      for (let px = originX + 2; px < W; px += 2) {
        const x = (px - originX) / scale;
        if (x <= 0) continue;
        const y = Math.log(x) / Math.log(l31Base);
        const py = originY - y * scale;
        if (py >= -100 && py <= H + 100) {
          if (!started) { ctx.moveTo(px, py); started = true; }
          else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();

      // Fixed points (0, 1) and (1, 0)
      const pExp0 = { x: originX, y: originY - 1 * scale };
      const pLog0 = { x: originX + 1 * scale, y: originY };

      [pExp0, pLog0].forEach((p, idx) => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, 5, 0, Math.PI * 2);
        ctx.fillStyle = idx === 0 ? "#38bdf8" : "#fbbf24";
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 11px sans-serif";
      ctx.fillText("(0, 1)", pExp0.x - 22, pExp0.y - 6);

      ctx.fillStyle = "#fbbf24";
      ctx.fillText("(1, 0)", pLog0.x + 4, pLog0.y + 16);

      // Current tracked points
      const curExpY = Math.pow(l31Base, trackX);
      const ptA = { x: originX + trackX * scale, y: originY - curExpY * scale };
      const ptB = { x: originX + curExpY * scale, y: originY - trackX * scale };

      if (ptA.y >= 0 && ptA.y <= H && ptB.x >= 0 && ptB.x <= W) {
        // Reflection segment between (x, a^x) and (a^x, x)
        ctx.strokeStyle = "rgba(244, 63, 94, 0.6)";
        ctx.setLineDash([3, 3]);
        ctx.beginPath(); ctx.moveTo(ptA.x, ptA.y); ctx.lineTo(ptB.x, ptB.y); ctx.stroke();
        ctx.setLineDash([]);

        // Dots
        [ptA, ptB].forEach(p => {
          ctx.beginPath(); ctx.arc(p.x, p.y, 5.5, 0, Math.PI * 2);
          ctx.fillStyle = "#f43f5e"; ctx.fill();
          ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke();
        });

        ctx.fillStyle = "#f43f5e";
        ctx.font = "bold 11px sans-serif";
        ctx.fillText(`P(${trackX.toFixed(1)}, ${curExpY.toFixed(2)})`, ptA.x - 10, ptA.y - 10);
        ctx.fillText(`Q(${curExpY.toFixed(2)}, ${trackX.toFixed(1)})`, ptB.x + 8, ptB.y + 4);
      }

      // Legend
      ctx.font = "bold 13px sans-serif";
      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`y = ${l31Base.toFixed(2)}ˣ (지수함수)`, 25, 30);
      ctx.fillStyle = "#fbbf24";
      ctx.fillText(`y = log_${l31Base.toFixed(2)}(x) (로그함수)`, 25, 50);

      // Update Audit Stats
      const statBox = document.getElementById("statL31_box");
      if (statBox) {
        statBox.innerHTML = `
          <div>• 지수함수 점 P: <strong style="color: #38bdf8;">(${trackX.toFixed(2)}, ${curExpY.toFixed(2)})</strong></div>
          <div>• 로그함수 대칭점 Q: <strong style="color: #facc15;">(${curExpY.toFixed(2)}, ${trackX.toFixed(2)})</strong></div>
          <div>• y = x 대칭성: <strong style="color: #34d399;">선분 PQ는 y=x와 수직으로 교차</strong></div>
          <div>• 밑 $a$ 성질: <strong style="color: ${l31Base > 1 ? '#38bdf8' : '#fbbf24'};">${l31Base > 1 ? 'a > 1 (증가함수)' : '0 < a < 1 (감소함수)'}</strong></div>
        `;
      }
    }
