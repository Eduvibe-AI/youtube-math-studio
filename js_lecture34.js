// ==========================================
// Lecture 34: 중학도형 핵심 정리 · 각의 이등분선과 닮음
// Canvas: cvsLec34
// ==========================================
let l34_ax = 240; // Vertex A x position
let l34_ay = 100; // Vertex A y position

function updateL34Ax(val) {
  l34_ax = parseFloat(val);
  const lbl = document.getElementById('lblL34Ax');
  if (lbl) lbl.textContent = l34_ax;
  renderL34();
}

function updateL34Ay(val) {
  l34_ay = parseFloat(val);
  const lbl = document.getElementById('lblL34Ay');
  if (lbl) lbl.textContent = l34_ay;
  renderL34();
}

function renderL34() {
  const cvs = document.getElementById('cvsLec34');
  if (!cvs) return;
  const ctx = cvs.getContext('2d');
  const w = cvs.width = cvs.parentElement ? cvs.parentElement.clientWidth : 720;
  const h = cvs.height = 420;

  ctx.fillStyle = '#080d17';
  ctx.fillRect(0, 0, w, h);

  // Triangle vertices
  const pA = { x: (w * l34_ax) / 600, y: l34_ay };
  const pB = { x: w * 0.15, y: h - 80 };
  const pC = { x: w * 0.85, y: h - 80 };

  // Calculate side lengths
  const c = Math.hypot(pA.x - pB.x, pA.y - pB.y); // AB
  const b = Math.hypot(pA.x - pC.x, pA.y - pC.y); // AC
  const a = Math.hypot(pC.x - pB.x, pC.y - pB.y); // BC

  // Point D by Angle Bisector: BD : CD = c : b => t = c / (b + c)
  const t = c / (b + c);
  const pD = {
    x: pB.x + t * (pC.x - pB.x),
    y: pB.y + t * (pC.y - pB.y)
  };

  const lenBD = t * a;
  const lenCD = (1 - t) * a;

  // Grid / background subtle lines
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
  ctx.lineWidth = 1;
  for (let x = 40; x < w; x += 40) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
  }

  // Draw Triangle ABC
  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 2.8;
  ctx.beginPath();
  ctx.moveTo(pA.x, pA.y);
  ctx.lineTo(pB.x, pB.y);
  ctx.lineTo(pC.x, pC.y);
  ctx.closePath();
  ctx.stroke();
  ctx.fillStyle = 'rgba(56, 189, 248, 0.05)';
  ctx.fill();

  // Draw Angle Bisector AD
  ctx.strokeStyle = '#f43f5e';
  ctx.lineWidth = 2.5;
  ctx.setLineDash([5, 4]);
  ctx.beginPath();
  ctx.moveTo(pA.x, pA.y);
  ctx.lineTo(pD.x, pD.y);
  ctx.stroke();
  ctx.setLineDash([]);

  // Angle Arcs at A
  const angB = Math.atan2(pB.y - pA.y, pB.x - pA.x);
  const angD = Math.atan2(pD.y - pA.y, pD.x - pA.x);
  const angC = Math.atan2(pC.y - pA.y, pC.x - pA.x);

  ctx.strokeStyle = '#fbbf24';
  ctx.lineWidth = 2;
  ctx.beginPath(); ctx.arc(pA.x, pA.y, 28, angB, angD); ctx.stroke();
  ctx.beginPath(); ctx.arc(pA.x, pA.y, 34, angD, angC); ctx.stroke();

  // Dots
  [pA, pB, pC, pD].forEach((pt, i) => {
    ctx.fillStyle = i === 3 ? '#f43f5e' : (i === 0 ? '#fbbf24' : '#38bdf8');
    ctx.beginPath(); ctx.arc(pt.x, pt.y, 5.5, 0, Math.PI * 2); ctx.fill();
  });

  // Labels
  ctx.font = 'bold 15px Outfit, sans-serif';
  ctx.fillStyle = '#fbbf24';
  ctx.fillText('A', pA.x - 6, pA.y - 12);
  ctx.fillStyle = '#38bdf8';
  ctx.fillText('B', pB.x - 18, pB.y + 18);
  ctx.fillText('C', pC.x + 8, pC.y + 18);
  ctx.fillStyle = '#f43f5e';
  ctx.fillText('D (내분점)', pD.x - 22, pD.y + 24);

  // Side length annotations
  ctx.font = '12px Outfit, sans-serif';
  ctx.fillStyle = '#cbd5e1';
  ctx.fillText(`c (AB) = ${(c/20).toFixed(1)}`, (pA.x + pB.x) / 2 - 40, (pA.y + pB.y) / 2);
  ctx.fillText(`b (AC) = ${(b/20).toFixed(1)}`, (pA.x + pC.x) / 2 + 10, (pA.y + pC.y) / 2);
  ctx.fillStyle = '#f43f5e';
  ctx.fillText(`BD = ${(lenBD/20).toFixed(1)}`, (pB.x + pD.x) / 2 - 15, pB.y - 10);
  ctx.fillText(`CD = ${(lenCD/20).toFixed(1)}`, (pD.x + pC.x) / 2 - 15, pC.y - 10);

  // Live Stats in DOM
  const cardAB_AC = document.getElementById('statL34AB_AC');
  const cardBD_CD = document.getElementById('statL34BD_CD');
  const cardEqual = document.getElementById('statL34Equal');

  const ratio1 = c / b;
  const ratio2 = lenBD / lenCD;

  if (cardAB_AC) cardAB_AC.textContent = `AB/AC = ${(c/20).toFixed(1)} / ${(b/20).toFixed(1)} = ${ratio1.toFixed(3)}`;
  if (cardBD_CD) cardBD_CD.textContent = `BD/CD = ${(lenBD/20).toFixed(1)} / ${(lenCD/20).toFixed(1)} = ${ratio2.toFixed(3)}`;
  if (cardEqual) cardEqual.textContent = `비율 완벽 일치: ${ratio1.toFixed(3)} == ${ratio2.toFixed(3)}`;
}

window.addEventListener('resize', () => {
  const v34 = document.getElementById('lecture34View');
  if (v34 && v34.style.display !== 'none') renderL34();
});
