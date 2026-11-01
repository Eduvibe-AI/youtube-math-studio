/* 공통수학 1 (2022 개정 교육과정 · 12강 사슬: 40 → 41 → 42 → 43 → 44 → 45 → 46 → 47 → 48 → 49 → 50 → 51)
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
const estMs = t => Math.max(1800, Math.round(Array.from(t || "").length * 135) + 450);

const COMMON1_CHAIN = [
  { lec: 40, step: 1,  badge: "대칭·교대식",   title: "곱셈공식 변형과 대칭식(x+y=u, xy=v)" },
  { lec: 41, step: 2,  badge: "중근나머지",    title: "나머지정리 (x−α)² 중근 인수와 미분" },
  { lec: 42, step: 3,  badge: "고차인수분해",  title: "복이차식과 상반방정식(x+1/x) 해법" },
  { lec: 43, step: 4,  badge: "복소수·ω",      title: "i의 4주기 순환성과 허근 ω(x³=1) 공식" },
  { lec: 44, step: 5,  badge: "두근의차",      title: "판별식 D와 두 근의 차 √D/|a| 공식" },
  { lec: 45, step: 6,  badge: "차함수탄생",    title: "이차함수와 직선 위치관계 · 차함수 h(x)" },
  { lec: 46, step: 7,  badge: "제한범위최대",  title: "제한된 범위 이차함수 최대·최소 (대칭축)" },
  { lec: 47, step: 8,  badge: "삼차근구조",    title: "삼차방정식 세 근의 구조(α,β,γ)와 켤레근" },
  { lec: 48, step: 9,  badge: "절댓값거리합",  title: "절댓값 부등식과 거리 합 |x−a|+|x−b|" },
  { lec: 49, step: 10, badge: "근의분리",      title: "이차방정식 실근의 위치 (함·판·축 3초)" },
  { lec: 50, step: 11, badge: "순열·조합",     title: "합·곱의 법칙과 순열(nPr)·조합(nCr)" },
  { lec: 51, step: 12, badge: "행렬거듭제곱",  title: "[2022 신설] 행렬 연산과 케일리-해밀턴" }
];

function common1ChainNavHtml(curLec) {
  const idx = COMMON1_CHAIN.findIndex(c => c.lec === curLec);
  const prev = idx > 0 ? COMMON1_CHAIN[idx - 1] : null;
  const next = idx >= 0 && idx < COMMON1_CHAIN.length - 1 ? COMMON1_CHAIN[idx + 1] : null;
  return `
    <div class="l2s-chain-box" style="margin-bottom:16px;padding:12px 14px;border-radius:12px;background:rgba(15,23,42,.82);border:1px solid rgba(244,63,94,.35)">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:10px">
        <span style="font-size:13px;font-weight:800;color:#fda4af">📕 공통수학 1 · 수업 단원·개념 연결 사슬 (${idx + 1} / ${COMMON1_CHAIN.length}단계)</span>
        <div style="display:flex;gap:6px">
          ${prev ? `<button type="button" class="l2s-btn" data-chain-lec="${prev.lec}" style="padding:4px 10px;font-size:12px">← 이전: 제${prev.lec}강 (${prev.badge})</button>` : ""}
          ${next ? `<button type="button" class="l2s-btn pri" data-chain-lec="${next.lec}" style="padding:4px 10px;font-size:12px">다음: 제${next.lec}강 (${next.badge}) →</button>` : ""}
        </div>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:5px">
        ${COMMON1_CHAIN.map(c => {
          const on = c.lec === curLec;
          return `<button type="button" data-chain-lec="${c.lec}" style="padding:4px 9px;border-radius:999px;font-size:11.5px;font-weight:${on ? 800 : 600};cursor:pointer;border:1px solid ${on ? "#facc15" : "rgba(148,163,184,.25)"};background:${on ? "rgba(250,204,21,.18)" : "rgba(15,23,42,.6)"};color:${on ? "#fde047" : "#cbd5e1"}">${c.step}. 제${c.lec}강 ${c.badge}</button>`;
        }).join("")}
      </div>
    </div>`;
}

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
    subj: "common1",
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

const COMMON1_SPECS_A = [
  {
    lec: 40,
    title: "숏츠식 판서 미리보기 · 곱셈공식 변형과 대칭식·교대식 구조",
    desc: "두 문자를 바꾸어도 같은 대칭식을 기본대칭식 $u=x+y,\\ v=xy$ 로 일관되게 표현하는 원리와 거듭제곱 합 공식을 정리합니다.",
    hookTitle: "곱셈공식 변형 · 대칭식의 법칙", hookSub: "합(u)과 곱(v) 두 개로 모든 거듭제곱 정복",
    hookSay: "복잡한 곱셈공식을 외우지 않고 합과 곱 두 개로 즉시 푸는 대칭식 원리, 30초 만에 정리합니다.",
    hookCap: "대칭식 기본 정리 · 30초 완성",
    whySay: "엑스와 와이를 서로 바꾸어도 식이 변하지 않는 대칭식은 언제나 합 유와 곱 브이 두 개의 조합만으로 백 퍼센트 나타낼 수 있습니다.",
    whyCap: "$f(x,y)=f(y,x)$ 대칭식 $\\Longrightarrow\\ u=x+y,\\ v=xy$ 로만 표현 가능",
    histTag: "뉴턴·가우스", histSay: "거듭제곱의 합을 기본대칭식으로 나타내는 뉴턴 항등식과 가우스의 기본대칭식 정리가 대수학의 토대가 되었습니다.",
    histCap: "뉴턴의 거듭제곱 합 공식과 가우스 대칭다항식 정리",
    fParts: [
      { say: "합을 유, 곱을 브이라 하면 제곱의 합은 유 제곱 빼기 이 브이입니다.", cap: "$x^{2}+y^{2}=(x+y)^{2}-2xy=u^{2}-2v$" },
      { say: "세제곱의 합은 유 세제곱 빼기 삼 유 브이로 인수분해 공식보다 변형 공식이 계산에 훨씬 빠릅니다.", cap: "$x^{3}+y^{3}=(x+y)^{3}-3xy(x+y)=u^{3}-3uv$" },
      { say: "차의 제곱은 합의 제곱에서 사 브이를 뺀 것과 같아 합과 곱만 알면 차도 즉시 구해집니다.", cap: "$(x-y)^{2}=(x+y)^{2}-4xy=u^{2}-4v$" }
    ],
    fChips: [
      "u=x+y,\\quad v=xy\\ \\Longrightarrow\\ x^{2}+y^{2}=u^{2}-2v",
      "x^{3}+y^{3}=(x+y)^{3}-3xy(x+y)=u^{3}-3uv",
      "(x-y)^{2}=u^{2}-4v,\\qquad x^{4}+y^{4}=(u^{2}-2v)^{2}-2v^{2}"
    ],
    fLabels: ["3차 대칭식 변형", "차의 제곱 & 4차 합"],
    exParts: [
      { say: "예를 들어 엑스 더하기 와이가 삼이고 엑스 와이가 일일 때 세제곱의 합을 구해 봅시다.", cap: "$x+y=3,\\ xy=1$ 일 때 $x^{3}+y^{3}$ 구하기" },
      { say: "합의 세제곱 이십칠에서 삼 곱하기 일 곱하기 삼인 구를 뺍니다.", cap: "$x^{3}+y^{3}=3^{3}-3\\times 1\\times 3$" },
      { say: "따라서 이십칠 빼기 구, 십팔이 됩니다.", cap: "$27-9=18$" }
    ],
    exChips: [
      "u=x+y=3,\\quad v=xy=1",
      "x^{3}+y^{3}=u^{3}-3uv=3^{3}-3(1)(3)",
      "27-9=18"
    ],
    exLabels: ["u=3, v=1 대입", "정답 18"],
    exGraph: {
      f: x => 0.35 * (x - 1.5) * (x - 1.5) + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "합 u = x + y" }, r2: { x: 2.5, col: PK, label: "곱 v = xy" },
      fn: { t: "모든 대칭식은 u = x + y 와 v = xy 의 다항식!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "u³ − 3uv", finalS: "x³ + y³ = 18", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 엑스 더하기 와이가 사이고 제곱의 합이 십일 때, 세제곱의 합은 얼마일까요?", cap: "$x+y=4,\\ x^{2}+y^{2}=10$ 일 때 $x^{3}+y^{3}$ 구하기 (자작 문항)" },
      { say: "먼저 사의 제곱 십육에서 십을 빼고 이로 나누면 곱 엑스 와이는 삼입니다.", cap: "$16-2xy=10\\ \\Rightarrow\\ xy=3$" },
      { say: "따라서 사의 세제곱 육십사에서 삼 곱하기 삼 곱하기 사인 삼십육을 빼면 이십팔입니다.", cap: "$4^{3}-3(3)(4)=64-36=28$" }
    ],
    examChips: [
      "x^{2}+y^{2}=4^{2}-2xy=10\\ \\Rightarrow\\ xy=3",
      "x^{3}+y^{3}=4^{3}-3(3)(4)",
      "64-36=28"
    ],
    examLabels: ["곱 xy = 3 도출", "정답 28"],
    examGraph: {
      f: x => 0.35 * (x - 1.5) * (x - 1.5) + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "u = 4, v = 3" }, r2: { x: 2.4, col: GO, label: "4³ − 3·3·4 = 28" },
      fn: { t: "u = 4, v = 3  ⇒  x³ + y³ = 64 − 36 = 28", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "xy = 3", finalS: "정답 = 28", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 문제에 제곱의 합이 주어지면 무조건 합의 제곱 공식부터 써서 곱 엑스 와이를 먼저 구합니다.", cap: "① $x+y$ 와 $x^{2}+y^{2}$ 가 보이면 $\\Longrightarrow$ 곱 $xy$ 부터 즉시 계산!" },
      { say: "둘째, 엑스 더하기 엑스분의 일 꼴은 곱이 항상 일이므로 공식에서 브이 자리에 일을 넣으면 됩니다.", cap: "② $x+\\dfrac{1}{x}=u$ 꼴은 곱 $v=1$ 인 특수 대칭식 ($x^{3}+x^{-3}=u^{3}-3u$)" },
      { say: "셋째, 세 문자 세제곱 공식에서는 합이 영이면 세제곱의 합이 삼 엑스 와이 제트와 같아집니다.", cap: "③ $x+y+z=0\\ \\Longrightarrow\\ x^{3}+y^{3}+z^{3}=3xyz$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 다항식을 완전제곱식으로 나눌 때의 나머지를 구하는 제사십일강입니다.", cap: "제41강 · 나머지정리 $(x-\\alpha)^{2}$ 중근 인수와 미분" },
      { tag: "연계 ②", say: "근과 계수의 관계로 바로 연결되는 제사십사강도 이어서 보세요.", cap: "제44강 · 판별식 $D$ 와 근과 계수의 관계" },
      { tag: "이 사이트", say: "이 사이트의 제사십일강과 제사십사강을 이어서 보세요.", cap: "제41강 · 중근 나머지정리  /  제44강 · 근과 계수의 관계" }
    ],
    nextLinks: [
      { lec: 41, label: "제41강 열기 (중근 나머지정리)" },
      { lec: 44, label: "제44강 열기 (근과 계수의 관계)" },
      { lec: 27, label: "제27강 열기 (수학 II 다항함수 눈)" }
    ]
  },
  {
    lec: 41,
    title: "숏츠식 판서 미리보기 · 나머지정리 (x − α)² 중근 인수와 미분·조립제법",
    desc: "다항식 $f(x)$ 를 $(x-\\alpha)^{2}$ 으로 나눈 나머지 $R(x)=f'(\\alpha)(x-\\alpha)+f(\\alpha)$ 와 인수정리 접선 의미를 확인합니다.",
    hookTitle: "나머지정리 · (x − α)² 중근 공식", hookSub: "연속조립제법과 미분계수로 5초 만에 풀이",
    hookSay: "완전제곱식으로 나눈 나머지를 연립방정식 없이 5초 만에 쓰는 공식, 바로 정리합니다.",
    hookCap: "$(x-\\alpha)^{2}$ 나머지 공식 · 30초 정리",
    whySay: "일차식의 제곱으로 나눈 일차 나머지를 에이 곱하기 엑스 빼기 알파 더하기 비로 놓으면, 비는 함숫값이고 에이는 그 점에서의 접선의 기울기입니다.",
    whyCap: "$f(x)=(x-\\alpha)^{2}Q(x)+a(x-\\alpha)+b\\ \\Rightarrow\\ b=f(\\alpha),\\ a=f'(\\alpha)$",
    histTag: "베주·테일러", histSay: "일차식으로 나눈 나머지가 함숫값이라는 베주의 나머지정리를 알파 중심 일차 테일러 전개로 확장한 원리입니다.",
    histCap: "베주(Bézout)의 나머지정리와 $x=\\alpha$ 중심 다항식 전개",
    fParts: [
      { say: "에프 엑스를 엑스 빼기 알파의 제곱으로 나눈 나머지를 에이 엑스 더하기 비 대신 에이 괄호 엑스 빼기 알파 더하기 비로 둡니다.", cap: "$f(x)=(x-\\alpha)^{2}Q(x)+a(x-\\alpha)+b$" },
      { say: "엑스에 알파를 대입하면 상수 비는 에프 알파가 되고, 양변을 엑스 빼기 알파로 한 번 더 정리하면 에이는 에프 프라임 알파입니다.", cap: "$b=f(\\alpha),\\quad a=f'(\\alpha)$ (조립제법 두 번의 나머지)" },
      { say: "특히 나머지가 영이면 에프 알파와 에프 프라임 알파가 모두 영이어서 엑스축에 접하는 중근이 됩니다.", cap: "$(x-\\alpha)^{2}$ 나누어떨어짐 $\\Longleftrightarrow\\ f(\\alpha)=0,\\ f'(\\alpha)=0$ (접점)" }
    ],
    fChips: [
      "f(x)=(x-\\alpha)^{2}Q(x)+a(x-\\alpha)+b",
      "b=f(\\alpha),\\qquad a=f'(\\alpha)",
      "R(x)=f'(\\alpha)(x-\\alpha)+f(\\alpha)"
    ],
    fLabels: ["x = α 대입 & 미분", "1차 나머지 즉시 완성"],
    exParts: [
      { say: "예를 들어 엑스 세제곱 더하기 일을 엑스 빼기 일의 제곱으로 나눈 나머지를 구해 봅시다.", cap: "$f(x)=x^{3}+1$ 을 $(x-1)^{2}$ 으로 나눈 나머지" },
      { say: "일에서의 함숫값 에프 일은 이이고, 미분한 삼 엑스 제곱에 일을 넣으면 기울기는 삼입니다.", cap: "$f(1)=2,\\quad f'(1)=3$" },
      { say: "따라서 나머지는 삼 곱하기 괄호 엑스 빼기 일 더하기 이, 즉 삼 엑스 빼기 일입니다.", cap: "$R(x)=3(x-1)+2=3x-1$" }
    ],
    exChips: [
      "f(x)=x^{3}+1\\ \\Rightarrow\\ f(1)=2,\\quad f'(x)=3x^{2}\\Rightarrow f'(1)=3",
      "R(x)=3(x-1)+2",
      "R(x)=3x-1"
    ],
    exLabels: ["f(1)=2, f'(1)=3", "나머지 3x − 1"],
    exGraph: {
      f: x => 0.32 * x * x * x + 0.35, GY0: 390, GV: 110, xr: [0, 2.5], area: [0.4, 2.1], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.0, col: CY, label: "접점 x = α" }, r2: { x: 2.0, col: PK, label: "접선 y = R(x)" },
      fn: { t: "(x − α)² 로 나눈 나머지 R(x) = x = α 에서의 접선 방정식!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "R(x) = 접선!", finalS: "R(x) = 3x − 1", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 다항식 엑스 네제곱 빼기 삼 엑스 더하기 이를 엑스 빼기 일의 제곱으로 나눈 나머지를 알 엑스라 할 때, 알 이의 값은 얼마일까요?", cap: "$f(x)=x^{4}-3x+2$ 를 $(x-1)^{2}$ 으로 나눈 나머지 $R(2)$ (자작 문항)" },
      { say: "에프 일은 영이고, 도함수 사 엑스 세제곱 빼기 삼에 일을 넣으면 일입니다.", cap: "$f(1)=0,\\quad f'(1)=4-3=1$" },
      { say: "나머지 알 엑스는 엑스 빼기 일이므로 알 이는 일입니다.", cap: "$R(x)=1\\cdot(x-1)+0=x-1\\ \\Rightarrow\\ R(2)=1$" }
    ],
    examChips: [
      "f(1)=1-3+2=0,\\quad f'(1)=4(1)^{3}-3=1",
      "R(x)=1\\cdot(x-1)+0=x-1",
      "R(2)=2-1=1"
    ],
    examLabels: ["R(x) = x − 1", "정답 R(2) = 1"],
    examGraph: {
      f: x => 0.35 * Math.pow(x - 0.8, 2) + 0.3, GY0: 390, GV: 110, xr: [0, 2.6], area: [0.3, 2.2], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.8, col: CY, label: "f(1) = 0" }, r2: { x: 2.0, col: GO, label: "f'(1) = 1" },
      fn: { t: "R(x) = f'(1)(x − 1) + f(1) = x − 1  ⇒  R(2) = 1", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "R(x) = x − 1", finalS: "R(2) = 1", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 서술형에서 미분을 쓸 수 없을 때는 알파로 조립제법을 두 번 연속 실행하면 첫 나머지가 비, 둘째 나머지가 에이입니다.", cap: "① 서술형 해법: $x=\\alpha$ 로 연속조립제법 2회 $\\Rightarrow$ 나머지 $b,\\ a$" },
      { say: "둘째, 기하학적으로 엑스 빼기 알파의 제곱으로 나눈 나머지 알 엑스는 곡선 위의 점 알파에서의 접선 방정식입니다.", cap: "② 기하적 본질: $(x-\\alpha)^{2}$ 나머지 $R(x)$ 는 $x=\\alpha$ 에서의 접선!" },
      { say: "셋째, 이 원리가 그대로 수학 투의 제이십칠강 다항함수 인수 작성법으로 이어집니다.", cap: "③ 수학 II 연결: $f(x)-R(x)=(x-\\alpha)^{2}Q(x)$ (접점 $=$ 중근 인수)" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 복이차식과 상반방정식 등 고차다항식의 인수분해를 다루는 제사십이강입니다.", cap: "제42강 · 고차식 인수분해 (복이차식과 상반방정식)" },
      { tag: "연계 ②", say: "수학 투에서 접선과 중근 인수를 활용하는 제이십칠강도 함께 보세요.", cap: "제27강 · 다항함수를 보는 눈 (인수와 대칭성)" },
      { tag: "이 사이트", say: "이 사이트의 제사십이강과 제이십칠강을 이어서 보세요.", cap: "제42강 · 고차식 인수분해  /  제27강 · 다항함수를 보는 눈" }
    ],
    nextLinks: [
      { lec: 42, label: "제42강 열기 (고차식 인수분해)" },
      { lec: 27, label: "제27강 열기 (수학 II 다항함수 눈)" },
      { lec: 40, label: "제40강 열기 (대칭식 변형)" }
    ]
  },
  {
    lec: 42,
    title: "숏츠식 판서 미리보기 · 고차식 인수분해 (복이차식과 상반방정식)",
    desc: "짝수 차수만 있는 복이차식($A^{2}-B^{2}$ 변형)과 계수가 대칭인 상반방정식($x+1/x$ 치환)의 해법을 정리합니다.",
    hookTitle: "고차식 인수분해 · 복이차식 & 상반식", hookSub: "합차공식(A²−B²)과 역수 대칭 치환 30초 정리",
    hookSay: "조립제법이 안 되는 사차식을 단숨에 인수분해하는 두 가지 비법, 30초 만에 정리합니다.",
    hookCap: "복이차식·상반방정식 · 30초 정리",
    whySay: "인수분해가 안 되는 사차식은 가운데 이차항을 조절해 제곱 빼기 제곱 꼴을 만들거나, 엑스 제곱으로 묶어 역수 대칭식으로 바꾸면 이차식으로 풀립니다.",
    whyCap: "복이차식($A^{2}-B^{2}$ 합차) · 상반방정식($x+\\dfrac{1}{x}=t$ 치환)",
    histTag: "페라리·갈루아", histSay: "사차방정식을 이차방정식들의 곱으로 분해하는 해법은 16세기 이탈리아 수학자 페라리에 의해 발견되었습니다.",
    histCap: "페라리의 4차방정식 분해법과 대칭 다항식 치환",
    fParts: [
      { say: "짝수 차수만 있는 복이차식이 바로 인수분해되지 않으면, 사차항과 상수항을 기준으로 완전제곱식을 만들고 뒤를 제곱수로 맞춥니다.", cap: "복이차식: $(x^{2}\\pm k)^{2}-(mx)^{2}$ 꼴로 변형 후 합차공식" },
      { say: "계수가 좌우 대칭인 사차 상반식은 가운데 엑스 제곱으로 묶어냅니다.", cap: "상반식: $x^{2}\\!\\left(x^{2}+ax+b+\\dfrac{a}{x}+\\dfrac{1}{x^{2}}\\right)$" },
      { say: "엑스 더하기 엑스분의 일을 티로 치환하면 엑스 제곱 더하기 엑스 제곱분의 일은 티 제곱 빼기 이가 되어 이차식으로 인수분해됩니다.", cap: "$x+\\dfrac{1}{x}=t\\ \\Longrightarrow\\ x^{2}+\\dfrac{1}{x^{2}}=t^{2}-2$" }
    ],
    fChips: [
      "\\text{복이차식: }x^{4}+ax^{2}+b^{2}=(x^{2}+b)^{2}-(kx)^{2}\\ \\Rightarrow\\ (A+B)(A-B)",
      "\\text{상반식: 가운데 }x^{2}\\text{ 으로 묶고 }x+\\dfrac{1}{x}=t\\text{ 치환}",
      "x^{2}+\\dfrac{1}{x^{2}}=t^{2}-2\\ \\Longrightarrow\\ t\\text{ 에 대한 이차식 인수분해}"
    ],
    fLabels: ["A² − B² 합차 변형", "t = x + 1/x 치환"],
    exParts: [
      { say: "예를 들어 엑스 네제곱 더하기 엑스 제곱 더하기 일을 인수분해해 봅시다.", cap: "$x^{4}+x^{2}+1$ 의 인수분해 (오메가 모체식)" },
      { say: "엑스 제곱을 하나 더하고 빼면 엑스 제곱 더하기 일 전체의 제곱 빼기 엑스 제곱이 됩니다.", cap: "$(x^{2}+1)^{2}-x^{2}$" },
      { say: "합차공식을 쓰면 엑스 제곱 더하기 엑스 더하기 일 곱하기 엑스 제곱 빼기 엑스 더하기 일로 인수분해됩니다.", cap: "$(x^{2}+x+1)(x^{2}-x+1)$" }
    ],
    exChips: [
      "x^{4}+x^{2}+1=(x^{4}+2x^{2}+1)-x^{2}",
      "=(x^{2}+1)^{2}-x^{2}",
      "=(x^{2}+x+1)(x^{2}-x+1)"
    ],
    exLabels: ["+x² − x² 조절", "합차공식 완성"],
    exGraph: {
      f: x => 0.22 * Math.pow(x - 1.5, 4) + 0.35 * Math.pow(x - 1.5, 2) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "x² − x + 1" }, r2: { x: 2.4, col: PK, label: "x² + x + 1" },
      fn: { t: "x⁴ + x² + 1 = (x² + x + 1)(x² − x + 1)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(x²+1)² − x²", finalS: "복이차식 분해!", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 다항식 엑스 네제곱 빼기 삼 엑스 제곱 더하기 구가 두 이차식의 곱으로 인수분해될 때, 두 이차식에 엑스는 이를 대입한 값들의 합은 얼마일까요?", cap: "$x^{4}-3x^{2}+9=(x^{2}+ax+3)(x^{2}-ax+3)$ 에서 $x=2$ 대입 합 (자작 문항)" },
      { say: "엑스 네제곱 더하기 육 엑스 제곱 더하기 구에서 구 엑스 제곱을 뺀 형태이므로 에이는 삼입니다.", cap: "$(x^{2}+3)^{2}-(3x)^{2}=(x^{2}+3x+3)(x^{2}-3x+3)$" },
      { say: "두 이차식에 이를 대입하면 십삼과 일이므로 합은 십사입니다.", cap: "$13+1=14$" }
    ],
    examChips: [
      "x^{4}-3x^{2}+9=(x^{2}+3)^{2}-(3x)^{2}",
      "=(x^{2}+3x+3)(x^{2}-3x+3)",
      "x=2\\text{ 대입 합 }=(4+6+3)+(4-6+3)=13+1=14"
    ],
    examLabels: ["(x²+3)² − (3x)²", "정답 14"],
    examGraph: {
      f: x => 0.25 * Math.pow(x - 1.5, 4) + 0.3 * Math.pow(x - 1.5, 2) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "f₁(2) = 13" }, r2: { x: 2.4, col: GO, label: "f₂(2) = 1" },
      fn: { t: "(x² + 3x + 3)(x² − 3x + 3)  ⇒  13 + 1 = 14", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "a = 3", finalS: "합 = 14", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 엑스 네제곱 더하기 엑스 제곱 더하기 일의 인수분해는 오메가 문제에서도 그대로 쓰이므로 외워 두면 좋습니다.", cap: "① 필수 암기: $x^{4}+x^{2}+1=(x^{2}+x+1)(x^{2}-x+1)$" },
      { say: "둘째, 복이차식 변형 시 뒤쪽이 마이너스 완전제곱이 나오도록 가운데 부호를 플러스와 마이너스 두 경우 중 선택합니다.", cap: "② $(x^{2}\\pm b)^{2}-(kx)^{2}$ 에서 뒤쪽이 제곱수가 되는 부호 선택!" },
      { say: "셋째, 홀수 차수 상반방정식은 반드시 엑스는 마이너스 일 또는 일을 근으로 가집니다.", cap: "③ 홀수차 대칭 계수 방정식 $\\Longrightarrow$ $x=\\pm 1$ 조립제법 1회 후 짝수차 상반식!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 복소수 아이의 사주기와 삼차방정식의 허근 오메가를 다루는 제사십삼강입니다.", cap: "제43강 · 복소수 $i$ 의 4주기 순환성과 허근 $\\omega$" },
      { tag: "연계 ②", say: "삼차방정식 세 근의 구조를 다루는 제사십칠강도 이어서 보세요.", cap: "제47강 · 삼차방정식 세 근의 구조와 켤레근" },
      { tag: "이 사이트", say: "이 사이트의 제사십삼강과 제사십칠강을 이어서 보세요.", cap: "제43강 · 복소수와 $\\omega$  /  제47강 · 삼차방정식 근의 구조" }
    ],
    nextLinks: [
      { lec: 43, label: "제43강 열기 (복소수와 오메가)" },
      { lec: 47, label: "제47강 열기 (삼차방정식 근의 구조)" },
      { lec: 41, label: "제41강 열기 (중근 나머지정리)" }
    ]
  },
  {
    lec: 43,
    title: "숏츠식 판서 미리보기 · 복소수 i의 4주기 순환성과 허근 ω 3초 암산법",
    desc: "$i^{4}=1$ 에 따른 연속 4개 합 $=0$ 성질과 $x^{3}=1$ 의 한 허근 $\\omega$ 의 3주기·근과 계수 공식을 정리합니다.",
    hookTitle: "복소수 i의 4주기 & 오메가(ω) 3주기", hookSub: "연속 4개 합 = 0 · ω³ = 1, ω² + ω + 1 = 0",
    hookSay: "백 제곱, 천 제곱이 나오는 복소수 아이와 오메가 문제를 3초 만에 암산하는 규칙, 바로 정리합니다.",
    hookCap: "복소수 $i$ & 허근 $\\omega$ · 30초 정리",
    whySay: "복소수 아이는 곱할 때마다 복소평면에서 구십도씩 회전하므로 네 번마다 제자리로 돌아오고, 오메가는 백이십도씩 회전하므로 세 번마다 일이 됩니다.",
    whyCap: "$i$: $90^{\\circ}$ 회전(4주기, 4개 합 $=0$) · $\\omega$: $120^{\\circ}$ 회전(3주기, 3개 합 $=0$)",
    histTag: "가우스·오일러", histSay: "허수 단위 아이 기호는 오일러가 도입했고, 가우스가 복소평면 위에서 단위근의 기하학적 회전 대칭성을 확립했습니다.",
    histCap: "오일러의 기호 $i=\\sqrt{-1}$ 와 가우스의 복소평면 단위근",
    fParts: [
      { say: "아이, 아이 제곱, 아이 세제곱, 아이 네제곱은 아이, 마이너스 일, 마이너스 아이, 일로 연속된 네 개의 합이 항상 영입니다.", cap: "$i^{1}+i^{2}+i^{3}+i^{4}=i-1-i+1=0$ (4개씩 소거)" },
      { say: "일 더하기 아이 분의 일 빼기 아이는 마이너스 아이이고, 일 빼기 아이 분의 일 더하기 아이는 아이로 즉시 바꿉니다.", cap: "$\\dfrac{1-i}{1+i}=-i,\\quad \\dfrac{1+i}{1-i}=i,\\quad (1\\pm i)^{2}=\\pm 2i$" },
      { say: "엑스 세제곱은 일의 허근 오메가는 오메가 세제곱이 일이고 오메가 제곱 더하기 오메가 더하기 일이 영입니다.", cap: "$\\omega^{3}=1,\\quad \\omega^{2}+\\omega+1=0,\\quad \\omega+\\bar{\\omega}=-1,\\ \\omega\\bar{\\omega}=1$" }
    ],
    fChips: [
      "i^{n}+i^{n+1}+i^{n+2}+i^{n+3}=0,\\qquad \\dfrac{1\\pm i}{1\\mp i}=\\pm i",
      "x^{3}=1\\text{ 의 허근 }\\omega\\ \\Longrightarrow\\ \\omega^{3}=1,\\quad \\omega^{2}+\\omega+1=0",
      "\\omega+\\bar{\\omega}=-1,\\qquad \\omega\\bar{\\omega}=1,\\qquad \\omega^{2}=\\bar{\\omega}=\\dfrac{1}{\\omega}"
    ],
    fLabels: ["i의 4주기 & 분수 암산", "오메가 3주기 & 켤레근"],
    exParts: [
      { say: "예를 들어 엑스 세제곱은 일의 한 허근 오메가에 대하여 일 더하기 오메가 더하기 오메가 제곱부터 오메가 백 제곱까지의 합을 구해 봅시다.", cap: "$1+\\omega+\\omega^{2}+\\cdots+\\omega^{100}$ 의 값" },
      { say: "연속된 세 항의 합이 영이고 전체 항의 개수는 일부터 백까지에 상수 일까지 합쳐 백일 개입니다.", cap: "전체 $101$개 항 $=3\\times 33+2$개 남음" },
      { say: "앞에서나 뒤에서나 세 개씩 묶어 지우면 일 더하기 오메가만 남고, 이는 마이너스 오메가 제곱과 같습니다.", cap: "남는 항 $=1+\\omega=-\\omega^{2}$" }
    ],
    exChips: [
      "1+\\omega+\\omega^{2}=0\\quad (\\text{연속 3개 항의 합 }=0)",
      "\\text{항의 개수 }101=3\\times 33+2\\ \\Rightarrow\\ 1+\\omega\\text{ 남음}",
      "1+\\omega=-\\omega^{2}"
    ],
    exLabels: ["3개씩 묶어 0 소거", "남는 2개 항 정리"],
    exGraph: {
      f: x => Math.cos(x * 2.1) * 1.1 + 1.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "i : 4주기 순환" }, r2: { x: 2.3, col: PK, label: "ω : 3주기 순환" },
      fn: { t: "i 는 4개씩 합 = 0,  ω 는 3개씩 합 = 0!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "주기 묶음 소거", finalS: "1 + ω = −ω²", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 방정식 엑스 세제곱은 일의 한 허근을 오메가라 할 때, 오메가 십 제곱 더하기 오메가 이십 제곱 더하기 오메가 삼십 제곱의 값은 얼마일까요?", cap: "$\\omega^{3}=1$ 인 허근 $\\omega$ 에 대해 $\\omega^{10}+\\omega^{20}+\\omega^{30}$ (자작 문항)" },
      { say: "지수를 삼으로 나눈 나머지로 바꾸면 십은 일, 이십은 이, 삼십은 영이 됩니다.", cap: "$\\omega^{10}=\\omega^{1},\\quad \\omega^{20}=\\omega^{2},\\quad \\omega^{30}=\\omega^{0}=1$" },
      { say: "따라서 오메가 더하기 오메가 제곱 더하기 일이므로 정답은 영입니다.", cap: "$\\omega+\\omega^{2}+1=0$" }
    ],
    examChips: [
      "\\omega^{3}=1\\ \\Longrightarrow\\ \\text{지수를 }3\\text{ 으로 나눈 나머지로 축소}",
      "\\omega^{10}+\\omega^{20}+\\omega^{30}=\\omega^{1}+\\omega^{2}+1",
      "\\omega^{2}+\\omega+1=0"
    ],
    examLabels: ["지수를 3으로 나눈 나머지", "정답 0"],
    examGraph: {
      f: x => Math.cos(x * 2.1) * 1.1 + 1.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.8, col: CY, label: "ω¹⁰ = ω" }, r2: { x: 2.2, col: GO, label: "ω²⁰ = ω², ω³⁰ = 1" },
      fn: { t: "ω¹⁰ + ω²⁰ + ω³⁰ = ω + ω² + 1 = 0", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "ω + ω² + 1", finalS: "정답 = 0", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 거듭제곱 합을 구할 때는 일부터 시작하므로 전체 항의 개수가 엔 개가 아니라 엔 더하기 일 개임을 주의합니다.", cap: "① $1+z+z^{2}+\\cdots+z^{n}$ 의 항의 개수는 $n+1$ 개! (뒤에서부터 묶으면 안전)" },
      { say: "둘째, 루트 이 분의 일 플러스 아이를 제곱하면 바로 아이가 되어 팔 주기를 가집니다.", cap: "② $\\left(\\dfrac{1\\pm i}{\\sqrt{2}}\\right)^{2}=\\pm i\\ \\Longrightarrow\\ 8$주기 순환!" },
      { say: "셋째, 엑스 세제곱은 마이너스 일의 허근 오메가는 오메가 제곱 빼기 오메가 더하기 일이 영이므로 부호를 꼭 구분합니다.", cap: "③ $x^{3}=-1$ 의 허근: $\\omega^{3}=-1,\\quad \\omega^{2}-\\omega+1=0$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 이차방정식 판별식과 두 근의 차 공식을 다루는 제사십사강입니다.", cap: "제44강 · 판별식 $D$ 와 두 근의 차 $\\dfrac{\\sqrt{D}}{|a|}$ 공식" },
      { tag: "연계 ②", say: "단위원 위에서 회전각을 다루는 수학 원의 제십육강과도 연결됩니다.", cap: "제16강 · 단위원 삼각함수 정복" },
      { tag: "이 사이트", say: "이 사이트의 제사십사강과 제십육강을 이어서 보세요.", cap: "제44강 · 판별식과 두 근의 차  /  제16강 · 단위원 삼각함수" }
    ],
    nextLinks: [
      { lec: 44, label: "제44강 열기 (판별식과 두 근의 차)" },
      { lec: 16, label: "제16강 열기 (단위원 삼각함수)" },
      { lec: 42, label: "제42강 열기 (고차식 인수분해)" }
    ]
  },
  {
    lec: 44,
    title: "숏츠식 판서 미리보기 · 판별식 D의 본질과 두 근의 차 공식",
    desc: "이차방정식 $ax^{2}+bx+c=0$ 의 근과 계수의 관계와 두 근의 거리 $|\\beta-\\alpha|=\\frac{\\sqrt{D}}{|a|}$ 를 정리합니다.",
    hookTitle: "판별식 D와 두 근의 차 3초 공식", hookSub: "|β − α| = √D / |a| 로 정적분 넓이까지 직결",
    hookSay: "이차방정식의 두 근을 직접 구하지 않고 두 근 사이의 거리를 3초 만에 구하는 공식, 바로 정리합니다.",
    hookCap: "두 근의 차 $\\dfrac{\\sqrt{D}}{|a|}$ · 30초 정리",
    whySay: "근의 공식에서 두 근을 빼면 마이너스 비가 지워지고 이 에이 분의 이 루트 디가 남아, 두 근의 차가 절댓값 에이 분의 루트 디가 됩니다.",
    whyCap: "근의 공식 $\\dfrac{-b\\pm\\sqrt{D}}{2a}$ 의 차 $\\Longrightarrow\\ |\\beta-\\alpha|=\\dfrac{\\sqrt{D}}{|a|}$",
    histTag: "비에트 정리", histSay: "방정식의 근과 계수 사이의 대칭적 관계식을 체계화한 사람은 16세기 프랑스 수학자 프랑수아 비에트입니다.",
    histCap: "비에트 정리(Vieta's Formulas)와 판별식 $D=b^{2}-4ac$",
    fParts: [
      { say: "이차방정식의 두 근 알파, 베타의 합은 마이너스 에이분의 비이고 곱은 에이분의 씨입니다.", cap: "$\\alpha+\\beta=-\\dfrac{b}{a},\\qquad \\alpha\\beta=\\dfrac{c}{a}$" },
      { say: "두 근의 차 절댓값 베타 빼기 알파는 최고차항 계수의 절댓값 에이 분의 루트 판별식 디입니다.", cap: "$|\\beta-\\alpha|=\\sqrt{(\\alpha+\\beta)^{2}-4\\alpha\\beta}=\\dfrac{\\sqrt{b^{2}-4ac}}{|a|}=\\dfrac{\\sqrt{D}}{|a|}$" },
      { say: "따라서 판별식 디가 양수이면 두 근의 거리가 양수여서 서로 다른 두 실근이고, 영이면 거리가 영이어서 중근입니다.", cap: "$D\\gt 0$ (서로 다른 두 점) · $D=0$ (거리 $0$, 접점) · $D\\lt 0$ (허근)" }
    ],
    fChips: [
      "\\alpha+\\beta=-\\dfrac{b}{a},\\qquad \\alpha\\beta=\\dfrac{c}{a}",
      "|\\beta-\\alpha|=\\dfrac{\\sqrt{b^{2}-4ac}}{|a|}=\\dfrac{\\sqrt{D}}{|a|}",
      "\\text{이차함수 넓이 }S=\\dfrac{|a|}{6}(\\beta-\\alpha)^{3}=\\dfrac{D\\sqrt{D}}{6a^{2}}"
    ],
    fLabels: ["근의 공식 뺄셈", "정적분 1/6 넓이 공식 직결"],
    exParts: [
      { say: "예를 들어 이차방정식 엑스 제곱 빼기 오 엑스 더하기 삼은 영의 두 근의 차를 구해 봅시다.", cap: "$x^{2}-5x+3=0$ 의 두 근 $\\alpha, \\beta$ 의 차 $|\\beta-\\alpha|$" },
      { say: "판별식 디는 이십오 빼기 십이로 십삼이고 최고차항 계수 에이는 일입니다.", cap: "$D=(-5)^{2}-4(1)(3)=25-12=13$" },
      { say: "따라서 두 근의 차는 일 분의 루트 십삼, 즉 루트 십삼입니다.", cap: "$|\\beta-\\alpha|=\\dfrac{\\sqrt{13}}{1}=\\sqrt{13}$" }
    ],
    exChips: [
      "x^{2}-5x+3=0\\ \\Rightarrow\\ a=1,\\ b=-5,\\ c=3",
      "D=(-5)^{2}-4(1)(3)=13",
      "|\\beta-\\alpha|=\\dfrac{\\sqrt{13}}{1}=\\sqrt{13}"
    ],
    exLabels: ["판별식 D = 13", "두 근의 차 √13"],
    exGraph: {
      f: x => 0.45 * (x - 0.5) * (x - 2.5) + 0.85, GY0: 390, GV: 110, xr: [0, 3], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "근 α" }, r2: { x: 2.5, col: PK, label: "근 β (거리 √D/|a|)" },
      fn: { t: "두 교점 사이의 가로 거리 |β − α| = √D / |a|", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "D = 25 − 12 = 13", finalS: "|β − α| = √13", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 이차방정식 이 엑스 제곱 빼기 육 엑스 더하기 케이는 영의 두 실근의 차가 사일 때, 상수 케이의 값은 얼마일까요?", cap: "$2x^{2}-6x+k=0$ 의 두 근의 차가 $4$ 일 때 $k$ 구하기 (자작 문항)" },
      { say: "두 근의 차 공식에 의해 이 분의 루트 삼십육 빼기 팔 케이가 사입니다.", cap: "$\\dfrac{\\sqrt{36-8k}}{2}=4\\ \\Rightarrow\\ \\sqrt{36-8k}=8$" },
      { say: "양변을 제곱하면 삼십육 빼기 팔 케이가 육십사이므로 케이는 마이너스 이분의 칠입니다.", cap: "$36-8k=64\\ \\Rightarrow\\ 8k=-28\\ \\Rightarrow\\ k=-\\dfrac{7}{2}$" }
    ],
    examChips: [
      "|\\beta-\\alpha|=\\dfrac{\\sqrt{(-6)^{2}-4(2)k}}{2}=4",
      "36-8k=8^{2}=64",
      "8k=-28\\ \\Rightarrow\\ k=-\\dfrac{7}{2}"
    ],
    examLabels: ["√D / 2 = 4", "정답 k = −7/2"],
    examGraph: {
      f: x => 0.45 * (x - 0.4) * (x - 2.6) + 0.9, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "α" }, r2: { x: 2.6, col: GO, label: "β (|β−α| = 4)" },
      fn: { t: "√(36 − 8k) / 2 = 4  ⇒  36 − 8k = 64  ⇒  k = −7/2", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "36 − 8k = 64", finalS: "k = −7/2", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 최고차항 계수 에이가 일이 아닐 때는 분모에 반드시 절댓값 에이로 나누어야 실수를 피합니다.", cap: "① 최고차항 계수 $a\\neq 1$ 주의: 분모에 $|a|$ 필수!" },
      { say: "둘째, 이차함수와 직선이 잘리는 현의 길이는 기울기가 엠일 때 루트 일 더하기 엠 제곱 곱하기 두 근의 차입니다.", cap: "② 기울기 $m$ 직선의 현의 길이 $=\\sqrt{1+m^{2}}\\,|\\beta-\\alpha|$" },
      { say: "셋째, 수학 투의 정적분 육분의 일 넓이 공식에 이 두 근의 차 공식을 대입하면 인수분해가 안 돼도 넓이가 바로 나옵니다.", cap: "③ 수학 II 제2강 연결: $S=\\dfrac{|a|}{6}(\\beta-\\alpha)^{3}$ 에 즉시 대입!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 이차함수와 직선의 위치관계를 차함수로 해석하는 제사십오강입니다.", cap: "제45강 · 이차함수와 직선의 위치관계 · 차함수 $h(x)$" },
      { tag: "연계 ②", say: "수학 투의 정적분 넓이 만능 공식 제이강과도 바로 이어집니다.", cap: "제2강 · 정적분 넓이 만능 공식 (수학 II)" },
      { tag: "이 사이트", say: "이 사이트의 제사십오강과 제이강을 이어서 보세요.", cap: "제45강 · 차함수의 탄생  /  제2강 · 정적분 넓이 만능 공식" }
    ],
    nextLinks: [
      { lec: 45, label: "제45강 열기 (차함수의 탄생)" },
      { lec: 2, label: "제2강 열기 (수학 II 넓이 공식)" },
      { lec: 43, label: "제43강 열기 (복소수와 오메가)" }
    ]
  },
  {
    lec: 45,
    title: "숏츠식 판서 미리보기 · 이차함수와 직선의 위치관계 (차함수의 탄생)",
    desc: "곡선 $y=f(x)$ 와 직선 $y=g(x)$ 의 교점·접점을 차함수 $h(x)=f(x)-g(x)$ 의 인수 구조로 해석합니다.",
    hookTitle: "이차함수와 직선 · 차함수의 탄생", hookSub: "f(x) − g(x) = a(x − α)(x − β) 3초 식 세우기",
    hookSay: "이차함수와 직선이 만나는 문제를 차함수 하나로 깔끔하게 끝내는 원리, 30초 만에 정리합니다.",
    hookCap: "이차함수 차함수 공식 · 30초 정리",
    whySay: "직선을 이항해 에프 엑스 빼기 쥐 엑스를 새로운 이차함수로 보면, 비스듬한 직선과의 교점이 수평한 엑스축과의 절편으로 바뀌어 식이 한 줄로 세워집니다.",
    whyCap: "연립방정식 $f(x)=g(x)\\ \\Longleftrightarrow$ 차함수 $h(x)=f(x)-g(x)=0$ 의 근",
    histTag: "해석기하", histSay: "기하학적 교점을 두 함수의 차로 이루어진 방정식의 근으로 환원하는 해석기하학의 핵심 아이디어입니다.",
    histCap: "교점의 대수적 인수 분해: $f(x)-g(x)=a(x-\\alpha)(x-\\beta)$",
    fParts: [
      { say: "이차함수 에프 엑스와 일차함수 쥐 엑스가 알파와 베타에서 만나면 차함수 에이치 엑스는 에이 곱하기 엑스 빼기 알파 곱하기 엑스 빼기 베타입니다.", cap: "두 교점 $\\alpha,\\ \\beta\\ \\Longrightarrow\\ f(x)-g(x)=a(x-\\alpha)(x-\\beta)$" },
      { say: "직선이 엑스는 알파에서 이차함수에 접하면 판별식 디가 영이고 차함수는 에이 곱하기 엑스 빼기 알파의 완전제곱입니다.", cap: "접점 $x=\\alpha\\ \\Longrightarrow\\ f(x)-g(x)=a(x-\\alpha)^{2}\\ (D=0)$" },
      { say: "차함수에서 일차항과 상수항만 바뀌고 최고차항 계수 에이는 원래 이차함수와 똑같이 유지됩니다.", cap: "직선 $g(x)$ 를 빼도 2차항 계수 $a$ 는 불변!" }
    ],
    fChips: [
      "\\text{두 교점 }\\alpha,\\ \\beta\\ \\Longrightarrow\\ f(x)-g(x)=a(x-\\alpha)(x-\\beta)",
      "\\text{접점 }x=\\alpha\\ \\Longrightarrow\\ f(x)-g(x)=a(x-\\alpha)^{2}\\quad (D=0)",
      "\\text{두 교점의 중점 }\\dfrac{\\alpha+\\beta}{2}=-\\dfrac{b-m}{2a}"
    ],
    fLabels: ["교점 → 일차인수 곱", "접점 → 완전제곱 인수"],
    exParts: [
      { say: "예를 들어 최고차항 계수가 일인 이차함수 에프 엑스가 직선 와이는 이엑스 더하기 일과 엑스는 일, 삼에서 만날 때 에프 사를 구해 봅시다.", cap: "$f(x)$ 와 $y=2x+1$ 이 $x=1, 3$ 에서 만날 때 $f(4)$" },
      { say: "차함수 에프 엑스 빼기 괄호 이엑스 더하기 일은 엑스 빼기 일 곱하기 엑스 빼기 삼으로 바로 세워집니다.", cap: "$f(x)-(2x+1)=(x-1)(x-3)$" },
      { say: "엑스에 사를 대입하면 에프 사 빼기 구는 삼 곱하기 일이므로 에프 사는 십이입니다.", cap: "$f(4)-9=3\\times 1=3\\ \\Rightarrow\\ f(4)=12$" }
    ],
    exChips: [
      "f(x)-(2x+1)=(x-1)(x-3)",
      "f(x)=(x-1)(x-3)+2x+1",
      "f(4)=(3)(1)+9=12"
    ],
    exLabels: ["차함수 식 작성", "f(4) = 12"],
    exGraph: {
      f: x => 0.45 * (x - 0.6) * (x - 2.4) + 0.85, GY0: 390, GV: 110, xr: [0, 3], area: [0.6, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "교점 x = 1" }, r2: { x: 2.4, col: PK, label: "교점 x = 3" },
      fn: { t: "차함수 h(x) = f(x) − g(x) = a(x − 1)(x − 3)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(x−1)(x−3)", finalS: "f(4) = 12", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 최고차항의 계수가 일인 이차함수 에프 엑스의 그래프가 직선 와이는 삼 엑스 빼기 이보다 항상 위쪽에 있거나 엑스는 이에서 접할 때, 에프 오의 값은 얼마일까요?", cap: "$f(x)$ 가 $y=3x-2$ 와 $x=2$ 에서 접할 때 $f(5)$ 구하기 (자작 문항)" },
      { say: "엑스는 이에서 접하므로 에프 엑스 빼기 괄호 삼 엑스 빼기 이는 엑스 빼기 이의 제곱입니다.", cap: "$f(x)-(3x-2)=(x-2)^{2}$" },
      { say: "엑스에 오를 대입하면 에프 오 빼기 십삼은 구이므로 에프 오는 이십이입니다.", cap: "$f(5)-13=3^{2}=9\\ \\Rightarrow\\ f(5)=22$" }
    ],
    examChips: [
      "x=2\\text{ 에서 접함}\\ \\Longrightarrow\\ f(x)-(3x-2)=(x-2)^{2}",
      "f(x)=(x-2)^{2}+3x-2",
      "f(5)=(5-2)^{2}+15-2=9+13=22"
    ],
    examLabels: ["접점 x=2 → (x−2)²", "정답 f(5) = 22"],
    examGraph: {
      f: x => 0.5 * (x - 1.5) * (x - 1.5) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.5, col: CY, label: "접점 x = 2 (중근)" }, r2: { x: 2.5, col: GO, label: "x = 5 대입" },
      fn: { t: "f(x) − (3x − 2) = (x − 2)²  ⇒  f(5) = 9 + 13 = 22", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(x − 2)²", finalS: "f(5) = 22", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 이차함수식을 에이 엑스 제곱 더하기 비 엑스 더하기 씨로 두고 연립하는 대신 무조건 차함수 인수꼴로 세웁니다.", cap: "① 미지수 $a,b,c$ 연립 금지 $\\Longrightarrow$ 차함수 $f(x)-g(x)$ 인수꼴 직행!" },
      { say: "둘째, 평행한 직선들 중에서 이차함수에 접하는 직선과의 접점에서 곡선까지의 세로 거리가 최대·최소를 결정합니다.", cap: "② 곡선 위의 점과 직선 사이 최소 거리 $\\Longrightarrow$ 기울기가 같은 접선!" },
      { say: "셋째, 이 차함수 기법이 수학 투의 제구강 정적분과 차함수의 마법으로 백 퍼센트 그대로 확장됩니다.", cap: "③ 수학 II 제9강 직결: 둘러싸인 넓이 $=\\int_{\\alpha}^{\\beta}|f(x)-g(x)|\\,dx$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 제한된 범위에서 이차함수의 최대·최소를 대칭축 위치로 푸는 제사십육강입니다.", cap: "제46강 · 제한된 범위에서 이차함수의 최대·최소" },
      { tag: "연계 ②", say: "수학 투에서 차함수로 넓이를 구하는 제구강도 함께 보세요.", cap: "제9강 · 정적분과 넓이 & 차함수의 마법 (수학 II)" },
      { tag: "이 사이트", say: "이 사이트의 제사십육강과 제구강을 이어서 보세요.", cap: "제46강 · 이차함수 최대·최소  /  제9강 · 차함수의 마법" }
    ],
    nextLinks: [
      { lec: 46, label: "제46강 열기 (이차함수 최대·최소)" },
      { lec: 9, label: "제9강 열기 (수학 II 차함수 마법)" },
      { lec: 44, label: "제44강 열기 (판별식과 두 근의 차)" }
    ]
  }
];

const COMMON1_SPECS_B = [
  {
    lec: 46,
    title: "숏츠식 판서 미리보기 · 제한된 범위에서 이차함수의 최대·최소",
    desc: "닫힌구간 $[p, q]$ 에서 이차함수 $y=a(x-m)^{2}+n$ 의 최댓값·최솟값을 대칭축 $x=m$ 과의 가로 거리로 판별합니다.",
    hookTitle: "제한된 범위 이차함수 최대·최소", hookSub: "대칭축에서 가까우면 극값 · 멀수록 반대쪽 끝값!",
    hookSay: "제한된 범위에서 이차함수의 최대·최소를 그래프 다 그리지 않고 대칭축 거리만으로 3초 만에 찾는 법, 바로 정리합니다.",
    hookCap: "이차함수 제한 범위 최대·최소 · 30초 정리",
    whySay: "이차함수는 대칭축 엑스는 엠에 대하여 완전한 좌우 대칭이므로, 대칭축에서 가로 거리가 멀어질수록 함숫값이 단조롭게 커지거나 작아집니다.",
    whyCap: "아래로 볼록($a\\gt 0$): 대칭축 $x=m$ 에서 최소, 대칭축에서 먼 끝점에서 최대!",
    histTag: "대칭 최적화", histSay: "포물선의 대칭축을 기준으로 극값을 판별하는 원리는 페르마의 극대·극소 연구의 출발점이 되었습니다.",
    histCap: "포물선의 선대칭($x=m$)과 구간 경계값 비교 원리",
    fParts: [
      { say: "먼저 이차함수의 대칭축 엑스는 마이너스 이 에이 분의 비를 구하고, 주어진 구간 피부터 큐 안에 들어있는지 확인합니다.", cap: "1단계: 대칭축 $x=m=-\\dfrac{b}{2a}$ 위치 확인" },
      { say: "아래로 볼록할 때 대칭축이 구간 안에 있으면 꼭짓점이 최솟값이고, 대칭축에서 더 먼 쪽 끝점이 최댓값입니다.", cap: "2단계(축 포함): 최소 $=f(m)$, 최대 $=$ 축에서 더 먼 경계의 함숫값" },
      { say: "대칭축이 구간 밖에 있으면 대칭축에서 가까운 끝점이 최소, 먼 끝점이 최대가 됩니다.", cap: "3단계(축 불포함): 양 끝점 $f(p),\\ f(q)$ 중에서만 최대·최소 결정!" }
    ],
    fChips: [
      "\\text{대칭축 }x=m=-\\dfrac{b}{2a}\\in[p,q]\\ (a\\gt 0)\\ \\Longrightarrow\\ \\text{최소 }=f(m)",
      "|x-m|\\text{ 이 클수록 함숫값 증가}\\ \\Longrightarrow\\ \\text{축에서 먼 끝점이 최대!}",
      "m\\notin[p,q]\\ \\Longrightarrow\\ \\text{가까운 끝점이 최소, 먼 끝점이 최대}"
    ],
    fLabels: ["축 포함 여부 확인", "축과의 거리 |x−m| 비교"],
    exParts: [
      { say: "예를 들어 일 이상 사 이하에서 에프 엑스는 엑스 제곱 빼기 사 엑스 더하기 오의 최댓값과 최솟값을 구해 봅시다.", cap: "$1\\le x\\le 4$ 에서 $f(x)=x^{2}-4x+5=(x-2)^{2}+1$" },
      { say: "대칭축 엑스는 이가 구간 안에 있으므로 엑스는 이에서 최솟값 일입니다.", cap: "대칭축 $x=2\\in[1,4]\\ \\Rightarrow\\ \\text{최솟값 }f(2)=1$" },
      { say: "이에서 사까지의 거리가 일까지의 거리보다 멀므로 엑스는 사에서 최댓값 오를 가집니다.", cap: "$|4-2|\\gt |1-2|\\ \\Rightarrow\\ \\text{최댓값 }f(4)=2^{2}+1=5$" }
    ],
    exChips: [
      "f(x)=(x-2)^{2}+1,\\qquad \\text{구간 }[1,4]\\text{ 안에 대칭축 }x=2\\text{ 포함}",
      "\\text{최솟값 }m=f(2)=1",
      "\\text{축 }x=2\\text{ 에서 더 먼 }x=4\\ \\Longrightarrow\\ \\text{최댓값 }M=f(4)=5"
    ],
    exLabels: ["꼭짓점 최소 1", "먼 끝점 x=4 최대 5"],
    exGraph: {
      f: x => 0.45 * (x - 1.2) * (x - 1.2) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.5, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.2, col: CY, label: "대칭축 x = 2 (최소 1)" }, r2: { x: 2.6, col: PK, label: "먼 끝 x = 4 (최대 5)" },
      fn: { t: "대칭축 x = 2 에서 최소 1, 더 먼 끝 x = 4 에서 최대 5", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "축 거리 비교", finalS: "M + m = 6", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 영 이상 삼 이하에서 이차함수 와이는 엑스 제곱 빼기 이엑스 더하기 케이의 최댓값이 칠일 때, 최솟값은 얼마일까요?", cap: "$0\\le x\\le 3$ 에서 $y=x^{2}-2x+k$ 의 최댓값이 $7$ 일 때 최솟값 (자작 문항)" },
      { say: "대칭축 엑스는 일에서 더 먼 엑스는 삼에서 최댓값을 가지므로 삼을 대입한 삼 더하기 케이가 칠, 케이는 사입니다.", cap: "대칭축 $x=1\\ \\Rightarrow\\ x=3$ 에서 최대 $3+k=7\\ \\Rightarrow\\ k=4$" },
      { say: "최솟값은 대칭축 엑스는 일에서의 함숫값이므로 사 빼기 일, 삼입니다.", cap: "최솟값 $=f(1)=1-2+4=3$" }
    ],
    examChips: [
      "y=(x-1)^{2}+k-1,\\qquad x\\in[0,3]",
      "x=3\\text{ 에서 최댓값 }2^{2}+k-1=k+3=7\\ \\Rightarrow\\ k=4",
      "x=1\\text{ 에서 최솟값 }=k-1=3"
    ],
    examLabels: ["x=3 최대 → k=4", "정답 최솟값 3"],
    examGraph: {
      f: x => 0.45 * (x - 0.9) * (x - 0.9) + 0.45, GY0: 390, GV: 110, xr: [0, 3], area: [0.2, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.9, col: CY, label: "x = 1 (최소 k−1)" }, r2: { x: 2.5, col: GO, label: "x = 3 (최대 k+3=7)" },
      fn: { t: "최대(x=3)와 최소(x=1)의 높이 차 = (3 − 1)² = 4!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "높이 차 = 2² = 4", finalS: "최솟값 = 7 − 4 = 3", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 최댓값과 최솟값의 차는 상수 케이와 무관하게 최고차항 계수 곱하기 가로 거리의 제곱이므로 케이를 구하지 않고도 바로 나옵니다.", cap: "① 꿀팁: $M-m=|a|(x_{\\text{먼}}-m)^{2}$ (상수항 $k$ 구할 필요 없이 즉시 암산!)" },
      { say: "둘째, 대칭축에 미지수 에이가 들어 있으면 축이 구간 왼쪽, 내부, 오른쪽에 있는 세 가지 경우로 나눕니다.", cap: "② 미지수 대칭축 $x=a$: ① $a\\lt p$ · ② $p\\le a\\le q$ · ③ $a\\gt q$ 3분할" },
      { say: "셋째, 공통부분을 티로 치환할 때는 반드시 티의 새로운 제한 범위를 먼저 구해야 합니다.", cap: "③ 치환의 철칙: $t=g(x)$ 치환 즉시 $t$ 의 범위부터 표시!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 삼차방정식의 세 근의 구조와 켤레근 성질을 다루는 제사십칠강입니다.", cap: "제47강 · 삼차방정식 세 근의 구조와 켤레근" },
      { tag: "연계 ②", say: "합성함수 치환과 그래프를 다루는 제이십이강도 이어서 보세요.", cap: "제22강 · 합성함수 그래프 그리기 (N축 스킬)" },
      { tag: "이 사이트", say: "이 사이트의 제사십칠강과 제이십이강을 이어서 보세요.", cap: "제47강 · 삼차방정식 근의 구조  /  제22강 · 합성함수 그래프" }
    ],
    nextLinks: [
      { lec: 47, label: "제47강 열기 (삼차방정식 근의 구조)" },
      { lec: 22, label: "제22강 열기 (합성함수 N축)" },
      { lec: 45, label: "제45강 열기 (차함수의 탄생)" }
    ]
  },
  {
    lec: 47,
    title: "숏츠식 판서 미리보기 · 삼차방정식 세 근의 구조와 켤레근",
    desc: "실계수 삼차방정식 $ax^{3}+bx^{2}+cx+d=0$ 의 근과 계수의 관계와 실근·중근·허근 구조 판별법을 정리합니다.",
    hookTitle: "삼차방정식 세 근의 구조와 켤레근", hookSub: "반드시 실근 1개 이상 · 조립제법 후 판별식 D!",
    hookSay: "삼차방정식이 중근이나 허근을 가질 조건을 실수 없이 판별하는 핵심 공식, 30초 만에 정리합니다.",
    hookCap: "삼차방정식 근의 구조 · 30초 정리",
    whySay: "삼차방정식은 인수분해하면 일차식 곱하기 이차식이 되므로, 조립제법으로 실근 하나를 먼저 찾은 뒤 남은 이차식의 판별식만 보면 모든 근의 구조가 결정됩니다.",
    whyCap: "$(x-\\alpha)(ax^{2}+px+q)=0$ 분해 후 이차식 판별식 $D$ 와 $x=\\alpha$ 대입 체크!",
    histTag: "카르다노·비에트", histSay: "삼차방정식의 일반 해법은 16세기 카르다노와 타르탈리아가 밝혔고, 세 근과 계수의 대칭 관계는 비에트가 완성했습니다.",
    histCap: "카르다노의 삼차방정식 해법과 3차 비에트 정리",
    fParts: [
      { say: "삼차방정식의 세 근의 합은 마이너스 에이분의 비, 두 개씩 곱의 합은 에이분의 씨, 세 근의 곱은 마이너스 에이분의 디입니다.", cap: "$\\alpha+\\beta+\\gamma=-\\dfrac{b}{a},\\quad \\alpha\\beta+\\beta\\gamma+\\gamma\\alpha=\\dfrac{c}{a},\\quad \\alpha\\beta\\gamma=-\\dfrac{d}{a}$" },
      { say: "실계수 삼차방정식이 한 허근 피 더하기 큐 아이를 가지면 켤레복소수 피 빼기 큐 아이도 반드시 근이고 나머지 한 근은 실근입니다.", cap: "실계수 켤레근: $p+qi$ 가 근 $\\Longrightarrow\\ p-qi$ 도 근 (나머지 1개는 실근)" },
      { say: "삼차방정식이 중근을 가질 조건은 인수분해 후 이차식이 중근을 갖거나, 이차식이 앞의 실근 알파를 근으로 갖는 두 가지입니다.", cap: "중근 2케이스: ① 이차식 $D=0$ 또는 ② 이차식에 $x=\\alpha$ 대입 $=0$ (놓치기 쉬움!)" }
    ],
    fChips: [
      "\\alpha+\\beta+\\gamma=-\\dfrac{b}{a},\\quad \\alpha\\beta+\\beta\\gamma+\\gamma\\alpha=\\dfrac{c}{a},\\quad \\alpha\\beta\\gamma=-\\dfrac{d}{a}",
      "(x-\\alpha)(x^{2}+px+q)=0\\text{ 중근}\\iff D=0\\text{ 또는 }\\alpha^{2}+p\\alpha+q=0",
      "\\text{실계수 방정식 허근 }p+qi\\ \\Longrightarrow\\ \\text{켤레근 }p-qi\\text{ 자동 확정!}"
    ],
    fLabels: ["근과 계수의 관계 (부호 교대)", "중근 2가지 케이스 & 켤레근"],
    exParts: [
      { say: "예를 들어 삼차방정식 엑스 세제곱 빼기 삼 엑스 제곱 더하기 에이 엑스 더하기 비는 영의 한 근이 일 더하기 아이일 때 실수 에이, 비를 구해 봅시다.", cap: "$x^{3}-3x^{2}+ax+b=0$ 의 한 근이 $1+i$ 일 때 $a+b$" },
      { say: "켤레근 일 빼기 아이도 근이고, 세 근의 합이 삼이므로 나머지 실근 하나는 일입니다.", cap: "두 허근의 합 $=2$, 세 근의 합 $=3\\ \\Rightarrow\\ \\text{나머지 실근 }=1$" },
      { say: "두 허근의 곱은 이므로 세 근 일, 일 더하기 아이, 일 빼기 아이로부터 에이는 사, 비는 마이너스 이가 됩니다.", cap: "$a=2+2=4,\\quad b=-(1\\times 2)=-2\\ \\Rightarrow\\ a+b=2$" }
    ],
    exChips: [
      "\\text{세 근: }1+i,\\ 1-i,\\ \\gamma\\quad (\\text{합 }=2+\\gamma=3\\ \\Rightarrow\\ \\gamma=1)",
      "\\text{두 개씩 곱의 합 }a=1\\cdot(2)+(1+i)(1-i)=2+2=4",
      "\\text{세 근의 곱 }-b=1\\cdot 2=2\\ \\Rightarrow\\ b=-2,\\quad a+b=2"
    ],
    exLabels: ["세 근의 합 = 3 → 실근 1", "a = 4, b = −2"],
    exGraph: {
      f: x => 0.4 * (x - 1.5) * ((x - 1.5) * (x - 1.5) - 1.2) + 1.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "실근 α" }, r2: { x: 2.3, col: PK, label: "이차식 판별식 D" },
      fn: { t: "삼차방정식 = (x − α)(이차식) = 0 으로 쪼개어 해석!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "켤레근 1 ± i", finalS: "a + b = 2", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 삼차방정식 괄호 엑스 빼기 이 곱하기 괄호 엑스 제곱 빼기 이 케이 엑스 더하기 사가 중근을 갖도록 하는 모든 양수 케이의 값의 합은 얼마일까요?", cap: "$(x-2)(x^{2}-2kx+4)=0$ 이 중근을 갖는 양수 $k$ 의 합 (자작 문항)" },
      { say: "첫째, 뒤의 이차식이 중근을 가질 때 사분의 디는 케이 제곱 빼기 사가 영이므로 양수 케이는 이입니다.", cap: "케이스 ①: $D/4=k^{2}-4=0\\ \\Rightarrow\\ k=2$ (이때 중근 $x=2$, 삼중근)" },
      { say: "둘째, 뒤의 이차식이 엑스는 이를 근으로 가질 때도 사 빼기 사 케이 더하기 사는 영에서 케이는 이가 되어 양수 케이는 이 하나뿐입니다.", cap: "케이스 ②: $x=2$ 대입 $4-4k+4=0\\ \\Rightarrow\\ k=2$ (동일) $\\Rightarrow$ 정답 $2$" }
    ],
    examChips: [
      "(x-2)(x^{2}-2kx+4)=0\\text{ 의 중근 조건}",
      "\\text{① }D/4=k^{2}-4=0\\ \\Rightarrow\\ k=2\\ (k\\gt 0)",
      "\\text{② }x=2\\text{ 대입: }8-4k=0\\ \\Rightarrow\\ k=2\\ \\Longrightarrow\\ \\text{양수 }k=2"
    ],
    examLabels: ["D=0 과 x=2 대입 점검", "정답 k = 2"],
    examGraph: {
      f: x => 0.35 * Math.pow(x - 1.5, 3) + 1.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.5, col: CY, label: "x = 2 (중근·삼중근)" }, r2: { x: 2.4, col: GO, label: "k = 2" },
      fn: { t: "중근 조건: ① 이차식 D = 0  또는  ② 이차식에 앞의 근 대입 = 0", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "k² − 4 = 0", finalS: "k = 2", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 삼차방정식의 중근 조건에서 뒤의 이차식에 앞의 일차식 근을 대입하는 두 번째 케이스를 절대 빠뜨리면 안 됩니다.", cap: "① 서술형 감점 1순위: 이차식에 앞의 실근 $x=\\alpha$ 대입 케이스 필수 확인!" },
      { say: "둘째, 미지수 케이가 포함된 삼차식은 케이가 있는 항끼리 묶어 케이가 지워지는 엑스 값을 넣으면 조립제법 실근이 바로 보입니다.", cap: "② 미지수 $k$ 포함 조립제법: $k$ 에 관해 정리해 $k$ 가 소거되는 $x$ 대입!" },
      { say: "셋째, 모든 실계수 홀수차 방정식은 그래프가 위아래 끝을 통과하므로 적어도 하나의 실근을 무조건 가집니다.", cap: "③ 홀수차 실계수 방정식 $\\Longrightarrow$ 실근 최소 1개 무조건 존재!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 절댓값 기호를 포함한 부등식과 거리 합 그래프를 다루는 제사십팔강입니다.", cap: "제48강 · 절댓값 부등식과 거리 합 $|x-a|+|x-b|$ 그래프" },
      { tag: "연계 ②", say: "삼차함수 비율관계와 극대·극소 높이차를 다루는 제삼십칠강도 이어서 보세요.", cap: "제37강 · 삼차함수 비율관계와 극대·극소 높이차 공식" },
      { tag: "이 사이트", say: "이 사이트의 제사십팔강과 제삼십칠강을 이어서 보세요.", cap: "제48강 · 절댓값 부등식  /  제37강 · 삼차함수 비율관계" }
    ],
    nextLinks: [
      { lec: 48, label: "제48강 열기 (절댓값 부등식)" },
      { lec: 37, label: "제37강 열기 (삼차함수 비율관계)" },
      { lec: 46, label: "제46강 열기 (이차함수 최대·최소)" }
    ]
  },
  {
    lec: 48,
    title: "숏츠식 판서 미리보기 · 절댓값 부등식과 거리 합 그래프",
    desc: "$|x-a|+|x-b|$ 를 수직선 위 두 점까지의 거리의 합으로 해석하고 평평한 바닥(최솟값 $|b-a|$) 개형을 정리합니다.",
    hookTitle: "절댓값 부등식 · 거리 합과 바닥 공식", hookSub: "|x − a| + |x − b| 최솟값 = |b − a| 3초 풀이",
    hookSay: "구간을 일일이 나누지 않고 절댓값 합 부등식을 3초 만에 푸는 거리 해석과 바닥 그래프, 바로 정리합니다.",
    hookCap: "절댓값 거리 합 그래프 · 30초 정리",
    whySay: "절댓값 엑스 빼기 에이는 수직선에서 점 에이까지의 거리이므로, 두 절댓값의 합은 에이와 비 사이에 있을 때 항상 에이와 비 사이의 거리로 일정한 최솟값을 가집니다.",
    whyCap: "$a\\le x\\le b$ 에서 $|x-a|+|x-b|=(x-a)+(b-x)=b-a$ (평평한 바닥!)",
    histTag: "거리 공간", histSay: "절댓값을 두 점 사이의 거리 함수로 해석하는 관점은 바이어슈트라스와 프레셰의 거리 공간 이론으로 발전했습니다.",
    histCap: "수직선 위의 거리 함수 $d(x,a)=|x-a|$ 와 삼각부등식",
    fParts: [
      { say: "절댓값 엑스 빼기 에이가 케이보다 작다는 것은 에이로부터 거리가 케이 미만인 열린구간입니다.", cap: "$|x-a|\\lt k\\ \\Longleftrightarrow\\ -k\\lt x-a\\lt k\\ \\Longleftrightarrow\\ a-k\\lt x\\lt a+k$" },
      { say: "두 절댓값의 합 와이는 절댓값 엑스 빼기 에이 더하기 절댓값 엑스 빼기 비는 에이와 비 사이에서 높이가 비 빼기 에이로 평평한 사발 모양입니다.", cap: "$a\\le x\\le b$ 구간에서 $y=b-a$ 일정 (최솟값 $=b-a$)" },
      { say: "양 끝 바깥에서는 기울기가 플러스 마이너스 이인 직선으로 올라가므로, 높이가 씨 이하가 되는 가로 폭을 대칭으로 바로 구합니다.", cap: "바깥 기울기 $=\\pm 2$ (여유 높이 $\\Delta y$ 의 절반씩 양옆으로 확장!)" }
    ],
    fChips: [
      "|x-a|\\le k\\ \\Longleftrightarrow\\ a-k\\le x\\le a+k\\quad (k\\ge 0)",
      "y=|x-a|+|x-b|\\ (a\\lt b)\\ \\Longrightarrow\\ a\\le x\\le b\\text{ 에서 최솟값 }b-a",
      "|x-a|+|x-b|\\le c\\ (c\\ge b-a)\\ \\Longrightarrow\\ \\text{해의 길이 }=c"
    ],
    fLabels: ["에이·비 사이 평평한 바닥", "기울기 ±2 대칭 확장"],
    exParts: [
      { say: "예를 들어 부등식 절댓값 엑스 빼기 일 더하기 절댓값 엑스 빼기 오가 팔 이하인 해를 구해 봅시다.", cap: "$|x-1|+|x-5|\\le 8$ 의 해 구하기" },
      { say: "일과 오 사이에서 바닥 높이는 사이고, 팔이 되려면 위로 사만큼 더 올라가야 하는데 기울기가 이므로 양옆으로 이씩 넓어집니다.", cap: "바닥 높이 $=5-1=4$, 여유 높이 $8-4=4\\ \\Rightarrow$ 좌우로 $\\dfrac{4}{2}=2$ 확장" },
      { say: "따라서 일에서 왼쪽으로 이 간 마이너스 일부터 오에서 오른쪽으로 이 간 칠까지입니다.", cap: "$-1\\le x\\le 7$ (양 끝의 차 $=7-(-1)=8$)" }
    ],
    exChips: [
      "|x-1|+|x-5|\\le 8\\quad (\\text{바닥 구간 }[1,5],\\ \\text{최솟값 }5-1=4)",
      "\\text{여유 높이 }8-4=4,\\quad \\text{기울기 }2\\ \\Rightarrow\\ \\text{좌우 }\\dfrac{4}{2}=2\\text{ 씩 확장}",
      "1-2\\le x\\le 5+2\\ \\Longrightarrow\\ -1\\le x\\le 7"
    ],
    exLabels: ["바닥 높이 4, 여유 4", "좌우 2씩 확장 → [−1, 7]"],
    exGraph: {
      f: x => Math.abs(x - 0.8) + Math.abs(x - 2.2) - 0.9, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.8, col: CY, label: "꺾임점 x = a" }, r2: { x: 2.2, col: PK, label: "꺾임점 x = b" },
      fn: { t: "y = |x − a| + |x − b| : [a, b] 에서 평평한 바닥 (최소 b − a)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "바닥 높이 = b − a", finalS: "−1 ≤ x ≤ 7", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 모든 실수 엑스에 대하여 부등식 절댓값 엑스 빼기 이 더하기 절댓값 엑스 더하기 삼이 케이 이상이 항상 성립하도록 하는 실수 케이의 최댓값은 얼마일까요?", cap: "모든 실수 $x$ 에 대해 $|x-2|+|x+3|\\ge k$ 성립하는 $k$ 최댓값 (자작 문항)" },
      { say: "좌변 함수의 최솟값은 두 기준점 마이너스 삼과 이 사이의 거리입니다.", cap: "좌변 최솟값 $=2-(-3)=5$ ($-3\\le x\\le 2$ 에서 일정)" },
      { say: "항상 케이 이상이려면 케이가 최솟값 오 이하이어야 하므로 케이의 최댓값은 오입니다.", cap: "$k\\le 5\\ \\Rightarrow\\ \\text{최댓값 }5$" }
    ],
    examChips: [
      "f(x)=|x-2|+|x-(-3)|",
      "\\text{최솟값 }=2-(-3)=5\\quad (-3\\le x\\le 2)",
      "k\\le 5\\ \\Longrightarrow\\ k\\text{ 의 최댓값 }=5"
    ],
    examLabels: ["두 기준점 거리 = 5", "정답 5"],
    examGraph: {
      f: x => Math.abs(x - 0.7) + Math.abs(x - 2.3) - 1.0, GY0: 390, GV: 110, xr: [0, 3], area: [0.7, 2.3], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "x = −3" }, r2: { x: 2.3, col: GO, label: "x = 2 (거리 5)" },
      fn: { t: "|x − 2| + |x + 3| 의 최솟값 = |2 − (−3)| = 5", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "2 − (−3) = 5", finalS: "최댓값 k = 5", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 절댓값이 홀수 개 더해지면 가운데 기준점 하나에서 뾰족한 최솟값을 갖고, 짝수 개 더해지면 가운데 구간 전체가 평평한 바닥이 됩니다.", cap: "① 홀수 개 합: 중앙값 1점에서 최소 · 짝수 개 합: 중앙 구간 전체에서 최소!" },
      { say: "둘째, 절댓값 엑스 빼기 에이 더하기 절댓값 엑스 빼기 비가 씨 이하일 때 해가 존재하면 양 끝점의 차는 언제나 씨와 같습니다.", cap: "② $|x-a|+|x-b|\\le c\\ (c\\ge |b-a|)$ 의 해 $\\alpha\\le x\\le\\beta\\ \\Rightarrow\\ \\beta-\\alpha=c$" },
      { say: "셋째, 절댓값 그래프의 대칭 이동은 제십삼강의 네 가지 절댓값 그래프 규칙과 함께 보면 완벽합니다.", cap: "③ 제13강 연계: 꺾임점 좌표만 대입해 직선으로 이으면 개형 완성!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 이차방정식 실근의 위치를 함숫값, 판별식, 대칭축 세 가지로 판별하는 제사십구강입니다.", cap: "제49강 · 이차방정식 실근의 위치 (근의 분리: 함·판·축)" },
      { tag: "연계 ②", say: "절댓값 그래프 4대 유형을 다루는 제십삼강도 함께 보세요.", cap: "제13강 · $y$ 와 $f(x)$ 차이 & 절댓값 그래프" },
      { tag: "이 사이트", say: "이 사이트의 제사십구강과 제십삼강을 이어서 보세요.", cap: "제49강 · 근의 분리(함·판·축)  /  제13강 · 절댓값 그래프" }
    ],
    nextLinks: [
      { lec: 49, label: "제49강 열기 (근의 분리 함·판·축)" },
      { lec: 13, label: "제13강 열기 (절댓값 4대 그래프)" },
      { lec: 47, label: "제47강 열기 (삼차방정식 근의 구조)" }
    ]
  },
  {
    lec: 49,
    title: "숏츠식 판서 미리보기 · 이차방정식 실근의 위치 (근의 분리: 함·판·축)",
    desc: "이차방정식의 두 실근이 특정 값 $p$ 보다 크거나 두 수 사이에 있을 조건을 경계 함숫값·판별식·대칭축 3단계로 정리합니다.",
    hookTitle: "이차방정식 근의 분리 · 함·판·축 법칙", hookSub: "경계 함숫값(함) · 판별식(판) · 대칭축(축) 3초 판별",
    hookSay: "이차방정식의 두 근이 일보다 크다거나 두 근 사이에 일이 있다는 조건을 3초 만에 식으로 바꾸는 함·판·축 법칙, 바로 정리합니다.",
    hookCap: "이차방정식 근의 분리(함·판·축) · 30초 정리",
    whySay: "두 근이 모두 피보다 크려면 경계 함숫값만 양수여서는 부족하고, 엑스축과 만나야 하므로 판별식 조건과 대칭축 위치까지 세 가지를 모두 만족해야 그래프가 하나로 고정됩니다.",
    whyCap: "두 근 모두 $\\gt p$: ① $f(p)\\gt 0$ (함) + ② $D\\ge 0$ (판) + ③ 축 $\\gt p$ (축)",
    histTag: "실근 분리", histSay: "다항방정식의 실근이 존재하는 구간을 부호 변화로 분리하는 원리는 볼차노의 사이값 정리와 연결됩니다.",
    histCap: "경계에서의 함숫값 부호(사이값 정리)와 포물선 개형 고정",
    fParts: [
      { say: "아래로 볼록한 이차함수의 두 근이 모두 피보다 크려면 에프 피가 양수, 판별식이 영 이상, 대칭축이 피보다 커야 합니다.", cap: "두 근 $\\gt p$: ① $f(p)\\gt 0$ · ② $D\\ge 0$ · ③ 대칭축 $-\\dfrac{b}{2a}\\gt p$" },
      { say: "반면 두 근 사이에 피가 있을 때는 경계 함숫값 에프 피가 음수라는 조건 단 하나만 쓰면 됩니다.", cap: "두 근 사이에 $p$ 존재 ($\\alpha\\lt p\\lt\\beta$): $f(p)\\lt 0$ 단 1개로 끝!" },
      { say: "왜냐하면 아래로 볼록한 함수가 한 점에서 음수이면 위로 올라가면서 엑스축을 무조건 두 번 뚫고 지나가 판별식이 자동으로 양수가 되기 때문입니다.", cap: "$a\\gt 0$ 이고 $f(p)\\lt 0\\ \\Longrightarrow\\ D\\gt 0$ 자동 성립 (판·축 생략!)" }
    ],
    fChips: [
      "\\text{두 근 모두 }\\gt p\\ :\\ \\text{① }f(p)\\gt 0\\quad \\text{② }D\\ge 0\\quad \\text{③ 축 }\\gt p",
      "\\text{두 근 사이에 }p\\text{ 존재 }(\\alpha\\lt p\\lt\\beta)\\ :\\ f(p)\\lt 0\\text{ (단 1개 조건!)}",
      "\\text{두 근이 }(p,q)\\text{ 사이 : }f(p)\\gt 0,\\ f(q)\\gt 0,\\ D\\ge 0,\\ p\\lt\\text{축}\\lt q"
    ],
    fLabels: ["같은 쪽 → 함·판·축 3개", "근 사이 → 함숫값 < 0 단 1개!"],
    exParts: [
      { say: "예를 들어 이차방정식 엑스 제곱 빼기 이 케이 엑스 더하기 케이 더하기 육은 영의 두 근 사이에 일이 있을 때 정수 케이의 최솟값을 구해 봅시다.", cap: "$x^{2}-2kx+k+6=0$ 의 두 근 사이에 $1$ 이 있을 조건" },
      { say: "두 근 사이에 일이 있으므로 함숫값 에프 일이 음수라는 조건 하나만 쓰면 됩니다.", cap: "$f(1)=1-2k+k+6\\lt 0$" },
      { say: "칠 빼기 케이가 음수이므로 케이는 칠보다 크고, 정수 케이의 최솟값은 팔입니다.", cap: "$7-k\\lt 0\\ \\Rightarrow\\ k\\gt 7\\ \\Rightarrow\\ \\text{최소 정수 }8$" }
    ],
    exChips: [
      "f(x)=x^{2}-2kx+k+6\\quad (\\text{두 근 사이에 }1\\text{ 존재})",
      "f(1)=1-2k+k+6\\lt 0",
      "k\\gt 7\\ \\Longrightarrow\\ \\text{정수 }k\\text{ 의 최솟값 }=8"
    ],
    exLabels: ["f(1) < 0 단 1개 적용", "k > 7 → 최소 정수 8"],
    exGraph: {
      f: x => 0.5 * (x - 0.5) * (x - 2.3) + 0.85, GY0: 390, GV: 110, xr: [0, 3], area: [0.5, 2.3], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "근 α < 1" }, r2: { x: 2.3, col: PK, label: "근 β > 1 (f(1) < 0)" },
      fn: { t: "두 근 사이에 p 가 있을 때 ⇔ f(p) < 0 단 하나로 끝!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "f(1) < 0", finalS: "k > 7 (최소 8)", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 이차방정식 엑스 제곱 빼기 두 배의 케이 엑스 더하기 사 케이는 영의 두 실근이 모두 일보다 크도록 하는 자연수 케이의 최솟값은 얼마일까요?", cap: "$x^{2}-2kx+4k=0$ 의 두 실근이 모두 $1$ 보다 클 자연수 $k$ 최솟값 (자작 문항)" },
      { say: "함숫값 에프 일은 일 더하기 이 케이가 양수, 대칭축 케이는 일보다 크고, 판별식 케이 제곱 빼기 사 케이가 영 이상이어야 합니다.", cap: "① $f(1)=1+2k\\gt 0$ · ② 축 $k\\gt 1$ · ③ $D/4=k(k-4)\\ge 0$" },
      { say: "세 조건의 공통범위는 케이가 사 이상이므로 자연수 케이의 최솟값은 사입니다.", cap: "공통범위 $k\\ge 4\\ \\Rightarrow\\ \\text{최솟값 }4$" }
    ],
    examChips: [
      "\\text{① }f(1)=1+2k\\gt 0\\quad \\text{② 축 }k\\gt 1",
      "\\text{③ }D/4=k^{2}-4k=k(k-4)\\ge 0\\ \\Rightarrow\\ k\\le 0\\text{ 또는 }k\\ge 4",
      "\\text{공통범위 }k\\ge 4\\ \\Longrightarrow\\ \\text{자연수 }k\\text{ 최솟값 }=4"
    ],
    examLabels: ["함·판·축 3조건 교집합", "정답 4"],
    examGraph: {
      f: x => 0.55 * (x - 1.2) * (x - 2.4) + 0.75, GY0: 390, GV: 110, xr: [0, 3], area: [1.2, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "경계 p = 1 (f(1)>0)" }, r2: { x: 1.8, col: GO, label: "대칭축 k ≥ 4" },
      fn: { t: "두 근 > 1 : f(1) > 0, 축 > 1, D ≥ 0  ⇒  k ≥ 4", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "함·판·축 교집합", finalS: "최소 자연수 k = 4", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 문제에 서로 다른 두 실근이라는 말이 없으면 두 실근은 중근을 포함하므로 판별식에 반드시 등호를 넣습니다.", cap: "① ‘서로 다른’ 문구가 없으면 $\\Longrightarrow$ $D\\ge 0$ (등호 필수!)" },
      { say: "둘째, 두 근의 부호가 양수와 음수라는 조건은 두 근 사이에 영이 있다는 뜻이므로 에프 영이 음수, 즉 두 근의 곱이 음수 하나만 씁니다.", cap: "② 양근 1개·음근 1개 $\\Longleftrightarrow$ 두 근 사이에 $0$ 존재 $\\Longleftrightarrow\\ f(0)\\lt 0$" },
      { say: "셋째, 지수방정식에서 이의 엑스 제곱을 티로 치환해 두 양근을 가지려면 티가 일보다 큰 두 근을 가져야 하므로 이 근의 분리로 풉니다.", cap: "③ 수학 I 지수치환 연결: $x\\gt 0\\ \\Longleftrightarrow\\ t=2^{x}\\gt 1$ 인 근의 분리!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 경우의 수 합의 법칙·곱의 법칙과 순열·조합을 완벽히 구분하는 제오십강입니다.", cap: "제50강 · 합·곱의 법칙과 순열(${}_{n}\\mathrm{P}_{r}$)·조합(${}_{n}\\mathrm{C}_{r}$)" },
      { tag: "연계 ②", say: "지수·로그 치환 방정식으로 연결되는 제삼십일강도 함께 보세요.", cap: "제31강 · 지수함수와 로그함수 총정리 (수학 I)" },
      { tag: "이 사이트", say: "이 사이트의 제오십강과 제삼십일강을 이어서 보세요.", cap: "제50강 · 경우의 수와 순열·조합  /  제31강 · 지수·로그함수" }
    ],
    nextLinks: [
      { lec: 50, label: "제50강 열기 (순열과 조합)" },
      { lec: 31, label: "제31강 열기 (지수·로그 총정리)" },
      { lec: 48, label: "제48강 열기 (절댓값 부등식)" }
    ]
  },
  {
    lec: 50,
    title: "숏츠식 판서 미리보기 · 합·곱의 법칙과 순열(nPr)·조합(nCr) 완벽 구분",
    desc: "동시·연속 사건의 곱의 법칙과 순서 유무에 따른 순열 ${}_{n}\\mathrm{P}_{r}$, 조합 ${}_{n}\\mathrm{C}_{r}=\\frac{{}_{n}\\mathrm{P}_{r}}{r!}$ 의 관계를 정리합니다.",
    hookTitle: "순열(nPr) vs 조합(nCr) 3초 구분법", hookSub: "뽑기만 하면 조합(nCr) · 뽑아서 줄 세우면 순열(nPr)!",
    hookSay: "순열을 쓸지 조합을 쓸지 헷갈리는 경우의 수 문제를 3초 만에 구분하는 기준, 바로 정리합니다.",
    hookCap: "순열·조합 구분 공식 · 30초 정리",
    whySay: "모든 순열은 먼저 알 명을 순서 없이 뽑는 조합을 한 뒤, 뽑힌 알 명을 일렬로 줄 세우는 알 팩토리얼을 곱한 두 단계 과정입니다.",
    whyCap: "$\\text{순열 }{}_{n}\\mathrm{P}_{r}=\\underbrace{{}_{n}\\mathrm{C}_{r}}_{\\text{뽑기}}\\times\\underbrace{r!}_{\\text{배열}}\\ \\Longleftrightarrow\\ {}_{n}\\mathrm{C}_{r}=\\dfrac{{}_{n}\\mathrm{P}_{r}}{r!}$",
    histTag: "파스칼·페르마", histSay: "조합의 대칭성과 이항계수의 성질은 17세기 파스칼의 삼각형 연구에서 체계화되었습니다.",
    histCap: "파스칼의 삼각형과 조합 항등식 ${}_{n}\\mathrm{C}_{r}={}_{n}\\mathrm{C}_{n-r}$",
    fParts: [
      { say: "서로 다른 엔 개에서 알 개를 뽑기만 하면 조합 엔 씨 알이고, 뽑아서 서로 다른 자리에 배정하면 순열 엔 피 알입니다.", cap: "자리가 구별됨(반장·부반장) $\\Rightarrow\\ {}_{n}\\mathrm{P}_{r}$ · 구별 없음(대표 2명) $\\Rightarrow\\ {}_{n}\\mathrm{C}_{r}$" },
      { say: "엔 씨 알은 엔 피 알을 중복되는 순서 가짓수인 알 팩토리얼로 나눈 값이며, 엔 씨 엔 빼기 알과 같습니다.", cap: "${}_{n}\\mathrm{C}_{r}=\\dfrac{n(n-1)\\cdots(n-r+1)}{r!}=\\dfrac{n!}{r!(n-r)!}={}_{n}\\mathrm{C}_{n-r}$" },
      { say: "크기 순서가 이미 정해진 배열이나 증가함수 에프의 개수는 줄 세우는 방법이 한 가지뿐이므로 무조건 조합으로 풉니다.", cap: "$x_{1}\\lt x_{2}\\Rightarrow f(x_{1})\\lt f(x_{2})$ 함수 개수 $=$ 공역에서 정의역 개수만큼 뽑기 ${}_{n}\\mathrm{C}_{r}$!" }
    ],
    fChips: [
      "{}_{n}\\mathrm{P}_{r}={}_{n}\\mathrm{C}_{r}\\times r!\\qquad \\Longleftrightarrow\\qquad {}_{n}\\mathrm{C}_{r}=\\dfrac{{}_{n}\\mathrm{P}_{r}}{r!}={}_{n}\\mathrm{C}_{n-r}",
      "\\text{이웃 조건: 묶어서 1개로 배열}\\times(\\text{묶음 내부 배열})",
      "\\text{순서가 정해진 배열(증가함수 }f\\text{): 뽑기만 하면 자동 배정 }\\Longrightarrow\\ {}_{n}\\mathrm{C}_{r}"
    ],
    fLabels: ["순열 = 뽑기(조합) × 나열(r!)", "이웃 묶기 & 증가함수 조합"],
    exParts: [
      { say: "예를 들어 다섯 개의 숫자 일, 이, 삼, 사, 오 중에서 세 개를 뽑아 백의 자리, 십의 자리, 일의 자리 숫자가 커지는 세 자리 자연수의 개수를 구해 봅시다.", cap: "백의 자리 $\\lt$ 십의 자리 $\\lt$ 일의 자리인 세 자리 수의 개수" },
      { say: "숫자 세 개만 뽑으면 작은 수부터 자리가 한 가지로 자동 결정됩니다.", cap: "세 숫자 선택 즉시 크기순 배열 $1$가지 확정!" },
      { say: "따라서 오 씨 삼은 오 씨 이와 같으므로 십 개입니다.", cap: "${}_{5}\\mathrm{C}_{3}={}_{5}\\mathrm{C}_{2}=\\dfrac{5\\times 4}{2\\times 1}=10$" }
    ],
    exChips: [
      "a\\lt b\\lt c\\text{ 인 세 자리 자연수 }\\overline{abc}",
      "\\{1,2,3,4,5\\}\\text{ 중 }3\\text{개를 뽑기만 하면 순서 자동 확정!}",
      "{}_{5}\\mathrm{C}_{3}={}_{5}\\mathrm{C}_{2}=\\dfrac{5\\times 4}{2}=10"
    ],
    exLabels: ["순서 고정 → 조합", "정답 10개"],
    exGraph: {
      f: x => 1.65 * Math.exp(-0.9 * (x - 1.5) * (x - 1.5)) + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "nCr = nCn−r 대칭" }, r2: { x: 2.3, col: PK, label: "순열 = nCr × r!" },
      fn: { t: "선(先) 선택 nCr  ×  후(後) 나열 r!  =  순열 nPr", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "5C3 = 5C2", finalS: "10가지", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 집합 엑스는 일, 이, 삼에서 집합 와이는 일, 이, 삼, 사, 오, 육으로의 함수 에프 중에서 에프 일이 에프 이보다 작고 에프 이가 에프 삼보다 작은 함수의 개수는 몇 개일까요?", cap: "$X=\\{1,2,3\\}\\to Y=\\{1,2,3,4,5,6\\}$ 에서 $f(1)\\lt f(2)\\lt f(3)$ 인 함수 개수 (자작 문항)" },
      { say: "공역의 여섯 개 원소 중에서 서로 다른 세 개를 뽑기만 하면 작은 값부터 에프 일, 에프 이, 에프 삼에 자동 대응됩니다.", cap: "공역 $6$개 중 $3$개 선택 $\\Rightarrow\\ {}_{6}\\mathrm{C}_{3}$" },
      { say: "육 곱하기 오 곱하기 사를 삼 팩토리얼 육으로 나누면 정답은 이십입니다.", cap: "${}_{6}\\mathrm{C}_{3}=\\dfrac{6\\times 5\\times 4}{3\\times 2\\times 1}=20$" }
    ],
    examChips: [
      "f(1)\\lt f(2)\\lt f(3)\\ \\Longrightarrow\\ \\text{순서가 정해진 대응(조합)}",
      "\\text{공역 }6\\text{개 원소 중 }3\\text{개 선택: }{}_{6}\\mathrm{C}_{3}",
      "\\dfrac{6\\times 5\\times 4}{6}=20"
    ],
    examLabels: ["증가함수 → 6C3", "정답 20"],
    examGraph: {
      f: x => 1.65 * Math.exp(-0.9 * (x - 1.5) * (x - 1.5)) + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "정의역 3개" }, r2: { x: 2.3, col: GO, label: "공역 6개 중 3개 선택" },
      fn: { t: "f(1) < f(2) < f(3) 증가함수 개수 = 6C3 = 20", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "6C3 = (6·5·4)/6", finalS: "20개", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 복잡한 배열 문제는 처음부터 피를 쓰지 말고 먼저 씨로 뽑은 뒤 팩토리얼을 곱하는 습관을 들이면 절대 안 틀립니다.", cap: "① 실전 공식: (먼저 ${}_{n}\\mathrm{C}_{r}$ 로 뽑기) $\\times$ (나중에 줄 세우기)" },
      { say: "둘째, 이웃하지 않게 배열할 때는 상관없는 것들을 먼저 배열하고 양 끝과 사이사이 빈자리에 끼워 넣습니다.", cap: "② 이웃 금지 조건 $\\Longrightarrow$ 나머지 먼저 배열 후 빈틈에 삽입!" },
      { say: "셋째, 원소 여섯 개를 두 개, 두 개, 두 개로 똑같은 개수의 조로 나눌 때는 같은 개수인 삼 팩토리얼로 나누어야 합니다.", cap: "③ 분할·분배 주의: 크기가 같은 조가 $k$개이면 $\\dfrac{1}{k!}$ 곱하기!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 2022 개정 공통수학 원에 새롭게 돌아온 행렬의 연산과 거듭제곱 제오십일강입니다.", cap: "제51강 · [2022 신설] 행렬의 연산과 거듭제곱($A^{n}$)" },
      { tag: "연계 ②", say: "약수의 개수와 총곱을 다루는 제십오강과도 함께 복습해 보세요.", cap: "제15강 · 약수의 총곱 & 기하평균 공식" },
      { tag: "이 사이트", say: "이 사이트의 제오십일강과 제십오강을 이어서 보세요.", cap: "제51강 · 행렬의 연산과 거듭제곱  /  제15강 · 약수의 총곱" }
    ],
    nextLinks: [
      { lec: 51, label: "제51강 열기 (2022 신설 행렬)" },
      { lec: 15, label: "제15강 열기 (약수의 총곱)" },
      { lec: 49, label: "제49강 열기 (근의 분리 함·판·축)" }
    ]
  },
  {
    lec: 51,
    title: "숏츠식 판서 미리보기 · [2022 개정 신설] 행렬의 연산과 거듭제곱",
    desc: "행렬의 곱셈 원리(가로$\\times$세로 내적), 교환법칙 불성립($AB\\neq BA$), 케일리-해밀턴 차수 낮추기 공식을 정리합니다.",
    hookTitle: "[2022 신설] 행렬 곱셈과 거듭제곱", hookSub: "가로×세로 곱셈 · AB ≠ BA · 케일리-해밀턴 차수 축소",
    hookSay: "2022 개정 공통수학 원에 부활한 행렬 단원의 곱셈 법칙과 거듭제곱 암산법, 30초 만에 정리합니다.",
    hookCap: "행렬 곱셈·거듭제곱 · 30초 정리",
    whySay: "행렬의 곱셈은 앞 행렬의 가로 행과 뒤 행렬의 세로 열을 짝지어 곱해 더하므로 순서가 바뀌면 결과가 달라지며, 이차 항등식을 쓰면 고차 거듭제곱이 일차식으로 줄어듭니다.",
    whyCap: "$AB\\neq BA$ 주의! · $A^{2}-(a+d)A+(ad-bc)E=O$ 차수 축소",
    histTag: "케일리·실베스터", histSay: "행렬이라는 용어는 실베스터가 처음 사용했고, 아서 케일리가 행렬 대수와 케일리-해밀턴 정리를 확립했습니다.",
    histCap: "케일리(Arthur Cayley)의 행렬 대수와 케일리-해밀턴 항등식(1858)",
    fParts: [
      { say: "행렬 에이와 비의 곱에서 아이행 제이열 성분은 에이의 아이행과 비의 제이열 성분을 순서대로 곱해 더한 값입니다.", cap: "$(AB)_{ij}=(\\text{앞의 }i\\text{행})\\cdot(\\text{뒤의 }j\\text{열})$" },
      { say: "행렬은 교환법칙 에이 비와 비 에이가 일반적으로 같지 않으므로 에이 더하기 비의 제곱은 에이 제곱 더하기 에이 비 더하기 비 에이 더하기 비 제곱입니다.", cap: "$AB\\neq BA\\ \\Longrightarrow\\ (A+B)^{2}=A^{2}+AB+BA+B^{2}$" },
      { say: "이차 정사각행렬 에이는 에이 제곱 빼기 대각선 합 에이 더하기 행렬식 이는 영행렬을 만족하여 거듭제곱 차수를 바로 낮춥니다.", cap: "$A^{2}-(a+d)A+(ad-bc)E=O$ (케일리-해밀턴 차수 낮추기)" }
    ],
    fChips: [
      "AB\\neq BA\\ \\Longrightarrow\\ (A+B)(A-B)=A^{2}-AB+BA-B^{2}",
      "\\text{단위행렬 }E=\\begin{pmatrix}1&0\\\\0&1\\end{pmatrix}\\ :\\ AE=EA=A,\\quad E^{n}=E",
      "A=\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix}\\ \\Longrightarrow\\ A^{2}-(a+d)A+(ad-bc)E=O"
    ],
    fLabels: ["교환법칙 불성립 주의", "케일리-해밀턴 차수 축소"],
    exParts: [
      { say: "예를 들어 일행이 일, 이이고 이행이 영, 일인 삼각행렬 에이를 엔 번 거듭제곱한 행렬을 구해 봅시다.", cap: "$A=\\begin{pmatrix}1&2\\\\0&1\\end{pmatrix}$ 일 때 $A^{n}$ 구하기" },
      { say: "에이 제곱을 계산하면 오른쪽 위 성분만 이 더하기 이로 사가 되고, 세제곱은 육이 됩니다.", cap: "$A^{2}=\\begin{pmatrix}1&4\\\\0&1\\end{pmatrix},\\quad A^{3}=\\begin{pmatrix}1&6\\\\0&1\\end{pmatrix}$" },
      { say: "따라서 에이의 엔 제곱에서 오른쪽 위 성분은 이 엔이 됩니다.", cap: "$A^{n}=\\begin{pmatrix}1&2n\\\\0&1\\end{pmatrix}$" }
    ],
    exChips: [
      "\\begin{pmatrix}1&k\\\\0&1\\end{pmatrix}^{2}=\\begin{pmatrix}1&2k\\\\0&1\\end{pmatrix}",
      "\\begin{pmatrix}1&k\\\\0&1\\end{pmatrix}^{n}=\\begin{pmatrix}1&nk\\\\0&1\\end{pmatrix}",
      "A=\\begin{pmatrix}1&2\\\\0&1\\end{pmatrix}\\ \\Longrightarrow\\ A^{10}=\\begin{pmatrix}1&20\\\\0&1\\end{pmatrix}"
    ],
    exLabels: ["삼각행렬 거듭제곱 규칙", "우상단 성분 = nk"],
    exGraph: {
      f: x => 0.7 * x + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "가로행 × 세로열" }, r2: { x: 2.3, col: PK, label: "A² = (a+d)A − ΔE" },
      fn: { t: "행렬 거듭제곱: 규칙성 발견(A², A³) 또는 차수 낮추기!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "우상단 = 2n", finalS: "A¹⁰ 우상단 = 20", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 이차 정사각행렬 에이의 일행이 일, 마이너스 일이고 이행이 이, 마이너스 일일 때, 에이 네제곱의 모든 성분의 합은 얼마일까요?", cap: "$A=\\begin{pmatrix}1&-1\\\\2&-1\\end{pmatrix}$ 일 때 $A^{4}$ 의 모든 성분의 합 (자작 문항)" },
      { say: "주대각선 성분의 합 에이 더하기 디가 영이고 에이 디 빼기 비 씨가 일이어서 에이 제곱 더하기 이는 영행렬, 즉 에이 제곱은 마이너스 이입니다.", cap: "$a+d=0,\\ ad-bc=-1-(-2)=1\\ \\Rightarrow\\ A^{2}=-E$" },
      { say: "따라서 에이 네제곱은 단위행렬 이가 되므로 모든 성분의 합은 일 더하기 일, 이입니다.", cap: "$A^{4}=(-E)^{2}=E=\\begin{pmatrix}1&0\\\\0&1\\end{pmatrix}\\ \\Rightarrow\\ \\text{성분 합 }=2$" }
    ],
    examChips: [
      "a+d=1+(-1)=0,\\qquad ad-bc=-1-(-2)=1",
      "A^{2}-0\\cdot A+1\\cdot E=O\\ \\Longrightarrow\\ A^{2}=-E",
      "A^{4}=(-E)^{2}=E\\ \\Longrightarrow\\ \\text{모든 성분의 합 }=1+0+0+1=2"
    ],
    examLabels: ["A² = −E 도출", "정답 A⁴ = E → 합 2"],
    examGraph: {
      f: x => Math.cos(x * 2.1) * 1.1 + 1.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.8, col: CY, label: "A² = −E" }, r2: { x: 2.2, col: GO, label: "A⁴ = E (4주기)" },
      fn: { t: "a + d = 0, ad − bc = 1  ⇒  A² = −E,  A⁴ = E!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "A⁴ = E", finalS: "성분 합 = 2", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 에이 더하기 비의 제곱이 에이 제곱 더하기 이 에이 비 더하기 비 제곱과 같으려면 반드시 에이 비는 비 에이라는 교환법칙이 성립해야 합니다.", cap: "① $(A+B)^{2}=A^{2}+2AB+B^{2}\\ \\Longleftrightarrow\\ AB=BA$ (교환 성립 조건!)" },
      { say: "둘째, 행렬 에이에 단위행렬 이를 더한 행렬과는 언제나 교환법칙이 성립하므로 곱셈공식을 다항식처럼 그대로 쓸 수 있습니다.", cap: "② $A$ 와 $E$ 의 다항식끼리는 무조건 교환법칙 성립 ($A^{3}+E=(A+E)(A^{2}-A+E)$)" },
      { say: "셋째, 행렬의 모든 성분의 합을 구할 때는 각 행의 합이 일정한지 먼저 확인하면 계산이 절반으로 줄어듭니다.", cap: "③ 대각행렬 $\\begin{pmatrix}p&0\\\\0&q\\end{pmatrix}^{n}=\\begin{pmatrix}p^{n}&0\\\\0&q^{n}\\end{pmatrix}$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "이로써 공통수학 원 열두 개 강의 사슬이 모두 완성되었습니다. 이어서 공통수학 투의 유리함수 제십강으로 넘어가 보세요.", cap: "제10강 · 유리함수 평행이동 3초 공식 (공통수학 2 연계)" },
      { tag: "연계 ②", say: "공통수학 원의 출발점인 제사십강 대칭식 변형으로 돌아가 전체 흐름을 복습할 수도 있습니다.", cap: "제40강 · 곱셈공식 변형과 대칭식 구조 (공통수학 1 처음으로)" },
      { tag: "이 사이트", say: "이 사이트의 제십강과 제사십강을 이어서 보세요.", cap: "제10강 · 공통수학 2 유리함수  /  제40강 · 공통수학 1 대칭식" }
    ],
    nextLinks: [
      { lec: 10, label: "제10강 열기 (공통수학 2 유리함수)" },
      { lec: 40, label: "제40강 열기 (공통수학 1 처음으로)" },
      { lec: 2, label: "제2강 열기 (미적분 I 넓이 공식)" }
    ]
  }
];

const ALL_SPECS = [...COMMON1_SPECS_A, ...COMMON1_SPECS_B];
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
  const cInfo = COMMON1_CHAIN.find(c => c.lec === cfg.lec) || { step: 1, badge: "공통수학 1", title: cfg.title };
  mainEl.innerHTML = `
    <div class="glass-card" style="margin-bottom:22px;border-left:5px solid #f43f5e">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px">
        <span class="badge-pill" style="background:rgba(244,63,94,.18);color:#fda4af;border-color:rgba(244,63,94,.4)">
          📕 2022 개정 공통수학 1 · 사슬 ${cInfo.step}/12단계 (${cInfo.badge})
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
    mount.innerHTML = `${common1ChainNavHtml(cfg.lec)}
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
      const ok = await speak("안녕하세요. 공통수학 원 핵심 공식을 함께 정리해 볼까요?");
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

const COMMON1_PLAYERS = {};
function initCommon1() {
  CONFIGS.forEach(cfg => {
    if (!COMMON1_PLAYERS[cfg.lec]) COMMON1_PLAYERS[cfg.lec] = createPlayer(cfg);
    COMMON1_PLAYERS[cfg.lec].init();
  });
}

window.Common1Shorts = { PLAYERS: COMMON1_PLAYERS, CONFIGS, initCommon1 };
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initCommon1);
else initCommon1();
window.addEventListener("load", initCommon1);
})();
