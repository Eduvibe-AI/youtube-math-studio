    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 24 (TOP-TIER THINKING PROCESS)    */
    /* ============================================================== */
    let l24Mode = 1;

    function setL24Mode(m) {
      l24Mode = m;
      for (let i = 1; i <= 3; i++) {
        const btn = document.getElementById(`btnL24_mode${i}`);
        if (btn) btn.classList.toggle("active", i === m);
      }
      updateL24();
    }

    function switchL24Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL24_${i}`);
        const content = document.getElementById(`tabL24_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture24View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode24() {
      const codeEl = document.querySelector("#manimPre24 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제24강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL24() {
      updateL24();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture24View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL24() {
      const cvs = document.getElementById("cvsLec24");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      const angEl = document.getElementById("slL24_angle");
      const abEl = document.getElementById("slL24_ab");
      const degB = angEl ? parseFloat(angEl.value) : 60.0;
      const lenAB = abEl ? parseFloat(abEl.value) : 3.0;

      const vAng = document.getElementById("valL24_angle");
      const vAB = document.getElementById("valL24_ab");
      if (vAng) vAng.innerText = degB.toFixed(0) + "°";
      if (vAB) vAB.innerText = lenAB.toFixed(1);

      ctx.clearRect(0, 0, W, H);

      // Solve for x = BC using Cosine rule:
      // AC^2 = 13
      // 13 = lenAB^2 + x^2 - 2 * lenAB * x * cos(degB)
      // x^2 - (2 * lenAB * cosB) * x + (lenAB^2 - 13) = 0
      const radB = (degB * Math.PI) / 180;
      const cosB = Math.cos(radB);
      const bCoeff = -2 * lenAB * cosB;
      const cCoeff = lenAB * lenAB - 13.0;
      const disc = bCoeff * bCoeff - 4 * cCoeff;

      let lenBC = 4.0;
      if (disc >= 0) {
        const root1 = (-bCoeff + Math.sqrt(disc)) / 2;
        const root2 = (-bCoeff - Math.sqrt(disc)) / 2;
        lenBC = Math.max(root1, root2);
      }

      const areaS1 = 0.5 * lenAB * lenBC * Math.sin(radB);

      const statBox = document.getElementById("statL24_box");
      if (statBox) {
        statBox.innerHTML = `
          <div>• 코사인 2차 방정식: <strong style="color: #38bdf8;">$x^2 - ${( -bCoeff ).toFixed(2)}x + ${( cCoeff ).toFixed(2)} = 0$</strong></div>
          <div>• 공통선분 해: <strong style="color: #34d399;">$x = \\overline{BC} = ${lenBC.toFixed(2)}$</strong></div>
          <div>• $\\triangle ABC$ 넓이 $S_1 = $ <strong style="color: #f43f5e;">${areaS1.toFixed(3)}</strong></div>
        `;
        if (window.renderMathInElement) renderMathInElement(statBox, { delimiters: [{left: '$', right: '$', display: false}] });
      }

      // Drawing Geometry on Canvas
      // Origin at B(120, 290)
      const scale = 52;
      const ox = 120, oy = 290;

      const pB = { x: ox, y: oy };
      const pC = { x: ox + lenBC * scale, y: oy };
      const pA = {
        x: ox + lenAB * scale * Math.cos(radB),
        y: oy - lenAB * scale * Math.sin(radB)
      };
      // Point D forming adjacent triangle ACD
      const pD = {
        x: pC.x + 1.8 * scale,
        y: pC.y - 2.2 * scale
      };

      // Draw Circumcircle if Mode 3
      if (l24Mode === 3) {
        // Circumcircle through A, B, C
        // circumradius R = AC / (2 * sin B)
        const lenAC = Math.sqrt(13);
        const R = lenAC / (2 * Math.sin(radB));
        ctx.strokeStyle = "rgba(168, 85, 247, 0.35)";
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        // Approximate circumcenter
        const midBC = (pB.x + pC.x) / 2;
        const cy = oy - Math.sqrt(Math.max(0, (R*scale)**2 - ((lenBC*scale)/2)**2));
        ctx.arc(midBC, cy, R * scale, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#c084fc";
        ctx.font = "bold 11px sans-serif";
        ctx.fillText(`외접원 2R = ${(2*R).toFixed(2)}`, midBC - 40, cy - R * scale - 6);
      }

      // Fill Triangle ABC
      ctx.fillStyle = "rgba(56, 189, 248, 0.08)";
      ctx.beginPath();
      ctx.moveTo(pB.x, pB.y);
      ctx.lineTo(pA.x, pA.y);
      ctx.lineTo(pC.x, pC.y);
      ctx.closePath();
      ctx.fill();

      // Fill Triangle ACD
      ctx.fillStyle = "rgba(52, 211, 153, 0.08)";
      ctx.beginPath();
      ctx.moveTo(pA.x, pA.y);
      ctx.lineTo(pC.x, pC.y);
      ctx.lineTo(pD.x, pD.y);
      ctx.closePath();
      ctx.fill();

      // Draw Edges
      // AB
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(pB.x, pB.y); ctx.lineTo(pA.x, pA.y);
      ctx.stroke();

      // BC (Common chord highlighted in GOLD if Mode 1)
      ctx.strokeStyle = (l24Mode === 1) ? "#facc15" : "#64748b";
      ctx.lineWidth = (l24Mode === 1) ? 4.5 : 2.5;
      ctx.beginPath();
      ctx.moveTo(pB.x, pB.y); ctx.lineTo(pC.x, pC.y);
      ctx.stroke();

      // AC
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(pA.x, pA.y); ctx.lineTo(pC.x, pC.y);
      ctx.stroke();

      // CD and AD
      ctx.strokeStyle = "#34d399";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(pC.x, pC.y); ctx.lineTo(pD.x, pD.y);
      ctx.lineTo(pA.x, pA.y);
      ctx.stroke();

      // Angle Arc at B
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(pB.x, pB.y, 28, 0, -radB, true);
      ctx.stroke();
      ctx.fillStyle = "#facc15";
      ctx.font = "bold 12px sans-serif";
      ctx.fillText(`${degB.toFixed(0)}°`, pB.x + 34, pB.y - 12);

      // Vertices Dots & Labels
      const pts = [
        { pt: pB, name: "B", color: "#fff", offX: -16, offY: 16 },
        { pt: pA, name: "A", color: "#38bdf8", offX: -6, offY: -12 },
        { pt: pC, name: "C", color: "#facc15", offX: 8, offY: 16 },
        { pt: pD, name: "D", color: "#34d399", offX: 10, offY: -6 }
      ];

      pts.forEach(p => {
        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.pt.x, p.pt.y, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#000";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = p.color;
        ctx.font = "bold 14px sans-serif";
        ctx.fillText(p.name, p.pt.x + p.offX, p.pt.y + p.offY);
      });

      // Edge Labels
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px 'Consolas', monospace";
      ctx.fillText(`c = ${lenAB.toFixed(1)}`, (pB.x + pA.x)/2 - 38, (pB.y + pA.y)/2);

      ctx.fillStyle = "#f43f5e";
      ctx.fillText("√13", (pA.x + pC.x)/2 + 10, (pA.y + pC.y)/2);

      ctx.fillStyle = (l24Mode === 1) ? "#facc15" : "#94a3b8";
      ctx.font = "bold 13px 'Consolas', monospace";
      ctx.fillText(`공통선분 x = ${lenBC.toFixed(2)}`, (pB.x + pC.x)/2 - 45, pB.y + 24);

      // Area tags
      ctx.fillStyle = "rgba(56, 189, 248, 0.8)";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("S₁", (pB.x + pA.x + pC.x)/3 - 10, (pB.y + pA.y + pC.y)/3);

      ctx.fillStyle = "rgba(52, 211, 153, 0.8)";
      ctx.fillText("S₂", (pA.x + pC.x + pD.x)/3 - 10, (pA.y + pC.y + pD.y)/3);

      // Mode Callout Banner
      if (l24Mode === 1) {
        ctx.fillStyle = "rgba(250, 204, 21, 0.15)";
        ctx.strokeStyle = "#facc15";
        ctx.lineWidth = 1.5;
        ctx.fillRect(10, 10, 310, 48);
        ctx.strokeRect(10, 10, 310, 48);

        ctx.fillStyle = "#facc15";
        ctx.font = "bold 12px sans-serif";
        ctx.fillText("★ 1등급 필연성: 공통변 x 우선 지정", 20, 28);
        ctx.fillStyle = "#fff";
        ctx.font = "11px sans-serif";
        ctx.fillText("x가 구해지면 삼각형 ACD의 미지수가 연속 해금됩니다!", 20, 45);
      } else if (l24Mode === 2) {
        ctx.fillStyle = "rgba(244, 63, 94, 0.15)";
        ctx.strokeStyle = "#f43f5e";
        ctx.lineWidth = 1.5;
        ctx.fillRect(10, 10, 310, 48);
        ctx.strokeRect(10, 10, 310, 48);

        ctx.fillStyle = "#f43f5e";
        ctx.font = "bold 12px sans-serif";
        ctx.fillText("⚠️ 하위권의 실수: 각 β를 미지수로 두는 함정", 20, 28);
        ctx.fillStyle = "#fff";
        ctx.font = "11px sans-serif";
        ctx.fillText("β는 독립되어 있어 인접 삼각형과 연결되지 않습니다!", 20, 45);
      }
    }
