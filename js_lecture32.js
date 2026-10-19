// ==========================================
// Lecture 32: 지수·로그 확대·축소 & 실전 비율 관계
// Canvas: cvsLec32
// ==========================================
let l32_k = 4.0;
let l32_m = 4.0;
let l32_mode = 'exp'; // 'exp' (수평 1:1) or 'log' (수직 1:2)

function setL32Mode(mode) {
  l32_mode = mode;
  const btnExp = document.getElementById('btnL32Exp');
  const btnLog = document.getElementById('btnL32Log');
  if (btnExp && btnLog) {
    if (mode === 'exp') {
      btnExp.style.background = '#0284c7';
      btnExp.style.color = '#fff';
      btnLog.style.background = 'rgba(255,255,255,0.08)';
      btnLog.style.color = '#cbd5e1';
    } else {
      btnLog.style.background = '#a855f7';
      btnLog.style.color = '#fff';
      btnExp.style.background = 'rgba(255,255,255,0.08)';
      btnExp.style.color = '#cbd5e1';
    }
  }
  renderL32();
}

function updateL32K(val) {
  l32_k = parseFloat(val);
  const lbl = document.getElementById('lblL32K');
  if (lbl) lbl.textContent = l32_k.toFixed(2);
  renderL32();
}

function updateL32M(val) {
  l32_m = parseFloat(val);
  const lbl = document.getElementById('lblL32M');
  if (lbl) lbl.textContent = l32_m.toFixed(2);
  renderL32();
}

function renderL32() {
  const cvs = document.getElementById('cvsLec32');
  if (!cvs) return;
  const ctx = cvs.getContext('2d');
  const w = cvs.width = cvs.parentElement ? cvs.parentElement.clientWidth : 720;
  const h = cvs.height = 440;

  ctx.fillStyle = '#080d17';
  ctx.fillRect(0, 0, w, h);

  // Coordinate setup
  const ox = 90;
  const oy = h - 60;
  const scaleX = (w - 140) / 5.5;
  const scaleY = (h - 100) / 8.5;

  const toX = x => ox + x * scaleX;
  const toY = y => oy - y * scaleY;

  // Grid
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
  ctx.lineWidth = 1;
  for (let x = 0; x <= 5; x += 1) {
    ctx.beginPath();
    ctx.moveTo(toX(x), toY(-0.5));
    ctx.lineTo(toX(x), toY(8));
    ctx.stroke();
  }
  for (let y = 0; y <= 8; y += 1) {
    ctx.beginPath();
    ctx.moveTo(toX(-0.5), toY(y));
    ctx.lineTo(toX(5.5), toY(y));
    ctx.stroke();
  }

  // Axes
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)';
  ctx.lineWidth = 1.8;
  ctx.beginPath();
  ctx.moveTo(toX(-0.5), toY(0));
  ctx.lineTo(toX(5.3), toY(0));
  ctx.moveTo(toX(0), toY(-0.5));
  ctx.lineTo(toX(0), toY(8.2));
  ctx.stroke();

  // Axis Labels
  ctx.fillStyle = '#94a3b8';
  ctx.font = '12px Outfit, sans-serif';
  ctx.fillText('x', toX(5.2), toY(0) + 18);
  ctx.fillText('y', toX(0) - 18, toY(8.1));
  ctx.fillText('O', toX(0) - 15, toY(0) + 16);

  for (let x = 1; x <= 5; x++) {
    ctx.fillText(x, toX(x) - 4, toY(0) + 16);
  }
  for (let y = 2; y <= 8; y += 2) {
    ctx.fillText(y, toX(0) - 20, toY(y) + 4);
  }

  if (l32_mode === 'exp') {
    // Mode EXP: y = 2^x and y = 4^x = 2^(2x)
    // 1. Plot y = 2^x (Sky Blue)
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let px = 0; px <= w; px += 2) {
      const x = (px - ox) / scaleX;
      if (x >= -0.5 && x <= 3.2) {
        const y = Math.pow(2, x);
        const py = toY(y);
        if (px === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
    }
    ctx.stroke();

    // 2. Plot y = 4^x (Emerald)
    ctx.strokeStyle = '#34d399';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let px = 0; px <= w; px += 2) {
      const x = (px - ox) / scaleX;
      if (x >= -0.5 && x <= 1.6) {
        const y = Math.pow(4, x);
        const py = toY(y);
        if (px === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
    }
    ctx.stroke();

    // Curve labels
    ctx.font = 'bold 13px Outfit, sans-serif';
    ctx.fillStyle = '#34d399';
    ctx.fillText('y = 4^x = 2^(2x)', toX(1.4) - 40, toY(6.8));
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('y = 2^x', toX(2.8) + 8, toY(7.0));

    // Horizontal Line y = l32_k
    const yVal = l32_k;
    const py = toY(yVal);

    ctx.strokeStyle = '#fbbf24';
    ctx.lineWidth = 1.8;
    ctx.setLineDash([5, 4]);
    ctx.beginPath();
    ctx.moveTo(toX(0), py);
    ctx.lineTo(toX(4.5), py);
    ctx.stroke();
    ctx.setLineDash([]);

    // Intersection points
    const xA = Math.log2(yVal) / 2; // 4^x = yVal
    const xB = Math.log2(yVal);     // 2^x = yVal

    // Segment OA and AB
    const pxO = toX(0);
    const pxA = toX(xA);
    const pxB = toX(xB);

    // Thick highlight on horizontal line
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 3.5;
    ctx.beginPath();
    ctx.moveTo(pxO, py);
    ctx.lineTo(pxB, py);
    ctx.stroke();

    // Dots
    ctx.fillStyle = '#fb7185';
    ctx.beginPath(); ctx.arc(pxA, py, 6, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath(); ctx.arc(pxB, py, 6, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#94a3b8';
    ctx.beginPath(); ctx.arc(pxO, py, 4, 0, Math.PI * 2); ctx.fill();

    // Point Labels
    ctx.font = 'bold 12px Outfit, sans-serif';
    ctx.fillStyle = '#fb7185';
    ctx.fillText(`A(${xA.toFixed(2)}, ${yVal.toFixed(1)})`, pxA - 20, py - 12);
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`B(${xB.toFixed(2)}, ${yVal.toFixed(1)})`, pxB + 8, py - 12);

    // 1 : 1 bracket indicator
    ctx.strokeStyle = '#fbbf24';
    ctx.lineWidth = 1.5;
    const braceY = py + 22;
    // Tick marks
    ctx.beginPath();
    ctx.moveTo(pxO, py + 6); ctx.lineTo(pxO, braceY);
    ctx.moveTo(pxA, py + 6); ctx.lineTo(pxA, braceY);
    ctx.moveTo(pxB, py + 6); ctx.lineTo(pxB, braceY);
    ctx.stroke();

    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 13px Outfit, sans-serif';
    ctx.fillText('1', (pxO + pxA) / 2 - 4, braceY + 16);
    ctx.fillText('1', (pxA + pxB) / 2 - 4, braceY + 16);
    ctx.fillText('(비율 1 : 1 중점)', (pxO + pxB) / 2 - 45, braceY + 32);

    // Stat Cards
    const cardA = document.getElementById('statL32ValA');
    const cardB = document.getElementById('statL32ValB');
    const cardRatio = document.getElementById('statL32ValRatio');
    if (cardA) cardA.textContent = `xA = ${xA.toFixed(2)}`;
    if (cardB) cardB.textContent = `xB = ${xB.toFixed(2)}`;
    if (cardRatio) cardRatio.textContent = `xA : (xB - xA) = 1 : 1 (OA = AB = ${xA.toFixed(2)})`;
  } else {
    // Mode LOG: y = log_2(x) and y = log_4(x) = (1/2)log_2(x)
    // 1. Plot y = log_2(x) (Purple)
    ctx.strokeStyle = '#c084fc';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let px = toX(0.08); px <= toX(5.2); px += 2) {
      const x = (px - ox) / scaleX;
      if (x > 0.05) {
        const y = Math.log2(x);
        const py = toY(y);
        if (px === toX(0.08)) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
    }
    ctx.stroke();

    // 2. Plot y = log_4(x) (Pink)
    ctx.strokeStyle = '#f472b6';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let px = toX(0.08); px <= toX(5.2); px += 2) {
      const x = (px - ox) / scaleX;
      if (x > 0.05) {
        const y = 0.5 * Math.log2(x);
        const py = toY(y);
        if (px === toX(0.08)) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
    }
    ctx.stroke();

    // Labels
    ctx.font = 'bold 13px Outfit, sans-serif';
    ctx.fillStyle = '#c084fc';
    ctx.fillText('y = log_2(x)', toX(4.2), toY(2.2));
    ctx.fillStyle = '#f472b6';
    ctx.fillText('y = log_4(x) = (1/2)log_2(x)', toX(3.5), toY(1.0) + 20);

    // Vertical line x = l32_m
    const xVal = l32_m;
    const px = toX(xVal);

    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1.8;
    ctx.setLineDash([5, 4]);
    ctx.beginPath();
    ctx.moveTo(px, toY(-0.5));
    ctx.lineTo(px, toY(3.5));
    ctx.stroke();
    ctx.setLineDash([]);

    const yC = 0.5 * Math.log2(xVal);
    const yD = Math.log2(xVal);

    const pyBase = toY(0);
    const pyC = toY(yC);
    const pyD = toY(yD);

    // Highlight vertical segment
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 3.5;
    ctx.beginPath();
    ctx.moveTo(px, pyBase);
    ctx.lineTo(px, pyD);
    ctx.stroke();

    // Dots
    ctx.fillStyle = '#f472b6';
    ctx.beginPath(); ctx.arc(px, pyC, 6, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#c084fc';
    ctx.beginPath(); ctx.arc(px, pyD, 6, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#94a3b8';
    ctx.beginPath(); ctx.arc(px, pyBase, 4, 0, Math.PI * 2); ctx.fill();

    // Labels
    ctx.font = 'bold 12px Outfit, sans-serif';
    ctx.fillStyle = '#f472b6';
    ctx.fillText(`C(${xVal.toFixed(1)}, ${yC.toFixed(2)})`, px + 10, pyC + 4);
    ctx.fillStyle = '#c084fc';
    ctx.fillText(`D(${xVal.toFixed(1)}, ${yD.toFixed(2)})`, px + 10, pyD - 8);

    // Bracket for 1 : 1 (Total height 2)
    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 13px Outfit, sans-serif';
    ctx.fillText('1', px - 18, (pyBase + pyC) / 2 + 4);
    ctx.fillText('1', px - 18, (pyC + pyD) / 2 + 4);
    ctx.fillText('높이비 1 : 2', px - 40, pyD - 20);

    // Stat Cards
    const cardA = document.getElementById('statL32ValA');
    const cardB = document.getElementById('statL32ValB');
    const cardRatio = document.getElementById('statL32ValRatio');
    if (cardA) cardA.textContent = `yC = ${yC.toFixed(2)}`;
    if (cardB) cardB.textContent = `yD = ${yD.toFixed(2)}`;
    if (cardRatio) cardRatio.textContent = `yC : yD = 1 : 2 (yD - yC = yC = ${yC.toFixed(2)})`;
  }
}

window.addEventListener('resize', () => {
  const v32 = document.getElementById('lecture32View');
  if (v32 && v32.style.display !== 'none') renderL32();
});
