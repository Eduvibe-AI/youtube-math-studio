// ==========================================
// Lecture 33: 정적분의 본질 · 넓이 vs 함숫값의 이중성
// Canvas: cvsLec33
// ==========================================
let l33_x = 3.0; // Current upper bound for integral
let l33_fnType = 'cubic'; // 'cubic' (대칭 두 루프) or 'quadratic' (단일 포물선)

function setL33Preset(val) {
  l33_x = parseFloat(val);
  const slider = document.getElementById('sliderL33X');
  const lbl = document.getElementById('lblL33X');
  if (slider) slider.value = l33_x;
  if (lbl) lbl.textContent = l33_x.toFixed(2);
  renderL33();
}

function updateL33X(val) {
  l33_x = parseFloat(val);
  const lbl = document.getElementById('lblL33X');
  if (lbl) lbl.textContent = l33_x.toFixed(2);
  renderL33();
}

// Cubic f(t) = -(t - 1)(t - 3)(t - 5) / 2
// Roots at 1, 3, 5
// Interval [1, 3]: f(t) > 0 (Local max area +S1)
// Interval [3, 5]: f(t) < 0 (Local min area -S2, S1 = S2 = 2)
function f33(t) {
  return -0.5 * (t - 1) * (t - 3) * (t - 5);
}

// Antiderivative g(x) = int_1^x f(t)dt with g(1) = 0
// f(t) = -0.5 * (t^3 - 9t^2 + 23t - 15)
// int f(t)dt = -0.5 * (t^4/4 - 3t^3 + 23t^2/2 - 15t) + C
function g33_raw(t) {
  return -0.5 * ((t**4)/4 - 3*(t**3) + 11.5*(t**2) - 15*t);
}
const G33_CONST = g33_raw(1.0);
function g33(x) {
  return g33_raw(x) - G33_CONST;
}

// Geometric Area int_1^x |f(t)|dt
function geomArea33(x) {
  const steps = 100;
  const dt = (x - 1.0) / steps;
  let sum = 0;
  for (let i = 0; i < steps; i++) {
    const t = 1.0 + (i + 0.5) * dt;
    sum += Math.abs(f33(t)) * dt;
  }
  return sum;
}

function renderL33() {
  const cvs = document.getElementById('cvsLec33');
  if (!cvs) return;
  const ctx = cvs.getContext('2d');
  const w = cvs.width = cvs.parentElement ? cvs.parentElement.clientWidth : 720;
  const h = cvs.height = 460;

  ctx.fillStyle = '#080d17';
  ctx.fillRect(0, 0, w, h);

  // Split into Top (f(t)) and Bottom (g(x)) panels
  const topH = 210;
  const botH = 210;
  const ox = 70;
  const scaleX = (w - 120) / 4.8; // t from 0.8 to 5.5

  const toPxX = t => ox + (t - 0.8) * scaleX;

  // ----------------------------------------------------
  // TOP PANEL: f(t) [피적분함수: 부호 있는 넓이]
  // ----------------------------------------------------
  const topOy = 125;
  const topScaleY = 55; // y in [-1.8, 1.8]
  const toTopY = y => topOy - y * topScaleY;

  // Top Grid & Axis
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(toPxX(0.8), toTopY(0));
  ctx.lineTo(toPxX(5.5), toTopY(0));
  ctx.stroke();

  // Top Title Banner
  ctx.fillStyle = '#94a3b8';
  ctx.font = 'bold 12px Outfit, sans-serif';
  ctx.fillText('① 피적분함수 관점: f(t)의 부호 있는 넓이 누적', ox, 24);

  // Shading integral from 1 to l33_x
  const curX = l33_x;
  ctx.beginPath();
  let firstPt = true;
  for (let t = 1.0; t <= curX; t += 0.02) {
    const px = toPxX(t);
    const py = toTopY(f33(t));
    if (firstPt) { ctx.moveTo(toPxX(1.0), toTopY(0)); ctx.lineTo(px, py); firstPt = false; }
    else ctx.lineTo(px, py);
  }
  ctx.lineTo(toPxX(curX), toTopY(0));
  ctx.closePath();

  // Create subtle gradient for shading
  const grad = ctx.createLinearGradient(0, toTopY(1.5), 0, toTopY(-1.5));
  grad.addColorStop(0, 'rgba(56, 189, 248, 0.45)');  // Blue positive
  grad.addColorStop(0.5, 'rgba(56, 189, 248, 0.1)');
  grad.addColorStop(1, 'rgba(244, 63, 94, 0.45)');   // Red negative
  ctx.fillStyle = grad;
  ctx.fill();

  // Draw f(t) curve
  ctx.strokeStyle = '#f1f5f9';
  ctx.lineWidth = 2.4;
  ctx.beginPath();
  for (let t = 0.8; t <= 5.4; t += 0.03) {
    const px = toPxX(t);
    const py = toTopY(f33(t));
    if (t === 0.8) ctx.moveTo(px, py);
    else ctx.lineTo(px, py);
  }
  ctx.stroke();

  // Area Labels (+S1 and -S2)
  ctx.font = 'bold 13px Outfit, sans-serif';
  ctx.fillStyle = '#38bdf8';
  ctx.fillText('+S₁ (양수 넓이)', toPxX(2.0) - 30, toTopY(0.7));
  ctx.fillStyle = '#fb7185';
  ctx.fillText('-S₂ (음수 넓이)', toPxX(4.0) - 30, toTopY(-0.7));

  // Roots on axis
  [1, 3, 5].forEach(r => {
    ctx.fillStyle = '#cbd5e1';
    ctx.beginPath(); ctx.arc(toPxX(r), toTopY(0), 4, 0, Math.PI * 2); ctx.fill();
    ctx.font = '11px Outfit, sans-serif';
    ctx.fillText(`t=${r}`, toPxX(r) - 8, toTopY(0) + 16);
  });

  // ----------------------------------------------------
  // BOTTOM PANEL: g(x) = int_1^x f(t)dt [원함수: 높이 변화량]
  // ----------------------------------------------------
  const botOy = 390;
  const botScaleY = 60; // g(x) in [-0.5, 2.5]
  const toBotY = y => botOy - y * botScaleY;

  // Divider
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
  ctx.setLineDash([4, 4]);
  ctx.beginPath();
  ctx.moveTo(ox - 20, 230);
  ctx.lineTo(w - 40, 230);
  ctx.stroke();
  ctx.setLineDash([]);

  // Bottom Title
  ctx.fillStyle = '#fbbf24';
  ctx.font = 'bold 12px Outfit, sans-serif';
  ctx.fillText('② 원함수 관점 (고수의 시각): g(x) = ∫₁ˣ f(t)dt 의 함숫값 높이 변화', ox, 252);

  // Bottom Axis
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
  ctx.beginPath();
  ctx.moveTo(toPxX(0.8), toBotY(0));
  ctx.lineTo(toPxX(5.5), toBotY(0));
  ctx.stroke();

  // Draw g(x) curve
  ctx.strokeStyle = '#fbbf24';
  ctx.lineWidth = 2.6;
  ctx.beginPath();
  for (let t = 0.8; t <= 5.4; t += 0.03) {
    const px = toPxX(t);
    const py = toBotY(g33(t));
    if (t === 0.8) ctx.moveTo(px, py);
    else ctx.lineTo(px, py);
  }
  ctx.stroke();

  // Vertical Synchronized Tracker Line
  const pxCur = toPxX(curX);
  const pyCurTop = toTopY(f33(curX));
  const valG = g33(curX);
  const pyCurBot = toBotY(valG);

  ctx.strokeStyle = '#a855f7';
  ctx.lineWidth = 1.8;
  ctx.setLineDash([4, 4]);
  ctx.beginPath();
  ctx.moveTo(pxCur, 35);
  ctx.lineTo(pxCur, h - 20);
  ctx.stroke();
  ctx.setLineDash([]);

  // Point on Top Curve
  ctx.fillStyle = '#a855f7';
  ctx.beginPath(); ctx.arc(pxCur, pyCurTop, 5, 0, Math.PI * 2); ctx.fill();

  // Point on Bottom Curve
  ctx.fillStyle = '#fbbf24';
  ctx.beginPath(); ctx.arc(pxCur, pyCurBot, 6, 0, Math.PI * 2); ctx.fill();

  // Track point label
  ctx.font = 'bold 12px Outfit, sans-serif';
  ctx.fillStyle = '#fbbf24';
  ctx.fillText(`g(${curX.toFixed(2)}) = ${valG.toFixed(2)}`, pxCur + 10, pyCurBot - 8);

  // Extreme Point Marks on g(x)
  // x = 3 is local max (peak value = +2.0)
  ctx.fillStyle = '#38bdf8';
  ctx.beginPath(); ctx.arc(toPxX(3), toBotY(g33(3)), 4, 0, Math.PI * 2); ctx.fill();
  ctx.font = '10px Outfit, sans-serif';
  ctx.fillText('극댓값 (x=3)', toPxX(3) - 20, toBotY(g33(3)) - 10);

  // x = 5 is local min (g(5) = 0 because S1 = S2)
  ctx.fillStyle = '#fb7185';
  ctx.beginPath(); ctx.arc(toPxX(5), toBotY(g33(5)), 4, 0, Math.PI * 2); ctx.fill();
  ctx.fillText('상쇄점 (x=5)', toPxX(5) - 20, toBotY(g33(5)) + 18);

  // Update Live Stat Cards in DOM
  const valSigned = valG;
  const valGeom = geomArea33(curX);
  const valDeriv = f33(curX);

  const cardSigned = document.getElementById('statL33Signed');
  const cardGeom = document.getElementById('statL33Geom');
  const cardDeriv = document.getElementById('statL33Deriv');

  if (cardSigned) cardSigned.textContent = `${valSigned >= 0 ? '+' : ''}${valSigned.toFixed(2)}`;
  if (cardGeom) cardGeom.textContent = valGeom.toFixed(2);
  if (cardDeriv) {
    if (Math.abs(valDeriv) < 0.05) {
      cardDeriv.textContent = `f(${curX.toFixed(2)}) ≈ 0 (극점)`;
      cardDeriv.style.color = '#fbbf24';
    } else if (valDeriv > 0) {
      cardDeriv.textContent = `f(x) > 0 (g(x) 증가 중)`;
      cardDeriv.style.color = '#38bdf8';
    } else {
      cardDeriv.textContent = `f(x) < 0 (g(x) 감소 중!)`;
      cardDeriv.style.color = '#fb7185';
    }
  }
}

window.addEventListener('resize', () => {
  const v33 = document.getElementById('lecture33View');
  if (v33 && v33.style.display !== 'none') renderL33();
});
