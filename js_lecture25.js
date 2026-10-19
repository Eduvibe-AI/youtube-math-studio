    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 25 (RECURRENCE RELATIONS BIG 4)   */
    /* ============================================================== */
    let l25Mode = 1;

    function setL25Mode(m) {
      l25Mode = m;
      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`btnL25_mode${i}`);
        if (btn) btn.classList.toggle("active", i === m);
      }
      updateL25();
    }

    function switchL25Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL25_${i}`);
        const content = document.getElementById(`tabL25_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture25View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode25() {
      const codeEl = document.querySelector("#manimPre25 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제25강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL25() {
      updateL25();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture25View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL25() {
      const cvs = document.getElementById("cvsLec25");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const a1El = document.getElementById("slL25_a1");
      const pEl = document.getElementById("slL25_p");
      const qEl = document.getElementById("slL25_q");
      const a1 = a1El ? parseFloat(a1El.value) : 1.0;
      const p = pEl ? parseFloat(pEl.value) : 2.0;
      const q = qEl ? parseFloat(qEl.value) : 3.0;

      const va1 = document.getElementById("valL25_a1");
      const vp = document.getElementById("valL25_p");
      const vq = document.getElementById("valL25_q");
      if (va1) va1.innerText = a1.toFixed(0);
      if (vp) vp.innerText = p.toFixed(1);
      if (vq) vq.innerText = q.toFixed(0);

      ctx.clearRect(0, 0, W, H);

      // Generate sequence terms a_1 .. a_8
      const terms = [a1];
      const N = 8;
      for (let n = 1; n < N; n++) {
        let nextVal = 0;
        if (l25Mode === 1) { // a_{n+1} = p * a_n + q
          nextVal = p * terms[n - 1] + q;
        } else if (l25Mode === 2) { // a_{n+1} = a_n + p * n
          nextVal = terms[n - 1] + p * n;
        } else if (l25Mode === 3) { // a_{n+1} = (n / (n + 1)) * a_n
          nextVal = (n / (n + 1)) * terms[n - 1];
        } else { // a_{n+1} = a_n + q (등차) or p * a_n (등비)
          nextVal = terms[n - 1] + q;
        }
        terms.push(nextVal);
      }

      // Background grid
      ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
      ctx.lineWidth = 1;
      for (let x = 40; x < W; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke();
      }
      for (let y = 30; y < H; y += 30) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
      }

      // Find min and max for scaling
      let minVal = Math.min(0, ...terms);
      let maxVal = Math.max(10, ...terms);
      if (minVal === maxVal) maxVal += 1;
      const padY = (maxVal - minVal) * 0.15;
      minVal -= padY; maxVal += padY;

      const originY = H - 40 - (0 - minVal) / (maxVal - minVal) * (H - 80);
      // Axis
      ctx.strokeStyle = "rgba(148, 163, 184, 0.5)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(40, originY);
      ctx.lineTo(W - 20, originY);
      ctx.stroke();

      // Plot stems and points
      const stepX = (W - 90) / (N - 1);
      ctx.fillStyle = "#38bdf8";

      // Connecting line
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i < N; i++) {
        const px = 55 + i * stepX;
        const py = H - 40 - (terms[i] - minVal) / (maxVal - minVal) * (H - 80);
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Stem dots and labels
      for (let i = 0; i < N; i++) {
        const px = 55 + i * stepX;
        const py = H - 40 - (terms[i] - minVal) / (maxVal - minVal) * (H - 80);

        // Vertical stem
        ctx.strokeStyle = "rgba(56, 189, 248, 0.25)";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(px, originY);
        ctx.lineTo(px, py);
        ctx.stroke();

        // Node circle
        ctx.beginPath();
        ctx.arc(px, py, 6, 0, Math.PI * 2);
        ctx.fillStyle = i === 0 ? "#facc15" : "#38bdf8";
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        // Term name & value
        ctx.fillStyle = "#94a3b8";
        ctx.font = "11px 'Inter', sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(`a${i + 1}`, px, originY + 16);

        ctx.fillStyle = "#facc15";
        ctx.font = "bold 11px 'Inter', sans-serif";
        const valText = terms[i] > 9999 ? terms[i].toExponential(1) : (Math.abs(terms[i]) < 10 ? terms[i].toFixed(2) : terms[i].toFixed(0));
        ctx.fillText(valText, px, py - 10);
      }

      // Title & Alpha line if mode 1
      if (l25Mode === 1 && Math.abs(1 - p) > 0.001) {
        const alpha = q / (1 - p);
        if (alpha >= minVal && alpha <= maxVal) {
          const alphaY = H - 40 - (alpha - minVal) / (maxVal - minVal) * (H - 80);
          ctx.strokeStyle = "rgba(244, 63, 94, 0.7)";
          ctx.setLineDash([6, 6]);
          ctx.beginPath();
          ctx.moveTo(40, alphaY);
          ctx.lineTo(W - 20, alphaY);
          ctx.stroke();
          ctx.setLineDash([]);
          ctx.fillStyle = "#f43f5e";
          ctx.font = "bold 11px 'Inter', sans-serif";
          ctx.textAlign = "right";
          ctx.fillText(`점근선 α = ${alpha.toFixed(2)}`, W - 30, alphaY - 6);
        }
      }

      // Update text statistics
      const statBox = document.getElementById("statL25_box");
      if (statBox) {
        if (l25Mode === 1) {
          const alpha = (1 - p !== 0) ? (q / (1 - p)) : NaN;
          statBox.innerHTML = `
            <div>• 점화식: <strong style="color: #38bdf8;">a_{n+1} = ${p.toFixed(1)} a_n + ${q >= 0 ? '+' : ''}${q.toFixed(0)}</strong></div>
            <div>• 특성근: <strong style="color: #34d399;">α = ${isNaN(alpha) ? '정의 불가(등차)' : alpha.toFixed(2)}</strong></div>
            <div>• 일반항: <strong style="color: #facc15;">a_n = (${(a1 - alpha).toFixed(1)}) · (${p.toFixed(1)})^{n-1} + (${alpha.toFixed(1)})</strong></div>
            <div>• 초반 5개항: <strong style="color: #f43f5e;">${terms.slice(0, 5).map(v => v.toFixed(1)).join(", ")}</strong></div>
          `;
        } else if (l25Mode === 2) {
          statBox.innerHTML = `
            <div>• 계차 점화식: <strong style="color: #38bdf8;">a_{n+1} - a_n = ${p.toFixed(1)}n</strong></div>
            <div>• 계차 수열: <strong style="color: #34d399;">b_n = ${p.toFixed(1)}n</strong></div>
            <div>• 일반항 유도: <strong style="color: #facc15;">a_n = a_1 + ∑_{k=1}^{n-1} (${p.toFixed(1)}k)</strong></div>
            <div>• 초반 5개항: <strong style="color: #f43f5e;">${terms.slice(0, 5).map(v => v.toFixed(1)).join(", ")}</strong></div>
          `;
        } else if (l25Mode === 3) {
          statBox.innerHTML = `
            <div>• 계비 점화식: <strong style="color: #38bdf8;">a_{n+1} = (n / (n+1)) · a_n</strong></div>
            <div>• 연속 곱셈: <strong style="color: #34d399;">대각선 연쇄 약분 (Telescoping)</strong></div>
            <div>• 일반항 유도: <strong style="color: #facc15;">a_n = a_1 / n</strong></div>
            <div>• 초반 5개항: <strong style="color: #f43f5e;">${terms.slice(0, 5).map(v => v.toFixed(2)).join(", ")}</strong></div>
          `;
        } else {
          statBox.innerHTML = `
            <div>• 기본 등차 점화식: <strong style="color: #38bdf8;">a_{n+1} - a_n = d = ${q.toFixed(0)}</strong></div>
            <div>• 공차: <strong style="color: #34d399;">d = ${q.toFixed(0)}</strong></div>
            <div>• 일반항: <strong style="color: #facc15;">a_n = ${a1} + (n-1)·(${q.toFixed(0)})</strong></div>
            <div>• 초반 5개항: <strong style="color: #f43f5e;">${terms.slice(0, 5).map(v => v.toFixed(0)).join(", ")}</strong></div>
          `;
        }
      }
    }
