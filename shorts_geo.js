/* 제5,34,35,6,12,23,26강 · 기하 & 미적분 숏츠식 판서 미리보기 사슬 (7개 강의 통합 모듈) */
(function () {
"use strict";

const $ = id => document.getElementById(id);
const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
const ease = t => 1 - Math.pow(1 - clamp(t, 0, 1), 3);
const F = "GowunDodumL2, 'Gowun Dodum', 'Malgun Gothic', sans-serif";
const CY = "#22d3ee", PK = "#f472b6", GO = "#facc15", GR = "#4ade80", VI = "#a855f7", INK = "#f8fafc", MUT = "#94a3b8";

const GEO_CHAIN = [
  { lec: 5,  step: 1, badge: "피타고라스", title: "유클리드 등적변형 증명" },
  { lec: 34, step: 2, badge: "중학도형",   title: "내각 이등분선·무게중심" },
  { lec: 35, step: 3, badge: "원의성질",   title: "원주각·중심각·접현각" },
  { lec: 6,  step: 4, badge: "수능기하7",  title: "사영·접현각·할선(방멱)" },
  { lec: 12, step: 5, badge: "직각쌍곡선", title: "쌍곡선 넓이 S = T 불변" },
  { lec: 23, step: 6, badge: "포물선7대",  title: "초점현 조화평균·접선직교" },
  { lec: 26, step: 7, badge: "테일러급수", title: "초월함수의 다항식 근사" }
];

function goLecture(lec) {
  if (typeof window.switchLecture === "function") {
    window.switchLecture(lec);
    setTimeout(() => { window.scrollTo({ top: 0, behavior: "smooth" }); }, 60);
  }
}

function geoChainNavHtml(curLec) {
  const idx = GEO_CHAIN.findIndex(c => c.lec === curLec);
  const prev = idx > 0 ? GEO_CHAIN[idx - 1] : null;
  const next = idx >= 0 && idx < GEO_CHAIN.length - 1 ? GEO_CHAIN[idx + 1] : null;
  return `
    <div class="l2s-chain-box" style="margin-bottom:16px;padding:12px 14px;border-radius:12px;background:rgba(15,23,42,.82);border:1px solid rgba(168,85,247,.32)">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:10px">
        <span style="font-size:13px;font-weight:800;color:#e9d5ff">📐 기하 & 미적분 · 수업 단원·개념 연결 사슬 (${idx + 1} / ${GEO_CHAIN.length}단계)</span>
        <div style="display:flex;gap:6px">
          ${prev ? `<button type="button" class="l2s-btn" data-chain-lec="${prev.lec}" style="padding:4px 10px;font-size:12px">← 이전: 제${prev.lec}강 (${prev.badge})</button>` : ""}
          ${next ? `<button type="button" class="l2s-btn pri" data-chain-lec="${next.lec}" style="padding:4px 10px;font-size:12px">다음: 제${next.lec}강 (${next.badge}) →</button>` : ""}
        </div>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:5px">
        ${GEO_CHAIN.map(c => {
          const on = c.lec === curLec;
          return `<button type="button" data-chain-lec="${c.lec}" style="padding:4px 9px;border-radius:999px;font-size:11.5px;font-weight:${on ? 800 : 600};cursor:pointer;border:1px solid ${on ? "#facc15" : "rgba(148,163,184,.25)"};background:${on ? "rgba(250,204,21,.18)" : "rgba(15,23,42,.6)"};color:${on ? "#fde047" : "#cbd5e1"}">${c.step}. 제${c.lec}강 ${c.badge}</button>`;
        }).join("")}
      </div>
    </div>`;
}

function tex(s, disp) {
  if (!window.katex) return s;
  try { return katex.renderToString(s, { displayMode: !!disp, throwOnError: false }); }
  catch (e) { return s; }
}

const GEO_SPECS = [
  {
    lec: 5, subj: "geo",
    title: "숏츠식 판서 미리보기 · 피타고라스 정리 유클리드 증명",
    desc: "직각삼각형의 세 변 위 정사각형에서 평행선 등적변형과 $SAS$ 합동으로 $a^{2}+b^{2}=c^{2}$ 을 유도합니다.",
    hookTitle: "피타고라스 · 유클리드 증명", hookSub: "등적변형 → SAS 합동 → 등적변형 30초 정리",
    hookSay: "피타고라스 정리의 유클리드 증명을 세 단계 등적변형과 합동으로 30초 만에 정리합니다.",
    hookCap: "유클리드 증명 3단계 · 30초 정리",
    whySay: "정사각형의 절반인 삼각형을 평행선을 따라 미끄러뜨리고 90도 회전 합동을 쓰면, 위쪽 두 정사각형 넓이가 아래 직사각형들로 그대로 옮겨집니다.",
    whyCap: "등적변형(밑변·높이 일정) $\\to$ $SAS$ 회전 합동 $\\to$ 등적변형",
    histTag: "원론 1권 47", histSay: "유클리드 원론 제1권의 마지막 법칙인 법칙 47번에 수록되어 ‘풍차 증명’이라는 별명으로 불립니다.",
    histCap: "유클리드 《원론》 제1권 법칙 47 (풍차 도형 증명)",
    fParts: [
      { say: "한 변이 비인 정사각형의 절반 삼각형에서 꼭짓점을 평행선을 따라 이동시키면 넓이가 그대로 유지됩니다.", cap: "1단계(등적변형): $\\dfrac{1}{2}b^{2}=\\triangle CAD=\\triangle CAB$" },
      { say: "두 정사각형의 한 변씩과 끼인각 구십도 더하기 각 에이가 같으므로 구십도 회전한 두 삼각형은 에스에이에스 합동입니다.", cap: "2단계($SAS$ 합동): $\\triangle CAB\\equiv\\triangle KAH$" },
      { say: "다시 평행선 등적변형을 적용하면 왼쪽 직사각형 넓이가 비 제곱, 오른쪽이 에이 제곱이 되어 합은 씨 제곱입니다.", cap: "3단계: 왼쪽 직사각형 $=b^{2}$, 오른쪽 $=a^{2}\\ \\Rightarrow\\ a^{2}+b^{2}=c^{2}$" }
    ],
    fChips: [
      "\\text{1단계(등적): }\\dfrac{1}{2}b^{2}=\\triangle CAD=\\triangle CAB",
      "\\text{2단계(합동): }\\triangle CAB\\equiv\\triangle KAH\\ (SAS)\\ \\Rightarrow\\ \\text{직사각형 }=b^{2}",
      "\\text{좌측 }b^{2}+\\text{우측 }a^{2}=c^{2}"
    ],
    fLabels: ["등적변형 → SAS 합동", "다시 등적변형 → 합산"],
    exParts: [
      { say: "예를 들어 두 직각변의 길이가 삼과 사이고 빗변이 오인 직각삼각형에서 유클리드 도형의 넓이를 구해 봅시다.", cap: "$b=3,\\ a=4,\\ c=5$ 인 유클리드 풍차 도형" },
      { say: "작은 정사각형 넓이 구는 수선의 발로 나뉜 왼쪽 직사각형 넓이와 같고, 색칠한 삼각형 넓이는 그 절반인 이분의 구입니다.", cap: "왼쪽 직사각형 $=3^{2}=9,\\quad \\triangle CAB=\\dfrac{9}{2}$" },
      { say: "오른쪽 직사각형 넓이는 십육이므로 두 직사각형의 합은 구 더하기 십육, 이십오가 됩니다.", cap: "전체 정사각형 $=9+16=25=5^{2}$" }
    ],
    exChips: [
      "b=3,\\ a=4,\\ c=5\\ \\Rightarrow\\ b^{2}=9,\\ a^{2}=16",
      "\\triangle CAB=\\triangle KAH=\\dfrac{1}{2}b^{2}=\\dfrac{9}{2}",
      "\\text{좌측 직사각형 }9+\\text{우측 직사각형 }16=25=c^{2}"
    ],
    exLabels: ["절반 삼각형 9/2", "직사각형 합 25"],
    exGraph: {
      f: x => 0.35 * x * x + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.9, col: CY, label: "좌측 b² = 9" }, r2: { x: 2.3, col: PK, label: "우측 a² = 16" },
      fn: { t: "유클리드 등적변형: b² + a² = c² (9 + 16 = 25)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "SAS 회전 합동", finalS: "9 + 16 = 25", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 유클리드 증명 도형에서 직각변 에이 비가 육이고 에이 씨가 팔일 때, 꼭짓점 씨에서 빗변 정사각형으로 내린 수선이 나누는 왼쪽 직사각형의 넓이는 얼마일까요?", cap: "$\\overline{AB}=6,\\ \\overline{AC}=8$ 일 때 왼쪽 직사각형 넓이 구하기 (자작 문항)" },
      { say: "유클리드 등적변형과 에스에이에스 합동에 의해 왼쪽 직사각형의 넓이는 왼쪽 정사각형의 넓이와 정확히 같습니다.", cap: "왼쪽 직사각형 넓이 $=\\overline{AB}^{2}$" },
      { say: "따라서 육의 제곱인 삼십육입니다.", cap: "$6^{2}=36$" }
    ],
    examChips: [
      "\\overline{AB}=6,\\quad \\overline{AC}=8,\\quad \\overline{BC}=10",
      "\\text{왼쪽 직사각형 넓이 }=\\overline{AB}^{2}",
      "6^{2}=36"
    ],
    examLabels: ["유클리드 넓이 보존", "정답 36"],
    examGraph: {
      f: x => 0.35 * x * x + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.9, col: CY, label: "좌측 6² = 36" }, r2: { x: 2.3, col: GO, label: "우측 8² = 64" },
      fn: { t: "왼쪽 직사각형 = AB² = 36, 오른쪽 = AC² = 64", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "AB² = 6²", finalS: "넓이 = 36", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 유클리드 도형 안에 등장하는 네 개의 핵심 삼각형 넓이는 모두 작은 정사각형 넓이의 절반으로 같습니다.", cap: "① 핵심 삼각형 4개의 넓이 $=\\dfrac{1}{2}b^{2}$ 으로 모두 동일!" },
      { say: "둘째, 빗변에 내린 수선은 빗변 정사각형을 비 제곱과 에이 제곱의 비율로 분할합니다.", cap: "② 수선에 의한 직사각형 분할 비 $=b^{2}:a^{2}$" },
      { say: "셋째, 합동인 두 삼각형의 대응변이 서로 구십도로 만나므로 두 선분은 항상 수직입니다.", cap: "③ $90^{\\circ}$ 회전 합동 $\\Longrightarrow$ 대응변끼리 수직 교차!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 내각의 이등분선 정리와 무게중심·외심·내심을 총정리하는 제삼십사강입니다.", cap: "제34강 · 중학도형 핵심 총정리 (이등분선·무게중심)" },
      { tag: "연계 ②", say: "원주각과 접현각의 핵심 성질을 다루는 제삼십오강도 이어서 보세요.", cap: "제35강 · 원의 성질 핵심 정리 (원주각·접현각)" },
      { tag: "이 사이트", say: "이 사이트의 제삼십사강과 제삼십오강을 이어서 보세요.", cap: "제34강 · 중학도형 총정리  /  제35강 · 원의 성질" }
    ],
    nextLinks: [
      { lec: 34, label: "제34강 열기 (중학도형 총정리)" },
      { lec: 35, label: "제35강 열기 (원의 성질)" },
      { lec: 6, label: "제6강 열기 (수능 기하 7대 정리)" }
    ]
  },
  {
    lec: 34, subj: "geo",
    title: "숏츠식 판서 미리보기 · 중학도형 핵심 총정리 (이등분선·무게중심)",
    desc: "내각의 이등분선 정리 $AB:AC=BD:CD$, 무게중심의 $2:1$ 내분과 6등분 넓이, 외심·내심 공식을 정리합니다.",
    hookTitle: "중학도형 필수 공식 총정리", hookSub: "각의 이등분선 · 무게중심 · 내접원 반지름",
    hookSay: "수능 도형 문제를 풀 때 가장 많이 쓰이는 중학도형 필수 공식 세 가지, 30초 만에 정리합니다.",
    hookCap: "중학도형 3대 공식 · 30초 정리",
    whySay: "수능 삼각함수 도형과 미적분 급수 문제에서 변의 길이 비와 넓이 비를 쪼개는 열쇠는 모두 중학 기하의 기본 정리에서 나옵니다.",
    whyCap: "내각 이등분선(하트 공식) + 무게중심($2:1$) + 내심 넓이($\\frac{1}{2}r\\cdot\\text{둘레}$)",
    histTag: "유클리드 기하", histSay: "내각의 이등분선 정리는 유클리드 원론 제6권 법칙 3번에, 무게중심의 평형 원리는 아르키메데스의 연구에 등장합니다.",
    histCap: "유클리드 《원론》 6권(이등분선 비례)과 아르키메데스 무게중심",
    fParts: [
      { say: "삼각형 내각의 이등분선이 밑변과 만나는 점 디에 대하여 왼쪽 변 대 오른쪽 변은 왼쪽 밑변 대 오른쪽 밑변입니다.", cap: "내각 이등분선: $\\overline{AB}:\\overline{AC}=\\overline{BD}:\\overline{CD}$" },
      { say: "세 중선의 교점인 무게중심 쥐는 각 중선을 꼭짓점으로부터 이 대 일로 내분하며 삼각형 넓이를 육등분합니다.", cap: "무게중심 $G$: 중선을 $2:1$ 내분, 작은 삼각형 넓이 $=\\dfrac{1}{6}S$" },
      { say: "내접원의 반지름 알을 알 때 삼각형의 넓이는 이분의 일 곱하기 알 곱하기 세 변의 길이의 합입니다.", cap: "내접원 반지름 $r$: 넓이 $S=\\dfrac{1}{2}r(a+b+c)$" }
    ],
    fChips: [
      "\\text{각의 이등분선: }\\overline{AB}:\\overline{AC}=\\overline{BD}:\\overline{CD}",
      "\\text{무게중심 }G\\text{: 중선 }2:1\\text{ 분할},\\quad S_{\\triangle GAB}=\\dfrac{1}{3}S",
      "\\text{내접원 넓이 공식: }S=\\dfrac{1}{2}r(a+b+c)"
    ],
    fLabels: ["양 옆변 비 = 밑변 비", "중선 2:1 & 내접원 반지름"],
    exParts: [
      { say: "예를 들어 에이 비가 육, 에이 씨가 구, 밑변 비 씨가 십인 삼각형에서 각 에이의 이등분선이 나누는 비 디의 길이를 구해 봅시다.", cap: "$\\overline{AB}=6,\\ \\overline{AC}=9,\\ \\overline{BC}=10$ 일 때 $\\overline{BD}$ 구하기" },
      { say: "양 옆변의 비가 육 대 구, 즉 이 대 삼이므로 밑변 십도 이 대 삼으로 내분됩니다.", cap: "$\\overline{BD}:\\overline{CD}=6:9=2:3$" },
      { say: "따라서 비 디의 길이는 십 곱하기 오분의 이, 사가 됩니다.", cap: "$\\overline{BD}=10\\times\\dfrac{2}{2+3}=4$" }
    ],
    exChips: [
      "\\overline{AB}:\\overline{AC}=6:9=2:3",
      "\\overline{BD}:\\overline{CD}=2:3\\quad (\\overline{BC}=10)",
      "\\overline{BD}=10\\times\\dfrac{2}{5}=4,\\quad \\overline{CD}=6"
    ],
    exLabels: ["옆변의 비 2 : 3", "밑변 내분 길이 4"],
    exGraph: {
      f: x => 2.2 - 0.55 * Math.abs(x - 1.2), GY0: 390, GV: 110, xr: [0, 3], area: [0.2, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "BD = 4 (비율 2)" }, r2: { x: 2.0, col: PK, label: "CD = 6 (비율 3)" },
      fn: { t: "내각 이등분선: AB : AC = BD : CD = 2 : 3", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "6 : 9 = 2 : 3", finalS: "BD = 4", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 세 변의 길이가 오, 십이, 십삼인 직각삼각형에 내접하는 원의 반지름 알은 얼마일까요?", cap: "세 변이 $5, 12, 13$ 인 직각삼각형의 내접원 반지름 $r$ (자작 문항)" },
      { say: "삼각형의 넓이는 이분의 일 곱하기 오 곱하기 십이로 삼십이고, 세 변의 둘레의 합은 삼십입니다.", cap: "$S=\\dfrac{1}{2}\\times 5\\times 12=30,\\quad a+b+c=30$" },
      { say: "이분의 일 곱하기 알 곱하기 삼십이 삼십이므로 반지름 알은 이입니다.", cap: "$\\dfrac{1}{2}r\\times 30=30\\ \\Rightarrow\\ r=2$" }
    ],
    examChips: [
      "S=\\dfrac{1}{2}\\times 5\\times 12=30",
      "S=\\dfrac{1}{2}r(5+12+13)=15r",
      "15r=30\\ \\Rightarrow\\ r=2"
    ],
    examLabels: ["넓이 = 1/2·r·둘레", "정답 r = 2"],
    examGraph: {
      f: x => 2.4 - 0.7 * x, GY0: 390, GV: 110, xr: [0, 3], area: [0.2, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.8, col: CY, label: "내접원 반지름 r" }, r2: { x: 2.2, col: GO, label: "둘레 5+12+13=30" },
      fn: { t: "직각삼각형 내접원: r = (a + b − c)/2 = (5 + 12 − 13)/2 = 2", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "15r = 30", finalS: "r = 2", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 직각삼각형의 내접원 반지름은 두 직각변의 합에서 빗변을 뺀 뒤 이로 나누면 1초 만에 나옵니다.", cap: "① 직각삼각형 내접원 반지름 $r=\\dfrac{a+b-c}{2}$" },
      { say: "둘째, 직각삼각형의 외심은 항상 빗변의 중점에 위치하므로 외접원 반지름은 빗변의 절반입니다.", cap: "② 직각삼각형 외심 $=$ 빗변의 중점 $\\left(R=\\dfrac{c}{2}\\right)$" },
      { say: "셋째, 가게 이등분선이 나오면 밑변의 길이 비뿐만 아니라 두 삼각형의 넓이 비도 양 옆변의 비와 같습니다.", cap: "③ 이등분선 분할 넓이 비 $S_{\\triangle ABD}:S_{\\triangle ACD}=\\overline{AB}:\\overline{AC}$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 원주각과 중심각, 내접사각형, 접현각을 총정리하는 제삼십오강입니다.", cap: "제35강 · 원의 성질 핵심 정리 (원주각과 접현각)" },
      { tag: "연계 ②", say: "수능 기하 7대 핵심정리를 집대성한 제육강도 이어서 보세요.", cap: "제6강 · 수능 기하 7대 핵심정리 총정리" },
      { tag: "이 사이트", say: "이 사이트의 제삼십오강과 제육강을 이어서 보세요.", cap: "제35강 · 원의 성질  /  제6강 · 수능 기하 7대 정리" }
    ],
    nextLinks: [
      { lec: 35, label: "제35강 열기 (원의 성질)" },
      { lec: 6, label: "제6강 열기 (수능 기하 7대 정리)" },
      { lec: 5, label: "제5강 열기 (피타고라스 정리)" }
    ]
  },
  {
    lec: 35, subj: "geo",
    title: "숏츠식 판서 미리보기 · 원의 성질 핵심 정리 (원주각과 접현각)",
    desc: "중심각과 원주각의 $2:1$ 관계, 반원의 원주각 $90^{\\circ}$, 내접사각형 대각의 합 $180^{\\circ}$, 접현각 정리를 정리합니다.",
    hookTitle: "원의 성질 · 원주각과 접현각", hookSub: "중심각의 절반 · 반원 90° · 내접사각형 180°",
    hookSay: "원만 나오면 자동으로 떠올려야 할 원주각과 접현각의 4대 공식, 30초 만에 정리합니다.",
    hookCap: "원의 성질 4대 정리 · 30초 정리",
    whySay: "원 위의 점은 중심으로부터 거리가 같아 이등변삼각형이 만들어지므로, 원주각은 위치에 상관없이 항상 중심각의 절반으로 일정합니다.",
    whyCap: "반지름 이등변삼각형 외각 성질 $\\Rightarrow$ 원주각 $=\\dfrac{1}{2}\\times$중심각",
    histTag: "탈레스·유클리드", histSay: "반원에 내접하는 원주각이 직각이라는 탈레스의 정리와 유클리드 원론 제3권의 원주각 정리가 그 기원입니다.",
    histCap: "탈레스의 반원 직각 정리와 유클리드 《원론》 제3권",
    fParts: [
      { say: "한 호에 대한 원주각의 크기는 모두 같으며 중심각 크기의 절반이고, 지름에 대한 원주각은 항상 구십도입니다.", cap: "원주각 $=\\dfrac{1}{2}\\times$중심각, 지름(반원)의 원주각 $=90^{\\circ}$" },
      { say: "원에 내접하는 사각형에서 마주 보는 대각의 합은 백팔십도이므로 한 외각은 내대각의 크기와 같습니다.", cap: "내접사각형 대각의 합 $\\angle A+\\angle C=180^{\\circ}$" },
      { say: "원의 접선과 현이 이루는 접현각의 크기는 그 호에 대한 원주각의 크기와 같습니다.", cap: "접현각 정리: $\\angle BAT=\\angle BCA$ (접선과 현의 각 $=$ 원주각)" }
    ],
    fChips: [
      "\\text{원주각 }=\\dfrac{1}{2}\\times\\text{중심각},\\quad \\text{지름의 원주각 }=90^{\\circ}",
      "\\text{내접사각형 대각의 합 }\\angle A+\\angle C=180^{\\circ}",
      "\\text{접현각 정리: }\\angle(\\text{접선, 현})=\\angle(\\text{호의 원주각})"
    ],
    fLabels: ["원주각 = 1/2 중심각", "내접사각형 & 접현각"],
    exParts: [
      { say: "예를 들어 호 에이 비에 대한 중심각이 백십도일 때 원주각과 마주 보는 내접사각형 각의 크기를 구해 봅시다.", cap: "중심각 $\\angle AOB=110^{\\circ}$ 일 때 원주각과 대각 구하기" },
      { say: "원주각 피는 중심각 백십도의 절반이므로 오십오도입니다.", cap: "원주각 $\\angle APB=\\dfrac{110^{\\circ}}{2}=55^{\\circ}$" },
      { say: "내접사각형에서 마주 보는 각 큐는 백팔십도에서 오십오도를 뺀 백이십오도입니다.", cap: "대각 $\\angle AQB=180^{\\circ}-55^{\\circ}=125^{\\circ}$" }
    ],
    exChips: [
      "\\angle AOB=110^{\\circ}\\ \\Rightarrow\\ \\angle APB=\\dfrac{110^{\\circ}}{2}=55^{\\circ}",
      "\\angle APB+\\angle AQB=180^{\\circ}",
      "\\angle AQB=180^{\\circ}-55^{\\circ}=125^{\\circ}"
    ],
    exLabels: ["원주각 55°", "내접사각형 대각 125°"],
    exGraph: {
      f: x => Math.sqrt(Math.max(0, 2.25 - (x - 1.5) * (x - 1.5))) + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "원주각 55°" }, r2: { x: 2.3, col: PK, label: "중심각 110°" },
      fn: { t: "같은 호의 원주각은 일정 (= 중심각의 1/2)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "110° ÷ 2 = 55°", finalS: "대각 = 125°", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 원 위의 점 에이에서의 접선과 현 에이 비가 이루는 각이 삼십팔도이고 에이 씨가 원의 지름일 때, 각 비 에이 씨의 크기는 몇 도일까요?", cap: "접현각 $\\angle BAT=38^{\\circ}$ 이고 $\\overline{AC}$ 가 지름일 때 $\\angle BAC$ (자작 문항)" },
      { say: "접현각 정리에 의해 호 에이 비의 원주각인 각 에이 씨 비는 삼십팔도이고, 지름의 원주각인 각 에이 비 씨는 구십도입니다.", cap: "$\\angle ACB=38^{\\circ},\\quad \\angle ABC=90^{\\circ}$" },
      { say: "따라서 직각삼각형에서 구십도 빼기 삼십팔도는 오십이도입니다.", cap: "$\\angle BAC=90^{\\circ}-38^{\\circ}=52^{\\circ}$" }
    ],
    examChips: [
      "\\text{접현각 }\\angle BAT=38^{\\circ}\\ \\Rightarrow\\ \\angle ACB=38^{\\circ}",
      "\\overline{AC}\\text{ 가 지름}\\ \\Rightarrow\\ \\angle ABC=90^{\\circ}",
      "\\angle BAC=90^{\\circ}-38^{\\circ}=52^{\\circ}"
    ],
    examLabels: ["접현각 + 지름 90°", "정답 52°"],
    examGraph: {
      f: x => Math.sqrt(Math.max(0, 2.25 - (x - 1.5) * (x - 1.5))) + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "접현각 38°" }, r2: { x: 2.4, col: GO, label: "지름 원주각 90°" },
      fn: { t: "접현각 ∠ACB = 38°, 반원 ∠ABC = 90°  ⇒  ∠BAC = 52°", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "90° − 38°", finalS: "∠BAC = 52°", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 문제에 원의 지름이 주어지면 원 위의 점과 이어 구십도 직각 표시부터 합니다.", cap: "① 지름 발견 즉시 $\\Longrightarrow$ 원주각 $90^{\\circ}$ 직각 표시!" },
      { say: "둘째, 마주 보는 두 각의 합이 백팔십도인 사각형이 보이면 네 꼭짓점을 지나는 외접원을 그릴 수 있습니다.", cap: "② 대각의 합 $=180^{\\circ}\\ \\Longleftrightarrow$ 네 점이 한 원 위에 존재(공원점)" },
      { say: "셋째, 원의 접선이 나오면 중심과 접점을 잇는 수선과 접현각 두 가지를 동시에 체크합니다.", cap: "③ 원의 접선 $\\Longrightarrow$ (반지름$\\perp$접선) + (접현각$=$원주각)" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 직각삼각형 사영 정리와 방멱 정리까지 수능 기하 7대 핵심정리를 총정리하는 제육강입니다.", cap: "제6강 · 수능 기하 7대 핵심정리 총정리" },
      { tag: "연계 ②", say: "직각쌍곡선의 넓이 불변 정리를 다루는 제십이강도 이어서 보세요.", cap: "제12강 · 직각쌍곡선 넓이 불변 정리 (S = T)" },
      { tag: "이 사이트", say: "이 사이트의 제육강과 제십이강을 이어서 보세요.", cap: "제6강 · 수능 기하 7대 정리  /  제12강 · 직각쌍곡선 넓이" }
    ],
    nextLinks: [
      { lec: 6, label: "제6강 열기 (수능 기하 7대 정리)" },
      { lec: 12, label: "제12강 열기 (직각쌍곡선 넓이)" },
      { lec: 34, label: "제34강 열기 (중학도형 총정리)" }
    ]
  },
  {
    lec: 6, subj: "geo",
    title: "숏츠식 판서 미리보기 · 수능 기하 7대 핵심정리 총정리",
    desc: "직각삼각형 사영 정리($a^{2}=pc,\\ h^{2}=pq$)와 원의 방멱(할선·접선) 정리($PA\\cdot PB=PT^{2}$)를 정리합니다.",
    hookTitle: "수능 기하 7대 핵심정리", hookSub: "소 공식 · 직각삼각형 사영 · 할선(방멱) 정리",
    hookSay: "수능 도형 문제에서 식을 가장 빠르게 세워 주는 사영 정리와 방멱 정리, 30초 만에 정리합니다.",
    hookCap: "수능 기하 사영·방멱 정리 · 30초 정리",
    whySay: "직각삼각형 안에 수선을 내리면 세 직각삼각형이 모두 닮음이 되고, 원에서 두 할선을 그으면 원주각에 의해 닮음 삼각형이 생겨 길이의 곱이 일정해집니다.",
    whyCap: "AA 닮음 비례식 $\\Rightarrow$ 직각삼각형 제곱 공식 & 원의 방멱 공식",
    histTag: "유클리드·슈타이너", histSay: "비례중항 정리는 유클리드 원론 6권에 등장하며, 원에 대한 점의 방멱 개념은 19세기 기하학자 슈타이너가 명명했습니다.",
    histCap: "유클리드 비례중항($h^{2}=pq$)과 슈타이너의 원의 방멱(Power of a Point)",
    fParts: [
      { say: "직각삼각형의 직각 꼭짓점에서 빗변에 수선을 내리면 왼쪽 변의 제곱은 가까운 조각 곱하기 전체 빗변입니다.", cap: "직각삼각형 사영: $a^{2}=p\\cdot c,\\quad b^{2}=q\\cdot c$" },
      { say: "높이 에이치의 제곱은 왼쪽 조각 곱하기 오른쪽 조각이고, 두 직각변의 곱은 밑변 곱하기 높이와 같습니다.", cap: "높이 제곱 $h^{2}=p\\cdot q$, 소(牛) 넓이 공식 $a\\cdot b=c\\cdot h$" },
      { say: "원 밖의 점 피에서 그은 접선 피 티의 제곱은 할선의 가까운 거리 피 에이 곱하기 먼 거리 피 비와 같습니다.", cap: "방멱(접선·할선) 정리: $\\overline{PT}^{2}=\\overline{PA}\\cdot\\overline{PB}$" }
    ],
    fChips: [
      "a^{2}=p\\cdot c,\\qquad b^{2}=q\\cdot c,\\qquad h^{2}=p\\cdot q",
      "a\\cdot b=c\\cdot h\\quad (\\text{직각삼각형 넓이 불변: 소 공식})",
      "\\overline{PT}^{2}=\\overline{PA}\\cdot\\overline{PB}\\quad (\\text{원의 접선·할선 방멱 정리})"
    ],
    fLabels: ["직각삼각형 제곱 공식", "원의 방멱 정리"],
    exParts: [
      { say: "예를 들어 직각삼각형의 빗변에 내린 수선의 발이 빗변을 사와 구로 나눌 때 높이 에이치를 구해 봅시다.", cap: "빗변 분할 $p=4,\\ q=9$ 일 때 높이 $h$ 구하기" },
      { say: "높이 에이치의 제곱은 왼쪽 조각 사 곱하기 오른쪽 조각 구로 삼십육입니다.", cap: "$h^{2}=p\\cdot q=4\\times 9=36$" },
      { say: "따라서 높이 에이치는 육이고, 왼쪽 직각변의 제곱은 사 곱하기 십삼으로 오십이입니다.", cap: "$h=6,\\quad a^{2}=4\\times(4+9)=52$" }
    ],
    exChips: [
      "p=4,\\quad q=9,\\quad c=4+9=13",
      "h^{2}=p\\cdot q=4\\times 9=36\\ \\Rightarrow\\ h=6",
      "a=\\sqrt{4\\times 13}=2\\sqrt{13},\\quad b=\\sqrt{9\\times 13}=3\\sqrt{13}"
    ],
    exLabels: ["h² = pq = 36", "높이 h = 6"],
    exGraph: {
      f: x => 2.1 - 0.55 * Math.abs(x - 1.0), GY0: 390, GV: 110, xr: [0, 3], area: [0.2, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "p = 4" }, r2: { x: 2.1, col: PK, label: "q = 9 (h = 6)" },
      fn: { t: "직각삼각형 비례중항(기하평균): h² = p · q = 4 × 9 = 36", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "h² = 4 × 9", finalS: "h = 6", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 원 밖의 점 피에서 원에 그은 접선의 길이가 육이고, 원을 지나는 할선이 원과 만나는 가까운 거리가 사일 때, 원 내부 현 에이 비의 길이는 얼마일까요?", cap: "$\\overline{PT}=6,\\ \\overline{PA}=4$ 일 때 현 $\\overline{AB}$ 의 길이 구하기 (자작 문항)" },
      { say: "방멱 정리에 의해 육의 제곱 삼십육은 사 곱하기 피 비이므로 전체 길이 피 비는 구입니다.", cap: "$6^{2}=4\\times\\overline{PB}\\ \\Rightarrow\\ \\overline{PB}=9$" },
      { say: "따라서 현 에이 비의 길이는 구 빼기 사, 오입니다.", cap: "$\\overline{AB}=\\overline{PB}-\\overline{PA}=9-4=5$" }
    ],
    examChips: [
      "\\overline{PT}^{2}=\\overline{PA}\\cdot\\overline{PB}\\ \\Rightarrow\\ 6^{2}=4\\cdot\\overline{PB}",
      "\\overline{PB}=\\dfrac{36}{4}=9",
      "\\overline{AB}=\\overline{PB}-\\overline{PA}=9-4=5"
    ],
    examLabels: ["PT² = PA · PB", "정답 AB = 5"],
    examGraph: {
      f: x => Math.sqrt(Math.max(0, 2.25 - (x - 1.8) * (x - 1.8))) + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.5, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "접선 PT = 6" }, r2: { x: 2.2, col: GO, label: "PA=4, PB=9 → AB=5" },
      fn: { t: "방멱 정리: PT² = PA · PB  ⇒  36 = 4 × 9", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "PB = 9", finalS: "현 AB = 5", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 직각삼각형 안에 또 수선이 보이면 동그라미 각과 엑스 각을 표시해 닮음비와 제곱 공식을 즉시 적용합니다.", cap: "① 직각 속의 수선 $\\Longrightarrow$ $\\bigcirc+\\times=90^{\\circ}$ 표시 후 사영 공식!" },
      { say: "둘째, 원의 두 현이 원 내부에서 교차할 때도 양쪽 조각의 곱이 서로 같다는 내부 방멱이 성립합니다.", cap: "② 원 내부 교점 $P$: $\\overline{PA}\\cdot\\overline{PB}=\\overline{PC}\\cdot\\overline{PD}$" },
      { say: "셋째, 두 원이 외접하거나 내접할 때는 중심끼리 잇는 보조선과 공통접선의 직각삼각형을 만듭니다.", cap: "③ 두 원과 공통접선 $\\Longrightarrow$ 중심 연결선과 직각삼각형 작도!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 직각쌍곡선에서 부채꼴 넓이 에스와 적분 넓이 티가 같아지는 제십이강입니다.", cap: "제12강 · 직각쌍곡선 넓이 불변 정리 (S = T)" },
      { tag: "연계 ②", say: "이차곡선 포물선의 7대 기하 성질을 다루는 제이십삼강도 이어서 보세요.", cap: "제23강 · 포물선의 기하학적 성질 7가지" },
      { tag: "이 사이트", say: "이 사이트의 제십이강과 제이십삼강을 이어서 보세요.", cap: "제12강 · 직각쌍곡선 넓이  /  제23강 · 포물선 7대 성질" }
    ],
    nextLinks: [
      { lec: 12, label: "제12강 열기 (직각쌍곡선 넓이)" },
      { lec: 23, label: "제23강 열기 (포물선 7대 성질)" },
      { lec: 35, label: "제35강 열기 (원의 성질)" }
    ]
  },
  {
    lec: 12, subj: "geo",
    title: "숏츠식 판서 미리보기 · 직각쌍곡선 넓이 불변 정리 (S = T)",
    desc: "유리함수 $y=k/x$ 위의 두 점 $A, B$ 와 원점이 이루는 영역 $S$ 가 $x$축 아래 적분 영역 $T$ 와 같음을 증명합니다.",
    hookTitle: "직각쌍곡선 넓이 S = T 공식", hookSub: "직각삼각형 등적변형으로 10초 만에 증명",
    hookSay: "유리함수에서 원점과 곡선 호가 이루는 넓이 에스가 엑스축 아래 적분 넓이 티와 정확히 같은 이유, 30초 만에 정리합니다.",
    hookCap: "직각쌍곡선 $S=T$ 정리 · 30초 정리",
    whySay: "와이는 엑스분의 케이 위의 점에서 엑스축에 내린 직각삼각형 넓이는 항상 이분의 일 케이로 일정하므로, 공통부분을 빼고 더하면 두 넓이가 완전히 같아집니다.",
    whyCap: "$\\triangle OAA'=\\triangle OBB'=\\dfrac{1}{2}|k|$ 일정 $\\Rightarrow\\ S=T$",
    histTag: "쌍곡선 로그", histSay: "17세기 수학자 그레고리우스와 베르누이는 쌍곡선 아래 넓이 티가 자연로그 함수와 같음을 발견했습니다.",
    histCap: "그레고리우스의 쌍곡선 구적법: $T=k\\ln(b/a)$",
    fParts: [
      { say: "와이는 엑스분의 케이 위의 두 점에서 엑스축에 수선을 내리면 두 직각삼각형 넓이는 모두 이분의 일 케이입니다.", cap: "$\\triangle OAA'=\\triangle OBB'=\\dfrac{1}{2}k$ (넓이 일정)" },
      { say: "겹치는 작은 삼각형 넓이를 똑같이 빼면 왼쪽 조각과 아래쪽 조각 넓이가 같아져 에스는 티가 됩니다.", cap: "공통부분 제거 후 곡선 조각 결합 $\\Longrightarrow\\ S=T$" },
      { say: "두 점을 이은 삼각형 오 에이 비의 넓이는 사다리꼴 에이 에이 프라임 비 프라임 비의 넓이와 같습니다.", cap: "$\\triangle OAB=\\text{사다리꼴 }AA'B'B=\\dfrac{1}{2}\\left(\\dfrac{k}{a}+\\dfrac{k}{b}\\right)(b-a)$" }
    ],
    fChips: [
      "y=\\dfrac{k}{x}\\ (x\\gt 0)\\ \\Longrightarrow\\ S_{\\triangle OAA'}=S_{\\triangle OBB'}=\\dfrac{1}{2}k",
      "\\text{곡선 부채꼴 }S=\\text{곡선 아래 적분 넓이 }T=\\int_{a}^{b}\\dfrac{k}{x}\\,dx",
      "S_{\\triangle OAB}=\\text{사다리꼴 }AA'B'B=\\dfrac{k(b^{2}-a^{2})}{2ab}"
    ],
    fLabels: ["직각삼각형 넓이 1/2 k", "S = T & △OAB = 사다리꼴"],
    exParts: [
      { say: "예를 들어 와이는 엑스분의 사 위의 점 에이 일 콤마 사와 비 사 콤마 일에 대하여 삼각형 오 에이 비의 넓이를 구해 봅시다.", cap: "$y=\\dfrac{4}{x}$ 위의 $A(1,4),\\ B(4,1)$ 일 때 $\\triangle OAB$ 넓이" },
      { say: "삼각형 오 에이 비의 넓이는 엑스축으로 내린 사다리꼴의 넓이와 같습니다.", cap: "$S_{\\triangle OAB}=\\text{사다리꼴 }AA'B'B$" },
      { say: "윗변 일 더하기 아랫변 사에 높이 삼을 곱하고 이로 나누면 이분의 십오입니다.", cap: "$\\dfrac{1}{2}\\times(4+1)\\times(4-1)=\\dfrac{15}{2}$" }
    ],
    exChips: [
      "A(1,4),\\quad B(4,1)\\quad \\left(y=\\dfrac{4}{x}\\right)",
      "S_{\\triangle OAB}=\\text{사다리꼴 }AA'B'B=\\dfrac{1}{2}(y_{A}+y_{B})(x_{B}-x_{A})",
      "S_{\\triangle OAB}=\\dfrac{1}{2}(4+1)(4-1)=\\dfrac{15}{2}"
    ],
    exLabels: ["△OAB = 사다리꼴", "넓이 15/2"],
    exGraph: {
      f: x => 1.8 / (x + 0.5) + 0.25, GY0: 390, GV: 115, xr: [0.2, 3.0], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "A(1, 4)" }, r2: { x: 2.5, col: PK, label: "B(4, 1)" },
      fn: { t: "직각쌍곡선 y = k/x : 부채꼴 넓이 S = 아래 적분 넓이 T", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "S = T (등적변형)", finalS: "△OAB = 15/2", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 곡선 와이는 엑스분의 육 위의 두 점 에이 일 콤마 육과 비 삼 콤마 이에 대하여 삼각형 오 에이 비의 넓이는 얼마일까요?", cap: "$y=\\dfrac{6}{x}$ 위의 $A(1,6),\\ B(3,2)$ 일 때 $\\triangle OAB$ 넓이 (자작 문항)" },
      { say: "등적변형에 의해 삼각형 오 에이 비의 넓이는 엑스좌표 일부터 삼까지의 사다리꼴 넓이와 같습니다.", cap: "사다리꼴 넓이 $=\\dfrac{1}{2}(6+2)\\times(3-1)$" },
      { say: "이분의 일 곱하기 팔 곱하기 이므로 정답은 팔입니다.", cap: "$\\dfrac{1}{2}\\times 8\\times 2=8$" }
    ],
    examChips: [
      "A(1,6),\\quad B(3,2)\\quad \\left(y=\\dfrac{6}{x}\\right)",
      "S_{\\triangle OAB}=\\dfrac{1}{2}(6+2)(3-1)",
      "S_{\\triangle OAB}=8"
    ],
    examLabels: ["사다리꼴 등적변형", "정답 8"],
    examGraph: {
      f: x => 1.9 / (x + 0.5) + 0.25, GY0: 390, GV: 115, xr: [0.2, 3.0], area: [0.5, 2.3], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "A(1, 6)" }, r2: { x: 2.3, col: GO, label: "B(3, 2)" },
      fn: { t: "△OAB 넓이 = 사다리꼴 (6 + 2) × (3 − 1) / 2 = 8", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "사다리꼴 치환", finalS: "넓이 = 8", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 유리함수 위의 점에서 점근선에 수선을 내리면 직사각형 넓이는 언제나 절댓값 케이로 일정합니다.", cap: "① 점근선에 내린 직사각형 넓이 $=|k|$ 일정 (직각삼각형은 $|k|/2$)" },
      { say: "둘째, 원점과 두 점이 이루는 삼각형 넓이는 신발끈 공식 대신 엑스축 사다리꼴 넓이로 바꾸면 암산됩니다.", cap: "② $\\triangle OAB$ 넓이 $=$ $x$축(또는 $y$축) 사다리꼴 넓이!" },
      { say: "셋째, 미적분에서 곡선 아래 넓이 티를 정적분하면 케이 곱하기 엘엔 에이분의 비가 됩니다.", cap: "③ 미적분 연결: $S=T=\\int_{a}^{b}\\dfrac{k}{x}\\,dx=k\\ln\\dfrac{b}{a}$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 포물선의 초점 현 조화평균과 접선 마름모 등 7대 성질을 다루는 제이십삼강입니다.", cap: "제23강 · 포물선의 기하학적 성질 7가지" },
      { tag: "연계 ②", say: "초월함수를 다항함수로 근사하는 테일러 급수 제이십육강도 이어서 보세요.", cap: "제26강 · 테일러 급수 (초월함수의 다항식 근사)" },
      { tag: "이 사이트", say: "이 사이트의 제이십삼강과 제이십육강을 이어서 보세요.", cap: "제23강 · 포물선 7대 성질  /  제26강 · 테일러 급수" }
    ],
    nextLinks: [
      { lec: 23, label: "제23강 열기 (포물선 7대 성질)" },
      { lec: 26, label: "제26강 열기 (테일러 급수)" },
      { lec: 10, label: "제10강 열기 (유리함수 평행이동)" }
    ]
  },
  {
    lec: 23, subj: "geo",
    title: "숏츠식 판서 미리보기 · 포물선의 기하학적 성질 7가지 완전 정복",
    desc: "포물선 $y^{2}=4px$ 의 정의($\\overline{FP}=\\overline{PH}$), 초점 현의 조화평균 $\\frac{1}{a}+\\frac{1}{b}=\\frac{1}{p}$, 접선 마름모 성질을 정리합니다.",
    hookTitle: "포물선의 기하학적 성질 7가지", hookSub: "정의(FP=PH) · 조화평균 · 준선 직교 · 접선 마름모",
    hookSay: "복잡한 연립방정식 없이 포물선 문제를 10초 만에 푸는 기하 성질, 30초 만에 정리합니다.",
    hookCap: "포물선 핵심 기하 성질 · 30초 정리",
    whySay: "포물선은 초점까지의 거리와 준선까지의 거리가 같은 점들의 집합이므로, 항상 준선으로 수선의 발을 내려 길이를 옮기는 것이 모든 성질의 출발점입니다.",
    whyCap: "포물선 정의 $\\overline{FP}=x_{1}+p$ $\\Rightarrow$ 조화평균·접선 마름모 유도",
    histTag: "아폴로니오스", histSay: "원뿔을 모선에 평행한 평면으로 자른 단면 곡선에 포물선이라는 이름을 붙인 사람은 고대 그리스의 아폴로니오스입니다.",
    histCap: "아폴로니오스 《원뿔곡선론》과 포물선의 광학적 반사 성질",
    fParts: [
      { say: "포물선 와이 제곱은 사 피 엑스 위의 점에서 초점까지의 거리는 엑스좌표 더하기 피와 같습니다.", cap: "정의: $\\overline{FP}=\\overline{PH}=x_{1}+p$" },
      { say: "초점을 지나는 현이 초점에서 에이와 비로 나뉠 때 에이분의 일 더하기 비분의 일은 피분의 일로 일정합니다.", cap: "초점 현 조화평균: $\\dfrac{1}{a}+\\dfrac{1}{b}=\\dfrac{1}{p}$" },
      { say: "점 엑스 원에서의 접선의 엑스절편은 마이너스 엑스 원이므로 초점과 접점, 절편은 이등변삼각형과 마름모를 이룹니다.", cap: "접선 절편 $(-x_{1},0)\\ \\Longrightarrow\\ \\overline{FP}=\\overline{FT}=x_{1}+p$" }
    ],
    fChips: [
      "y^{2}=4px\\ \\Longrightarrow\\ \\overline{FP}=\\overline{PH}=x_{1}+p",
      "\\text{초점 현 조화평균: }\\dfrac{1}{a}+\\dfrac{1}{b}=\\dfrac{1}{p}\\quad (\\cos\\theta=\\dfrac{a-b}{a+b})",
      "\\text{접선 }x\\text{절편 }T(-x_{1},0)\\ \\Longrightarrow\\ \\overline{FP}=\\overline{FT}=x_{1}+p"
    ],
    fLabels: ["초점 거리 = x₁ + p", "조화평균 & 접선 마름모"],
    exParts: [
      { say: "예를 들어 와이 제곱은 팔 엑스의 초점을 지나는 직선이 포물선과 만나는 두 조각이 삼과 비일 때 비를 구해 봅시다.", cap: "$y^{2}=8x\\ (p=2)$ 에서 초점 현 조각 $a=3$ 일 때 $b$ 구하기" },
      { say: "초점 피는 이이므로 조화평균 공식 삼분의 일 더하기 비분의 일은 이분의 일이 성립합니다.", cap: "$\\dfrac{1}{3}+\\dfrac{1}{b}=\\dfrac{1}{2}$" },
      { say: "비분의 일이 육분의 일이므로 비는 육이고 현 전체 길이는 구입니다.", cap: "$\\dfrac{1}{b}=\\dfrac{1}{6}\\ \\Rightarrow\\ b=6,\\quad a+b=9$" }
    ],
    exChips: [
      "y^{2}=8x=4\\cdot 2x\\ \\Rightarrow\\ p=2",
      "\\dfrac{1}{3}+\\dfrac{1}{b}=\\dfrac{1}{2}\\ \\Rightarrow\\ \\dfrac{1}{b}=\\dfrac{1}{6}",
      "b=6,\\qquad \\text{초점 현 전체 길이 }a+b=3+6=9"
    ],
    exLabels: ["p = 2, a = 3", "b = 6 (현 길이 9)"],
    exGraph: {
      f: x => 1.35 * Math.sqrt(Math.max(0, x)), GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "초점 F(p, 0)" }, r2: { x: 2.2, col: PK, label: "FP = PH = x₁ + p" },
      fn: { t: "포물선 초점 현: 1/a + 1/b = 1/p  (3 과 6 → p = 2)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "1/3 + 1/b = 1/2", finalS: "b = 6", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 와이 제곱은 십이 엑스 위의 점 피에서 그은 접선의 엑스절편을 티라 할 때, 에프 티가 칠이면 점 피의 엑스좌표는 얼마일까요?", cap: "$y^{2}=12x$ 의 접선 절편 $T$ 에 대해 $\\overline{FT}=7$ 일 때 $x_{1}$ (자작 문항)" },
      { say: "초점 피는 삼이고, 접선 마름모 성질에 의해 에프 티의 길이는 엑스 원 더하기 삼입니다.", cap: "$p=3,\\quad \\overline{FT}=\\overline{FP}=x_{1}+3=7$" },
      { say: "따라서 엑스 원은 칠 빼기 삼, 사입니다.", cap: "$x_{1}=7-3=4$" }
    ],
    examChips: [
      "y^{2}=12x\\ \\Rightarrow\\ p=3,\\quad F(3,0)",
      "\\overline{FT}=\\overline{FP}=x_{1}+p=x_{1}+3=7",
      "x_{1}=4"
    ],
    examLabels: ["FT = FP = x₁ + p", "정답 x₁ = 4"],
    examGraph: {
      f: x => 1.35 * Math.sqrt(Math.max(0, x)), GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "초점 F(3, 0)" }, r2: { x: 2.3, col: GO, label: "접점 P(4, y₁)" },
      fn: { t: "접선 절편 T(−x₁, 0)  ⇒  FT = FP = x₁ + p = 7", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "x₁ + 3 = 7", finalS: "x₁ = 4", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 포물선 문제에서 초점 거리가 주어지면 즉시 준선을 긋고 엑스좌표 더하기 피로 바꿉니다.", cap: "① 포물선 제1원칙: 준선 작도 후 $\\overline{FP}=x_{1}+p$ 변환!" },
      { say: "둘째, 준선 위의 한 점에서 포물선에 그은 두 접선은 언제나 수직으로 만납니다.", cap: "② 준선 위의 점에서 그은 두 접선의 교각 $=90^{\\circ}$ (수직!)" },
      { say: "셋째, 초점을 지나는 직선의 기울기 각이 세타이면 코사인 세타는 에이 더하기 비분의 에이 빼기 비입니다.", cap: "③ 초점 현 기울기 공식: $\\cos\\theta=\\dfrac{a-b}{a+b}$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 초월함수를 다항함수로 바꾸는 미적분의 꽃, 테일러 급수 제이십육강입니다.", cap: "제26강 · 테일러 급수 (초월함수가 다항함수로 바뀌는 기적)" },
      { tag: "연계 ②", say: "기하 사슬의 출발점인 제오강 피타고라스 정리로 돌아가 복습할 수도 있습니다.", cap: "제5강 · 피타고라스 정리 유클리드 증명" },
      { tag: "이 사이트", say: "이 사이트의 제이십육강과 제오강을 이어서 보세요.", cap: "제26강 · 테일러 급수  /  제5강 · 피타고라스 정리" }
    ],
    nextLinks: [
      { lec: 26, label: "제26강 열기 (테일러 급수)" },
      { lec: 5, label: "제5강 열기 (기하 사슬 처음으로)" },
      { lec: 6, label: "제6강 열기 (수능 기하 7대 정리)" }
    ]
  },
  {
    lec: 26, subj: "geo",
    title: "숏츠식 판서 미리보기 · 테일러 급수와 초월함수 극한 근사",
    desc: "$x=0$ 에서 미분계수를 일치시키는 매클로린 급수 $f(x)=\\sum \\frac{f^{(n)}(0)}{n!}x^{n}$ 와 $e^{x},\\ \\sin x,\\ \\cos x$ 근사를 정리합니다.",
    hookTitle: "테일러 급수 · 초월함수의 다항식 변신", hookSub: "eˣ · sin x · cos x 전개와 극한 3초 풀이",
    hookSay: "초월함수가 다항함수로 바뀌는 원리와 극한을 3초 만에 푸는 테일러 근사법, 바로 정리합니다.",
    hookCap: "테일러·매클로린 급수 · 30초 정리",
    whySay: "엑스는 영에서 함숫값과 각 차수의 미분계수를 차례대로 일치시키면 엔 팩토리얼 분모가 생기며 곡선에 밀착합니다.",
    whyCap: "$n$번 미분 시 $x^{n}\\to n!$ 상쇄를 위해 계수 $\\dfrac{f^{(n)}(0)}{n!}$ 등장",
    histTag: "테일러·오일러", histSay: "브룩 테일러가 일반화했고, 오일러가 이를 통해 지수함수와 삼각함수를 하나로 묶은 오일러 공식을 완성했습니다.",
    histCap: "테일러 급수(1715)와 오일러 공식 $e^{ix}=\\cos x+i\\sin x$",
    fParts: [
      { say: "이의 엑스 제곱은 일 더하기 엑스 더하기 이 팩토리얼 분의 엑스 제곱으로 모든 차수가 양수입니다.", cap: "$e^{x}=1+x+\\dfrac{x^{2}}{2!}+\\dfrac{x^{3}}{3!}+\\cdots$" },
      { say: "사인 엑스는 홀수 차수만 교대로 나오고, 코사인 엑스는 짝수 차수만 교대로 나옵니다.", cap: "$\\sin x=x-\\dfrac{x^{3}}{3!}+\\cdots,\\quad \\cos x=1-\\dfrac{x^{2}}{2!}+\\dfrac{x^{4}}{4!}-\\cdots$" },
      { say: "영으로 가는 극한에서 일 빼기 코사인 엑스는 이분의 일 엑스 제곱, 엑스 빼기 사인 엑스는 육분의 일 엑스 세제곱입니다.", cap: "$x\\to 0$ 극한: $1-\\cos x\\approx\\dfrac{1}{2}x^{2},\\quad x-\\sin x\\approx\\dfrac{1}{6}x^{3}$" }
    ],
    fChips: [
      "e^{x}=1+x+\\dfrac{x^{2}}{2!}+\\dfrac{x^{3}}{3!}+\\cdots",
      "\\sin x=x-\\dfrac{x^{3}}{6}+\\cdots,\\qquad \\cos x=1-\\dfrac{x^{2}}{2}+\\dfrac{x^{4}}{24}-\\cdots",
      "x\\to 0\\text{ 근사: }1-\\cos x\\approx\\dfrac{1}{2}x^{2},\\quad x-\\sin x\\approx\\dfrac{1}{6}x^{3}"
    ],
    fLabels: ["3대 초월함수 전개", "x → 0 극한 다항식 근사"],
    exParts: [
      { say: "예를 들어 엑스가 영으로 갈 때 엑스 세제곱 분의 엑스 빼기 사인 엑스의 극한을 구해 봅시다.", cap: "$\\displaystyle\\lim_{x\\to 0}\\dfrac{x-\\sin x}{x^{3}}$ 의 극한값" },
      { say: "사인 엑스를 삼차 항까지 전개하면 앞의 엑스가 지워지고 육분의 일 엑스 세제곱이 남습니다.", cap: "$x-\\left(x-\\dfrac{x^{3}}{6}+\\cdots\\right)=\\dfrac{1}{6}x^{3}+\\cdots$" },
      { say: "따라서 분모 엑스 세제곱으로 나누면 극한값은 육분의 일입니다.", cap: "극한값 $=\\dfrac{1}{6}$" }
    ],
    exChips: [
      "\\sin x=x-\\dfrac{x^{3}}{3!}+\\dfrac{x^{5}}{5!}-\\cdots",
      "x-\\sin x=\\dfrac{1}{6}x^{3}-\\dfrac{1}{120}x^{5}+\\cdots",
      "\\lim_{x\\to 0}\\dfrac{x-\\sin x}{x^{3}}=\\dfrac{1}{6}"
    ],
    exLabels: ["sin x 3차 근사", "극한값 1/6"],
    exGraph: {
      f: x => Math.sin(x * 1.1) * 1.3 + 0.8, GY0: 390, GV: 110, xr: [0, 3], area: [0.2, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "1차 접선 y = x" }, r2: { x: 2.1, col: PK, label: "3차 근사 x − x³/6" },
      fn: { t: "차수가 높아질수록 다항식이 sin x 곡선에 완벽히 밀착!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "x − sin x ≈ x³/6", finalS: "극한값 = 1/6", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 엑스가 영으로 갈 때 엑스 제곱 분의 이의 이엑스 제곱 빼기 일 빼기 이엑스의 극한값은 얼마일까요?", cap: "$\\displaystyle\\lim_{x\\to 0}\\dfrac{e^{2x}-1-2x}{x^{2}}$ 구하기 (자작 문항)" },
      { say: "이의 티 제곱 전개식에 티 대신 이엑스를 넣으면 일 더하기 이엑스 더하기 이분의 사 엑스 제곱이 됩니다.", cap: "$e^{2x}\\approx 1+2x+\\dfrac{(2x)^{2}}{2!}=1+2x+2x^{2}$" },
      { say: "일 더하기 이엑스를 빼면 분자에 이 엑스 제곱만 남으므로 분모 엑스 제곱으로 나누면 정답은 이입니다.", cap: "$\\lim_{x\\to 0}\\dfrac{2x^{2}}{x^{2}}=2$" }
    ],
    examChips: [
      "e^{u}=1+u+\\dfrac{u^{2}}{2!}+\\cdots\\quad (u=2x\\text{ 대입})",
      "e^{2x}-1-2x=\\dfrac{(2x)^{2}}{2!}+\\cdots=2x^{2}+\\cdots",
      "\\lim_{x\\to 0}\\dfrac{e^{2x}-1-2x}{x^{2}}=2"
    ],
    examLabels: ["2차 항까지 전개", "정답 2"],
    examGraph: {
      f: x => 0.35 * Math.exp(0.75 * x), GY0: 390, GV: 110, xr: [0, 3], area: [0.2, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "1차 근사 1 + 2x" }, r2: { x: 2.1, col: GO, label: "2차 항 2x²" },
      fn: { t: "e^(2x) ≈ 1 + 2x + 2x²  ⇒  극한값 = 2", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(2x)² / 2! = 2x²", finalS: "극한값 = 2", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 영 분의 영 꼴 극한에서 일차 항이 서로 지워지면 테일러 급수의 이차 항이나 삼차 항이 극한값을 결정합니다.", cap: "① $0/0$ 꼴에서 1차 항 소거 시 $\\Longrightarrow$ 2차·3차 테일러 항이 주인공!" },
      { say: "둘째, 사인 엑스를 미분하면 코사인 엑스가 되듯 매클로린 급수도 항별로 미분하면 그대로 코사인 급수가 됩니다.", cap: "② $(\\sin x)'=\\left(x-\\dfrac{x^{3}}{3!}+\\cdots\\right)'=1-\\dfrac{x^{2}}{2!}+\\cdots=\\cos x$" },
      { say: "셋째, 탄젠트 엑스의 삼차 근사는 엑스 더하기 삼분의 일 엑스 세제곱이므로 사인과 부호가 반대입니다.", cap: "③ $\\tan x\\approx x+\\dfrac{1}{3}x^{3}\\ \\Rightarrow\\ \\tan x-\\sin x\\approx\\dfrac{1}{2}x^{3}$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "이로써 기하와 미적분 일곱 개 강의 사슬이 모두 완성되었습니다. 제오강 피타고라스 정리로 돌아가 복습해 보세요.", cap: "제5강 · 피타고라스 정리 유클리드 증명 (기하 사슬 처음으로)" },
      { tag: "연계 ②", say: "수학 투의 정적분 넓이 공식 제이강이나 수학 원의 삼각함수 제칠강으로도 이어갈 수 있습니다.", cap: "제2강 · 정적분 넓이 만능 공식 (수학 II)  /  제7강 · 삼각함수 (수학 I)" },
      { tag: "이 사이트", say: "이 사이트의 모든 세미나 강의를 단원별 사슬로 자유롭게탐구해 보세요.", cap: "전 단원(수학(하) · 수학 I · 수학 II · 기하&미적분) 숏츠 사슬 완성!" }
    ],
    nextLinks: [
      { lec: 5, label: "제5강 열기 (기하 사슬 처음으로)" },
      { lec: 2, label: "제2강 열기 (수학 II 넓이 공식)" },
      { lec: 7, label: "제7강 열기 (수학 I 삼각함수)" }
    ]
  }
];

const K = (texStr, disp) => {
  try { return window.katex.renderToString(texStr, { displayMode: !!disp, throwOnError: false }); }
  catch (e) { return String(texStr); }
};
const inline = s => String(s || "").replace(/\$([^$]+)\$/g, (m, t) => K(t));
const reduced = () => matchMedia("(prefers-reduced-motion: reduce)").matches;
const sleep = ms => new Promise(r => setTimeout(r, ms));
const estMs = t => Math.max(1800, Math.round(Array.from(t || "").length * 165) + 600);

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
    subj: spec.subj,
    hostId: `l${spec.lec}ShortsHost`,
    prefix: `l${spec.lec}s`,
    title: spec.title,
    desc: spec.desc,
    nextLinks: spec.nextLinks,
    SCENES,
    chipDefs
  };
}

const CONFIGS = GEO_SPECS.map(makeLectureConfig);
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
  if (typeof window.switchLecture === "function") {
    window.switchLecture(lecNum);
    setTimeout(() => { window.scrollTo({ top: 0, behavior: "smooth" }); }, 60);
    return;
  }
  if (typeof window.setLecture === "function") window.setLecture(lecNum, false);
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
    const mount = $(cfg.hostId);
    if (!mount || mount.dataset.ready) return;
    if (!window.katex) { setTimeout(init, 300); return; }
    mount.dataset.ready = "1";
    mount.innerHTML = `${geoChainNavHtml(cfg.lec)}
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
      const ok = await speak("안녕하세요. 핵심 공식을 함께 정리해 볼까요?");
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

const GEO_PLAYERS = {};
function initGeo() {
  CONFIGS.forEach(cfg => {
    if (!GEO_PLAYERS[cfg.lec]) GEO_PLAYERS[cfg.lec] = createPlayer(cfg);
    GEO_PLAYERS[cfg.lec].init();
  });
}

window.GeoShorts = { PLAYERS: GEO_PLAYERS, CONFIGS, initGeo };
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initGeo);
else initGeo();
window.addEventListener("load", initGeo);
})();
