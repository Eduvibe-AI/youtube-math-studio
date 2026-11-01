/* 중학 도형 → 수능 직결 12대 법칙 마스터 (12강 사슬: 124 → 125 → 126 → 127 → 128 → 129 → 130 → 131 → 132 → 133 → 134 → 135)
   9:16 세로 숏츠 판서 시리즈 & 강의 본문 요약 카드. 대본·수능형 자작 문항·그래프·연출 모두 직접 제작. */
(function () {
"use strict";

const $ = id => document.getElementById(id);
const K = (tex, disp) => {
  try { return window.katex.renderToString(tex, { displayMode: !!disp, throwOnError: false }); }
  catch (e) { return String(tex); }
};
const inline = s => String(s || "").replace(/\$([^$]+)\$/g, (m, t) => K(t));
const reduced = () => matchMedia("(prefers-reduced-motion: reduce)").matches;
const sleep = ms => new Promise(r => setTimeout(r, ms));
const CY = "#38bdf8", PK = "#f472b6", GO = "#fbbf24";
const estMs = t => Math.max(1800, Math.round(Array.from(t || "").length * 115) + 380);

const MIDGEO_CHAIN = [
  { lec: 124, step: 1,  badge: "원주각내접",  title: "원주각·중심각(θ↔2θ)·반원(90°)과 공원점 판정" },
  { lec: 125, step: 2,  badge: "접선현각",    title: "원 밖의 접선 길이(PA=PB)와 접선·현이 이루는 각(접현각)" },
  { lec: 126, step: 3,  badge: "원의방멱",    title: "원의 방멱정리 3종(PA·PB=PC·PD=PT²)과 닮음비 유도" },
  { lec: 127, step: 4,  badge: "내심반지름",  title: "삼각형의 내심(I)과 내접원 넓이 S = ½r(a+b+c) 공식" },
  { lec: 128, step: 5,  badge: "외심수심",    title: "삼각형의 외심(O)·수심(H)과 사인법칙 지름(2R) 보조선" },
  { lec: 129, step: 6,  badge: "무게중심",    title: "무게중심(G) 2:1 내분·6등분 넓이와 파푸스 중선정리" },
  { lec: 130, step: 7,  badge: "각이등분선",  title: "내각·외각의 이등분선 비율(AB:AC=BD:CD)과 길이 공식" },
  { lec: 131, step: 8,  badge: "사영정리",    title: "직각삼각형 닮음 사영정리 4대 공식(h²=xy, a²=xc)과 소 공식" },
  { lec: 132, step: 9,  badge: "직교대각선",  title: "피타고라스 직교 대각선(a²+c²=b²+d²)과 히포크라테스 원" },
  { lec: 133, step: 10, badge: "닮음넓이비",  title: "평행선 닮음비(m:n)·넓이비(m²:n²)와 등비급수 도형 공비" },
  { lec: 134, step: 11, badge: "외접원접선",  title: "두 원의 외접·내접 중심거리와 공통외접선 길이 2√(Rr)" },
  { lec: 135, step: 12, badge: "톨레미정리",  title: "원 내접 사각형 코사인법칙 대각선과 톨레미 정리(ac+bd=pq)" }
];

function midgeoChainNavHtml(curLec) {
  const idx = MIDGEO_CHAIN.findIndex(c => c.lec === curLec);
  const prev = idx > 0 ? MIDGEO_CHAIN[idx - 1] : null;
  const next = idx >= 0 && idx < MIDGEO_CHAIN.length - 1 ? MIDGEO_CHAIN[idx + 1] : null;
  return `
    <div class="l2s-chain-box" style="margin-bottom:16px;padding:12px 14px;border-radius:12px;background:rgba(15,23,42,.82);border:1px solid rgba(251,146,60,.38)">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:10px">
        <span style="font-size:13px;font-weight:800;color:#fdba74">📐 중학 도형 → 수능 직결 12대 법칙 마스터 · 수업 단원·개념 연결 사슬 (${idx + 1} / ${MIDGEO_CHAIN.length}단계)</span>
        <div style="display:flex;gap:6px">
          ${prev ? `<button type="button" class="l2s-btn" data-chain-lec="${prev.lec}">← 이전 (${prev.step}단계 · 제${prev.lec}강)</button>` : ""}
          ${next ? `<button type="button" class="l2s-btn on" data-chain-lec="${next.lec}">다음 (${next.step}단계 · 제${next.lec}강) →</button>` : `<button type="button" class="l2s-btn on" data-chain-lec="124">중학 도형 첫 단계로 →</button>`}
        </div>
      </div>
      <div style="display:flex;gap:5px;flex-wrap:wrap">
        ${MIDGEO_CHAIN.map(c => `
          <button type="button" data-chain-lec="${c.lec}" style="padding:4px 8px;border-radius:999px;font-size:11px;font-weight:700;cursor:pointer;border:1px solid ${c.lec === curLec ? '#f97316' : 'rgba(148,163,184,.28)'};background:${c.lec === curLec ? 'rgba(249,115,22,.22)' : 'rgba(15,23,42,.6)'};color:${c.lec === curLec ? '#fdba74' : '#cbd5e1'}">
            ${c.step}. 제${c.lec}강 (${c.badge})
          </button>
        `).join("")}
      </div>
    </div>
  `;
}

const MIDGEO_SPECS_A = [
  {
    lec: 124,
    title: "숏츠식 판서 미리보기 · 원주각·중심각(θ↔2θ)·반원(90°)과 공원점 판정",
    desc: "한 호에 대한 중심각은 원주각의 2배($2\\theta$)이고 지름의 원주각은 $90^\\circ$입니다. 마주 보는 두 각의 합이 $180^\\circ$이면 네 점이 한 원 위에 놓입니다.",
    hookTitle: "중심각은 원주각의 2배 · 지름을 보면 무조건 직각(90°)!", hookSub: "마주 보는 두 각의 합이 180° 이면 네 점은 한 원 위의 공원점!",
    hookSay: "수능 삼각함수 도형 문제에서 보조선 하나로 문제를 끝내는 원주각과 중심각, 그리고 네 점이 한 원 위에 있을 조건을 삼십 초 만에 정리합니다.",
    hookCap: "원주각·중심각 & 공원점 · 30초 정리",
    whySay: "원의 중심과 원주 위의 세 점을 이으면 반지름이 같은 두 이등변삼각형이 만들어지고, 외각의 성질에 의해 중심각이 항상 원주각의 두 배가 됩니다.",
    whyCap: "반지름 $OA=OB=OC$ 이등변삼각형 외각 합 $\\Longrightarrow\\ \\angle AOB = 2\\angle ACB$!",
    histTag: "탈레스의 반원 정리와 유클리드 제3권", histSay: "고대 그리스의 탈레스는 반원에 내접하는 삼각형은 언제나 직각삼각형임을 증명하고 기하학 논증의 시대를 열었습니다.",
    histCap: "탈레스 정리: 현 $AB$ 가 지름($\\angle AOB=180^\\circ$) $\\Longleftrightarrow\\ \\angle ACB=90^\\circ$!",
    fParts: [
      { say: "같은 호에 대한 원주각의 크기는 모두 같고, 중심각의 크기는 원주각의 정확히 두 배입니다.", cap: "원주각·중심각 법칙: $\\angle APB=\\angle AQB=\\theta\\ \\Longleftrightarrow\\ \\angle AOB=2\\theta$" },
      { say: "지름에 대한 중심각은 백팔십도이므로 반원에 내접하는 원주각은 언제나 구십도 직각입니다.", cap: "탈레스 반원 정리: 선분 $AB$ 가 지름 $\\Longleftrightarrow\\ \\angle APB=90^\\circ$ (피타고라스·사인법칙 직결!)" },
      { say: "사각형의 마주 보는 두 내각의 합이 백팔십도이거나 한 외각이 내대각과 같으면 네 꼭짓점은 한 원 위에 있습니다.", cap: "공원점(내접사각형) 조건: $\\angle A+\\angle C=180^\\circ$ 또는 $\\angle APB=\\angle AQB$" }
    ],
    fChips: [
      "\\angle AOB=2\\angle APB,\\quad \\overline{AB}\\text{ 지름}\\iff \\angle APB=90^\\circ",
      "\\text{내접사각형}\\iff \\angle A+\\angle C=180^\\circ\\iff \\text{외각}=\\text{내대각}",
      "\\text{호의 길이 }l\\propto \\text{중심각 }2\\theta\\propto \\text{원주각 }\\theta\\text{ (현의 길이는 비례 X)}"
    ],
    fLabels: ["중심각 = 2 × 원주각", "대각 합 180° ➔ 한 원 위의 4점"],
    exParts: [
      { say: "예를 들어 반지름이 오인 원에서 지름 에이비에 대하여 현 에이씨가 팔일 때, 각 에이피비와 삼각형 에이비씨의 넓이를 구해 봅시다.", cap: "반지름 $R=5$ (지름 $AB=10$), 현 $AC=8$ 일 때 내접 $\\triangle ABC$ 의 넓이 구하기" },
      { say: "선분 에이비가 지름이므로 원주각 에이씨비는 구십도이고, 피타고라스 정리에 의해 나머지 현 비씨는 육입니다.", cap: "지름 $AB=10\\implies \\angle ACB=90^\\circ\\implies BC=\\sqrt{10^2-8^2}=6$" },
      { say: "따라서 직각삼각형 에이비씨의 넓이는 이분의 일 곱하기 팔 곱하기 육인 이십사입니다.", cap: "$S=\\dfrac{1}{2}\\times AC\\times BC=\\dfrac{1}{2}\\times 8\\times 6=24$" }
    ],
    exChips: [
      "\\overline{AB}=2R=10\\text{ (지름)}\\implies \\angle ACB=90^\\circ",
      "\\overline{BC}=\\sqrt{10^2-8^2}=6\\quad(3:4:5\\text{ 직각삼각형})",
      "\\therefore\\ S_{\\triangle ABC}=\\dfrac{1}{2}\\times 8\\times 6=24"
    ],
    exLabels: ["지름 원주각 = 90°", "BC = 6 ➔ 넓이 S = 24"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 2.1 - (x - 1.5) * (x - 1.5))), GY0: 390, GV: 185, xr: [0.1, 2.9], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.3, col: CY, label: "A(지름 끝)" }, r2: { x: 2.7, col: PK, label: "B(2R=10)" },
      fn: { t: "반원 위의 점 C 에서 ∠ACB = 90° (AC=8, BC=6)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "∠ACB = 90°", finalS: "넓이 = 24", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 예각삼각형 에이비씨의 꼭짓점 비와 씨에서 대변에 내린 수선의 발을 각각 디와 이라 할 때, 에이비가 십이고 사인 에이가 오분의 사라면 선분 디이의 길이는 얼마일까요?", cap: "$\\triangle ABC$ 에서 수선의 발 $D,E$ 에 대해 $BC=10,\\ \\cos A=\\dfrac{3}{5}$ 일 때 $DE$ 길이 (자작 문항)" },
      { say: "각 비디씨와 각 비이씨가 모두 구십도이므로 네 점 비, 씨, 디, 이는 선분 비씨를 지름으로 하는 한 원 위에 있습니다.", cap: "$\\angle BDC=\\angle BEC=90^\\circ\\implies B,C,D,E$ 공원점 $\\implies \\triangle ADE\\sim\\triangle ABC$" },
      { say: "내접사각형의 성질로 삼각형 에이디이와 에이비씨의 닮음비가 코사인 에이인 오분의 삼이므로 디이는 십 곱하기 오분의 삼인 육입니다.", cap: "닮음비 $\\dfrac{AD}{AB}=\\cos A=\\dfrac{3}{5}\\implies DE=BC\\cos A=10\\times\\dfrac{3}{5}=6$" }
    ],
    examChips: [
      "\\angle BDC=\\angle BEC=90^\\circ\\implies B,C,D,E\\text{ 는 지름 }BC\\text{ 인 원 위의 점}",
      "\\triangle ADE\\sim\\triangle ABC\\quad(\\text{닮음비 }=\\dfrac{AD}{AB}=\\cos A=\\dfrac{3}{5})",
      "\\therefore\\ \\overline{DE}=\\overline{BC}\\cos A=10\\times\\dfrac{3}{5}=6"
    ],
    examLabels: ["직각 2개 ➔ 공원점 발견", "닮음비 cos A ➔ DE = 6"],
    examGraph: {
      f: x => -0.55 * (x - 1.5) * (x - 1.5) + 1.55, GY0: 390, GV: 155, xr: [0.2, 2.8], area: [0.6, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "D(수선의 발)" }, r2: { x: 2.4, col: GO, label: "E(수선의 발)" },
      fn: { t: "∠BDC = ∠BEC = 90° 공원점 ➔ DE = BC·cos A", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "닮음비 cos A", finalS: "DE = 6", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 문제에 직각이 두 개 보이면 무조건 마주 보고 더해서 백팔십도가 되는지, 혹은 같은 선분을 바라보는지 확인해 숨은 원을 그리세요.", cap: "① 직각 2개 발견 공식: $\\angle P+\\angle Q=180^\\circ$ 또는 $\\angle APB=\\angle AQB=90^\\circ\\implies$ 숨은 원 작도!" },
      { say: "둘째, 두 수선의 발을 이은 선분 디이는 원래 밑변 비씨에 코사인 에이를 곱한 길이로 축소된다는 공식은 수능 킬러의 단골 소재입니다.", cap: "② 수선의 발 삼각형 공식: $\\triangle ADE\\sim\\triangle ABC$ (닮음비 $=|\\cos A|\\implies DE=BC|\\cos A|$)!" },
      { say: "셋째, 호의 길이와 부채꼴 넓이는 중심각에 정비례하지만 현의 길이는 정비례하지 않으므로 주의하세요.", cap: "③ 비례 주의: 호의 길이 $l$ 은 원주각 $\\theta$ 에 정비례하지만 현의 길이($2R\\sin\\theta$)는 정비례 X!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 원 밖의 점에서 그은 접선의 길이와 접선과 현이 이루는 각을 다루는 제백이십오강입니다.", cap: "제125강 · 원의 접선 길이($PA=PB$)와 접현각 정리" },
      { tag: "연계 ②", say: "사인법칙과 외접원 반지름 공식을 다루는 제칠강도 함께 복습해 보세요.", cap: "제7강 · 사인법칙과 외접원 지름 $2R$ (대수)" },
      { tag: "이 사이트", say: "이 사이트의 제백이십오강과 제칠강을 이어서 보세요.", cap: "제125강 · 접선과 접현각  /  제7강 · 사인법칙" }
    ],
    nextLinks: [
      { lec: 125, label: "제125강 열기 (접선과 접현각)" },
      { lec: 7, label: "제7강 열기 (사인법칙과 외접원)" },
      { lec: 135, label: "제135강 열기 (내접사각형과 톨레미)" }
    ]
  },
  {
    lec: 125,
    title: "숏츠식 판서 미리보기 · 원 밖의 접선 길이(PA=PB)와 접선·현이 이루는 각(접현각)",
    desc: "원 밖의 한 점 $P$ 에서 그은 두 접선의 길이는 같고($PA=PB$), 접선 $AT$ 와 현 $AB$ 가 이루는 각은 그 호에 대한 원주각($\\angle BCA$)과 같습니다.",
    hookTitle: "두 접선 길이는 무조건 같고 · 접현각은 건너편 원주각과 같다!", hookSub: "중심에서 접점에 수선(90°) 긋기 + ∠BAT = ∠BCA!",
    hookSay: "원이 등장하는 수능 도형 문제에서 아홉 문제 중 여덟 문제에 쓰이는 접선 수직 보조선과 접현각 정리를 삼십 초 만에 마스터합니다.",
    hookCap: "접선의 성질과 접현각 · 30초 정리",
    whySay: "원의 중심 오에서 두 접점 에이와 비에 반지름을 그으면 각각 직각이 되고, 직각삼각형 피오에이와 피오비가 합동이므로 두 접선의 길이가 완벽히 같아집니다.",
    whyCap: "$\\triangle POA\\equiv\\triangle POB\\text{ (RHS 합동)}\\ \\Longrightarrow\\ PA=PB,\\ \\angle APO=\\angle BPO$!",
    histTag: "유클리드 원론 제3권 명제 32", histSay: "유클리드는 원론 제삼권에서 지름을 지나는 직각삼각형의 원주각을 움직여 현이 접선에 한없이 가까워질 때의 극한으로 접현각 정리를 증명했습니다.",
    histCap: "접선 $AT$ 와 현 $AB$ 의 사잇각 $\\angle BAT$ $=$ 호 $AB$ 에 대한 원주각 $\\angle BCA$!",
    fParts: [
      { say: "원 밖의 점 피에서 그은 두 접점 에이, 비에 대하여 피에이와 피비는 같고, 중심각과 피의 각의 합은 백팔십도여서 네 점 피, 에이, 오, 비는 한 원 위에 있습니다.", cap: "접선 3종 세트: $PA=PB$, $PO\\perp AB$ (수직이등분), $\\angle APB+\\angle AOB=180^\\circ$" },
      { say: "접선 에이티와 현 에이비가 이루는 각 비에이티는 그 각 내부에 있는 호 에이비에 대한 원주각 비씨에이와 항상 같습니다.", cap: "접현각 정리: $\\angle BAT = \\angle BCA$ (접선 옆 각 $=$ 건너편 원주각!)" },
      { say: "외접하는 삼각형의 둘레는 접점까지의 같은 길이 세 쌍의 합으로 쪼개어 방정식을 세우면 모든 변의 길이가 풀립니다.", cap: "접선 길이 치환: $AR=AQ=x,\\ BP=BR=y,\\ CQ=CP=z$ 로 둘레 분해!" }
    ],
    fChips: [
      "\\overline{PA}=\\overline{PB}=\\sqrt{\\overline{PO}^2-R^2},\\quad \\angle APB+\\angle AOB=180^\\circ",
      "\\text{접현각 정리}:\\ \\angle BAT=\\angle BCA\\quad(\\text{접선·현 사잇각}=\\text{원주각})",
      "\\overline{PO}\\perp\\overline{AB}\\implies \\text{현 }AB\\text{ 는 }PO\\text{ 에 의해 수직이등분}"
    ],
    fLabels: ["RHS 합동 ➔ PA = PB", "접현각 ∠BAT = 원주각 ∠BCA"],
    exParts: [
      { say: "예를 들어 반지름이 삼인 원의 중심 오에서 거리가 오인 점 피에서 그은 두 접점 에이, 비에 대하여 접선의 길이 피에이와 현 에이비의 길이를 구해 봅시다.", cap: "반지름 $R=3$, 중심거리 $PO=5$ 일 때 접선 길이 $PA$ 와 현 $AB$ 의 길이 구하기" },
      { say: "직각삼각형 피에이오에서 피타고라스 정리에 의해 접선 피에이의 길이는 사입니다.", cap: "$\\angle PAO=90^\\circ\\implies PA=\\sqrt{PO^2-OA^2}=\\sqrt{5^2-3^2}=4$" },
      { say: "직각삼각형의 넓이 공식인 소 공식에 의해 에이비의 절반 에이치가 오분의 십이이므로 현 에이비의 길이는 오분의 이십사입니다.", cap: "$OA\\cdot PA=PO\\cdot AH\\implies 3\\times 4=5\\cdot AH\\implies AB=2AH=\\dfrac{24}{5}$" }
    ],
    exChips: [
      "\\angle PAO=90^\\circ\\implies \\overline{PA}=\\sqrt{5^2-3^2}=4",
      "\\text{소 공식}:\\ 3\\times 4=5\\times \\overline{AH}\\implies \\overline{AH}=\\dfrac{12}{5}",
      "\\therefore\\ \\overline{PA}=4,\\quad \\overline{AB}=2\\overline{AH}=\\dfrac{24}{5}"
    ],
    exLabels: ["피타고라스 ➔ PA = 4", "소 공식 ➔ 현 AB = 24/5"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 1.5 - (x - 1.1) * (x - 1.1))) + 0.3, GY0: 390, GV: 165, xr: [0.1, 2.9], area: [0.3, 2.3], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.1, col: CY, label: "중심 O(R=3)" }, r2: { x: 2.6, col: GO, label: "P(PO=5)" },
      fn: { t: "직각삼각형 PAO (3 : 4 : 5) 와 수선의 발 AH = 12/5", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "PA = 4", finalS: "AB = 24/5", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 원 위의 점 에이에서의 접선 위의 점 피에서 그은 할선이 원과 만나는 두 점을 비, 씨라 할 때, 피에이가 육, 에이비가 사, 에이씨가 구라면 선분 비씨의 길이는 얼마일까요?", cap: "접선 $PA=6$, 할선 $PBC$ 에 대해 $AB=4,\\ AC=9,\\ \\angle PAB=\\angle PCA$ 일 때 $BC$ (자작 문항)" },
      { say: "접현각 정리에 의해 각 피에이비와 각 피씨에이가 같고 각 피가 공통이므로 삼각형 피에이비와 피씨에이는 에이에이 닮음입니다.", cap: "접현각 $\\angle PAB=\\angle PCA$, $\\angle P$ 공통 $\\implies \\triangle PAB\\sim\\triangle PCA$ ($4:9$ 닮음!)" },
      { say: "닮음비가 사 대 구인 이 대 삼이므로 피비는 사, 피씨는 구가 되어 선분 비씨의 길이는 구 빼기 사인 오입니다.", cap: "닮음비 $AB:CA=4:9\\implies PB:PA=4:6\\implies PB=4,\\ PC=9\\ \\therefore\\ BC=5$" }
    ],
    examChips: [
      "\\text{접현각 }\\angle PAB=\\angle PCA\\implies \\triangle PAB\\sim\\triangle PCA",
      "\\overline{PB}:\\overline{PA}=\\overline{PA}:\\overline{PC}=\\overline{AB}:\\overline{CA}=4:9",
      "\\overline{PA}=6\\implies \\overline{PB}=4,\\ \\overline{PC}=9\\quad(\\therefore\\ \\overline{BC}=9-4=5)"
    ],
    examLabels: ["접현각 ➔ △PAB ∼ △PCA", "PB=4, PC=9 ➔ BC = 5"],
    examGraph: {
      f: x => 0.45 * (x - 0.5) * (x - 0.5) + 0.4, GY0: 390, GV: 130, xr: [0.2, 2.8], area: [0.6, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.0, col: CY, label: "PB = 4" }, r2: { x: 2.25, col: PK, label: "PC = 9" },
      fn: { t: "접현각 AA 닮음비 4 : 9 (또는 2 : 3) ➔ BC = PC − PB = 5", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "닮음비 2:3", finalS: "BC = 5", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 원과 접선이 나오면 문제를 읽기도 전에 원의 중심에서 접점까지 수선부터 긋고 직각 표시를 하세요.", cap: "① 제1보조선 철칙: 원 $+$ 접선 등장 $\\Longrightarrow$ 무조건 중심 $O\\to$ 접점 $T$ 수선($90^\\circ$) 긋기!" },
      { say: "둘째, 접현각은 원 밖의 점에서 그은 접선과 할선이 만드는 두 삼각형이 닮음임을 증명하는 핵심 열쇠입니다.", cap: "② 접현각 $\\implies$ $\\triangle PAB\\sim\\triangle PCA$ 닮음비($AB:CA=PB:PA=PA:PC$) 자동 성립!" },
      { say: "셋째, 원에 외접하는 사각형은 마주 보는 두 변의 길이의 합이 서로 같다는 피톳 정리도 함께 기억해 두세요.", cap: "③ 외접사각형(피톳 정리): 원에 외접하는 사각형 $ABCD\\iff AB+CD = BC+DA$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 방금 본 접현각 닮음에서 바로 유도되는 원의 방멱정리 삼종 세트를 다루는 제백이십육강입니다.", cap: "제126강 · 원의 방멱정리 3종($PA\\cdot PB=PC\\cdot PD=PT^2$)" },
      { tag: "연계 ②", say: "원주각과 중심각, 내접사각형을 다루는 제백이십사강도 함께 복습해 보세요.", cap: "제124강 · 원주각·중심각과 공원점 판정" },
      { tag: "이 사이트", say: "이 사이트의 제백이십육강과 제백이십사강을 이어서 보세요.", cap: "제126강 · 원의 방멱정리  /  제124강 · 원주각과 공원점" }
    ],
    nextLinks: [
      { lec: 126, label: "제126강 열기 (원의 방멱정리 3종)" },
      { lec: 124, label: "제124강 열기 (원주각과 공원점)" },
      { lec: 134, label: "제134강 열기 (두 원의 공통접선)" }
    ]
  },
  {
    lec: 126,
    title: "숏츠식 판서 미리보기 · 원의 방멱정리 3종(PA·PB=PC·PD=PT²)과 닮음비 유도",
    desc: "한 점 $P$ 를 지나는 두 직선이 원과 만날 때 $PA\\cdot PB = PC\\cdot PD = PT^2 = |d^2-R^2|$ 이 성립합니다. 코사인법칙 연립을 3초에 생략하는 필살기입니다.",
    hookTitle: "원의 방멱정리 · 짧은 것 × 긴 것 = 접선의 제곱!", hookSub: "PA · PB = PC · PD = PT² = |PO² − R²|!",
    hookSay: "원을 가로지르는 두 할선이나 접선이 나올 때 코사인법칙 없이 변의 길이를 일초 만에 구하는 원의 방멱정리 세 가지를 바로 정리합니다.",
    hookCap: "원의 방멱정리 3종 · 30초 정리",
    whySay: "원주각이나 접현각이 같다는 성질로 두 삼각형 피에이씨와 피디비가 항상 에이에이 닮음이 되므로, 비례식의 내항과 외항을 곱하면 피에이 곱하기 피비는 피씨 곱하기 피디가 됩니다.",
    whyCap: "원주각 $\\angle PAC=\\angle PDB\\implies \\triangle PAC\\sim\\triangle PDB\\implies PA:PD=PC:PB$!",
    histTag: "야코프 슈타이너의 방멱(Power of a Point)", histSay: "십구 세기 기하학자 야코프 슈타이너는 점 피에서 원에 그은 선분들의 곱이 직선의 방향과 무관하게 중심거리 제곱 빼기 반지름 제곱으로 일정함을 밝혀 방멱이라 이름 붙였습니다.",
    histCap: "슈타이너 방멱 불변량: $PA\\cdot PB = |PO^2 - R^2|$ (할선의 방향과 무관한 상수!)",
    fParts: [
      { say: "원 내부에서 두 현이 점 피에서 만나면 피에이 곱하기 피비는 피씨 곱하기 피디와 같습니다.", cap: "제1방멱(원 내부 교차): $PA\\cdot PB = PC\\cdot PD = R^2 - PO^2$" },
      { say: "원 외부의 점 피에서 두 할선을 그으면 항상 점 피에서부터 짧은 길이 곱하기 전체 긴 길이끼리 같습니다.", cap: "제2방멱(원 외부 할선): $PA\\cdot PB = PC\\cdot PD$ (주의: $PA\\cdot AB$ 가 아니라 $PA\\cdot PB$!)" },
      { say: "할선 하나가 원에 접선 피티가 되면 두 교점이 하나로 합쳐지므로 피에이 곱하기 피비는 피티의 제곱과 같습니다.", cap: "제3방멱(접선·할선 정리): $PT^2 = PA\\cdot PB = PO^2 - R^2$" }
    ],
    fChips: [
      "\\text{내부·외부 할선}:\\ \\overline{PA}\\cdot\\overline{PB}=\\overline{PC}\\cdot\\overline{PD}",
      "\\text{접선과 할선}:\\ \\overline{PT}^2=\\overline{PA}\\cdot\\overline{PB}",
      "\\text{슈타이너 방멱 공식}:\\ \\overline{PA}\\cdot\\overline{PB}=|\\overline{PO}^2-R^2|"
    ],
    fLabels: ["두 할선의 곱 = 일정", "접선² = 짧은 것 × 전체 긴 것"],
    exParts: [
      { say: "예를 들어 원 밖의 점 피에서 그은 접선의 길이가 피티는 팔이고, 할선이 원과 만나는 점 에이, 비에 대하여 피에이가 사일 때 현 에이비의 길이를 구해 봅시다.", cap: "접선 $PT=8$, 할선 시작점 $PA=4$ 일 때 원 내부의 현 $AB$ 의 길이 구하기" },
      { say: "접선과 할선의 방멱정리에 의해 팔의 제곱 육십사는 사 곱하기 전체 길이 피비와 같으므로 피비는 십육입니다.", cap: "$PT^2=PA\\cdot PB\\implies 8^2=4\\cdot PB\\implies PB=16$" },
      { say: "따라서 원 안의 현 에이비의 길이는 전체 피비 십육에서 피에이 사를 뺀 십이입니다.", cap: "$\\overline{AB}=\\overline{PB}-\\overline{PA}=16-4=12$" }
    ],
    exChips: [
      "\\overline{PT}^2=\\overline{PA}\\cdot\\overline{PB}\\implies 8^2=4\\times \\overline{PB}",
      "\\overline{PB}=\\dfrac{64}{4}=16\\quad(\\text{점 }P\\text{ 에서 끝점 }B\\text{ 까지 전체 길이})",
      "\\therefore\\ \\text{현 }\\overline{AB}=\\overline{PB}-\\overline{PA}=16-4=12"
    ],
    exLabels: ["8² = 4 × PB ➔ PB = 16", "현 AB = 16 − 4 = 12"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 1.6 - (x - 1.8) * (x - 1.8))) + 0.3, GY0: 390, GV: 165, xr: [0.1, 2.9], area: [0.6, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "A(PA=4)" }, r2: { x: 2.7, col: PK, label: "B(PB=16)" },
      fn: { t: "접선·할선 방멱 PT² = PA·PB (64 = 4 × 16) ➔ AB = 12", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "PT² = PA·PB", finalS: "AB = 12", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 반지름이 칠인 원 내부의 점 피를 지나는 현 에이비에서 피에이가 사, 피비가 구일 때 원의 중심 오에서 점 피까지의 거리 오피를 구해 볼까요?", cap: "반지름 $R=7$ 인 원 내부의 점 $P$ 에서 $PA=4,\\ PB=9$ 일 때 중심거리 $OP$ (자작 문항)" },
      { say: "점 피와 중심 오를 지나는 지름을 그으면 점 피는 지름을 칠 빼기 오피와 칠 더하기 오피로 나눕니다.", cap: "지름 할선 작도: 두 조각의 길이는 $(R-OP)=(7-d)$ 와 $(R+OP)=(7+d)$!" },
      { say: "내부 방멱정리에 의해 칠 빼기 디 곱하기 칠 더하기 디는 사 곱하기 구인 삼십육이므로 디제곱은 십삼, 즉 오피는 루트 십삼입니다.", cap: "$(7-d)(7+d)=4\\times 9\\implies 49-d^2=36\\implies d=\\overline{OP}=\\sqrt{13}$" }
    ],
    examChips: [
      "\\text{지름 할선 방멱}:\\ (R-d)(R+d)=\\overline{PA}\\cdot\\overline{PB}",
      "7^2-d^2=4\\times 9=36\\implies d^2=49-36=13",
      "\\therefore\\ \\overline{OP}=d=\\sqrt{13}"
    ],
    examLabels: ["R² − d² = PA·PB = 36", "d² = 49 − 36 = 13"],
    examGraph: {
      f: x => -0.55 * (x - 1.5) * (x - 1.5) + 1.6, GY0: 390, GV: 155, xr: [0.2, 2.8], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "7 − d" }, r2: { x: 2.6, col: GO, label: "7 + d" },
      fn: { t: "슈타이너 방멱 R² − d² = PA·PB (49 − d² = 36)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "49 − d² = 36", finalS: "OP = √13", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 외부 할선 방멱을 쓸 때 피에이 곱하기 에이비로 잘못 쓰는 실수가 가장 많습니다. 무조건 출발점 피에서부터의 길이끼리 곱하세요.", cap: "① 오답 1순위 주의: $PA\\cdot AB$ (X) $\\longrightarrow$ 반드시 출발점 $P$ 기준 $PA\\cdot PB$ (O)!" },
      { say: "둘째, 중심거리가 주어지면 중심 오를 지나는 지름 할선을 그어 알 마이너스 디와 알 플러스 디의 곱으로 식을 세우세요.", cap: "② 중심거리 방멱 공식: 원 내부는 $R^2-d^2=PA\\cdot PB$, 원 외부는 $d^2-R^2=PA\\cdot PB$!" },
      { say: "셋째, 역으로 피에이 곱하기 피비가 피씨 곱하기 피디와 같으면 네 점 에이, 비, 씨, 디는 한 원 위에 있다는 공원점 판정법이 됩니다.", cap: "③ 방멱의 역정리: $PA\\cdot PB=PC\\cdot PD$ 성립 $\\Longleftrightarrow$ 네 점 $A,B,C,D$ 는 한 원 위의 점!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 삼각형의 내심과 내접원 반지름 넓이 공식을 다루는 제백이십칠강입니다.", cap: "제127강 · 삼각형의 내심($I$)과 내접원 반지름 넓이 공식" },
      { tag: "연계 ②", say: "접선의 길이와 접현각 정리를 다루는 제백이십오강도 함께 복습해 보세요.", cap: "제125강 · 접선 길이($PA=PB$)와 접현각 정리" },
      { tag: "이 사이트", say: "이 사이트의 제백이십칠강과 제백이십오강을 이어서 보세요.", cap: "제127강 · 삼각형 내심과 반지름  /  제125강 · 접선과 접현각" }
    ],
    nextLinks: [
      { lec: 127, label: "제127강 열기 (삼각형 내심과 반지름)" },
      { lec: 125, label: "제125강 열기 (접선과 접현각)" },
      { lec: 8, label: "제8강 열기 (코사인법칙 할선 연계)" }
    ]
  },
  {
    lec: 127,
    title: "숏츠식 판서 미리보기 · 삼각형의 내심(I)과 내접원 넓이 S = ½r(a+b+c) 공식",
    desc: "세 내각의 이등분선의 교점인 내심($I$)에서 세 변까지의 거리는 내접원 반지름 $r$ 로 같으며, 넓이 $S=\\frac{1}{2}r(a+b+c)$ 와 직각삼각형 $r=\\frac{a+b-c}{2}$ 를 정리합니다.",
    hookTitle: "내접원 반지름 r 이 보이면 무조건 넓이 S = ½ r (a+b+c)!", hookSub: "직각삼각형 내접원 반지름은 더 빠르다 ➔ r = (a + b − c) / 2!",
    hookSay: "삼각형 안에 내접원이 그려진 문제에서 백 퍼센트 쓰이는 내심 넓이 분할 공식과 직각삼각형 일초 공식, 바로 정리합니다.",
    hookCap: "내심과 내접원 반지름 · 30초 정리",
    whySay: "삼각형의 내심 아이와 세 꼭짓점을 이으면 삼각형이 높이가 모두 내접원 반지름 알인 세 개의 작은 삼각형으로 쪼개지므로, 전체 넓이는 이분의 일 알 곱하기 둘레의 합이 됩니다.",
    whyCap: "$S = S_{\\triangle IAB}+S_{\\triangle IBC}+S_{\\triangle ICA} = \\dfrac{1}{2}cr+\\dfrac{1}{2}ar+\\dfrac{1}{2}br = \\dfrac{1}{2}r(a+b+c)$!",
    histTag: "헤론의 넓이 공식과 내접원", histSay: "고대 알렉산드리아의 헤론은 내접원 반지름과 삼각형의 반둘레의 곱으로 넓이를 구하는 이 원리를 확장하여 세 변의 길이만으로 넓이를 구하는 헤론의 공식을 완성했습니다.",
    histCap: "반둘레 $s=\\dfrac{a+b+c}{2}$ 일 때 $S = r\\cdot s$ (내접원 반지름 $r = \\dfrac{S}{s}$!)",
    fParts: [
      { say: "삼각형의 넓이 에스와 세 변의 길이를 알면 내접원의 반지름 알은 이 에스를 세 변의 합으로 나누어 즉시 구할 수 있습니다.", cap: "내접원 반지름 만능 공식: $S=\\dfrac{1}{2}r(a+b+c)\\ \\Longleftrightarrow\\ r=\\dfrac{2S}{a+b+c}$" },
      { say: "특히 직각삼각형에서는 꼭짓점 부근이 정사각형 알 바이 알이 되므로 내접원 반지름 알은 두 직각변의 합에서 빗변을 뺀 값의 절반입니다.", cap: "직각삼각형($\\angle C=90^\\circ$) 전용 공식: $r = \\dfrac{a+b-c}{2}$ (정사각형 격자 성질!)" },
      { say: "내심 아이에서 바라본 중심각 비아이씨는 항상 구십도 더하기 꼭짓점 각 에이의 절반입니다.", cap: "내심 각 공식: $\\angle BIC = 90^\\circ + \\dfrac{1}{2}\\angle A$ (외심 $\\angle BOC = 2\\angle A$ 와 구별!)" }
    ],
    fChips: [
      "S=\\dfrac{1}{2}r(a+b+c)\\iff r=\\dfrac{2S}{a+b+c}",
      "\\text{직각삼각형}(\\angle C=90^\\circ):\\ r=\\dfrac{a+b-c}{2}",
      "\\angle BIC=90^\\circ+\\dfrac{1}{2}\\angle A,\\quad \\overline{AD}=\\dfrac{b+c-a}{2}"
    ],
    fLabels: ["넓이 S = ½ r × 둘레", "직각삼각형 r = (a+b−c)/2"],
    exParts: [
      { say: "예를 들어 세 변의 길이가 오, 십이, 십삼인 직각삼각형에 내접하는 원의 반지름 알과 내심에서 직각 꼭짓점까지의 거리를 구해 봅시다.", cap: "세 변이 $5,12,13$ 인 직각삼각형의 내접원 반지름 $r$ 과 $CI$ 의 길이 구하기" },
      { say: "직각삼각형 내접원 공식에 의해 반지름 알은 오 더하기 십이 빼기 십삼을 이로 나눈 이입니다.", cap: "$r=\\dfrac{a+b-c}{2}=\\dfrac{5+12-13}{2}=2$ (넓이 $30=\\dfrac{1}{2}r(30)$ 과도 일치!)" },
      { say: "직각 꼭짓점 씨와 내심 아이는 한 변이 이인 정사각형의 대각선이므로 거리는 이 루트 이입니다.", cap: "정사각형 대각선: $\\overline{CI}=\\sqrt{2}\\,r=2\\sqrt{2}$" }
    ],
    exChips: [
      "5^2+12^2=13^2\\implies \\angle C=90^\\circ\\text{ 직각삼각형}",
      "r=\\dfrac{5+12-13}{2}=2\\quad\\left(\\text{또는 }30=\\dfrac{1}{2}r(30)\\implies r=2\\right)",
      "\\therefore\\ r=2,\\quad \\overline{CI}=\\sqrt{2}\\,r=2\\sqrt{2}"
    ],
    exLabels: ["r = (5+12−13)/2 = 2", "직각 꼭짓점 거리 = √2 r"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 1.3 - (x - 1.2) * (x - 1.2))) + 0.3, GY0: 390, GV: 165, xr: [0.1, 2.9], area: [0.3, 2.3], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.2, col: CY, label: "내심 I(r=2)" }, r2: { x: 2.3, col: GO, label: "접점 D" },
      fn: { t: "5:12:13 직각삼각형 내접원 r = (5+12−13)/2 = 2", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "r = 2", finalS: "CI = 2√2", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 에이비가 오, 비씨가 칠, 씨에이가 팔인 삼각형 에이비씨에서 각 비가 육십도일 때 내접원의 반지름 알을 구해 볼까요?", cap: "$c=5,\\ a=7,\\ b=8,\\ \\angle B=60^\\circ$ 인 $\\triangle ABC$ 의 내접원 반지름 $r$ (자작 문항)" },
      { say: "먼저 삼각형의 넓이 에스는 이분의 일 곱하기 오 곱하기 칠 곱하기 사인 육십도이므로 사분의 삼십오 루트 삼입니다.", cap: "$S=\\dfrac{1}{2}ca\\sin 60^\\circ=\\dfrac{1}{2}\\times 5\\times 7\\times\\dfrac{\\sqrt{3}}{2}=\\dfrac{35\\sqrt{3}}{4}$" },
      { say: "둘레의 합이 이십이므로 넓이 공식에 대입하면 십 알이 사분의 삼십오 루트 삼이 되어 반지름 알은 팔분의 칠 루트 삼입니다.", cap: "$S=\\dfrac{1}{2}r(5+7+8)=10r=\\dfrac{35\\sqrt{3}}{4}\\implies r=\\dfrac{7\\sqrt{3}}{8}$" }
    ],
    examChips: [
      "S=\\dfrac{1}{2}\\times 5\\times 7\\sin 60^\\circ=\\dfrac{35\\sqrt{3}}{4}",
      "S=\\dfrac{1}{2}r(5+7+8)=10r",
      "\\therefore\\ 10r=\\dfrac{35\\sqrt{3}}{4}\\implies r=\\dfrac{7\\sqrt{3}}{8}"
    ],
    examLabels: ["사인 넓이 S = 35√3 / 4", "10r = S ➔ r = 7√3 / 8"],
    examGraph: {
      f: x => -0.55 * (x - 1.5) * (x - 1.5) + 1.55, GY0: 390, GV: 155, xr: [0.2, 2.8], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "둘레 a+b+c = 20" }, r2: { x: 2.3, col: PK, label: "S = 35√3 / 4" },
      fn: { t: "사인 넓이 공식과 내접원 넓이 공식의 연립: ½ca sinB = ½r(a+b+c)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "10r = 35√3/4", finalS: "r = 7√3/8", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 수능에서 내접원의 반지름 알을 물어보면 구십구 퍼센트 다른 방법인 이분의 일 에이비 사인 세타로 넓이를 먼저 구한 뒤 둘레 공식과 연립하는 문제입니다.", cap: "① 내접원 $r$ 구하기 표준 루트: $\\dfrac{1}{2}ab\\sin C$ 로 $S$ 계산 $\\longrightarrow\\ S=\\dfrac{1}{2}r(a+b+c)$ 연립!" },
      { say: "둘째, 꼭짓점 에이에서 내접원의 접점까지의 길이는 언제나 반둘레 에스에서 마주 보는 변 에이를 뺀 값입니다.", cap: "② 접점까지의 길이 공식: $\\overline{AD}=\\overline{AE}=s-a=\\dfrac{b+c-a}{2}$!" },
      { say: "셋째, 미적분 무한등비급수 도형에서 직각삼각형 안의 원이 나오면 알은 이분의 에이 더하기 비 빼기 씨로 일초 만에 첫째항을 구하세요.", cap: "③ 등비급수 도형 필살기: 직각삼각형 내접원은 $r=\\dfrac{a+b-c}{2}$, 꼭짓점-내심 거리는 $\\sqrt{2}\\,r$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 삼각형의 외심과 수심, 그리고 사인법칙 지름 보조선을 다루는 제백이십팔강입니다.", cap: "제128강 · 삼각형의 외심($O$)·수심($H$)과 사인법칙 지름($2R$)" },
      { tag: "연계 ②", say: "내각과 외각의 이등분선 정리를 다루는 제백삼십강도 함께 확인해 보세요.", cap: "제130강 · 내각·외각의 이등분선 정리($AB:AC=BD:CD$)" },
      { tag: "이 사이트", say: "이 사이트의 제백이십팔강과 제백삼십강을 이어서 보세요.", cap: "제128강 · 외심·수심과 외접원  /  제130강 · 각의 이등분선" }
    ],
    nextLinks: [
      { lec: 128, label: "제128강 열기 (외심·수심과 외접원)" },
      { lec: 130, label: "제130강 열기 (각의 이등분선 정리)" },
      { lec: 16, label: "제16강 열기 (삼각형 넓이 5대 공식)" }
    ]
  },
  {
    lec: 128,
    title: "숏츠식 판서 미리보기 · 삼각형의 외심(O)·수심(H)과 사인법칙 지름(2R) 보조선",
    desc: "세 변의 수직이등분선의 교점인 외심($O$)은 세 꼭짓점까지의 거리가 외접원 반지름 $R$ 로 같습니다. 지름 보조선으로 사인법칙 $a=2R\\sin A$ 를 직관적으로 증명합니다.",
    hookTitle: "외심 O 가 보이면 꼭짓점까지 R = R = R 이등변삼각형 3개!", hookSub: "직각삼각형의 외심은 무조건 빗변의 중점(R = c / 2)!",
    hookSay: "사인법칙의 뿌리인 삼각형의 외심과 직각삼각형 빗변의 중점 성질, 그리고 수심과의 대칭 관계까지 삼십 초 만에 정리합니다.",
    hookCap: "외심·수심과 외접원 · 30초 정리",
    whySay: "외심 오를 지나는 지름 비프라임씨를 그으면 원주각 에이와 에이프라임이 같고 지름에 대한 원주각이 구십도가 되어, 직각삼각형에서 사인 에이는 이알 분의 에이가 바로 유도됩니다.",
    whyCap: "지름 $B'C=2R$ 작도 $\\implies \\angle B'AC=90^\\circ\\implies \\sin A=\\sin A'=\\dfrac{a}{2R}$!",
    histTag: "오일러 직선(Euler Line)", histSay: "레온하르트 오일러는 어떤 삼각형에서든 외심 오와 무게중심 지, 그리고 세 수선의 교점인 수심 에이치가 항상 한 직선 위에 일 대 이의 비율로 놓인다는 오일러 직선을 발견했습니다.",
    histCap: "오일러 직선 정리: 외심 $O$ — 무게중심 $G$ — 수심 $H$ 일직선 ($OG:GH = 1:2$!)",
    fParts: [
      { say: "외심 오에서 세 꼭짓점까지의 거리는 모두 외접원 반지름 라지 알로 같고, 외심에서 변에 내린 수선은 그 변을 수직이등분합니다.", cap: "외심 기본 성질: $OA=OB=OC=R$ · 중심각 $\\angle BOC=2\\angle A$ · 현 수직이등분!" },
      { say: "특히 직각삼각형의 외심은 언제나 빗변의 중점에 위치하므로, 빗변의 중점에서 세 꼭짓점까지의 거리가 모두 빗변의 절반으로 같습니다.", cap: "직각삼각형 외심 철칙: 외심 $O=$ 빗변의 중점 $M\\implies MA=MB=MC=\\dfrac{c}{2}=R$!" },
      { say: "세 꼭짓점에서 대변에 내린 수선의 교점인 수심 에이치에서는 마주 보는 각 에이와 각 비에이치씨의 합이 백팔십도가 됩니다.", cap: "수심($H$) 각 공식: $\\angle BHC = 180^\\circ - \\angle A$ (수선의 발 사각형 공원점!)" }
    ],
    fChips: [
      "\\overline{OA}=\\overline{OB}=\\overline{OC}=R,\\quad \\angle BOC=2\\angle A,\\quad a=2R\\sin A",
      "\\text{직각삼각형 외심 }M:\\ \\overline{MA}=\\overline{MB}=\\overline{MC}=\\dfrac{c}{2}=R",
      "\\text{수심 }H:\\ \\angle BHC=180^\\circ-\\angle A,\\quad \\overline{AH}=2R|\\cos A|"
    ],
    fLabels: ["OA = OB = OC = R (외접원)", "직각삼각형 외심 = 빗변 중점"],
    exParts: [
      { say: "예를 들어 각 씨가 구십도인 직각삼각형에서 두 직각변이 육과 팔일 때 외접원 반지름 라지 알과 내접원 반지름 스몰 알의 합을 구해 봅시다.", cap: "직각변이 $6,8$ 이고 빗변이 $10$ 인 직각삼각형에서 $R+r$ 구하기" },
      { say: "빗변의 길이가 십이므로 외접원 반지름 라지 알은 빗변의 절반인 오입니다.", cap: "외심 $=$ 빗변의 중점 $\\implies R=\\dfrac{10}{2}=5$" },
      { say: "내접원 반지름 스몰 알은 육 더하기 팔 빼기 십을 이로 나눈 이이므로 두 반지름의 합은 칠입니다.", cap: "$r=\\dfrac{6+8-10}{2}=2\\implies R+r=5+2=7$" }
    ],
    exChips: [
      "c=\\sqrt{6^2+8^2}=10\\implies \\text{외접원 반지름 }R=\\dfrac{c}{2}=5",
      "\\text{내접원 반지름 }r=\\dfrac{6+8-10}{2}=2",
      "\\therefore\\ R+r=5+2=7\\quad(\\text{참고: 직각삼각형 }a+b=2(R+r))"
    ],
    exLabels: ["외접원 R = c/2 = 5", "내접원 r = 2 ➔ R+r = 7"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 2.0 - (x - 1.5) * (x - 1.5))), GY0: 390, GV: 185, xr: [0.1, 2.9], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.5, col: CY, label: "빗변 중점 M(외심)" }, r2: { x: 2.7, col: GO, label: "R = 5, r = 2" },
      fn: { t: "직각삼각형 빗변 중점 M = 외심 O (MA=MB=MC=R=5)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "R=5, r=2", finalS: "R + r = 7", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 예각삼각형 에이비씨의 외심을 오라 할 때, 각 에이가 육십도이고 비씨가 육 루트 삼이라면 삼각형 오비씨의 넓이는 얼마일까요?", cap: "$\\angle A=60^\\circ,\\ BC=6\\sqrt{3}$ 인 $\\triangle ABC$ 의 외심 $O$ 에 대해 $\\triangle OBC$ 넓이 (자작 문항)" },
      { say: "사인법칙에 의해 이알은 사인 육십도 분의 육 루트 삼인 십이이므로 외접원 반지름 라지 알은 육입니다.", cap: "$2R=\\dfrac{BC}{\\sin 60^\\circ}=\\dfrac{6\\sqrt{3}}{\\sqrt{3}/2}=12\\implies OB=OC=R=6$" },
      { say: "중심각 비오씨는 원주각 육십도의 두 배인 백이십도이므로 삼각형 오비씨의 넓이는 이분의 일 곱하기 육의 제곱 곱하기 사인 백이십도인 구 루트 삼입니다.", cap: "$\\angle BOC=2\\angle A=120^\\circ\\implies S_{\\triangle OBC}=\\dfrac{1}{2}\\times 6^2\\sin 120^\\circ=9\\sqrt{3}$" }
    ],
    examChips: [
      "\\text{사인법칙}:\\ 2R=\\dfrac{6\\sqrt{3}}{\\sin 60^\\circ}=12\\implies \\overline{OB}=\\overline{OC}=R=6",
      "\\text{중심각}:\\ \\angle BOC=2\\angle A=120^\\circ",
      "\\therefore\\ S_{\\triangle OBC}=\\dfrac{1}{2}\\times 6\\times 6\\sin 120^\\circ=9\\sqrt{3}"
    ],
    examLabels: ["사인법칙 ➔ R = 6", "중심각 120° ➔ 넓이 9√3"],
    examGraph: {
      f: x => -0.5 * (x - 1.5) * (x - 1.5) + 1.55, GY0: 390, GV: 155, xr: [0.2, 2.8], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "B(OB=6)" }, r2: { x: 2.5, col: PK, label: "C(OC=6)" },
      fn: { t: "이등변삼각형 △OBC (OB=OC=R=6, ∠BOC=120°)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "R=6, 120°", finalS: "S = 9√3", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 문제에서 직각삼각형의 빗변의 중점이 찍혀 있으면 무조건 외심임을 눈치채고 직각 꼭짓점까지 이은 중선의 길이가 빗변의 절반임을 표시하세요.", cap: "① 직각삼각형 빗변 중점 $M$ 등장 $\\Longrightarrow\\ MA=MB=MC$ (외접원 반지름 $R$) 즉시 표시!" },
      { say: "둘째, 외심 오가 등장하면 삼각형 오에이비, 오비씨, 오씨에이는 모두 양변이 라지 알인 이등변삼각형입니다.", cap: "② 외심 보조선: $OA,OB,OC$ 를 그으면 꼭짓각이 $2C, 2A, 2B$ 인 이등변삼각형 3개 완성!" },
      { say: "셋째, 둔각삼각형의 외심은 삼각형의 외부에 놓이고 중심각은 삼백육십도 빼기 이 에이가 됩니다.", cap: "③ 외심의 위치: 예각삼각형(내부) · 직각삼각형(빗변 중점) · 둔각삼각형(외부)!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 삼각형의 무게중심 이 대 일 내분과 파푸스의 중선정리를 다루는 제백이십구강입니다.", cap: "제129강 · 무게중심($G$) $2:1$ 내분·6등분 넓이와 파푸스 중선정리" },
      { tag: "연계 ②", say: "삼각형의 내심과 내접원 반지름 공식을 다루는 제백이십칠강도 함께 복습해 보세요.", cap: "제127강 · 삼각형의 내심($I$)과 내접원 넓이 공식" },
      { tag: "이 사이트", say: "이 사이트의 제백이십구강과 제백이십칠강을 이어서 보세요.", cap: "제129강 · 무게중심과 중선정리  /  제127강 · 내심과 내접원" }
    ],
    nextLinks: [
      { lec: 129, label: "제129강 열기 (무게중심과 중선정리)" },
      { lec: 127, label: "제127강 열기 (내심과 내접원)" },
      { lec: 7, label: "제7강 열기 (사인법칙과 외접원)" }
    ]
  },
  {
    lec: 129,
    title: "숏츠식 판서 미리보기 · 무게중심(G) 2:1 내분·6등분 넓이와 파푸스 중선정리",
    desc: "세 중선의 교점인 무게중심($G$)은 중선을 꼭짓점으로부터 $2:1$ 로 내분하고 삼각형 넓이를 6등분합니다. 중선의 길이는 파푸스 정리 $b^2+c^2=2(m^2+d^2)$ 로 구합니다.",
    hookTitle: "무게중심 G 는 중선을 무조건 2:1 내분 · 넓이는 6등분!", hookSub: "중선의 길이 m 은 파푸스 중선정리 b² + c² = 2 (m² + d²)!",
    hookSay: "도형과 벡터, 좌표기하 전 영역에서 가장 많이 등장하는 무게중심의 이 대 일 비율과 파푸스 중선정리를 삼십 초 만에 완벽 정리합니다.",
    hookCap: "무게중심 & 파푸스 중선정리 · 30초 정리",
    whySay: "두 중선의 발 디와 이를 이으면 중점연결정리에 의해 밑변 에이비와 평행하고 길이가 절반이 되므로, 모래시계 닮음에 의해 무게중심 지가 중선을 정확히 이 대 일로 내분합니다.",
    whyCap: "중점연결정리 $DE\\parallel AB,\\ DE=\\dfrac{1}{2}AB\\implies \\triangle ABG\\sim\\triangle DEG\\ (2:1$ 닮음!)",
    histTag: "아르키메데스의 무게중심과 파푸스 정리", histSay: "아르키메데스는 삼각형 판의 물리적 평형점이 세 중선의 교점임을 증명했고, 알렉산드리아의 파푸스는 평행사변형 대각선 제곱의 합 공식으로 중선의 길이를 계산했습니다.",
    histCap: "아르키메데스 질량중심 $G=\\dfrac{A+B+C}{3}$ · 파푸스 $AB^2+AC^2=2(AM^2+BM^2)$!",
    fParts: [
      { say: "무게중심 지는 각 중선을 꼭짓점으로부터 이 대 일로 내분하고, 세 중선은 삼각형의 넓이를 똑같은 넓이 여섯 조각으로 육등분합니다.", cap: "무게중심 비율·넓이: $AG:GM=2:1$ · $S_{\\triangle GAB}=S_{\\triangle GBC}=S_{\\triangle GCA}=\\dfrac{1}{3}S$" },
      { say: "밑변의 중점 엠을 연결한 중선의 길이 엠을 구할 때는 양옆 두 변의 제곱의 합이 중선 제곱 더하기 반밑변 제곱의 두 배와 같다는 파푸스 정리를 씁니다.", cap: "파푸스 중선정리: $AB^2+AC^2 = 2(AM^2+BM^2)$ (코사인법칙 2번을 1줄로 단축!)" },
      { say: "벡터에서 점 지가 무게중심일 필요충분조건은 지에이 더하기 지비 더하기 지씨가 영벡터가 되는 것입니다.", cap: "벡터·좌표 표현: $\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\vec{0}\\ \\Longleftrightarrow\\ G\\left(\\dfrac{x_1+x_2+x_3}{3},\\dfrac{y_1+y_2+y_3}{3}\\right)$" }
    ],
    fChips: [
      "\\overline{AG}:\\overline{GM}=2:1,\\quad S_{\\triangle GBC}=\\dfrac{1}{3}S,\\quad S_{\\triangle GBD}=\\dfrac{1}{6}S",
      "\\text{파푸스 중선정리}:\\ b^2+c^2=2\\left(\\overline{AM}^2+\\overline{BM}^2\\right)",
      "\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\vec{0}\\iff \\overrightarrow{PG}=\\dfrac{\\overrightarrow{PA}+\\overrightarrow{PB}+\\overrightarrow{PC}}{3}"
    ],
    fLabels: ["꼭짓점부터 2 : 1 내분", "파푸스: b²+c² = 2(AM²+BM²)"],
    exParts: [
      { say: "예를 들어 에이비가 칠, 에이씨가 오, 비씨가 육인 삼각형 에이비씨에서 변 비씨의 중점을 엠, 무게중심을 지라 할 때 선분 에이지의 길이를 구해 봅시다.", cap: "$AB=7,\\ AC=5,\\ BC=6$ 일 때 중선 $AM$ 과 무게중심까지의 거리 $AG$ 구하기" },
      { say: "반밑변 비엠이 삼이므로 파푸스 중선정리에 대입하면 사십구 더하기 이십오는 이 곱하기 에이엠 제곱 더하기 구가 되어 에이엠은 루트 이십팔, 즉 이 루트 칠입니다.", cap: "$7^2+5^2=2(AM^2+3^2)\\implies 74=2(AM^2+9)\\implies AM=2\\sqrt{7}$" },
      { say: "무게중심 지는 중선 에이엠을 이 대 일로 내분하므로 에이지는 에이엠의 삼분의 이인 삼분의 사 루트 칠입니다.", cap: "$\\overline{AG}=\\dfrac{2}{3}\\overline{AM}=\\dfrac{4\\sqrt{7}}{3}$" }
    ],
    exChips: [
      "\\overline{BM}=3,\\quad 7^2+5^2=2\\left(\\overline{AM}^2+3^2\\right)\\implies 74=2(\\overline{AM}^2+9)",
      "\\overline{AM}^2=37-9=28\\implies \\overline{AM}=2\\sqrt{7}",
      "\\therefore\\ \\overline{AG}=\\dfrac{2}{3}\\overline{AM}=\\dfrac{4\\sqrt{7}}{3}"
    ],
    exLabels: ["파푸스 ➔ AM = 2√7", "2:1 내분 ➔ AG = 4√7 / 3"],
    exGraph: {
      f: x => -0.55 * (x - 1.5) * (x - 1.5) + 1.55, GY0: 390, GV: 155, xr: [0.2, 2.8], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.5, col: CY, label: "중점 M(BM=3)" }, r2: { x: 1.5, col: GO, label: "무게중심 G(2:1)" },
      fn: { t: "파푸스 중선정리 AM = 2√7 ➔ AG = (2/3)AM = 4√7 / 3", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "AM = 2√7", finalS: "AG = 4√7/3", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 삼각형 에이비씨의 두 중선 비이와 씨에프가 서로 수직으로 만나고 그 길이가 각각 구와 십이일 때, 삼각형 에이비씨의 넓이와 변 비씨의 길이를 구해 볼까요?", cap: "두 중선 $BE=9,\\ CF=12$ 가 무게중심 $G$ 에서 직교할 때 $\\triangle ABC$ 넓이와 $BC$ (자작 문항)" },
      { say: "무게중심 지가 두 중선을 이 대 일로 나누므로 비지는 육, 씨지는 팔이고, 직각삼각형 비지씨에서 피타고라스 정리에 의해 비씨는 십입니다.", cap: "$BG=\\dfrac{2}{3}(9)=6,\\ CG=\\dfrac{2}{3}(12)=8\\implies BC=\\sqrt{6^2+8^2}=10$" },
      { say: "또한 직각삼각형 비지씨의 넓이가 이십사인데 이것이 전체 넓이의 삼분의 일이므로 삼각형 에이비씨의 넓이는 칠십이입니다.", cap: "$S_{\\triangle GBC}=\\dfrac{1}{2}\\times 6\\times 8=24=\\dfrac{1}{3}S_{\\triangle ABC}\\implies S_{\\triangle ABC}=72$" }
    ],
    examChips: [
      "\\overline{BG}=\\dfrac{2}{3}\\times 9=6,\\quad \\overline{CG}=\\dfrac{2}{3}\\times 12=8\\quad(\\angle BGC=90^\\circ)",
      "\\overline{BC}=\\sqrt{6^2+8^2}=10,\\quad S_{\\triangle GBC}=\\dfrac{1}{2}\\times 6\\times 8=24",
      "\\therefore\\ S_{\\triangle ABC}=3\\,S_{\\triangle GBC}=72,\\quad \\overline{BC}=10"
    ],
    examLabels: ["BG=6, CG=8 ➔ BC = 10", "넓이 S = 3 × 24 = 72"],
    examGraph: {
      f: x => 0.45 * (x - 1.5) * (x - 1.5) + 0.45, GY0: 390, GV: 140, xr: [0.2, 2.8], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "BG = 6" }, r2: { x: 2.3, col: PK, label: "CG = 8 (직교)" },
      fn: { t: "직교하는 두 중선 ➔ △GBC 는 6:8:10 직각삼각형 (넓이 1/3)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "S_GBC = 24", finalS: "전체 S = 72", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 문제에 중점이 두 개 보이면 무조건 무게중심이나 중점연결정리를 의심해야 합니다.", cap: "① 중점 2개 등장 신호: 중선 2개 교점 $=$ 무게중심($2:1$) · 중점끼리 연결 $=$ 밑변의 $\\dfrac{1}{2}$ 평행선!" },
      { say: "둘째, 정삼각형에서는 외심, 내심, 무게중심, 수심이 모두 한 점으로 일치하므로 높이를 이 대 일로 나눈 점이 곧 외접원과 내접원의 중심입니다.", cap: "② 정삼각형 만능 비율: 외심$=$내심$=$무게중심 $\\implies R:r = 2:1$ ($R=\\dfrac{\\sqrt{3}}{3}a,\\ r=\\dfrac{\\sqrt{3}}{6}a$)!" },
      { say: "셋째, 삼각형의 세 변의 중점을 연결해 만든 작은 삼각형의 무게중심은 원래 큰 삼각형의 무게중심과 언제나 일치합니다.", cap: "③ 무게중심 불변성: 세 변을 같은 비율 $m:n$ 으로 내분한 삼각형의 무게중심 $=$ 원래 무게중심 $G$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 삼각형의 내각과 외각의 이등분선 비율과 길이 공식을 다루는 제백삼십강입니다.", cap: "제130강 · 내각·외각의 이등분선 정리($AB:AC=BD:CD$)" },
      { tag: "연계 ②", say: "내분점과 외분점, 아폴로니우스의 원을 다루는 제오십이강도 함께 복습해 보세요.", cap: "제52강 · 내분·외분점과 무게중심·아폴로니우스 원 (공통수학 2)" },
      { tag: "이 사이트", say: "이 사이트의 제백삼십강과 제오십이강을 이어서 보세요.", cap: "제130강 · 각의 이등분선 정리  /  제52강 · 내분점과 무게중심" }
    ],
    nextLinks: [
      { lec: 130, label: "제130강 열기 (각의 이등분선 정리)" },
      { lec: 52, label: "제52강 열기 (내분·외분과 무게중심)" },
      { lec: 128, label: "제128강 열기 (외심·수심과 외접원)" }
    ]
  }
];

const MIDGEO_SPECS_B = [
  {
    lec: 130,
    title: "숏츠식 판서 미리보기 · 내각·외각의 이등분선 비율(AB:AC=BD:CD)과 길이 공식",
    desc: "삼각형 $\\angle A$ 의 내각·외각의 이등분선이 밑변 $BC$ 와 만나는 점 $D$ 는 언제나 $AB:AC=BD:CD$ 를 만족하며, 이등분선 길이는 $AD^2=AB\\cdot AC-BD\\cdot CD$ 또는 넓이 합으로 구합니다.",
    hookTitle: "각의 이등분선 · 양옆 변의 비(c:b) = 밑변 조각의 비(BD:CD)!", hookSub: "이등분선 길이 x 는 넓이 합 S = S₁ + S₂ 또는 AD² = bc − mn!",
    hookSay: "수능 도형과 해석기하에서 해마다 출제되는 내각의 이등분선 비율 공식과 이등분선의 길이를 구하는 두 가지 필살기를 바로 정리합니다.",
    hookCap: "각의 이등분선 정리 · 30초 정리",
    whySay: "두 삼각형 에이비디와 에이씨디의 넓이 비를 밑변 비디 대 씨디로 구한 값과, 끼인각이 절반으로 같다는 성질을 이용해 이분의 일 에이비 사인 세타로 구한 값이 같으므로 양옆 변의 비가 밑변의 비가 됩니다.",
    whyCap: "$\\dfrac{S_{\\triangle ABD}}{S_{\\triangle ACD}}=\\dfrac{BD}{CD}=\\dfrac{\\frac{1}{2}\\,AB\\cdot AD\\sin(\\theta/2)}{\\frac{1}{2}\\,AC\\cdot AD\\sin(\\theta/2)}=\\dfrac{AB}{AC}$!",
    histTag: "유클리드 원론 제6권 명제 3과 스튜어트 정리", histSay: "유클리드는 평행선 보조선을 그어 이등변삼각형을 만드는 기하학적 방법으로 각의 이등분선 비례식을 증명했고, 스튜어트는 이등분선의 길이 제곱이 양옆 변의 곱 빼기 밑변 조각의 곱임을 밝혔습니다.",
    histCap: "비율: $AB:AC = BD:CD$ · 길이 제곱: $AD^2 = AB\\cdot AC - BD\\cdot CD$!",
    fParts: [
      { say: "각 에이의 내각의 이등분선이 밑변과 만나는 점 디는 밑변 비씨를 양옆 변의 길이의 비인 에이비 대 에이씨로 내분합니다.", cap: "내각의 이등분선 정리: $AB:AC = BD:CD$ (내분점 공식 + 넓이비 $S_1:S_2=c:b$!)" },
      { say: "각 에이의 외각의 이등분선이 밑변의 연장선과 만나는 점 디프라임은 밑변 비씨를 에이비 대 에이씨로 외분합니다.", cap: "외각의 이등분선 정리: $AB:AC = BD':CD'$ (나이키 공식 · 아폴로니우스 원의 지름 양끝!)" },
      { say: "각의 이등분선 자체의 길이 에이디를 구할 때는 전체 넓이는 왼쪽 넓이 더하기 오른쪽 넓이라는 식을 세우거나 에이디 제곱은 에이비 곱하기 에이씨 빼기 비디 곱하기 씨디 공식을 씁니다.", cap: "이등분선 길이 공식: ① $S=S_1+S_2$ (특수각) ② $AD^2 = AB\\cdot AC - BD\\cdot CD$ (일반각!)" }
    ],
    fChips: [
      "\\text{내각·외각 이등분선}:\\ \\overline{AB}:\\overline{AC}=\\overline{BD}:\\overline{CD}",
      "\\text{넓이 합 공식}:\\ \\dfrac{1}{2}bc\\sin A=\\dfrac{1}{2}(b+c)\\,\\overline{AD}\\sin\\dfrac{A}{2}",
      "\\text{스튜어트 길이 공식}:\\ \\overline{AD}^2=\\overline{AB}\\cdot\\overline{AC}-\\overline{BD}\\cdot\\overline{CD}"
    ],
    fLabels: ["AB : AC = BD : CD", "AD² = AB·AC − BD·CD"],
    exParts: [
      { say: "예를 들어 에이비가 육, 에이씨가 삼이고 각 에이가 백이십도인 삼각형에서 각 에이의 이등분선 에이디의 길이를 구해 봅시다.", cap: "$AB=6,\\ AC=3,\\ \\angle A=120^\\circ$ 일 때 각의 이등분선 $AD=x$ 의 길이 구하기" },
      { say: "전체 넓이는 이분의 일 곱하기 육 곱하기 삼 곱하기 사인 백이십도이고, 두 조각의 넓이 합은 이분의 일 곱하기 육 더하기 삼 곱하기 엑스 사인 육십도입니다.", cap: "$\\dfrac{1}{2}\\cdot 6\\cdot 3\\sin 120^\\circ = \\dfrac{1}{2}(6+3)x\\sin 60^\\circ$" },
      { say: "사인 백이십도와 사인 육십도가 약분되므로 십팔은 구 엑스가 되어 이등분선의 길이 엑스는 이입니다.", cap: "$\\sin 120^\\circ=\\sin 60^\\circ\\text{ 약분}\\implies 18=9x\\implies \\overline{AD}=x=2$" }
    ],
    exChips: [
      "S=S_{\\triangle ABD}+S_{\\triangle ACD}\\implies \\dfrac{1}{2}(6)(3)\\sin 120^\\circ=\\dfrac{1}{2}(6+3)x\\sin 60^\\circ",
      "\\sin 120^\\circ=\\sin 60^\\circ=\\dfrac{\\sqrt{3}}{2}\\text{ 양변 약분}",
      "\\therefore\\ x=\\dfrac{2\\times 6\\times 3}{6+3}=\\dfrac{36}{9}=2"
    ],
    exLabels: ["S = S₁ + S₂ 넓이 분할", "AD = 2bc/(b+c) = 2"],
    exGraph: {
      f: x => -0.55 * (x - 1.3) * (x - 1.3) + 1.55, GY0: 390, GV: 155, xr: [0.2, 2.8], area: [0.4, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "B(AB=6)" }, r2: { x: 1.8, col: GO, label: "D(BD:CD=2:1)" },
      fn: { t: "∠A = 120° 이등분 (60° + 60°) 넓이 합 S = S₁ + S₂", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "BD:CD = 2:1", finalS: "AD = 2", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 에이비가 사, 에이씨가 유, 비씨가 오인 삼각형 에이비씨에서 각 에이의 이등분선이 비씨와 만나는 점을 디라 할 때 선분 에이디의 제곱을 구해 볼까요?", cap: "세 변이 $AB=4,\\ AC=6,\\ BC=5$ 일 때 각의 이등분선 길이 제곱 $AD^2$ 구하기 (자작 문항)" },
      { say: "에이비 대 에이씨가 사 대 유인 이 대 삼이므로, 오인 밑변 비씨를 이 대 삼으로 나누면 비디는 이, 씨디는 삼입니다.", cap: "$BD:CD = AB:AC = 4:6 = 2:3\\implies BD=2,\\ CD=3$" },
      { say: "스튜어트 이등분선 길이 공식에 대입하면 에이디의 제곱은 사 곱하기 유 빼기 이 곱하기 삼인 십팔입니다.", cap: "$\\overline{AD}^2 = \\overline{AB}\\cdot\\overline{AC} - \\overline{BD}\\cdot\\overline{CD} = 4\\times 6 - 2\\times 3 = 18$" }
    ],
    examChips: [
      "\\overline{BD}:\\overline{CD}=4:6=2:3,\\quad \\overline{BC}=5\\implies \\overline{BD}=2,\\ \\overline{CD}=3",
      "\\overline{AD}^2=\\overline{AB}\\cdot\\overline{AC}-\\overline{BD}\\cdot\\overline{CD}",
      "\\therefore\\ \\overline{AD}^2=4\\times 6-2\\times 3=24-6=18\\quad(\\overline{AD}=3\\sqrt{2})"
    ],
    examLabels: ["2:3 내분 ➔ BD=2, CD=3", "AD² = 24 − 6 = 18"],
    examGraph: {
      f: x => 0.45 * (x - 1.4) * (x - 1.4) + 0.45, GY0: 390, GV: 140, xr: [0.2, 2.8], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "BD = 2" }, r2: { x: 2.1, col: PK, label: "CD = 3" },
      fn: { t: "스튜어트 공식 AD² = AB·AC − BD·CD = 24 − 6 = 18", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "24 − 6", finalS: "AD² = 18", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 백이십도나 구십도, 육십도를 이등분할 때는 넓이 합 공식 에스는 에스원 더하기 에스투가 가장 빠릅니다.", cap: "① 특수각($60^\\circ,90^\\circ,120^\\circ$) 이등분선 길이: 무조건 넓이 합 $S=S_1+S_2$ 로 3초 암산!" },
      { say: "둘째, 세 변의 길이만 주어졌을 때는 코사인법칙을 두 번 쓰는 대신 에이디 제곱은 에이비 에이씨 빼기 비디 씨디 공식을 쓰면 계산 시간이 십분의 일로 줄어듭니다.", cap: "② 세 변이 주어진 일반각 이등분선: $AD^2 = bc - mn$ 공식으로 코사인법칙 생략!" },
      { say: "셋째, 내각의 이등분선과 외각의 이등분선은 항상 수직으로 만나며, 두 교점 디와 디프라임을 지름의 양 끝으로 하는 원이 바로 아폴로니우스의 원입니다.", cap: "③ 아폴로니우스 원과의 연결: 내각·외각 이등분선은 직교($90^\\circ$)하며 $DD'$ 가 원의 지름!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 직각삼각형 수선의 발 사영정리 사대 공식과 소 공식을 다루는 제백삼십일강입니다.", cap: "제131강 · 직각삼각형 닮음 사영정리 4대 공식($h^2=xy,\\ a^2=xc$)" },
      { tag: "연계 ②", say: "삼각형의 내심과 내접원 넓이 공식을 다루는 제백이십칠강도 함께 복습해 보세요.", cap: "제127강 · 삼각형 내심($I$)과 내접원 넓이 공식" },
      { tag: "이 사이트", say: "이 사이트의 제백삼십일강과 제백이십칠강을 이어서 보세요.", cap: "제131강 · 직각삼각형 사영정리  /  제127강 · 삼각형의 내심" }
    ],
    nextLinks: [
      { lec: 131, label: "제131강 열기 (직각삼각형 사영정리)" },
      { lec: 127, label: "제127강 열기 (삼각형 내심과 반지름)" },
      { lec: 52, label: "제52강 열기 (아폴로니우스의 원)" }
    ]
  },
  {
    lec: 131,
    title: "숏츠식 판서 미리보기 · 직각삼각형 닮음 사영정리 4대 공식(h²=xy, a²=xc)과 소 공식",
    desc: "직각삼각형의 직각 꼭짓점에서 빗변에 수선의 발 $H$ 를 내리면 3개의 직각삼각형이 모두 닮음이 되어 $a^2=xc,\\ b^2=yc,\\ h^2=xy,\\ ab=ch$ 4대 공식이 성립합니다.",
    hookTitle: "직각 속의 직각 · 제곱은 가까운 것 × 전체, 높이는 좌 × 우!", hookSub: "a² = x·c · b² = y·c · h² = x·y · a·b = c·h (소 牛 공식)!",
    hookSay: "직각삼각형의 직각 꼭짓점에서 빗변에 수선을 내린 도형! 수능 미적분과 기하에서 숨 쉬듯 쓰이는 사영정리 사대 공식을 삼십 초 만에 완벽 암기합니다.",
    hookCap: "직각삼각형 사영정리 4대 공식 · 30초 정리",
    whySay: "동그라미 각과 엑스 각의 합을 구십도라 하면, 직각삼각형 안에 생기는 왼쪽 작은 삼각형과 오른쪽 작은 삼각형, 그리고 전체 큰 삼각형 세 개가 모두 에이에이 닮음이 됩니다.",
    whyCap: "$\\circ + \\times = 90^\\circ\\implies \\triangle ABC\\sim\\triangle DBA\\sim\\triangle DAC$ (3중 AA 닮음 비례식!)",
    histTag: "유클리드의 피타고라스 증명과 기하평균", histSay: "유클리드는 왼쪽 제곱 에이제곱은 엑스씨와 오른쪽 제곱 비제곱은 와이씨를 더하면 엑스 더하기 와이가 씨이므로 피타고라스 정리가 증명된다는 사실을 보였습니다.",
    histCap: "$a^2+b^2 = xc + yc = (x+y)c = c^2$ · 높이 $h=\\sqrt{xy}$ 는 기하평균!",
    fParts: [
      { say: "양옆 직각변의 제곱은 자기 쪽 가까운 밑변 조각 곱하기 빗변 전체 길이와 같습니다.", cap: "양옆 제곱 공식: $a^2 = x\\cdot c$ (왼쪽$^2=$ 가까운 것 $\\times$ 전체), $b^2 = y\\cdot c$ (오른쪽$^2$)" },
      { say: "가운데 수선의 높이 제곱은 왼쪽 밑변 조각 엑스와 오른쪽 밑변 조각 와이의 곱과 같습니다.", cap: "높이 제곱 공식(기하평균): $h^2 = x\\cdot y\\ \\Longleftrightarrow\\ h = \\sqrt{xy}$" },
      { say: "두 직각변 에이 곱하기 비는 밑변 씨 곱하기 높이 에이치와 같으며, 한자 소 우 모양을 닮아 소 공식이라 부릅니다.", cap: "넓이 불변 소(牛) 공식: $a\\cdot b = c\\cdot h$ ($\\because\\ \\dfrac{1}{2}ab = \\dfrac{1}{2}ch$)!" }
    ],
    fChips: [
      "a^2=x\\cdot c,\\quad b^2=y\\cdot c\\quad\\left(\\implies a^2:b^2=x:y\\right)",
      "h^2=x\\cdot y\\quad(\\text{높이 }h=\\sqrt{xy}\\text{ 는 }x,y\\text{ 의 기하평균})",
      "\\text{소(牛) 공식}:\\ a\\cdot b=c\\cdot h,\\quad \\dfrac{1}{h^2}=\\dfrac{1}{a^2}+\\dfrac{1}{b^2}"
    ],
    fLabels: ["a² = xc, b² = yc, h² = xy", "소 공식 a·b = c·h"],
    exParts: [
      { say: "예를 들어 각 에이가 구십도인 직각삼각형에서 빗변에 내린 수선의 발 에이치에 대하여 비에이치가 사, 씨에이치가 구일 때 높이 에이치와 변 에이비의 길이를 구해 봅시다.", cap: "빗변 조각이 $x=4,\\ y=9$ (전체 $c=13$)일 때 높이 $h$ 와 직각변 $a$ 구하기" },
      { say: "높이 제곱 공식에 의해 에이치 제곱은 사 곱하기 구인 삼십육이므로 높이 에이치는 육입니다.", cap: "$h^2 = x\\cdot y = 4\\times 9 = 36\\implies h = 6$" },
      { say: "왼쪽 직각변 제곱 공식에 의해 에이 제곱은 가까운 사 곱하기 전체 십삼인 오십이이므로 에이는 이 루트 십삼입니다.", cap: "$a^2 = x\\cdot c = 4\\times(4+9) = 52\\implies a = 2\\sqrt{13}$" }
    ],
    exChips: [
      "h^2=x\\cdot y=4\\times 9=36\\implies h=6",
      "a^2=x\\cdot c=4\\times(4+9)=52\\implies a=2\\sqrt{13}",
      "\\therefore\\ h=6,\\quad a=2\\sqrt{13},\\quad b=\\sqrt{9\\times 13}=3\\sqrt{13}"
    ],
    exLabels: ["h² = 4×9 = 36 ➔ h = 6", "a² = 4×13 = 52 ➔ a = 2√13"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 1.69 - (x - 1.5) * (x - 1.5))), GY0: 390, GV: 185, xr: [0.1, 2.9], area: [0.2, 2.8], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.9, col: CY, label: "x = 4" }, r2: { x: 2.3, col: GO, label: "y = 9 (h=6)" },
      fn: { t: "반원 위의 직각삼각형과 기하평균 높이 h = √(xy) = 6", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "h² = 4 × 9", finalS: "h = 6", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 두 직각변의 길이가 십오와 이십인 직각삼각형에서 직각 꼭짓점에서 빗변에 내린 수선의 발을 에이치라 할 때, 선분 비에이치와 씨에이치의 길이의 차를 구해 볼까요?", cap: "직각변이 $a=15,\\ b=20$ (빗변 $c=25$)일 때 $|x-y|=|BH-CH|$ 구하기 (자작 문항)" },
      { say: "빗변 씨가 이십오이므로 사영정리에 의해 십오의 제곱 이백이십오는 이십오 엑스가 되어 엑스는 구입니다.", cap: "$c=\\sqrt{15^2+20^2}=25,\\quad 15^2=25x\\implies x=\\dfrac{225}{25}=9$" },
      { say: "나머지 조각 와이는 이십오 빼기 구인 십육이므로 두 선분의 길이의 차는 십육 빼기 구인 칠입니다.", cap: "$y=25-9=16\\quad(\\text{또는 }20^2=25y)\\ \\therefore\\ |x-y|=16-9=7$" }
    ],
    examChips: [
      "c=\\sqrt{15^2+20^2}=25,\\quad a^2=xc\\implies 225=25x\\implies x=9",
      "b^2=yc\\implies 400=25y\\implies y=16\\quad(x:y=a^2:b^2=9:16)",
      "\\therefore\\ |x-y|=16-9=7\\quad\\left(\\text{높이 }h=\\dfrac{15\\times 20}{25}=12\\right)"
    ],
    examLabels: ["x : y = a² : b² = 9 : 16", "x=9, y=16 ➔ 차 = 7"],
    examGraph: {
      f: x => -0.55 * (x - 1.3) * (x - 1.3) + 1.55, GY0: 390, GV: 155, xr: [0.2, 2.8], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.9, col: CY, label: "x = 9" }, r2: { x: 2.2, col: PK, label: "y = 16" },
      fn: { t: "빗변 분할비 x : y = a² : b² = 15² : 20² = 9 : 16", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "x=9, y=16", finalS: "차 = 7", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 사영정리에서 빗변의 두 조각 엑스 대 와이의 비율은 양옆 직각변의 제곱의 비인 에이제곱 대 비제곱과 같다는 사실을 외워 두면 계산이 일초 만에 끝납니다.", cap: "① 빗변 조각 비율 공식: $x : y = a^2 : b^2$ ($3:4:5$ 직각삼각형이면 $x:y=9:16$!) " },
      { say: "둘째, 반원의 지름 위에 한 점을 찍고 수선을 올리면 그 높이가 바로 양쪽 조각의 기하평균 루트 엑스와이이므로 산술기하평균의 기하학적 증명이 됩니다.", cap: "② 산술·기하평균 도형: 반지름 $\\dfrac{x+y}{2}\\ge$ 수선 높이 $h=\\sqrt{xy}$!" },
      { say: "셋째, 원 밖의 점에서 접선을 그었을 때 중심과 연결한 직각삼각형에서 현의 절반을 구할 때가 사영정리가 가장 많이 쓰이는 순간입니다.", cap: "③ 원의 접선 결합: 중심 $O$, 밖의 점 $P$, 접점 $T$ 에서 $\\angle OTP=90^\\circ\\implies$ 사영정리 4대 공식 자동 발동!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 대각선이 직교하는 사각형의 피타고라스 공식과 히포크라테스의 초승달 넓이를 다루는 제백삼십이강입니다.", cap: "제132강 · 직교 대각선($a^2+c^2=b^2+d^2$)과 히포크라테스 원" },
      { tag: "연계 ②", say: "산술·기하평균과 코시-슈바르츠 부등식을 다루는 제오십구강도 함께 복습해 보세요.", cap: "제59강 · 산술·기하평균과 코시-슈바르츠 부등식 (공통수학 2)" },
      { tag: "이 사이트", say: "이 사이트의 제백삼십이강과 제오십구강을 이어서 보세요.", cap: "제132강 · 직교 대각선과 피타고라스  /  제59강 · 산술·기하평균" }
    ],
    nextLinks: [
      { lec: 132, label: "제132강 열기 (직교 대각선 공식)" },
      { lec: 59, label: "제59강 열기 (산술·기하평균 도형)" },
      { lec: 125, label: "제125강 열기 (접선 직각삼각형)" }
    ]
  },
  {
    lec: 132,
    title: "숏츠식 판서 미리보기 · 피타고라스 직교 대각선(a²+c²=b²+d²)과 히포크라테스 원",
    desc: "사각형의 두 대각선이 직교하면 마주 보는 두 변의 제곱의 합이 같고($a^2+c^2=b^2+d^2$), 직각삼각형 세 변을 지름으로 하는 히포크라테스 초승달 넓이는 삼각형 넓이와 같습니다.",
    hookTitle: "대각선이 직교하면 마주 보는 변의 제곱의 합이 같다!", hookSub: "a² + c² = b² + d² · 히포크라테스 초승달 넓이 = 직각삼각형 넓이!",
    hookSay: "사각형의 두 대각선이 수직으로 만날 때 성립하는 피타고라스 마주 보는 변 공식과 직각삼각형 위의 반원 넓이 공식을 삼십 초 만에 정리합니다.",
    hookCap: "직교 대각선 & 히포크라테스 원 · 30초 정리",
    whySay: "두 대각선이 수직으로 만나는 교점을 기준으로 네 조각의 길이를 피, 큐, 알, 에스라 하면, 마주 보는 변의 제곱의 합이 둘 다 피제곱 더하기 큐제곱 더하기 알제곱 더하기 에스제곱으로 똑같아집니다.",
    whyCap: "$a^2+c^2 = (p^2+q^2)+(r^2+s^2) = (q^2+r^2)+(p^2+s^2) = b^2+d^2$!",
    histTag: "히포크라테스의 초승달 구적법", histSay: "고대 그리스의 히포크라테스는 곡선으로 둘러싸인 두 초승달 모양의 넓이의 합이 유리수 직각삼각형의 넓이와 정확히 같음을 증명하여 인류 최초의 곡선 구적에 성공했습니다.",
    histCap: "히포크라테스 정리: 두 직각변 위 반원 $S_1+S_2=$ 빗변 반원 $S_3\\implies$ 초승달 합 $=S_{\\triangle ABC}$!",
    fParts: [
      { say: "두 대각선이 직교하는 사각형에서는 항상 마주 보는 대변의 제곱의 합 에이제곱 더하기 씨제곱과 비제곱 더하기 디제곱이 같습니다.", cap: "직교 대각선 정리: $AC\\perp BD\\ \\Longleftrightarrow\\ AB^2 + CD^2 = BC^2 + DA^2$" },
      { say: "직사각형 내부의 임의의 점 피에서 네 꼭짓점까지 이은 선분에서도 마주 보는 꼭짓점까지의 거리 제곱의 합이 서로 같습니다.", cap: "영국 국기 정리(직사각형 내부 점 $P$): $PA^2 + PC^2 = PB^2 + PD^2$" },
      { say: "직각삼각형의 세 변을 지름으로 하는 세 반원에서 양쪽 두 반원의 넓이 합은 빗변 반원의 넓이와 같고, 색칠된 두 초승달의 넓이 합은 직각삼각형의 넓이와 같습니다.", cap: "히포크라테스의 원: $S_1+S_2=S_3$ 이고, 두 초승달 넓이 합 $= S_{\\triangle ABC} = \\dfrac{1}{2}ab$!" }
    ],
    fChips: [
      "\\overline{AC}\\perp\\overline{BD}\\iff a^2+c^2=b^2+d^2\\quad(\\text{마주 보는 변의 제곱 합 일치})",
      "\\text{직사각형 내부·외부 점 }P:\\ \\overline{PA}^2+\\overline{PC}^2=\\overline{PB}^2+\\overline{PD}^2",
      "\\text{히포크라테스 초승달 넓이 합}=S_{\\triangle ABC}=\\dfrac{1}{2}ab"
    ],
    fLabels: ["직교 대각선: a²+c² = b²+d²", "초승달 넓이 = ½ ab"],
    exParts: [
      { say: "예를 들어 두 대각선이 수직으로 만나는 사각형 에이비씨디에서 에이비가 삼, 비씨가 오, 씨디가 사일 때 나머지 한 변 디에이의 길이를 구해 봅시다.", cap: "$AC\\perp BD$ 인 사각형에서 $AB=3,\\ BC=5,\\ CD=4$ 일 때 $DA=x$ 구하기" },
      { say: "마주 보는 변의 제곱의 합이 같으므로 삼의 제곱 더하기 사의 제곱은 오의 제곱 더하기 엑스 제곱이 어서 아니, 마주 보는 변을 정확히 짝지어 봅시다.", cap: "마주 보는 대변 짝짓기: $AB(3)$ 와 $CD(4)$ 가 마주 보고, $BC(5)$ 와 $DA(x)$ 가 마주 봄!" },
      { say: "만약 에이비가 사, 비씨가 삼, 씨디가 유이라면 사의 제곱 더하기 유의 제곱 오십이는 삼의 제곱 더하기 엑스 제곱이므로 엑스는 루트 사십삼입니다.", cap: "$AB=4,\\ BC=3,\\ CD=6$ 이면 $4^2+6^2=3^2+x^2\\implies 52=9+x^2\\implies x=\\sqrt{43}$" }
    ],
    exChips: [
      "\\overline{AB}=4,\\ \\overline{BC}=3,\\ \\overline{CD}=6,\\ \\overline{DA}=x\\quad(\\overline{AC}\\perp\\overline{BD})",
      "\\overline{AB}^2+\\overline{CD}^2=\\overline{BC}^2+\\overline{DA}^2\\implies 4^2+6^2=3^2+x^2",
      "\\therefore\\ x^2=16+36-9=43\\implies x=\\sqrt{43}"
    ],
    exLabels: ["4² + 6² = 3² + x²", "x² = 43 ➔ x = √43"],
    exGraph: {
      f: x => -0.55 * (x - 1.5) * (x - 1.5) + 1.55, GY0: 390, GV: 155, xr: [0.2, 2.8], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "a²+c² = 52" }, r2: { x: 2.4, col: GO, label: "b²+x² = 52" },
      fn: { t: "직교 대각선 사각형: 마주 보는 대변 제곱의 합 불변 (a²+c² = b²+d²)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "52 − 9 = 43", finalS: "DA = √43", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 두 직각변의 길이가 육과 팔인 직각삼각형의 세 변을 각각 지름으로 하는 반원을 그릴 때, 작은 두 반원에서 큰 반원과 겹치는 부분을 뺀 색칠된 초승달 모양의 넓이를 구해 볼까요?", cap: "직각변이 $6,8$ 인 직각삼각형의 히포크라테스 초승달 넓이 구하기 (자작 문항)" },
      { say: "원주율 파이를 전혀 계산할 필요가 없습니다. 히포크라테스의 정리에 의해 색칠된 두 초승달의 넓이의 합은 가운데 직각삼각형의 넓이와 정확히 같습니다.", cap: "초승달 넓이 $= (S_{\\text{반원 }a}+S_{\\text{반원 }b}+S_{\\triangle}) - S_{\\text{반원 }c} = S_{\\triangle ABC}$ (파이 소거!)" },
      { say: "따라서 넓이는 이분의 일 곱하기 육 곱하기 팔인 이십사입니다.", cap: "$S_{\\text{초승달}} = \\dfrac{1}{2}\\times 6\\times 8 = 24$ ($\\pi$ 가 전혀 없는 유리수 정답!)" }
    ],
    examChips: [
      "S_{\\text{반원 }a}+S_{\\text{반원 }b}=\\dfrac{\\pi}{8}(6^2+8^2)=\\dfrac{\\pi}{8}(10^2)=S_{\\text{반원 }c}",
      "S_{\\text{초승달}}=(S_{\\text{반원 }a}+S_{\\text{반원 }b}+S_{\\triangle ABC})-S_{\\text{반원 }c}=S_{\\triangle ABC}",
      "\\therefore\\ S_{\\text{초승달}}=\\dfrac{1}{2}\\times 6\\times 8=24"
    ],
    examLabels: ["반원 넓이 S₁+S₂ = S₃ 소거", "초승달 넓이 = ½×6×8 = 24"],
    examGraph: {
      f: x => Math.sqrt(Math.max(0, 1.8 - (x - 1.5) * (x - 1.5))), GY0: 390, GV: 185, xr: [0.1, 2.9], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "초승달 L₁" }, r2: { x: 2.5, col: PK, label: "초승달 L₂" },
      fn: { t: "히포크라테스 초승달 L₁ + L₂ = 직각삼각형 넓이 ½ab = 24", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "π 완전 소거!", finalS: "넓이 = 24", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 사각형의 넓이는 두 대각선의 길이 피, 큐와 끼인각 세타에 대하여 이분의 일 피큐 사인 세타이며, 대각선이 직교하면 이분의 일 피큐가 됩니다.", cap: "① 직교 대각선 사각형 넓이: 마름모·연 모양처럼 $AC\\perp BD$ 이면 $S = \\dfrac{1}{2}\\,\\overline{AC}\\cdot\\overline{BD}$!" },
      { say: "둘째, 피타고라스 정리는 반원뿐만 아니라 직각삼각형의 세 변 위에 어떤 닮은 도형을 그려도 왼쪽 넓이 더하기 오른쪽 넓이는 빗변 도형 넓이와 같습니다.", cap: "② 피타고라스 일반화: 세 변을 한 변으로 하는 정삼각형·정사각형·반원 모두 $S_a + S_b = S_c$!" },
      { say: "셋째, 꼭짓점 씨에서 밑변 에이비에 수선을 내렸을 때도 양옆 변 제곱의 차는 밑변 두 조각 제곱의 차와 같다는 성질로 높이를 구할 수 있습니다.", cap: "③ 수선의 발 피타고라스 차 공식: $AH\\perp BC$ 이면 $AB^2 - AC^2 = BH^2 - CH^2$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 평행선 닮음비와 넓이비, 부피비, 그리고 미적분 무한등비급수 도형의 공비를 삼초 만에 구하는 제백삼십삼강입니다.", cap: "제133강 · 평행선 닮음비($m:n$)·넓이비($m^2:n^2$)와 등비급수 도형 공비" },
      { tag: "연계 ②", say: "직각삼각형 사영정리 사대 공식을 다루는 제백삼십일강도 함께 복습해 보세요.", cap: "제131강 · 직각삼각형 닮음 사영정리 4대 공식" },
      { tag: "이 사이트", say: "이 사이트의 제백삼십삼강과 제백삼십일강을 이어서 보세요.", cap: "제133강 · 닮음비·넓이비와 등비급수  /  제131강 · 직각삼각형 사영정리" }
    ],
    nextLinks: [
      { lec: 133, label: "제133강 열기 (닮음·넓이비와 등비급수)" },
      { lec: 131, label: "제131강 열기 (직각삼각형 사영정리)" },
      { lec: 77, label: "제77강 열기 (등비급수 도형 킬러)" }
    ]
  },
  {
    lec: 133,
    title: "숏츠식 판서 미리보기 · 평행선 닮음비(m:n)·넓이비(m²:n²)와 등비급수 도형 공비",
    desc: "닮음비가 $1:k$ 이면 넓이비는 $1:k^2$, 부피비는 $1:k^3$ 입니다. 사다리꼴 대각선 모래시계 넓이비($m^2:mn:mn:n^2$)와 나비 공식($\\frac{1}{c}=\\frac{1}{a}+\\frac{1}{b}$)을 정리합니다.",
    hookTitle: "길이비가 1:k 이면 넓이비는 무조건 1:k² (등비급수 공비 R = k²)!", hookSub: "사다리꼴 4조각 넓이비는 m² : mn : mn : n²!",
    hookSay: "미적분 등비급수 도형 문제의 공비를 구하는 핵심 열쇠인 닮음비와 넓이비, 그리고 사다리꼴 모래시계 공식을 삼십 초 만에 마스터합니다.",
    hookCap: "닮음비·넓이비 & 모래시계 · 30초 정리",
    whySay: "두 평행선 사이에서 엇각과 맞꼭지각이 같으므로 모래시계 모양의 두 삼각형은 에이에이 닮음이 되고, 모든 대응하는 길이의 비가 에이 대 비로 일정해집니다.",
    whyCap: "평행선 엇각 일치 $\\implies$ 모래시계 $\\triangle PAB\\sim\\triangle PCD$ (길이비 $m:n\\implies$ 넓이비 $m^2:n^2$!)",
    histTag: "탈레스의 피라미드 측량과 프랙탈 자기유사성", histSay: "탈레스는 막대기의 그림자 길이 비로 거대한 피라미드의 높이를 쟀고, 현대 기하학에서는 이 닮음 축소 비율의 제곱으로 무한 프랙탈 도형의 넓이 합을 계산합니다.",
    histCap: "첫째 도형 넓이 $S_1$, 외곽 틀 길이 닮음비 $1:k\\implies$ 넓이 공비 $R=k^2\\implies S=\\dfrac{S_1}{1-k^2}$!",
    fParts: [
      { say: "닮음비가 엠 대 엔인 두 평면도형의 둘레의 길이 비는 엠 대 엔이고, 넓이의 비는 제곱인 엠제곱 대 엔제곱, 입체도형의 부피의 비는 세제곱인 엠세제곱 대 엔세제곱입니다.", cap: "차원별 비율 법칙: 길이비 $m:n\\implies$ 넓이비 $m^2:n^2\\implies$ 부피비 $m^3:n^3$!" },
      { say: "윗변과 아랫변의 비가 엠 대 엔인 사다리꼴에서 두 대각선을 그으면 위, 양옆 날개 두 개, 아래 네 삼각형의 넓이 비는 엠제곱 대 엠엔 대 엠엔 대 엔제곱이 됩니다.", cap: "사다리꼴 4분할 넓이 공식: 위($m^2$) : 왼쪽 날개($mn$) : 오른쪽 날개($mn$) : 아래($n^2$)!" },
      { say: "양쪽 기둥의 높이가 에이와 비일 때 교차하는 선분의 교점 높이 씨는 역수의 합이 같다는 조화평균 공식으로 일초 만에 구합니다.", cap: "평행선 교차 나비 공식: $\\dfrac{1}{c} = \\dfrac{1}{a} + \\dfrac{1}{b}\\ \\Longleftrightarrow\\ c = \\dfrac{ab}{a+b}$!" }
    ],
    fChips: [
      "\\text{닮음비 }1:k\\implies \\text{넓이 공비 }R=k^2\\implies \\sum_{n=1}^{\\infty}S_n=\\dfrac{S_1}{1-k^2}",
      "\\text{사다리꼴 대각선 4조각 넓이비}=m^2 : mn : mn : n^2",
      "\\text{평행 기둥 교점 높이}:\\ \\dfrac{1}{c}=\\dfrac{1}{a}+\\dfrac{1}{b}\\iff c=\\dfrac{ab}{a+b}"
    ],
    fLabels: ["길이비 k ➔ 넓이 공비 k²", "사다리꼴 m² : mn : mn : n²"],
    exParts: [
      { say: "예를 들어 에이디와 비씨가 평행하고 길이의 비가 이 대 삼인 사다리꼴 에이비씨디에서 두 대각선의 교점을 오라 할 때, 삼각형 오에이디가 사라면 사다리꼴 전체 넓이를 구해 봅시다.", cap: "$AD\\parallel BC$ 이고 $AD:BC=2:3$ 인 사다리꼴에서 $S_{\\triangle OAD}=4$ 일 때 전체 넓이 구하기" },
      { say: "닮음비가 이 대 삼이므로 위, 양옆 날개, 아래 조각의 넓이 비는 사 대 유 대 유 대 구입니다.", cap: "$m:n=2:3\\implies$ 4조각 넓이비 $= 2^2 : (2\\cdot 3) : (2\\cdot 3) : 3^2 = 4 : 6 : 6 : 9$" },
      { say: "위쪽 넓이가 사와 정확히 같으므로 네 조각을 모두 더한 사다리꼴 전체의 넓이는 사 더하기 유 더하기 유 더하기 구인 이십오입니다.", cap: "$S_{\\text{전체}} = 4 + 6 + 6 + 9 = (2+3)^2 = 25$" }
    ],
    exChips: [
      "\\overline{AD}:\\overline{BC}=2:3\\implies 4\\text{조각 넓이비}=4:6:6:9",
      "S_{\\triangle OAD}=4\\implies S_{\\triangle OAB}=S_{\\triangle OCD}=6,\\quad S_{\\triangle OBC}=9",
      "\\therefore\\ S_{ABCD}=4+6+6+9=(2+3)^2=25"
    ],
    exLabels: ["넓이비 4 : 6 : 6 : 9", "전체 넓이 = (2+3)² = 25"],
    exGraph: {
      f: x => 0.35 * (x - 1.5) * (x - 1.5) + 0.55, GY0: 390, GV: 140, xr: [0.2, 2.8], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "위 m² = 4" }, r2: { x: 2.4, col: GO, label: "아래 n² = 9" },
      fn: { t: "사다리꼴 대각선 4조각 넓이 합 = m² + 2mn + n² = (m+n)² = 25", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "4+6+6+9", finalS: "전체 = 25", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 밑변이 유이고 높이가 사인 이등변삼각형에 내접하는 정사각형을 한없이 그릴 때, 첫 번째 정사각형의 한 변의 길이와 넓이 등비급수의 공비를 구해 볼까요?", cap: "밑변 $6$, 높이 $4$ 인 삼각형에 내접하는 정사각형의 한 변 $x$ 와 넓이 공비 $R$ (자작 문항)" },
      { say: "정사각형의 한 변을 엑스라 하면 위쪽 작은 삼각형과 전체 삼각형의 닮음식에 의해 사 빼기 엑스 대 사는 엑스 대 유이 되어 엑스는 오분의 십이입니다.", cap: "평행선 닮음: $\\dfrac{4-x}{4}=\\dfrac{x}{6}\\implies 24-6x=4x\\implies x=\\dfrac{12}{5}$ (공식 $\\dfrac{ah}{a+h}$!)" },
      { say: "높이가 사에서 사 빼기 오분의 십이인 오분의 팔로 줄어들므로 길이 닮음비는 오분의 이이고, 따라서 넓이 공비는 제곱인 이십오분의 사입니다.", cap: "길이비 $k=\\dfrac{4-x}{4}=\\dfrac{2}{5}\\implies$ 넓이 공비 $R=k^2=\\left(\\dfrac{2}{5}\\right)^2=\\dfrac{4}{25}$" }
    ],
    examChips: [
      "\\text{내접 정사각형 한 변}:\\ x=\\dfrac{6\\times 4}{6+4}=\\dfrac{24}{10}=\\dfrac{12}{5}",
      "\\text{높이 축소비(길이비)}:\\ k=\\dfrac{4-12/5}{4}=\\dfrac{8/5}{4}=\\dfrac{2}{5}",
      "\\therefore\\ \\text{넓이 등비급수 공비 }R=k^2=\\left(\\dfrac{2}{5}\\right)^2=\\dfrac{4}{25}"
    ],
    examLabels: ["정사각형 한 변 x = ah/(a+h)", "길이비 2/5 ➔ 넓이 공비 4/25"],
    examGraph: {
      f: x => 1.6 * Math.exp(-0.7 * x), GY0: 390, GV: 175, xr: [0.1, 2.8], area: [0.2, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "x = 12/5" }, r2: { x: 1.8, col: PK, label: "k = 2/5" },
      fn: { t: "삼각형 내접 정사각형 한 변 x = ah/(a+h) 와 넓이 공비 k²", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "k = 2/5", finalS: "R = 4/25", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 밑변이 에이이고 높이가 에이치인 어떤 삼각형이든 그 안에 내접하는 정사각형의 한 변의 길이는 항상 에이 더하기 에이치 분의 에이에이치입니다.", cap: "① 내접 정사각형 1초 공식: 밑변 $a$, 높이 $h$ 삼각형의 내접 정사각형 한 변 $x = \\dfrac{ah}{a+h}$!" },
      { say: "둘째, 사다리꼴에서 위쪽 삼각형 넓이가 피이고 아래쪽 삼각형 넓이가 큐이면 사다리꼴 전체 넓이는 루트 피 더하기 루트 큐의 전체 제곱입니다.", cap: "② 사다리꼴 넓이 완전제곱 공식: $S_{\\text{전체}} = (\\sqrt{S_{\\text{위}}} + \\sqrt{S_{\\text{아래}}})^2$!" },
      { say: "셋째, 등비급수에서 도형이 두 개씩 갈라지는 프랙탈이면 넓이 공비 케이제곱에 개수 이까지 곱한 이 케이제곱이 최종 공비가 됩니다.", cap: "③ 프랙탈 개수 공비: 도형이 매 단계 $N$개씩 분열하면 공비 $R = N\\cdot k^2$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 외접하거나 내접하는 두 원의 중심거리와 공통외접선의 길이를 다루는 제백삼십사강입니다.", cap: "제134강 · 두 원의 외접·내접 중심거리와 공통외접선 길이 $2\\sqrt{Rr}$" },
      { tag: "연계 ②", say: "무한등비급수와 도형 프랙탈 넓이 극한을 다루는 제칠십칠강도 함께 복습해 보세요.", cap: "제77강 · 무한등비급수 수렴 조건과 도형 프랙탈 극한 (미적분)" },
      { tag: "이 사이트", say: "이 사이트의 제백삼십사강과 제칠십칠강을 이어서 보세요.", cap: "제134강 · 두 원의 접선과 중심거리  /  제77강 · 등비급수 도형 극한" }
    ],
    nextLinks: [
      { lec: 134, label: "제134강 열기 (두 원의 공통접선)" },
      { lec: 77, label: "제77강 열기 (등비급수 도형 킬러)" },
      { lec: 131, label: "제131강 열기 (직각삼각형 사영정리)" }
    ]
  },
  {
    lec: 134,
    title: "숏츠식 판서 미리보기 · 두 원의 외접·내접 중심거리와 공통외접선 길이 2√(Rr)",
    desc: "두 원이 외접하면 중심거리는 $R+r$, 내접하면 $R-r$ 입니다. 외접하는 두 원의 공통외접선 길이는 직사각형 평행이동 보조선에 의해 $l=2\\sqrt{Rr}$ 로 즉시 구해집니다.",
    hookTitle: "외접하는 두 원이 보이면 중심끼리 이어라 ➔ 빗변 R+r, 밑변 R−r!", hookSub: "공통외접선의 길이는 기하평균의 2배 ➔ l = 2√(R·r)!",
    hookSay: "원 두 개가 서로 접하고 직선에도 접하는 고난도 도형 문제! 보조선 세 개로 직각삼각형을 만들어 일초 만에 푸는 공식을 바로 정리합니다.",
    hookCap: "두 원의 외접·공통접선 · 30초 정리",
    whySay: "두 원의 중심을 이은 빗변 알 플러스 스몰 알과, 작은 원의 중심에서 큰 원의 반지름에 수선을 내려 만든 직각삼각형에서 피타고라스 정리를 쓰면 접선의 길이가 이 루트 알알로 바로 유도됩니다.",
    whyCap: "$l = \\sqrt{(R+r)^2 - (R-r)^2} = \\sqrt{4Rr} = 2\\sqrt{Rr}$ (기하평균의 2배!)",
    histTag: "데카르트의 원 정리와 포드 원(Ford Circles)", histSay: "수평선에 접하면서 서로 외접하는 원들의 반지름 관계는 데카르트의 사원 정리와 정수론의 포드 원으로 발전하여 현대 기하학의 아름다운 정리가 되었습니다.",
    histCap: "세 원이 서로 외접하고 직선에 접할 때: $\\dfrac{1}{\\sqrt{r_3}} = \\dfrac{1}{\\sqrt{r_1}} + \\dfrac{1}{\\sqrt{r_2}}$!",
    fParts: [
      { say: "두 원이 서로 접할 때는 무조건 두 중심 오원, 오투를 잇는 선분을 그으세요. 외접하면 중심거리는 반지름의 합이고 내접하면 반지름의 차입니다.", cap: "중심선 보조선 철칙: 외접 $\\iff d = R + r$ · 내접 $\\iff d = |R - r|$ (접점은 항상 중심선 위!)" },
      { say: "외접하는 두 원의 공통외접선의 길이 엘은 직각삼각형의 빗변 알 더하기 알과 높이 알 빼기 알에 의해 언제나 이 루트 알 곱하기 알입니다.", cap: "외접 두 원의 공통외접선 공식: $l = \\sqrt{(R+r)^2-(R-r)^2} = 2\\sqrt{Rr}$!" },
      { say: "일반적인 중심거리 디가 주어졌을 때 공통외접선은 디제곱 빼기 반지름 차의 제곱에 루트를 씌우고, 공통내접선은 반지름 합의 제곱을 뺍니다.", cap: "일반 공통접선: 외접선 $l_{\\text{외}}=\\sqrt{d^2-(R-r)^2}$ · 내접선 $l_{\\text{내}}=\\sqrt{d^2-(R+r)^2}$" }
    ],
    fChips: [
      "\\text{외접 중심거리 }d=R+r,\\quad \\text{내접 중심거리 }d=|R-r|",
      "\\text{외접 두 원의 공통외접선 길이}:\\ l=\\sqrt{(R+r)^2-(R-r)^2}=2\\sqrt{Rr}",
      "\\text{일반 중심거리 }d:\\ l_{\\text{외}}=\\sqrt{d^2-(R-r)^2},\\quad l_{\\text{내}}=\\sqrt{d^2-(R+r)^2}"
    ],
    fLabels: ["빗변 R+r, 높이 R−r", "공통외접선 l = 2√(Rr)"],
    exParts: [
      { say: "예를 들어 반지름이 구인 큰 원과 반지름이 사인 작은 원이 서로 외접하면서 동시에 직선 엘에 접할 때, 두 접점 에이와 비 사이의 거리를 구해 봅시다.", cap: "반지름 $R=9,\\ r=4$ 인 두 원이 서로 외접할 때 공통외접선의 길이 $AB$ 구하기" },
      { say: "두 중심을 이은 빗변은 구 더하기 사인 십삼이고, 반지름의 차는 구 빼기 사인 오입니다.", cap: "빗변 $d=9+4=13$, 높이 $R-r=9-4=5$ ($5:12:13$ 직각삼각형!)" },
      { say: "공통외접선 공식 이 루트 구 곱하기 사에 대입해도 즉시 이 곱하기 유인 십이가 나옵니다.", cap: "$\\overline{AB} = 2\\sqrt{Rr} = 2\\sqrt{9\\times 4} = 12$ (또는 $\\sqrt{13^2-5^2}=12$)" }
    ],
    exChips: [
      "R=9,\\ r=4\\implies \\text{중심거리 }d=9+4=13,\\quad R-r=5",
      "\\overline{AB}=2\\sqrt{Rr}=2\\sqrt{9\\times 4}=2\\times 6=12",
      "\\therefore\\ \\text{공통외접선의 길이 }\\overline{AB}=12"
    ],
    exLabels: ["5 : 12 : 13 직각삼각형", "l = 2√(9×4) = 12"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 1.6 - (x - 1.0) * (x - 1.0))) + 0.25, GY0: 390, GV: 165, xr: [0.1, 2.9], area: [0.3, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.0, col: CY, label: "큰 원 R = 9" }, r2: { x: 2.3, col: GO, label: "작은 원 r = 4" },
      fn: { t: "외접하는 두 원의 공통외접선 길이 AB = 2√(Rr) = 12", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "2√(9 × 4)", finalS: "AB = 12", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 방금 본 반지름이 구인 원과 사인 원, 그리고 직선 엘 사이의 틈새에 동시에 외접하는 세 번째 작은 원의 반지름 엑스를 구해 볼까요?", cap: "$R=9,\\ r=4$ 와 직선에 동시에 접하는 틈새 원의 반지름 $x$ 구하기 (자작 문항)" },
      { say: "큰 원과 틈새 원 사이의 가로 거리는 이 루트 구엑스이고, 작은 원과 틈새 원 사이의 가로 거리는 이 루트 사엑스입니다.", cap: "공통외접선 분할: $l = 2\\sqrt{9x} + 2\\sqrt{4x} = 2\\sqrt{9\\times 4}$" },
      { say: "이 두 길이의 합이 전체 십이와 같으므로 삼 루트 엑스 더하기 이 루트 엑스는 유이 되어 반지름 엑스는 이십오분의 삼십육입니다.", cap: "$(3+2)\\sqrt{x}=6\\implies \\sqrt{x}=\\dfrac{6}{5}\\implies x=\\dfrac{36}{25}$" }
    ],
    examChips: [
      "2\\sqrt{Rx}+2\\sqrt{rx}=2\\sqrt{Rr}\\iff \\dfrac{1}{\\sqrt{x}}=\\dfrac{1}{\\sqrt{R}}+\\dfrac{1}{\\sqrt{r}}",
      "\\dfrac{1}{\\sqrt{x}}=\\dfrac{1}{3}+\\dfrac{1}{2}=\\dfrac{5}{6}\\implies \\sqrt{x}=\\dfrac{6}{5}",
      "\\therefore\\ x=\\left(\\dfrac{6}{5}\\right)^2=\\dfrac{36}{25}"
    ],
    examLabels: ["2√(9x) + 2√(4x) = 12", "1/√x = 1/3 + 1/2 ➔ x = 36/25"],
    examGraph: {
      f: x => 0.45 * (x - 1.6) * (x - 1.6) + 0.35, GY0: 390, GV: 140, xr: [0.2, 2.8], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "2√(9x) = 6√x" }, r2: { x: 2.3, col: PK, label: "2√(4x) = 4√x" },
      fn: { t: "데카르트 접원 공식: 2√(Rx) + 2√(rx) = 2√(Rr)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "5√x = 6", finalS: "x = 36/25", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 두 원이 접하는 문제가 나오면 무조건 중심과 중심, 그리고 접점을 한 직선으로 잇는 보조선부터 그으세요.", cap: "① 원과 원의 접점 제1보조선: 두 중심 $O_1,O_2$ 와 접점 $T$ 는 언제나 한 직선 위에 있다!" },
      { say: "둘째, 작은 원의 중심에서 큰 원의 반지름에 수선을 내려 직사각형과 직각삼각형으로 쪼개는 것이 모든 공통접선 문제의 표준 해법입니다.", cap: "② 직사각형 평행이동 보조선: 공통접선을 평행이동하여 빗변 $d$, 한 변 $R\\mp r$ 직각삼각형 작도!" },
      { say: "셋째, 부채꼴 안에 원이 내접할 때도 부채꼴의 중심과 내접원의 중심을 이으면 거리가 라지 알 빼기 스몰 알이 됩니다.", cap: "③ 부채꼴 내접원 핵심 식: 중심거리 $OO' = R - r$ 이고 중심각 이등분선($\\theta/2$)에서 $\\sin(\\theta/2)=\\dfrac{r}{R-r}$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 중학 도형 마스터의 대단원인 원에 내접하는 사각형의 코사인법칙과 톨레미 정리를 다루는 제백삼십오강입니다.", cap: "제135강 · 원 내접 사각형 코사인법칙과 톨레미 정리($ac+bd=pq$)" },
      { tag: "연계 ②", say: "원 밖의 점에서 그은 접선과 접현각 정리를 다루는 제백이십오강도 함께 복습해 보세요.", cap: "제125강 · 원의 접선 길이($PA=PB$)와 접현각 정리" },
      { tag: "이 사이트", say: "이 사이트의 제백삼십오강과 제백이십오강을 이어서 보세요.", cap: "제135강 · 내접사각형과 톨레미 정리  /  제125강 · 접선과 접현각" }
    ],
    nextLinks: [
      { lec: 135, label: "제135강 열기 (내접사각형과 톨레미)" },
      { lec: 125, label: "제125강 열기 (접선과 접현각)" },
      { lec: 54, label: "제54강 열기 (원의 방정식과 접선)" }
    ]
  },
  {
    lec: 135,
    title: "숏츠식 판서 미리보기 · 원 내접 사각형 코사인법칙 대각선과 톨레미 정리(ac+bd=pq)",
    desc: "원에 내접하는 사각형은 마주 보는 각의 합이 $\\pi$ 이므로 $\\cos(\\pi-\\theta)=-\\cos\\theta$ 로 대각선을 구하며, 마주 보는 변의 곱의 합은 두 대각선의 곱과 같습니다($ac+bd=pq$).",
    hookTitle: "내접사각형 킬러 · 마주 보는 변의 곱의 합 = 두 대각선의 곱!", hookSub: "cos(π−θ) = −cos θ 연립 + 톨레미 정리 a·c + b·d = p·q!",
    hookSay: "중학 도형 마스터의 마지막 열두 번째 시간! 수능 삼각함수 도형 사점 문항의 최강 무기인 내접사각형 코사인 연립과 톨레미 정리를 삼십 초 만에 완성합니다.",
    hookCap: "내접사각형 & 톨레미 정리 · 30초 정리",
    whySay: "원에 내접하는 사각형은 마주 보는 두 각의 합이 파이이므로 한쪽 코사인이 코사인 세타이면 맞은편 코사인은 마이너스 코사인 세타가 되어, 공통 대각선의 제곱을 두 번 표현해 연립할 수 있습니다.",
    whyCap: "$\\angle A+\\angle C=\\pi\\implies \\cos C=-\\cos A\\implies BD^2$ 을 $\\triangle ABD$ 와 $\\triangle CBD$ 두 방식으로 연립!",
    histTag: "클라우디오스 프톨레마이오스의 알마게스트", histSay: "고대 천문학자 프톨레마이오스는 천체 관측을 위한 삼각함수 현의 표를 만들면서 원에 내접하는 사각형의 두 대각선의 곱이 마주 보는 대변의 곱의 합과 같다는 톨레미 정리를 증명했습니다.",
    histCap: "톨레미(Ptolemy) 정리: 원 내접 사각형 $ABCD$ 에서 $AB\\cdot CD + BC\\cdot DA = AC\\cdot BD$!",
    fParts: [
      { say: "원에 내접하는 사각형의 네 변이 주어지면 대각선 비디의 제곱을 삼각형 에이비디와 씨비디에서 각각 코사인법칙으로 세워 코사인 세타와 대각선을 동시에 구합니다.", cap: "코사인 연립 공식: $a^2+d^2-2ad\\cos A = b^2+c^2+2bc\\cos A$ ($\\because\\ \\cos(\\pi-A)=-\\cos A$!)" },
      { say: "내접사각형의 마주 보는 두 쌍의 대변의 곱을 더한 에이씨 더하기 비디는 두 대각선의 곱 피큐와 언제나 정확히 같습니다.", cap: "톨레미 정리: $a\\cdot c + b\\cdot d = p\\cdot q$ (대각선 길이를 3초 만에 검산·도출하는 필살기!)" },
      { say: "특히 원에 내접하는 정삼각형 에이비씨와 호 위의 점 피를 연결하면 가장 긴 선분 피에이는 짧은 두 선분 피비 더하기 피씨와 항상 같습니다.", cap: "정삼각형 톨레미 따름정리: $a\\cdot PA = a\\cdot PB + a\\cdot PC\\ \\Longleftrightarrow\\ PA = PB + PC$!" }
    ],
    fChips: [
      "\\angle A+\\angle C=\\pi\\implies \\cos C=-\\cos A,\\quad \\sin C=\\sin A",
      "\\text{톨레미 정리}:\\ \\overline{AB}\\cdot\\overline{CD}+\\overline{BC}\\cdot\\overline{DA}=\\overline{AC}\\cdot\\overline{BD}",
      "\\text{정삼각형 }\\triangle ABC\\text{ 내접원 위의 점 }P:\\ \\overline{PA}=\\overline{PB}+\\overline{PC}"
    ],
    fLabels: ["cos(π−θ) = −cos θ 연립", "톨레미: ac + bd = pq"],
    exParts: [
      { say: "예를 들어 한 원에 내접하는 정삼각형 에이비씨의 짧은 호 비씨 위의 점 피에 대하여 피비가 삼이고 피씨가 오일 때, 선분 피에이의 길이와 삼각형 피비씨의 넓이를 구해 봅시다.", cap: "정삼각형 외접원 위의 점 $P$ 에서 $PB=3,\\ PC=5$ 일 때 $PA$ 와 $S_{\\triangle PBC}$ 구하기" },
      { say: "정삼각형의 세 변의 길이가 모두 에이로 같으므로 톨레미 정리를 쓰면 에이 약분 후 피에이는 삼 더하기 오인 팔이 일초 만에 나옵니다.", cap: "톨레미 정리: $a\\cdot PA = a\\cdot PB + a\\cdot PC\\implies PA = 3 + 5 = 8$" },
      { say: "또한 마주 보는 각 비피씨는 백팔십도 빼기 육십도인 백이십도이므로 삼각형 피비씨의 넓이는 사분의 십오 루트 삼입니다.", cap: "$\\angle BPC=180^\\circ-60^\\circ=120^\\circ\\implies S_{\\triangle PBC}=\\dfrac{1}{2}\\times 3\\times 5\\sin 120^\\circ=\\dfrac{15\\sqrt{3}}{4}$" }
    ],
    exChips: [
      "\\text{정삼각형 톨레미}:\\ a\\cdot\\overline{PA}=a\\cdot\\overline{PB}+a\\cdot\\overline{PC}\\implies \\overline{PA}=3+5=8",
      "\\angle A=60^\\circ\\implies \\angle BPC=180^\\circ-60^\\circ=120^\\circ",
      "\\therefore\\ \\overline{PA}=8,\\quad S_{\\triangle PBC}=\\dfrac{1}{2}\\times 3\\times 5\\sin 120^\\circ=\\dfrac{15\\sqrt{3}}{4}"
    ],
    exLabels: ["정삼각형 톨레미 PA = PB + PC", "PA = 8, 넓이 = 15√3 / 4"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 1.8 - (x - 1.5) * (x - 1.5))), GY0: 390, GV: 185, xr: [0.1, 2.9], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "PB = 3" }, r2: { x: 2.5, col: GO, label: "PC = 5" },
      fn: { t: "정삼각형 내접원 위의 점 P ➔ PA = PB + PC = 3 + 5 = 8", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "PA = PB + PC", finalS: "PA = 8", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 원에 내접하는 사각형 에이비씨디에서 에이비가 이, 비씨가 삼, 씨디가 사, 디에이가 삼이고 두 대각선의 길이가 같을 때 대각선 에이씨의 제곱을 구해 볼까요?", cap: "원 내접 사각형에서 $a=2,\\ b=3,\\ c=4,\\ d=3$ 이고 $AC=BD$ 일 때 $AC^2$ (자작 문항)" },
      { say: "톨레미 정리에 대입하면 마주 보는 변의 곱의 합은 이 곱하기 사 더하기 삼 곱하기 삼인 십칠입니다.", cap: "톨레미 정리: $AB\\cdot CD + BC\\cdot DA = 2\\times 4 + 3\\times 3 = 8 + 9 = 17$" },
      { say: "이 값이 두 대각선의 곱 에이씨 곱하기 비디와 같은데 두 대각선의 길이가 같으므로 에이씨의 제곱은 바로 십칠입니다.", cap: "$\\overline{AC}\\cdot\\overline{BD} = \\overline{AC}^2 = 17$ (코사인법칙 연립 없이 3초 해결!)" }
    ],
    examChips: [
      "\\text{톨레미 정리}:\\ \\overline{AC}\\cdot\\overline{BD}=\\overline{AB}\\cdot\\overline{CD}+\\overline{BC}\\cdot\\overline{DA}",
      "\\overline{AC}=\\overline{BD}\\text{ (등변사다리꼴 대칭)}\\implies \\overline{AC}^2=2\\times 4+3\\times 3",
      "\\therefore\\ \\overline{AC}^2=8+9=17\\quad(\\overline{AC}=\\sqrt{17})"
    ],
    examLabels: ["톨레미 AC·BD = 2×4 + 3×3", "AC² = 17 (3초 완성!)"],
    examGraph: {
      f: x => -0.5 * (x - 1.5) * (x - 1.5) + 1.55, GY0: 390, GV: 155, xr: [0.2, 2.8], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "ac = 2×4 = 8" }, r2: { x: 2.4, col: PK, label: "bd = 3×3 = 9" },
      fn: { t: "톨레미 정리 AC·BD = ac + bd = 8 + 9 = 17", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "8 + 9 = 17", finalS: "AC² = 17", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 원에 내접하는 사각형에서 사인 에이와 사인 파이 빼기 에이는 서로 같으므로 두 삼각형의 넓이 비는 단순히 양옆 변의 곱의 비인 에이디 대 비씨와 같습니다.", cap: "① 내접사각형 넓이 분할비: $\\sin A=\\sin C\\implies S_{\\triangle ABD}:S_{\\triangle CBD} = (a\\cdot d):(b\\cdot c)$!" },
      { say: "둘째, 원에 내접하는 사다리꼴은 무조건 양옆 다리 길이가 같은 등변사다리꼴이며 두 대각선의 길이도 같습니다.", cap: "② 원에 내접하는 사다리꼴 $\\Longleftrightarrow$ 무조건 등변사다리꼴($b=d,\\ p=q$)!" },
      { say: "셋째, 이로써 중학 도형에서 수능으로 직결되는 열두 가지 핵심 법칙 사슬을 모두 완주하셨습니다. 이제 삼각함수 도형과 등비급수 도형 킬러에 자신 있게 도전하세요!", cap: "③ 중학 도형 12대 법칙 완주! 제124강부터 이어 보며 도형 보조선을 완벽히 체화하세요." }
    ],
    nextParts: [
      { tag: "연계 ①", say: "중학 도형 열두 개 법칙의 첫 단계인 원주각과 중심각, 공원점 판정을 복습하려면 제백이십사강으로 이동하세요.", cap: "제124강 · 원주각·중심각과 네 점이 한 원 위에 있을 조건" },
      { tag: "연계 ②", say: "코사인법칙과 할선 정리를 결합한 수능 도형 풀이를 다루는 제팔강도 함께 확인해 보세요.", cap: "제8강 · 코사인법칙과 할선 정리 (대수)" },
      { tag: "이 사이트", say: "이 사이트의 제백이십사강과 제팔강을 이어서 보세요.", cap: "제124강 · 원주각과 공원점  /  제8강 · 코사인법칙" }
    ],
    nextLinks: [
      { lec: 124, label: "제124강 열기 (중학 도형 첫 단계)" },
      { lec: 8, label: "제8강 열기 (코사인법칙과 할선)" },
      { lec: 16, label: "제16강 열기 (삼각형 넓이 5대 공식)" }
    ]
  }
];

function makeLectureConfig(spec) {
  const SCENES = [
    { id: "hook", type: "hook", title: spec.hookTitle, sub: spec.hookSub, parts: [
      { say: spec.hookSay, cap: spec.hookCap }
    ] },
    { id: "why", type: "list", head: spec.whyHead || "이 공식을 배우는 이유", parts: [
      { say: spec.whySay, cap: spec.whyCap }
    ] },
    { id: "hist", type: "list", head: spec.histHead || "개념의 뿌리", parts: [
      { tag: spec.histTag, say: spec.histSay, cap: spec.histCap }
    ] },
    { id: "formula", type: "chips", head: spec.fHead || "공식 만들기", parts: spec.fParts },
    { id: "ex", type: "chips", head: spec.exHead || "예제", parts: spec.exParts },
    { id: "exam", type: "chips", head: spec.examHead || "수능·모의고사 적용", parts: spec.examParts },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: spec.tips },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: spec.nextParts }
  ];

  const threeRowChipDef = (chips, graph, labels) => ({
    graph,
    chips: [
      { id: "T1", tex: chips[0], cls: "cy sm" },
      { id: "T2", tex: chips[1], cls: "pk sm" },
      { id: "T3", tex: chips[2], cls: "go v" }
    ],
    state(ph) {
      const y0 = graph ? 20 : 50, y1 = graph ? 180 : 220, y2 = graph ? 345 : 405;
      return {
        T1: { x: 480, y: y0, op: 1, pop: ph === 0 ? 1 : 0 },
        T2: { x: 480, y: y1, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
        T3: { x: 480, y: y2, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
      };
    },
    links(ph) {
      const L = [];
      if (ph === 1) L.push({ a: "T1", b: "T2", col: CY, label: labels && labels[0] });
      if (ph >= 2) L.push({ a: "T2", b: "T3", col: GO, label: labels && labels[1] });
      return L;
    },
    fx: ph => ph >= 2 ? "confetti" : ph === 1 ? "spark" : ""
  });

  const chipDefs = {
    formula: threeRowChipDef(spec.fChips, null, spec.fLabels),
    ex: threeRowChipDef(spec.exChips, spec.exGraph, spec.exLabels),
    exam: threeRowChipDef(spec.examChips, spec.examGraph, spec.examLabels)
  };

  return {
    lec: spec.lec,
    subj: "midgeo",
    hostId: `l${spec.lec}ShortsHost`,
    mainId: `l${spec.lec}MainContent`,
    prefix: `l${spec.lec}s`,
    title: spec.title,
    desc: spec.desc,
    fChips: spec.fChips,
    tips: spec.tips,
    nextLinks: spec.nextLinks,
    SCENES,
    chipDefs
  };
}

const ALL_SPECS = [...MIDGEO_SPECS_A, ...MIDGEO_SPECS_B];
const CONFIGS = ALL_SPECS.map(makeLectureConfig);
CONFIGS.forEach(cfg => {
  cfg.SCENES.forEach(s => {
    s.parts.forEach(p => { p.ms = estMs(p.say); });
    s.ms = s.parts.reduce((a, p) => a + p.ms, 0);
  });
});

let audioCtx = null;
function getAudio() {
  if (reduced()) return null;
  const AC = window.AudioContext || window.webkitAudioContext;
  if (!AC) return null;
  if (!audioCtx) { try { audioCtx = new AC(); } catch (e) { return null; } }
  if (audioCtx && audioCtx.state === "suspended") { try { audioCtx.resume(); } catch (e) { /* 무시 */ } }
  return audioCtx;
}
function playSfx(kind, enabled) {
  if (!enabled || reduced()) return;
  const ctx = getAudio();
  if (!ctx) return;
  const now = ctx.currentTime;
  try {
    if (kind === "whoosh") {
      const o = ctx.createOscillator(), g = ctx.createGain();
      o.type = "sine"; o.frequency.setValueAtTime(220, now); o.frequency.exponentialRampToValueAtTime(520, now + 0.18);
      g.gain.setValueAtTime(0.001, now); g.gain.linearRampToValueAtTime(0.045, now + 0.05); g.gain.exponentialRampToValueAtTime(0.001, now + 0.19);
      o.connect(g); g.connect(ctx.destination); o.start(now); o.stop(now + 0.2);
    } else if (kind === "pop") {
      const o = ctx.createOscillator(), g = ctx.createGain();
      o.type = "triangle"; o.frequency.setValueAtTime(520, now); o.frequency.exponentialRampToValueAtTime(880, now + 0.11);
      g.gain.setValueAtTime(0.06, now); g.gain.exponentialRampToValueAtTime(0.001, now + 0.13);
      o.connect(g); g.connect(ctx.destination); o.start(now); o.stop(now + 0.14);
    } else if (kind === "chime") {
      [523.25, 659.25, 783.99, 1046.5].forEach((freq, i) => {
        const o = ctx.createOscillator(), g = ctx.createGain(), t0 = now + i * 0.07;
        o.type = "sine"; o.frequency.setValueAtTime(freq, t0);
        g.gain.setValueAtTime(0.05, t0); g.gain.exponentialRampToValueAtTime(0.001, t0 + 0.35);
        o.connect(g); g.connect(ctx.destination); o.start(t0); o.stop(t0 + 0.36);
      });
    }
  } catch (e) { /* 무시 */ }
}

const tf = (x, y, extra) => `translate(${x}px,${y}px) translate(-50%,0)${extra || ""}`;
const mathLen = s => (String(s).match(/\$([^$]+)\$/g) || []).reduce((a, m) => a + m.length - 2, 0);
function splitCap(cap) {
  const i = String(cap).indexOf("$");
  if (i < 0 || mathLen(cap) < 14) return { html: inline(cap) };
  return { label: cap.slice(0, i).trim(), eq: inline(cap.slice(i)) };
}

function goLecturePage(lecNum) {
  if (typeof window.openLectureShorts === "function") {
    window.openLectureShorts(lecNum);
    return;
  }
  if (typeof window.setLecture === "function") {
    window.setLecture(lecNum, true);
    return;
  }
  if (typeof window.switchLecture === "function") {
    window.switchLecture(lecNum);
    setTimeout(() => { window.scrollTo({ top: 0, behavior: "smooth" }); }, 60);
  }
}

function renderMainCard(cfg) {
  const mainEl = $(cfg.mainId);
  if (!mainEl || mainEl.dataset.ready) return;
  mainEl.dataset.ready = "1";
  const cInfo = MIDGEO_CHAIN.find(c => c.lec === cfg.lec) || { step: 1, badge: "중학 도형 마스터", title: cfg.title };
  mainEl.innerHTML = `
    <div class="glass-card" style="margin-bottom:22px;border-left:5px solid #f97316">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px">
        <span class="badge-pill" style="background:rgba(249,115,22,.18);color:#fdba74;border-color:rgba(249,115,22,.4)">
          📐 중학 도형 → 수능 12대 법칙 · 사슬 ${cInfo.step}/12단계 (${cInfo.badge})
        </span>
        <span style="color:var(--text-dim);font-size:.85rem">⚡ 수업 단원·개념 연결 순 핵심 요약 & 9:16 판서 보드</span>
      </div>
      <h2 style="font-size:1.55rem;font-weight:800;color:#fff;margin:0 0 8px 0">
        제${cfg.lec}강 · ${cInfo.title}
      </h2>
      <p class="js-main-desc" style="color:var(--text-muted);font-size:.95rem;line-height:1.65;margin:0 0 16px 0">${cfg.desc}</p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px">
        ${(cfg.fChips || []).map((chip, idx) => `
          <div style="background:rgba(15,23,42,.65);border:1px solid rgba(148,163,184,.18);border-radius:10px;padding:12px 14px">
            <div style="font-size:.78rem;font-weight:700;color:${idx === 0 ? "#38bdf8" : idx === 1 ? "#f472b6" : "#facc15"};margin-bottom:6px">핵심 공식 ${idx + 1}</div>
            <div class="js-main-katex" data-tex="${String(chip).replace(/"/g, "&quot;")}" style="font-size:.95rem;color:#f8fafc;overflow-x:auto"></div>
          </div>
        `).join("")}
      </div>
    </div>`;
  try {
    if (window.katex) {
      mainEl.querySelectorAll(".js-main-katex").forEach(el => {
        el.innerHTML = K(el.getAttribute("data-tex"), false);
      });
    }
    if (window.renderMathInElement) {
      const dEl = mainEl.querySelector(".js-main-desc");
      if (dEl) renderMathInElement(dEl, { delimiters: [{ left: "$", right: "$", display: false }] });
    }
  } catch (e) { /* 무시 */ }
}

function createPlayer(cfg) {
  const pfx = cfg.prefix, SCENES = cfg.SCENES, chipDefs = cfg.chipDefs;
  const total = SCENES.reduce((a, s) => a + s.ms, 0);
  const KEEP = [];
  let host, stageEl, frameEl, cur = { s: 0, p: 0 }, runId = 0, playing = false, curDefId = "";
  const qid = suffix => $(`${pfx}_${suffix}`);
  const sfxEnabled = () => !!(qid("SfxOn") && qid("SfxOn").checked);

  function scaleStage() {
    if (frameEl && stageEl && frameEl.clientWidth > 0) {
      stageEl.style.transform = `scale(${frameEl.clientWidth / 1080})`;
    }
  }
  function burst(x, y, n, colors) {
    const h = stageEl.querySelector(".l2s-chips");
    if (!h || reduced()) return;
    playSfx("pop", sfxEnabled());
    for (let i = 0; i < n; i++) {
      const d = document.createElement("div"); d.className = "l2s-fx";
      const sz = 10 + Math.random() * 16, c = colors[i % colors.length];
      d.style.cssText = `left:${x}px;top:${y}px;width:${sz}px;height:${sz}px;background:${c};box-shadow:0 0 18px ${c}`;
      h.appendChild(d);
      const a = Math.random() * Math.PI * 2, r = 90 + Math.random() * 150;
      d.animate([{ transform: "translate(0,0) scale(1)", opacity: 1 }, { transform: `translate(${Math.cos(a) * r}px,${Math.sin(a) * r}px) scale(.2)`, opacity: 0 }], { duration: 700 + Math.random() * 400, easing: "cubic-bezier(.1,.8,.3,1)" }).onfinish = () => d.remove();
    }
  }
  function confetti() {
    if (reduced()) return;
    playSfx("chime", sfxEnabled());
    const cs = ["#fbbf24", "#f472b6", "#38bdf8", "#34d399", "#a78bfa", "#fb7185"];
    for (let i = 0; i < 46; i++) {
      const d = document.createElement("div"); d.className = "l2s-conf";
      d.style.cssText = `left:${Math.random() * 1040}px;background:${cs[i % cs.length]}`;
      stageEl.appendChild(d);
      d.animate([{ transform: "translateY(0) rotate(0deg)", opacity: 1 }, { transform: `translate(${(Math.random() - 0.5) * 240}px,${1500 + Math.random() * 400}px) rotate(${(Math.random() - 0.5) * 1080}deg)`, opacity: 0.9 }], { duration: 1800 + Math.random() * 1400, delay: Math.random() * 500, easing: "cubic-bezier(.3,.1,.6,1)" }).onfinish = () => d.remove();
    }
  }
  function fly(hostEl, m, n) {
    const { el, x0, y0, o, dist } = m;
    const arc = 70 + Math.min(150, dist * 0.2), mx = (x0 + o.x) / 2, my = (y0 + o.y) / 2 - arc;
    const rot = (o.x >= x0 ? 1 : -1) * (7 + Math.random() * 7), delay = n * 80 + 350;
    el.style.transform = tf(o.x, o.y);
    if (reduced()) return;
    if (n === 0) playSfx("whoosh", sfxEnabled());
    const kf = [{ transform: tf(x0, y0, " scale(1) rotate(0deg)") }, { transform: tf(mx, my, ` scale(1.22) rotate(${rot}deg)`), offset: 0.5 }, { transform: tf(o.x, o.y, " scale(1) rotate(0deg)") }];
    const opt = { duration: 1100, delay, easing: "cubic-bezier(.22,1,.36,1)", fill: "both" };
    const an = el.animate(kf, opt); an.onfinish = () => an.cancel();
    [0.11, 0.22].forEach((lag, gi) => {
      const g = el.cloneNode(true); g.removeAttribute("data-id"); g.classList.add("ghost"); g.style.opacity = 0; g.style.transform = tf(x0, y0); hostEl.appendChild(g);
      g.animate(kf.map((f, q) => Object.assign({}, f, { opacity: q === 1 ? 0.34 - gi * 0.12 : 0 })), Object.assign({}, opt, { delay: delay + lag * 1000 })).onfinish = () => g.remove();
    });
  }
  function drawLinks(chipsEl, def, S, ph, animate) {
    const svg = chipsEl.querySelector(".l2s-links"); svg.innerHTML = "";
    const NS = "http://www.w3.org/2000/svg";
    (def.links(ph) || []).forEach((lk, gi) => {
      const A = chipsEl.querySelector(`[data-id="${lk.a}"]`), B = chipsEl.querySelector(`[data-id="${lk.b}"]`); if (!A || !B) return;
      const a = S[lk.a], b = S[lk.b];
      const x1 = a.x, y1 = a.y + A.offsetHeight, x2 = b.x, y2 = b.y;
      const dy = Math.max(60, Math.abs(y2 - y1) * 0.5), d = `M ${x1} ${y1} C ${x1} ${y1 + dy}, ${x2} ${y2 - dy}, ${x2} ${y2}`;
      const g = document.createElementNS(NS, "g"); g.style.color = lk.col;
      const p = document.createElementNS(NS, "path"); p.setAttribute("d", d); p.setAttribute("stroke", lk.col); g.appendChild(p);
      [[x1, y1], [x2, y2]].forEach(pt => { const c = document.createElementNS(NS, "circle"); c.setAttribute("cx", pt[0]); c.setAttribute("cy", pt[1]); c.setAttribute("r", 12); c.setAttribute("fill", lk.col); g.appendChild(c); });
      let tx = null;
      if (lk.label) { tx = document.createElementNS(NS, "text"); tx.setAttribute("x", (x1 + x2) / 2); tx.setAttribute("y", (y1 + y2) / 2 + 10); tx.setAttribute("fill", GO); tx.textContent = lk.label; g.appendChild(tx); }
      svg.appendChild(g);
      if (animate && !reduced()) {
        const L = p.getTotalLength(), dl = gi * 200;
        p.style.strokeDasharray = L; p.animate([{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: 650, delay: dl, easing: "cubic-bezier(.3,.7,.3,1)", fill: "both" });
        g.querySelectorAll("circle").forEach(c => c.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 300, delay: dl + 300, fill: "both" }));
        if (tx) tx.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 350, delay: dl + 450, fill: "both" });
      }
    });
  }
  function graphHtml(c) {
    const gx0 = c.gx0 != null ? c.gx0 : 90, gu = c.gux != null ? c.gux : 240;
    const px = x => gx0 + gu * x, py = x => c.GY0 - c.GV * c.f(x);
    let d = "", first = true;
    for (let x = c.xr[0]; x <= c.xr[1] + 0.001; x += 0.05) { d += (first ? "M" : "L") + px(x).toFixed(1) + " " + py(x).toFixed(1) + " "; first = false; }
    let a = `M ${px(c.area[0])} ${c.GY0} `;
    for (let x = c.area[0]; x <= c.area[1] + 0.001; x += 0.05) a += `L ${px(x).toFixed(1)} ${py(x).toFixed(1)} `;
    a += `L ${px(c.area[1])} ${c.GY0} Z`;
    const clipId = `${pfx}_gClip`;
    return `<svg class="l2s-graph" viewBox="0 0 960 480">
      <defs><clipPath id="${clipId}"><rect class="js-gClipR" x="0" y="0" width="0" height="480"></rect></clipPath></defs>
      <g stroke="rgba(255,255,255,.45)" stroke-width="3" fill="none"><line x1="20" y1="${c.GY0}" x2="900" y2="${c.GY0}"></line><line x1="${gx0}" y1="${c.ybot}" x2="${gx0}" y2="${c.ytop}"></line></g>
      <text x="925" y="${c.GY0 + 12}" fill="#cbd5e1" font-size="38">x</text><text x="${gx0 + 18}" y="${c.ytop + 8}" fill="#cbd5e1" font-size="38">y</text>
      <g class="js-gScale" style="transform-origin:0 ${c.GY0}px">
        <path class="js-gArea" d="${a}" fill="rgba(251,191,36,.38)" clip-path="url(#${clipId})"></path>
        <path class="js-gCurve" d="${d}" fill="none" stroke="#e2e8f0" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke" style="filter:drop-shadow(0 0 8px rgba(226,232,240,.5))"></path>
      </g>
      <g class="js-gRoots" opacity="0"><circle cx="${px(c.r1.x)}" cy="${c.GY0}" r="15" fill="${c.r1.col}"></circle><circle cx="${px(c.r2.x)}" cy="${c.GY0}" r="15" fill="${c.r2.col}"></circle>
        <text x="${Math.max(150, Math.min(810, px(c.r1.x)))}" y="${c.labelY}" fill="${c.r1.col}" font-size="34" text-anchor="middle">${c.r1.label}</text>
        <text x="${Math.max(150, Math.min(810, px(c.r2.x)))}" y="${c.labelY}" fill="${c.r2.col}" font-size="34" text-anchor="middle">${c.r2.label}</text></g>
      <text class="js-gFn" x="${c.fn.x}" y="${c.fn.y}" fill="#e2e8f0" font-size="36" text-anchor="middle" opacity="0">${c.fn.t}</text>
      <text class="js-gS" x="${c.sPos[0]}" y="${c.sPos[1]}" fill="${GO}" font-size="54" font-weight="800" text-anchor="middle" opacity="0">${c.sOpenTxt}</text>
    </svg>`;
  }
  function graphPhase(boardEl, ph, animate, fresh, c) {
    const q = sel => boardEl.querySelector(sel);
    const curve = q(".js-gCurve"); if (!curve) return;
    const L = curve.getTotalLength(), area = q(".js-gArea"), clipR = q(".js-gClipR"), roots = q(".js-gRoots"), fn = q(".js-gFn"), S = q(".js-gS");
    if (fresh) {
      if (animate && !reduced()) {
        curve.style.strokeDasharray = L; curve.animate([{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: 1800, easing: "cubic-bezier(.4,.1,.3,1)", fill: "both" });
        clipR.animate([{ width: "0px" }, { width: "960px" }], { duration: 1500, delay: 1500, easing: "ease-out", fill: "both" });
        roots.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 500, delay: 900, fill: "both" });
        fn.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 600, delay: 1200, fill: "both" });
      } else {
        clipR.setAttribute("width", 960); roots.setAttribute("opacity", 1); fn.setAttribute("opacity", 1);
      }
    }
    const reach = ph >= c.finalPh;
    if (reach) {
      S.textContent = c.finalS; S.setAttribute("opacity", 1);
      if (animate && !reduced()) { S.animate([{ opacity: 0, transform: "scale(.6)" }, { opacity: 1, transform: "scale(1)" }], { duration: 600, easing: "cubic-bezier(.2,1.4,.4,1)", fill: "both" }); area.animate([{ fillOpacity: 1 }, { fillOpacity: 1.9 }, { fillOpacity: 1 }], { duration: 900 }); }
    } else {
      S.textContent = c.sOpenTxt; S.setAttribute("opacity", fresh && animate ? 0 : 1);
      if (fresh && animate && !reduced()) S.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 500, delay: 2200, fill: "both" });
    }
  }
  function renderChips(sc, k, animate) {
    const def = chipDefs[sc.id];
    let chipsEl = stageEl.querySelector(".l2s-chips"), fresh = false;
    if (!chipsEl || curDefId !== sc.id) {
      fresh = true; curDefId = sc.id;
      stageEl.querySelector(".l2s-board").innerHTML = `<div class="l2s-head" style="margin-bottom:0">${sc.head}</div>${def.graph ? graphHtml(def.graph) : ""}<div class="l2s-chips ${def.graph ? "g" : ""}"><svg class="l2s-links" viewBox="0 0 960 930"></svg>${def.chips.map(c => `<div class="l2c ${c.cls}" data-id="${c.id}"></div>`).join("")}</div>`;
      chipsEl = stageEl.querySelector(".l2s-chips");
      const S0 = def.state(0);
      def.chips.forEach(c => {
        const el = chipsEl.querySelector(`[data-id="${c.id}"]`), o = S0[c.id];
        el.innerHTML = c.tex ? K(c.tex) : ""; el.dataset.h = c.tex; el.dataset.x = o.x; el.dataset.y = o.y;
        el.style.transform = tf(o.x, o.y); el.style.opacity = o.op; if (o.w) el.style.width = o.w + "px";
      });
    }
    const S = def.state(k), flying = [];
    def.chips.forEach(c => {
      const el = chipsEl.querySelector(`[data-id="${c.id}"]`), o = S[c.id], texStr = o.tex != null ? o.tex : c.tex;
      const x0 = +el.dataset.x, y0 = +el.dataset.y, dist = Math.hypot(o.x - x0, o.y - y0);
      const seen = (+el.style.opacity || 0) > 0.05 || o.op > 0.05, changed = el.dataset.h !== texStr;
      if (changed) { el.innerHTML = K(texStr); el.dataset.h = texStr; }
      if (o.w) el.style.width = o.w + "px";
      if (animate && dist > 8 && seen) flying.push({ el, x0, y0, o, dist }); else el.style.transform = tf(o.x, o.y);
      el.style.opacity = o.op; el.dataset.x = o.x; el.dataset.y = o.y;
      if (animate && o.pop && !(dist > 8) && (changed || !fresh) && o.op > 0.05 && !reduced()) {
        setTimeout(() => {
          const a = el.animate([{ transform: tf(o.x, o.y, " scale(1)") }, { transform: tf(o.x, o.y, " scale(1.35)"), offset: 0.4 }, { transform: tf(o.x, o.y, " scale(1)") }], { duration: 520, easing: "cubic-bezier(.2,1.4,.4,1)" });
          a.onfinish = () => { el.style.transform = tf(o.x, o.y); };
          burst(o.x, o.y + 40, 10, [GO, "#fde68a", PK, CY]);
        }, 450);
      }
    });
    flying.sort((a, b) => a.x0 - b.x0).forEach((m, n) => fly(chipsEl, m, n));
    drawLinks(chipsEl, def, S, k, animate);
    if (def.graph) graphPhase(stageEl.querySelector(".l2s-board"), k, animate, fresh, def.graph);
    const fxk = def.fx(k); if (animate && fxk === "confetti") setTimeout(confetti, 700);
    return sc.parts[k].cap;
  }
  function fitMath() {
    if (!stageEl) return;
    stageEl.querySelectorAll(".l2s-fit").forEach(el => {
      el.style.fontSize = "";
      const box = el.closest(".l2s-fitbox") || el.parentElement, avail = box.clientWidth - 16, w = el.scrollWidth;
      if (w > avail && avail > 100) el.style.fontSize = (parseFloat(getComputedStyle(el).fontSize) * avail / w * 0.96) + "px";
    });
    stageEl.querySelectorAll(".l2c").forEach(el => {
      el.style.fontSize = "";
      const kEl = el.querySelector(".katex");
      const w = Math.max(el.offsetWidth, el.scrollWidth, kEl ? kEl.offsetWidth + 48 : 0);
      if (w > 860) el.style.fontSize = (parseFloat(getComputedStyle(el).fontSize) * 860 / w * 0.96) + "px";
    });
  }
  function listBoard(sc, k) {
    const its = sc.parts.map(p => ({ tag: p.tag || "", cap: p.cap })), upto = k >= 0 ? k + 1 : its.length;
    return `<div class="l2s-head">${sc.head}</div>` + its.slice(0, upto).map((x, n) => {
      const s = splitCap(x.cap);
      const body = s.eq
        ? `<span class="l2s-itbody l2s-fitbox"><span class="l2s-lab">${inline(s.label)}</span><span class="l2s-eq l2s-fit">${s.eq}</span></span>`
        : `<span class="l2s-itbody txt l2s-fitbox"><span class="l2s-fit" style="display:inline-block">${s.html}</span></span>`;
      return `<div class="l2s-item ${n === upto - 1 ? "cur" : ""}">${x.tag ? `<em>${x.tag}</em>` : ""}${body}</div>`;
    }).join("");
  }
  function render(si, pi, animate) {
    const sc = SCENES[si]; cur = { s: si, p: pi };
    if (!stageEl.querySelector(".l2s-board")) {
      stageEl.innerHTML = `<div class="l2s-board"></div><div class="l2s-cap"><span></span></div><div class="l2s-bar" id="${pfx}_Bar"></div>`;
    }
    let cap = sc.parts[pi].cap;
    if (sc.type === "chips") cap = renderChips(sc, pi, animate);
    else {
      curDefId = "";
      const b = stageEl.querySelector(".l2s-board");
      b.innerHTML = sc.type === "hook" ? `<div class="l2s-big">${sc.title}</div><div class="l2s-sub">${sc.sub}</div>` : listBoard(sc, pi);
    }
    const c = stageEl.querySelector(".l2s-cap span"), sp = splitCap(cap);
    c.innerHTML = sp.eq ? `<span class="l2s-lab">${inline(sp.label)}</span><span class="l2s-capeq l2s-fit">${sp.eq}</span>` : `<span class="l2s-fit" style="display:inline-block">${sp.html}</span>`;
    stageEl.querySelector(".l2s-cap").classList.add("l2s-fitbox");
    c.style.animation = "none"; c.offsetWidth; c.style.animation = "";
    let before = 0; for (let i = 0; i < si; i++) before += SCENES[i].ms; for (let j = 0; j < pi; j++) before += sc.parts[j].ms;
    const bar = qid("Bar");
    if (bar) {
      bar.style.transition = "none"; bar.style.width = (before / total * 100) + "%";
      if (animate) { bar.offsetWidth; bar.style.transition = `width ${sc.parts[pi].ms / 1000}s linear`; bar.style.width = ((before + sc.parts[pi].ms) / total * 100) + "%"; }
    }
    const st = qid("Time");
    if (st) st.textContent = `${si + 1} / ${SCENES.length} 장면 · 예상 전체 ${Math.floor(Math.round(total / 1000) / 60)}분 ${Math.round(Math.round(total / 1000) % 60)}초 (3분 미만)`;
    host.querySelectorAll(".l2s-sc").forEach((e, i) => e.classList.toggle("on", i === si));
    scaleStage();
    fitMath();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitMath);
    setTimeout(fitMath, 350);
  }
  const NATURAL = v => /natural|neural|online|google/i.test(v.name);
  const voicesReady = () => new Promise(res => {
    if (!window.speechSynthesis || speechSynthesis.getVoices().length) return res();
    const t = setTimeout(res, 1500);
    speechSynthesis.addEventListener("voiceschanged", () => { clearTimeout(t); res(); }, { once: true });
  });
  function pickVoice() {
    const vs = window.speechSynthesis ? speechSynthesis.getVoices() : [];
    const sel = qid("Voice") && qid("Voice").value;
    return vs.find(v => v.name === sel) || vs.filter(v => /^ko/i.test(v.lang)).sort((a, b) => NATURAL(b) - NATURAL(a))[0] || null;
  }
  function setState(m) { const e = qid("State"); if (e) e.textContent = m; }
  function say1(text, voice, rate, pitch) {
    return new Promise(res => {
      const u = new SpeechSynthesisUtterance(text); KEEP.push(u); u.lang = "ko-KR"; if (voice) u.voice = voice; u.rate = rate; u.pitch = pitch;
      let done = false, started = false, tm = 0, ts = 0;
      const fin = ok => { if (done) return; done = true; clearTimeout(tm); clearTimeout(ts); const k = KEEP.indexOf(u); if (k >= 0) KEEP.splice(k, 1); res(ok); };
      u.onstart = () => { started = true; clearTimeout(ts); setState("읽는 중…"); }; u.onend = () => fin(true); u.onerror = () => fin(false);
      tm = setTimeout(() => fin(started), Math.max(7000, text.length * 360));
      ts = setTimeout(() => { if (!started) { try { speechSynthesis.cancel(); } catch (e) { /* 무시 */ } fin(false); } }, 3000);
      try { speechSynthesis.speak(u); } catch (e) { fin(false); }
    });
  }
  async function speak(text) {
    if (!qid("VoiceOn") || !qid("VoiceOn").checked || !window.speechSynthesis || !text) return true;
    await voicesReady();
    try { speechSynthesis.cancel(); speechSynthesis.resume(); } catch (e) { /* 무시 */ }
    await sleep(90);
    const rate = +(qid("Rate") && qid("Rate").value) || 1;
    let voice = pickVoice(), retried = false;
    const parts = String(text).split(/(?<=[.!?])\s+/).filter(Boolean);
    for (const s of parts) {
      let ok = await say1(s, voice, rate, 1);
      if (!ok && !retried) { retried = true; voice = null; ok = await say1(s, null, 1, 1); }
      if (!ok) { setState("소리가 시작되지 않았습니다. 볼륨·탭 음소거를 확인하세요."); return false; }
      await sleep(130);
    }
    setState(""); return true;
  }
  async function playFrom(si, pi) {
    if (window.Math2Shorts && window.Math2Shorts.PLAYERS) {
      Object.values(window.Math2Shorts.PLAYERS).forEach(p => { if (p && p.stop) p.stop(); });
    }
    const my = ++runId; playing = true;
    const btn = qid("Play"); if (btn) btn.textContent = "일시정지";
    for (let i = si; i < SCENES.length; i++) {
      for (let j = (i === si ? pi : 0); j < SCENES[i].parts.length; j++) {
        if (my !== runId) return;
        render(i, j, true);
        const p = SCENES[i].parts[j], rate = +(qid("Rate") && qid("Rate").value) || 1;
        await Promise.all([sleep(p.ms / rate), speak(p.say)]);
      }
    }
    if (my === runId) { stop(); render(0, 0, false); }
  }
  function stop() {
    runId++; playing = false;
    const b = qid("Play"); if (b) b.textContent = "재생";
    if (window.speechSynthesis) { try { speechSynthesis.cancel(); } catch (e) { /* 무시 */ } }
  }
  function step(d) {
    const was = playing; stop();
    let { s, p } = cur; p += d;
    if (p < 0) { s = Math.max(0, s - 1); p = SCENES[s].parts.length - 1; }
    else if (p >= SCENES[s].parts.length) { s = Math.min(SCENES.length - 1, s + 1); p = 0; }
    render(s, p, false); if (was) playFrom(s, p);
  }
  function fillVoices() {
    const sel = qid("Voice"); if (!sel || !window.speechSynthesis) return;
    const vs = speechSynthesis.getVoices().filter(v => /^ko/i.test(v.lang)).sort((a, b) => NATURAL(b) - NATURAL(a)), cur0 = sel.value;
    sel.innerHTML = vs.map(v => `<option value="${v.name}">${NATURAL(v) ? "★ " : ""}${v.name}</option>`).join("") || `<option value="">기본 음성</option>`;
    if (cur0) sel.value = cur0;
  }
  function init() {
    renderMainCard(cfg);
    const mount = $(cfg.hostId);
    if (!mount || mount.dataset.ready) return;
    if (!window.katex) { setTimeout(init, 300); return; }
    mount.dataset.ready = "1";
    mount.innerHTML = `${midgeoChainNavHtml(cfg.lec)}
      <h2 style="font-size:1.25rem;margin-bottom:6px">${cfg.title}</h2>
      <p class="l2s-note js-desc" style="margin-bottom:14px">${cfg.desc}</p>
      <div class="l2s-wrap">
        <div class="l2s-frame" id="${pfx}_Frame"><div class="l2s-stage" id="${pfx}_Stage"></div></div>
        <div class="l2s-ctl">
          <div class="l2s-row">
            <button class="l2s-btn" id="${pfx}_Prev" type="button">‹ 이전</button>
            <button class="l2s-btn pri" id="${pfx}_Play" type="button">재생</button>
            <button class="l2s-btn" id="${pfx}_Next" type="button">다음 ›</button>
          </div>
          <div class="l2s-opt">
            <label><input type="checkbox" id="${pfx}_VoiceOn" checked> 음성</label>
            <label><input type="checkbox" id="${pfx}_SfxOn" checked> 효과음</label>
            <label>속도 <input type="range" id="${pfx}_Rate" min="0.8" max="1.4" step="0.05" value="1" style="width:90px"></label>
            <label>목소리 <select id="${pfx}_Voice"></select></label>
            <button class="l2s-btn" id="${pfx}_Test" type="button" style="padding:4px 10px">음성 시험</button>
          </div>
          <div class="l2s-state" id="${pfx}_State"></div>
          <div class="l2s-note" id="${pfx}_Time"></div>
          <div class="l2s-list" id="${pfx}_List">${SCENES.map((s, i) => `<div class="l2s-sc" data-i="${i}">${i + 1}. ${s.head || s.title}</div>`).join("")}</div>
          <div class="l2s-row" id="${pfx}_Links">
            <span class="l2s-note" style="margin:0">이어서 볼 강의</span>
            ${cfg.nextLinks.map(lk => `<button class="l2s-btn" type="button" data-lec="${lk.lec}">${lk.label}</button>`).join("")}
          </div>
          <p class="l2s-note">★ 표시는 더 자연스러운 목소리입니다. Edge 브라우저에서 열면 ‘Natural’ 한국어 목소리가 나오며, 이 목소리는 글이 Microsoft 서버로 전송됩니다. (역사 연도·인물 서술은 공개 전 출처 확인이 필요합니다.)</p>
        </div>
      </div>`;
    try {
      if (window.renderMathInElement) {
        renderMathInElement(mount.querySelector(".js-desc"), { delimiters: [{ left: "$", right: "$", display: false }] });
      }
    } catch (e) { /* 무시 */ }
    host = mount; frameEl = qid("Frame"); stageEl = qid("Stage");
    new ResizeObserver(scaleStage).observe(frameEl);
    mount.onclick = e => {
      const cb = e.target.closest("[data-chain-lec]");
      if (cb) { goLecturePage(+cb.dataset.chainLec); return; }
      const lb = e.target.closest("[data-lec]");
      if (lb) { goLecturePage(+lb.dataset.lec); }
    };
    qid("Play").onclick = () => { if (playing) stop(); else playFrom(cur.s, cur.p); };
    qid("Prev").onclick = () => step(-1);
    qid("Next").onclick = () => step(1);
    qid("List").onclick = e => {
      const it = e.target.closest("[data-i]"); if (!it) return;
      const was = playing; stop(); render(+it.dataset.i, 0, false); if (was) playFrom(+it.dataset.i, 0);
    };
    qid("Test").onclick = async () => {
      stop(); qid("VoiceOn").checked = true; setState("시험 중…");
      const ok = await speak("안녕하세요. 중학 도형에서 수능으로 직결되는 열두 가지 법칙을 함께 정리해 볼까요?");
      setState(ok ? "소리가 정상입니다" : "소리가 시작되지 않았습니다");
    };
    if (window.speechSynthesis) {
      speechSynthesis.addEventListener("voiceschanged", fillVoices);
      setTimeout(fillVoices, 300);
    }
    render(0, 0, false);
  }
  const api = { init, render, stop, SCENES, scaleStage };
  if (window.Math2Shorts && window.Math2Shorts.PLAYERS) {
    window.Math2Shorts.PLAYERS[cfg.lec] = api;
  }
  return api;
}

const MIDGEO_PLAYERS = {};
function initMidGeo() {
  CONFIGS.forEach(cfg => {
    if (!MIDGEO_PLAYERS[cfg.lec]) MIDGEO_PLAYERS[cfg.lec] = createPlayer(cfg);
    MIDGEO_PLAYERS[cfg.lec].init();
  });
}

window.MidGeoShorts = { PLAYERS: MIDGEO_PLAYERS, CONFIGS, initMidGeo };
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initMidGeo);
else initMidGeo();
window.addEventListener("load", initMidGeo);
})();
