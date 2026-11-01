/* 미적분 심화 (12강 사슬: 76 → 77 → 78 → 79 → 80 → 81 → 82 → 83 → 84 → 85 → 86 → 87)
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

const CALC_CHAIN = [
  { lec: 76, step: 1,  badge: "수열극한",      title: "수열의 극한 샌드위치와 등비수열 r^n 4구간 분류" },
  { lec: 77, step: 2,  badge: "프랙탈급수",    title: "무한급수 성질과 도형 등비급수 a/(1−r)" },
  { lec: 78, step: 3,  badge: "자연상수e",     title: "자연상수 e 정의와 지수·로그 극한 1차 근사" },
  { lec: 79, step: 4,  badge: "덧셈정리",      title: "삼각함수 덧셈정리·배각과 두 직선이 이루는 각" },
  { lec: 80, step: 5,  badge: "도형극한",      title: "삼각함수 극한 sin x/x 와 도형 극한 3초 근사" },
  { lec: 81, step: 6,  badge: "연쇄법칙",      title: "몫의 미분법·합성함수 연쇄법칙과 매개변수 미분" },
  { lec: 82, step: 7,  badge: "역함수미분",    title: "역함수 미분법 1/f'(a)과 이계도함수·변곡점" },
  { lec: 83, step: 8,  badge: "초월개형",      title: "수능 필수 초월함수 개형 (xe^{-x}, ln x/x)" },
  { lec: 84, step: 9,  badge: "치환적분",      title: "치환적분법과 속미분 분수 적분 ln|f(x)|" },
  { lec: 85, step: 10, badge: "부분적분",      title: "부분적분법(로다삼지)과 3초 도표적분(DI법)" },
  { lec: 86, step: 11, badge: "급수적분",      title: "정적분과 무한급수의 변환 3가지 치환 기준" },
  { lec: 87, step: 12, badge: "부피·길이",     title: "단면 넓이 적분 부피와 곡선의 길이·이동거리" }
];

function calcChainNavHtml(curLec) {
  const idx = CALC_CHAIN.findIndex(c => c.lec === curLec);
  const prev = idx > 0 ? CALC_CHAIN[idx - 1] : null;
  const next = idx >= 0 && idx < CALC_CHAIN.length - 1 ? CALC_CHAIN[idx + 1] : null;
  return `
    <div class="l2s-chain-box" style="margin-bottom:16px;padding:12px 14px;border-radius:12px;background:rgba(15,23,42,.82);border:1px solid rgba(52,211,153,.35)">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:10px">
        <span style="font-size:13px;font-weight:800;color:#6ee7b7">📗 미적분 심화 · 수업 단원·개념 연결 사슬 (${idx + 1} / ${CALC_CHAIN.length}단계)</span>
        <div style="display:flex;gap:6px">
          ${prev ? `<button type="button" class="l2s-btn" data-chain-lec="${prev.lec}">← 이전 (${prev.step}단계 · 제${prev.lec}강)</button>` : ""}
          ${next ? `<button type="button" class="l2s-btn on" data-chain-lec="${next.lec}">다음 (${next.step}단계 · 제${next.lec}강) →</button>` : `<button type="button" class="l2s-btn on" data-chain-lec="76">미적분 심화 첫 단계로 →</button>`}
        </div>
      </div>
      <div style="display:flex;gap:5px;flex-wrap:wrap">
        ${CALC_CHAIN.map(c => `
          <button type="button" data-chain-lec="${c.lec}" style="padding:4px 8px;border-radius:999px;font-size:11px;font-weight:700;cursor:pointer;border:1px solid ${c.lec === curLec ? '#34d399' : 'rgba(148,163,184,.28)'};background:${c.lec === curLec ? 'rgba(52,211,153,.22)' : 'rgba(15,23,42,.6)'};color:${c.lec === curLec ? '#6ee7b7' : '#cbd5e1'}">
            ${c.step}. 제${c.lec}강 (${c.badge})
          </button>
        `).join("")}
      </div>
    </div>
  `;
}

const CALC_SPECS_A = [
  {
    lec: 76,
    title: "숏츠식 판서 미리보기 · 수열의 극한 샌드위치 정리와 등비수열 r^n 4구간 분류",
    desc: "수열의 극한 대소관계(조임정리)와 등비수열 $r^{n}$ 이 포함된 함수 $f(x)=\\lim_{n\\to\\infty}\\frac{x^{n+1}}{x^{n}+1}$ 의 4구간 분류법을 정리합니다.",
    hookTitle: "등비수열 극한 4구간 & 대장항 법칙", hookSub: "밑의 절댓값 |r| 이 가장 큰 대장항만 남기고 다 지운다!",
    hookSay: "등비수열의 극한에서 분모·분자의 대장항만 보고 3초 만에 답을 내는 원리와 4구간 분류법, 바로 정리합니다.",
    hookCap: "수열의 극한과 등비수열 극한 · 30초 정리",
    whySay: "공비 알의 절댓값이 일보다 작으면 엔이 무한대로 갈 때 영으로 사라지고 일보다 크면 무한대로 커지므로, 절댓값이 일인 경계를 기준으로 네 구간으로 나누어야 함수가 정확히 정의됩니다.",
    whyCap: "등비수열 $r^{n}$ 수렴 조건: $-1\\lt r\\le 1$ (등호는 $+1$ 쪽에만 포함!)",
    histTag: "코시·바이어슈트라스", histSay: "무한수열의 수렴과 조임정리는 19세기 코시와 바이어슈트라스가 해석학의 엄밀한 기초를 세우면서 완성되었습니다.",
    histCap: "수열의 수렴 정의와 샌드위치 조임정리($a_{n}\\le b_{n}\\le c_{n}$)",
    fParts: [
      { say: "무한대 분의 무한대 꼴 등비수열 극한은 밑의 절댓값이 가장 큰 대장항의 계수 비로 바로 구합니다.", cap: "$\\lim_{n\\to\\infty}\\dfrac{a\\cdot 3^{n}+2^{n}}{b\\cdot 3^{n}-2^{n}}=\\dfrac{a}{b}$ (밑이 작은 $2^{n}$ 은 먼지처럼 소거!)" },
      { say: "공비에 미지수 엑스가 들어 있으면 절댓값 엑스가 일보다 클 때, 일보다 작을 때, 엑스가 일일 때, 마이너스 일일 때 네 구간으로 나눕니다.", cap: "$x^{n}$ 포함 극한 4분류: ① $|x|\\gt 1$ · ② $|x|\\lt 1$ · ③ $x=1$ · ④ $x=-1$" },
      { say: "부등식 에이엔보다 비엔이 크더라도 극한을 취하면 같아질 수 있으므로 반드시 등호가 생깁니다.", cap: "샌드위치 정리: $a_{n}\\lt b_{n}\\lt c_{n}$ 이고 양 끝 극한이 $\\alpha$ 이면 $\\lim b_{n}=\\alpha$" }
    ],
    fChips: [
      "r^{n}\\text{ 수렴}\\iff -1\\lt r\\le 1,\\ ar^{n-1}\\text{ 수렴}\\iff a=0\\text{ 또는 }-1\\lt r\\le 1",
      "|x|\\lt 1\\implies \\lim x^{n}=0,\\quad |x|\\gt 1\\implies \\dfrac{1}{x^{n}}\\to 0\\text{ (최고차 나눔)}",
      "a_{n}\\lt b_{n}\\text{ 이어도 }\\lim a_{n}\\le\\lim b_{n}\\quad (\\text{극한 취하면 등호 생성!})"
    ],
    fLabels: ["수렴 조건 −1 < r ≤ 1", "4구간 분류 & 샌드위치"],
    exParts: [
      { say: "예를 들어 리미트 엔이 무한대로 갈 때 삼의 엔 제곱 더하기 이의 엔 제곱 분의 삼의 엔 더하기 일 제곱 빼기 이의 엔 제곱을 구해 봅시다.", cap: "$\\lim_{n\\to\\infty}\\dfrac{3^{n+1}-2^{n}}{3^{n}+2^{n}}$ 의 값 구하기" },
      { say: "밑이 더 작은 이의 엔 제곱은 지워지고 대장항인 삼의 엔 제곱만 남습니다.", cap: "$2^{n}$ 항 소거 $\\Rightarrow\\ \\dfrac{3\\cdot 3^{n}}{1\\cdot 3^{n}}$" },
      { say: "따라서 계수 비는 일 분의 삼, 삼입니다.", cap: "극한값 $=3$" }
    ],
    exChips: [
      "\\lim_{n\\to\\infty}\\dfrac{3^{n+1}-2^{n}}{3^{n}+2^{n}}=\\lim_{n\\to\\infty}\\dfrac{3\\cdot 3^{n}-2^{n}}{1\\cdot 3^{n}+2^{n}}",
      "\\text{대장항 }3^{n}\\text{ 계수 비교 (밑이 작은 }2^{n}\\text{ 소거)}",
      "=\\dfrac{3}{1}=3"
    ],
    exLabels: ["대장항 3^n 만 남기기", "극한값 = 3"],
    exGraph: {
      f: x => 1.55 / (1 + Math.exp(-3 * (x - 1.5))) + 0.25, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "|x| < 1 (x^n → 0)" }, r2: { x: 2.3, col: PK, label: "|x| > 1 (x^n 대장)" },
      fn: { t: "x^n 극한 함수는 경계 x = ±1 에서 불연속이 생기기 쉽다!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "3·3^n / 1·3^n", finalS: "극한값 = 3", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 수열 에이엔이 모든 자연수 엔에 대하여 삼 엔 더하기 일보다 크고 삼 엔 더하기 사보다 작을 때, 리미트 엔이 무한대로 갈 때 엔 분의 에이엔의 값은 얼마일까요?", cap: "$3n+1\\lt a_{n}\\lt 3n+4$ 일 때 $\\lim_{n\\to\\infty}\\dfrac{a_{n}}{n}$ 의 값 (자작 문항)" },
      { say: "세 변을 모두 양수 엔으로 나누면 좌변은 삼 더하기 엔분의 일, 우변은 삼 더하기 엔분의 사가 됩니다.", cap: "$3+\\dfrac{1}{n}\\lt\\dfrac{a_{n}}{n}\\lt 3+\\dfrac{4}{n}$" },
      { say: "양 끝이 모두 삼으로 수렴하므로 조임정리에 의해 구하는 극한값도 삼입니다.", cap: "양 끝 극한 $=3\\ \\Rightarrow\\ \\lim_{n\\to\\infty}\\dfrac{a_{n}}{n}=3$" }
    ],
    examChips: [
      "3n+1\\lt a_{n}\\lt 3n+4\\ \\xrightarrow{\\div n}\\ 3+\\dfrac{1}{n}\\lt\\dfrac{a_{n}}{n}\\lt 3+\\dfrac{4}{n}",
      "\\lim_{n\\to\\infty}\\left(3+\\dfrac{1}{n}\\right)=3,\\qquad \\lim_{n\\to\\infty}\\left(3+\\dfrac{4}{n}\\right)=3",
      "\\therefore\\ \\lim_{n\\to\\infty}\\dfrac{a_{n}}{n}=3"
    ],
    examLabels: ["양변 n 으로 나누기", "정답 3"],
    examGraph: {
      f: x => 1.1 + 0.4 * Math.exp(-1.2 * x) * Math.cos(3 * x), GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "상한·하한 조임" }, r2: { x: 2.4, col: GO, label: "극한 α = 3" },
      fn: { t: "샌드위치 조임정리: 양 끝이 같은 값 α 로 가면 가운데도 무조건 α!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "3 ≤ lim ≤ 3", finalS: "3", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 등비수열 에이 곱하기 알의 엔 빼기 일 제곱이 수렴할 조건에서는 공비 조건뿐 아니라 첫째항 에이가 영일 때도 수렴한다는 점을 절대 놓치면 안 됩니다.", cap: "① 서술형 감점 1순위: $ar^{n-1}$ 수렴 조건 $\\Longleftrightarrow$ $a=0$ 또는 $-1\\lt r\\le 1$!" },
      { say: "둘째, 루트 빼기 루트 꼴의 무한대 빼기 무한대 극한은 유리화 대신 근호 안의 일차항 계수의 절반으로 암산할 수 있습니다.", cap: "② 암산 꿀팁: $\\lim_{n\\to\\infty}\\left(\\sqrt{n^{2}+an}-\\sqrt{n^{2}+bn}\\right)=\\dfrac{a-b}{2}$!" },
      { say: "셋째, 함수의 극한 성질 진위판정을 다루는 수학 투 제이십구강과 함께 보면 극한 진위 문제가 완벽해집니다.", cap: "③ 제29강 연계: 수렴하는 두 수열끼리만 사칙연산(분모 $\\neq 0$) 성립!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 무한급수의 수렴 판정과 도형 프랙탈 등비급수를 다루는 제칠십칠강입니다.", cap: "제77강 · 무한급수 성질과 도형 등비급수 $\\dfrac{a}{1-r}$" },
      { tag: "연계 ②", say: "극한 성질 진위판정을 다루는 제이십구강도 함께 보세요.", cap: "제29강 · 함수의 극한 성질 진위판정 (수학 II)" },
      { tag: "이 사이트", say: "이 사이트의 제칠십칠강과 제이십구강을 이어서 보세요.", cap: "제77강 · 무한등비급수 도형  /  제29강 · 극한 진위판정" }
    ],
    nextLinks: [
      { lec: 77, label: "제77강 열기 (도형 등비급수)" },
      { lec: 29, label: "제29강 열기 (극한 진위판정)" },
      { lec: 25, label: "제25강 열기 (수열 점화식)" }
    ]
  },
  {
    lec: 77,
    title: "숏츠식 판서 미리보기 · 무한급수 성질과 도형 등비급수 a/(1−r)",
    desc: "무한급수 수렴 판정($\\sum a_{n}$ 수렴 $\\Rightarrow \\lim a_{n}=0$), 부분분수 망원급수와 도형 프랙탈 등비급수 $S=\\frac{a}{1-r}$ (넓이비 $=\\text{길이비}^{2}$)를 정리합니다.",
    hookTitle: "도형 무한등비급수 S = a / (1 − r)", hookSub: "첫째항 a 구하고 · 닮음비 1:k 이면 넓이 공비 r = k²!",
    hookSay: "수능 미적분에 매년 출제되는 프랙탈 도형 무한등비급수를 닮음비 하나로 3초 만에 푸는 법, 바로 정리합니다.",
    hookCap: "무한급수와 도형 등비급수 · 30초 정리",
    whySay: "부분합 에스엔이 수렴하면 에스엔 빼기 에스엔마이너스일인 일반항 에이엔의 극한은 반드시 영이 되어야 하며, 등비급수는 절댓값 알이 일보다 작을 때 일 빼기 알 분의 에이로 수렴합니다.",
    whyCap: "$\\sum_{n=1}^{\\infty}a_{n}$ 수렴 $\\Longrightarrow\\ \\lim_{n\\to\\infty}a_{n}=0$, 등비급수 합 $S=\\dfrac{a}{1-r}\\ (|r|\\lt 1)$",
    histTag: "제논·아르키메데스", histSay: "제논의 역설에서 출발한 무한합의 개념은 아르키메데스의 포물선 넓이 급수와 오일러의 무한급수 연구로 완성되었습니다.",
    histCap: "등비급수 수렴($|r|\\lt 1$)과 부분분수 망원급수(Telescoping Series)",
    fParts: [
      { say: "급수 시그마 에이엔이 수렴하면 리미트 에이엔은 무조건 영이며, 대우명제에 의해 리미트 에이엔이 영이 아니면 급수는 백 퍼센트 발산합니다.", cap: "급수 수렴 필요조건: $\\sum a_{n}$ 수렴 $\\Longrightarrow\\ \\lim_{n\\to\\infty}a_{n}=0$ (역은 성립 안 함!)" },
      { say: "등비급수의 수렴 조건은 등비수열보다 범위가 좁아 플러스 일일 때도 발산하므로 공비 알이 마이너스 일 초과 일 미만일 때만 일 빼기 알 분의 에이로 수렴합니다.", cap: "등비급수 수렴: $-1\\lt r\\lt 1$ ($r=1$ 제외!) $\\Longrightarrow\\ S=\\dfrac{a}{1-r}$" },
      { say: "도형 프랙탈 문제에서는 도형 전체를 직접 구하지 말고 외접하는 큰 정사각형이나 원의 길이 닮음비 케이를 구해 제곱하면 넓이 공비 알이 바로 나옵니다.", cap: "도형 급수 핵심: 길이 닮음비 $1:k\\ \\Longrightarrow\\ \\text{넓이 공비 }r=k^{2}$ (개수가 $m$배면 $r=mk^{2}$!)" }
    ],
    fChips: [
      "\\sum_{n=1}^{\\infty}a_{n}\\text{ 수렴}\\implies \\lim a_{n}=0,\\quad \\sum_{n=1}^{\\infty}ar^{n-1}=\\dfrac{a}{1-r}\\ (|r|\\lt 1)",
      "\\text{부분분수 급수: }\\sum_{n=1}^{\\infty}\\dfrac{1}{n(n+k)}=\\dfrac{1}{k}\\left(1+\\dfrac{1}{2}+\\cdots+\\dfrac{1}{k}\\right)",
      "\\text{프랙탈 넓이 급수: 길이비 }1:k,\\ \\text{개수비 }1:m\\ \\Longrightarrow\\ \\text{공비 }r=m\\cdot k^{2}"
    ],
    fLabels: ["등비급수 S = a / (1 − r)", "닮음비 제곱 r = m·k²"],
    exParts: [
      { say: "예를 들어 첫째항 넓이가 십팔이고 길이의 닮음비가 삼 대 일로 계속 줄어드는 정사각형들의 넓이의 총합을 구해 봅시다.", cap: "첫째항 넓이 $a=18$, 길이 닮음비 $3:1$ 인 무한 도형 넓이 합" },
      { say: "길이 비가 일 대 삼분의 일이므로 넓이의 공비 알은 제곱한 구분의 일입니다.", cap: "길이비 $1:\\dfrac{1}{3}\\ \\Rightarrow\\ \\text{넓이 공비 }r=\\left(\\dfrac{1}{3}\\right)^{2}=\\dfrac{1}{9}$" },
      { say: "따라서 일 빼기 구분의 일 분의 십팔이므로 사분의 팔십일입니다.", cap: "$S=\\dfrac{18}{1-1/9}=\\dfrac{18}{8/9}=\\dfrac{81}{4}$" }
    ],
    exChips: [
      "a=18,\\qquad \\text{길이비 }=\\dfrac{1}{3}\\ \\Longrightarrow\\ \\text{넓이 공비 }r=\\left(\\dfrac{1}{3}\\right)^{2}=\\dfrac{1}{9}",
      "S=\\dfrac{a}{1-r}=\\dfrac{18}{1-\\frac{1}{9}}",
      "=\\dfrac{81}{4}"
    ],
    exLabels: ["넓이 공비 r = (1/3)² = 1/9", "합 S = 81/4"],
    exGraph: {
      f: x => 1.7 * (1 - Math.exp(-1.3 * x)) + 0.25, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.5, col: CY, label: "첫째항 a = 18" }, r2: { x: 2.5, col: PK, label: "수렴값 a/(1−r)" },
      fn: { t: "도형 등비급수: 외접 도형의 길이비 k 를 구해 r = k² 대입!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "18 / (8/9)", finalS: "81 / 4", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 급수 시그마 엔은 일부터 무한대까지 엔 분의 에이엔 빼기 사가 수렴할 때, 리미트 엔이 무한대로 갈 때 이 엔 더하기 일 분의 삼 에이엔의 값은 얼마일까요?", cap: "$\\sum_{n=1}^{\\infty}\\left(\\dfrac{a_{n}}{n}-4\\right)$ 가 수렴할 때 $\\lim_{n\\to\\infty}\\dfrac{3a_{n}}{2n+1}$ (자작 문항)" },
      { say: "급수가 수렴하므로 괄호 안의 일반항 엔 분의 에이엔 빼기 사의 극한이 영이어야 합니다. 즉 엔 분의 에이엔의 극한은 사입니다.", cap: "$\\lim_{n\\to\\infty}\\left(\\dfrac{a_{n}}{n}-4\\right)=0\\ \\Rightarrow\\ \\lim_{n\\to\\infty}\\dfrac{a_{n}}{n}=4$" },
      { say: "구하는 식의 분모·분자를 엔으로 나누면 이 분의 삼 곱하기 사가 되어 정답은 육입니다.", cap: "$\\lim_{n\\to\\infty}\\dfrac{3(a_{n}/n)}{2+1/n}=\\dfrac{3\\times 4}{2}=6$" }
    ],
    examChips: [
      "\\sum_{n=1}^{\\infty}\\left(\\dfrac{a_{n}}{n}-4\\right)\\text{ 수렴}\\ \\Longrightarrow\\ \\lim_{n\\to\\infty}\\dfrac{a_{n}}{n}=4",
      "\\lim_{n\\to\\infty}\\dfrac{3a_{n}}{2n+1}=\\lim_{n\\to\\infty}\\dfrac{3\\cdot\\frac{a_{n}}{n}}{2+\\frac{1}{n}}",
      "=\\dfrac{3\\times 4}{2}=6"
    ],
    examLabels: ["lim(a_n/n) = 4", "정답 6"],
    examGraph: {
      f: x => 1.5 * Math.exp(-1.2 * x) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.6, col: CY, label: "급수 수렴 → 일반항 → 0" }, r2: { x: 2.3, col: GO, label: "3×4 / 2 = 6" },
      fn: { t: "∑(일반항) 수렴 ⇒ lim(일반항) = 0 으로 극한값 즉시 추출!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "3 × 4 / 2", finalS: "6", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 등비수열의 수렴 조건에는 알은 일이 포함되지만 등비급수의 수렴 조건에는 알은 일이 빠진다는 차이를 꼭 기억하세요.", cap: "① 수렴 조건 비교: 등비수열 $-1\\lt r\\le 1$ vs 등비급수 $-1\\lt r\\lt 1$ ($r=1$ 제외!)" },
      { say: "둘째, 그림이 두 갈래씩 갈라지는 나무 모양 프랙탈에서는 한 개당 넓이 비 케이 제곱에 개수 증가 배수 이까지 곱해 공비를 이 케이 제곱으로 잡아야 합니다.", cap: "② 개수 증가 프랙탈 주의: 도형이 매 단계 $m$배로 늘어나면 공비 $r=m\\cdot k^{2}$!" },
      { say: "셋째, 원과 접선이 포함된 프랙탈 도형은 기하 기본기인 제삼십사강, 제삼십오강과 함께 보면닮음비가 한눈에 보입니다.", cap: "③ 제34·35강 도형 연계: 직각삼각형 닮음·원 중심선 피타고라스로 $k$ 도출!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 미적분의 주인공인 자연상수 이의 정의와 지수·로그함수의 극한을 다루는 제칠십팔강입니다.", cap: "제78강 · 자연상수 $e$ 정의와 지수·로그함수 극한" },
      { tag: "연계 ②", say: "도형 닮음비를 빠르게 찾는 제삼십사강, 제삼십오강도 함께 보세요.", cap: "제34강 · 중학도형 총정리  /  제35강 · 원의 성질 총정리" },
      { tag: "이 사이트", say: "이 사이트의 제칠십팔강과 제삼십오강을 이어서 보세요.", cap: "제78강 · 자연상수 $e$ 와 지수·로그 극한  /  제35강 · 원의 성질" }
    ],
    nextLinks: [
      { lec: 78, label: "제78강 열기 (자연상수 e 극한)" },
      { lec: 35, label: "제35강 열기 (원의 성질 총정리)" },
      { lec: 76, label: "제76강 열기 (수열의 극한)" }
    ]
  },
  {
    lec: 78,
    title: "숏츠식 판서 미리보기 · 자연상수 e 정의와 지수·로그 극한 1차 근사",
    desc: "자연상수 $e=\\lim_{x\\to 0}(1+x)^{1/x}$ 의 역수 지수 맞추기와 $\\frac{e^{x}-1}{x}\\to 1,\\ \\frac{\\ln(1+x)}{x}\\to 1$ 의 원점 접선 1차 근사를 정리합니다.",
    hookTitle: "자연상수 e & 지수·로그 극한 1초 근사", hookSub: "x → 0 일 때 e^x − 1 ≈ x · ln(1 + x) ≈ x 로 즉시 치환!",
    hookSay: "지수함수와 로그함수의 극한을 복잡한 변형 없이 1초 만에 암산하는 원점 접선 근사법, 바로 정리합니다.",
    hookCap: "자연상수 e 와 지수·로그 극한 · 30초 정리",
    whySay: "엑스는 영에서 와이는 이의 엑스 제곱 빼기 일과 와이는 엘엔 일 더하기 엑스의 접선의 기울기가 모두 정확히 일이므로, 영 근처에서 두 함수는 직선 와이는 엑스와 똑같이 행동합니다.",
    whyCap: "$x\\to 0$ 일 때 접선 근사: $e^{ax}-1\\approx ax,\\qquad \\ln(1+bx)\\approx bx$",
    histTag: "베르누이·오일러", histSay: "자연상수 e는 야코프 베르누이가 연속 복리 이자를 계산하며 발견했고, 오일러가 기호 e를 도입해 미적분학의 표준 밑으로 확립했습니다.",
    histCap: "연속 복리 극한 $e=\\lim_{n\\to\\infty}\\left(1+\\dfrac{1}{n}\\right)^{n}\\approx 2.71828$",
    fParts: [
      { say: "일 더하기 영의 무한대 제곱 꼴은 괄호 안의 일 뒤에 더해진 식과 지수가 정확히 역수 관계일 때 자연상수 이가 됩니다.", cap: "$\\lim_{\\square\\to 0}(1+\\square)^{\\frac{1}{\\square}}=e\\ \\Longrightarrow\\ \\lim_{x\\to 0}(1+ax)^{\\frac{b}{x}}=e^{ab}$" },
      { say: "엑스가 영으로 갈 때 엑스 분의 이의 엑스 제곱 빼기 일과 엑스 분의 엘엔 일 더하기 엑스는 모두 일로 수렴합니다.", cap: "$\\lim_{x\\to 0}\\dfrac{e^{x}-1}{x}=1,\\qquad \\lim_{x\\to 0}\\dfrac{\\ln(1+x)}{x}=1$" },
      { say: "밑이 이가 아닌 일반 밑 에이일 때는 지수 극한에는 분자에 엘엔 에이가 곱해지고, 로그 극한에는 분모에 엘엔 에이가 들어갑니다.", cap: "$\\lim_{x\\to 0}\\dfrac{a^{x}-1}{x}=\\ln a,\\qquad \\lim_{x\\to 0}\\dfrac{\\log_{a}(1+x)}{x}=\\dfrac{1}{\\ln a}$" }
    ],
    fChips: [
      "\\lim_{x\\to 0}(1+ax)^{\\frac{b}{x}}=e^{ab},\\qquad \\lim_{x\\to 0}\\dfrac{e^{ax}-1}{bx}=\\dfrac{a}{b}",
      "\\lim_{x\\to 0}\\dfrac{\\ln(1+ax)}{bx}=\\dfrac{a}{b}",
      "\\lim_{x\\to 0}\\dfrac{a^{x}-1}{x}=\\ln a,\\qquad \\lim_{x\\to 0}\\dfrac{\\log_{a}(1+x)}{x}=\\dfrac{1}{\\ln a}"
    ],
    fLabels: ["(1 + ax)^(b/x) = e^(ab)", "e^(ax)−1 ≈ ax, ln(1+ax) ≈ ax"],
    exParts: [
      { say: "예를 들어 리미트 엑스가 영으로 갈 때 엘엔 일 더하기 이 엑스 분의 이에 육 엑스 제곱 빼기 일의 극한값을 구해 봅시다.", cap: "$\\lim_{x\\to 0}\\dfrac{e^{6x}-1}{\\ln(1+2x)}$ 의 값 구하기" },
      { say: "영 근처에서 분자는 육 엑스로, 분모는 이 엑스로 근사됩니다.", cap: "$e^{6x}-1\\approx 6x,\\qquad \\ln(1+2x)\\approx 2x$" },
      { say: "따라서 계수 비인 이 분의 육, 삼입니다.", cap: "$\\dfrac{6x}{2x}=3$" }
    ],
    exChips: [
      "\\lim_{x\\to 0}\\dfrac{e^{6x}-1}{\\ln(1+2x)}",
      "=\\lim_{x\\to 0}\\left(\\dfrac{e^{6x}-1}{6x}\\cdot\\dfrac{2x}{\\ln(1+2x)}\\cdot\\dfrac{6}{2}\\right)",
      "=1\\cdot 1\\cdot 3=3"
    ],
    exLabels: ["6x / 2x 계수 비교", "극한값 = 3"],
    exGraph: {
      f: x => 0.45 * (Math.exp(0.9 * (x - 1.2)) - 1) + 0.8, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.2, col: CY, label: "원점 (0, 0) 접선 기울기 1" }, r2: { x: 2.2, col: PK, label: "e^x−1 ≈ x ≈ ln(1+x)" },
      fn: { t: "원점(x=0)에서 e^x − 1 과 ln(1 + x) 는 직선 y = x 에 동시에 접한다!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "6x / 2x", finalS: "극한값 = 3", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 함수 에프 엑스가 엑스가 영이 아닐 때 삼 엑스 분의 엘엔 일 더하기 구 엑스이고 엑스는 영에서 연속일 때, 에프 영의 값은 얼마일까요?", cap: "$x\\neq 0$ 에서 $f(x)=\\dfrac{\\ln(1+9x)}{3x}$ 가 $x=0$ 에서 연속일 때 $f(0)$ (자작 문항)" },
      { say: "엑스는 영에서 연속이므로 에프 영은 엑스가 영으로 갈 때의 극한값과 같습니다.", cap: "$f(0)=\\lim_{x\\to 0}\\dfrac{\\ln(1+9x)}{3x}$" },
      { say: "분자 엘엔 일 더하기 구 엑스는 구 엑스와 같으므로 삼 엑스 분의 구 엑스, 정답은 삼입니다.", cap: "$\\dfrac{9}{3}=3$" }
    ],
    examChips: [
      "f(0)=\\lim_{x\\to 0}f(x)=\\lim_{x\\to 0}\\dfrac{\\ln(1+9x)}{3x}",
      "=\\lim_{x\\to 0}\\dfrac{\\ln(1+9x)}{9x}\\times\\dfrac{9}{3}",
      "=1\\times 3=3"
    ],
    examLabels: ["9x / 3x 계수 비", "정답 f(0) = 3"],
    examGraph: {
      f: x => 0.9 * Math.log(1 + 0.8 * x) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.3, col: CY, label: "x → 0 극한" }, r2: { x: 2.2, col: GO, label: "f(0) = 9/3 = 3" },
      fn: { t: "연속 조건: f(0) = lim [ln(1 + 9x) / 3x] = 9 / 3 = 3", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "9 / 3", finalS: "f(0) = 3", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 이에 에이 엑스 제곱 빼기 이에 비 엑스 제곱이 분자에 있으면 가운데에 빼기 일 더하기 일을 넣어 에이 빼기 비 곱하기 엑스로 바로 바꿉니다.", cap: "① $e^{ax}-e^{bx}=(e^{ax}-1)-(e^{bx}-1)\\approx(a-b)x$ 즉시 암산!" },
      { say: "둘째, 엑스가 영이 아니라 에이로 갈 때는 엑스 빼기 에이를 티로 치환해 티가 영으로 가는 표준 공식으로 바꿉니다.", cap: "② $x\\to a$ 일 때의 초월극한: 무조건 $t=x-a\\ (t\\to 0)$ 치환!" },
      { say: "셋째, 이 원점 일차 근사는 제이십육강의 테일러 급수 일차항에서 나온 원리이므로 함께 보면 완벽히 이해됩니다.", cap: "③ 제26강 테일러 급수 연결: $e^{x}=1+x+\\dfrac{x^{2}}{2!}+\\cdots$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 삼각함수의 덧셈정리와 두 직선이 이루는 각을 다루는 제칠십구강입니다.", cap: "제79강 · 삼각함수 덧셈정리·배각과 두 직선이 이루는 각" },
      { tag: "연계 ②", say: "초월함수의 테일러 급수 근사를 다루는 제이십육강도 함께 보세요.", cap: "제26강 · 테일러 급수 (초월함수의 다항식 근사)" },
      { tag: "이 사이트", say: "이 사이트의 제칠십구강과 제이십육강을 이어서 보세요.", cap: "제79강 · 삼각함수 덧셈정리  /  제26강 · 테일러 급수" }
    ],
    nextLinks: [
      { lec: 79, label: "제79강 열기 (삼각함수 덧셈정리)" },
      { lec: 26, label: "제26강 열기 (테일러 급수)" },
      { lec: 80, label: "제80강 열기 (삼각함수 도형극한)" }
    ]
  },
  {
    lec: 79,
    title: "숏츠식 판서 미리보기 · 삼각함수 덧셈정리·배각과 두 직선이 이루는 각",
    desc: "$\\sin(\\alpha\\pm\\beta),\\ \\cos(\\alpha\\pm\\beta),\\ \\tan(\\alpha\\pm\\beta)$ 덧셈정리와 배각공식, 두 직선이 이루는 예각 $\\tan\\theta=\\left|\\frac{m_{1}-m_{2}}{1+m_{1}m_{2}}\\right|$ 를 정리합니다.",
    hookTitle: "삼각함수 덧셈정리 & 두 직선 각 tan θ", hookSub: "싸코코싸 · 코코마싸싸 · 일마탄탄 분의 탄뿔탄!",
    hookSay: "삼각함수 미분과 도형 문제의 필수 무기인 덧셈정리와 두 직선이 이루는 각 탄젠트 공식, 30초 만에 정리합니다.",
    hookCap: "삼각함수 덧셈정리와 배각공식 · 30초 정리",
    whySay: "단위원을 알파만큼 회전한 뒤 다시 베타만큼 회전하는 행렬 변환이나 피타고라스·코사인법칙을 적용하면 합과 차의 삼각함수가 각 삼각함수의 곱으로 분해됩니다.",
    whyCap: "기울기 $m_{1}=\\tan\\alpha,\\ m_{2}=\\tan\\beta\\ \\Longrightarrow\\ \\tan(\\alpha-\\beta)=\\dfrac{m_{1}-m_{2}}{1+m_{1}m_{2}}$",
    histTag: "프톨레마이오스", histSay: "삼각함수 덧셈정리는 고대 천문학자 프톨레마이오스가 알마게스트에서 원에 내접하는 사각형의 프톨레마이오스 정리로 유도했습니다.",
    histCap: "프톨레마이오스 현의 표와 삼각함수 덧셈정리·배각공식",
    fParts: [
      { say: "사인 알파 더하기 베타는 싸코코싸로 부호가 같고, 코사인 알파 더하기 베타는 코코마싸싸로 부호가 반대입니다.", cap: "$\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta,\\quad \\cos(\\alpha\\pm\\beta)=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta$" },
      { say: "탄젠트 알파 빼기 베타는 일 더하기 탄탄 분의 탄 빼기 탄이며, 두 직선의 기울기 엠원과 엠투를 넣으면 두 직선이 이루는 예각의 탄젠트가 됩니다.", cap: "두 직선이 이루는 예각 $\\theta$: $\\tan\\theta=\\left|\\dfrac{m_{1}-m_{2}}{1+m_{1}m_{2}}\\right|$" },
      { say: "베타 자리에 알파를 넣으면 사인 이 알파는 이 사인 코사인이고, 코사인 이 알파는 코사인 제곱 빼기 사인 제곱인 배각공식이 됩니다.", cap: "배각공식: $\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha,\\quad \\cos 2\\alpha=2\\cos^{2}\\alpha-1=1-2\\sin^{2}\\alpha$" }
    ],
    fChips: [
      "\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta\\quad (\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha)",
      "\\cos(\\alpha\\pm\\beta)=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta\\quad (\\cos 2\\alpha=2\\cos^{2}\\alpha-1)",
      "\\tan(\\alpha\\pm\\beta)=\\dfrac{\\tan\\alpha\\pm\\tan\\beta}{1\\mp\\tan\\alpha\\tan\\beta},\\qquad \\tan\\theta=\\left|\\dfrac{m_{1}-m_{2}}{1+m_{1}m_{2}}\\right|"
    ],
    fLabels: ["싸코코싸 · 코코마싸싸", "두 직선 예각 & 배각공식"],
    exParts: [
      { say: "예를 들어 두 직선 와이는 삼 엑스 더하기 일과 와이는 이분의 일 엑스 빼기 일이 이루는 예각의 크기를 세타라 할 때 세타를 구해 봅시다.", cap: "두 직선 $y=3x+1$ 과 $y=\\dfrac{1}{2}x-1$ 이 이루는 예각 $\\theta$" },
      { say: "기울기가 삼과 이분의 일이므로 탄젠트 공식에 대입하면 일 더하기 이분의 삼 분에 삼 빼기 이분의 일입니다.", cap: "$\\tan\\theta=\\left|\\dfrac{3-1/2}{1+3\\cdot(1/2)}\\right|=\\dfrac{5/2}{5/2}=1$" },
      { say: "탄젠트 세타가 일이므로 예각 세타는 사분의 파이, 사십오도입니다.", cap: "$\\tan\\theta=1\\ \\Rightarrow\\ \\theta=\\dfrac{\\pi}{4}\\ (45^\\circ)$" }
    ],
    exChips: [
      "m_{1}=3,\\qquad m_{2}=\\dfrac{1}{2}",
      "\\tan\\theta=\\left|\\dfrac{3-\\frac{1}{2}}{1+3\\cdot\\frac{1}{2}}\\right|=\\dfrac{\\frac{5}{2}}{\\frac{5}{2}}=1",
      "\\therefore\\ \\theta=\\dfrac{\\pi}{4}\\quad (45^\\circ)"
    ],
    exLabels: ["분모 5/2, 분자 5/2", "θ = π/4 (45°)"],
    exGraph: {
      f: x => 0.75 * Math.sin(1.2 * x) + 0.9, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "기울기 m₁ = tan α" }, r2: { x: 2.1, col: PK, label: "기울기 m₂ = tan β" },
      fn: { t: "두 직선의 각 θ = |α − β| ⇒ tan θ = |(m₁ − m₂) / (1 + m₁m₂)|", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(5/2) / (5/2)", finalS: "θ = π/4", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 그림이나 좌표에서 탄젠트 알파가 이분의 일이고 탄젠트 베타가 삼분의 일일 때, 알파 더하기 베타가 예각이면 그 크기는 얼마일까요?", cap: "$\\tan\\alpha=\\dfrac{1}{2},\\ \\tan\\beta=\\dfrac{1}{3}$ 일 때 예각 $\\alpha+\\beta$ 의 크기 (자작 문항)" },
      { say: "탄젠트 알파 더하기 베타는 일 빼기 육분의 일 분에 이분의 일 더하기 삼분의 일입니다.", cap: "$\\tan(\\alpha+\\beta)=\\dfrac{1/2+1/3}{1-(1/2)(1/3)}=\\dfrac{5/6}{5/6}=1$" },
      { say: "분모와 분자가 모두 육분의 오로 같아 일이 되므로, 알파 더하기 베타는 사분의 파이입니다.", cap: "$\\tan(\\alpha+\\beta)=1\\ \\Rightarrow\\ \\alpha+\\beta=\\dfrac{\\pi}{4}$" }
    ],
    examChips: [
      "\\tan\\alpha=\\dfrac{1}{2},\\qquad \\tan\\beta=\\dfrac{1}{3}",
      "\\tan(\\alpha+\\beta)=\\dfrac{\\frac{1}{2}+\\frac{1}{3}}{1-\\frac{1}{2}\\cdot\\frac{1}{3}}=\\dfrac{\\frac{5}{6}}{\\frac{5}{6}}=1",
      "\\therefore\\ \\alpha+\\beta=\\dfrac{\\pi}{4}"
    ],
    examLabels: ["tan(1/2) + tan(1/3) → 1", "정답 π/4"],
    examGraph: {
      f: x => 0.45 * x + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.8, col: CY, label: "tan α = 1/2" }, r2: { x: 2.2, col: GO, label: "tan β = 1/3 → 합 π/4" },
      fn: { t: "황금 비율 암기: tan α = 1/2, tan β = 1/3  ⇔  α + β = 45° (π/4)!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(5/6) / (5/6)", finalS: "π / 4", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 탄젠트 값이 이분의 일과 삼분의 일인 두 각의 합이 사십오도라는 것과 일과 이, 삼인 세 각의 합이 백팔십도라는 것은 외워두면 도형 문제가 삼 초 만에 풀립니다.", cap: "① 필수 암기 쌍: $\\tan\\alpha=\\dfrac{1}{2},\\ \\tan\\beta=\\dfrac{1}{3}\\ \\Longrightarrow\\ \\alpha+\\beta=\\dfrac{\\pi}{4}$!" },
      { say: "둘째, 코사인 배각공식을 거꾸로 정리한 반각공식 사인 제곱은 이분의 일 빼기 코사인 이 알파는 삼각함수 적분에서 차수를 낮출 때 필수로 쓰입니다.", cap: "② 적분 필수 반각 변형: $\\sin^{2}x=\\dfrac{1-\\cos 2x}{2},\\quad \\cos^{2}x=\\dfrac{1+\\cos 2x}{2}$" },
      { say: "셋째, 단위원 삼각함수 정의를 다루는 제십육강과 코사인법칙 제삼십강을 함께 보면 삼각함수 공식 체계가 완성됩니다.", cap: "③ 제16·30강 연계: 단위원 대칭성 + 코사인법칙 + 덧셈정리!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 삼각함수의 극한과 수능 도형 극한을 근사식으로 삼 초 만에 푸는 제팔십강입니다.", cap: "제80강 · 삼각함수 극한 $\\dfrac{\\sin x}{x}=1$ 과 도형 극한 3초 근사" },
      { tag: "연계 ②", say: "단위원 삼각함수를 다루는 제십육강도 함께 보세요.", cap: "제16강 · 단위원 삼각함수 정복 (수학 I)" },
      { tag: "이 사이트", say: "이 사이트의 제팔십강과 제십육강을 이어서 보세요.", cap: "제80강 · 삼각함수 도형 극한  /  제16강 · 단위원 삼각함수" }
    ],
    nextLinks: [
      { lec: 80, label: "제80강 열기 (삼각함수 도형극한)" },
      { lec: 16, label: "제16강 열기 (단위원 삼각함수)" },
      { lec: 78, label: "제78강 열기 (자연상수 e 극한)" }
    ]
  },
  {
    lec: 80,
    title: "숏츠식 판서 미리보기 · 삼각함수 극한 sin x/x 와 도형 극한 3초 근사",
    desc: "$\\lim_{x\\to 0}\\frac{\\sin x}{x}=1,\\ \\lim_{x\\to 0}\\frac{\\tan x}{x}=1$ 과 $\\lim_{x\\to 0}\\frac{1-\\cos x}{x^{2}}=\\frac{1}{2}$ 을 이용한 도형 극한 초고속 근사법을 정리합니다.",
    hookTitle: "삼각함수 도형 극한 · 3초 근사 공식", hookSub: "sin θ ≈ θ · tan θ ≈ θ · 1 − cos θ ≈ ½ θ²!",
    hookSay: "수능 미적분 28·29번 단골인 삼각함수 도형 극한에서 복잡한 식 정리 없이 세타의 다항식으로 바로 바꾸는 근사법, 30초 만에 정리합니다.",
    hookCap: "삼각함수 극한과 도형 근사 · 30초 정리",
    whySay: "단위원 부채꼴에서 내접 삼각형 넓이보다 부채꼴 넓이가 크고 외접 직각삼각형 넓이보다 작다는 부등식에 조임정리를 쓰면 사인 엑스 나누기 엑스가 일로 수렴합니다.",
    whyCap: "$\\sin x\\lt x\\lt\\tan x\\ (0\\lt x\\lt\\frac{\\pi}{2})\\ \\Longrightarrow\\ \\lim_{x\\to 0}\\dfrac{\\sin x}{x}=1$",
    histTag: "아르키메데스·코시", histSay: "원둘레를 내접·외접 다각형으로 조여 극한을 구한 아르키메데스의 착출법이 사인 극한 증명의 직접적 원형입니다.",
    histCap: "부채꼴 넓이 샌드위치 증명과 2차 근사 $1-\\cos x=2\\sin^{2}\\frac{x}{2}\\approx\\dfrac{1}{2}x^{2}$",
    fParts: [
      { say: "라디안 각도 엑스가 영으로 갈 때 사인 에이 엑스와 탄젠트 에이 엑스는 모두 일차식 에이 엑스로 똑같이 근사됩니다.", cap: "1차 근사($x\\to 0$): $\\sin(ax)\\approx ax,\\qquad \\tan(ax)\\approx ax$" },
      { say: "일 빼기 코사인 엑스는 분자·분모에 일 더하기 코사인을 곱하면 이분의 일 엑스 제곱으로 수렴하는 이차식입니다.", cap: "2차 근사($x\\to 0$): $\\lim_{x\\to 0}\\dfrac{1-\\cos x}{x^{2}}=\\dfrac{1}{2}\\ \\Longleftrightarrow\\ 1-\\cos x\\approx\\dfrac{1}{2}x^{2}$!" },
      { say: "도형 극한에서 넓이 에스 세타를 구할 때도 처음부터 세타가 영 근처라고 생각하고 변의 길이를 세타의 몇 제곱인지 차수만 세면 계산이 끝납니다.", cap: "도형 극한 실전 팁: 각 변의 길이를 $k\\cdot\\theta^{n}$ 단항식으로 근사 후 대입!" }
    ],
    fChips: [
      "\\lim_{x\\to 0}\\dfrac{\\sin(ax)}{bx}=\\dfrac{a}{b},\\qquad \\lim_{x\\to 0}\\dfrac{\\tan(ax)}{bx}=\\dfrac{a}{b}",
      "\\lim_{x\\to 0}\\dfrac{1-\\cos x}{x^{2}}=\\dfrac{1}{2},\\qquad \\lim_{x\\to 0}\\dfrac{1-\\cos(ax)}{x^{2}}=\\dfrac{a^{2}}{2}",
      "\\theta\\to 0\\text{ 도형 근사: }\\sin\\theta\\approx\\theta,\\quad \\tan\\theta\\approx\\theta,\\quad 1-\\cos\\theta\\approx\\dfrac{1}{2}\\theta^{2}"
    ],
    fLabels: ["sin x ≈ tan x ≈ x (1차)", "1 − cos x ≈ ½ x² (2차!)"],
    exParts: [
      { say: "예를 들어 리미트 엑스가 영으로 갈 때 엑스 제곱 분의 일 빼기 코사인 사 엑스의 값을 구해 봅시다.", cap: "$\\lim_{x\\to 0}\\dfrac{1-\\cos 4x}{x^{2}}$ 의 값 구하기" },
      { say: "일 빼기 코사인 사 엑스는 이분의 일 곱하기 사 엑스 전체의 제곱인 팔 엑스 제곱으로 근사됩니다.", cap: "$1-\\cos 4x\\approx\\dfrac{1}{2}(4x)^{2}=8x^{2}$" },
      { say: "따라서 엑스 제곱으로 나누면 극한값은 팔입니다.", cap: "$\\dfrac{8x^{2}}{x^{2}}=8$" }
    ],
    exChips: [
      "\\lim_{x\\to 0}\\dfrac{1-\\cos 4x}{x^{2}}",
      "1-\\cos(4x)\\approx\\dfrac{1}{2}(4x)^{2}=8x^{2}",
      "\\therefore\\ \\lim_{x\\to 0}\\dfrac{8x^{2}}{x^{2}}=8"
    ],
    exLabels: ["½ × (4x)² = 8x²", "극한값 = 8"],
    exGraph: {
      f: x => (x === 1.5 ? 1.5 : 1.5 * Math.sin(2.2 * (x - 1.5)) / (2.2 * (x - 1.5))) + 0.15, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.5, col: CY, label: "x → 0 에서 sin x / x → 1" }, r2: { x: 2.3, col: PK, label: "1−cos x ≈ ½x²" },
      fn: { t: "1차: sin x ≈ tan x ≈ x   /   2차: 1 − cos x ≈ ½ x²", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "½ × 4²", finalS: "극한값 = 8", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 반지름의 길이가 일이고 중심각의 크기가 세타인 부채꼴에서 호의 양 끝점과 반지름에 내린 수선의 발이 만드는 직각삼각형 넓이를 에스 세타라 할 때, 세타 세제곱 분의 에스 세타의 극한값은 얼마일까요?", cap: "반지름 $1$, 중심각 $\\theta$ 부채꼴에서 밑변 $1-\\cos\\theta$, 높이 $\\sin\\theta$ 인 삼각형 넓이 $S(\\theta)$ 의 $\\lim_{\\theta\\to 0+}\\dfrac{S(\\theta)}{\\theta^{3}}$ (자작 문항)" },
      { say: "삼각형의 밑변 일 빼기 코사인 세타는 이분의 일 세타 제곱이고, 높이 사인 세타는 세타입니다.", cap: "밑변 $1-\\cos\\theta\\approx\\dfrac{1}{2}\\theta^{2}$, 높이 $\\sin\\theta\\approx\\theta$" },
      { say: "넓이 에스 세타는 이분의 일 곱하기 이분의 일 세타 제곱 곱하기 세타인 사분의 일 세타 세제곱이므로, 정답은 사분의 일입니다.", cap: "$S(\\theta)\\approx\\dfrac{1}{2}\\cdot\\left(\\dfrac{1}{2}\\theta^{2}\\right)\\cdot\\theta=\\dfrac{1}{4}\\theta^{3}\\ \\Rightarrow\\ \\dfrac{1}{4}$" }
    ],
    examChips: [
      "S(\\theta)=\\dfrac{1}{2}(1-\\cos\\theta)\\sin\\theta",
      "\\theta\\to 0+\\text{ 근사: }S(\\theta)\\approx\\dfrac{1}{2}\\left(\\dfrac{1}{2}\\theta^{2}\\right)\\theta=\\dfrac{1}{4}\\theta^{3}",
      "\\lim_{\\theta\\to 0+}\\dfrac{S(\\theta)}{\\theta^{3}}=\\dfrac{1}{4}"
    ],
    examLabels: ["½ × (½θ²) × θ = ¼θ³", "정답 1/4"],
    examGraph: {
      f: x => 0.45 * (x - 0.3) * (x - 0.3) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "밑변 1−cos θ ≈ ½θ²" }, r2: { x: 2.3, col: GO, label: "높이 sin θ ≈ θ → 1/4" },
      fn: { t: "분모가 θ³ 이면 넓이는 (2차 변 ½θ²) × (1차 변 θ) 구조!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "½ × ½", finalS: "1 / 4", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 문제의 분모가 세타 세제곱이면 구하는 넓이의 두 변이 일차와 이차의 곱이라는 힌트이므로 차수 검산이 즉시 가능합니다.", cap: "① 분모 차수 힌트 법칙: 분모가 $\\theta^{3}$ 이면 $S(\\theta)$ 는 무조건 $k\\theta^{3}$ (차수 검산!)" },
      { say: "둘째, 탄젠트 엑스 빼기 사인 엑스처럼 일차항끼리 서로 지워지는 뺄셈에서는 테일러 삼차항에 의해 이분의 일 엑스 세제곱이 됩니다.", cap: "② 1차 소거 뺄셈 공식: $\\tan x-\\sin x=\\tan x(1-\\cos x)\\approx\\dfrac{1}{2}x^{3}$!" },
      { say: "셋째, 도형 문제 최상위권의 시선을 다루는 제이십사강과 삼각함수 비율관계 제이십일강을 함께 보면 도형 극한이 완벽히 정복됩니다.", cap: "③ 제21·24강 연계: 원주각·접선·이등변삼각형 보조선 + $\\theta$ 근사!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 몫의 미분법, 합성함수 연쇄법칙과 음함수·매개변수 미분법을 다루는 제팔십일강입니다.", cap: "제81강 · 몫·합성함수 연쇄법칙과 음함수·매개변수 미분" },
      { tag: "연계 ②", say: "수능 도형 보조선의 시선을 다루는 제이십사강도 함께 보세요.", cap: "제24강 · 도형 문제 최상위권의 시선 (수학 I)" },
      { tag: "이 사이트", say: "이 사이트의 제팔십일강과 제이십사강을 이어서 보세요.", cap: "제81강 · 여러 가지 미분법  /  제24강 · 도형 최상위권 시선" }
    ],
    nextLinks: [
      { lec: 81, label: "제81강 열기 (몫·합성·매개변수 미분)" },
      { lec: 24, label: "제24강 열기 (도형 최상위권 시선)" },
      { lec: 79, label: "제79강 열기 (삼각함수 덧셈정리)" }
    ]
  },
  {
    lec: 81,
    title: "숏츠식 판서 미리보기 · 몫의 미분법·합성함수 연쇄법칙과 매개변수 미분",
    desc: "몫의 미분법 $\\left(\\frac{f}{g}\\right)'=\\frac{f'g-fg'}{g^{2}}$, 합성함수 연쇄법칙 $(f(g(x)))'=f'(g(x))g'(x)$ 와 음함수·매개변수 미분법을 정리합니다.",
    hookTitle: "몫·합성 미분 & 매개변수 미분 3초 공식", hookSub: "겉미분 × 속미분 · 분모 제곱 분에 미그마그미!",
    hookSay: "초월함수 미분의 엔진인 몫의 미분법과 합성함수 속미분, 매개변수 미분 공식을 30초 만에 정리합니다.",
    hookCap: "여러 가지 미분법 총정리 · 30초 정리",
    whySay: "합성함수의 순간변화율은 안쪽 함수의 변화율과 바깥쪽 함수의 변화율이 연쇄적으로 곱해지는 라이프니츠 분수 약분 구조를 가집니다.",
    whyCap: "연쇄법칙(Chain Rule): $\\dfrac{dy}{dx}=\\dfrac{dy}{du}\\cdot\\dfrac{du}{dx}=f'\\bigl(g(x)\\bigr)\\cdot g'(x)$",
    histTag: "라이프니츠", histSay: "분수 형태의 미분 기호 dy/dx와 연쇄법칙, 몫의 미분법 공식은 라이프니츠가 1684년 논문에서 체계화했습니다.",
    histCap: "라이프니츠 미분 기호 $\\dfrac{dy}{dx}$ 와 매개변수 미분 $\\dfrac{dy/dt}{dx/dt}$",
    fParts: [
      { say: "분수함수를 미분하는 몫의 미분법은 분모를 제곱한 뒤, 분자는 분자 미분 곱하기 분모 빼기 분자 그대로 곱하기 분모 미분입니다.", cap: "몫의 미분법: $\\left(\\dfrac{f}{g}\\right)'=\\dfrac{f'g-fg'}{g^{2}}$ (분자가 상수 $1$ 이면 $-\\dfrac{g'}{g^{2}}$!)" },
      { say: "합성함수 에프 쥐 엑스의 미분은 겉함수를 미분한 에프 프라임 쥐 엑스에 속함수 미분 쥐 프라임 엑스를 반드시 곱합니다.", cap: "합성함수 미분: $\\bigl(f(g(x))\\bigr)'=f'\\bigl(g(x)\\bigr)\\cdot g'(x),\\quad \\bigl(\\ln|f(x)|\\bigr)'=\\dfrac{f'(x)}{f(x)}$" },
      { say: "매개변수 티로 나타낸 함수의 기울기 디와이 디엑스는 와이를 티로 미분한 값을 엑스를 티로 미분한 값으로 나누어 구합니다.", cap: "매개변수 미분: $\\dfrac{dy}{dx}=\\dfrac{dy/dt}{dx/dt}$ · 음함수 미분: $y^{n}$ 미분 시 $ny^{n-1}\\dfrac{dy}{dx}$!" }
    ],
    fChips: [
      "\\left(\\dfrac{f}{g}\\right)'=\\dfrac{f'g-fg'}{g^{2}},\\qquad \\left(\\dfrac{1}{g}\\right)'=-\\dfrac{g'}{g^{2}}",
      "\\bigl(f(g(x))\\bigr)'=f'\\bigl(g(x)\\bigr)\\cdot g'(x),\\qquad \\bigl(\\ln|f(x)|\\bigr)'=\\dfrac{f'(x)}{f(x)}",
      "\\text{매개변수: }\\dfrac{dy}{dx}=\\dfrac{dy/dt}{dx/dt},\\qquad \\text{음함수: }\\dfrac{d}{dx}\\bigl(y^{2}\\bigr)=2y\\dfrac{dy}{dx}"
    ],
    fLabels: ["분모² 분의 (미그 − 그미)", "겉미분 × 속미분 & 매개변수"],
    exParts: [
      { say: "예를 들어 매개변수 티로 나타낸 곡선 엑스는 티 제곱 더하기 티, 와이는 티 세제곱 빼기 일에서 티는 일일 때의 접선의 기울기를 구해 봅시다.", cap: "$x=t^{2}+t,\\ y=t^{3}-1$ 에서 $t=1$ 일 때 $\\dfrac{dy}{dx}$" },
      { say: "티로 각각 미분하면 디엑스 디티는 이 티 더하기 일, 디와이 디티는 삼 티 제곱입니다.", cap: "$\\dfrac{dx}{dt}=2t+1,\\qquad \\dfrac{dy}{dt}=3t^{2}$" },
      { say: "티에 일을 대입해 나누면 삼 분의 삼이므로 접선의 기울기는 일입니다.", cap: "$\\left.\\dfrac{dy}{dx}\\right|_{t=1}=\\dfrac{3(1)^{2}}{2(1)+1}=\\dfrac{3}{3}=1$" }
    ],
    exChips: [
      "\\dfrac{dx}{dt}=2t+1,\\qquad \\dfrac{dy}{dt}=3t^{2}",
      "\\dfrac{dy}{dx}=\\dfrac{3t^{2}}{2t+1}",
      "t=1\\text{ 대입}\\ \\Longrightarrow\\ \\dfrac{dy}{dx}=\\dfrac{3}{3}=1"
    ],
    exLabels: ["(dy/dt) / (dx/dt)", "기울기 = 1"],
    exGraph: {
      f: x => 0.45 * (x - 0.6) * (x - 0.6) + 0.4, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.4, col: CY, label: "t = 1 대응점 (2, 0)" }, r2: { x: 2.3, col: PK, label: "dy/dx = (dy/dt)/(dx/dt)" },
      fn: { t: "합성 미분: 겉미분 × 속미분  /  매개변수 미분: (dy/dt) ÷ (dx/dt)", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "3t² / (2t + 1)", finalS: "dy/dx = 1", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 함수 에프 엑스는 엘엔 엑스 제곱 더하기 삼에 대하여 에프 프라임 일의 값은 얼마일까요?", cap: "$f(x)=\\ln(x^{2}+3)$ 일 때 $f'(1)$ 의 값 (자작 문항)" },
      { say: "합성함수 로그 미분 공식에 의해 에프 프라임 엑스는 진수 그대로 분의 진수 속미분, 즉 엑스 제곱 더하기 삼 분의 이 엑스입니다.", cap: "$f'(x)=\\dfrac{(x^{2}+3)'}{x^{2}+3}=\\dfrac{2x}{x^{2}+3}$" },
      { say: "엑스에 일을 대입하면 사 분의 이, 이분의 일입니다.", cap: "$f'(1)=\\dfrac{2}{1+3}=\\dfrac{1}{2}$" }
    ],
    examChips: [
      "f(x)=\\ln(x^{2}+3)\\ \\Longrightarrow\\ \\bigl(\\ln g(x)\\bigr)'=\\dfrac{g'(x)}{g(x)}",
      "f'(x)=\\dfrac{2x}{x^{2}+3}",
      "f'(1)=\\dfrac{2}{4}=\\dfrac{1}{2}"
    ],
    examLabels: ["진수 분의 진수미분", "정답 1/2"],
    examGraph: {
      f: x => 0.7 * Math.log(x * x + 1.5) + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.0, col: CY, label: "x = 1" }, r2: { x: 2.2, col: GO, label: "f'(1) = 2/4 = 1/2" },
      fn: { t: "(ln f(x))' = f'(x) / f(x) · 적분할 때도 그대로 역연산!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "2x / (x² + 3)", finalS: "1 / 2", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 분자가 상수인 분수함수를 미분할 때는 일반 몫의 미분법 대신 마이너스 분모 제곱 분의 분모 속미분 공식을 쓰면 부호 실수가 없습니다.", cap: "① 상수 분자 꿀팁: $\\left(\\dfrac{k}{g(x)}\\right)'=-\\dfrac{k\\cdot g'(x)}{\\{g(x)\\}^{2}}$!" },
      { say: "둘째, 다항식 여러 개가 곱해지거나 거듭제곱된 복잡한 식을 미분할 때는 양변에 절댓값 자연로그를 씌우는 로그미분법이 가장 빠릅니다.", cap: "② 로그미분법: $\\ln|f(x)|$ 미분 $\\Longrightarrow\\ f'(x)=f(x)\\left(\\dfrac{g'}{g}+\\dfrac{h'}{h}\\right)$" },
      { say: "셋째, 진수 분의 진수미분 구조는 제팔십사강의 치환적분에서 가장 중요한 적분 공식으로 다시 등장합니다.", cap: "③ 제84강 적분 직결: $\\int\\dfrac{f'(x)}{f(x)}\\,dx=\\ln|f(x)|+C$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 역함수의 미분법과 이계도함수·변곡점을 다루는 제팔십이강입니다.", cap: "제82강 · 역함수 미분법 $\\dfrac{1}{f'(a)}$ 과 이계도함수·변곡점" },
      { tag: "연계 ②", say: "초월함수 그래프 개형을 총정리하는 제팔십삼강도 이어서 보세요.", cap: "제83강 · 수능 필수 초월함수 개형 마스터" },
      { tag: "이 사이트", say: "이 사이트의 제팔십이강과 제팔십삼강을 이어서 보세요.", cap: "제82강 · 역함수 미분과 변곡점  /  제83강 · 초월함수 개형" }
    ],
    nextLinks: [
      { lec: 82, label: "제82강 열기 (역함수 미분·변곡점)" },
      { lec: 83, label: "제83강 열기 (초월함수 4대 개형)" },
      { lec: 80, label: "제80강 열기 (삼각함수 도형극한)" }
    ]
  }
];

const CALC_SPECS_B = [
  {
    lec: 82,
    title: "숏츠식 판서 미리보기 · 역함수 미분법 1/f'(a)과 이계도함수·변곡점",
    desc: "역함수 미분법 $(f^{-1})'(b)=\\frac{1}{f'(a)}$ ($f(a)=b$ 대응점)과 이계도함수 $f''(x)=0$ 의 부호 변화에 따른 변곡점 판정법을 정리합니다.",
    hookTitle: "역함수 미분 1/f'(a) & 변곡점 조건", hookSub: "f(a) = b 짝꿍 먼저 찾고 기울기 역수 · 변곡점은 f'' 부호 변화!",
    hookSay: "역함수 미분에서 대입할 숫자를 헷갈리지 않는 법과 변곡점의 정확한 판정 조건, 30초 만에 정리합니다.",
    hookCap: "역함수 미분법과 변곡점 · 30초 정리",
    whySay: "역함수는 직선 와이는 엑스에 대하여 대칭이므로 엑스와 와이 변화량이 서로 뒤집혀, 점 에이 콤마 비에서의 접선 기울기와 대칭점 비 콤마 에이에서의 접선 기울기는 정확히 역수 관계가 됩니다.",
    whyCap: "$f(a)=b\\ \\Longleftrightarrow\\ f^{-1}(b)=a\\ \\Longrightarrow\\ (f^{-1})'(b)=\\dfrac{1}{f'(a)}$",
    histTag: "오일러·코시", histSay: "역함수의 도함수 정리와 곡선의 오목·볼록을 이계도함수로 판별하는 이론은 오일러와 코시의 미분학에서 확립되었습니다.",
    histCap: "와이는 엑스 대칭 접선 기울기 역수($m\\cdot m'=1$)와 변곡점($f''$ 부호 변화)",
    fParts: [
      { say: "역함수의 미분계수 쥐 프라임 비를 구할 때는 절대 비를 미분식에 바로 넣지 말고, 에프 에이는 비가 되는 짝꿍 엑스좌표 에이부터 찾습니다.", cap: "1단계(대응점 찾기): $g(b)=a\\ \\Longleftrightarrow\\ f(a)=b$ 를 만족하는 $a$ 먼저 구하기!" },
      { say: "짝꿍 에이를 찾았으면 원래 함수를 미분한 에프 프라임 에이의 역수 에프 프라임 에이 분의 일이 바로 쥐 프라임 비입니다.", cap: "2단계(기울기 역수): $g'(b)=\\dfrac{1}{f'(a)}$" },
      { say: "곡선의 오목과 볼록이 바뀌는 변곡점은 이계도함수 에프 더블프라임이 영이면서 좌우에서 부호가 바뀌는 점입니다.", cap: "변곡점 판정: $f''(a)=0$ 이고 $x=a$ 좌우에서 $f''(x)$ 부호 반전 (짝수 중근 제외!)" }
    ],
    fChips: [
      "g=f^{-1},\\quad f(a)=b\\ \\Longrightarrow\\ g'(b)=\\dfrac{1}{f'(a)}\\quad (f'(a)\\neq 0)",
      "f''(x)\\gt 0\\implies \\text{아래로 볼록},\\qquad f''(x)\\lt 0\\implies \\text{위로 볼록}",
      "\\text{변곡점}\\ \\Longleftrightarrow\\ f''(x)=0\\text{ 이고 좌우에서 }f''(x)\\text{ 의 부호가 바뀜!}"
    ],
    fLabels: ["f(a)=b 대응점 → 1/f'(a)", "f''(x) 부호 반전 = 변곡점"],
    exParts: [
      { say: "예를 들어 에프 엑스는 엑스 세제곱 더하기 이 엑스 더하기 일의 역함수를 쥐 엑스라 할 때 쥐 프라임 사의 값을 구해 봅시다.", cap: "$f(x)=x^{3}+2x+1$ 의 역함수 $g(x)$ 에 대해 $g'(4)$ 구하기" },
      { say: "먼저 에프 에이는 사가 되는 에이를 찾으면 일 더하기 이 더하기 일이 사이므로 에이는 일입니다.", cap: "$f(a)=a^{3}+2a+1=4\\ \\Rightarrow\\ a=1$ (대응점 $(1,4)$ 확보!)" },
      { say: "에프 프라임 엑스는 삼 엑스 제곱 더하기 이이므로 에프 프라임 일은 오이고, 역수를 취한 오분의 일이 정답입니다.", cap: "$f'(x)=3x^{2}+2\\Rightarrow f'(1)=5\\ \\Rightarrow\\ g'(4)=\\dfrac{1}{f'(1)}=\\dfrac{1}{5}$" }
    ],
    exChips: [
      "f(a)=a^{3}+2a+1=4\\ \\Longrightarrow\\ a=1\\quad (\\text{즉 }g(4)=1)",
      "f'(x)=3x^{2}+2\\ \\Longrightarrow\\ f'(1)=5",
      "g'(4)=\\dfrac{1}{f'(1)}=\\dfrac{1}{5}"
    ],
    exLabels: ["f(1) = 4 짝꿍 찾기", "g'(4) = 1/5"],
    exGraph: {
      f: x => 0.35 * Math.pow(x - 1.5, 3) + 0.5 * (x - 1.5) + 1.1, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.6], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.5, col: CY, label: "변곡점 f''(x) = 0" }, r2: { x: 2.3, col: PK, label: "g'(b) = 1 / f'(a)" },
      fn: { t: "역함수 미분: ① f(a) = b 인 a 찾기 → ② 1 / f'(a) 역수!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "f(1)=4, f'(1)=5", finalS: "g'(4) = 1/5", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 곡선 와이는 엑스 곱하기 이에 엑스 제곱의 변곡점의 엑스좌표는 얼마일까요?", cap: "곡선 $y=xe^{x}$ 의 변곡점의 $x$좌표 구하기 (자작 문항)" },
      { say: "한 번 미분하면 엑스 더하기 일 곱하기 이에 엑스 제곱이고, 한 번 더 미분하면 엑스 더하기 이 곱하기 이에 엑스 제곱입니다.", cap: "$y'=(x+1)e^{x},\\qquad y''=(x+2)e^{x}$" },
      { say: "이의 엑스 제곱은 항상 양수이므로 엑스는 마이너스 이에서 이계도함수가 영이고 부호가 바뀌어 변곡점의 엑스좌표는 마이너스 이입니다.", cap: "$y''=0\\ \\Rightarrow\\ x=-2$ (부호 변화 확인 $\\Rightarrow$ 정답 $-2$)" }
    ],
    examChips: [
      "y=xe^{x}\\ \\Longrightarrow\\ y'=(x+1)e^{x}",
      "y''=(x+2)e^{x}=0",
      "x=-2\\text{ 좌우에서 부호 반전}\\ \\Longrightarrow\\ \\text{변곡점 }x=-2"
    ],
    examLabels: ["y'' = (x+2)e^x = 0", "정답 x = −2"],
    examGraph: {
      f: x => 0.55 * (x - 1.0) * Math.exp(0.6 * (x - 1.0)) + 0.85, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.7, col: CY, label: "변곡점 x = −2" }, r2: { x: 1.4, col: GO, label: "극소 x = −1" },
      fn: { t: "(ax + b)e^x 미분 공식: 미분할 때마다 상수항에 a 씩만 더한다!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(x + 2)e^x = 0", finalS: "x = −2", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 다항식 피 엑스 곱하기 이에 엑스 제곱을 미분하면 피 엑스 더하기 피 프라임 엑스 전체에 이에 엑스 제곱을 곱한 것과 같아 암산으로 미분됩니다.", cap: "① 초고속 미분 공식: $\\bigl(P(x)e^{x}\\bigr)'=\\bigl(P(x)+P'(x)\\bigr)e^{x}$!" },
      { say: "둘째, 변곡점에서의 접선은 곡선을 뚫고 지나가는 뚫접이므로 접선 개수가 바뀌는 경계선이 됩니다.", cap: "② 제3강 연결: 변곡접선은 곡선을 뚫고 지나가며 외부 점 접선 개수의 경계!" },
      { say: "셋째, 극값의 정확한 정의를 다루는 제십사강과 변곡접선 제삼강을 함께 보면 미분 판정 개념이 완벽해집니다.", cap: "③ 제3·14강 연계: 극값($f'$ 부호 변화) vs 변곡점($f''$ 부호 변화)!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 미적분 킬러 문제를 지배하는 4대 초월함수 그래프 개형을 외우는 제팔십삼강입니다.", cap: "제83강 · 수능 필수 초월함수 개형 마스터 ($xe^{-x},\\ \\ln x/x$)" },
      { tag: "연계 ②", say: "변곡접선의 성질을 다루는 수학 투 제삼강도 함께 보세요.", cap: "제3강 · 변곡접선 정리하기 (수학 II)" },
      { tag: "이 사이트", say: "이 사이트의 제팔십삼강과 제삼강을 이어서 보세요.", cap: "제83강 · 초월함수 개형 마스터  /  제3강 · 변곡접선 정리" }
    ],
    nextLinks: [
      { lec: 83, label: "제83강 열기 (초월함수 4대 개형)" },
      { lec: 3, label: "제3강 열기 (변곡접선 정리)" },
      { lec: 81, label: "제81강 열기 (몫·합성·매개변수)" }
    ]
  },
  {
    lec: 83,
    title: "숏츠식 판서 미리보기 · 수능 필수 초월함수 개형 (xe^{-x}, ln x/x)",
    desc: "수능 미적분에 반복 출제되는 $y=xe^{x},\\ y=xe^{-x},\\ y=x\\ln x,\\ y=\\frac{\\ln x}{x}$ 의 극값($\\pm\\frac{1}{e}$)과 점근선·변곡점을 정리합니다.",
    hookTitle: "초월함수 4대 개형 · 1/e 의 법칙", hookSub: "xe^{-x} 와 (ln x)/x 모두 최댓값 = 1/e · 점근선 y = 0!",
    hookSay: "미분하지 않고도 1초 만에 그리는 수능 필수 초월함수 4대 개형과 자연상수 이분의 일 극값 법칙, 바로 정리합니다.",
    hookCap: "수능 필수 초월함수 4대 개형 · 30초 정리",
    whySay: "지수함수와 다항식, 로그함수와 다항식이 곱해지거나 나누어지면 무한대에서 지수함수가 가장 빠르게 커지고 로그함수가 가장 느리게 커지므로 한쪽 끝에서 엑스축에 달라붙는 점근선이 생깁니다.",
    whyCap: "무한대 속도 서열: $\\ln x \\ll x^{n} \\ll e^{x}\\ \\Longrightarrow\\ \\lim_{x\\to\\infty}\\dfrac{x}{e^{x}}=0,\\ \\lim_{x\\to\\infty}\\dfrac{\\ln x}{x}=0$",
    histTag: "오일러와 성장 속도", histSay: "초월함수의 극값 1/e와 성장 속도 비교는 오일러가 발견한 지수 문제(a^b = b^a)의 해법에서 유래했습니다.",
    histCap: "$y=\\dfrac{\\ln x}{x}$ 의 최댓값 $f(e)=\\dfrac{1}{e}$ 와 $a^{b}=b^{a}$ 대소 비교",
    fParts: [
      { say: "와이는 엑스 곱하기 이에 마이너스 엑스 제곱은 원점을 지나고 엑스는 일에서 최댓값 이분의 일을 찍은 뒤 오른쪽 점근선 영으로 내려갑니다.", cap: "① $y=xe^{-x}$: $x=1$ 에서 극대 $\\dfrac{1}{e}$, 변곡점 $x=2$, 우측 점근선 $y=0$" },
      { say: "와이는 엑스 분의 엘엔 엑스는 일 콤마 영을 지나고 엑스는 이에서 최댓값 이분의 일을 찍은 뒤 오른쪽 점근선 영으로 내려갑니다.", cap: "② $y=\\dfrac{\\ln x}{x}$: $x=e$ 에서 극대 $\\dfrac{1}{e}$, 변곡점 $x=e^{3/2}$, 우측 점근선 $y=0$" },
      { say: "와이는 엑스 곱하기 엘엔 엑스는 엑스는 이분의 일에서 최솟값 마이너스 이분의 일을 가집니다.", cap: "③ $y=x\\ln x$: $x=\\dfrac{1}{e}$ 에서 극소 $-\\dfrac{1}{e}$ · ④ $y=xe^{x}$: $x=-1$ 에서 극소 $-\\dfrac{1}{e}$" }
    ],
    fChips: [
      "y=xe^{-x}:\\ x=1\\text{ 최대 }\\dfrac{1}{e},\\ \\text{변곡점 }x=2,\\ \\lim_{x\\to\\infty}y=0",
      "y=\\dfrac{\\ln x}{x}\\ :\\ x=e\\text{ 에서 최댓값 }\\dfrac{1}{e},\\quad \\text{변곡점 }x=e\\sqrt{e},\\quad \\lim_{x\\to\\infty}y=0",
      "y=x\\ln x:\\ x=\\dfrac{1}{e}\\text{ 최소 }-\\dfrac{1}{e},\\quad y=xe^{x}:\\ x=-1\\text{ 최소 }-\\dfrac{1}{e}"
    ],
    fLabels: ["xe^{-x}(x=1) · ln x/x(x=e) 최대 1/e", "x ln x · xe^x 최소 −1/e"],
    exParts: [
      { say: "예를 들어 방정식 엑스 곱하기 이에 마이너스 엑스 제곱은 케이가 서로 다른 두 실근을 갖도록 하는 실수 케이의 범위를 구해 봅시다.", cap: "$xe^{-x}=k$ 가 서로 다른 두 실근을 가질 $k$ 의 범위" },
      { say: "와이는 엑스 이에 마이너스 엑스 제곱은 엑스는 일에서 극댓값 이분의 일을 갖고 오른쪽으로 영에 수렴합니다.", cap: "극댓값 $f(1)=\\dfrac{1}{e}$, 우측 점근선 $y=0$" },
      { say: "따라서 수평선 와이는 케이가 영보다 크고 이분의 일보다 작을 때 두 점에서 만납니다.", cap: "$0\\lt k\\lt\\dfrac{1}{e}$" }
    ],
    exChips: [
      "f(x)=xe^{-x}\\ \\Longrightarrow\\ f'(x)=(1-x)e^{-x}=0\\quad (x=1)",
      "\\text{극댓값 }f(1)=\\dfrac{1}{e},\\qquad \\lim_{x\\to\\infty}xe^{-x}=0^{+}",
      "\\text{서로 다른 두 실근 조건: }0\\lt k\\lt\\dfrac{1}{e}"
    ],
    exLabels: ["극대 1/e, 점근선 y=0", "0 < k < 1/e"],
    exGraph: {
      f: x => 2.1 * x * Math.exp(-0.95 * x) + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.05, col: CY, label: "극대 x = 1 (높이 1/e)" }, r2: { x: 2.1, col: PK, label: "변곡점 x = 2 (점근선 0)" },
      fn: { t: "y = xe^{-x} : 원점 통과 → x=1 극대(1/e) → x=2 변곡점 → y=0 점근선!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "극댓값 = 1/e", finalS: "0 < k < 1/e", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 양수 엑스에서 정의된 함수 에프 엑스는 엑스 분의 엘엔 엑스의 최댓값과 그때의 엑스 값의 곱은 얼마일까요?", cap: "$x\\gt 0$ 에서 $f(x)=\\dfrac{\\ln x}{x}$ 의 최댓값 $M$ 과 그때의 $x=a$ 에 대해 $a\\times M$ (자작 문항)" },
      { say: "에프 엑스는 엑스는 이에서 최댓값 이분의 일을 가집니다.", cap: "$x=e$ 에서 최댓값 $M=f(e)=\\dfrac{1}{e}$" },
      { say: "따라서 에이는 이이고 최댓값은 이분의 일이므로 두 값의 곱은 일입니다.", cap: "$a\\times M=e\\times\\dfrac{1}{e}=1$" }
    ],
    examChips: [
      "f(x)=\\dfrac{\\ln x}{x}\\ \\Longrightarrow\\ f'(x)=\\dfrac{1-\\ln x}{x^{2}}=0",
      "x=e\\text{ 에서 최댓값 }M=f(e)=\\dfrac{1}{e}",
      "a\\times M=e\\times\\dfrac{1}{e}=1"
    ],
    examLabels: ["x = e 에서 최대 1/e", "정답 1"],
    examGraph: {
      f: x => 1.8 * Math.log(x + 0.6) / (x + 0.6) + 0.35, GY0: 390, GV: 110, xr: [0.2, 3], area: [0.4, 2.7], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 1.1, col: CY, label: "x = e (최대 1/e)" }, r2: { x: 2.4, col: GO, label: "e × (1/e) = 1" },
      fn: { t: "y = (ln x)/x 는 x = e 에서 최댓값 1/e ⇒ e^π > π^e 증명 완성!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "e × (1/e)", finalS: "1", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 엑스 이에 마이너스 엑스 제곱은 원점과 극대 일, 변곡점 이가 일씩 일정한 간격으로 떨어져 있어 비율관계처럼 외워두면 편리합니다.", cap: "① $y=xe^{-x}$ 등간격 법칙: 절편 $x=0$ $\\to$ 극대 $x=1$ $\\to$ 변곡점 $x=2$ (간격 $1$ 일정!)" },
      { say: "둘째, 이에 파이 제곱과 파이의 이 제곱의 대소 비교는 엑스 분의 엘엔 엑스가 엑스는 이에서 최대라는 성질로 일 초 만에 판별됩니다.", cap: "② $\\dfrac{\\ln e}{e}\\gt\\dfrac{\\ln\\pi}{\\pi}\\ \\Longleftrightarrow\\ \\pi\\ln e\\gt e\\ln\\pi\\ \\Longleftrightarrow\\ e^{\\pi}\\gt\\pi^{e}$!" },
      { say: "셋째, 고교 교과서 14개 그래프를 총정리한 제이십팔강과 함께 보면 초월함수 개형이 한눈에 체계화됩니다.", cap: "③ 제28강 연계: 대한민국 고교 교과서 14개 핵심 그래프 총정리!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 속미분 구조를 거꾸로 적분하는 치환적분법과 로그적분 제팔십사강입니다.", cap: "제84강 · 치환적분법과 속미분 분수 적분 $\\ln|f(x)|$" },
      { tag: "연계 ②", say: "교과서 14개 필수 그래프를 총정리한 제이십팔강도 함께 보세요.", cap: "제28강 · 대한민국 고교 교과서 14개 그래프 총정리" },
      { tag: "이 사이트", say: "이 사이트의 제팔십사강과 제이십팔강을 이어서 보세요.", cap: "제84강 · 치환적분법  /  제28강 · 14개 그래프 총정리" }
    ],
    nextLinks: [
      { lec: 84, label: "제84강 열기 (치환적분·로그적분)" },
      { lec: 28, label: "제28강 열기 (14개 그래프 총정리)" },
      { lec: 82, label: "제82강 열기 (역함수 미분·변곡점)" }
    ]
  },
  {
    lec: 84,
    title: "숏츠식 판서 미리보기 · 치환적분법과 속미분 분수 적분 ln|f(x)|",
    desc: "합성함수 미분의 역연산인 치환적분 $\\int f(g(x))g'(x)\\,dx=\\int f(t)\\,dt$ 와 분수 적분 $\\int\\frac{f'(x)}{f(x)}\\,dx=\\ln|f(x)|+C$ 를 정리합니다.",
    hookTitle: "치환적분 & 분수 적분 ln|f(x)|", hookSub: "곱해진 속미분 g'(x)dx = dt · 분모 미분이 분자면 ln|분모|!",
    hookSay: "복잡한 초월함수 적분을 한 줄로 끝내는 속미분 치환적분과 분수함수 로그 적분 공식, 30초 만에 정리합니다.",
    hookCap: "치환적분법과 로그적분 · 30초 정리",
    whySay: "합성함수 에프 쥐 엑스를 미분할 때 바깥에 곱해졌던 속미분 쥐 프라임 엑스가 적분 기호 안에서는 디엑스와 합쳐져 디티로 흡수되면서 단순한 기본 함수 적분으로 바뀝니다.",
    whyCap: "$g(x)=t\\ \\Longrightarrow\\ g'(x)\\,dx=dt\\ \\Longrightarrow\\ \\int f\\bigl(g(x)\\bigr)g'(x)\\,dx=\\int f(t)\\,dt$",
    histTag: "라이프니츠 표기법", histSay: "미분소 dx와 dt를 분수처럼 약분해 변수를 바꾸는 치환적분법은 라이프니츠 미적분 기호의 가장 강력한 장점입니다.",
    histCap: "미분소 변환 $g'(x)\\,dx=dt$ 와 로그 적분 $\\int\\dfrac{f'(x)}{f(x)}\\,dx=\\ln|f(x)|+C$",
    fParts: [
      { say: "식 안에 복잡한 덩어리 쥐 엑스가 있고 그 미분인 쥐 프라임 엑스가 곱해져 있으면 쥐 엑스를 티로 치환합니다.", cap: "치환적분 핵심: 속함수 $g(x)=t$ 로 두면 $g'(x)\\,dx=dt$ 로 한 번에 흡수!" },
      { say: "분수식을 적분할 때는 가장 먼저 분모를 미분한 식이 분자에 있는지 확인하고, 있으면 즉시 엘엔 절댓값 분모로 적분합니다.", cap: "분수 적분 1순위: $\\int\\dfrac{f'(x)}{f(x)}\\,dx=\\ln|f(x)|+C$ (탄젠트 적분도 $-\\ln|\\cos x|+C$!)" },
      { say: "정적분에서 치환적분을 할 때는 엑스의 아래끝과 위끝도 반드시 티의 범위로 함께 바꾸어야 다시 엑스로 되돌리는 수고를 덜 수 있습니다.", cap: "정적분 치환 철칙: $x=a\\to t=g(a),\\ x=b\\to t=g(b)$ 적분 구간 동시 변환!" }
    ],
    fChips: [
      "\\int f\\bigl(g(x)\\bigr)g'(x)\\,dx=\\int f(t)\\,dt\\quad (t=g(x),\\ dt=g'(x)\\,dx)",
      "\\int\\dfrac{f'(x)}{f(x)}\\,dx=\\ln|f(x)|+C,\\qquad \\int\\tan x\\,dx=-\\ln|\\cos x|+C",
      "\\int_{a}^{b}f\\bigl(g(x)\\bigr)g'(x)\\,dx=\\int_{g(a)}^{g(b)}f(t)\\,dt"
    ],
    fLabels: ["g'(x)dx = dt 흡수", "분모 분의 분모미분 = ln|분모|"],
    exParts: [
      { say: "예를 들어 인테그랄 영부터 일까지 엑스 제곱 더하기 일 분의 이 엑스 디엑스의 값을 구해 봅시다.", cap: "$\\int_{0}^{1}\\dfrac{2x}{x^{2}+1}\\,dx$ 의 값 구하기" },
      { say: "분모 엑스 제곱 더하기 일을 미분한 이 엑스가 분자에 그대로 있으므로 부정적분은 엘엔 엑스 제곱 더하기 일입니다.", cap: "$(x^{2}+1)'=2x\\ \\Rightarrow\\ \\Bigl[\\ln(x^{2}+1)\\Bigr]_{0}^{1}$" },
      { say: "위끝 일을 대입한 엘엔 이에서 영을 대입한 엘엔 일 즉 영을 빼면 엘엔 이입니다.", cap: "$\\ln 2-\\ln 1=\\ln 2$" }
    ],
    exChips: [
      "\\int_{0}^{1}\\dfrac{2x}{x^{2}+1}\\,dx=\\int_{0}^{1}\\dfrac{(x^{2}+1)'}{x^{2}+1}\\,dx",
      "=\\Bigl[\\ln(x^{2}+1)\\Bigr]_{0}^{1}",
      "=\\ln 2-\\ln 1=\\ln 2"
    ],
    exLabels: ["분모 미분 = 2x 확인", "정답 ln 2"],
    exGraph: {
      f: x => 1.5 * x / (x * x + 0.8) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.2], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "x = 0 → t = 1" }, r2: { x: 2.2, col: PK, label: "x = 1 → t = 2" },
      fn: { t: "분수 적분 제1원칙: 분모를 미분한 식이 분자에 있는지부터 본다!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "[ln(x² + 1)]", finalS: "ln 2", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 정적분 인테그랄 일부터 이까지 엑스 분의 엘엔 엑스 전체의 세제곱 디엑스의 값은 얼마일까요?", cap: "$\\int_{1}^{e}\\dfrac{(\\ln x)^{3}}{x}\\,dx$ 의 값 구하기 (자작 문항)" },
      { say: "엘엔 엑스를 티로 치환하면 엑스 분의 일 디엑스가 통째로 디티가 되고, 적분 구간은 영부터 일까지로 바뀝니다.", cap: "$\\ln x=t\\ \\Rightarrow\\ \\dfrac{1}{x}\\,dx=dt$, 구간 $[1,e]\\to[0,1]$" },
      { say: "인테그랄 영부터 일까지 티 세제곱 디티이므로 정답은 사분의 일입니다.", cap: "$\\int_{0}^{1}t^{3}\\,dt=\\left[\\dfrac{1}{4}t^{4}\\right]_{0}^{1}=\\dfrac{1}{4}$" }
    ],
    examChips: [
      "\\ln x=t\\text{ 치환}\\ \\Longrightarrow\\ \\dfrac{1}{x}\\,dx=dt,\\quad (x=1\\to t=0,\\ x=e\\to t=1)",
      "\\int_{1}^{e}\\dfrac{(\\ln x)^{3}}{x}\\,dx=\\int_{0}^{1}t^{3}\\,dt",
      "=\\left[\\dfrac{1}{4}t^{4}\\right]_{0}^{1}=\\dfrac{1}{4}"
    ],
    examLabels: ["ln x = t, dx/x = dt", "정답 1/4"],
    examGraph: {
      f: x => 0.45 * Math.pow(x - 0.4, 3) + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "t = 0 (x = 1)" }, r2: { x: 2.4, col: GO, label: "t = 1 (x = e) → 1/4" },
      fn: { t: "ln x 와 1/x 이 함께 보이면 100% ln x = t 치환적분!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "∫₀¹ t³ dt", finalS: "1 / 4", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 엘엔 엑스와 엑스분의 일이 함께 보이면 백 퍼센트 엘엔 엑스를 티로 치환하는 문제입니다.", cap: "① 조건반사 공식: $\\ln x$ 와 $\\dfrac{1}{x}\\,dx$ 가 함께 있으면 $\\ln x=t$ 치환!" },
      { say: "둘째, 사인과 코사인이 곱해진 적분에서는 홀수 거듭제곱인 쪽 하나를 디엑스 옆으로 빼고 나머지 반대쪽 삼각함수를 티로 치환합니다.", cap: "② 삼각함수 곱 적분: $\\sin x\\,dx=-d(\\cos x)$ 또는 $\\cos x\\,dx=d(\\sin x)$ 치환!" },
      { say: "셋째, 속미분 짝꿍이 곱해져 있지 않은 서로 다른 종류의 두 함수 곱은 다음 강의인 부분적분법으로 풉니다.", cap: "③ 치환적분 vs 부분적분: 속미분 짝꿍 있음 $\\to$ 치환 / 짝꿍 없음 $\\to$ 부분적분!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 서로 다른 두 함수의 곱을 적분하는 부분적분법과 도표적분 제팔십오강입니다.", cap: "제85강 · 부분적분법(로다삼지)과 3초 도표적분(DI법)" },
      { tag: "연계 ②", say: "합성함수 미분과 로그 미분을 다루는 제팔십일강도 함께 복습해 보세요.", cap: "제81강 · 몫·합성함수 연쇄법칙과 매개변수 미분" },
      { tag: "이 사이트", say: "이 사이트의 제팔십오강과 제팔십일강을 이어서 보세요.", cap: "제85강 · 부분적분과 도표적분  /  제81강 · 합성함수 미분" }
    ],
    nextLinks: [
      { lec: 85, label: "제85강 열기 (부분적분·도표적분)" },
      { lec: 81, label: "제81강 열기 (몫·합성함수 미분)" },
      { lec: 86, label: "제86강 열기 (정적분과 급수 변환)" }
    ]
  },
  {
    lec: 85,
    title: "숏츠식 판서 미리보기 · 부분적분법(로다삼지)과 3초 도표적분(DI법)",
    desc: "곱의 미분법 역연산인 부분적분 $\\int u\\,v'\\,dx=uv-\\int u'v\\,dx$, 미분 우선순위(로·다·삼·지)와 도표적분(Tabular Integration)을 정리합니다.",
    hookTitle: "부분적분 ‘로·다·삼·지’ & 도표적분", hookSub: "로그·다항·삼각·지수 순으로 미분 선택 · 대각선 부호 교대!",
    hookSay: "다항식과 지수·삼각함수가 곱해진 적분을 실수 없이 3초 만에 끝내는 로다삼지 법칙과 도표적분법, 바로 정리합니다.",
    hookCap: "부분적분법과 도표적분 · 30초 정리",
    whySay: "두 함수의 곱 유 브이를 미분한 식을 적분하여 이항하면, 미분하기 쉬운 함수 유는 미분해서 차수를 낮추고 적분하기 쉬운 브이 프라임은 적분하는 부분적분 공식이 됩니다.",
    whyCap: "$(uv)'=u'v+uv'\\ \\Longleftrightarrow\\ \\int u\\,v'\\,dx=u\\,v-\\int u'\\,v\\,dx$",
    histTag: "브룩 테일러", histSay: "곱의 미분법을 역으로 적분에 활용한 부분적분법은 1715년 영국의 수학자 브룩 테일러가 정립했습니다.",
    histCap: "테일러(1715)의 부분적분 공식과 로·다·삼·지(LIATE) 우선순위",
    fParts: [
      { say: "서로 다른 두 함수가 곱해져 있을 때는 로그함수, 다항함수, 삼각함수, 지수함수 순서인 로다삼지에서 앞쪽을 미분할 함수 유로 잡습니다.", cap: "미분($u$) 선택 우선순위: 로($\\ln x$) $\\to$ 다($x^{n}$) $\\to$ 삼($\\sin,\\cos$) $\\to$ 지($e^{x}$)" },
      { say: "로그함수 엘엔 엑스 단독 적분은 앞에 상수 일이 곱해진 것으로 보고 엘엔 엑스를 미분, 일을 적분하여 엑스 엘엔 엑스 빼기 엑스를 얻습니다.", cap: "필수 암기: $\\int\\ln x\\,dx=x\\ln x-x+C$" },
      { say: "다항식 곱하기 이에 엑스 제곱은 왼쪽 열은 영이 될 때까지 계속 미분하고 오른쪽 열은 계속 적분한 뒤 플러스, 마이너스 부호를 번갈아 대각선으로 곱합니다.", cap: "도표적분(DI법): $\\int P(x)e^{x}\\,dx=\\bigl(P(x)-P'(x)+P''(x)-\\cdots\\bigr)e^{x}+C$!" }
    ],
    fChips: [
      "\\int u\\,v'\\,dx=u\\,v-\\int u'\\,v\\,dx\\qquad (\\text{미분 }u\\text{ 우선순위: 로}\\cdot\\text{다}\\cdot\\text{삼}\\cdot\\text{지})",
      "\\int\\ln x\\,dx=x\\ln x-x+C,\\qquad \\int x\\,e^{x}\\,dx=(x-1)e^{x}+C",
      "\\text{도표적분: }\\int P(x)e^{x}\\,dx=\\bigl(P(x)-P'(x)+P''(x)-\\cdots\\bigr)e^{x}+C"
    ],
    fLabels: ["로·다·삼·지 미분 선택", "도표적분 (P − P' + P'')e^x"],
    exParts: [
      { say: "예를 들어 인테그랄 영부터 일까지 엑스 곱하기 이에 엑스 제곱 디엑스의 값을 구해 봅시다.", cap: "$\\int_{0}^{1}x\\,e^{x}\\,dx$ 의 값 구하기" },
      { say: "엑스를 미분하면 일이고 부호를 교대하면 부정적분은 엑스 빼기 일 곱하기 이에 엑스 제곱입니다.", cap: "$\\int x\\,e^{x}\\,dx=(x-1)e^{x}+C$" },
      { say: "일을 대입하면 영이고 영을 대입하면 마이너스 일이므로 영 빼기 마이너스 일, 정답은 일입니다.", cap: "$\\Bigl[(x-1)e^{x}\\Bigr]_{0}^{1}=0-(-1)=1$" }
    ],
    exChips: [
      "\\int_{0}^{1}x\\,e^{x}\\,dx=\\Bigl[(x-1)e^{x}\\Bigr]_{0}^{1}",
      "=(1-1)e^{1}-(0-1)e^{0}",
      "=0-(-1)=1"
    ],
    exLabels: ["부정적분 (x − 1)e^x", "정답 1"],
    exGraph: {
      f: x => 0.55 * x * Math.exp(0.55 * x) + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.2], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "x = 0" }, r2: { x: 2.2, col: PK, label: "x = 1 (넓이 = 1)" },
      fn: { t: "∫ P(x)e^x dx = (P − P' + P'')e^x · 부호만 교대로 미분!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "[(x − 1)e^x]₀¹", finalS: "정적분 = 1", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 정적분 인테그랄 일부터 이까지 엘엔 엑스 디엑스의 값은 얼마일까요?", cap: "$\\int_{1}^{e}\\ln x\\,dx$ 의 값 구하기 (자작 문항)" },
      { say: "엘엔 엑스의 부정적분은 엑스 엘엔 엑스 빼기 엑스입니다.", cap: "$\\Bigl[x\\ln x-x\\Bigr]_{1}^{e}$" },
      { say: "위끝 이를 대입하면 이 빼기 이인 영이고, 아래끝 일을 대입하면 영 빼기 일인 마이너스 일이므로 영 빼기 마이너스 일, 일입니다.", cap: "$(e-e)-(0-1)=1$" }
    ],
    examChips: [
      "\\int_{1}^{e}\\ln x\\,dx=\\Bigl[x\\ln x-x\\Bigr]_{1}^{e}",
      "=(e\\ln e-e)-(1\\ln 1-1)",
      "=0-(-1)=1"
    ],
    examLabels: ["[x ln x − x]₁^e", "정답 1"],
    examGraph: {
      f: x => 0.85 * Math.log(x + 0.6) + 0.35, GY0: 390, GV: 110, xr: [0.2, 3], area: [0.4, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "x = 1" }, r2: { x: 2.4, col: GO, label: "x = e (정적분 = 1)" },
      fn: { t: "쌍둥이 공식 암기: ∫₀¹ x e^x dx = 1  ,  ∫₁^e ln x dx = 1!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "[x ln x − x]₁^e", finalS: "1", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 인테그랄 일부터 이까지 엘엔 엑스 디엑스가 일이라는 것과 영부터 일까지 엑스 이에 엑스 제곱 디엑스가 일이라는 것은 역함수 대칭 쌍으로 함께 외워두면 삼 초 만에 풀립니다.", cap: "① 역함수 쌍둥이 정적분: $\\int_{1}^{e}\\ln x\\,dx=1,\\quad \\int_{0}^{1}xe^{x}\\,dx=1$!" },
      { say: "둘째, 엑스 제곱 곱하기 이에 엑스 제곱을 도표적분하면 엑스 제곱 빼기 이 엑스 더하기 이 전체에 이에 엑스 제곱을 곱한 식이 일 초 만에 나옵니다.", cap: "② 2차 도표적분: $\\int x^{2}e^{x}\\,dx=(x^{2}-2x+2)e^{x}+C$!" },
      { say: "셋째, 이에 엑스 제곱 곱하기 사인 엑스처럼 둘 다 영이 되지 않는 순환형 부분적분은 두 번 부분적분한 뒤 원래 적분식을 좌변으로 이항해 이로 나눕니다.", cap: "③ 순환형 적분 $\\int e^{x}\\sin x\\,dx=\\dfrac{1}{2}e^{x}(\\sin x-\\cos x)+C$" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 리미트 시그마 무한급수를 정적분으로 바꾸는 제팔십육강입니다.", cap: "제86강 · 정적분과 무한급수의 변환 3가지 기준" },
      { tag: "연계 ②", say: "치환적분과 분수 로그적분을 다루는 제팔십사강도 함께 복습해 보세요.", cap: "제84강 · 치환적분법과 속미분 로그적분" },
      { tag: "이 사이트", say: "이 사이트의 제팔십육강과 제팔십사강을 이어서 보세요.", cap: "제86강 · 정적분과 급수의 합  /  제84강 · 치환적분법" }
    ],
    nextLinks: [
      { lec: 86, label: "제86강 열기 (정적분과 급수 변환)" },
      { lec: 84, label: "제84강 열기 (치환적분·로그적분)" },
      { lec: 87, label: "제87강 열기 (단면 부피·곡선 길이)" }
    ]
  },
  {
    lec: 86,
    title: "숏츠식 판서 미리보기 · 정적분과 무한급수의 변환 3가지 치환 기준",
    desc: "리만 합 $\\lim_{n\\to\\infty}\\frac{1}{n}\\sum_{k=1}^{n}f\\left(a+\\frac{p}{n}k\\right)$ 을 정적분으로 바꾸는 3가지 방법($a+\\frac{p}{n}k=x$ vs $\\frac{p}{n}k=x$ vs $\\frac{k}{n}=x$)을 정리합니다.",
    hookTitle: "무한급수 → 정적분 변환 3초 공식", hookSub: "k/n → x · 1/n → dx · 적분구간은 [0, 1] 로 통일!",
    hookSay: "리미트 시그마로 주어진 무한급수를 실수 없이 3초 만에 정적분으로 바꾸는 황금 규칙, 바로 정리합니다.",
    hookCap: "정적분과 급수의 변환 · 30초 정리",
    whySay: "구간을 엔 등분한 직사각형들의 가로 폭 엔 분의 피가 디엑스가 되고 케이 번째 엑스좌표가 변수 엑스가 되어, 엔이 무한대로 갈 때 직사각형 넓이의 합이 곡선 아래 정적분 넓이로 수렴합니다.",
    whyCap: "가로 폭 $\\Delta x=\\dfrac{p}{n}\\to dx$, 높이 $f(x_{k})\\to f(x)$, $\\lim_{n\\to\\infty}\\sum\\to\\int$",
    histTag: "리만 적분", histSay: "구분구적법의 분할 합이 극한에서 정적분으로 수렴한다는 엄밀한 정의는 베른하르트 리만의 리만 합에서 완성되었습니다.",
    histCap: "리만 합(Riemann Sum) $\\lim_{n\\to\\infty}\\sum_{k=1}^{n}f(x_{k})\\Delta x=\\int_{a}^{b}f(x)\\,dx$",
    fParts: [
      { say: "가장 실수가 없는 방법은 무조건 엔 분의 케이만 엑스로 바꾸고, 시그마 앞의 엔 분의 일은 디엑스로, 적분 구간은 영부터 일까지로 고정하는 것입니다.", cap: "황금 공식(실수 0%): $\\dfrac{k}{n}\\to x,\\quad \\dfrac{1}{n}\\to dx,\\quad \\text{적분구간 }[0,1]$ 고정!" },
      { say: "만약 에이 더하기 엔 분의 피 케이 전체를 엑스로 치환하면, 케이 앞의 계수 엔 분의 피가 디엑스가 되고 적분 구간은 에이부터 에이 더하기 피까지가 됩니다.", cap: "전체 치환: $a+\\dfrac{p}{n}k\\to x,\\quad \\dfrac{p}{n}\\to dx,\\quad \\text{적분구간 }[a,\\ a+p]$" },
      { say: "시그마 안에 엔 분의 케이 모양이 안 보이면 분모·분자를 엔의 거듭제곱으로 묶거나 나누어 강제로 엔 분의 케이와 엔 분의 일을 만들어 냅니다.", cap: "식 변형: $\\dfrac{1}{n}$ (가로 폭) 과 $\\dfrac{k}{n}$ (변수 $x$) 2개 세트를 강제 생성!" }
    ],
    fChips: [
      "\\lim_{n\\to\\infty}\\dfrac{1}{n}\\sum_{k=1}^{n}f\\left(\\dfrac{k}{n}\\right)=\\int_{0}^{1}f(x)\\,dx\\qquad \\left(\\dfrac{k}{n}\\to x,\\ \\dfrac{1}{n}\\to dx\\right)",
      "\\lim_{n\\to\\infty}\\dfrac{p}{n}\\sum_{k=1}^{n}f\\left(a+\\dfrac{p}{n}k\\right)=\\int_{a}^{a+p}f(x)\\,dx",
      "\\lim_{n\\to\\infty}\\dfrac{1}{n}\\sum_{k=1}^{n}f\\left(a+\\dfrac{p}{n}k\\right)=\\int_{0}^{1}f(a+px)\\,dx"
    ],
    fLabels: ["k/n → x, 1/n → dx, [0, 1]", "전체 치환 시 dx = (p/n) 주의!"],
    exParts: [
      { say: "예를 들어 리미트 엔이 무한대로 갈 때 엔 분의 일 시그마 케이는 일부터 엔까지 일 더하기 엔 분의 이 케이 전체의 세제곱의 값을 구해 봅시다.", cap: "$\\lim_{n\\to\\infty}\\dfrac{1}{n}\\sum_{k=1}^{n}\\left(1+\\dfrac{2k}{n}\\right)^{3}$ 의 값 구하기" },
      { say: "엔 분의 케이를 엑스로, 엔 분의 일을 디엑스로 바꾸면 인테그랄 영부터 일까지 일 더하기 이 엑스의 세제곱 디엑스가 됩니다.", cap: "$\\dfrac{k}{n}\\to x,\\ \\dfrac{1}{n}\\to dx\\ \\Rightarrow\\ \\int_{0}^{1}(1+2x)^{3}\\,dx$" },
      { say: "적분하면 팔 분의 일 곱하기 일 더하기 이 엑스의 네 제곱이므로 팔 분의 팔십일 빼기 일, 십입니다.", cap: "$\\left[\\dfrac{1}{8}(1+2x)^{4}\\right]_{0}^{1}=\\dfrac{81-1}{8}=10$" }
    ],
    exChips: [
      "\\lim_{n\\to\\infty}\\dfrac{1}{n}\\sum_{k=1}^{n}\\left(1+2\\cdot\\dfrac{k}{n}\\right)^{3}=\\int_{0}^{1}(1+2x)^{3}\\,dx",
      "=\\left[\\dfrac{1}{4}\\cdot\\dfrac{1}{2}(1+2x)^{4}\\right]_{0}^{1}",
      "=\\dfrac{3^{4}-1^{4}}{8}=\\dfrac{80}{8}=10"
    ],
    exLabels: ["∫₀¹ (1 + 2x)³ dx", "정답 10"],
    exGraph: {
      f: x => 0.35 * Math.pow(0.8 * x + 0.6, 3) + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "k = 1 → x = 0" }, r2: { x: 2.5, col: PK, label: "k = n → x = 1" },
      fn: { t: "k/n → x , 1/n → dx , 구간 [0, 1] 로 바꾸면 계수 실수 0%!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "(81 − 1) / 8", finalS: "10", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 리미트 엔이 무한대로 갈 때 시그마 케이는 일부터 엔까지 엔 더하기 케이 분의 일의 값은 얼마일까요?", cap: "$\\lim_{n\\to\\infty}\\sum_{k=1}^{n}\\dfrac{1}{n+k}$ 의 값 구하기 (자작 문항)" },
      { say: "분모에서 엔을 밖으로 묶어내면 엔 분의 일 곱하기 일 더하기 엔 분의 케이 분의 일이 됩니다.", cap: "$\\dfrac{1}{n+k}=\\dfrac{1}{n}\\cdot\\dfrac{1}{1+k/n}$ (가로 폭 $\\dfrac{1}{n}$ 과 $\\dfrac{k}{n}$ 동시 탄생!)" },
      { say: "인테그랄 영부터 일까지 일 더하기 엑스 분의 일 디엑스이므로 엘엔 이 빼기 엘엔 일, 정답은 엘엔 이입니다.", cap: "$\\int_{0}^{1}\\dfrac{1}{1+x}\\,dx=\\Bigl[\\ln(1+x)\\Bigr]_{0}^{1}=\\ln 2$" }
    ],
    examChips: [
      "\\lim_{n\\to\\infty}\\sum_{k=1}^{n}\\dfrac{1}{n+k}=\\lim_{n\\to\\infty}\\dfrac{1}{n}\\sum_{k=1}^{n}\\dfrac{1}{1+\\frac{k}{n}}",
      "=\\int_{0}^{1}\\dfrac{1}{1+x}\\,dx=\\Bigl[\\ln(1+x)\\Bigr]_{0}^{1}",
      "=\\ln 2"
    ],
    examLabels: ["분모 n 묶기 → ∫₀¹ dx/(1+x)", "정답 ln 2"],
    examGraph: {
      f: x => 1.4 / (0.8 * x + 1) + 0.3, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "x = 0" }, r2: { x: 2.4, col: GO, label: "x = 1 (넓이 ln 2)" },
      fn: { t: "1/(n + k) = (1/n) · 1/(1 + k/n) ⇒ ∫₀¹ 1/(1 + x) dx = ln 2", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "[ln(1 + x)]₀¹", finalS: "ln 2", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 시그마가 케이는 일부터 이엔까지이면 적분 구간만 영부터 이까지로 늘어나고 나머지는 똑같습니다.", cap: "① 위끝이 $2n$ 일 때: $\\sum_{k=1}^{2n}\\ \\Longrightarrow\\ \\text{적분 구간만 }[0,2]$ 로 확장!" },
      { say: "둘째, 적분은 왜 직사각형부터 시작할까를 다룬 제삼십팔강과 원뿔의 부피 구분구적법 제삼십구강을 함께 보면 원리가 완벽히 연결됩니다.", cap: "② 제38·39강 구분구적법 직결: 직사각형 엔 등분 합 $\\longrightarrow$ 정적분!" },
      { say: "셋째, 이 구분구적법 원리를 삼차원 입체도형의 단면 넓이에 그대로 적용한 것이 바로 다음 강의인 입체도형의 부피입니다.", cap: "③ 제87강 부피 직결: 단면 기둥 부피 합 $\\sum S(x_{k})\\Delta x\\longrightarrow\\int_{a}^{b}S(x)\\,dx$!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "다음은 미적분 심화의 대단원 완결편인 입체도형의 부피와 곡선의 길이 제팔십칠강입니다.", cap: "제87강 · 단면 넓이 적분 부피와 곡선의 길이·이동거리" },
      { tag: "연계 ②", say: "구분구적법의 본질을 다루는 제삼십팔강, 제삼십구강도 함께 보세요.", cap: "제38강 · 적분은 왜 직사각형부터 시작할까  /  제39강 · 원뿔 부피 증명" },
      { tag: "이 사이트", say: "이 사이트의 제팔십칠강과 제삼십팔강을 이어서 보세요.", cap: "제87강 · 단면 부피와 곡선 길이  /  제38강 · 구분구적법의 본질" }
    ],
    nextLinks: [
      { lec: 87, label: "제87강 열기 (단면 부피·곡선 길이)" },
      { lec: 38, label: "제38강 열기 (구분구적법의 본질)" },
      { lec: 39, label: "제39강 열기 (원뿔 부피 증명)" }
    ]
  },
  {
    lec: 87,
    title: "숏츠식 판서 미리보기 · 단면 넓이 적분 부피와 곡선의 길이·이동거리",
    desc: "단면 넓이 $S(x)$ 를 적분하는 입체 부피 $V=\\int_{a}^{b}S(x)\\,dx$ 와 평면 운동 이동거리·곡선의 길이 $l=\\int_{a}^{b}\\sqrt{1+\\{f'(x)\\}^{2}}\\,dx$ 를 정리합니다.",
    hookTitle: "입체도형 부피 ∫S(x)dx & 곡선의 길이", hookSub: "단면 한 조각 넓이 S(x) 만 구해서 적분 · 길이는 √(dx² + dy²)!",
    hookSay: "미적분의 마지막 단원인 입체도형의 부피와 곡선의 길이를 그림을 입체로 그리지 않고도 3초 만에 푸는 공식, 바로 정리합니다.",
    hookCap: "입체도형의 부피와 곡선의 길이 · 30초 정리",
    whySay: "입체도형을 엑스축에 수직인 평면으로 자른 단면의 넓이 에스 엑스에 얇은 두께 디엑스를 곱해 모두 더하면 부피가 되고, 미소 직각삼각형의 빗변 루트 디엑스 제곱 더하기 디와이 제곱을 적분하면 곡선의 길이가 됩니다.",
    whyCap: "부피 $V=\\int_{a}^{b}S(x)\\,dx$, 곡선의 길이 $l=\\int_{a}^{b}\\sqrt{(dx)^{2}+(dy)^{2}}=\\int_{a}^{b}\\sqrt{1+\\{f'(x)\\}^{2}}\\,dx$",
    histTag: "카발리에리·아르키메데스", histSay: "단면의 넓이가 같으면 부피도 같다는 카발리에리의 원리가 정적분 부피 공식의 모태가 되었습니다.",
    histCap: "카발리에리의 원리와 호의 길이(Arc Length) 미소 피타고라스 적분",
    fParts: [
      { say: "입체도형의 부피는 입체를 그리지 말고, 위치 엑스에서의 밑변 길이를 구해 단면 도형의 넓이 에스 엑스 식만 세워 에이부터 비까지 적분합니다.", cap: "단면 부피 공식: $V=\\int_{a}^{b}S(x)\\,dx$ (정사각형: $l^{2}$, 정삼각형: $\\dfrac{\\sqrt{3}}{4}l^{2}$, 반원: $\\dfrac{\\pi}{8}l^{2}$)" },
      { say: "평면 위를 움직이는 점의 이동거리와 매개변수 곡선의 길이는 속력인 루트 디엑스 디티의 제곱 더하기 디와이 디티의 제곱을 적분합니다.", cap: "평면 이동거리·길이: $l=\\int_{a}^{b}\\sqrt{\\left(\\dfrac{dx}{dt}\\right)^{2}+\\left(\\dfrac{dy}{dt}\\right)^{2}}\\,dt$" },
      { say: "일반 함수 와이는 에프 엑스의 곡선의 길이는 루트 일 더하기 에프 프라임 엑스의 제곱을 적분하며, 근호 안이 무조건 완전제곱식이 되도록 출제됩니다.", cap: "곡선의 길이: $l=\\int_{a}^{b}\\sqrt{1+\\{f'(x)\\}^{2}}\\,dx$ ($1+\\{f'(x)\\}^{2}$ 은 완전제곱 변형!)" }
    ],
    fChips: [
      "V=\\int_{a}^{b}S(x)\\,dx\\quad \\left(\\text{정사각형 }l^{2},\\ \\text{정삼각형 }\\dfrac{\\sqrt{3}}{4}l^{2},\\ \\text{반원 }\\dfrac{\\pi}{8}l^{2}\\right)",
      "\\text{매개변수 이동거리·길이 }l=\\int_{t_{1}}^{t_{2}}\\sqrt{\\left(\\dfrac{dx}{dt}\\right)^{2}+\\left(\\dfrac{dy}{dt}\\right)^{2}}\\,dt",
      "\\text{곡선 }y=f(x)\\text{ 의 길이 }l=\\int_{a}^{b}\\sqrt{1+\\{f'(x)\\}^{2}}\\,dx"
    ],
    fLabels: ["단면 넓이 S(x) 적분 = 부피", "속력 √(x'² + y'²) 적분 = 길이"],
    exParts: [
      { say: "예를 들어 엑스가 영부터 사까지일 때 곡선 와이는 루트 엑스와 엑스축 사이의 선분을 한 변으로 하는 정사각형 단면 입체의 부피를 구해 봅시다.", cap: "$0\\le x\\le 4$ 에서 밑변 $l=\\sqrt{x}$ 인 정사각형 단면 입체의 부피" },
      { say: "한 변의 길이가 루트 엑스이므로 정사각형 단면의 넓이 에스 엑스는 제곱한 엑스입니다.", cap: "단면 넓이 $S(x)=(\\sqrt{x})^{2}=x$" },
      { say: "인테그랄 영부터 사까지 엑스 디엑스이므로 이분의 일 곱하기 십육, 팔입니다.", cap: "$V=\\int_{0}^{4}x\\,dx=\\left[\\dfrac{1}{2}x^{2}\\right]_{0}^{4}=8$" }
    ],
    exChips: [
      "\\text{단면 정사각형 한 변 }l=\\sqrt{x}\\ \\Longrightarrow\\ S(x)=l^{2}=x",
      "V=\\int_{0}^{4}S(x)\\,dx=\\int_{0}^{4}x\\,dx",
      "=\\left[\\dfrac{1}{2}x^{2}\\right]_{0}^{4}=8"
    ],
    exLabels: ["단면 넓이 S(x) = x", "부피 V = 8"],
    exGraph: {
      f: x => 0.55 * x + 0.35, GY0: 390, GV: 110, xr: [0, 3], area: [0.3, 2.5], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.3, col: CY, label: "x = 0" }, r2: { x: 2.5, col: PK, label: "x = 4 (단면 S(x)=x)" },
      fn: { t: "입체 부피 = ∫ S(x) dx · 단면 도형의 넓이 식 S(x) 하나면 끝!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "∫₀⁴ x dx", finalS: "부피 V = 8", finalPh: 2, scaleTo: 1
    },
    examParts: [
      { say: "수능형 문제입니다. 시각 티가 영부터 이까지일 때 좌표평면 위를 움직이는 점 피의 위치가 엑스는 삼 티, 와이는 사 티 더하기 일일 때 점 피가 움직인 거리는 얼마일까요?", cap: "$0\\le t\\le 2$ 에서 $x=3t,\\ y=4t+1$ 인 점 $P$ 의 이동거리 (자작 문항)" },
      { say: "속도 성분은 디엑스 디티가 삼, 디와이 디티가 사이므로 속력은 루트 구 더하기 십육, 오로 일정합니다.", cap: "속력 $v=\\sqrt{3^{2}+4^{2}}=5$" },
      { say: "인테그랄 영부터 이까지 오 디티이므로 이동거리는 십입니다.", cap: "$s=\\int_{0}^{2}5\\,dt=10$" }
    ],
    examChips: [
      "\\dfrac{dx}{dt}=3,\\quad \\dfrac{dy}{dt}=4\\ \\Longrightarrow\\ \\text{속력 }\\sqrt{3^{2}+4^{2}}=5",
      "s=\\int_{0}^{2}\\sqrt{\\left(\\dfrac{dx}{dt}\\right)^{2}+\\left(\\dfrac{dy}{dt}\\right)^{2}}\\,dt=\\int_{0}^{2}5\\,dt",
      "=10"
    ],
    examLabels: ["속력 √(3² + 4²) = 5", "정답 이동거리 10"],
    examGraph: {
      f: x => 1.1, GY0: 390, GV: 110, xr: [0, 3], area: [0.4, 2.4], ytop: 45, ybot: 445, labelY: 448,
      r1: { x: 0.4, col: CY, label: "t = 0" }, r2: { x: 2.4, col: GO, label: "t = 2 (속력 5 × 2 = 10)" },
      fn: { t: "평면 이동거리 = 속력 √((dx/dt)² + (dy/dt)²) 의 정적분!", x: 480, y: 72 }, sPos: [480, 275], sOpenTxt: "5 × 2", finalS: "거리 = 10", finalPh: 2, scaleTo: 1
    },
    tips: [
      { say: "첫째, 단면이 정삼각형이면 정사각형 부피를 먼저 구한 뒤 마지막에 사분의 루트 삼만 곱하면 계산이 훨씬 깔끔합니다.", cap: "① 단면 상수 밖으로 빼기: 정삼각형은 $\\dfrac{\\sqrt{3}}{4}\\int l^{2}\\,dx$, 반원은 $\\dfrac{\\pi}{8}\\int l^{2}\\,dx$!" },
      { say: "둘째, 곡선의 길이 문제에서 에프 엑스가 에이 빼기 비 모양이면 일 더하기 에프 프라임의 제곱은 가운데 부호만 플러스로 바뀐 에이 프라임 더하기 비 프라임의 완전제곱이 됩니다.", cap: "② 완전제곱 마법: $\\left(a-\\dfrac{1}{4a}\\right)^{2}+1=\\left(a+\\dfrac{1}{4a}\\right)^{2}$ (가운데 부호만 $+$ 로!)" },
      { say: "셋째, 이로써 미적분 심화 열두 개 강의 사슬이 모두 완성되었습니다. 첫 단계인 제칠십육강 수열의 극한부터 전체 흐름을 복습해 보세요.", cap: "③ 제76강~제87강 완결: 수열의 극한 $\\to$ 초월함수 미분 $\\to$ 적분과 부피 완성!" }
    ],
    nextParts: [
      { tag: "연계 ①", say: "미적분 심화의 출발점인 제칠십육강 수열의 극한과 제칠십칠강 도형 등비급수로 돌아가 전체 흐름을 복습해 보세요.", cap: "제76강 · 수열의 극한  /  제77강 · 도형 프랙탈 등비급수" },
      { tag: "연계 ②", say: "원뿔의 부피와 구분구적법 증명을 다루는 제삼십구강도 함께 보세요.", cap: "제39강 · 원뿔의 부피와 구분구적법 증명" },
      { tag: "이 사이트", say: "이 사이트의 제칠십육강과 제삼십구강을 이어서 보세요.", cap: "제76강 · 미적분 심화 첫 단계  /  제39강 · 원뿔 부피 증명" }
    ],
    nextLinks: [
      { lec: 76, label: "제76강 열기 (미적분 심화 첫 단계)" },
      { lec: 39, label: "제39강 열기 (원뿔 부피 증명)" },
      { lec: 83, label: "제83강 열기 (초월함수 4대 개형)" }
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
    subj: "calc",
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

const ALL_SPECS = [...CALC_SPECS_A, ...CALC_SPECS_B];
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
  const cInfo = CALC_CHAIN.find(c => c.lec === cfg.lec) || { step: 1, badge: "미적분 심화", title: cfg.title };
  mainEl.innerHTML = `
    <div class="glass-card" style="margin-bottom:22px;border-left:5px solid #34d399">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px">
        <span class="badge-pill" style="background:rgba(52,211,153,.18);color:#6ee7b7;border-color:rgba(52,211,153,.4)">
          📗 미적분 심화 · 사슬 ${cInfo.step}/12단계 (${cInfo.badge})
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
    mount.innerHTML = `${calcChainNavHtml(cfg.lec)}
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
      const ok = await speak("안녕하세요. 미적분 심화 핵심 공식을 함께 정리해 볼까요?");
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

const CALC_PLAYERS = {};
function initCalc() {
  CONFIGS.forEach(cfg => {
    if (!CALC_PLAYERS[cfg.lec]) CALC_PLAYERS[cfg.lec] = createPlayer(cfg);
    CALC_PLAYERS[cfg.lec].init();
  });
}

window.CalcShorts = { PLAYERS: CALC_PLAYERS, CONFIGS, initCalc };
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initCalc);
else initCalc();
window.addEventListener("load", initCalc);
})();
