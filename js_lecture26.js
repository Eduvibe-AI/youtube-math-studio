    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 26 (TAYLOR SERIES SIMULATOR)      */
    /* ============================================================== */
    let l26Func = 1; // 1: exp(x), 2: sin(x), 3: cos(x)

    function setL26Func(f) {
      l26Func = f;
      for (let i = 1; i <= 3; i++) {
        const btn = document.getElementById(`btnL26_func${i}`);
        if (btn) btn.classList.toggle("active", i === f);
      }
      updateL26();
    }

    function switchL26Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL26_${i}`);
        const content = document.getElementById(`tabL26_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture26View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode26() {
      const codeEl = document.querySelector("#manimPre26 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제26강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL26() {
      updateL26();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture26View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function factorial(n) {
      let r = 1;
      for (let i = 2; i <= n; i++) r *= i;
      return r;
    }

    function updateL26() {
      const cvs = document.getElementById("cvsLec26");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const degEl = document.getElementById("slL26_degree");
      const N = degEl ? parseInt(degEl.value, 10) : 3;

      const vDeg = document.getElementById("valL26_degree");
      if (vDeg) vDeg.innerText = N + "차";

      ctx.clearRect(0, 0, W, H);

      // Coordinate system setup
      const originX = W / 2;
      const originY = H / 2 + 30;
      const scaleX = 65; // pixels per unit
      const scaleY = 65;

      // Grid
      ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
      ctx.lineWidth = 1;
      for (let x = originX % scaleX; x < W; x += scaleX) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke();
      }
      for (let y = originY % scaleY; y < H; y += scaleY) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
      }

      // Axes
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(0, originY); ctx.lineTo(W, originY); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(originX, 0); ctx.lineTo(originX, H); ctx.stroke();

      // Axis ticks & labels
      ctx.fillStyle = "#64748b";
      ctx.font = "10px sans-serif";
      ctx.textAlign = "center";
      for (let u = -4; u <= 4; u++) {
        if (u === 0) continue;
        const px = originX + u * scaleX;
        ctx.fillText(u, px, originY + 14);
      }

      // Exact functions
      function exactF(x) {
        if (l26Func === 1) return Math.exp(x);
        if (l26Func === 2) return Math.sin(x);
        return Math.cos(x);
      }

      // Taylor Polynomial P_N(x)
      function taylorP(x, degree) {
        let sum = 0;
        if (l26Func === 1) { // e^x = sum_{k=0}^N x^k / k!
          for (let k = 0; k <= degree; k++) {
            sum += Math.pow(x, k) / factorial(k);
          }
        } else if (l26Func === 2) { // sin(x) = sum_{k=0} (-1)^k x^{2k+1} / (2k+1)!
          for (let k = 0; 2 * k + 1 <= degree; k++) {
            const sign = (k % 2 === 0) ? 1 : -1;
            sum += sign * Math.pow(x, 2 * k + 1) / factorial(2 * k + 1);
          }
        } else { // cos(x) = sum_{k=0} (-1)^k x^{2k} / (2k)!
          for (let k = 0; 2 * k <= degree; k++) {
            const sign = (k % 2 === 0) ? 1 : -1;
            sum += sign * Math.pow(x, 2 * k) / factorial(2 * k);
          }
        }
        return sum;
      }

      // 1. Draw True Function Curve (Glowing Cyan)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.shadowColor = "rgba(56, 189, 248, 0.5)";
      ctx.shadowBlur = 8;
      ctx.beginPath();
      let started = false;
      for (let px = 0; px < W; px += 2) {
        const x = (px - originX) / scaleX;
        const y = exactF(x);
        const py = originY - y * scaleY;
        if (py >= -200 && py <= H + 200) {
          if (!started) { ctx.moveTo(px, py); started = true; }
          else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();
      ctx.shadowBlur = 0;

      // 2. Draw Taylor Polynomial P_N(x) (Vivid Yellow)
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2.5;
      ctx.shadowColor = "rgba(250, 204, 21, 0.6)";
      ctx.shadowBlur = 8;
      ctx.beginPath();
      started = false;
      for (let px = 0; px < W; px += 2) {
        const x = (px - originX) / scaleX;
        const y = taylorP(x, N);
        const py = originY - y * scaleY;
        if (py >= -200 && py <= H + 200) {
          if (!started) { ctx.moveTo(px, py); started = true; }
          else ctx.lineTo(px, py);
        }
      }
      ctx.stroke();
      ctx.shadowBlur = 0;

      // Tangent / Center dot at (0, f(0))
      const f0 = exactF(0);
      const dotX = originX;
      const dotY = originY - f0 * scaleY;
      ctx.beginPath();
      ctx.arc(dotX, dotY, 5, 0, Math.PI * 2);
      ctx.fillStyle = "#f43f5e";
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Legend
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px sans-serif";
      ctx.textAlign = "left";
      const fName = l26Func === 1 ? "f(x) = e^x (참값)" : (l26Func === 2 ? "f(x) = sin x (참값)" : "f(x) = cos x (참값)");
      ctx.fillText(fName, 20, 30);

      ctx.fillStyle = "#facc15";
      ctx.fillText(`P${N}(x) (${N}차 테일러 근사 다항식)`, 20, 50);

      // Audit text update
      const statBox = document.getElementById("statL26_box");
      if (statBox) {
        const testX = 1.0;
        const trueVal = exactF(testX);
        const approxVal = taylorP(testX, N);
        const err = Math.abs(trueVal - approxVal);
        const pct = (err / Math.abs(trueVal)) * 100;

        let polyStr = "";
        if (l26Func === 1) {
          const parts = ["1"];
          if (N >= 1) parts.push("x");
          if (N >= 2) parts.push("\\frac{x^2}{2}");
          if (N >= 3) parts.push("\\frac{x^3}{6}");
          if (N >= 4) parts.push("\\frac{x^4}{24}");
          if (N >= 5) parts.push("\\frac{x^5}{120}");
          if (N >= 6) parts.push("\\cdots");
          polyStr = parts.join(" + ");
        } else if (l26Func === 2) {
          const parts = ["x"];
          if (N >= 3) parts.push("-\\frac{x^3}{6}");
          if (N >= 5) parts.push("+\\frac{x^5}{120}");
          if (N >= 7) parts.push("-\\frac{x^7}{5040}");
          if (N >= 9) parts.push("+\\frac{x^9}{362880}");
          polyStr = parts.join(" ");
        } else {
          const parts = ["1"];
          if (N >= 2) parts.push("-\\frac{x^2}{2}");
          if (N >= 4) parts.push("+\\frac{x^4}{24}");
          if (N >= 6) parts.push("-\\frac{x^6}{720}");
          if (N >= 8) parts.push("+\\frac{x^8}{40320}");
          polyStr = parts.join(" ");
        }

        statBox.innerHTML = `
          <div>• 대상 초월함수: <strong style="color: #38bdf8;">${fName}</strong></div>
          <div>• ${N}차 근사 다항식: <strong style="color: #facc15;">P_${N}(x) = ${polyStr}</strong></div>
          <div>• x = 1.0 검증: <strong style="color: #34d399;">참값 ${trueVal.toFixed(4)} vs 근사 ${approxVal.toFixed(4)} (오차 ${pct.toFixed(2)}%)</strong></div>
        `;
      }
    }
