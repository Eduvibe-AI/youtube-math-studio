// ==========================================
// Lecture 35: 원의 성질 핵심 정리 · 원주각과 접현각
// Canvas: cvsLec35
// ==========================================
let l35_angP = 1.3; // Angle of point P on circle (in radians)
let l35_isDiameter = false; // Diameter mode toggle

function toggleL35Diameter() {
  l35_isDiameter = !l35_isDiameter;
  const btn = document.getElementById('btnL35Diam');
  if (btn) {
    if (l35_isDiameter) {
      btn.style.background = '#f43f5e';
      btn.style.color = '#fff';
      btn.textContent = '지름 모드 ON (원주각 = 90°)';
    } else {
      btn.style.background = 'rgba(255,255,255,0.08)';
      btn.style.color = '#cbd5e1';
      btn.textContent = '지름 모드 OFF (일반 호)';
    }
  }
  renderL35();
}

function updateL35AngP(val) {
  l35_angP = parseFloat(val);
  const lbl = document.getElementById('lblL35AngP');
  if (lbl) lbl.textContent = `${(l35_angP * 180 / Math.PI).toFixed(0)}°`;
  renderL35();
}

function renderL35() {
  const cvs = document.getElementById('cvsLec35');
  if (!cvs) return;
  const ctx = cvs.getContext('2d');
  const w = cvs.width = cvs.parentElement ? cvs.parentElement.clientWidth : 720;
  const h = cvs.height = 420;

  ctx.fillStyle = '#080d17';
  ctx.fillRect(0, 0, w, h);

  const cx = w * 0.45;
  const cy = h * 0.52;
  const R = Math.min(w * 0.28, h * 0.38);

  // Circle
  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 2.4;
  ctx.beginPath();
  ctx.arc(cx, cy, R, 0, Math.PI * 2);
  ctx.stroke();

  // Circle Center O
  ctx.fillStyle = '#f1f5f9';
  ctx.beginPath(); ctx.arc(cx, cy, 4, 0, Math.PI * 2); ctx.fill();
  ctx.font = 'bold 13px Outfit, sans-serif';
  ctx.fillText('O', cx - 14, cy - 8);

  // Points A and B on circle
  let angA, angB;
  if (l35_isDiameter) {
    angA = Math.PI; // -180 deg
    angB = 0;       // 0 deg (Diameter AB)
  } else {
    angA = -2.4;    // Approx 220 deg
    angB = -0.7;    // Approx 320 deg
  }

  const pA = { x: cx + R * Math.cos(angA), y: cy + R * Math.sin(angA) };
  const pB = { x: cx + R * Math.cos(angB), y: cy + R * Math.sin(angB) };

  // Point P on circle
  const pP = { x: cx + R * Math.cos(l35_angP), y: cy + R * Math.sin(l35_angP) };

  // Minor arc AB highlight
  ctx.strokeStyle = '#fbbf24';
  ctx.lineWidth = 4;
  ctx.beginPath();
  ctx.arc(cx, cy, R, angA, angB, false);
  ctx.stroke();

  // Central lines OA and OB
  ctx.strokeStyle = '#fbbf24';
  ctx.lineWidth = 1.8;
  ctx.setLineDash([4, 4]);
  ctx.beginPath();
  ctx.moveTo(cx, cy); ctx.lineTo(pA.x, pA.y);
  ctx.moveTo(cx, cy); ctx.lineTo(pB.x, pB.y);
  ctx.stroke();
  ctx.setLineDash([]);

  // Inscribed lines PA and PB
  ctx.strokeStyle = '#f43f5e';
  ctx.lineWidth = 2.5;
  ctx.beginPath();
  ctx.moveTo(pP.x, pP.y); ctx.lineTo(pA.x, pA.y);
  ctx.lineTo(pB.x, pB.y); ctx.stroke();

  // Central Angle value
  let centralAngRad = angB - angA;
  if (centralAngRad < 0) centralAngRad += Math.PI * 2;
  const centralDeg = (centralAngRad * 180 / Math.PI);

  // Inscribed Angle value
  const inscribedDeg = centralDeg / 2;

  // Dots
  [pA, pB, pP].forEach((pt, i) => {
    ctx.fillStyle = i === 2 ? '#f43f5e' : '#fbbf24';
    ctx.beginPath(); ctx.arc(pt.x, pt.y, 5.5, 0, Math.PI * 2); ctx.fill();
  });

  // Labels
  ctx.font = 'bold 14px Outfit, sans-serif';
  ctx.fillStyle = '#fbbf24';
  ctx.fillText('A', pA.x - 16, pA.y + (angA < 0 ? -8 : 16));
  ctx.fillText('B', pB.x + 10, pB.y + (angB < 0 ? -8 : 16));
  ctx.fillStyle = '#f43f5e';
  ctx.fillText(`P (원주각 ${inscribedDeg.toFixed(1)}°)`, pP.x - 40, pP.y - 12);

  if (l35_isDiameter) {
    ctx.fillStyle = '#34d399';
    ctx.font = 'bold 13px Outfit, sans-serif';
    ctx.fillText('선분 AB = 지름 (직각삼각형 탄생)', cx - 80, cy + 28);
  }

  // Live Stats in DOM
  const cardInscribed = document.getElementById('statL35Inscribed');
  const cardCentral = document.getElementById('statL35Central');
  const cardRelation = document.getElementById('statL35Relation');

  if (cardInscribed) cardInscribed.textContent = `∠APB = ${inscribedDeg.toFixed(1)}°`;
  if (cardCentral) cardCentral.textContent = `∠AOB = ${centralDeg.toFixed(1)}°`;
  if (cardRelation) {
    cardRelation.textContent = l35_isDiameter 
      ? '지름에 대한 원주각 = 항상 90° (직각)'
      : `원주각(${inscribedDeg.toFixed(1)}°) = 중심각(${centralDeg.toFixed(1)}°) × 1/2`;
  }
}

window.addEventListener('resize', () => {
  const v35 = document.getElementById('lecture35View');
  if (v35 && v35.style.display !== 'none') renderL35();
});
