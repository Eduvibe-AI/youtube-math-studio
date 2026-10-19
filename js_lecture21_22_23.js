    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 21 (TRIG RATIO RELATIONS)         */
    /* ============================================================== */
    let l21Target = 0.5;

    function setL21Target(tgt) {
      l21Target = tgt;
      const btns = [
        { id: "btnL21_tgt_half", val: 0.5 },
        { id: "btnL21_tgt_sq2", val: Math.SQRT1_2 },
        { id: "btnL21_tgt_sq3", val: Math.sqrt(3)/2 },
        { id: "btnL21_tgt_all", val: "all" }
      ];
      btns.forEach(b => {
        const el = document.getElementById(b.id);
        if (el) el.classList.toggle("active", b.val === tgt);
      });
      updateL21();
    }

    function switchL21Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL21_${i}`);
        const content = document.getElementById(`tabL21_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture21View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode21() {
      const codeEl = document.querySelector("#manimPre21 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제21강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL21() {
      updateL21();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture21View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL21() {
      const cvs = document.getElementById("cvsLec21");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const ampEl = document.getElementById("slL21_amp");
      const freqEl = document.getElementById("slL21_freq");
      const amp = ampEl ? parseFloat(ampEl.value) : 1.0;
      const freq = freqEl ? parseFloat(freqEl.value) : 1.0;

      const vAmp = document.getElementById("valL21_amp");
      const vFreq = document.getElementById("valL21_freq");
      if (vAmp) vAmp.innerText = amp.toFixed(1);
      if (vFreq) vFreq.innerText = freq.toFixed(2);

      const showGrid = document.getElementById("chkL21_grid") ? document.getElementById("chkL21_grid").checked : true;
      const showRatio = document.getElementById("chkL21_ratio") ? document.getElementById("chkL21_ratio").checked : true;

      ctx.clearRect(0, 0, W, H);

      // Coordinate mapping: 0 to 2*pi (x), -1.5 to 1.5 (y)
      const padL = 50, padR = 40, padT = 30, padB = 40;
      const graphW = W - padL - padR;
      const graphH = H - padT - padB;
      const midY = padT + graphH / 2;

      function toX(val) { return padL + (val / (2 * Math.PI)) * graphW; }
      function toY(val) { return midY - (val / (1.5 * amp)) * (graphH / 2); }

      // 8-Box Grid Overlay
      if (showGrid) {
        ctx.strokeStyle = "rgba(56, 189, 248, 0.2)";
        ctx.lineWidth = 1;
        ctx.setLineDash([4, 4]);

        // 4 Columns: 0, pi/2, pi, 3pi/2, 2pi
        for (let i = 0; i <= 4; i++) {
          const x = toX(i * Math.PI / 2);
          ctx.beginPath();
          ctx.moveTo(x, padT);
          ctx.lineTo(x, padT + graphH);
          ctx.stroke();
        }

        // 2 Rows: top (+amp), middle (0), bottom (-amp)
        [amp, 0, -amp].forEach(yVal => {
          const y = toY(yVal);
          ctx.beginPath();
          ctx.moveTo(padL, y);
          ctx.lineTo(padL + graphW, y);
          ctx.stroke();
        });
        ctx.setLineDash([]);
      }

      // Axes
      ctx.strokeStyle = "rgba(255, 255, 255, 0.4)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padL, midY);
      ctx.lineTo(padL + graphW + 15, midY);
      ctx.moveTo(padL, padT + graphH);
      ctx.lineTo(padL, padT - 10);
      ctx.stroke();

      // Axis labels
      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px 'Consolas', monospace";
      ctx.fillText("O", padL - 14, midY + 14);
      ctx.fillText("π/2", toX(Math.PI / 2) - 8, midY + 16);
      ctx.fillText("π", toX(Math.PI) - 4, midY + 16);
      ctx.fillText("3π/2", toX(3 * Math.PI / 2) - 10, midY + 16);
      ctx.fillText("2π", toX(2 * Math.PI) - 8, midY + 16);

      ctx.fillText(amp.toFixed(1), padL - 26, toY(amp) + 4);
      ctx.fillText((-amp).toFixed(1), padL - 30, toY(-amp) + 4);

      // Plot y = amp * sin(freq * x)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      const steps = 240;
      for (let i = 0; i <= steps; i++) {
        const xVal = (i / steps) * (2 * Math.PI);
        const yVal = amp * Math.sin(freq * xVal);
        const px = toX(xVal);
        const py = toY(yVal);
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Ratio Highlights
      const targets = (l21Target === "all") ? [0.5, Math.SQRT1_2, Math.sqrt(3)/2] : [l21Target];

      targets.forEach(tgt => {
        const tgtVal = tgt * amp;
        const tgtX1 = Math.asin(tgt) / freq;
        const tgtX2 = (Math.PI - Math.asin(tgt)) / freq;

        // Horizontal target line
        ctx.strokeStyle = (tgt === 0.5) ? "#facc15" : ((tgt === Math.SQRT1_2) ? "#c084fc" : "#34d399");
        ctx.lineWidth = 1.5;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(padL, toY(tgtVal));
        ctx.lineTo(toX(Math.PI / freq), toY(tgtVal));
        ctx.stroke();
        ctx.setLineDash([]);

        // Points
        [tgtX1, tgtX2].forEach(tx => {
          if (tx >= 0 && tx <= 2 * Math.PI) {
            const sx = toX(tx);
            const sy = toY(tgtVal);

            // Vertical drop line
            ctx.strokeStyle = "rgba(250, 204, 21, 0.4)";
            ctx.setLineDash([2, 2]);
            ctx.beginPath();
            ctx.moveTo(sx, sy);
            ctx.lineTo(sx, midY);
            ctx.stroke();
            ctx.setLineDash([]);

            // Dot
            ctx.fillStyle = (tgt === 0.5) ? "#f43f5e" : "#facc15";
            ctx.beginPath();
            ctx.arc(sx, sy, 4.5, 0, Math.PI * 2);
            ctx.fill();
            ctx.strokeStyle = "#fff";
            ctx.lineWidth = 1.5;
            ctx.stroke();
          }
        });

        // If target is 0.5 and showRatio, draw 1:2 ratio brackets on [0, pi/2]
        if (tgt === 0.5 && showRatio && freq === 1.0) {
          const x0 = toX(0);
          const x1 = toX(Math.PI / 6);
          const x2 = toX(Math.PI / 2);
          const bracketY = midY + 28;

          ctx.strokeStyle = "#facc15";
          ctx.lineWidth = 2;

          // Segment 1 (1 part)
          ctx.beginPath();
          ctx.moveTo(x0, bracketY);
          ctx.lineTo(x1, bracketY);
          ctx.stroke();

          // Segment 2 (2 parts)
          ctx.strokeStyle = "#38bdf8";
          ctx.beginPath();
          ctx.moveTo(x1, bracketY);
          ctx.lineTo(x2, bracketY);
          ctx.stroke();

          ctx.fillStyle = "#facc15";
          ctx.font = "bold 12px 'Consolas', monospace";
          ctx.fillText("비율 1", (x0 + x1)/2 - 16, bracketY + 16);

          ctx.fillStyle = "#38bdf8";
          ctx.fillText("비율 2", (x1 + x2)/2 - 16, bracketY + 16);

          // Top label
          ctx.fillStyle = "#facc15";
          ctx.font = "bold 11px sans-serif";
          ctx.fillText("★ 1:2 분할점 (π/6)", x1 - 35, toY(tgtVal) - 10);
        }
      });
    }

    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 22 (N-AXIS COMPOSITE FUNCTIONS)   */
    /* ============================================================== */
    let l22Preset = 1;
    let l22Timer = null;
    let l22Direction = 1;

    function setL22Preset(p) {
      l22Preset = p;
      for (let i = 1; i <= 3; i++) {
        const btn = document.getElementById(`btnL22_preset${i}`);
        if (btn) btn.classList.toggle("active", i === p);
      }
      updateL22();
    }

    function toggleL22AutoPlay() {
      const btn = document.getElementById("btnL22_play");
      if (l22Timer) {
        clearInterval(l22Timer);
        l22Timer = null;
        if (btn) btn.innerText = "▶ 자동 왕복 애니메이션";
      } else {
        if (btn) btn.innerText = "⏸ 정지";
        l22Timer = setInterval(() => {
          const sl = document.getElementById("slL22_x");
          if (!sl) return;
          let cur = parseFloat(sl.value) + 0.05 * l22Direction;
          if (cur >= 4.0) { cur = 4.0; l22Direction = -1; }
          else if (cur <= 0.0) { cur = 0.0; l22Direction = 1; }
          sl.value = cur.toFixed(2);
          updateL22();
        }, 35);
      }
    }

    function switchL22Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL22_${i}`);
        const content = document.getElementById(`tabL22_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture22View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode22() {
      const codeEl = document.querySelector("#manimPre22 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제22강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL22() {
      updateL22();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture22View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL22() {
      const cvs = document.getElementById("cvsLec22");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const slX = document.getElementById("slL22_x");
      const curX = slX ? parseFloat(slX.value) : 1.5;
      const vX = document.getElementById("valL22_x");
      if (vX) vX.innerText = curX.toFixed(2);

      const showFull = document.getElementById("chkL22_full") ? document.getElementById("chkL22_full").checked : true;

      ctx.clearRect(0, 0, W, H);

      // Function definitions based on preset
      function g(x) {
        if (l22Preset === 1) {
          // Triangle tent: 0->0, 2->3, 4->0
          return (x <= 2) ? 1.5 * x : 3.0 - 1.5 * (x - 2);
        } else if (l22Preset === 2) {
          // Parabola: -(x-2)^2 + 3.2
          return -(x - 2) * (x - 2) * 0.8 + 3.2;
        } else {
          // Sine: 1.5 * sin(pi*x/2) + 1.5
          return 1.5 * Math.sin((Math.PI * x) / 2) + 1.5;
        }
      }

      function f(t) {
        if (l22Preset === 1) {
          // W-shape: |t - 1.5| * 1.5 + 0.5
          return Math.abs(t - 1.5) * 1.5 + 0.5;
        } else if (l22Preset === 2) {
          // Linear / ramp: 0.8 * t + 0.4
          return 0.8 * t + 0.4;
        } else {
          // Double bump: -0.6*(t-1.8)^2 + 2.8
          return -0.6 * (t - 1.8) * (t - 1.8) + 2.8;
        }
      }

      const curT = g(curX);
      const curY = f(curT);

      const statBox = document.getElementById("statL22_box");
      if (statBox) {
        statBox.innerHTML = `
          <div>• 입력 $x = $ <strong style="color: #38bdf8;">${curX.toFixed(2)}</strong></div>
          <div>• 속함수 $t = g(x) = $ <strong style="color: #34d399;">${curT.toFixed(2)}</strong></div>
          <div>• 최종 합성값 $y = f(g(x)) = $ <strong style="color: #f43f5e;">${curY.toFixed(2)}</strong></div>
        `;
        if (window.renderMathInElement) renderMathInElement(statBox, { delimiters: [{left: '$', right: '$', display: false}] });
      }

      const originX = 260, originY = 240;
      const scaleX = 50, scaleT = 50, scaleY = 45;

      // Coordinate axes lines:
      ctx.strokeStyle = "rgba(255, 255, 255, 0.3)";
      ctx.lineWidth = 1.5;

      // Common vertical T-axis
      ctx.beginPath();
      ctx.moveTo(originX, 30);
      ctx.lineTo(originX, H - 20);
      ctx.stroke();

      // Common horizontal X-axis
      ctx.beginPath();
      ctx.moveTo(20, originY);
      ctx.lineTo(W - 20, originY);
      ctx.stroke();

      // Labels
      ctx.fillStyle = "#94a3b8";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText("x 축 (정의역)", 30, originY + 18);
      ctx.fillText("x 축", originX + 220, originY + 18);
      ctx.fillText("공통 t 축", originX + 8, 45);
      ctx.fillText("y 축 (합성 출력)", 25, 45);

      function toScreenG(x, t) { return { x: originX - x * scaleX, y: originY + t * scaleT }; }
      function toScreenF(t, y) { return { x: originX + t * scaleX, y: originY - y * scaleY }; }
      function toScreenComp(x, y) { return { x: originX - x * scaleX, y: originY - y * scaleY }; }

      // Draw g(x) curve
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let s = 0; s <= 80; s++) {
        const xVal = (s / 80) * 4.0;
        const pt = toScreenG(xVal, g(xVal));
        if (s === 0) ctx.moveTo(pt.x, pt.y);
        else ctx.lineTo(pt.x, pt.y);
      }
      ctx.stroke();
      ctx.fillStyle = "#38bdf8";
      ctx.fillText("속함수 t = g(x)", originX - 180, originY + 160);

      // Draw f(t) curve in Top-Right
      ctx.strokeStyle = "#34d399";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let s = 0; s <= 80; s++) {
        const tVal = (s / 80) * 4.0;
        const pt = toScreenF(tVal, f(tVal));
        if (s === 0) ctx.moveTo(pt.x, pt.y);
        else ctx.lineTo(pt.x, pt.y);
      }
      ctx.stroke();
      ctx.fillStyle = "#34d399";
      ctx.fillText("겉함수 y = f(t)", originX + 110, originY - 150);

      // Draw composite curve in Top-Left
      if (showFull) {
        ctx.strokeStyle = "rgba(244, 63, 94, 0.4)";
        ctx.lineWidth = 2;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        for (let s = 0; s <= 80; s++) {
          const xVal = (s / 80) * 4.0;
          const pt = toScreenComp(xVal, f(g(xVal)));
          if (s === 0) ctx.moveTo(pt.x, pt.y);
          else ctx.lineTo(pt.x, pt.y);
        }
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Laser Trace for current X
      const pInput = { x: originX - curX * scaleX, y: originY };
      const pG = toScreenG(curX, curT);
      const pAxisT = { x: originX + curT * scaleX, y: originY };
      const pF = toScreenF(curT, curY);
      const pComp = toScreenComp(curX, curY);

      // Laser lines
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);

      // 1. Input x down to g(x)
      ctx.beginPath();
      ctx.moveTo(pInput.x, pInput.y);
      ctx.lineTo(pG.x, pG.y);
      // 2. g(x) across to diagonal / common axis
      ctx.lineTo(originX, pG.y);
      ctx.stroke();

      // Arc / reflection from vertical T to horizontal T:
      ctx.strokeStyle = "rgba(250, 204, 21, 0.6)";
      ctx.beginPath();
      ctx.arc(originX, originY, curT * scaleT, Math.PI / 2, 0, true);
      ctx.stroke();

      // 3. Up to f(t)
      ctx.beginPath();
      ctx.moveTo(pAxisT.x, originY);
      ctx.lineTo(pF.x, pF.y);
      // 4. Horizontal left to composite point
      ctx.lineTo(pComp.x, pF.y);
      // 5. Down to x axis
      ctx.lineTo(pInput.x, originY);
      ctx.stroke();
      ctx.setLineDash([]);

      // Highlight Points
      [pInput, pG, pAxisT, pF, pComp].forEach((pt, idx) => {
        ctx.fillStyle = (idx === 4) ? "#f43f5e" : "#facc15";
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, (idx === 4) ? 6 : 4.5, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#fff";
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      ctx.fillStyle = "#f43f5e";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText("합성 (x, f(g(x)))", pComp.x - 30, pComp.y - 10);
    }

    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 23 (PARABOLA 7 PROPERTIES)        */
    /* ============================================================== */
    let l23Mode = 1;

    function setL23Mode(m) {
      l23Mode = m;
      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`btnL23_mode${i}`);
        if (btn) btn.classList.toggle("active", i === m);
      }
      updateL23();
    }

    function switchL23Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL23_${i}`);
        const content = document.getElementById(`tabL23_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture23View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode23() {
      const codeEl = document.querySelector("#manimPre23 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제23강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL23() {
      updateL23();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture23View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL23() {
      const cvs = document.getElementById("cvsLec23");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const pEl = document.getElementById("slL23_p");
      const angEl = document.getElementById("slL23_angle");
      const pVal = pEl ? parseFloat(pEl.value) : 1.0;
      const deg = angEl ? parseFloat(angEl.value) : 65.0;

      const vp = document.getElementById("valL23_p");
      const vang = document.getElementById("valL23_angle");
      if (vp) vp.innerText = pVal.toFixed(1);
      if (vang) vang.innerText = deg.toFixed(0) + "°";

      ctx.clearRect(0, 0, W, H);

      // Coordinate mapping: origin at (200, H/2)
      const ox = 200, oy = H / 2;
      const scale = 55;

      function toX(x) { return ox + x * scale; }
      function toY(y) { return oy - y * scale; }

      // Directrix x = -p
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(toX(-pVal), 20);
      ctx.lineTo(toX(-pVal), H - 20);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = "#f43f5e";
      ctx.font = "bold 11px sans-serif";
      ctx.fillText(`준선 x = -${pVal.toFixed(1)}`, toX(-pVal) - 65, 35);

      // Axes
      ctx.strokeStyle = "rgba(255, 255, 255, 0.3)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(20, oy); ctx.lineTo(W - 20, oy);
      ctx.moveTo(ox, H - 20); ctx.lineTo(ox, 20);
      ctx.stroke();

      // Focus F(p, 0)
      ctx.fillStyle = "#facc15";
      ctx.beginPath();
      ctx.arc(toX(pVal), oy, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillText(`F(${pVal.toFixed(1)}, 0)`, toX(pVal) - 15, oy + 20);

      // Parabola y^2 = 4px -> x = y^2 / (4p)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let y = -4.2; y <= 4.2; y += 0.05) {
        const x = (y * y) / (4 * pVal);
        const px = toX(x), py = toY(y);
        if (y === -4.2) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Focal Chord AB passing through F(p, 0) with angle theta
      const rad = (deg * Math.PI) / 180;
      const m = Math.tan(rad);

      // Intersection of line y = m(x - p) and y^2 = 4px
      const sqrtTerm = Math.sqrt(1 + m * m);
      const yA = (2 * pVal + 2 * pVal * sqrtTerm) / m;
      const xA = (yA * yA) / (4 * pVal);
      const yB = (2 * pVal - 2 * pVal * sqrtTerm) / m;
      const xB = (yB * yB) / (4 * pVal);

      const distA = Math.sqrt((xA - pVal)**2 + yA**2);
      const distB = Math.sqrt((xB - pVal)**2 + yB**2);
      const harmonicSum = (1 / distA) + (1 / distB);

      const statBox = document.getElementById("statL23_box");
      if (statBox) {
        statBox.innerHTML = `
          <div>• 초점거리 $a = \\overline{AF} = $ <strong style="color: #38bdf8;">${distA.toFixed(2)}</strong>, $b = \\overline{BF} = $ <strong style="color: #34d399;">${distB.toFixed(2)}</strong></div>
          <div>• 조화평균 계산: $\\frac{1}{a} + \\frac{1}{b} = $ <strong style="color: #facc15;">${harmonicSum.toFixed(3)}</strong></div>
          <div>• 이론값 $1/p = $ <strong style="color: #f43f5e;">${(1/pVal).toFixed(3)} (완벽 일치!)</strong></div>
        `;
        if (window.renderMathInElement) renderMathInElement(statBox, { delimiters: [{left: '$', right: '$', display: false}] });
      }

      // Draw Chord AB
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(toX(xA), toY(yA));
      ctx.lineTo(toX(xB), toY(yB));
      ctx.stroke();

      // Points A and B
      [ {x: xA, y: yA, name: "A", color: "#38bdf8"},
        {x: xB, y: yB, name: "B", color: "#34d399"} ].forEach(pt => {
        ctx.fillStyle = pt.color;
        ctx.beginPath();
        ctx.arc(toX(pt.x), toY(pt.y), 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#fff";
        ctx.stroke();
        ctx.fillText(pt.name, toX(pt.x) + 8, toY(pt.y) - 6);
      });

      // MODE 1: Harmonic mean display
      if (l23Mode === 1) {
        ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
        ctx.setLineDash([2, 2]);
        ctx.beginPath();
        ctx.moveTo(toX(xA), toY(yA)); ctx.lineTo(toX(-pVal), toY(yA));
        ctx.moveTo(toX(xB), toY(yB)); ctx.lineTo(toX(-pVal), toY(yB));
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // MODE 2: Orthogonal Tangents
      if (l23Mode === 2 || l23Mode === 1) {
        const xT = -pVal;
        const yT = (yA + yB) / 2;

        ctx.strokeStyle = "rgba(168, 85, 247, 0.8)";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(toX(xA), toY(yA)); ctx.lineTo(toX(xT), toY(yT));
        ctx.moveTo(toX(xB), toY(yB)); ctx.lineTo(toX(xT), toY(yT));
        ctx.stroke();

        ctx.fillStyle = "#c084fc";
        ctx.beginPath();
        ctx.arc(toX(xT), toY(yT), 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText("T (직각 90° 교점)", toX(xT) - 95, toY(yT) + 4);
      }

      // MODE 3: Rhombus and reflection
      if (l23Mode === 3) {
        const xInt = -xA;
        ctx.strokeStyle = "#facc15";
        ctx.lineWidth = 1.8;
        ctx.beginPath();
        ctx.moveTo(toX(xA), toY(yA)); ctx.lineTo(toX(xInt), oy);
        ctx.stroke();

        ctx.strokeStyle = "#38bdf8";
        ctx.beginPath();
        ctx.moveTo(W - 20, toY(yA)); ctx.lineTo(toX(xA), toY(yA));
        ctx.lineTo(toX(pVal), oy);
        ctx.stroke();

        ctx.fillStyle = "#facc15";
        ctx.fillText("입사 광선", W - 80, toY(yA) - 8);
        ctx.fillText("초점 집광 반사", (toX(xA) + toX(pVal))/2 - 30, (toY(yA) + oy)/2 - 10);
      }

      // MODE 4: Circle tangent to directrix
      if (l23Mode === 4) {
        const midX = (xA + xB) / 2;
        const midY = (yA + yB) / 2;
        const radCirc = Math.sqrt((xA - xB)**2 + (yA - yB)**2) / 2;

        ctx.strokeStyle = "rgba(52, 211, 153, 0.6)";
        ctx.lineWidth = 1.8;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.arc(toX(midX), toY(midY), radCirc * scale, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#34d399";
        ctx.fillText("지름원은 준선에 접함!", toX(midX) - 50, toY(midY) - radCirc * scale - 6);
      }
    }
