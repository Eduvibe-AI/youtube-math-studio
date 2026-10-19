    /* ============================================================== */
    /* JAVASCRIPT LOGIC FOR LECTURE 29 (LIMIT TRUTH TESTING)          */
    /* ============================================================== */
    let l29Case = 1;

    const L29_CASES = [
      null,
      {
        prop: "lim f(x) 와 lim [f(x) + g(x)] 가 수렴  ⟹  lim g(x) 수렴",
        sub: "f(x) + g(x) = h(x)  ⟹  g(x) = h(x) - f(x)",
        isTrue: true,
        reason: "수렴하는 두 함수 h(x)와 f(x)의 뺄셈이므로 나눗셈이 없어 분모가 0이 될 위험이 전혀 없음.",
        flow: ["f(x) 수렴", "h(x) 수렴", "g(x) = h(x) - f(x)", "100% 수렴 (참)"]
      },
      {
        prop: "lim f(x) 와 lim [f(x) · g(x)] 가 수렴  ⟹  lim g(x) 수렴",
        sub: "f(x) · g(x) = k(x)  ⟹  g(x) = k(x) / f(x)",
        isTrue: false,
        reason: "분모에 위치한 f(x)의 극한값이 0이 되는 경우(lim f(x) = 0) 나눗셈이 불가능하여 발산할 수 있음. (반례: f(x)=0, g(x)=1/x)",
        flow: ["f(x) 수렴", "k(x) 수렴", "g(x) = k(x) / f(x)", "lim f(x)=0 가능! (거짓)"]
      },
      {
        prop: "lim f(x) 와 lim [g(x) / f(x)] 가 수렴  ⟹  lim g(x) 수렴",
        sub: "g(x) / f(x) = h(x)  ⟹  g(x) = f(x) · h(x)",
        isTrue: true,
        reason: "g(x)가 수렴하는 두 함수의 곱 f(x) · h(x)로 표현되므로 분모에 0이 들어갈 걱정 없이 곱셈 법칙 성립.",
        flow: ["f(x) 수렴", "h(x) 수렴", "g(x) = f(x) · h(x)", "100% 수렴 (참)"]
      },
      {
        prop: "lim [f(x) + g(x)] 와 lim [f(x) - g(x)] 가 수렴  ⟹  lim f(x) 수렴",
        sub: "f+g = h, f-g = k  ⟹  f(x) = (h(x) + k(x)) / 2",
        isTrue: true,
        reason: "상수 2로 나누는 것은 분모가 0이 아니므로 수렴하는 두 함수의 덧셈 후 상수배는 무조건 수렴.",
        flow: ["h(x) 수렴", "k(x) 수렴", "f(x) = (h + k)/2", "100% 수렴 (참)"]
      }
    ];

    function setL29Case(c) {
      l29Case = c;
      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`btnL29_case${i}`);
        if (btn) btn.classList.toggle("active", i === c);
      }
      updateL29();
    }

    function switchL29Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL29_${i}`);
        const content = document.getElementById(`tabL29_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture29View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode29() {
      const codeEl = document.querySelector("#manimPre29 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("제29강 Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL29() {
      updateL29();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture29View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function updateL29() {
      const cvs = document.getElementById("cvsLec29");
      if (!cvs) return;
      const ctx = cvs.getContext("2d");
      const W = cvs.width, H = cvs.height;

      ctx.clearRect(0, 0, W, H);

      const info = L29_CASES[l29Case] || L29_CASES[1];

      // Background grid
      ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
      ctx.lineWidth = 1;
      for (let x = 40; x < W; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke();
      }
      for (let y = 30; y < H; y += 30) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
      }

      // Card Header Box
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.strokeStyle = info.isTrue ? "rgba(52, 211, 153, 0.4)" : "rgba(244, 63, 94, 0.4)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.roundRect(30, 25, W - 60, 70, 12);
      ctx.fill();
      ctx.stroke();

      // Proposition Text
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px sans-serif";
      ctx.textAlign = "left";
      ctx.fillText("[명제]", 45, 52);
      ctx.fillStyle = "#f8fafc";
      ctx.font = "14px sans-serif";
      ctx.fillText(info.prop, 95, 52);

      // Substitution Text
      ctx.fillStyle = "#facc15";
      ctx.font = "bold 13px sans-serif";
      ctx.fillText("[치환]", 45, 76);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "13px sans-serif";
      ctx.fillText(info.sub, 95, 76);

      // 4 Flow Step Cards
      const cardY = 120;
      const cardW = 120;
      const cardH = 80;
      const gap = 15;
      const startX = 35;

      info.flow.forEach((step, idx) => {
        const cx = startX + idx * (cardW + gap);
        const isLast = idx === 3;
        const color = isLast ? (info.isTrue ? "#34d399" : "#f43f5e") : "#38bdf8";

        ctx.fillStyle = "rgba(15, 23, 42, 0.75)";
        ctx.strokeStyle = color;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.roundRect(cx, cardY, cardW, cardH, 10);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#94a3b8";
        ctx.font = "11px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(`Step ${idx + 1}`, cx + cardW / 2, cardY + 24);

        ctx.fillStyle = color;
        ctx.font = isLast ? "bold 13px sans-serif" : "bold 12px sans-serif";
        ctx.fillText(step, cx + cardW / 2, cardY + 52);

        // Arrow
        if (idx < 3) {
          const arrowX = cx + cardW + gap / 2;
          ctx.fillStyle = "#64748b";
          ctx.font = "bold 14px sans-serif";
          ctx.fillText("➔", arrowX, cardY + 45);
        }
      });

      // Big Verdict Banner
      const bannerY = 225;
      ctx.fillStyle = info.isTrue ? "rgba(52, 211, 153, 0.15)" : "rgba(244, 63, 94, 0.15)";
      ctx.strokeStyle = info.isTrue ? "#34d399" : "#f43f5e";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.roundRect(30, bannerY, W - 60, 160, 14);
      ctx.fill();
      ctx.stroke();

      // Verdict Stamp
      ctx.fillStyle = info.isTrue ? "#34d399" : "#f43f5e";
      ctx.font = "bold 24px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(info.isTrue ? "✔ 참 (TRUE)" : "✖ 거짓 (FALSE)", W / 2, bannerY + 45);

      // Reasoning
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "13px sans-serif";
      ctx.textAlign = "left";
      ctx.fillText("📌 핵심 판정 근거:", 55, bannerY + 80);

      // Wrap reason
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px sans-serif";
      const reasonWords = info.reason.split(" ");
      let line = "";
      let ly = bannerY + 105;
      for (let n = 0; n < reasonWords.length; n++) {
        const testLine = line + reasonWords[n] + " ";
        if (ctx.measureText(testLine).width > W - 120 && n > 0) {
          ctx.fillText(line, 55, ly);
          line = reasonWords[n] + " ";
          ly += 22;
        } else {
          line = testLine;
        }
      }
      ctx.fillText(line, 55, ly);

      // Update Audit HTML
      const statBox = document.getElementById("statL29_box");
      if (statBox) {
        statBox.innerHTML = `
          <div>• 선택 명제: <strong style="color: #38bdf8;">${info.prop}</strong></div>
          <div>• 치환 관계식: <strong style="color: #facc15;">${info.sub}</strong></div>
          <div>• 최종 판정: <strong style="color: ${info.isTrue ? '#34d399' : '#f43f5e'}; font-size: 1.1rem;">${info.isTrue ? '✔ 참 (True)' : '✖ 거짓 (False)'}</strong></div>
          <div>• 이유: <strong style="color: #cbd5e1;">${info.reason}</strong></div>
        `;
      }
    }
