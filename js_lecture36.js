// ==========================================
// Lecture 36: 다항함수 거리곱 공식과 고속 개형 추론
// Canvas: cvsLec36
// ==========================================
let l36_x0 = 3.0;
let l36_polyType = 'quadratic'; // 'quadratic' or 'cubic'

function setL36PolyType(type) {
  l36_polyType = type;
  const btnQuad = document.getElementById('btnL36Quad');
  const btnCube = document.getElementById('btnL36Cube');
  if (btnQuad && btnCube) {
    if (type === 'quadratic') {
      btnQuad.style.background = '#0284c7';
      btnQuad.style.color = '#fff';
      btnCube.style.background = 'rgba(255,255,255,0.08)';
      btnCube.style.color = '#cbd5e1';
    } else {
      btnCube.style.background = '#a855f7';
      btnCube.style.color = '#fff';
      btnQuad.style.background = 'rgba(255,255,255,0.08)';
      btnQuad.style.color = '#cbd5e1';
    }
  }
  renderL36();
}

function updateL36X0(val) {
  l36_x0 = parseFloat(val);
  const lbl = document.getElementById('lblL36X0');
  if (lbl) lbl.textContent = l36_x0.toFixed(2);
  renderL36();
}

function renderL36() {
  const cvs = document.getElementById('cvsLec36');
  if (!cvs) return;
  const ctx = cvs.getContext('2d');
  const w = cvs.width = cvs.parentElement ? cvs.parentElement.clientWidth : 720;
  const h = cvs.height = 420;

  ctx.fillStyle = '#080d17';
  ctx.fillRect(0, 0, w, h);

  const ox = 90;
  const oy = h * 0.65;
  const scaleX = (w - 140) / 6.0; // x in [0, 6]
  const scaleY = (h - 100) / 7.0;

  const toX = x => ox + x * scaleX;
  const toY = y => oy - y * scaleY;

  // Grid
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
  ctx.lineWidth = 1;
  for (let x = 0; x <= 6; x++) {
    ctx.beginPath(); ctx.moveTo(toX(x), toY(-2)); ctx.lineTo(toX(x), toY(5)); ctx.stroke();
  }
  for (let y = -2; y <= 5; y++) {
    ctx.beginPath(); ctx.moveTo(toX(0), toY(y)); ctx.lineTo(toX(6), toY(y)); ctx.stroke();
  }

  // Baseline y = 0
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
  ctx.lineWidth = 1.8;
  ctx.beginPath();
  ctx.moveTo(toX(0), toY(0));
  ctx.lineTo(toX(6.2), toY(0));
  ctx.stroke();

  // Axis labels
  ctx.font = '12px Outfit, sans-serif';
  ctx.fillStyle = '#94a3b8';
  for (let x = 1; x <= 6; x++) ctx.fillText(x, toX(x) - 4, toY(0) + 18);
  ctx.fillText('x', toX(6.1), toY(0) + 18);
  ctx.fillText('y=0 (기준선)', toX(0.2), toY(0) - 8);

  const curX = l36_x0;

  if (l36_polyType === 'quadratic') {
    // f(x) = -(x-1)(x-5) = -x^2 + 6x - 5 (a = -1)
    const fnQ = x => -(x - 1) * (x - 5);

    // Plot Parabola
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.6;
    ctx.beginPath();
    for (let x = 0.5; x <= 5.5; x += 0.05) {
      const px = toX(x);
      const py = toY(fnQ(x));
      if (x === 0.5) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Roots at x1 = 1, x2 = 5
    const r1 = 1, r2 = 5;
    [r1, r2].forEach(r => {
      ctx.fillStyle = '#fbbf24';
      ctx.beginPath(); ctx.arc(toX(r), toY(0), 5, 0, Math.PI * 2); ctx.fill();
    });
    ctx.font = 'bold 12px Outfit, sans-serif';
    ctx.fillStyle = '#fbbf24';
    ctx.fillText('x₁=1', toX(r1) - 12, toY(0) - 10);
    ctx.fillText('x₂=5', toX(r2) - 12, toY(0) - 10);

    // Current point on curve
    const yVal = fnQ(curX);
    const px0 = toX(curX);
    const py0 = toY(yVal);
    const pyBase = toY(0);

    // Height vertical line
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(px0, pyBase);
    ctx.lineTo(px0, py0);
    ctx.stroke();

    // Horizontal distance lines d1 and d2
    const d1 = Math.abs(curX - r1);
    const d2 = Math.abs(curX - r2);
    const heightCalc = d1 * d2;

    ctx.strokeStyle = '#fbbf24';
    ctx.lineWidth = 1.8;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(toX(r1), pyBase); ctx.lineTo(px0, pyBase);
    ctx.moveTo(toX(r2), pyBase); ctx.lineTo(px0, pyBase);
    ctx.stroke();
    ctx.setLineDash([]);

    // Point dot
    ctx.fillStyle = '#f43f5e';
    ctx.beginPath(); ctx.arc(px0, py0, 6, 0, Math.PI * 2); ctx.fill();
    ctx.fillText(`P(${curX.toFixed(2)}, h=${Math.abs(yVal).toFixed(2)})`, px0 + 8, py0 - 8);

    // Distance labels
    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 12px Outfit, sans-serif';
    if (d1 > 0.3) ctx.fillText(`d₁=${d1.toFixed(2)}`, (toX(r1) + px0) / 2 - 15, pyBase + 34);
    if (d2 > 0.3) ctx.fillText(`d₂=${d2.toFixed(2)}`, (px0 + toX(r2)) / 2 - 15, pyBase + 34);

    // Update DOM Stats
    const cardD1 = document.getElementById('statL36D1');
    const cardD2 = document.getElementById('statL36D2');
    const cardProd = document.getElementById('statL36Prod');

    if (cardD1) cardD1.textContent = `d₁ = |x₀ - 1| = ${d1.toFixed(2)}`;
    if (cardD2) cardD2.textContent = `d₂ = |x₀ - 5| = ${d2.toFixed(2)}`;
    if (cardProd) cardProd.textContent = `h = |a|·d₁·d₂ = 1 × ${d1.toFixed(2)} × ${d2.toFixed(2)} = ${heightCalc.toFixed(2)}`;
  } else {
    // Cubic f(x) = -(x - 1)^2 * (x - 4) (Tangent at 1, root at 4)
    const fnC = x => -(x - 1)**2 * (x - 4);

    ctx.strokeStyle = '#c084fc';
    ctx.lineWidth = 2.6;
    ctx.beginPath();
    for (let x = 0.5; x <= 4.4; x += 0.04) {
      const px = toX(x);
      const py = toY(fnC(x));
      if (x === 0.5) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Roots at x=1 (tangent) and x=4
    ctx.fillStyle = '#fbbf24';
    ctx.beginPath(); ctx.arc(toX(1), toY(0), 5, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.arc(toX(4), toY(0), 5, 0, Math.PI * 2); ctx.fill();

    ctx.font = 'bold 12px Outfit, sans-serif';
    ctx.fillStyle = '#fbbf24';
    ctx.fillText('x₁=1 (접점 d₁²)', toX(1) - 25, toY(0) - 10);
    ctx.fillText('x₂=4 (교점 d₂)', toX(4) - 15, toY(0) - 10);

    const yVal = fnC(curX);
    const px0 = toX(curX);
    const py0 = toY(yVal);
    const pyBase = toY(0);

    // Height vertical line
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(px0, pyBase); ctx.lineTo(px0, py0); ctx.stroke();

    const d1 = Math.abs(curX - 1);
    const d2 = Math.abs(curX - 4);
    const heightCalc = (d1**2) * d2;

    ctx.fillStyle = '#f43f5e';
    ctx.beginPath(); ctx.arc(px0, py0, 6, 0, Math.PI * 2); ctx.fill();
    ctx.fillText(`P(${curX.toFixed(2)}, h=${Math.abs(yVal).toFixed(2)})`, px0 + 8, py0 - 8);

    // Update DOM Stats
    const cardD1 = document.getElementById('statL36D1');
    const cardD2 = document.getElementById('statL36D2');
    const cardProd = document.getElementById('statL36Prod');

    if (cardD1) cardD1.textContent = `d₁ (접점) = ${d1.toFixed(2)} → d₁² = ${(d1**2).toFixed(2)}`;
    if (cardD2) cardD2.textContent = `d₂ (교점) = ${d2.toFixed(2)}`;
    if (cardProd) cardProd.textContent = `h = |a|·d₁²·d₂ = ${(d1**2).toFixed(2)} × ${d2.toFixed(2)} = ${heightCalc.toFixed(2)}`;
  }
}

window.addEventListener('resize', () => {
  const v36 = document.getElementById('lecture36View');
  if (v36 && v36.style.display !== 'none') renderL36();
});
