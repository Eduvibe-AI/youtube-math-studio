    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 30 (LAW OF COSINES LAB)           */
    /* ============================================================== */
    function switchL30Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL30_${i}`);
        const content = document.getElementById(`tabL30_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture30View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode30() {
      const codeEl = document.querySelector("#manimPre30 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제30강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL30() {
      updateL30();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture30View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL30() {
      const cvs = document.getElementById("cvsLec30");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const angEl = document.getElementById("slL30_angle");
      const bEl = document.getElementById("slL30_b");
      const cEl = document.getElementById("slL30_c");
      const degA = angEl ? parseFloat(angEl.value) : 60.0;
      const b = bEl ? parseFloat(bEl.value) : 4.0;
      const c = cEl ? parseFloat(cEl.value) : 5.0;

      const vAng = document.getElementById("valL30_angle");
      const vb = document.getElementById("valL30_b");
      const vc = document.getElementById("valL30_c");
      if (vAng) vAng.innerText = degA.toFixed(0) + "°";
      if (vb) vb.innerText = b.toFixed(1);
      if (vc) vc.innerText = c.toFixed(1);

      ctx.clearRect(0, 0, W, H);

      const radA = (degA * Math.PI) / 180;
      const cosA = Math.cos(radA);
      const a2 = b * b + c * c - 2 * b * c * cosA;
      const a = Math.sqrt(Math.max(0.01, a2));

      // Coordinate placement of triangle
      // A at (originX, originY)
      // C along positive horizontal or angled
      // Let A be at (180, 290)
      const scale = 36;
      const pA = { x: 180, y: 300 };
      const pB = { x: pA.x + c * scale, y: pA.y };
      const pC = { x: pA.x + b * scale * Math.cos(radA), y: pA.y - b * scale * Math.sin(radA) };

      // Background grid
      ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
      ctx.lineWidth = 1;
      for (let x = 40; x < W; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke();
      }
      for (let y = 30; y < H; y += 30) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
      }

      // Draw sides
      // Side c: A to B
      ctx.strokeStyle = "#fbbf24";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pB.x, pB.y); ctx.stroke();

      // Side b: A to C
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pC.x, pC.y); ctx.stroke();

      // Side a: B to C
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 3.5;
      ctx.beginPath(); ctx.moveTo(pB.x, pB.y); ctx.lineTo(pC.x, pC.y); ctx.stroke();

      // Angle arc at A
      ctx.strokeStyle = "#a855f7";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(pA.x, pA.y, 28, -radA, 0);
      ctx.stroke();

      // Labels on vertices
      const pts = [
        { pt: pA, name: "A", color: "#a855f7", offX: -16, offY: 16 },
        { pt: pB, name: "B", color: "#fbbf24", offX: 12, offY: 16 },
        { pt: pC, name: "C", color: "#38bdf8", offX: 0, offY: -12 }
      ];

      pts.forEach(p => {
        ctx.beginPath();
        ctx.arc(p.pt.x, p.pt.y, 5.5, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 13px sans-serif";
        ctx.fillText(p.name, p.pt.x + p.offX, p.pt.y + p.offY);
      });

      // Side length labels
      ctx.fillStyle = "#fbbf24";
      ctx.font = "bold 12px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(`c = ${c.toFixed(1)}`, (pA.x + pB.x) / 2, pA.y + 20);

      ctx.fillStyle = "#38bdf8";
      ctx.fillText(`b = ${b.toFixed(1)}`, (pA.x + pC.x) / 2 - 16, (pA.y + pC.y) / 2 - 6);

      ctx.fillStyle = "#f43f5e";
      ctx.fillText(`a = ${a.toFixed(2)}`, (pB.x + pC.x) / 2 + 18, (pB.y + pC.y) / 2);

      // Angle label at A
      ctx.fillStyle = "#c084fc";
      ctx.font = "bold 11px sans-serif";
      ctx.fillText(`${degA.toFixed(0)}°`, pA.x + 36, pA.y - 10);

      // Status indicator on top
      const typeStr = degA < 90 ? "예각삼각형 (Acute, cos A > 0)" : (degA === 90 ? "직각삼각형 (Right, a² = b² + c²)" : "둔각삼각형 (Obtuse, cos A < 0)");
      ctx.fillStyle = degA < 90 ? "#34d399" : (degA === 90 ? "#38bdf8" : "#f43f5e");
      ctx.font = "bold 13px sans-serif";
      ctx.textAlign = "left";
      ctx.fillText(`형태: ${typeStr}`, 25, 35);

      // Update Audit Stats
      const statBox = document.getElementById("statL30_box");
      if (statBox) {
        statBox.innerHTML = `
          <div>• 코사인값: <strong style="color: #38bdf8;">cos(${degA}°) = ${cosA.toFixed(3)}</strong></div>
          <div>• 코사인 계산: <strong style="color: #facc15;">${b}² + ${c}² - 2(${b})(${c})(${cosA.toFixed(3)}) = ${a2.toFixed(2)}</strong></div>
          <div>• 대변 길이: <strong style="color: #34d399; font-size: 1.05rem;">a = √(${a2.toFixed(2)}) ≈ ${a.toFixed(2)}</strong></div>
          <div>• 삼각형 형태: <strong style="color: ${degA < 90 ? '#34d399' : '#f43f5e'};">${typeStr}</strong></div>
        `;
      }
    }
