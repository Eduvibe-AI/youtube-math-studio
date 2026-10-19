// ==========================================
// Lecture 37: 삼차함수 비율관계와 극대·극소 높이차 공식
// Canvas: cvsLec37
// ==========================================
let l37_L = 2.0; // Distance between local max and local min
let l37_a = 1.0; // Leading coefficient

function updateL37L(val) {
  l37_L = parseFloat(val);
  const lbl = document.getElementById('lblL37L');
  if (lbl) lbl.textContent = l37_L.toFixed(2);
  renderL37();
}

function updateL37A(val) {
  l37_a = parseFloat(val);
  const lbl = document.getElementById('lblL37A');
  if (lbl) lbl.textContent = l37_a.toFixed(2);
  renderL37();
}

function renderL37() {
  const cvs = document.getElementById('cvsLec37');
  if (!cvs) return;
  const ctx = cvs.getContext('2d');
  const w = cvs.width = cvs.parentElement ? cvs.parentElement.clientWidth : 720;
  const h = cvs.height = 440;

  ctx.fillStyle = '#080d17';
  ctx.fillRect(0, 0, w, h);

  const L = l37_L;
  const a = l37_a;
  const H = (a / 2) * Math.pow(L, 3); // Height difference formula

  // Set inflection point at x = 0, y = 0
  // Local max at x = -L/2, Local min at x = +L/2
  // Tangent at max (y = H/2) touches again at x = L
  // Tangent at min (y = -H/2) touches again at x = -L
  // Coordinates range: x in [-1.5*L, 1.5*L], y in [-0.8*H, 0.8*H]
  const ox = w * 0.45;
  const oy = h * 0.52;

  const maxSpanX = Math.max(3.2, 1.5 * L);
  const maxSpanY = Math.max(4.5, 0.8 * H);

  const scaleX = (w * 0.38) / maxSpanX;
  const scaleY = (h * 0.38) / maxSpanY;

  const toX = x => ox + x * scaleX;
  const toY = y => oy - y * scaleY;

  // Grid
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(toX(-maxSpanX), toY(0)); ctx.lineTo(toX(maxSpanX), toY(0));
  ctx.moveTo(toX(0), toY(-maxSpanY)); ctx.lineTo(toX(0), toY(maxSpanY));
  ctx.stroke();

  // Cubic function: f'(x) = 3a (x + L/2)(x - L/2) = 3a(x^2 - L^2/4)
  // f(x) = a x^3 - (3/4) a L^2 x
  const fnCubic = x => a * Math.pow(x, 3) - 0.75 * a * Math.pow(L, 2) * x;

  // 1:1:1:1 Box Guidelines
  const xPts = [-L, -L/2, 0, L/2, L];
  const colPts = ['#34d399', '#f43f5e', '#cbd5e1', '#38bdf8', '#fbbf24'];
  const lblNames = ['접점(-L)', '극대(-L/2)', '변곡점(0)', '극소(+L/2)', '교점(+L)'];

  // Horizontal Tangents
  const yMax = fnCubic(-L/2); // +H/2
  const yMin = fnCubic(L/2);  // -H/2

  ctx.strokeStyle = 'rgba(251, 191, 36, 0.4)';
  ctx.lineWidth = 1.6;
  ctx.setLineDash([5, 4]);
  ctx.beginPath();
  ctx.moveTo(toX(-maxSpanX), toY(yMax)); ctx.lineTo(toX(maxSpanX), toY(yMax));
  ctx.moveTo(toX(-maxSpanX), toY(yMin)); ctx.lineTo(toX(maxSpanX), toY(yMin));
  ctx.stroke();
  ctx.setLineDash([]);

  // Vertical 1:1:1:1 division lines
  xPts.forEach((xp, i) => {
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.lineWidth = 1.2;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(toX(xp), toY(yMin) + 25);
    ctx.lineTo(toX(xp), toY(yMax) - 25);
    ctx.stroke();
    ctx.setLineDash([]);

    // Dots on curve
    const yp = fnCubic(xp);
    ctx.fillStyle = colPts[i];
    ctx.beginPath(); ctx.arc(toX(xp), toY(yp), 5, 0, Math.PI * 2); ctx.fill();

    // Bottom labels
    ctx.font = '11px Outfit, sans-serif';
    ctx.fillStyle = colPts[i];
    ctx.fillText(lblNames[i], toX(xp) - 22, toY(yMin) + 40);
  });

  // Draw 1:1:1:1 ratio brackets along top tangent
  ctx.font = 'bold 12px Outfit, sans-serif';
  ctx.fillStyle = '#fbbf24';
  for (let i = 0; i < 4; i++) {
    const midX = (toX(xPts[i]) + toX(xPts[i+1])) / 2;
    ctx.fillText('1', midX - 4, toY(yMax) - 12);
  }
  ctx.fillText('균등 1 : 1 : 1 : 1 4등분 박스', toX(-L/2) - 30, toY(yMax) - 30);

  // Plot Cubic Curve
  ctx.strokeStyle = '#f8fafc';
  ctx.lineWidth = 2.8;
  ctx.beginPath();
  for (let x = -maxSpanX; x <= maxSpanX; x += 0.05) {
    const px = toX(x);
    const py = toY(fnCubic(x));
    if (x === -maxSpanX) ctx.moveTo(px, py);
    else ctx.lineTo(px, py);
  }
  ctx.stroke();

  // Double arrow for Height H
  const arrowX = toX(L/2) + 40;
  ctx.strokeStyle = '#f43f5e';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(arrowX, toY(yMin));
  ctx.lineTo(arrowX, toY(yMax));
  ctx.stroke();

  // Arrow heads
  ctx.fillStyle = '#f43f5e';
  ctx.beginPath();
  ctx.moveTo(arrowX, toY(yMax)); ctx.lineTo(arrowX - 5, toY(yMax) + 10); ctx.lineTo(arrowX + 5, toY(yMax) + 10); ctx.fill();
  ctx.beginPath();
  ctx.moveTo(arrowX, toY(yMin)); ctx.lineTo(arrowX - 5, toY(yMin) - 10); ctx.lineTo(arrowX + 5, toY(yMin) - 10); ctx.fill();

  ctx.font = 'bold 13px Outfit, sans-serif';
  ctx.fillText(`H = ${H.toFixed(2)}`, arrowX + 12, (toY(yMin) + toY(yMax)) / 2 + 5);

  // Update DOM Stats
  const cardL = document.getElementById('statL37L');
  const cardH = document.getElementById('statL37H');
  const cardFormula = document.getElementById('statL37Formula');

  if (cardL) cardL.textContent = `간격 L = ${L.toFixed(2)} (비율간격 ${(L/2).toFixed(2)})`;
  if (cardH) cardH.textContent = `높이차 H = ${H.toFixed(2)}`;
  if (cardFormula) cardFormula.textContent = `H = (|${a.toFixed(1)}|/2) × ${L.toFixed(2)}³ = ${H.toFixed(2)}`;
}

window.addEventListener('resize', () => {
  const v37 = document.getElementById('lecture37View');
  if (v37 && v37.style.display !== 'none') renderL37();
});
