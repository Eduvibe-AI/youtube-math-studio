/* 기하 심화 (12강 사슬: 88 → 89 → 90 → 91 → 92 → 93 → 94 → 95 → 96 → 97 → 98 → 99)
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
const estMs = t => Math.max(1800, Math.round(Array.from(t || "").length * 125) + 400);

const GEOADV_CHAIN = [
  { lec: 88, step: 1,  badge: "포물선심화",    title: "포물선의 정의(PF=PH)와 초점 현·준선 직각 성질" },
  { lec: 89, step: 2,  badge: "초점삼각형",    title: "타원(r₁+r₂=2a)·쌍곡선(|r₁−r₂|=2a) 초점삼각형과 점근선" },
  { lec: 90, step: 3,  badge: "이차곡선접선",  title: "이차곡선 접선의 방정식 3대 공식과 광학적 반사 성질" },
  { lec: 91, step: 4,  badge: "벡터와자취",    title: "평면벡터 분점·일직선 조건(α+β=1)과 종점 자취 넓이" },
  { lec: 92, step: 5,  badge: "벡터내적",      title: "평면벡터 내적의 정사영 의미와 중점 분해 공식" },
  { lec: 93, step: 6,  badge: "직선원벡터",    title: "직선의 벡터방정식(방향·법선)과 원의 벡터방정식" },
  { lec: 94, step: 7,  badge: "꼬인위치각",    title: "공간도형 평면 결정 조건 4가지와 꼬인 위치의 각" },
  { lec: 95, step: 8,  badge: "삼수선정리",    title: "직선·평면 수직 조건과 삼수선의 정리 3유형 해법" },
  { lec: 96, step: 9,  badge: "이면각",        title: "이면각의 정의(교선 수선)와 정사면체·정팔면체 이면각" },
  { lec: 97, step: 10, badge: "정사영",        title: "정사영의 길이·넓이(S'=S cos θ)와 태양광선 그림자" },
  { lec: 98, step: 11, badge: "공간좌표",      title: "공간좌표 대칭·내분·무게중심과 대칭이동 최단거리" },
  { lec: 99, step: 12, badge: "구의방정식",    title: "구의 방정식, 좌표평면에 접하는 구와 단면 원" }
];

function geoadvChainNavHtml(curLec) {
  const idx = GEOADV_CHAIN.findIndex(c => c.lec === curLec);
  const prev = idx > 0 ? GEOADV_CHAIN[idx - 1] : null;
  const next = idx >= 0 && idx < GEOADV_CHAIN.length - 1 ? GEOADV_CHAIN[idx + 1] : null;
  return `
    <div class="l2s-chain-box" style="margin-bottom:16px;padding:12px 14px;border-radius:12px;background:rgba(15,23,42,.82);border:1px solid rgba(251,146,60,.35)">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:10px">
        <span style="font-size:13px;font-weight:800;color:#fdba74">📐 기하 심화 · 수업 단원·개념 연결 사슬 (${idx + 1} / ${GEOADV_CHAIN.length}단계)</span>
        <div style="display:flex;gap:6px">
          ${prev ? `<button type="button" class="l2s-btn" data-chain-lec="${prev.lec}">← 이전 (${prev.step}단계 · 제${prev.lec}강)</button>` : ""}
          ${next ? `<button type="button" class="l2s-btn on" data-chain-lec="${next.lec}">다음 (${next.step}단계 · 제${next.lec}강) →</button>` : `<button type="button" class="l2s-btn on" data-chain-lec="88">기하 심화 첫 단계로 →</button>`}
        </div>
      </div>
      <div style="display:flex;gap:5px;flex-wrap:wrap">
        ${GEOADV_CHAIN.map(c => `
          <button type="button" data-chain-lec="${c.lec}" style="padding:4px 8px;border-radius:999px;font-size:11px;font-weight:700;cursor:pointer;border:1px solid ${c.lec === curLec ? '#fb923c' : 'rgba(148,163,184,.28)'};background:${c.lec === curLec ? 'rgba(251,146,60,.22)' : 'rgba(15,23,42,.6)'};color:${c.lec === curLec ? '#fdba74' : '#cbd5e1'}">
            ${c.step}. 제${c.lec}강 (${c.badge})
          </button>
        `).join("")}
      </div>
    </div>
  `;
}

const GEOADV_SPECS_A = [
  {
    lec: 88,
    title: "숏츠식 판서 미리보기 · 포물선의 정의(PF=PH)와 초점 현·준선 직각 성질",
    desc: "포물선 $y^{2}=4px$ 의 정의($\\overline{PF}=\\overline{PH}=x_{1}+p$)와 초점 현 길이($x_{1}+x_{2}+2p$), 준선 위에서 그은 두 접선의 직교 성질을 정리합니다.",
    hookTitle: "포물선은 무조건 준선 수선의 발 H!", hookSub: "초점 거리 PF 를 준선 거리 PH = x + p 로 바꾸면 3초 끝!",
    hookSay: "포물선 문제가 나오면 식을 연립하기 전에 무조건 준선부터 긋고 수선의 발을 내려야 하는 이유, 30초 만에 정리합니다.",
    hookCap: "포물선의 정의와 초점 현 성질 · 30초 정리",
    whySay: "포물선 위의 점에서 초점까지의 비스듬한 거리 피에프는 준선까지의 수평 거리 피에이치와 항상 같으므로, 복잡한 피타고라스 계산이 엑스좌표 더하기 피라는 일차식으로 즉시 바뀝니다.",
    whyCap: "포물선 $y^{2}=4px\\ (p\\gt 0)$ 위 점 $P(x_{1},y_{1})$: $\\overline{PF}=\\overline{PH}=x_{1}+p$",
    histTag: "아폴로니오스·파포스", histSay: "고대 그리스의 아폴로니오스가 원뿔곡선에서 포물선을 명명했고, 파포스가 초점과 준선의 거리 비가 1이라는 정의를 확립했습니다.",
    histCap: "원뿔곡선(Conic Sections)과 초점·준선 등거리 정의 $\\overline{PF}=\\overline{PH}$",
    fParts: [
      { say: "와이 제곱은 사 피 엑스 위의 점 피에서 초점 에프까지의 거리는 점 피의 엑스좌표 엑스원에 피를 더한 값입니다.", cap: "초점 거리 공식: $\\overline{PF}=x_{1}+p$ ($x^{2}=4py$ 이면 $\\overline{PF}=y_{1}+p$)" },
      { say: "초점 에프를 지나는 직선이 포물선과 만나는 두 점 에이, 비 사이의 초점 현의 길이는 두 점의 엑스좌표 합 더하기 이 피입니다.", cap: "초점 현의 길이: $\\overline{AB}=\\overline{AF}+\\overline{BF}=(x_{1}+p)+(x_{2}+p)=x_{1}+x_{2}+2p$" },
      { say: "준선 위의 한 점에서 포물선에 그은 두 접선은 항상 서로 수직으로 만나며, 두 접점을 잇는 직선은 반드시 초점을 지납니다.", cap: "준선 접선 성질: 준선 위 점에서 그은 두 접선은 직교($m_{1}m_{2}=-1$)!" }
    ],
    fChips: [
      "y^{2}=4px\\ (p\\gt 0):\\ \\text{초점 }F(p,0),\\ \\text{준선 }x=-p,\\ \\overline{PF}=x_{1}+p",
      "\\text{초점 현 길이 }\\overline{AB}=x_{1}+x_{2}+2p,\\quad \\dfrac{1}{\\overline{AF}}+\\dfrac{1}{\\overline{BF}}=\\dfrac{1}{p}",
      "\\text{준선 위 점에서 그은 두 접선은 항상 수직 }(90^\\circ)\\text{ 교차!}"
    ],
    fLabels: ["초점 거리 PF = x₁ + p", "초점 현 AB = x₁ + x₂ + 2p"],
    exParts: [
      { say: "예를 들어 포물선 와이 제곱은 팔 엑스의 초점 에프를 지나는 직선이 포물선과 만나는 두 점 에이, 비의 엑스좌표의 합이 육일 때 선분 에이비의 길이를 구해 봅시다.", cap: "$y^{2}=8x$ 의 초점 현 양 끝점 $x_{1}+x_{2}=6$ 일 때 $\\overline{AB}$ 의 길이" },
      { say: "사 피가 팔이므로 피는 이이고, 준선은 엑스는 마이너스 이입니다.", cap: "$4p=8\\ \\Rightarrow\\ p=2$ (준선 $x=-2$)" },
      { say: "선분 에이비의 길이는 엑스원 더하기 엑스투 더하기 이 피이므로 육 더하기 사, 십입니다.", cap: "$\\overline{AB}=(x_{1}+x_{2})+2p=6+4=10$" }
    ],
    exChips: [
      "y^{2}=8x=4\\cdot 2x\\ \\Longrightarrow\\ p=2,\\quad x_{1}+x_{2}=6",
      "\\overline{AB}=\\overline{AF}+\\overline{BF}=(x_{1}+p)+(x_{2}+p)",
      "=(x_{1}+x_{2})+2p=6+4=10"
    ],
    exLabels: ["p = 2, x₁ + x₂ = 6", "초점 현 길이 = 10"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 1.3 * (x - 0.5))) + 0.25, GY0: 390, GV: 110, xr: [0.5, 3], area: [0.6, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.9, col: CY, label: "초점 F(p, 0)" }, r2: { x: 2.3, col: PK, label: "PF = PH = x₁ + p" },
      fn: { t: "포물선 정의: 비스듬한 PF 대신 수평 길이 x₁ + p 로 즉시 변환!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "6 + 2(2)", finalS: "AB = 10", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 포물선 와이 제곱은 십이 엑스 위의 점 피와 초점 에프에 대하여 선분 피에프의 길이가 칠일 때, 점 피의 엑스좌표는 얼마일까요?", cap: "$y^{2}=12x$ 위의 점 $P$ 에서 $\\overline{PF}=7$ 일 때 점 $P$ 의 $x$좌표 (자작 문항)" },
      { say: "사 피가 십이이므로 피는 삼입니다.", cap: "$4p=12\\ \\Rightarrow\\ p=3$" },
      { say: "초점 거리 공식 엑스원 더하기 삼이 칠이므로 점 피의 엑스좌표는 사입니다.", cap: "$\\overline{PF}=x_{1}+3=7\\ \\Rightarrow\\ x_{1}=4$" }
    ],
    examChips: [
      "y^{2}=12x=4\\cdot 3x\\ \\Longrightarrow\\ p=3",
      "\\overline{PF}=x_{1}+p=x_{1}+3=7",
      "\\therefore\\ x_{1}=4"
    ],
    examLabels: ["PF = x₁ + 3 = 7", "정답 x₁ = 4"],
    examGraph: {
      f: x => Math.sqrt(Math.max(0, 1.4 * (x - 0.4))) + 0.25, GY0: 390, GV: 110, xr: [0.4, 3], area: [0.5, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.8, col: CY, label: "초점 F(3, 0)" }, r2: { x: 2.2, col: GO, label: "x₁ = 7 − 3 = 4" },
      fn: { t: "PF = x₁ + p ⇔ x₁ = PF − p = 7 − 3 = 4", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "x₁ + 3 = 7", finalS: "x₁ = 4", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 문제 그림에 준선이 그려져 있지 않더라도 문제를 읽는 즉시 준선 엑스는 마이너스 피를 직접 긋고 수선의 발을 내려야 사다리꼴과 직각삼각형이 보입니다.", cap: "① 포물선 제1원칙: 준선 $x=-p$ 가 안 그려져 있으면 직접 긋고 시작!" },
      { say: "둘째, 초점을 지나는 직선이 에프에서 선분 에이비를 엠 대 엔으로 나누면 피 분의 일은 에이에프 분의 일 더하기 비에프 분의 일이라는 조화평균 공식이 성립합니다.", cap: "② 초점 현 조화비 공식: $\\dfrac{1}{\\overline{AF}}+\\dfrac{1}{\\overline{BF}}=\\dfrac{1}{p}$!" },
      { say: "셋째, 이차곡선의 기본 정의를 다룬 제오강과 함께 보면 포물선·타원·쌍곡선의 연결 고리가 한눈에 잡힙니다.", cap: "③ 제5강 이차곡선 정의 연계: 포물선(등거리) $\\to$ 타원(합 일정) $\\to$ 쌍곡선(차 일정)!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 타원과 쌍곡선의 초점삼각형과 점근선 성질을 다루는 제팔십구강입니다.", cap: "제89강 · 타원·쌍곡선 초점삼각형과 점근선 공식" },
      { tag: "연계 ②", say: "이차곡선 전체의 정의를 한눈에 비교하는 제오강도 함께 보세요.", cap: "제5강 · 이차곡선의 정의와 방정식" },
      { tag: "이 사이트", say: "이 사이트의 제팔십구강과 제오강을 이어서 보세요.", cap: "제89강 · 타원·쌍곡선 초점삼각형  /  제5강 · 이차곡선 정의" }
    ],
    nextLinks: [
      { lec: 89, label: "제89강 열기 (타원·쌍곡선 심화)" },
      { lec: 5, label: "제5강 열기 (이차곡선 정의)" },
      { lec: 90, label: "제90강 열기 (이차곡선 접선)" }
    ]
  },
  {
    lec: 89,
    title: "숏츠식 판서 미리보기 · 타원(r₁+r₂=2a)·쌍곡선(|r₁−r₂|=2a) 초점삼각형과 점근선",
    desc: "타원($r_{1}+r_{2}=2a,\\ c^{2}=a^{2}-b^{2}$)과 쌍곡선($|r_{1}-r_{2}|=2a,\\ c^{2}=a^{2}+b^{2}$)의 초점삼각형 피타고라스·코사인법칙 및 점근선 $y=\\pm\\frac{b}{a}x$ 를 정리합니다.",
    hookTitle: "타원·쌍곡선은 r₁, r₂ 연립방정식!", hookSub: "정의식(합·차 = 2a) 하나와 도형식(피타고라스·코사인) 하나면 끝!",
    hookSay: "타원과 쌍곡선 킬러 문제를 초점 거리 알원과 알투 두 글자로 세 줄 만에 푸는 초점삼각형 법칙, 바로 정리합니다.",
    hookCap: "타원·쌍곡선 초점삼각형과 점근선 · 30초 정리",
    whySay: "곡선 위의 점 피와 두 초점 에프, 에프프라임을 이으면 삼각형이 만들어지므로, 두 초점 거리를 알원과 알투로 놓으면 정의에서 식 하나, 직각삼각형이나 코사인법칙에서 식 하나가 나와 모든 길이가 구해집니다.",
    whyCap: "타원: $r_{1}+r_{2}=2a\\ (c^{2}=a^{2}-b^{2})$ · 쌍곡선: $|r_{1}-r_{2}|=2a\\ (c^{2}=a^{2}+b^{2})$",
    histTag: "케플러·뉴턴", histSay: "케플러가 행성 궤도가 태양을 한 초점으로 하는 타원임을 밝혔고, 뉴턴이 만유인력 법칙으로 타원·쌍곡선 궤도를 증명했습니다.",
    histCap: "케플러 행성 운동 제1법칙(타원 궤도)과 쌍곡선 점근선 $y=\\pm\\dfrac{b}{a}x$",
    fParts: [
      { say: "타원이나 쌍곡선 위의 점 피가 보이면 무조건 두 초점과 연결해 두 선분 길이를 알원, 알투라고 적고 합 또는 차가 이 에이라는 첫 번째 식을 세웁니다.", cap: "1단계(정의식): 타원은 $r_{1}+r_{2}=2a$, 쌍곡선은 $|r_{1}-r_{2}|=2a$" },
      { say: "초점삼각형 피에프에프프라임이 직각삼각형이면 알원 제곱 더하기 알투 제곱은 사 씨 제곱이라는 피타고라스 식과 곱셈공식을 연립해 넓이 이분의 일 알원 알투를 구합니다.", cap: "2단계(직각 초점삼각형): $r_{1}^{2}+r_{2}^{2}=(2c)^{2}=4c^{2}$ 과 곱셈공식 변형!" },
      { say: "쌍곡선 에이 제곱 분의 엑스 제곱 빼기 비 제곱 분의 와이 제곱은 일의 점근선은 와이는 플러스마이너스 에이 분의 비 엑스이며, 초점에서 점근선까지의 거리는 항상 비입니다.", cap: "쌍곡선 점근선: $y=\\pm\\dfrac{b}{a}x$ (초점 $F(c,0)$ 에서 점근선까지 거리 $=b$!)" }
    ],
    fChips: [
      "\\text{타원 }\\dfrac{x^{2}}{a^{2}}+\\dfrac{y^{2}}{b^{2}}=1:\\ r_{1}+r_{2}=2a,\\quad c^{2}=a^{2}-b^{2}",
      "\\text{쌍곡선 }\\dfrac{x^{2}}{a^{2}}-\\dfrac{y^{2}}{b^{2}}=1:\\ |r_{1}-r_{2}|=2a,\\ c^{2}=a^{2}+b^{2},\\ y=\\pm\\dfrac{b}{a}x",
      "\\angle FPF'=90^\\circ\\text{ 인 타원 초점삼각형 넓이 }S=\\dfrac{1}{2}r_{1}r_{2}=b^{2}"
    ],
    fLabels: ["합·차 = 2a 정의식 세우기", "직각 타원 초점삼각형 넓이 = b²"],
    exParts: [
      { say: "예를 들어 타원 구 분의 엑스 제곱 더하기 사 분의 와이 제곱은 일 위의 점 피와 두 초점 에프, 에프프라임에 대하여 각 에프피에프프라임이 구십도일 때 삼각형의 넓이를 구해 봅시다.", cap: "$\\dfrac{x^{2}}{9}+\\dfrac{y^{2}}{4}=1$ 에서 $\\angle FPF'=90^\\circ$ 일 때 $\\triangle FPF'$ 의 넓이" },
      { say: "알원 더하기 알투는 장축 길이 육이고, 씨 제곱은 구 빼기 사인 오이므로 빗변 제곱인 알원 제곱 더하기 알투 제곱은 사 씨 제곱, 이십입니다.", cap: "$r_{1}+r_{2}=6,\\quad r_{1}^{2}+r_{2}^{2}=4c^{2}=20$" },
      { say: "곱셈공식에 의해 이 알원 알투는 삼십육 빼기 이십인 십육이므로, 삼각형의 넓이 이분의 일 알원 알투는 사입니다.", cap: "$2r_{1}r_{2}=36-20=16\\ \\Rightarrow\\ S=\\dfrac{1}{2}r_{1}r_{2}=4\\ (=b^{2})$" }
    ],
    exChips: [
      "r_{1}+r_{2}=2a=6,\\qquad c^{2}=9-4=5\\implies r_{1}^{2}+r_{2}^{2}=4c^{2}=20",
      "2r_{1}r_{2}=(r_{1}+r_{2})^{2}-(r_{1}^{2}+r_{2}^{2})=36-20=16",
      "\\therefore\\ S=\\dfrac{1}{2}r_{1}r_{2}=4\\quad (=b^{2})"
    ],
    exLabels: ["r₁+r₂=6, r₁²+r₂²=20", "넓이 S = 4 (= b²)"],
    exGraph: {
      f: x => 1.5 * Math.sqrt(Math.max(0, 1 - 0.35 * (x - 1.5) * (x - 1.5))) + 0.25, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "초점 F'(−c, 0)" }, r2: { x: 2.4, col: PK, label: "초점 F(c, 0)" },
      fn: { t: "타원 직각 초점삼각형(∠FPF'=90°) 넓이 공식: S = b² = 4!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(36 − 20) / 4", finalS: "넓이 S = 4", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 쌍곡선 십육 분의 엑스 제곱 빼기 구 분의 와이 제곱은 일의 한 초점 에프에서 점근선에 내린 수선의 길이는 얼마일까요?", cap: "쌍곡선 $\\dfrac{x^{2}}{16}-\\dfrac{y^{2}}{9}=1$ 의 초점 $F$ 에서 점근선까지의 거리 (자작 문항)" },
      { say: "에이는 사, 비는 삼이므로 씨 제곱은 십육 더하기 구인 이십오, 초점은 오 콤마 영이고 점근선은 삼 엑스 빼기 사 와이는 영입니다.", cap: "$a=4,\\ b=3\\ \\Rightarrow\\ F(5,0)$, 점근선 $3x-4y=0$" },
      { say: "점과 직선 사이의 거리 공식을 쓰거나 초점·점근선 거리 성질 비를 쓰면 길이는 바로 삼입니다.", cap: "거리 $d=\\dfrac{|3\\cdot 5-0|}{\\sqrt{3^{2}+(-4)^{2}}}=\\dfrac{15}{5}=3\\ (=b)$" }
    ],
    examChips: [
      "a^{2}=16,\\ b^{2}=9\\ \\Longrightarrow\\ c=\\sqrt{16+9}=5,\\quad F(5,0)",
      "\\text{점근선 }y=\\pm\\dfrac{3}{4}x\\ \\Longleftrightarrow\\ 3x\\mp 4y=0",
      "\\text{거리 }d=\\dfrac{|3\\times 5|}{\\sqrt{3^{2}+4^{2}}}=\\dfrac{15}{5}=3\\quad (=b)"
    ],
    examLabels: ["초점 F(5,0), 점근선 3x−4y=0", "정답 거리 b = 3"],
    examGraph: {
      f: x => 0.65 * Math.sqrt(1 + 1.2 * (x - 1.5) * (x - 1.5)) + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "꼭짓점 a = 4" }, r2: { x: 2.3, col: GO, label: "점근선 거리 b = 3" },
      fn: { t: "쌍곡선 초점 F(c, 0) 에서 점근선까지 거리 = 무조건 b!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "15 / 5 = b", finalS: "3", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 타원에서 각 에프피에프프라임이 구십도인 직각 초점삼각형의 넓이는 계산할 필요도 없이 항상 단축 반지름의 제곱인 비 제곱입니다.", cap: "① 타원 직각 초점삼각형 넓이 1초 공식: $\\angle FPF'=90^\\circ\\ \\Longrightarrow\\ S=b^{2}$!" },
      { say: "둘째, 쌍곡선의 초점 에프에서 점근선에 수선의 발 에이치를 내리면 원점 오부터 에이치까지의 거리는 에이이고 에프부터 에이치까지의 거리는 비입니다.", cap: "② 쌍곡선 점근선 직각삼각형 $\\triangle OFH$: 빗변 $\\overline{OF}=c$, 밑변 $\\overline{OH}=a$, 높이 $\\overline{FH}=b$!" },
      { say: "셋째, 초점삼각형의 각이 특수각으로 주어지면 수학 원 제삼십강의 코사인법칙과 바로 결합됩니다.", cap: "③ 제30강 코사인법칙 결합: $(2c)^{2}=r_{1}^{2}+r_{2}^{2}-2r_{1}r_{2}\\cos\\theta$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 이차곡선의 접선의 방정식 3대 공식과 빛의 반사 성질을 다루는 제구십강입니다.", cap: "제90강 · 이차곡선 접선의 방정식과 광학적 반사 성질" },
      { tag: "연계 ②", say: "초점삼각형 풀이에 쓰이는 코사인법칙 제삼십강도 함께 보세요.", cap: "제30강 · 삼각함수 활용 코사인법칙 (수학 I)" },
      { tag: "이 사이트", say: "이 사이트의 제구십강과 제삼십강을 이어서 보세요.", cap: "제90강 · 이차곡선 접선 공식  /  제30강 · 코사인법칙" }
    ],
    nextLinks: [
      { lec: 90, label: "제90강 열기 (이차곡선 접선)" },
      { lec: 30, label: "제30강 열기 (코사인법칙)" },
      { lec: 88, label: "제88강 열기 (포물선 심화)" }
    ]
  },
  {
    lec: 90,
    title: "숏츠식 판서 미리보기 · 이차곡선 접선의 방정식 3대 공식과 광학적 반사 성질",
    desc: "포물선·타원·쌍곡선의 접점 $(x_{1},y_{1})$ 쪼개기 대입 공식과 기울기 $m$ 접선 공식($y=mx+\\frac{p}{m},\\ y=mx\\pm\\sqrt{a^{2}m^{2}\\pm b^{2}}$)을 정리합니다.",
    hookTitle: "이차곡선 접선 · 쪼개기 & 기울기 공식", hookSub: "접점은 x² → x₁x 로 쪼개고 · 기울기 m 은 공식에 바로 대입!",
    hookSay: "포물선, 타원, 쌍곡선 세 가지 접선의 방정식을 미분 없이 3초 만에 세우는 두 가지 만능 공식, 바로 정리합니다.",
    hookCap: "이차곡선 접선의 방정식 · 30초 정리",
    whySay: "음함수 미분법으로 구한 접선의 기울기를 정리하면 이차항 엑스 제곱을 엑스원 엑스로, 일차항 엑스를 이분의 엑스원 더하기 엑스로 바꾼 선형 변환식과 정확히 일치합니다.",
    whyCap: "접점 $(x_{1},y_{1})$ 공식: $x^{2}\\to x_{1}x,\\quad y^{2}\\to y_{1}y,\\quad x\\to\\dfrac{x_{1}+x}{2}$",
    histTag: "아폴로니오스·데카르트", histSay: "아폴로니오스는 원뿔곡선 접선이 축과 만나는 성질을 기하학적으로 증명했고, 초점에서 쏜 빛이 접선에서 반사되는 광학적 성질은 안테나와 망원경의 원리가 되었습니다.",
    histCap: "포물선 $x$절편 대칭($-x_{1},0$)과 이차곡선의 초점 반사 성질",
    fParts: [
      { say: "곡선 위의 접점 엑스원 콤마 와이원이 주어지면 제곱은 엑스원 엑스, 와이원 와이로 쪼개고 일차항 엑스는 이분의 엑스원 더하기 엑스로 바꿉니다.", cap: "접점 공식: 포물선 $y_{1}y=2p(x+x_{1})$, 타원·쌍곡선 $\\dfrac{x_{1}x}{a^{2}}\\pm\\dfrac{y_{1}y}{b^{2}}=1$" },
      { say: "기울기 엠이 주어지면 포물선은 와이는 엠 엑스 더하기 엠 분의 피이고, 타원과 쌍곡선은 와이는 엠 엑스 플러스마이너스 루트 에이 제곱 엠 제곱 플러스마이너스 비 제곱입니다.", cap: "기울기 $m$ 공식: 포물선 $y=mx+\\dfrac{p}{m}$, 타원·쌍곡선 $y=mx\\pm\\sqrt{a^{2}m^{2}\\pm b^{2}}$" },
      { say: "특히 포물선 위의 점 엑스원 콤마 와이원에서 그은 접선의 엑스절편은 항상 마이너스 엑스원이 되어 초점 에프를 중심으로 이등변삼각형(마름모)을 만듭니다.", cap: "포물선 접선 $x$절편 법칙: 접점 $(x_{1},y_{1})\\ \\Longrightarrow\\ x\\text{절편 }T(-x_{1},0)$ ($\\overline{FP}=\\overline{FT}=x_{1}+p$!)" }
    ],
    fChips: [
      "\\text{접점 }(x_{1},y_{1}):\\ y_{1}y=2p(x+x_{1}),\\qquad \\dfrac{x_{1}x}{a^{2}}\\pm\\dfrac{y_{1}y}{b^{2}}=1",
      "\\text{기울기 }m:\\ y=mx+\\dfrac{p}{m}\\ (\\text{포물선}),\\ y=mx\\pm\\sqrt{a^{2}m^{2}\\pm b^{2}}",
      "\\text{포물선 접선 }x\\text{절편 }T(-x_{1},0)\\ \\Longrightarrow\\ \\overline{FT}=x_{1}+p=\\overline{FP}\\ (\\text{이등변!})"
    ],
    fLabels: ["접점 쪼개기 & 기울기 공식", "포물선 접선 x절편 = −x₁"],
    exParts: [
      { say: "예를 들어 타원 오 분의 엑스 제곱 더하기 사 분의 와이 제곱은 일에 접하고 기울기가 일인 두 직선의 와이절편의 곱을 구해 봅시다.", cap: "$\\dfrac{x^{2}}{5}+\\dfrac{y^{2}}{4}=1$ 에 접하고 기울기 $m=1$ 인 두 접선의 $y$절편 곱" },
      { say: "에이 제곱이 오, 비 제곱이 사, 엠이 일이므로 루트 에이 제곱 엠 제곱 더하기 비 제곱은 루트 오 더하기 사, 삼입니다.", cap: "$y=1\\cdot x\\pm\\sqrt{5\\cdot 1^{2}+4}=x\\pm 3$" },
      { say: "따라서 두 와이절편은 플러스 삼과 마이너스 삼이므로 곱은 마이너스 구입니다.", cap: "$y\\text{절편 }3,\\ -3\\ \\Rightarrow\\ \\text{곱 }=-9$" }
    ],
    exChips: [
      "a^{2}=5,\\quad b^{2}=4,\\quad m=1",
      "y=mx\\pm\\sqrt{a^{2}m^{2}+b^{2}}=x\\pm\\sqrt{5(1)^{2}+4}=x\\pm 3",
      "\\text{두 }y\\text{절편의 곱 }=3\\times(-3)=-9"
    ],
    exLabels: ["y = x ± √(5 + 4) = x ± 3", "절편 곱 = −9"],
    exGraph: {
      f: x => 0.7 * x + 0.45, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "접선 y = x + 3" }, r2: { x: 2.3, col: PK, label: "접선 y = x − 3" },
      fn: { t: "타원 기울기 m 접선: y = mx ± √(a²m² + b²)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "y = x ± 3", finalS: "곱 = −9", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 포물선 와이 제곱은 팔 엑스 위의 점 삼 콤마 이 루트 육에서의 접선이 엑스축과 만나는 점을 티라 할 때, 초점 에프와 점 티 사이의 거리는 얼마일까요?", cap: "$y^{2}=8x$ 위 점 $P(3,2\\sqrt{6})$ 의 접선 $x$절편 $T$ 와 초점 $F$ 사이 거리 $\\overline{FT}$ (자작 문항)" },
      { say: "사 피가 팔이므로 초점 에프는 이 콤마 영이고, 접점의 엑스좌표가 삼이므로 접선의 엑스절편 티는 무조건 마이너스 삼 콤마 영입니다.", cap: "$F(2,0)$, 포물선 접선 $x$절편 성질로 $T(-3,0)$" },
      { say: "따라서 선분 에프티의 길이는 이 빼기 마이너스 삼, 오입니다.", cap: "$\\overline{FT}=2-(-3)=5\\ (=\\overline{FP}=x_{1}+p)$" }
    ],
    examChips: [
      "y^{2}=8x\\implies p=2,\\ F(2,0),\\quad \\text{접점 }x_{1}=3\\implies T(-3,0)",
      "\\overline{FT}=p-(-x_{1})=x_{1}+p=3+2",
      "=5"
    ],
    examLabels: ["T(−x₁, 0) = (−3, 0)", "정답 FT = 5"],
    examGraph: {
      f: x => Math.sqrt(Math.max(0, 1.35 * (x - 0.5))) + 0.25, GY0: 390, GV: 110, xr: [0.5, 3], area: [0.6, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "x절편 T(−x₁, 0)" }, r2: { x: 2.3, col: GO, label: "FT = FP = x₁+p = 5" },
      fn: { t: "포물선 접선 마름모 법칙: x절편 T(−x₁, 0) ⇒ FT = FP = x₁ + p!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "3 + 2", finalS: "FT = 5", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 타원 밖의 한 점에서 타원에 그은 두 접선이 서로 수직인 점들의 자취는 반지름이 루트 에이 제곱 더하기 비 제곱인 준원입니다.", cap: "① 수직 접선 자취(몬지의 원): 타원은 $x^{2}+y^{2}=a^{2}+b^{2}$, 쌍곡선은 $x^{2}+y^{2}=a^{2}-b^{2}$!" },
      { say: "둘째, 원의 접선 공식 엑스원 엑스 더하기 와이원 와이는 알 제곱을 다룬 공통수학 투 제오십육강과 똑같은 쪼개기 원리입니다.", cap: "② 제56강 원의 접선 직결: 모든 이차곡선 접점 공식은 $x^{2}\\to x_{1}x,\\ y^{2}\\to y_{1}y$!" },
      { say: "셋째, 음함수 미분법으로 접선 기울기를 직접 구하는 미적분 심화 제팔십일강도 함께 알아두면 공식을 잊어버려도 언제든 유도할 수 있습니다.", cap: "③ 제81강 음함수 미분 연계: $y^{2}=4px\\implies 2yy'=4p\\implies y'=\\dfrac{2p}{y_{1}}$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 기하의 두 번째 대단원인 평면벡터의 연산·일직선 조건과 자취 넓이를 다루는 제구십일강입니다.", cap: "제91강 · 평면벡터 분점·일직선 조건($\\alpha+\\beta=1$)과 자취 넓이" },
      { tag: "연계 ②", say: "원의 접선 방정식을 다루는 공통수학 투 제오십육강도 함께 보세요.", cap: "제56강 · 원과 직선의 위치관계와 접선 공식" },
      { tag: "이 사이트", say: "이 사이트의 제구십일강과 제오십육강을 이어서 보세요.", cap: "제91강 · 평면벡터와 자취  /  제56강 · 원의 접선 공식" }
    ],
    nextLinks: [
      { lec: 91, label: "제91강 열기 (평면벡터와 자취)" },
      { lec: 56, label: "제56강 열기 (원의 접선 공식)" },
      { lec: 81, label: "제81강 열기 (음함수 미분법)" }
    ]
  },
  {
    lec: 91,
    title: "숏츠식 판서 미리보기 · 평면벡터 분점·일직선 조건(α+β=1)과 종점 자취 넓이",
    desc: "위치벡터의 뺄셈 분해($\\overrightarrow{AB}=\\overrightarrow{OB}-\\overrightarrow{OA}$), 세 점 일직선 필요충분조건($\\alpha+\\beta=1$)과 종점 $P$ 의 영역 넓이 배율을 정리합니다.",
    hookTitle: "평면벡터 일직선 조건 α + β = 1", hookSub: "시점 통일 후 계수 합 = 1 이면 직선 AB · 부등식이면 삼각형 영역!",
    hookSay: "평면벡터에서 종점 피가 그리는 도형의 길이와 넓이를 그림을 복잡하게 그리지 않고 계수만 보고 3초 만에 푸는 법, 바로 정리합니다.",
    hookCap: "평면벡터 일직선 조건과 종점의 자취 · 30초 정리",
    whySay: "선분 에이비를 티 대 일 빼기 티로 내분하거나 외분하는 점 피의 위치벡터는 일 빼기 티 곱하기 오에이 더하기 티 곱하기 오비이므로, 두 계수의 합은 티가 어떤 값이든 항상 일입니다.",
    whyCap: "$\\overrightarrow{OP}=(1-t)\\overrightarrow{OA}+t\\overrightarrow{OB}\\ \\Longleftrightarrow\\ \\alpha+\\beta=1$ 이면 점 $P$ 는 직선 $AB$ 위!",
    histTag: "해밀턴·그라스만", histSay: "벡터 연산과 선형결합은 19세기 해밀턴과 그라스만이 기하학적 이동과 물리적 힘을 대수적으로 다루기 위해 창안했습니다.",
    histCap: "위치벡터 시점 통일($\\overrightarrow{AB}=\\vec{b}-\\vec{a}$)과 아핀 결합($\\alpha+\\beta=1$)",
    fParts: [
      { say: "시점이 제각각인 벡터가 나오면 뺄셈 공식 에이비 벡터는 오비 빼기 오에이를 써서 시점을 한 점으로 통일하거나, 반대로 덧셈으로 경유점을 합칩니다.", cap: "시점 통일 제1원칙: $\\overrightarrow{AB}=\\overrightarrow{OB}-\\overrightarrow{OA}$ (뒤종점 $-$ 앞시점!)" },
      { say: "오피 벡터는 알파 오에이 더하기 베타 오비에서 알파 더하기 베타가 일이면 직선 에이비이고, 알파와 베타가 모두 영 이상까지 붙으면 선분 에이비입니다.", cap: "일직선·선분 조건: $\\alpha+\\beta=1$ (직선 $AB$), $\\alpha+\\beta=1,\\ \\alpha,\\beta\\ge 0$ (선분 $AB$)" },
      { say: "알파 더하기 베타가 일 이하이고 알파, 베타가 영 이상이면 삼각형 오에이비 내부이며, 오에이·오비에 케이원, 케이투 배가 곱해지면 넓이도 케이원 곱하기 케이투 배가 됩니다.", cap: "영역 넓이 공식: $0\\le\\alpha,\\beta,\\ \\alpha+\\beta\\le 1\\ \\Longrightarrow\\ \\triangle OAB$ 내부!" }
    ],
    fChips: [
      "\\overrightarrow{OP}=\\alpha\\overrightarrow{OA}+\\beta\\overrightarrow{OB}:\\ \\alpha+\\beta=1\\iff P\\text{ 는 직선 }AB\\text{ 위의 점}",
      "\\alpha+\\beta=1\\ (\\alpha,\\beta\\ge 0)\\iff \\text{선분 }AB,\\ 0\\le\\alpha,\\beta\\le 1\\iff \\text{평행사변형}",
      "\\alpha+\\beta\\le k\\ (\\alpha,\\beta\\ge 0)\\ \\Longrightarrow\\ \\text{종점 }P\\text{ 의 영역 넓이 }=k^{2}\\cdot S_{\\triangle OAB}"
    ],
    fLabels: ["계수 합 α + β = 1 ⇒ 일직선", "α + β ≤ k ⇒ 넓이 k² 배"],
    exParts: [
      { say: "예를 들어 삼각형 오에이비의 넓이가 육일 때, 오피 벡터는 알파 오에이 더하기 베타 오비에서 알파, 베타가 영 이상이고 알파 더하기 베타가 이 이하인 점 피가 나타내는 영역의 넓이를 구해 봅시다.", cap: "$S_{\\triangle OAB}=6$ 이고 $\\alpha,\\beta\\ge 0,\\ \\alpha+\\beta\\le 2$ 일 때 점 $P$ 영역의 넓이" },
      { say: "알파 더하기 베타가 이 이하라는 조건은 양변을 이로 나누면 이분의 알파 더하기 이분의 베타가 일 이하이므로 두 변을 두 배 늘린 삼각형입니다.", cap: "$\\left(\\dfrac{\\alpha}{2}\\right)\\!(2\\overrightarrow{OA})+\\left(\\dfrac{\\beta}{2}\\right)\\!(2\\overrightarrow{OB})\\ \\Rightarrow\\ \\text{닮음비 }2\\text{배}$" },
      { say: "닮음비가 이배이므로 넓이는 사배가 되어 육 곱하기 사, 이십사입니다.", cap: "$\\text{넓이 }=2^{2}\\times 6=24$" }
    ],
    exChips: [
      "\\overrightarrow{OP}=\\alpha\\overrightarrow{OA}+\\beta\\overrightarrow{OB}=\\dfrac{\\alpha}{2}(2\\overrightarrow{OA})+\\dfrac{\\beta}{2}(2\\overrightarrow{OB})",
      "\\dfrac{\\alpha}{2}+\\dfrac{\\beta}{2}\\le 1\\quad (\\text{두 변이 }2\\text{배 확대된 삼각형 내부})",
      "\\text{넓이 }S=2^{2}\\times S_{\\triangle OAB}=4\\times 6=24"
    ],
    exLabels: ["닮음비 2배 → 넓이비 2² = 4배", "넓이 S = 24"],
    exGraph: {
      f: x => 1.8 - 0.65 * x, GY0: 390, GV: 110, xr: [0, 2.7], area: [0.2, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.2, col: CY, label: "α + β = 1 (선분 AB)" }, r2: { x: 2.4, col: PK, label: "α + β ≤ 2 (넓이 4배)" },
      fn: { t: "α + β ≤ k (α, β ≥ 0) ⇒ 삼각형 OAB 를 k 배 확대한 넓이 k²S!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "2² × 6", finalS: "넓이 = 24", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 평면 위의 서로 다른 세 점 에이, 비, 씨가 일직선 위에 있고 오씨 벡터가 삼분의 케이 오에이 더하기 오분의 이 오비일 때, 상수 케이의 값은 얼마일까요?", cap: "세 점 $A,B,C$ 가 일직선 위이고 $\\overrightarrow{OC}=\\dfrac{k}{3}\\overrightarrow{OA}+\\dfrac{2}{5}\\overrightarrow{OB}$ 일 때 $k$ (자작 문항)" },
      { say: "세 점이 한 직선 위에 있을 필요충분조건은 두 계수의 합이 일인 것입니다.", cap: "$\\dfrac{k}{3}+\\dfrac{2}{5}=1$" },
      { say: "삼분의 케이가 오분의 삼이므로 상수 케이는 오분의 구입니다.", cap: "$\\dfrac{k}{3}=\\dfrac{3}{5}\\ \\Rightarrow\\ k=\\dfrac{9}{5}$" }
    ],
    examChips: [
      "A,\\ B,\\ C\\text{ 가 일직선 위}\\ \\Longleftrightarrow\\ \\alpha+\\beta=1",
      "\\dfrac{k}{3}+\\dfrac{2}{5}=1\\ \\Longrightarrow\\ \\dfrac{k}{3}=\\dfrac{3}{5}",
      "\\therefore\\ k=\\dfrac{9}{5}"
    ],
    examLabels: ["계수 합 k/3 + 2/5 = 1", "정답 k = 9/5"],
    examGraph: {
      f: x => 1.5 - 0.45 * x, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "점 A" }, r2: { x: 2.3, col: GO, label: "α + β = 1 (직선 AB)" },
      fn: { t: "일직선 조건: 두 위치벡터 계수의 합 = 1 ⇔ k/3 + 2/5 = 1", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "k/3 = 3/5", finalS: "k = 9/5", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 이 피에이 벡터 더하기 삼 피비 벡터는 오 피씨 벡터처럼 점 피가 섞여 있는 식은 양변을 계수 합 오로 나누면 오분의 이 피에이 더하기 오분의 삼 피비가 내분점 벡터로 바로 바뀝니다.", cap: "① 내분점 합치기 마법: $m\\overrightarrow{PA}+n\\overrightarrow{PB}=(m+n)\\overrightarrow{PD}$ ($D$ 는 $AB$ 를 $n:m$ 내분점)!" },
      { say: "둘째, 삼각형 무게중심 조건은 피에이 더하기 피비 더하기 피씨 벡터가 영벡터인 것과 완전히 동치입니다.", cap: "② 무게중심 조건: $\\overrightarrow{PA}+\\overrightarrow{PB}+\\overrightarrow{PC}=\\vec{0}\\ \\Longleftrightarrow\\ P=G$ (무게중심)!" },
      { say: "셋째, 내분점과 무게중심의 좌표 공식은 공통수학 투 제오십이강과 일대일로 대응됩니다.", cap: "③ 제52강 내분·무게중심 직결: 좌표 공식이 그대로 위치벡터 공식!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 벡터 문제의 꽃인 평면벡터의 내적과 중점 분해 최대·최소를 다루는 제구십이강입니다.", cap: "제92강 · 평면벡터 내적의 정사영 의미와 중점 분해 공식" },
      { tag: "연계 ②", say: "내분점과 무게중심의 기하적 비율을 다루는 제오십이강도 함께 보세요.", cap: "제52강 · 내분점·외분점과 삼각형의 무게중심" },
      { tag: "이 사이트", say: "이 사이트의 제구십이강과 제오십이강을 이어서 보세요.", cap: "제92강 · 평면벡터 내적  /  제52강 · 내분점과 무게중심" }
    ],
    nextLinks: [
      { lec: 92, label: "제92강 열기 (평면벡터 내적)" },
      { lec: 52, label: "제52강 열기 (내분·무게중심)" },
      { lec: 93, label: "제93강 열기 (직선·원의 벡터)" }
    ]
  },
  {
    lec: 92,
    title: "숏츠식 판서 미리보기 · 평면벡터 내적의 정사영 의미와 중점 분해 공식",
    desc: "내적 $\\vec{a}\\cdot\\vec{b}=|\\vec{a}||\\vec{b}|\\cos\\theta=a_{1}b_{1}+a_{2}b_{2}$ 의 정사영 기하 해석과 중점 분해 공식 $\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=|\\overrightarrow{PM}|^{2}-\\frac{1}{4}\\overline{AB}^{2}$ 를 정리합니다.",
    hookTitle: "벡터 내적 · 정사영 곱 & 중점 M 분해!", hookSub: "PA · PB = |PM|² − (AB/2)² 로 바꾸면 동점 P 가 하나로 합쳐진다!",
    hookSay: "평면벡터 내적의 최대·최소 킬러 문제를 계산 없이 그림 하나로 3초 만에 푸는 정사영 법칙과 중점 분해 공식, 바로 정리합니다.",
    hookCap: "평면벡터의 내적과 최대·최소 · 30초 정리",
    whySay: "두 벡터의 내적에서 크기 곱하기 코사인 세타는 한 벡터를 다른 벡터의 직선 위로 수직으로 내린 그림자, 즉 정사영의 길이이므로 밑변 길이 곱하기 그림자 길이와 같습니다.",
    whyCap: "내적의 기하적 본질: $\\vec{a}\\cdot\\vec{b}=|\\vec{a}|\\cdot(|\\vec{b}|\\cos\\theta)=(\\text{기준 길이})\\times(\\text{정사영 길이})$",
    histTag: "깁스·헤비사이드", histSay: "벡터의 내적(Dot Product)은 19세기 말 물리학자 깁스와 헤비사이드가 힘과 이동거리의 곱인 일(Work)을 표현하기 위해 정립했습니다.",
    histCap: "물리학의 일($W=\\vec{F}\\cdot\\vec{s}$)과 중점 제곱차 항등식 $|\\overrightarrow{PM}|^{2}-\\dfrac{1}{4}\\overline{AB}^{2}$",
    fParts: [
      { say: "두 벡터가 모두 움직이지 않고 하나만 움직이면 고정된 벡터 위로 수선의 발을 내려 정사영 길이가 가장 길 때 최대, 반대 방향일 때 최소로 구합니다.", cap: "1법칙(정사영 해석): $\\overrightarrow{OA}\\cdot\\overrightarrow{OP}=\\overline{OA}\\times\\overline{OH}$ ($H$ 는 직선 $OA$ 위 수선의 발!)" },
      { say: "움직이는 점 피가 양쪽에 모두 들어 있는 피에이 내적 피비는 선분 에이비의 중점 엠을 경유점으로 끼워 넣으면 피엠 길이의 제곱 빼기 사분의 일 에이비 제곱이 됩니다.", cap: "2법칙(중점 분해): $\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=|\\overrightarrow{PM}|^{2}-\\dfrac{1}{4}\\overline{AB}^{2}$ ($M$ 은 $AB$ 의 중점!)" },
      { say: "원과 구가 없고 직각이 많이 보이면 주저하지 말고 원점을 잡아 성분 내적 엑스원 엑스투 더하기 와이원 와이투로 계산하는 것이 가장 빠릅니다.", cap: "3법칙(성분 내적): $\\vec{a}\\cdot\\vec{b}=a_{1}b_{1}+a_{2}b_{2},\\qquad \\vec{a}\\perp\\vec{b}\\iff \\vec{a}\\cdot\\vec{b}=0$" }
    ],
    fChips: [
      "\\vec{a}\\cdot\\vec{b}=|\\vec{a}||\\vec{b}|\\cos\\theta=a_{1}b_{1}+a_{2}b_{2}\\quad (\\vec{a}\\perp\\vec{b}\\iff \\vec{a}\\cdot\\vec{b}=0)",
      "\\text{정사영 해석: }\\overrightarrow{OA}\\cdot\\overrightarrow{OP}=\\overline{OA}\\cdot(\\overline{OP}\\cos\\theta)=\\pm\\overline{OA}\\cdot\\overline{OH}",
      "\\text{중점 분해: }\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=(\\overrightarrow{PM}+\\overrightarrow{MA})\\cdot(\\overrightarrow{PM}-\\overrightarrow{MA})=|\\overrightarrow{PM}|^{2}-\\dfrac{1}{4}\\overline{AB}^{2}"
    ],
    fLabels: ["기준 길이 × 정사영 길이", "PA·PB = |PM|² − (AB/2)²"],
    exParts: [
      { say: "예를 들어 길이가 사인 선분 에이비와 평면 위의 점 피에 대하여 피엠의 길이가 오일 때 피에이 내적 피비의 값을 구해 봅시다. 단, 엠은 에이비의 중점입니다.", cap: "$\\overline{AB}=4$, 중점 $M$ 에 대해 $\\overline{PM}=5$ 일 때 $\\overrightarrow{PA}\\cdot\\overrightarrow{PB}$ 의 값" },
      { say: "선분 에이비가 사이므로 반지름 격인 에이엠의 길이는 이입니다.", cap: "$\\dfrac{1}{2}\\overline{AB}=\\overline{AM}=2$" },
      { say: "중점 분해 공식에 의해 오의 제곱 빼기 이의 제곱이므로 이십일입니다.", cap: "$\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=5^{2}-2^{2}=25-4=21$" }
    ],
    exChips: [
      "\\overline{AB}=4\\ \\Longrightarrow\\ \\dfrac{1}{4}\\overline{AB}^{2}=\\overline{AM}^{2}=2^{2}=4",
      "\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=|\\overrightarrow{PM}|^{2}-\\overline{AM}^{2}",
      "=5^{2}-2^{2}=21"
    ],
    exLabels: ["|PM|² − AM² 공식 대입", "내적값 = 21"],
    exGraph: {
      f: x => 0.4 * (x - 1.2) * (x - 1.2) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.2, col: CY, label: "중점 M (최소 −AM²)" }, r2: { x: 2.4, col: PK, label: "PM 최대 → 내적 최대" },
      fn: { t: "PA · PB = |PM|² − AM² : 두 벡터에 흩어진 동점 P 를 PM 하나로 통합!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "5² − 2²", finalS: "21", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 한 변의 길이가 육인 정삼각형 에이비씨에서 변 비씨 위를 움직이는 점 피에 대하여 피에이 내적 피비의 최솟값은 얼마일까요?", cap: "한 변이 $6$ 인 정삼각형 $ABC$ 의 변 $BC$ 위 점 $P$ 에 대해 $\\overrightarrow{PA}\\cdot\\overrightarrow{PB}$ 의 최솟값 (자작 문항)" },
      { say: "선분 에이비의 중점을 엠이라 하면 피에이 내적 피비는 피엠 제곱 빼기 삼의 제곱, 즉 피엠 제곱 빼기 구입니다.", cap: "$\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=|\\overrightarrow{PM}|^{2}-3^{2}=|\\overrightarrow{PM}|^{2}-9$" },
      { say: "점 엠에서 변 비씨에 내린 수선의 길이는 삼 곱하기 사인 육십도인 이분의 삼 루트 삼이므로, 제곱한 사분의 이십칠에서 구를 빼면 최솟값은 마이너스 사분의 구입니다.", cap: "$\\min|\\overrightarrow{PM}|=3\\sin 60^\\circ=\\dfrac{3\\sqrt{3}}{2}\\ \\Rightarrow\\ \\dfrac{27}{4}-9=-\\dfrac{9}{4}$" }
    ],
    examChips: [
      "\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=|\\overrightarrow{PM}|^{2}-3^{2}=|\\overrightarrow{PM}|^{2}-9\\quad (M:\\ AB\\text{ 중점})",
      "\\min\\overline{PM}=\\overline{BM}\\sin 60^\\circ=3\\cdot\\dfrac{\\sqrt{3}}{2}\\implies \\min|\\overrightarrow{PM}|^{2}=\\dfrac{27}{4}",
      "\\therefore\\ \\text{최솟값 }=\\dfrac{27}{4}-9=-\\dfrac{9}{4}"
    ],
    examLabels: ["수선 길이 PM = 3√3 / 2", "정답 −9/4"],
    examGraph: {
      f: x => 0.45 * (x - 1.3) * (x - 1.3) + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.5, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.3, col: CY, label: "수선의 발 P (PM 최소)" }, r2: { x: 2.3, col: GO, label: "27/4 − 9 = −9/4" },
      fn: { t: "중점 M 에서 변 BC 까지 수선의 발일 때 |PM| 최소!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "27/4 − 9", finalS: "−9 / 4", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 원 위의 동점 피가 들어 있는 벡터는 무조건 원의 중심 씨를 경유점으로 쪼개어 피씨 벡터를 분리해 내면 반지름으로 크기가 고정됩니다.", cap: "① 원 위의 점 $P$ 제1원칙: 무조건 원의 중심 $C$ 를 끼워 넣어 $\\overrightarrow{OP}=\\overrightarrow{OC}+\\overrightarrow{CP}$ 분해!" },
      { say: "둘째, 피에이 내적 피비가 영이라는 식이 나오면 각 에이피비가 구십도이므로 점 피는 선분 에이비를 지름으로 하는 원 위에 있습니다.", cap: "② 지름의 원 조건: $\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=0\\ \\Longleftrightarrow\\ \\angle APB=90^\\circ$ ($AB$ 가 지름인 원)!" },
      { say: "셋째, 원의 성질과 원주각 구십도를 다루는 제삼십오강, 제오십오강과 함께 보면 도형 해석이 완벽해집니다.", cap: "③ 제35·55강 연계: 내적 $=0$ 은 곧 직각(탈레스 반원 원주각 $90^\\circ$)!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 직선의 방향벡터·법선벡터와 원의 벡터방정식을 다루는 제구십삼강입니다.", cap: "제93강 · 직선의 벡터방정식과 원의 벡터방정식" },
      { tag: "연계 ②", say: "원의 성질과 지름 원주각을 다루는 제삼십오강도 함께 보세요.", cap: "제35강 · 원의 성질 총정리 (기하 기본기)" },
      { tag: "이 사이트", say: "이 사이트의 제구십삼강과 제삼십오강을 이어서 보세요.", cap: "제93강 · 직선·원의 벡터방정식  /  제35강 · 원의 성질" }
    ],
    nextLinks: [
      { lec: 93, label: "제93강 열기 (직선·원 벡터방정식)" },
      { lec: 35, label: "제35강 열기 (원의 성질 총정리)" },
      { lec: 91, label: "제91강 열기 (평면벡터와 자취)" }
    ]
  },
  {
    lec: 93,
    title: "숏츠식 판서 미리보기 · 직선의 벡터방정식(방향·법선)과 원의 벡터방정식",
    desc: "직선의 방향벡터 $\\vec{u}=(u_{1},u_{2})$·법선벡터 $\\vec{n}=(a,b)$ 와 두 직선이 이루는 각 $\\cos\\theta=\\frac{|\\vec{u}_{1}\\cdot\\vec{u}_{2}|}{|\\vec{u}_{1}||\\vec{u}_{2}|}$, 원의 벡터방정식 2가지를 정리합니다.",
    hookTitle: "방향벡터 · 법선벡터 & 원의 벡터방정식", hookSub: "분모는 방향벡터 (u₁, u₂) · 계수는 법선벡터 (a, b)!",
    hookSay: "직선과 원의 벡터방정식을 일반 도형의 방정식으로 1초 만에 번역하는 방법, 바로 정리합니다.",
    hookCap: "직선과 원의 벡터방정식 · 30초 정리",
    whySay: "직선과 평행한 방향벡터 유와 직선에 수직인 법선벡터 엔을 이용하면 기울기가 무한대인 수직선까지 예외 없이 하나의 내적 방정식으로 깔끔하게 표현할 수 있습니다.",
    whyCap: "방향벡터 $\\vec{u}=(u_{1},u_{2})\\implies\\dfrac{x-x_{1}}{u_{1}}=\\dfrac{y-y_{1}}{u_{2}}$, 법선벡터 $\\vec{n}=(a,b)\\implies ax+by+c=0$",
    histTag: "데카르트·기브스", histSay: "데카르트의 해석기하학 방정식을 기브스의 벡터 내적 기호로 재해석하면서 2차원과 3차원 직선·평면·구의 공식이 하나로 통일되었습니다.",
    histCap: "직선의 방향·법선벡터와 원의 두 벡터방정식 $|\\vec{p}-\\vec{c}|=r,\\ (\\vec{p}-\\vec{a})\\cdot(\\vec{p}-\\vec{b})=0$",
    fParts: [
      { say: "유원 분의 엑스 빼기 엑스원은 유투 분의 와이 빼기 와이원 꼴에서 분모에 적힌 유원 콤마 유투가 바로 직선과 평행한 방향벡터이고, 기울기는 유원 분의 유투입니다.", cap: "방향벡터: $\\dfrac{x-x_{1}}{u_{1}}=\\dfrac{y-y_{1}}{u_{2}}\\ \\Longrightarrow\\ \\vec{u}=(u_{1},u_{2})$, 기울기 $m=\\dfrac{u_{2}}{u_{1}}$" },
      { say: "일반형 직선 에이 엑스 더하기 비 와이 더하기 씨는 영에서 엑스와 와이의 계수 에이 콤마 비는 직선에 수직인 법선벡터입니다.", cap: "법선벡터: $ax+by+c=0\\ \\Longrightarrow\\ \\vec{n}=(a,b)\\perp\\text{직선}$" },
      { say: "원의 벡터방정식은 중심과 반지름을 알려주는 피 빼기 씨의 크기는 알 꼴과, 양 끝점 에이, 비를 지름으로 하는 피 빼기 에이 내적 피 빼기 비는 영 꼴 두 가지입니다.", cap: "원의 벡터방정식: ① $|\\vec{p}-\\vec{c}|=r$ (중심 $C$, 반지름 $r$) · ② $(\\vec{p}-\\vec{a})\\cdot(\\vec{p}-\\vec{b})=0$ ($AB$ 가 지름)" }
    ],
    fChips: [
      "\\dfrac{x-x_{1}}{u_{1}}=\\dfrac{y-y_{1}}{u_{2}}\\implies \\vec{u}=(u_{1},u_{2}),\\ ax+by+c=0\\implies \\vec{n}=(a,b)",
      "\\text{두 직선이 이루는 예각: }\\cos\\theta=\\dfrac{|\\vec{u}_{1}\\cdot\\vec{u}_{2}|}{|\\vec{u}_{1}||\\vec{u}_{2}|}=\\dfrac{|\\vec{n}_{1}\\cdot\\vec{n}_{2}|}{|\\vec{n}_{1}||\\vec{n}_{2}|}",
      "|\\vec{p}-\\vec{c}|=r\\ (\\text{중심 }C,\\text{ 반지름 }r),\\quad (\\vec{p}-\\vec{a})\\cdot(\\vec{p}-\\vec{b})=0\\ (AB\\text{ 지름 원})"
    ],
    fLabels: ["분모 = 방향벡터, 계수 = 법선벡터", "원의 벡터방정식 2가지"],
    exParts: [
      { say: "예를 들어 두 직선 이 분의 엑스 빼기 일은 일 분의 와이 더하기 삼과 삼 분의 엑스는 마이너스 일 분의 와이 빼기 이가 이루는 예각의 크기 세타를 구해 봅시다.", cap: "$\\dfrac{x-1}{2}=\\dfrac{y+3}{1}$ 과 $\\dfrac{x}{3}=\\dfrac{y-2}{-1}$ 이 이루는 예각 $\\theta$" },
      { say: "두 직선의 방향벡터는 이 콤마 일과 삼 콤마 마이너스 일이므로 크기는 각각 루트 오와 루트 십이고 내적은 육 빼기 일인 오입니다.", cap: "$\\vec{u}_{1}=(2,1),\\ \\vec{u}_{2}=(3,-1)\\ \\Rightarrow\\ \\vec{u}_{1}\\cdot\\vec{u}_{2}=6-1=5$" },
      { say: "코사인 세타가 오 루트 이 분의 오, 즉 루트 이 분의 일이므로 예각 세타는 사분의 파이입니다.", cap: "$\\cos\\theta=\\dfrac{5}{\\sqrt{5}\\sqrt{10}}=\\dfrac{1}{\\sqrt{2}}\\ \\Rightarrow\\ \\theta=\\dfrac{\\pi}{4}$" }
    ],
    exChips: [
      "\\vec{u}_{1}=(2,1),\\quad \\vec{u}_{2}=(3,-1)\\ \\Longrightarrow\\ |\\vec{u}_{1}|=\\sqrt{5},\\ |\\vec{u}_{2}|=\\sqrt{10}",
      "\\cos\\theta=\\dfrac{|2\\cdot 3+1\\cdot(-1)|}{\\sqrt{5}\\cdot\\sqrt{10}}=\\dfrac{5}{5\\sqrt{2}}=\\dfrac{1}{\\sqrt{2}}",
      "\\therefore\\ \\theta=\\dfrac{\\pi}{4}\\quad (45^\\circ)"
    ],
    exLabels: ["내적 5 / (√5·√10) = 1/√2", "예각 θ = π/4"],
    exGraph: {
      f: x => 0.5 * x + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "방향벡터 u₁ = (2, 1)" }, r2: { x: 2.2, col: PK, label: "방향벡터 u₂ = (3, −1)" },
      fn: { t: "두 직선의 각: cos θ = |u₁ · u₂| / (|u₁||u₂|)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "cos θ = 1/√2", finalS: "θ = π/4", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 좌표평면 위의 두 점 에이 일 콤마 이, 비 오 콤마 유에 대하여 위치벡터 피가 피 빼기 에이 내적 피 빼기 비는 영을 만족할 때, 점 피가 나타내는 도형의 넓이는 얼마일까요?", cap: "$A(1,2),\\ B(5,6)$ 에 대해 $(\\vec{p}-\\vec{a})\\cdot(\\vec{p}-\\vec{b})=0$ 인 점 $P$ 도형의 넓이 (자작 문항)" },
      { say: "피 빼기 에이 내적 피 빼기 비는 영이므로 점 피는 선분 에이비를 지름으로 하는 원입니다.", cap: "$\\overrightarrow{AP}\\perp\\overrightarrow{BP}\\ \\Rightarrow\\ \\text{선분 }AB\\text{ 를 지름으로 하는 원}$" },
      { say: "지름 에이비의 길이가 사 루트 이이므로 반지름 알은 이 루트 이이고, 원의 넓이는 파이 알 제곱인 팔 파이입니다.", cap: "$\\overline{AB}=\\sqrt{4^{2}+4^{2}}=4\\sqrt{2}\\ \\Rightarrow\\ r=2\\sqrt{2}\\ \\Rightarrow\\ S=8\\pi$" }
    ],
    examChips: [
      "(\\vec{p}-\\vec{a})\\cdot(\\vec{p}-\\vec{b})=0\\ \\Longleftrightarrow\\ \\text{선분 }AB\\text{ 를 지름으로 하는 원}",
      "\\text{지름 }\\overline{AB}=\\sqrt{(5-1)^{2}+(6-2)^{2}}=4\\sqrt{2}\\ \\Longrightarrow\\ r=2\\sqrt{2}",
      "\\text{원의 넓이 }S=\\pi r^{2}=8\\pi"
    ],
    examLabels: ["지름 AB = 4√2 → r = 2√2", "정답 넓이 8π"],
    examGraph: {
      f: x => 1.45 * Math.sqrt(Math.max(0, 1 - (x - 1.5) * (x - 1.5))) + 0.3, GY0: 390, GV: 110, xr: [0.5, 2.5], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "A(1, 2)" }, r2: { x: 2.4, col: GO, label: "B(5, 6) (지름 4√2)" },
      fn: { t: "(p − a) · (p − b) = 0 ⇔ 선분 AB 를 지름으로 하는 원!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "π × (2√2)²", finalS: "8π", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 분수 꼴 직선의 방정식에서는 분자의 엑스와 와이 앞의 계수가 반드시 플러스 일로 정리되어 있어야 분모가 진짜 방향벡터가 됩니다.", cap: "① 함정 주의: $\\dfrac{2-x}{3}=\\dfrac{y-1}{4}$ 는 $\\dfrac{x-2}{-3}=\\dfrac{y-1}{4}$ 로 고쳐야 $\\vec{u}=(-3,4)$!" },
      { say: "둘째, 두 직선이 이루는 각을 구할 때 탄젠트 세타가 필요하면 미적분 심화 제칠십구강의 덧셈정리를 쓰고, 코사인 세타가 필요하면 벡터 내적을 쓰면 됩니다.", cap: "② 제79강 연결: $\\tan\\theta$ 는 기울기 덧셈정리, $\\cos\\theta$ 는 방향벡터 내적!" },
      { say: "셋째, 지름의 양 끝점으로 원을 세우는 공통수학 투 제오십오강과 완전히 같은 구조입니다.", cap: "③ 제55강 원의 방정식 직결: $(x-x_{1})(x-x_{2})+(y-y_{1})(y-y_{2})=0$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 기하의 세 번째 대단원인 공간도형의 평면 결정 조건과 꼬인 위치의 각을 다루는 제구십사강입니다.", cap: "제94강 · 공간도형 평면 결정 조건과 꼬인 위치의 두 직선이 이루는 각" },
      { tag: "연계 ②", say: "지름의 양 끝점으로 원의 방정식을 세우는 제오십오강도 함께 보세요.", cap: "제55강 · 원의 방정식과 아폴로니우스의 원" },
      { tag: "이 사이트", say: "이 사이트의 제구십사강과 제오십오강을 이어서 보세요.", cap: "제94강 · 공간도형과 꼬인 위치  /  제55강 · 원의 방정식" }
    ],
    nextLinks: [
      { lec: 94, label: "제94강 열기 (공간도형·꼬인위치)" },
      { lec: 55, label: "제55강 열기 (원의 방정식)" },
      { lec: 79, label: "제79강 열기 (두 직선의 각 tan θ)" }
    ]
  }
];


const GEOADV_SPECS_B = [
  {
    lec: 94,
    title: "숏츠식 판서 미리보기 · 공간도형 평면 결정 조건 4가지와 꼬인 위치의 각",
    desc: "공간에서 평면을 하나로 결정하는 4가지 조건과 꼬인 위치에 있는 두 직선이 이루는 각(평행이동 교차 후 코사인법칙)을 정리합니다.",
    hookTitle: "평면 결정 4조건 & 꼬인 위치의 각", hookSub: "만나지 않는 꼬인 두 직선은 한 직선을 평행이동해 붙여 놓고 푼다!",
    hookSay: "공간도형의 출발점인 평면 결정 조건 네 가지와 꼬인 위치의 두 직선이 이루는 각을 구하는 법, 30초 만에 정리합니다.",
    hookCap: "평면 결정 조건과 꼬인 위치의 각 · 30초 정리",
    whySay: "공간에서 만나지도 않고 평행하지도 않은 꼬인 위치의 두 직선은 그 상태로는 각을 잴 수 없으므로, 한 직선을 평행이동해 다른 직선과 한 점에서 만나게 만든 뒤 평면 삼각형으로 풀어야 합니다.",
    whyCap: "꼬인 위치 두 직선 $l, m$: $m$ 을 평행이동한 $m'$ 과 $l$ 이 한 점에서 만날 때 이루는 예각 $\\theta$!",
    histTag: "유클리드 원론 11권", histSay: "고대 그리스 유클리드는 원론 제11권에서 평면기하학을 3차원 입체기하학으로 확장하며 평면의 결정 조건과 공간 직선의 위치관계를 공리화했습니다.",
    histCap: "유클리드 입체기하학 공리와 꼬인 위치(Skew Lines)의 평행이동 각 정의",
    fParts: [
      { say: "공간에서 단 하나의 평면을 결정하는 조건은 한 직선 위에 있지 않은 세 점, 한 직선과 그 밖의 한 점, 한 점에서 만나는 두 직선, 평행한 두 직선 네 가지입니다.", cap: "평면 결정 4조건: ① 비일직선 3점 · ② 직선 + 외부 1점 · ③ 교차 2직선 · ④ 평행 2직선" },
      { say: "반면 꼬인 위치에 있는 두 직선은 아무리 연장해도 한 평면 위에 놓일 수 없으므로 평면을 결정하지 못합니다.", cap: "함정 1순위: 꼬인 위치의 두 직선은 평면을 결정할 수 없다!" },
      { say: "꼬인 위치의 두 모서리가 이루는 각의 코사인값은 정육면체나 정사면체에서 보조선으로 한 모서리를 평행이동해 삼각형을 만든 뒤 코사인법칙으로 구합니다.", cap: "꼬인 위치 각 풀이: ① 평행한 모서리로 이동 $\\to$ ② 삼각형 세 변 길이 구하기 $\\to$ ③ 코사인법칙!" }
    ],
    fChips: [
      "\\text{평면 결정 4조건: 비일직선 3점, 직선+외부점, 교차 2직선, 평행 2직선}",
      "\\text{공간 두 직선: 한 점 교차·평행 }(1\\text{평면})\\text{ vs 꼬인 위치 (평면 불가)}",
      "\\text{정사면체 마주 보는 꼬인 두 모서리가 이루는 각 }\\theta=90^\\circ\\ (\\text{수직!})"
    ],
    fLabels: ["꼬인 위치는 평행이동해 교차시키기", "정사면체 마주 보는 모서리 = 90°"],
    exParts: [
      { say: "예를 들어 정육면체 에이비씨디 이에프지에이치에서 꼬인 위치에 있는 모서리 에이비와 대각선 비지가 이루는 각이 아니라 에이비와 에프에이치가 이루는 예각의 크기를 구해 봅시다.", cap: "정육면체에서 꼬인 위치의 모서리 $AB$ 와 밑면 대각선 $FH$ 가 이루는 예각 $\\theta$" },
      { say: "모서리 에이비를 아래 밑면으로 평행이동하면 모서리 이에프와 겹쳐지므로 각 에이에프에이치 대신 각 이에프에이치를 구하면 됩니다.", cap: "$AB \\parallel EF\\ \\Rightarrow\\ \\angle(AB,FH)=\\angle EFH$" },
      { say: "밑면은 정사각형이고 에프에이치는 정사각형의 대각선이므로 이루는 각은 사십오도입니다.", cap: "정사각형 대각선 각 $\\theta=45^\\circ\\ \\left(\\dfrac{\\pi}{4}\\right)$" }
    ],
    exChips: [
      "\\text{정육면체에서 }AB \\parallel EF\\text{ 이므로 }AB\\text{ 를 }EF\\text{ 로 평행이동}",
      "\\text{꼬인 두 직선 }AB,\\ FH\\text{ 가 이루는 각 }=\\angle EFH",
      "\\triangle EFH\\text{ 는 직각이등변삼각형}\\ \\Longrightarrow\\ \\theta=45^\\circ"
    ],
    exLabels: ["AB 를 EF 로 평행이동", "예각 θ = 45°"],
    exGraph: {
      f: x => 1.2 + 0.35 * Math.cos(1.1 * x), GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "평행이동 AB → EF" }, r2: { x: 2.3, col: PK, label: "교차각 ∠EFH = 45°" },
      fn: { t: "꼬인 위치 각: 평행한 모서리로 옮겨 한 점에서 만나게 만든다!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "∠EFH (1:1:√2)", finalS: "θ = 45°", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 한 모서리의 길이가 이인 정사면체 에이비씨디에서 모서리 에이비의 중점을 엠이라 할 때, 꼬인 위치의 직선 씨엠과 에이디가 이루는 예각 세타에 대하여 코사인 세타의 값은 얼마일까요?", cap: "한 변 $2$ 인 정사면체 $ABCD$ 에서 $AB$ 중점 $M$ 에 대해 $CM$ 과 $AD$ 가 이루는 예각 $\\cos\\theta$ (자작 문항)" },
      { say: "비디의 중점을 엔이라 하면 중점연결정리에 의해 엠엔은 에이디와 평행하고 길이는 일입니다.", cap: "$BD$ 중점 $N$ 잡기 $\\Rightarrow\\ MN\\parallel AD,\\ \\overline{MN}=1,\\ \\overline{CM}=\\overline{CN}=\\sqrt{3}$" },
      { say: "삼각형 씨엠엔에서 변의 길이가 루트 삼, 일, 루트 삼이므로 코사인 세타는 이 곱하기 루트 삼 곱하기 일 분의 삼 더하기 일 빼기 삼, 육분의 루트 삼입니다.", cap: "$\\cos\\theta=\\dfrac{(\\sqrt{3})^{2}+1^{2}-(\\sqrt{3})^{2}}{2\\cdot\\sqrt{3}\\cdot 1}=\\dfrac{1}{2\\sqrt{3}}=\\dfrac{\\sqrt{3}}{6}$" }
    ],
    examChips: [
      "BD\\text{ 의 중점 }N:\\ MN\\parallel AD\\implies \\overline{MN}=1,\\quad \\overline{CM}=\\overline{CN}=\\sqrt{3}",
      "\\triangle CMN\\text{ 에서 코사인법칙: }\\cos\\theta=\\dfrac{3+1-3}{2\\cdot\\sqrt{3}\\cdot 1}",
      "=\\dfrac{1}{2\\sqrt{3}}=\\dfrac{\\sqrt{3}}{6}"
    ],
    examLabels: ["중점연결정리 MN ∥ AD", "정답 √3 / 6"],
    examGraph: {
      f: x => 1.35 - 0.25 * (x - 1.5) * (x - 1.5), GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "중점 N (MN = 1)" }, r2: { x: 2.3, col: GO, label: "cos θ = √3 / 6" },
      fn: { t: "중점이 보이면 다른 모서리의 중점 N 을 잡아 중점연결정리로 평행이동!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "1 / (2√3)", finalS: "√3 / 6", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 정사면체에서 마주 보는 두 모서리는 항상 서로 수직이므로 이루는 각이 구십도이고 코사인값은 영입니다.", cap: "① 정사면체 필수 상식: 마주 보는 꼬인 두 모서리는 무조건 수직($90^\\circ$)!" },
      { say: "둘째, 모서리의 중점이 등장하는 꼬인 위치 문제는 이웃한 모서리의 중점을 찍어 중점연결정리로 절반 길이 평행선을 만드는 것이 정석입니다.", cap: "② 중점 문제 필승법: 중점 $M$ 이 보이면 보조 중점 $N$ 을 찍어 $MN\\parallel AD$ 생성!" },
      { say: "셋째, 삼각형 세 변이 구해지면 수학 원 제삼십강의 코사인법칙으로 바로 마무리됩니다.", cap: "③ 제30강 코사인법칙 연계: 공간 각도 문제의 마지막 줄은 늘 코사인법칙!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 공간도형 킬러 문제의 핵심 도구인 삼수선의 정리를 다루는 제구십오강입니다.", cap: "제95강 · 직선·평면 수직 조건과 삼수선의 정리 3유형" },
      { tag: "연계 ②", say: "세 변의 길이로 코사인값을 구하는 제삼십강도 함께 보세요.", cap: "제30강 · 삼각함수 활용 코사인법칙 (수학 I)" },
      { tag: "이 사이트", say: "이 사이트의 제구십오강과 제삼십강을 이어서 보세요.", cap: "제95강 · 삼수선의 정리  /  제30강 · 코사인법칙" }
    ],
    nextLinks: [
      { lec: 95, label: "제95강 열기 (삼수선의 정리)" },
      { lec: 30, label: "제30강 열기 (코사인법칙)" },
      { lec: 96, label: "제96강 열기 (이면각과 정사면체)" }
    ]
  },
  {
    lec: 95,
    title: "숏츠식 판서 미리보기 · 직선·평면 수직 조건과 삼수선의 정리 3유형 해법",
    desc: "직선과 평면의 수직 조건($l\\perp\\alpha$)과 삼수선의 정리 3가지 유형($PO\\perp\\alpha,\\ OH\\perp l\\iff PH\\perp l$)을 이용한 입체 피타고라스 해법을 정리합니다.",
    hookTitle: "삼수선의 정리 · 직각 2개면 3번째도 직각!", hookSub: "바닥 수선 PO ⊥ α · 바닥 직각 OH ⊥ l · 빗면 직각 PH ⊥ l!",
    hookSay: "복잡한 3차원 공간도형 문제를 단 두 번의 피타고라스 정리로 끝내는 삼수선의 정리, 30초 만에 정리합니다.",
    hookCap: "직선·평면 수직과 삼수선의 정리 · 30초 정리",
    whySay: "평면 밖의 점 피에서 평면에 내린 수선 피오, 그 발 오에서 평면 위의 직선 엘에 내린 수선 오에이치, 그리고 점 피와 에이치를 이은 선분 피에이치 세 수선 중 두 개가 수직이면 나머지 하나도 자동으로 수직이 됩니다.",
    whyCap: "삼수선의 정리: ① $PO\\perp\\alpha,\\ OH\\perp l\\implies PH\\perp l$ · ② $PO\\perp\\alpha,\\ PH\\perp l\\implies OH\\perp l$",
    histTag: "유클리드·몽주", histSay: "삼수선의 정리는 유클리드 입체기하학에서 출발해 18세기 가스파르 몽주의 화법기하학에서 공간 수직 투영의 핵심 원리로 정립되었습니다.",
    histCap: "직선·평면 수직($l\\perp\\alpha$)과 삼수선의 정리(Theorem of Three Perpendiculars)",
    fParts: [
      { say: "직선 엘이 평면 알파와 수직이려면 평면 안의 평행하지 않은 서로 다른 두 직선과 수직이면 충분하고, 일단 수직이 되면 평면 위의 모든 직선과 수직입니다.", cap: "직선·평면 수직: $l$ 이 $\\alpha$ 위의 교차하는 두 직선과 수직 $\\Longrightarrow\\ l\\perp\\alpha$" },
      { say: "삼수선의 정리는 공중 수선 피오, 바닥 수선 오에이치, 빗면 수선 피에이치 세 개가 직각삼각형 피오에이치를 이루므로 피타고라스 정리를 두 번 연속 쓰는 문제입니다.", cap: "삼수선 계산 공식: 바닥에서 $\\overline{OH}$ 구하기 $\\longrightarrow\\ \\overline{PH}=\\sqrt{\\overline{PO}^{2}+\\overline{OH}^{2}}$" },
      { say: "특히 세 번째 유형은 바닥 직선 엘에 수직인 두 선분 피에이치와 오에이치가 만나고 피오가 바닥의 또 다른 직선과 수직일 때 비로소 피오가 평면 전체와 수직이 된다는 점을 주의해야 합니다.", cap: "제3유형 주의점: $PH\\perp l,\\ OH\\perp l$ 만으로는 $PO\\perp l$ 뿐! ($PO\\perp\\alpha$ 이려면 바닥 직선 1개 더 수직 필요)" }
    ],
    fChips: [
      "PO\\perp\\alpha\\text{ 일 때: }OH\\perp l\\iff PH\\perp l\\quad (\\text{삼수선 제1·2유형})",
      "\\text{제3유형: }PH\\perp l,\\ OH\\perp l,\\ PO\\perp OH\\implies PO\\perp\\alpha",
      "\\text{피타고라스 연쇄: }\\overline{PH}^{2}=\\overline{PO}^{2}+\\overline{OH}^{2}\\quad (\\angle POH=90^\\circ)"
    ],
    fLabels: ["직각 2개 → 3번째 직각 자동 완성", "PH² = PO² + OH²"],
    exParts: [
      { say: "예를 들어 평면 알파 밖의 점 피에서 평면에 내린 수선의 발 오까지의 거리가 사이고, 오에서 평면 위의 직선 엘까지의 거리가 삼일 때, 점 피에서 직선 엘까지의 거리를 구해 봅시다.", cap: "$\\overline{PO}=4,\\ \\overline{OH}=3$ 일 때 점 $P$ 에서 직선 $l$ 까지의 거리 $\\overline{PH}$" },
      { say: "삼수선의 정리에 의해 선분 피에이치가 바로 직선 엘과 수직을 이루는 최단거리입니다.", cap: "$PO\\perp\\alpha,\\ OH\\perp l\\ \\Rightarrow\\ PH\\perp l$" },
      { say: "직각삼각형 피오에이치에서 삼 대 사 대 오 피타고라스 정리를 쓰면 피에이치의 길이는 오입니다.", cap: "$\\overline{PH}=\\sqrt{4^{2}+3^{2}}=5$" }
    ],
    exChips: [
      "PO\\perp\\alpha,\\quad OH\\perp l\\ \\Longrightarrow\\ PH\\perp l\\quad (\\text{삼수선의 정리})",
      "\\triangle POH\\text{ 에서 }\\angle POH=90^\\circ",
      "\\overline{PH}=\\sqrt{\\overline{PO}^{2}+\\overline{OH}^{2}}=\\sqrt{4^{2}+3^{2}}=5"
    ],
    exLabels: ["바닥 OH = 3, 높이 PO = 4", "빗면 수선 PH = 5"],
    exGraph: {
      f: x => 1.5 - 0.45 * x, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "수선의 발 O (PO = 4)" }, r2: { x: 2.3, col: PK, label: "직선 위 발 H (OH = 3)" },
      fn: { t: "삼수선의 정리: 공간 거리 PH = √(PO² + OH²) = √(4² + 3²) = 5", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "√(16 + 9)", finalS: "PH = 5", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 각 오가 모두 구십도인 사면체 오에이비씨에서 오에이는 십오, 오비는 이십, 오씨는 구일 때, 꼭짓점 씨에서 모서리 에이비에 내린 수선의 길이는 얼마일까요?", cap: "$OA,OB,OC$ 가 서로 수직이고 $\\overline{OA}=15,\\ \\overline{OB}=20,\\ \\overline{OC}=9$ 일 때 $C$ 에서 $AB$ 까지 거리 (자작 문항)" },
      { say: "바닥 직각삼각형 오에이비에서 빗변 에이비는 이십오이고, 넓이 소 공식을 쓰면 오에서 에이비에 내린 수선 오에이치의 길이는 십이입니다.", cap: "$\\overline{AB}=25,\\quad \\overline{OH}=\\dfrac{15\\times 20}{25}=12$" },
      { say: "삼수선의 정리에 의해 구하는 길이 씨에이치는 루트 구의 제곱 더하기 십이의 제곱, 정답은 십오입니다.", cap: "$\\overline{CH}=\\sqrt{9^{2}+12^{2}}=15$" }
    ],
    examChips: [
      "\\overline{OA}=15,\\ \\overline{OB}=20\\implies \\overline{AB}=25,\\quad \\overline{OH}=\\dfrac{15\\times 20}{25}=12",
      "\\text{삼수선의 정리: }CO\\perp\\text{바닥},\\ OH\\perp AB\\implies CH\\perp AB",
      "\\overline{CH}=\\sqrt{\\overline{OC}^{2}+\\overline{OH}^{2}}=\\sqrt{9^{2}+12^{2}}=15"
    ],
    examLabels: ["소 공식 OH = 12, 높이 OC = 9", "정답 CH = 15"],
    examGraph: {
      f: x => 1.55 - 0.45 * x, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "바닥 소 공식 OH = 12" }, r2: { x: 2.3, col: GO, label: "삼수선 CH = 15" },
      fn: { t: "1단계: 바닥 소 공식(OH = ab/c) → 2단계: 삼수선 피타고라스(CH = √(OC²+OH²))", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "√(9² + 12²)", finalS: "CH = 15", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 삼수선의 정리는 항상 바닥 평면에서 직각삼각형의 소 공식이나 닮음으로 오에이치를 먼저 구하고, 세워진 직각삼각형에서 피에이치를 구하는 2단계로 풀립니다.", cap: "① 삼수선 표준 루틴: 1단계 바닥에서 $\\overline{OH}$ 구하기 $\\to$ 2단계 공중에서 $\\overline{PH}$ 구하기!" },
      { say: "둘째, 다음 강의에서 배울 두 평면이 이루는 각인 이면각의 코사인값은 바로 이 삼수선 직각삼각형의 빗변 분의 밑변, 피에이치 분의 오에이치입니다.", cap: "② 제96강 이면각 직결: 삼수선 삼각형 $\\triangle POH$ 의 $\\angle PHO=\\theta$ 가 곧 이면각!" },
      { say: "셋째, 바닥에서 오에이치를 구할 때 쓰이는 직각삼각형 소 공식과 사선식은 제삼십사강 중학도형 총정리에서 바로 복습할 수 있습니다.", cap: "③ 제34강 중학도형 연계: 직각삼각형 높이 $h=\\dfrac{ab}{c}$ (소 공식) 필수 활용!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 삼수선의 정리를 그대로 이어받아 두 평면이 이루는 각을 구하는 이면각 제구십육강입니다.", cap: "제96강 · 이면각의 정의와 정사면체·정팔면체 이면각" },
      { tag: "연계 ②", say: "직각삼각형 소 공식과 닮음을 다루는 제삼십사강도 함께 보세요.", cap: "제34강 · 중학도형 총정리 (기하 기본기)" },
      { tag: "이 사이트", say: "이 사이트의 제구십육강과 제삼십사강을 이어서 보세요.", cap: "제96강 · 이면각과 정사면체  /  제34강 · 중학도형 총정리" }
    ],
    nextLinks: [
      { lec: 96, label: "제96강 열기 (이면각과 정사면체)" },
      { lec: 34, label: "제34강 열기 (중학도형 총정리)" },
      { lec: 97, label: "제97강 열기 (정사영 S'=S cos θ)" }
    ]
  },
  {
    lec: 96,
    title: "숏츠식 판서 미리보기 · 이면각의 정의(교선 수선)와 정사면체·정팔면체 이면각",
    desc: "두 평면의 교선 $l$ 에 내린 두 수선이 이루는 이면각 $\\theta\\ (\\cos\\theta=\\frac{\\overline{OH}}{\\overline{PH}})$ 와 정사면체($\\cos\\theta=\\frac{1}{3}$), 정팔면체의 이면각 공식을 정리합니다.",
    hookTitle: "이면각 cos θ & 정사면체 1/3 법칙", hookSub: "교선에 내린 두 수선의 각 · 정사면체 이면각 cos θ = 무조건 1/3!",
    hookSay: "공간도형에서 두 평면이 이루는 이면각의 코사인을 3초 만에 구하는 정의법과 정사면체 3분의 1 법칙, 바로 정리합니다.",
    hookCap: "이면각의 정의와 정다면체 이면각 · 30초 정리",
    whySay: "두 평면이 만나는 교선 위의 한 점에서 각 평면을 따라 교선에 수직인 반직선을 그었을 때 두 수선이 이루는 각이 이면각이며, 삼수선의 정리를 쓰면 직각삼각형의 빗변 분의 밑변이 됩니다.",
    whyCap: "이면각 정의: 교선 $l$ 에 동시에 수직인 $PH\\perp l,\\ OH\\perp l$ 이 이루는 각 $\\theta\\ \\left(\\cos\\theta=\\dfrac{\\overline{OH}}{\\overline{PH}}\\right)$",
    histTag: "플라톤 입체와 유클리드", histSay: "정사면체와 정팔면체 등 5가지 플라톤 정다면체의 면과 면이 이루는 각은 유클리드 원론의 마지막 제13권에서 심도 있게 다루어졌습니다.",
    histCap: "플라톤 정다면체(정사면체 $\\cos\\theta=\\dfrac{1}{3}$, 정팔면체 $\\cos\\theta=-\\dfrac{1}{3}$)",
    fParts: [
      { say: "이면각을 구하는 정석은 삼수선의 정리로 교선에 수선의 발 에이치를 내려 직각삼각형 피오에이치를 만든 뒤 피에이치 분의 오에이치를 읽는 것입니다.", cap: "1법칙(삼수선 직각삼각형): $\\cos\\theta=\\dfrac{\\overline{OH}}{\\overline{PH}}$ (빗면 수선 분의 바닥 수선!)" },
      { say: "수선의 발이 한 점에서 안 만나고 어긋나 있으면 코사인법칙이 아니라 다음 강의의 정사영 넓이 공식 에스 분의 에스프라임으로 구합니다.", cap: "2법칙(넓이 비 활용): 두 삼각형이 교선을 공유하면 $\\cos\\theta=\\dfrac{h_{2}}{h_{1}}=\\dfrac{S_{2}}{S_{1}}$" },
      { say: "정사면체의 두 면이 이루는 이면각의 코사인은 항상 삼분의 일이고, 모서리와 밑면이 이루는 각의 코사인은 루트 삼분의 일입니다.", cap: "정사면체 필수 암기: 면과 면 $\\cos\\theta=\\dfrac{1}{3}$, 모서리와 면 $\\cos\\alpha=\\dfrac{1}{\\sqrt{3}}=\\dfrac{\\sqrt{3}}{3}$!" }
    ],
    fChips: [
      "\\text{이면각 정의: }PH\\perp l,\\ OH\\perp l\\text{ 일 때 }\\theta=\\angle PHO\\quad \\left(\\cos\\theta=\\dfrac{\\overline{OH}}{\\overline{PH}}\\right)",
      "\\text{정사면체: 면-면 }\\cos\\theta=\\dfrac{1}{3},\\ \\text{모서리-면 }\\cos\\alpha=\\dfrac{1}{\\sqrt{3}},\\ h=\\dfrac{\\sqrt{6}}{3}a",
      "\\text{정사각뿔(모서리 }a\\text{): }\\cos\\theta=\\dfrac{1}{\\sqrt{3}},\\quad \\text{정팔면체 예각 }\\cos\\theta=\\dfrac{1}{3}"
    ],
    fLabels: ["cos θ = OH / PH (삼수선)", "정사면체 이면각 cos θ = 1/3"],
    exParts: [
      { say: "예를 들어 한 모서리의 길이가 이인 정사면체 에이비씨디에서 옆면 에이비씨와 밑면 비씨디가 이루는 이면각 세타의 코사인값을 구해 봅시다.", cap: "한 변이 $2$ 인 정사면체에서 두 면이 이루는 이면각 $\\cos\\theta$ 유도" },
      { say: "교선 비씨의 중점을 엠이라 하면 빗면 높이 에이엠은 루트 삼이고, 꼭짓점 에이에서 밑면에 내린 수선의 발 지는 무게중심이므로 지엠은 에이엠의 삼분의 일입니다.", cap: "$\\overline{AM}=\\sqrt{3},\\quad G\\text{ 는 무게중심}\\ \\Rightarrow\\ \\overline{GM}=\\dfrac{1}{3}\\overline{AM}=\\dfrac{\\sqrt{3}}{3}$" },
      { say: "따라서 코사인 세타는 에이엠 분의 지엠이므로 삼분의 일입니다.", cap: "$\\cos\\theta=\\dfrac{\\overline{GM}}{\\overline{AM}}=\\dfrac{1}{3}$" }
    ],
    exChips: [
      "BC\\text{ 의 중점 }M:\\ AM\\perp BC,\\ DM\\perp BC\\quad (\\overline{AM}=\\overline{DM}=\\sqrt{3})",
      "\\text{수선의 발 }G\\text{ 는 }\\triangle BCD\\text{ 의 무게중심}\\implies \\overline{GM}=\\dfrac{1}{3}\\overline{DM}=\\dfrac{\\sqrt{3}}{3}",
      "\\cos\\theta=\\dfrac{\\overline{GM}}{\\overline{AM}}=\\dfrac{1}{3}"
    ],
    exLabels: ["무게중심 2:1 내분 → GM = AM/3", "cos θ = 1/3"],
    exGraph: {
      f: x => 1.5 - 0.45 * x, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "무게중심 G (GM = 1)" }, r2: { x: 2.3, col: PK, label: "교선 중점 M (AM = 3)" },
      fn: { t: "정사면체 수선의 발 = 밑면 무게중심 G (2:1) ⇒ cos θ = 1/3!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "GM / AM", finalS: "cos θ = 1/3", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 밑면이 한 변의 길이가 육인 정사각형이고 옆면이 모두 한 변의 길이가 육인 정삼각형인 정사각뿔에서 옆면과 밑면이 이루는 각 세타에 대하여 코사인 제곱 세타의 값은 얼마일까요?", cap: "모든 모서리가 $6$ 인 정사각뿔에서 옆면과 밑면의 이면각에 대해 $\\cos^{2}\\theta$ (자작 문항)" },
      { say: "옆면 정삼각형의 높이는 삼 루트 삼이고, 꼭짓점에서 밑면 정사각형 중심에 내린 수선의 발부터 밑변 중점까지의 거리는 삼입니다.", cap: "빗면 수선 $\\overline{PM}=3\\sqrt{3}$, 바닥 수선 $\\overline{OM}=3$" },
      { say: "코사인 세타가 삼 루트 삼 분의 삼, 즉 루트 삼분의 일이므로 제곱하면 삼분의 일입니다.", cap: "$\\cos\\theta=\\dfrac{3}{3\\sqrt{3}}=\\dfrac{1}{\\sqrt{3}}\\ \\Rightarrow\\ \\cos^{2}\\theta=\\dfrac{1}{3}$" }
    ],
    examChips: [
      "\\text{옆면 정삼각형 높이 }\\overline{PM}=6\\cdot\\dfrac{\\sqrt{3}}{2}=3\\sqrt{3},\\quad \\text{바닥 중심까지 }\\overline{OM}=3",
      "\\cos\\theta=\\dfrac{\\overline{OM}}{\\overline{PM}}=\\dfrac{3}{3\\sqrt{3}}=\\dfrac{1}{\\sqrt{3}}",
      "\\therefore\\ \\cos^{2}\\theta=\\dfrac{1}{3}"
    ],
    examLabels: ["OM = 3, PM = 3√3", "정답 cos²θ = 1/3"],
    examGraph: {
      f: x => 1.5 - 0.45 * x, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "바닥 OM = 3" }, r2: { x: 2.3, col: GO, label: "빗면 PM = 3√3" },
      fn: { t: "모든 모서리가 같은 정사각뿔: cos θ = 3 / (3√3) = 1/√3 ⇒ cos²θ = 1/3", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(1 / √3)²", finalS: "1 / 3", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 정사면체 두 개를 붙이면 정팔면체의 옆면 각도가 되므로, 정팔면체의 이웃한 두 면이 이루는 둔각의 코사인은 마이너스 삼분의 일이고 예각의 코사인은 플러스 삼분의 일입니다.", cap: "① 정팔면체 이면각 암기: 이웃한 두 면의 둔각 $\\cos(\\pi-\\theta)=-\\dfrac{1}{3}$ (예각은 $\\dfrac{1}{3}$)!" },
      { say: "둘째, 정사면체의 높이 삼분의 루트 육 에이와 부피 십이분의 루트 이 에이 세제곱은 외워 두면 수능 시험장에서 3분을 아껴 줍니다.", cap: "② 정사면체 3종 세트: $\\cos\\theta=\\dfrac{1}{3},\\quad h=\\dfrac{\\sqrt{6}}{3}a,\\quad V=\\dfrac{\\sqrt{2}}{12}a^{3}$!" },
      { say: "셋째, 구해 놓은 이면각 코사인 세타에 원래 도형 넓이를 곱하면 바로 다음 강의인 정사영 넓이가 됩니다.", cap: "③ 제97강 정사영 직결: 이면각 $\\cos\\theta$ 를 구하는 이유는 $S'=S\\cos\\theta$ 에 넣기 위함!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 이면각의 코사인을 그대로 활용해 그림자의 넓이를 구하는 정사영 제구십칠강입니다.", cap: "제97강 · 정사영의 길이·넓이($S'=S\\cos\\theta$)와 태양광선 그림자" },
      { tag: "연계 ②", say: "이면각 작도의 기초인 삼수선의 정리 제구십오강도 함께 보세요.", cap: "제95강 · 삼수선의 정리 3유형 해법" },
      { tag: "이 사이트", say: "이 사이트의 제구십칠강과 제구십오강을 이어서 보세요.", cap: "제97강 · 정사영과 그림자 넓이  /  제95강 · 삼수선의 정리" }
    ],
    nextLinks: [
      { lec: 97, label: "제97강 열기 (정사영과 그림자)" },
      { lec: 95, label: "제95강 열기 (삼수선의 정리)" },
      { lec: 52, label: "제52강 열기 (삼각형 무게중심)" }
    ]
  },
  {
    lec: 97,
    title: "숏츠식 판서 미리보기 · 정사영의 길이·넓이(S'=S cos θ)와 태양광선 그림자",
    desc: "정사영의 길이($l'=l\\cos\\theta$)와 정사영의 넓이($S'=S\\cos\\theta$), 경사면이나 비스듬한 태양광선에 의한 그림자 넓이 역산 공식을 정리합니다.",
    hookTitle: "정사영 S' = S cos θ & 비스듬한 빛 그림자", hookSub: "수직 그림자는 S cos θ · 비스듬한 빛은 빛에 수직인 평면을 경유!",
    hookSay: "공간도형 수능 단골 문항인 정사영의 넓이와 비스듬하게 비추는 태양광선의 그림자 넓이 공식, 30초 만에 정리합니다.",
    hookCap: "정사영의 길이·넓이와 그림자 · 30초 정리",
    whySay: "두 평면의 교선과 평행한 가로 길이는 정사영을 내려도 변하지 않고 교선과 수직인 세로 높이만 코사인 세타 배로 줄어들기 때문에, 어떤 평면도형이든 넓이도 정확히 코사인 세타 배가 됩니다.",
    whyCap: "가로 불변 · 세로 $\\cos\\theta$ 배 $\\Longrightarrow\\ S'=S\\cos\\theta$ (원·삼각형·다각형 모두 성립!)",
    histTag: "몽주 화법기하학", histSay: "정사영(Orthogonal Projection) 넓이 불변 비 법칙은 프랑스 수학자 가스파르 몽주가 건축과 공학 설계도를 그리는 화법기하학을 창시하며 확립했습니다.",
    histCap: "화법기하학의 수직 투영($S'=S\\cos\\theta$)과 코사인 역산($\\cos\\theta=\\dfrac{S'}{S}$)",
    fParts: [
      { say: "직선과 평면이 이루는 각이 알파일 때 선분의 정사영 길이는 엘 코사인 알파이고, 두 평면이 이루는 각이 세타일 때 도형의 정사영 넓이는 에스 코사인 세타입니다.", cap: "정사영 기본 공식: 길이 $l'=l\\cos\\alpha$, 넓이 $S'=S\\cos\\theta$" },
      { say: "반대로 교선에 수선을 내리기 어려운 두 평면의 이면각 코사인 세타는 원래 넓이 에스 분의 정사영 넓이 에스프라임으로 역산할 수 있습니다.", cap: "이면각 역산 공식: $\\cos\\theta=\\dfrac{S'}{S}$ (복잡한 수선 작도 없이 넓이 비로 끝!)" },
      { say: "빛이 바닥에 수직이 아니라 비스듬하게 비출 때는 빛과 수직인 가상 평면을 징검다리로 두면, 원래 도형 넓이에 코사인 알파를 곱한 값과 바닥 그림자 넓이에 코사인 베타를 곱한 값이 같습니다.", cap: "비스듬한 빛 그림자 법칙: $S\\cos\\alpha=S_{\\text{그림자}}\\cos\\beta\\ \\Longrightarrow\\ S_{\\text{그림자}}=\\dfrac{S\\cos\\alpha}{\\cos\\beta}$" }
    ],
    fChips: [
      "l'=l\\cos\\alpha\\ (\\text{선분-평면 각 }\\alpha),\\qquad S'=S\\cos\\theta\\ (\\text{평면-평면 이면각 }\\theta)",
      "\\text{이면각 역산: }\\cos\\theta=\\dfrac{S'}{S}\\quad (\\text{수선의 발 찾기 힘들 때 넓이 비로 계산!})",
      "\\text{비스듬한 빛: }S_{\\text{빛수직}}=S\\cos\\alpha=S_{\\text{그림자}}\\cos\\beta\\implies S_{\\text{그림자}}=S\\dfrac{\\cos\\alpha}{\\cos\\beta}"
    ],
    fLabels: ["정사영 넓이 S' = S cos θ", "비스듬한 빛 S cos α = S' cos β"],
    exParts: [
      { say: "예를 들어 한 변의 길이가 사인 정사면체 에이비씨디에서 삼각형 에이비씨의 평면 비씨디 위로의 정사영의 넓이를 구해 봅시다.", cap: "한 변이 $4$ 인 정사면체에서 $\\triangle ABC$ 의 밑면 $BCD$ 위 정사영 넓이 $S'$" },
      { say: "한 변이 사인 정삼각형의 넓이 에스는 사분의 루트 삼 곱하기 십육인 사 루트 삼이고, 정사면체의 이면각 코사인 세타는 삼분의 일입니다.", cap: "$S=\\dfrac{\\sqrt{3}}{4}\\cdot 4^{2}=4\\sqrt{3},\\qquad \\cos\\theta=\\dfrac{1}{3}$" },
      { say: "따라서 정사영의 넓이 에스프라임은 사 루트 삼 곱하기 삼분의 일, 삼분의 사 루트 삼입니다.", cap: "$S'=S\\cos\\theta=\\dfrac{4\\sqrt{3}}{3}$" }
    ],
    exChips: [
      "S=\\dfrac{\\sqrt{3}}{4}\\times 4^{2}=4\\sqrt{3},\\qquad \\text{정사면체 이면각 }\\cos\\theta=\\dfrac{1}{3}",
      "S'=S\\cos\\theta=4\\sqrt{3}\\times\\dfrac{1}{3}",
      "=\\dfrac{4\\sqrt{3}}{3}"
    ],
    exLabels: ["S = 4√3, cos θ = 1/3", "정사영 넓이 = 4√3 / 3"],
    exGraph: {
      f: x => 1.55 * Math.cos(0.45 * x), GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "원래 넓이 S = 4√3" }, r2: { x: 2.3, col: PK, label: "정사영 S' = S cos θ" },
      fn: { t: "정사면체 한 면의 밑면 위 정사영 넓이 = (1/3)S = 4√3 / 3", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "4√3 × (1/3)", finalS: "4√3 / 3", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 지면과 육십도의 각을 이루는 평면 위에 반지름의 길이가 사인 원판이 놓여 있을 때, 지면에 수직으로 비추는 태양광선에 의해 지면에 생기는 그림자의 넓이는 얼마일까요?", cap: "지면과 $60^\\circ$ 를 이루는 평면 위 반지름 $4$ 인 원의 수직 정사영 넓이 (자작 문항)" },
      { say: "원판의 넓이 에스는 파이 곱하기 사의 제곱인 십육 파이입니다.", cap: "$S=\\pi\\times 4^{2}=16\\pi$" },
      { say: "지면과 이루는 각이 육십도이고 빛이 지면에 수직이므로 정사영 공식에 의해 십육 파이 곱하기 코사인 육십도, 정답은 팔 파이입니다.", cap: "$S'=16\\pi\\cos 60^\\circ=16\\pi\\times\\dfrac{1}{2}=8\\pi$" }
    ],
    examChips: [
      "\\text{원판의 넓이 }S=\\pi r^{2}=\\pi\\times 4^{2}=16\\pi,\\qquad \\theta=60^\\circ",
      "S'=S\\cos 60^\\circ=16\\pi\\times\\dfrac{1}{2}",
      "=8\\pi"
    ],
    examLabels: ["16π × cos 60°", "정답 8π"],
    examGraph: {
      f: x => 1.45 * Math.sqrt(Math.max(0, 1 - 0.5 * (x - 1.5) * (x - 1.5))) + 0.3, GY0: 390, GV: 110, xr: [0.3, 2.7], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "원판 S = 16π" }, r2: { x: 2.4, col: GO, label: "타원 그림자 S' = 8π" },
      fn: { t: "반지름 a 인 원을 θ 만큼 기울인 정사영 = 장축 a, 단축 a cos θ 인 타원!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "16π × (1/2)", finalS: "8π", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 반지름이 에이인 원을 세타만큼 기울여 정사영을 내리면 장축 반지름은 에이로 그대로이고 단축 반지름만 에이 코사인 세타로 줄어든 타원이 됩니다.", cap: "① 원의 정사영 = 타원: 타원의 넓이 공식 $S=\\pi a(a\\cos\\theta)=\\pi ab$ 유도 원리!" },
      { say: "둘째, 구 전체를 평면에 정사영 내리면 어느 각도에서 빛을 비추든 단면 최대 원인 대원의 넓이 파이 알 제곱이 그대로 나옵니다.", cap: "② 구의 정사영 주의: 구는 입체이므로 평면 위 정사영이 항상 대원 넓이 $\\pi R^{2}$!" },
      { say: "셋째, 선분의 정사영 길이를 구할 때는 평면의 이면각 세타가 아니라 그 선분과 평면이 직접 이루는 각 알파를 써야 한다는 함정을 조심하세요.", cap: "③ 함정 1순위: 넓이는 항상 이면각 $\\theta$ 를 쓰지만, 선분 길이는 선분-평면 각 $\\alpha$ 사용!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 공간도형에 좌표를 입혀 대칭이동과 최단거리를 구하는 공간좌표 제구십팔강입니다.", cap: "제98강 · 공간좌표 대칭·내분·무게중심과 대칭이동 최단거리" },
      { tag: "연계 ②", say: "정사영 공식에 넣을 이면각 코사인을 구하는 제구십육강도 함께 보세요.", cap: "제96강 · 이면각의 정의와 정사면체·정팔면체 이면각" },
      { tag: "이 사이트", say: "이 사이트의 제구십팔강과 제구십육강을 이어서 보세요.", cap: "제98강 · 공간좌표와 최단거리  /  제96강 · 이면각" }
    ],
    nextLinks: [
      { lec: 98, label: "제98강 열기 (공간좌표·최단거리)" },
      { lec: 96, label: "제96강 열기 (이면각과 정사면체)" },
      { lec: 89, label: "제89강 열기 (타원 성질 연결)" }
    ]
  },
  {
    lec: 98,
    title: "숏츠식 판서 미리보기 · 공간좌표 대칭·내분·무게중심과 대칭이동 최단거리",
    desc: "공간좌표 $(x,y,z)$ 의 좌표축·좌표평면 수선의 발과 대칭이동 부호 규칙, 내분점·무게중심 및 평면 경유 최단거리($\\overline{AP}+\\overline{BP}\\ge\\overline{A'B}$)를 정리합니다.",
    hookTitle: "공간좌표 수선의 발·대칭 & 최단거리", hookSub: "언급된 문자만 남기면 수선의 발 · 언급 안 된 문자의 부호를 바꾸면 대칭이동!",
    hookSay: "공간좌표에서 엑스와이 평면, 엑스축에 내린 수선의 발과 대칭이동을 1초 만에 헷갈리지 않고 구하는 규칙, 바로 정리합니다.",
    hookCap: "공간좌표 대칭·분점과 최단거리 · 30초 정리",
    whySay: "평면좌표의 피타고라스 정리를 한 번 더 적용하면 두 점 사이의 거리는 루트 디엑스 제곱 더하기 디와이 제곱 더하기 디제트 제곱이 되며, 내분점과 무게중심 공식도 제트좌표 한 줄만 그대로 추가됩니다.",
    whyCap: "공간 두 점 거리 $d=\\sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}+(z_{2}-z_{1})^{2}}$, 무게중심 $G\\left(\\dfrac{\\sum x}{3},\\dfrac{\\sum y}{3},\\dfrac{\\sum z}{3}\\right)$",
    histTag: "오렘·데카르트·클레로", histSay: "데카르트의 2차원 좌표를 18세기 클레로와 오일러가 3차원 공간좌표(x, y, z)로 확장하면서 입체도형을 방정식으로 다룰 수 있게 되었습니다.",
    histCap: "3차원 직교좌표계 $(x,y,z)$ 와 좌표평면 거울 반사 최단거리",
    fParts: [
      { say: "수선의 발은 문제에서 부른 문자만 그대로 두고 안 부른 문자를 영으로 만들면 되고, 대칭이동은 부른 문자는 그대로 두고 안 부른 문자의 부호만 반대로 바꾸면 됩니다.", cap: "$xy$평면($x,y$ 부름): 수선의 발 $(a,b,0)$, 대칭점 $(a,b,-c)$ · $x$축 대칭점 $(a,-b,-c)$!" },
      { say: "점 피에서 좌표축까지의 거리는 안 부른 두 좌표의 제곱합에 루트를 씌운 값이고, 좌표평면까지의 거리는 안 부른 한 좌표의 절댓값입니다.", cap: "점 $(a,b,c)$ 거리: $xy$평면까지 $|c|$, $x$축까지 $\\sqrt{b^{2}+c^{2}}$!" },
      { say: "두 점 에이, 비에서 좌표평면 위의 점 피를 거쳐 가는 에이피 더하기 비피의 최단거리는 한 점을 그 좌표평면에 대칭이동한 점 에이프라임과 비를 직선으로 이은 길이입니다.", cap: "평면 경유 최단거리: $\\min(\\overline{AP}+\\overline{BP})=\\overline{A'B}$ ($A'$ 은 평면 대칭점!)" }
    ],
    fChips: [
      "P(a,b,c)\\text{ 와 }xy\\text{평면: 수선의 발 }(a,b,0),\\ \\text{대칭점 }(a,b,-c),\\ \\text{거리 }|c|",
      "P(a,b,c)\\text{ 와 }x\\text{축: 발 }(a,0,0),\\ \\text{대칭점 }(a,-b,-c),\\ \\text{거리 }\\sqrt{b^{2}+c^{2}}",
      "\\text{평면 위 점 }P\\text{ 경유 최단거리: }\\min(\\overline{AP}+\\overline{BP})=\\overline{A'B}"
    ],
    fLabels: ["안 부른 문자: 발은 0, 대칭은 부호 반대", "최단거리 = 대칭점 직선 연결"],
    exParts: [
      { say: "예를 들어 공간의 두 점 에이 일 콤마 이 콤마 삼과 비 오 콤마 유 콤마 일 및 엑스와이 평면 위의 점 피에 대하여 에이피 더하기 비피의 최솟값을 구해 봅시다.", cap: "$A(1,2,3),\\ B(5,6,1)$ 과 $xy$평면 위 점 $P$ 에 대해 $\\overline{AP}+\\overline{BP}$ 의 최솟값" },
      { say: "점 에이를 엑스와이 평면에 대칭이동한 점 에이프라임은 제트좌표의 부호만 바뀐 일 콤마 이 콤마 마이너스 삼입니다.", cap: "$A(1,2,3)\\xrightarrow{xy\\text{평면 대칭}}A'(1,2,-3)$" },
      { say: "선분 에이프라임 비의 길이는 루트 십육 더하기 십육 더하기 십육, 사 루트 삼입니다.", cap: "$\\overline{A'B}=\\sqrt{4^{2}+4^{2}+4^{2}}=4\\sqrt{3}$" }
    ],
    exChips: [
      "A(1,2,3)\\text{ 의 }xy\\text{평면 대칭점 }A'(1,2,-3)",
      "\\min(\\overline{AP}+\\overline{BP})=\\overline{A'B}=\\sqrt{(5-1)^{2}+(6-2)^{2}+(1-(-3))^{2}}",
      "=\\sqrt{16+16+16}=4\\sqrt{3}"
    ],
    exLabels: ["xy평면 대칭 A'(1, 2, −3)", "최솟값 = 4√3"],
    exGraph: {
      f: x => 0.55 * Math.sqrt(1 + (x - 1.4) * (x - 1.4)) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "대칭점 A'(1, 2, −3)" }, r2: { x: 2.3, col: PK, label: "직선 거리 A'B = 4√3" },
      fn: { t: "xy평면 경유 최단거리: z좌표 부호만 바꿔 직선 거리 계산!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "√(4² + 4² + 4²)", finalS: "4√3", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 점 피 삼 콤마 사 콤마 오에서 엑스축에 내린 수선의 발을 큐라 할 때, 선분 피큐의 길이는 얼마일까요?", cap: "점 $P(3,4,5)$ 에서 $x$축에 내린 수선의 발 $Q$ 에 대해 $\\overline{PQ}$ 의 길이 (자작 문항)" },
      { say: "엑스축에 내린 수선의 발 큐는 부른 문자 엑스만 남기고 나머지를 영으로 만든 삼 콤마 영 콤마 영입니다.", cap: "$Q(3,0,0)$" },
      { say: "따라서 선분 피큐의 길이는 루트 사의 제곱 더하기 오의 제곱, 루트 사십일입니다.", cap: "$\\overline{PQ}=\\sqrt{4^{2}+5^{2}}=\\sqrt{41}$" }
    ],
    examChips: [
      "P(3,4,5)\\text{ 에서 }x\\text{축 위 수선의 발 }Q(3,0,0)",
      "\\overline{PQ}=\\sqrt{(3-3)^{2}+(4-0)^{2}+(5-0)^{2}}",
      "=\\sqrt{16+25}=\\sqrt{41}"
    ],
    examLabels: ["x축 수선의 발 Q(3, 0, 0)", "정답 √41"],
    examGraph: {
      f: x => 0.45 * (x - 1.2) * (x - 1.2) + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.2, col: CY, label: "수선의 발 Q(3, 0, 0)" }, r2: { x: 2.3, col: GO, label: "PQ = √(4²+5²) = √41" },
      fn: { t: "x축까지 거리 = 안 부른 두 좌표 (y, z) 의 피타고라스 √(y² + z²)!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "√(4² + 5²)", finalS: "√41", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 선분 에이비가 엑스와이 평면과 만나는 점은 제트좌표가 영인 점이므로, 두 점의 제트좌표의 절댓값 비로 내분하거나 외분하는 점입니다.", cap: "① 평면 교점 꿀팁: 선분 $AB$ 가 $xy$평면과 만나는 점 $=$ $|z_{1}|:|z_{2}|$ 로 내분·외분하는 점!" },
      { say: "둘째, 평면의 대칭이동 최단거리 원리를 다룬 공통수학 투 제오십칠강과 완전히 똑같은 거울 반사 원리입니다.", cap: "② 제57강 대칭이동 직결: 2차원 직선 거울이 3차원 평면 거울로 확장된 것!" },
      { say: "셋째, 중심에서 모든 방향으로 같은 거리에 있는 점들의 자취를 세우면 바로 다음 마지막 강의인 구의 방정식이 됩니다.", cap: "③ 제99강 구의 방정식 직결: $\\overline{CP}=r\\iff (x-a)^{2}+(y-b)^{2}+(z-c)^{2}=r^{2}$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 기하 심화의 대단원 완결편인 구의 방정식과 단면 원을 다루는 제구십구강입니다.", cap: "제99강 · 구의 방정식, 좌표평면에 접하는 구와 단면 원" },
      { tag: "연계 ②", say: "대칭이동 최단거리의 기본 원리를 다루는 제오십칠강도 함께 보세요.", cap: "제57강 · 평행이동·대칭이동과 최단거리 (공통수학 2)" },
      { tag: "이 사이트", say: "이 사이트의 제구십구강과 제오십칠강을 이어서 보세요.", cap: "제99강 · 구의 방정식과 단면 원  /  제57강 · 대칭이동 최단거리" }
    ],
    nextLinks: [
      { lec: 99, label: "제99강 열기 (구의 방정식)" },
      { lec: 57, label: "제57강 열기 (대칭이동 최단거리)" },
      { lec: 52, label: "제52강 열기 (내분·무게중심)" }
    ]
  },
  {
    lec: 99,
    title: "숏츠식 판서 미리보기 · 구의 방정식, 좌표평면에 접하는 구와 단면 원",
    desc: "구의 방정식 $(x-a)^{2}+(y-b)^{2}+(z-c)^{2}=R^{2}$, 좌표평면·좌표축에 접하는 구의 조건과 평면으로 자른 단면 원의 반지름 $r'=\\sqrt{R^{2}-d^{2}}$ 를 정리합니다.",
    hookTitle: "구의 방정식 & 단면 원 반지름 √(R² − d²)", hookSub: "3차원 구 문제는 구의 중심을 지나는 2차원 단면 원으로 잘라 푼다!",
    hookSay: "기하의 마지막 단원인 구의 방정식과 평면으로 자른 단면 원의 넓이를 입체 그림 없이 3초 만에 푸는 법, 바로 정리합니다.",
    hookCap: "구의 방정식과 단면 원 · 30초 정리",
    whySay: "구는 어느 방향에서 잘라도 단면이 원이므로, 구의 중심에서 자른 평면이나 직선에 수선의 발을 내리면 구의 반지름 알과 거리 디, 단면 원의 반지름 알프라임이 항상 직각삼각형을 이룹니다.",
    whyCap: "단면 원 반지름 피타고라스: $r'=\\sqrt{R^{2}-d^{2}}$ ($R$: 구 반지름, $d$: 중심에서 평면까지 거리)",
    histTag: "아르키메데스의 구와 원기둥", histSay: "아르키메데스는 구의 단면 원 성질을 이용해 구의 부피와 겉넓이를 발견하고 자신의 묘비에 구와 외접 원기둥을 새겼습니다.",
    histCap: "구의 방정식 $(x-a)^{2}+(y-b)^{2}+(z-c)^{2}=R^{2}$ 과 단면 원 정사영",
    fParts: [
      { say: "중심이 에이 콤마 비 콤마 씨인 구가 엑스와이 평면에 접하면 반지름 알은 중심의 제트좌표의 절댓값 씨와 같습니다.", cap: "좌표평면 접선 조건: $xy$평면에 접함 $\\iff R=|c|$, 세 좌표평면에 동시 접함 $\\iff (\\pm r,\\pm r,\\pm r)$" },
      { say: "구와 평면이 만나서 생기는 교선은 항상 원이며, 중심에서 평면까지의 거리가 디이면 교선 원의 반지름은 루트 알 제곱 빼기 디 제곱입니다.", cap: "교선(단면 원) 반지름: $r'=\\sqrt{R^{2}-d^{2}}\\ \\Longrightarrow\\ \\text{단면 원 넓이 }=\\pi(R^{2}-d^{2})$" },
      { say: "구 밖의 점 피에서 구 위의 점까지의 거리의 최댓값은 중심 거리 디 더하기 알이고 최솟값은 디 빼기 알이며, 접선의 길이는 루트 디 제곱 빼기 알 제곱입니다.", cap: "구 외부 점 $P$ (중심 거리 $d$): 최대 $d+R$, 최소 $d-R$, 접선 길이 $l=\\sqrt{d^{2}-R^{2}}$!" }
    ],
    fChips: [
      "(x-a)^{2}+(y-b)^{2}+(z-c)^{2}=R^{2}:\\ xy\\text{평면에 접함}\\iff R=|c|",
      "\\text{평면 단면 원의 반지름 }r'=\\sqrt{R^{2}-d^{2}}\\ \\Longrightarrow\\ \\text{단면 넓이 }S=\\pi(R^{2}-d^{2})",
      "\\text{구 외부 점 }P(\\text{중심 거리 }d):\\ \\text{최대 }d+R,\\ \\text{최소 }d-R,\\ \\text{접선 }\\sqrt{d^{2}-R^{2}}"
    ],
    fLabels: ["xy평면 접함 ⇔ R = |c|", "단면 원 반지름 r' = √(R² − d²)"],
    exParts: [
      { say: "예를 들어 구 엑스 빼기 일의 제곱 더하기 와이 빼기 이의 제곱 더하기 제트 빼기 삼의 제곱은 이십오가 엑스와이 평면과 만나서 생기는 원의 넓이를 구해 봅시다.", cap: "$(x-1)^{2}+(y-2)^{2}+(z-3)^{2}=25$ 가 $xy$평면과 만나 생기는 단면 원의 넓이" },
      { say: "구의 반지름 알은 오이고, 중심 일 콤마 이 콤마 삼에서 엑스와이 평면까지의 거리 디는 제트좌표인 삼입니다.", cap: "$R=5,\\quad d=|3|=3$" },
      { say: "따라서 단면 원의 반지름 제곱은 이십오 빼기 구인 십육이므로 원의 넓이는 십육 파이입니다.", cap: "$r'^{2}=R^{2}-d^{2}=25-9=16\\ \\Rightarrow\\ S=16\\pi$" }
    ],
    exChips: [
      "\\text{중심 }C(1,2,3),\\quad R^{2}=25,\\quad xy\\text{평면까지 거리 }d=3",
      "r'^{2}=R^{2}-d^{2}=25-3^{2}=16\\quad (r'=4)",
      "\\text{단면 원의 넓이 }S=\\pi r'^{2}=16\\pi"
    ],
    exLabels: ["R = 5, d = 3 → r' = 4", "단면 넓이 = 16π"],
    exGraph: {
      f: x => 1.55 * Math.sqrt(Math.max(0, 1 - 0.45 * (x - 1.5) * (x - 1.5))) + 0.25, GY0: 390, GV: 110, xr: [0.2, 2.8], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "중심 거리 d = 3" }, r2: { x: 2.4, col: PK, label: "단면 반지름 r' = 4" },
      fn: { t: "구와 xy평면 교선: z = 0 대입 또는 r'² = R² − c² = 25 − 9 = 16!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "π × (25 − 9)", finalS: "16π", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 점 에이 사 콤마 삼 콤마 십이에서 구 엑스 제곱 더하기 와이 제곱 더하기 제트 제곱은 이십오 위의 점 피까지의 거리의 최댓값과 최솟값의 합은 얼마일까요?", cap: "점 $A(4,3,12)$ 에서 구 $x^{2}+y^{2}+z^{2}=25$ 위의 점 $P$ 까지 거리의 최대$+$최소 (자작 문항)" },
      { say: "원점인 구의 중심에서 점 에이까지의 거리 디는 루트 십육 더하기 구 더하기 백사십사, 즉 십삼이고 반지름 알은 오입니다.", cap: "$d=\\sqrt{4^{2}+3^{2}+12^{2}}=13,\\quad R=5$" },
      { say: "최댓값 디 더하기 알과 최솟값 디 빼기 알을 더하면 반지름 알이 소거되어 이 디가 남으므로 정답은 이십육입니다.", cap: "$(d+R)+(d-R)=2d=26$" }
    ],
    examChips: [
      "\\text{중심 }O(0,0,0),\\ R=5,\\quad d=\\overline{OA}=\\sqrt{4^{2}+3^{2}+12^{2}}=13",
      "M=d+R=18,\\qquad m=d-R=8",
      "M+m=2d=26"
    ],
    examLabels: ["중심 거리 d = 13", "정답 2d = 26"],
    examGraph: {
      f: x => 1.45 * Math.sqrt(Math.max(0, 1 - 0.5 * (x - 1.5) * (x - 1.5))) + 0.3, GY0: 390, GV: 110, xr: [0.3, 2.7], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "최소 d − R = 8" }, r2: { x: 2.4, col: GO, label: "최대 d + R = 18" },
      fn: { t: "구 밖의 점에서 거리 최대·최소: 중심 거리 d 기준 d ± R!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "18 + 8 = 2d", finalS: "26", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 구와 구가 만나서 생기는 교선 원을 포함하는 평면의 방정식은 두 구의 일반형 방정식을 변끼리 빼서 이차항을 소거하면 1초 만에 나옵니다.", cap: "① 두 구의 교평면 방정식: $(\\text{구 }1)-(\\text{구 }2)=0\\ \\Longrightarrow\\ ax+by+cz+d=0$ (공통현의 확장)!" },
      { say: "둘째, 구가 좌표축에 접할 때는 평면에 접할 때와 달리 피타고라스 공식을 써서 중심에서 축까지의 거리가 반지름 알과 같다고 식을 세워야 합니다.", cap: "② 축 접선 조건: 중심 $(a,b,c)$ 인 구가 $x$축에 접함 $\\iff R=\\sqrt{b^{2}+c^{2}}$!" },
      { say: "셋째, 이로써 기하 심화 열두 개 강의 사슬이 모두 완성되었습니다. 첫 단계인 제팔십팔강 포물선 심화부터 전체 흐름을 복습해 보세요.", cap: "③ 제88강~제99강 완결: 이차곡선 $\\to$ 평면벡터 $\\to$ 공간도형·공간좌표 완벽 마스터!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "기하 심화의 출발점인 제팔십팔강 포물선의 정의와 제구십이강 벡터의 내적으로 돌아가 전체 흐름을 복습해 보세요.", cap: "제88강 · 포물선 심화  /  제92강 · 평면벡터 내적과 중점 분해" },
      { tag: "연계 ②", say: "원의 방정식과 공통현을 다루는 공통수학 투 제오십오강, 제오십육강도 함께 복습해 보세요.", cap: "제55강 · 원의 방정식  /  제56강 · 원과 직선 위치관계" },
      { tag: "이 사이트", say: "이 사이트의 제팔십팔강과 제오십육강을 이어서 보세요.", cap: "제88강 · 기하 심화 첫 단계  /  제56강 · 원과 접선" }
    ],
    nextLinks: [
      { lec: 88, label: "제88강 열기 (기하 심화 첫 단계)" },
      { lec: 56, label: "제56강 열기 (원과 직선 위치관계)" },
      { lec: 95, label: "제95강 열기 (삼수선의 정리)" }
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
    subj: "geoadv",
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

const ALL_SPECS = [...GEOADV_SPECS_A, ...GEOADV_SPECS_B];
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
  const cInfo = GEOADV_CHAIN.find(c => c.lec === cfg.lec) || { step: 1, badge: "기하 심화", title: cfg.title };
  mainEl.innerHTML = `
    <div class="glass-card" style="margin-bottom:22px;border-left:5px solid #fb923c">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px">
        <span class="badge-pill" style="background:rgba(251,146,60,.18);color:#fdba74;border-color:rgba(251,146,60,.4)">
          📐 기하 심화 · 사슬 ${cInfo.step}/12단계 (${cInfo.badge})
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
      if (el.offsetWidth > 860) el.style.fontSize = (parseFloat(getComputedStyle(el).fontSize) * 860 / el.offsetWidth) + "px";
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
    if (st) st.textContent = `${si + 1} / ${SCENES.length} 장면 · 예상 전체 ${Math.floor(Math.round(total / 1000) / 60)}분 ${Math.round(total / 1000) % 60}초 (3분 미만)`;
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
    mount.innerHTML = `${geoadvChainNavHtml(cfg.lec)}
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
      const ok = await speak("안녕하세요. 기하 심화 핵심 공식을 함께 정리해 볼까요?");
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

const GEOADV_PLAYERS = {};
function initGeoAdv() {
  CONFIGS.forEach(cfg => {
    if (!GEOADV_PLAYERS[cfg.lec]) GEOADV_PLAYERS[cfg.lec] = createPlayer(cfg);
    GEOADV_PLAYERS[cfg.lec].init();
  });
}

window.GeoAdvShorts = { PLAYERS: GEOADV_PLAYERS, CONFIGS, initGeoAdv };
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initGeoAdv);
else initGeoAdv();
window.addEventListener("load", initGeoAdv);
})();
