/* 수학 II · 다항함수 미적분 연계 숏츠 판서 시리즈 (제9강 · 제1강 · 제3강 · 제4강)
   제2강(정적분 넓이 만능 공식) 마지막 장면 '다음에 이어서 볼 내용'에서 예고한 후속 강의를
   같은 9:16 세로 판서·식 조각 애니메이션·그래프·한국어 음성 규격으로 이어서 제공한다.
   대본·문항·그래프·연출 모두 직접 창작(자작 수능형 문항, 역사 서술은 출처 확인 필요 안내 포함). */
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
const CY = "#38bdf8", PK = "#f472b6", GO = "#fbbf24", GR = "#34d399", PU = "#a78bfa";
const cl = (c, t) => `\\textcolor{${c}}{${t}}`;
const estMs = t => Math.max(1800, Math.round(Array.from(t || "").length * 165) + 600);

/* ------------------------------------------------------------------ WebAudio 합성 효과음 (외부 파일 없음) */
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
      o.type = "sine";
      o.frequency.setValueAtTime(220, now);
      o.frequency.exponentialRampToValueAtTime(520, now + 0.18);
      g.gain.setValueAtTime(0.001, now);
      g.gain.linearRampToValueAtTime(0.045, now + 0.05);
      g.gain.exponentialRampToValueAtTime(0.001, now + 0.19);
      o.connect(g); g.connect(ctx.destination);
      o.start(now); o.stop(now + 0.2);
    } else if (kind === "pop") {
      const o = ctx.createOscillator(), g = ctx.createGain();
      o.type = "triangle";
      o.frequency.setValueAtTime(520, now);
      o.frequency.exponentialRampToValueAtTime(880, now + 0.11);
      g.gain.setValueAtTime(0.06, now);
      g.gain.exponentialRampToValueAtTime(0.001, now + 0.13);
      o.connect(g); g.connect(ctx.destination);
      o.start(now); o.stop(now + 0.14);
    } else if (kind === "chime") {
      [523.25, 659.25, 783.99, 1046.5].forEach((freq, i) => {
        const o = ctx.createOscillator(), g = ctx.createGain(), t0 = now + i * 0.07;
        o.type = "sine";
        o.frequency.setValueAtTime(freq, t0);
        g.gain.setValueAtTime(0.05, t0);
        g.gain.exponentialRampToValueAtTime(0.001, t0 + 0.35);
        o.connect(g); g.connect(ctx.destination);
        o.start(t0); o.stop(t0 + 0.36);
      });
    }
  } catch (e) { /* 오디오 차단 환경 무시 */ }
}

/* ------------------------------------------------------------------ 강의 이동 및 스크롤 */
const PLAYERS = {};
function stopAllPlayers() {
  Object.keys(PLAYERS).forEach(k => { if (PLAYERS[k] && PLAYERS[k].stop) PLAYERS[k].stop(); });
  if (window.speechSynthesis) { try { speechSynthesis.cancel(); } catch (e) { /* 무시 */ } }
}
function openLectureShorts(lecNum) {
  stopAllPlayers();
  if (typeof window.setLecture === "function") {
    window.setLecture(lecNum, false);
  }
  const hostId = `l${lecNum}ShortsHost`;
  setTimeout(() => {
    const el = $(hostId) || $(`lecture${lecNum}View`);
    if (el) {
      const top = el.getBoundingClientRect().top + window.pageYOffset - 80;
      window.scrollTo({ top: Math.max(0, top), behavior: "smooth" });
    }
  }, 60);
}
window.openLectureShorts = openLectureShorts;

/* ==================================================================
   1. 제9강 · 정적분과 넓이 & 차함수의 마법
      (제2강 마지막에 예고된 적용 ① 두 곡선 사이의 넓이 + 적용 ② 곡선과 접선 이중근 m=2)
   ================================================================== */
const L9_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "두 곡선과 접선 넓이 공식", sub: "차함수로 30초 풀이", parts: [
      { say: "두 곡선 사이의 넓이와 접선 넓이, 차함수로 묶어 30초 만에 정리합니다.", cap: "두 곡선·접선 넓이 · 차함수 30초 풀이" }
    ] },
    { id: "why", type: "list", head: "이 방법을 쓰는 이유", parts: [
      { say: "두 곡선이나 곡선과 접선으로 둘러싸인 넓이도, 두 식을 빼서 한 식으로 묶으면 정적분 넓이 공식을 그대로 쓸 수 있습니다.", cap: "두 식의 차 $f(x)-g(x)$ 로 묶으면 공식 한 줄" }
    ] },
    { id: "hist", type: "list", head: "원리의 배경", parts: [
      { tag: "17세기", say: "어느 위치에서나 세로 높이 차가 같으면 넓이도 같다는 생각은 카발리에리의 원리와 이어집니다.", cap: "세로 높이 차 $|f(x)-g(x)|$ 보존 원리" }
    ] },
    { id: "curve2", type: "chips", head: "적용 ① 두 곡선 사이의 넓이", parts: [
      { say: "이차곡선 엑스 제곱 빼기 이 엑스와 직선 엑스 사이의 넓이입니다. 두 식을 빼면 엑스 곱하기 엑스 빼기 삼으로 묶입니다.", cap: "차함수 $f(x)-g(x)=x(x-3)$" },
      { say: "교점 영과 삼이 모두 단일근이므로 엠은 일, 엔도 일입니다.", cap: "두 단일근 · $m=1,\\ n=1$" },
      { say: "분자는 일 팩토리얼 곱하기 일 팩토리얼, 분모는 일 더하기 일 더하기 일, 삼 팩토리얼입니다.", cap: "계수 $\\dfrac{1!\\,1!}{3!}=\\dfrac{1}{6}$" },
      { say: "구간의 길이 삼의 세제곱을 곱하면 육분의 일 곱하기 이십칠, 넓이는 이분의 구입니다.", cap: "$\\dfrac{1}{6}\\times 3^{3}=\\dfrac{9}{2}$" }
    ] },
    { id: "tangent", type: "chips", head: "적용 ② 곡선과 접선 사이의 넓이", parts: [
      { say: "다음은 삼차곡선과 접선 사이의 넓이입니다. 두 식을 빼면 접점 영은 이중근, 다른 교점 이는 단일근이 됩니다.", cap: "접점은 이중근($m=2$), 교점은 단일근($n=1$)" },
      { say: "엠은 이, 엔은 일이므로 분자는 이 팩토리얼 일 팩토리얼, 분모는 사 팩토리얼입니다.", cap: "계수 $\\dfrac{2!\\,1!}{4!}=\\dfrac{1}{12}$" },
      { say: "구간의 길이 이의 네제곱을 곱하면 십이분의 일 곱하기 십육, 넓이는 삼분의 사입니다.", cap: "$\\dfrac{1}{12}\\times 2^{4}=\\dfrac{4}{3}$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 삼차곡선 에이 엑스 세제곱 위의 점 일 콤마 에이에서의 접선과 곡선이 이루는 넓이가 사분의 이십칠일 때, 양수 에이를 구해 봅시다.", cap: "접선과 삼차곡선의 넓이가 $\\dfrac{27}{4}$ 일 때 $a$ 구하기 (자작 문항)" },
      { say: "접점 일은 이중근이라 엠은 이, 다른 교점 마이너스 이는 단일근이라 엔은 일이고 구간 길이는 삼입니다.", cap: "$m=2,\\ n=1$ · 구간 길이 $1-(-2)=3$" },
      { say: "공식에 넣으면 에이 곱하기 십이분의 일 곱하기 삼의 네제곱, 사분의 이십칠 에이입니다.", cap: "$a\\times\\dfrac{2!\\,1!}{4!}\\times 3^{4}=\\dfrac{27}{4}\\,a$" },
      { say: "넓이가 사분의 이십칠이므로 에이는 일입니다.", cap: "$a=1$ · 차함수로 묶으면 한 줄 완성" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 두 식을 빼서 인수분해하고 교점과 지수부터 읽습니다.", cap: "① $f(x)-g(x)=a(x-\\alpha)^{m}(x-\\beta)^{n}$ 로 묶기" },
      { say: "둘째, 스치는 접점은 무조건 이중근이라 엠은 이입니다.", cap: "② 접점은 이중근($m=2$), 뚫는 교점은 단일근($n=1$)" },
      { say: "셋째, 이차곡선과 직선은 육분의 일, 삼차곡선과 접선은 십이분의 일입니다.", cap: "③ 이차·직선 $\\dfrac{|a|}{6}(\\beta-\\alpha)^{3}$ · 삼차·접선 $\\dfrac{|a|}{12}(\\beta-\\alpha)^{4}$" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "다음은 다항함수 넓이의 비 일 대 엔 공식입니다. 직사각형을 차수 비율로 바로 나눕니다.", cap: "다항함수 넓이의 비 · $S_{1}:S_{2}=1:n$" },
      { tag: "연계 ②", say: "삼차함수의 대칭 중심과 변곡접선 성질도 이어서 정리합니다.", cap: "삼차함수 변곡접선 · 삼중근과 접선 개수 판별" },
      { tag: "이 사이트", say: "이 사이트의 제일강과 제삼강을 이어서 보세요.", cap: "제1강 · 다항함수 넓이의 비  /  제3강 · 변곡접선 정리하기" }
    ] }
  ];

  const G_CURVE2 = {
    f: x => x * (3 - x), GY0: 390, GV: 95, xr: [-0.3, 3.2], area: [0, 3], ytop: 40, ybot: 445, labelY: 448,
    r1: { x: 0, col: CY, label: "0 · 단일근 (m=1)" }, r2: { x: 3, col: PK, label: "3 · 단일근 (n=1)" },
    fn: { t: "h(x) = f(x) − g(x) = x(x − 3)", x: 610, y: 95 }, sPos: [450, 290], sOpenTxt: "S", finalS: "S = 9/2", finalPh: 3, scaleTo: 1
  };
  const G_TANGENT = {
    f: x => x * x * (2 - x), GY0: 390, GV: 180, xr: [-0.3, 2.25], area: [0, 2], ytop: 40, ybot: 445, labelY: 448, gux: 320,
    r1: { x: 0, col: CY, label: "0 · 접점 이중근 (m=2)" }, r2: { x: 2, col: PK, label: "2 · 교점 단일근 (n=1)" },
    fn: { t: "f(x) − g(x) = x²(x − 2)", x: 620, y: 95 }, sPos: [510, 295], sOpenTxt: "S", finalS: "S = 4/3", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => 0.16 * (x + 2) * (x - 1) * (x - 1), xr: [-2.2, 1.35], area: [-2, 1], GY0: 390, GV: 95, ytop: 40, ybot: 445, labelY: 448, gx0: 560, gux: 210,
    r1: { x: -2, col: PK, label: "−2 · 교점 (n=1)" }, r2: { x: 1, col: CY, label: "1 · 접점 이중근 (m=2)" },
    fn: { t: "f(x) − g(x) = a(x − 1)²(x + 2)", x: 560, y: 90 }, sPos: [380, 285], sOpenTxt: "S = 27/4", finalS: "a = 1 · S = 27/4", finalPh: 3, scaleTo: 1.15
  };

  const chipDefs = {
    curve2: (() => {
      const src = { Fm: [350, 15], Fn: [610, 15], Fd: [480, 15], Fp: [480, 210] };
      const fin = { Fm: [240, 210], Fn: [410, 210], Fd: [325, 345], Fp: [680, 275] };
      return {
        graph: G_CURVE2,
        chips: [
          { id: "T1", tex: "f(x)-g(x)=", cls: "pl" },
          { id: "T2", tex: `x^{${cl(CY, "1")}}`, cls: "cy" },
          { id: "T3", tex: `(x-3)^{${cl(PK, "1")}}`, cls: "pk" },
          { id: "E", tex: "S=", cls: "pl" },
          { id: "Fm", tex: "1!", cls: "cy" },
          { id: "Fn", tex: "1!", cls: "pk" },
          { id: "bar", tex: "", cls: "bar" },
          { id: "Fd", tex: "(1+1+1)!", cls: "go" },
          { id: "Fp", tex: "\\times 3^{3}", cls: "go" },
          { id: "R", tex: "\\dfrac{1}{6}\\times 27=\\dfrac{9}{2}", cls: "go big" }
        ],
        state(ph) {
          const S = {
            T1: { x: 165, y: 15, op: 1 },
            T2: { x: 430, y: 15, op: 1 },
            T3: { x: 685, y: 15, op: 1 }
          };
          const show = (id, minPh) => ({
            x: ph >= minPh ? fin[id][0] : src[id][0],
            y: ph >= minPh ? fin[id][1] : src[id][1],
            op: ph >= minPh ? 1 : 0
          });
          S.E = { x: 85, y: 270, op: ph >= 1 ? 1 : 0 };
          S.bar = { x: 325, y: 310, op: ph >= 1 ? 1 : 0, w: 340 };
          S.Fm = show("Fm", 1);
          S.Fn = show("Fn", 1);
          S.Fd = show("Fd", 2);
          S.Fp = show("Fp", 3);
          if (ph >= 2) { S.Fd.tex = "3!=6"; S.Fd.pop = 1; }
          if (ph >= 3) {
            ["Fm", "Fn", "Fd", "Fp", "E"].forEach(k => { S[k].op = 0.25; });
            S.bar.op = 0.25;
          }
          S.R = { x: 480, y: 400, op: ph >= 3 ? 1 : 0, pop: ph >= 3 ? 1 : 0 };
          return S;
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T2", b: "Fm", col: CY }, { a: "T3", b: "Fn", col: PK });
          if (ph === 2) L.push({ a: "T2", b: "Fd", col: CY }, { a: "T3", b: "Fd", col: PK, label: "1 + 1 + 1 = 3" });
          return L;
        },
        fx: ph => ph === 3 ? "confetti" : ph === 2 ? "spark" : ""
      };
    })(),
    tangent: (() => {
      const src = { Fm: [420, 15], Fn: [690, 15], Fd: [550, 15], Fp: [550, 210] };
      const fin = { Fm: [240, 200], Fn: [420, 200], Fd: [330, 335], Fp: [690, 265] };
      return {
        graph: G_TANGENT,
        chips: [
          { id: "T1", tex: "f(x)-g(x)=", cls: "pl" },
          { id: "T2", tex: `x^{${cl(CY, "2")}}`, cls: "cy" },
          { id: "T3", tex: `(x-2)^{${cl(PK, "1")}}`, cls: "pk" },
          { id: "E", tex: "S=", cls: "pl" },
          { id: "Fm", tex: "2!", cls: "cy" },
          { id: "Fn", tex: "1!", cls: "pk" },
          { id: "bar", tex: "", cls: "bar" },
          { id: "Fd", tex: "(2+1+1)!", cls: "go" },
          { id: "Fp", tex: "\\times 2^{4}", cls: "go" },
          { id: "R", tex: "\\dfrac{1}{12}\\times 16=\\dfrac{4}{3}", cls: "go big" }
        ],
        state(ph) {
          const S = {
            T1: { x: 165, y: 15, op: 1 },
            T2: { x: 430, y: 15, op: 1 },
            T3: { x: 685, y: 15, op: 1 }
          };
          const show = (id, minPh) => ({
            x: ph >= minPh ? fin[id][0] : src[id][0],
            y: ph >= minPh ? fin[id][1] : src[id][1],
            op: ph >= minPh ? 1 : 0
          });
          S.E = { x: 85, y: 265, op: ph >= 1 ? 1 : 0 };
          S.bar = { x: 330, y: 300, op: ph >= 1 ? 1 : 0, w: 350 };
          S.Fm = show("Fm", 1);
          S.Fn = show("Fn", 1);
          S.Fd = show("Fd", 1);
          S.Fp = show("Fp", 2);
          if (ph >= 2) {
            ["Fm", "Fn", "Fd", "Fp", "E"].forEach(k => { S[k].op = 0.25; });
            S.bar.op = 0.25;
          }
          S.R = { x: 480, y: 395, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 };
          return S;
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T2", b: "Fm", col: CY }, { a: "T3", b: "Fn", col: PK, label: "접점 m=2 · 교점 n=1" });
          return L;
        },
        fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
      };
    })(),
    exam: (() => {
      const src = { M: [350, 10], N: [620, 10], W: [480, 130] };
      return {
        graph: G_EXAM,
        chips: [
          { id: "T1", tex: "f-g=a", cls: "pl" },
          { id: "T2", tex: `(x-1)^{${cl(CY, "2")}}`, cls: "cy" },
          { id: "T3", tex: `(x+2)^{${cl(PK, "1")}}`, cls: "pk" },
          { id: "M", tex: "m=2,\\ n=1", cls: "cy" },
          { id: "N", tex: "\\beta-\\alpha=3", cls: "pk" },
          { id: "W", tex: "S=a\\times\\dfrac{2!\\,1!}{4!}\\times 3^{4}=\\dfrac{27}{4}\\,a", cls: "go" },
          { id: "V", tex: "\\dfrac{27}{4}\\,a=\\dfrac{27}{4}\\ \\Rightarrow\\ a=1", cls: "go v" }
        ],
        state(ph) {
          const S = {
            T1: { x: 145, y: 10, op: 1 },
            T2: { x: 430, y: 10, op: 1 },
            T3: { x: 735, y: 10, op: 1 }
          };
          S.M = { x: 310, y: ph >= 1 ? 130 : src.M[1], op: ph >= 1 ? (ph >= 2 ? 0.4 : 1) : 0 };
          S.N = { x: 660, y: ph >= 1 ? 130 : src.N[1], op: ph >= 1 ? (ph >= 2 ? 0.4 : 1) : 0 };
          S.W = { x: 480, y: ph >= 2 ? 255 : src.W[1], op: ph >= 2 ? (ph >= 3 ? 0.35 : 1) : 0, pop: ph === 2 ? 1 : 0 };
          S.V = { x: 480, y: 390, op: ph >= 3 ? 1 : 0, pop: ph >= 3 ? 1 : 0 };
          return S;
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T2", b: "M", col: CY }, { a: "T3", b: "N", col: PK });
          if (ph === 2) L.push({ a: "M", b: "W", col: CY }, { a: "N", b: "W", col: PK });
          return L;
        },
        fx: ph => ph === 3 ? "confetti" : ph === 2 ? "spark" : ""
      };
    })()
  };

  return {
    lec: 9,
    hostId: "l9ShortsHost",
    prefix: "l9s",
    title: "숏츠식 판서 미리보기 · 두 곡선과 접선 넓이 (차함수 마법)",
    desc: "제2강 마지막에 예고된 적용 ①(두 곡선 사이의 넓이)과 적용 ②(곡선과 접선 사이의 넓이, 접점 이중근 $m=2$)를 식 조각과 그래프로 확인합니다.",
    nextLinks: [
      { lec: 1, label: "제1강 열기 (넓이의 비 1:n)" },
      { lec: 3, label: "제3강 열기 (변곡접선)" },
      { lec: 2, label: "제2강 열기 (정적분 만능공식)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   2. 제1강 · 다항함수 넓이의 비 (S1 : S2 = 1 : n)
      (제2강·제9강에서 이어서 보기로 안내된 강의)
   ================================================================== */
const L1_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "다항함수 넓이의 비 1 : n", sub: "직사각형 분할 30초 풀이", parts: [
      { say: "다항함수 넓이의 비 일 대 엔 공식, 30초 만에 정리합니다.", cap: "다항함수 넓이의 비 $1:n$ · 30초 풀이" }
    ] },
    { id: "why", type: "list", head: "이 공식을 배우는 이유", parts: [
      { say: "꼭짓점을 지나는 거듭제곱 곡선이 직사각형을 나눌 때, 적분 계산 없이 일 대 엔 비율로 두 넓이를 바로 구합니다.", cap: "외접 직사각형 넓이를 $1:n$ 비율로 즉시 분할" }
    ] },
    { id: "hist", type: "list", head: "공식의 뿌리", parts: [
      { tag: "고대~17세기", say: "포물선의 넓이 비 일 대 이는 아르키메데스가 구적법으로 밝혔고, 일반 거듭제곱은 카발리에리가 확장했습니다.", cap: "아르키메데스 포물선 구적법과 카발리에리의 거듭제곱 적분" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기", parts: [
      { say: "엑스의 엔 제곱을 영에서 에이까지 적분하면, 엔 더하기 일분의 일 곱하기 에이의 엔 더하기 일 제곱입니다.", cap: "곡선 아래 넓이 $S_{1}=\\dfrac{1}{n+1}\\,a^{n+1}$" },
      { say: "전체 직사각형 넓이는 가로 에이 곱하기 세로 에이의 엔 제곱, 즉 에이의 엔 더하기 일 제곱입니다.", cap: "직사각형 넓이 $=a\\cdot a^{n}=a^{n+1}$" },
      { say: "직사각형에서 아래 넓이를 빼면, 곡선 위 넓이는 엔 더하기 일분의 엔 곱하기 에이의 엔 더하기 일 제곱이 됩니다.", cap: "곡선 위 넓이 $S_{2}=\\dfrac{n}{n+1}\\,a^{n+1}$" },
      { say: "따라서 아래 넓이 대 위 넓이의 비는 항상 일 대 엔입니다.", cap: "넓이의 비 $S_{1}:S_{2}=1:n$" }
    ] },
    { id: "ex", type: "chips", head: "예제", parts: [
      { say: "예를 들어 와이는 엑스 제곱에서 엑스가 삼일 때 직사각형 넓이는 삼 곱하기 구, 이십칠입니다.", cap: "직사각형 넓이 $=3\\times 9=27$" },
      { say: "차수가 이이므로 아래 넓이와 위 넓이의 비는 일 대 이입니다.", cap: "차수 $n=2\\ \\Rightarrow\\ S_{1}:S_{2}=1:2$" },
      { say: "전체 이십칠을 세 조각으로 나누면 아래 넓이는 구, 위 넓이는 십팔입니다.", cap: "$S_{1}=9,\\ S_{2}=18$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 곡선 에이 엑스 세제곱 위의 점 이 콤마 팔 에이에서 만든 직사각형 중, 곡선 위쪽 넓이가 이십사일 때 양수 에이는 얼마일까요?", cap: "곡선 위쪽 넓이 $S_{2}=24$ 일 때 $a$ 의 값 구하기 (자작 문항)" },
      { say: "삼차항이므로 아래 대 위 넓이 비는 일 대 삼이고, 위쪽이 이십사이므로 아래쪽 넓이는 팔입니다.", cap: "$S_{1}:S_{2}=1:3\\ \\Rightarrow\\ S_{1}=8$" },
      { say: "전체 직사각형 넓이는 팔 더하기 이십사, 삼십이입니다.", cap: "직사각형 전체 넓이 $S_{1}+S_{2}=32$" },
      { say: "가로 이 곱하기 세로 팔 에이가 삼십이이므로 에이는 이입니다.", cap: "$16a=32\\ \\Rightarrow\\ a=2$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 꼭짓점에서 축에 수선을 내려 외접 직사각형 넓이부터 구합니다.", cap: "① 외접 직사각형 넓이 $=(\\text{가로})\\times(\\text{세로})$" },
      { say: "둘째, 차수가 엔이면 전체를 엔 더하기 일 등분하여 일 대 엔으로 나눕니다.", cap: "② $S_{1}=\\dfrac{1}{n+1}\\,S_{\\text{직사각형}},\\ S_{2}=\\dfrac{n}{n+1}\\,S_{\\text{직사각형}}$" },
      { say: "셋째, 평행이동한 곡선도 꼭짓점을 기준으로 직사각형을 잡으면 비율은 똑같습니다.", cap: "③ $y=a(x-p)^{n}+q$ 도 꼭짓점 $(p,q)$ 기준 $1:n$" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "다음은 삼차함수의 대칭 중심인 변곡점과 변곡접선 정리입니다.", cap: "제3강 · 변곡접선과 삼중근, 접선의 개수 영역 판별" },
      { tag: "연계 ②", say: "다항함수 극값 위치를 내분점으로 바로 찾는 엠 대 엔 비율관계도 이어서 보세요.", cap: "제4강 · 다항함수 비율관계 ($m:n$ 내분점 공식)" },
      { tag: "이 사이트", say: "이 사이트의 제삼십삼강과 제삼십팔강을 이어서 보세요.", cap: "제33강 · 정적분의 본질(넓이 vs 함숫값)  /  제38강 · 적분은 왜 직사각형부터" }
    ] }
  ];

  const G_EX = {
    f: x => (x * x) / 3, GY0: 410, GV: 110, xr: [0, 3.05], area: [0, 3], ytop: 45, ybot: 445, labelY: 448, boxX: 3,
    r1: { x: 0, col: CY, label: "원점 (0, 0)" }, r2: { x: 3, col: PK, label: "x = 3 (높이 9)" },
    fn: { t: "y = x²  (직사각형 넓이 3×9 = 27)", x: 520, y: 72 }, sPos: [560, 335], sOpenTxt: "S₁ : S₂ = 1 : 2", finalS: "S₁ = 9 · S₂ = 18", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => (x * x * x) / 2.6, GY0: 410, GV: 105, xr: [0, 2.05], area: [0, 2], ytop: 45, ybot: 445, labelY: 448, gux: 340, boxX: 2,
    r1: { x: 0, col: CY, label: "원점 (0, 0)" }, r2: { x: 2, col: PK, label: "점 (2, 8a)" },
    fn: { t: "y = a·x³  (S₁ : S₂ = 1 : 3)", x: 510, y: 72 }, sPos: [540, 340], sOpenTxt: "S₂ = 24", finalS: "a = 2 (S₁=8, S₂=24)", finalPh: 3, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => {
      const src = { S1: [420, 40], Box: [480, 170], S2: [480, 170], R: [480, 300] };
      return {
        chips: [
          { id: "T1", tex: "\\displaystyle\\int_{0}^{a}x^{n}\\,dx", cls: "pl" },
          { id: "S1", tex: "S_{1}=\\dfrac{1}{n+1}\\,a^{n+1}", cls: "cy" },
          { id: "Box", tex: "S_{\\text{직사각형}}=a\\cdot a^{n}=a^{n+1}", cls: "go" },
          { id: "S2", tex: "S_{2}=\\dfrac{n}{n+1}\\,a^{n+1}", cls: "pk" },
          { id: "R", tex: "S_{1}:S_{2}=1:n", cls: "go big" }
        ],
        state(ph) {
          return {
            T1: { x: 230, y: 40, op: 1 },
            S1: { x: ph >= 0 ? 660 : src.S1[0], y: 40, op: 1, pop: ph === 0 ? 1 : 0 },
            Box: { x: 480, y: ph >= 1 ? 185 : src.Box[1], op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
            S2: { x: 480, y: ph >= 2 ? 320 : src.S2[1], op: ph >= 2 ? 1 : 0, pop: ph === 2 ? 1 : 0 },
            R: { x: 480, y: 475, op: ph >= 3 ? 1 : 0, pop: ph >= 3 ? 1 : 0 }
          };
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "S1", b: "Box", col: CY });
          if (ph === 2) L.push({ a: "Box", b: "S2", col: PK, label: "직사각형 − S₁" });
          if (ph === 3) L.push({ a: "S2", b: "R", col: GO, label: "1 : n 비율" });
          return L;
        },
        fx: ph => ph === 3 ? "confetti" : ph >= 1 ? "spark" : ""
      };
    })(),
    ex: (() => {
      return {
        graph: G_EX,
        chips: [
          { id: "T1", tex: "y=x^{2},\\ x\\in[0,3]", cls: "pl" },
          { id: "T2", tex: "S_{\\text{직사각형}}=3\\times 9=27", cls: "go" },
          { id: "M", tex: "n=2\\ \\Rightarrow\\ S_{1}:S_{2}=1:2", cls: "cy" },
          { id: "R", tex: "S_{1}=9,\\quad S_{2}=18", cls: "go big" }
        ],
        state(ph) {
          return {
            T1: { x: 240, y: 15, op: 1 },
            T2: { x: 690, y: 15, op: 1, pop: ph === 0 ? 1 : 0 },
            M: { x: 480, y: 165, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
            R: { x: 480, y: 335, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
          };
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
          if (ph === 2) L.push({ a: "M", b: "R", col: GO, label: "27을 1 : 2 로 분할" });
          return L;
        },
        fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
      };
    })(),
    exam: (() => {
      return {
        graph: G_EXAM,
        chips: [
          { id: "T1", tex: "y=a\\,x^{3}\\ (x=2)", cls: "pl" },
          { id: "T2", tex: "S_{2}=24", cls: "pk" },
          { id: "M", tex: "S_{1}:S_{2}=1:3\\ \\Rightarrow\\ S_{1}=8", cls: "cy" },
          { id: "W", tex: "S_{\\text{직사각형}}=8+24=32", cls: "go" },
          { id: "V", tex: "2\\times 8a=32\\ \\Rightarrow\\ a=2", cls: "go v" }
        ],
        state(ph) {
          return {
            T1: { x: 280, y: 10, op: 1 },
            T2: { x: 700, y: 10, op: 1 },
            M: { x: 480, y: 130, op: ph >= 1 ? (ph >= 3 ? 0.35 : 1) : 0, pop: ph === 1 ? 1 : 0 },
            W: { x: 480, y: 255, op: ph >= 2 ? (ph >= 3 ? 0.35 : 1) : 0, pop: ph === 2 ? 1 : 0 },
            V: { x: 480, y: 390, op: ph >= 3 ? 1 : 0, pop: ph >= 3 ? 1 : 0 }
          };
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T2", b: "M", col: CY });
          if (ph === 2) L.push({ a: "M", b: "W", col: GO });
          if (ph === 3) L.push({ a: "W", b: "V", col: PK });
          return L;
        },
        fx: ph => ph === 3 ? "confetti" : ph >= 1 ? "spark" : ""
      };
    })()
  };

  return {
    lec: 1,
    hostId: "l1ShortsHost",
    prefix: "l1s",
    title: "숏츠식 판서 미리보기 · 다항함수 넓이의 비 (1 : n)",
    desc: "제2강·제9강에서 이어지는 다항함수 넓이의 비 $S_{1}:S_{2}=1:n$ 공식을 외접 직사각형 분할 그래프와 식 조각으로 확인합니다.",
    nextLinks: [
      { lec: 33, label: "제33강 열기 (정적분의 본질)" },
      { lec: 38, label: "제38강 열기 (리만 직사각형)" },
      { lec: 3, label: "제3강 열기 (변곡접선)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   3. 제3강 · 변곡접선 정리하기
      (제1강·제9강 마지막에 이어서 보기로 안내된 강의)
   ================================================================== */
const L3_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "삼차함수 변곡접선 정리", sub: "삼중근과 접선 개수 30초 풀이", parts: [
      { say: "삼차함수의 변곡접선과 접선 개수 판별, 30초 만에 정리합니다.", cap: "삼차함수 변곡접선 · 30초 핵심 정리" }
    ] },
    { id: "why", type: "list", head: "변곡접선을 배우는 이유", parts: [
      { say: "삼차함수 그래프의 대칭 중심인 변곡점에서 그은 접선은 곡선을 뚫고 지나가며, 외부 점에서 그을 수 있는 접선 개수의 경계선이 됩니다.", cap: "곡선을 관통하는 유일한 접선 · 접선 개수의 경계선" }
    ] },
    { id: "hist", type: "list", head: "개념의 뿌리", parts: [
      { tag: "17세기", say: "곡선의 오목과 볼록이 바뀌는 변곡점 조건은 라이프니츠와 베르누이의 미적분 연구에서 체계화되었습니다.", cap: "이계도함수 부호가 바뀌는 대칭 중심" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기 · 대수적 삼중근", parts: [
      { say: "삼차함수 에프 엑스와 변곡접선 지 엑스를 빼면, 변곡점 알파에서 일차항과 이차항이 모두 사라집니다.", cap: "변곡점 $x=\\alpha$ 에서 $f(\\alpha)=g(\\alpha),\\ f'(\\alpha)=g'(\\alpha),\\ f''(\\alpha)=0$" },
      { say: "따라서 차함수 에프 엑스 빼기 지 엑스는 에이 곱하기 엑스 빼기 알파의 세제곱, 삼중근이 됩니다.", cap: "차함수 $f(x)-g(x)=a(x-\\alpha)^{3}$ (삼중근)" },
      { say: "접하면서도 곡선을 뚫고 지나가는 직선은 삼차함수에서 변곡접선뿐입니다.", cap: "접하면서 관통 $\\Longleftrightarrow$ 삼중근 $\\Longleftrightarrow$ 변곡접선" }
    ] },
    { id: "ex", type: "chips", head: "예제 · 영역별 접선의 개수", parts: [
      { say: "삼차곡선과 변곡접선은 평면을 네 영역으로 나눕니다. 오목과 볼록 안쪽 영역에서는 접선을 한 개만 그을 수 있습니다.", cap: "곡선 안쪽 영역 · 접선 $1$개" },
      { say: "삼차곡선과 변곡접선 사이의 쐐기 모양 영역에서는 접선을 세 개 그을 수 있습니다.", cap: "곡선과 변곡접선 사이 영역 · 접선 $3$개" },
      { say: "경계선인 곡선 위나 변곡접선 위의 점에서는 변곡점을 제외하면 접선을 두 개 그을 수 있습니다.", cap: "경계선 위(변곡점 제외) · 접선 $2$개" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 곡선 와이는 엑스 세제곱 빼기 삼 엑스 위의 점 일 콤마 마이너스 이가 변곡점일 때, 변곡접선의 와이절편은 얼마일까요?", cap: "곡선 $y=x^{3}-3x^{2}+2$ 의 변곡접선 $y$절편 구하기 (자작 문항)" },
      { say: "변곡점 엑스는 일이고, 미분계수는 삼 빼기 육, 마이너스 삼입니다.", cap: "변곡점 $(1, 0)$ · 기울기 $f'(1)=-3$" },
      { say: "따라서 변곡접선은 와이는 마이너스 삼 엑스 더하기 삼이고, 와이절편은 삼입니다.", cap: "변곡접선 $y=-3(x-1)=-3x+3\\ \\Rightarrow\\ y\\text{절편 } 3$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 삼차함수와 접선이 스치지 않고 뚫고 지나가면 무조건 변곡접선입니다.", cap: "① 접하며 관통 $=$ 삼중근 $(x-\\alpha)^{3}$" },
      { say: "둘째, 접선이 두 개 그어지는 점은 삼차곡선 위 아니면 변곡접선 위에 있습니다.", cap: "② 접선 $2$개 $\\Rightarrow$ 곡선 위 또는 변곡접선 위" },
      { say: "셋째, 삼차함수는 언제나 변곡점에 대하여 점대칭입니다.", cap: "③ 변곡점 $(\\alpha, f(\\alpha))$ 대칭: $f(\\alpha+x)+f(\\alpha-x)=2f(\\alpha)$" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "다음은 다항함수 비율관계의 핵심인 엠 대 엔 내분점 공식입니다.", cap: "제4강 · 다항함수 비율관계 ($m:n$ 내분점 공식)" },
      { tag: "연계 ②", say: "정적분 넓이 만능 공식과 차함수 넓이 공식도 함께 복습해 보세요.", cap: "제2강 · 정적분 넓이 만능 공식  /  제9강 · 차함수의 마법" },
      { tag: "이 사이트", say: "이 사이트의 제사강과 제이강을 이어서 보세요.", cap: "제4강 · 다항함수 비율관계  /  제2강 · 정적분 넓이 만능 공식" }
    ] }
  ];

  const G_EX = {
    f: x => 0.35 * (x - 1.5) * (x - 1.5) * (x - 1.5), GY0: 250, GV: 90, xr: [-0.2, 3.2], area: [0.2, 2.8], ytop: 40, ybot: 445, labelY: 448,
    r1: { x: 1.5, col: GO, label: "변곡점 α (삼중근 m=3)" }, r2: { x: 2.7, col: CY, label: "사이 영역: 접선 3개" },
    fn: { t: "f(x) − g(x) = a(x − α)³ (관통 접선)", x: 520, y: 78 }, sPos: [300, 165], sOpenTxt: "관통 삼중근", finalS: "안쪽 1개 · 경계 2개 · 사이 3개", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => 0.45 * (x * x * x - 3 * x * x + 2), GY0: 250, GV: 90, xr: [-0.6, 2.6], area: [0, 2], ytop: 40, ybot: 445, labelY: 448, gx0: 280, gux: 200,
    r1: { x: 1, col: CY, label: "변곡점 (1, 0)" }, r2: { x: 0, col: PK, label: "y절편 (0, 3)" },
    fn: { t: "y = x³ − 3x² + 2  /  변곡접선 y = −3x + 3", x: 500, y: 78 }, sPos: [560, 175], sOpenTxt: "f'(1) = −3", finalS: "y = −3x + 3 → y절편 3", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => {
      return {
        chips: [
          { id: "T1", tex: "f(\\alpha)=g(\\alpha),\\ f'(\\alpha)=g'(\\alpha),\\ f''(\\alpha)=0", cls: "cy sm" },
          { id: "T2", tex: "f(x)-g(x)=a(x-\\alpha)^{3}", cls: "go big" },
          { id: "T3", tex: "\\text{접하면서 관통}\\ \\Longleftrightarrow\\ \\text{삼중근 }(m=3)", cls: "pk" }
        ],
        state(ph) {
          return {
            T1: { x: 480, y: 70, op: 1, pop: ph === 0 ? 1 : 0 },
            T2: { x: 480, y: 245, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
            T3: { x: 480, y: 430, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
          };
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T1", b: "T2", col: CY, label: "일차·이차항 소거" });
          if (ph === 2) L.push({ a: "T2", b: "T3", col: GO, label: "부호 반전 → 관통" });
          return L;
        },
        fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
      };
    })(),
    ex: (() => {
      return {
        graph: G_EX,
        chips: [
          { id: "C1", tex: "\\text{곡선 안쪽 영역}:\\ \\text{접선 }1\\text{개}", cls: "cy" },
          { id: "C2", tex: "\\text{곡선과 변곡접선 사이}:\\ \\text{접선 }3\\text{개}", cls: "go" },
          { id: "C3", tex: "\\text{곡선·변곡접선 위(변곡점 제외)}:\\ \\text{접선 }2\\text{개}", cls: "pk sm" }
        ],
        state(ph) {
          return {
            C1: { x: 480, y: 40, op: 1, pop: ph === 0 ? 1 : 0 },
            C2: { x: 480, y: 190, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
            C3: { x: 480, y: 345, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
          };
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "C1", b: "C2", col: GO });
          if (ph === 2) L.push({ a: "C2", b: "C3", col: PK });
          return L;
        },
        fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
      };
    })(),
    exam: (() => {
      return {
        graph: G_EXAM,
        chips: [
          { id: "T1", tex: "f(x)=x^{3}-3x^{2}+2,\\quad f''(x)=6x-6=0", cls: "cy sm" },
          { id: "M", tex: "\\text{변곡점 }(1,0),\\quad f'(1)=3-6=-3", cls: "pk" },
          { id: "V", tex: "y=-3(x-1)=-3x+3\\ \\Rightarrow\\ y\\text{절편}=3", cls: "go v" }
        ],
        state(ph) {
          return {
            T1: { x: 480, y: 35, op: 1, pop: ph === 0 ? 1 : 0 },
            M: { x: 480, y: 190, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
            V: { x: 480, y: 355, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
          };
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
          if (ph === 2) L.push({ a: "M", b: "V", col: GO });
          return L;
        },
        fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
      };
    })()
  };

  return {
    lec: 3,
    hostId: "l3ShortsHost",
    prefix: "l3s",
    title: "숏츠식 판서 미리보기 · 변곡접선 정리하기",
    desc: "삼차함수 변곡접선의 대수적 삼중근 $(x-\\alpha)^{3}$ 성질과 영역별 접선 개수 판별법을 그래프로 확인합니다.",
    nextLinks: [
      { lec: 4, label: "제4강 열기 (m:n 내분점)" },
      { lec: 2, label: "제2강 열기 (정적분 만능공식)" },
      { lec: 9, label: "제9강 열기 (차함수의 마법)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   4. 제4강 · 다항함수 비율관계 (m : n 내분점)
   ================================================================== */
const L4_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "다항함수 m : n 내분점 공식", sub: "극값 위치 30초 풀이", parts: [
      { say: "다항함수 극값 위치를 바로 찾는 엠 대 엔 내분점 공식, 30초 만에 정리합니다.", cap: "다항함수 비율관계 $m:n$ 내분점 · 30초 풀이" }
    ] },
    { id: "why", type: "list", head: "이 공식을 배우는 이유", parts: [
      { say: "이차함수의 일 대 일, 삼차함수의 이 대 일, 사차함수의 삼 대 일을 따로 외우지 않고 지수 비 엠 대 엔 하나로 통합합니다.", cap: "$1:1,\\ 2:1,\\ 3:1$ 을 지수 비 $m:n$ 하나로 통합" }
    ] },
    { id: "hist", type: "list", head: "공식의 뿌리", parts: [
      { tag: "17세기", say: "두 근 사이에서 미분계수가 영인 점이 존재한다는 롤의 정리와 곱의 미분법에서 바로 유도됩니다.", cap: "롤의 정리와 곱의 미분법으로 유도" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기", parts: [
      { say: "엑스 빼기 에이의 엠 제곱 곱하기 엑스 빼기 비의 엔 제곱을 미분해 영이 되는 극값 위치 씨를 찾습니다.", cap: "$f(x)=p(x-a)^{m}(x-b)^{n}$ 의 극값 위치 $c$" },
      { say: "곱의 미분법으로 묶어 정리하면 씨 빼기 에이 대 비 빼기 씨의 거리 비가 정확히 엠 대 엔이 됩니다.", cap: "$(c-a):(b-c)=m:n$" },
      { say: "즉 극값 위치 씨는 두 근 에이와 비를 엠 대 엔으로 내분하는 점입니다.", cap: "내분점 $c=\\dfrac{mb+na}{m+n}$" }
    ] },
    { id: "ex", type: "chips", head: "예제", parts: [
      { say: "삼차함수 엑스 빼기 일의 제곱 곱하기 엑스 빼기 사는 일에서 이중근, 사에서 단일근입니다.", cap: "$a=1\\ (m=2),\\quad b=4\\ (n=1)$" },
      { say: "지수 비가 이 대 일이므로 일에서 사까지 거리 삼을 이 대 일로 내분하면 극소점 엑스는 삼입니다.", cap: "$1$과 $4$의 $2:1$ 내분점 $\\Rightarrow\\ c=3$" },
      { say: "만능 넓이 공식과 결합하면 두 근과 극값을 미분 없이 한 번에 읽을 수 있습니다.", cap: "극값 $c=3,\\ f(3)=(2)^{2}(-1)=-4$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 사차함수 엑스 빼기 이의 세제곱 곱하기 엑스 빼기 케이가 엑스는 팔에서 극솟값을 가질 때, 상수 케이는 얼마일까요?", cap: "$f(x)=(x-2)^{3}(x-k)$ 가 $x=8$ 에서 극소일 때 $k$ 구하기 (자작 문항)" },
      { say: "이에서 삼중근, 케이에서 단일근이므로 극소점 팔은 이와 케이를 삼 대 일로 내분하는 점입니다.", cap: "$m=3,\\ n=1\\ \\Rightarrow\\ 3:1$ 내분점이 $x=8$" },
      { say: "이에서 팔까지 거리가 육이므로, 삼 대 일 비율에서 팔부터 케이까지 거리는 이가 되어 케이는 십입니다.", cap: "$8-2=6\\ (3\\text{칸})\\ \\Rightarrow\\ k-8=2\\ (1\\text{칸})\\ \\Rightarrow\\ k=10$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 두 인수의 지수 엠과 엔이 그대로 내분 비율 엠 대 엔이 됩니다.", cap: "① 지수 $(m, n)\\ \\Rightarrow$ 거리 비 $m:n$" },
      { say: "둘째, 삼차함수 접점과 교점 사이는 언제나 이 대 일입니다.", cap: "② 삼차함수 접점($m=2$)과 교점($n=1$) $\\Rightarrow\\ 2:1$" },
      { say: "셋째, 사차함수 삼중근과 단일근 사이는 언제나 삼 대 일입니다.", cap: "③ 사차함수 삼중근($m=3$)과 단일근($n=1$) $\\Rightarrow\\ 3:1$" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "같은 지수 엠과 엔을 그대로 적분 넓이에 쓰는 정적분 넓이 만능 공식과 함께 보세요.", cap: "제2강 · 정적분 넓이 만능 공식 $\\dfrac{m!\\,n!}{(m+n+1)!}(\\beta-\\alpha)^{m+n+1}$" },
      { tag: "연계 ②", say: "두 곡선과 접선 넓이를 차함수로 묶는 제구강도 이어서 복습해 보세요.", cap: "제9강 · 정적분과 넓이 & 차함수의 마법" },
      { tag: "이 사이트", say: "이 사이트의 제이강과 제구강을 이어서 보세요.", cap: "제2강 · 정적분 넓이 만능 공식  /  제9강 · 차함수의 마법" }
    ] }
  ];

  const G_EX = {
    f: x => -0.35 * (x - 1) * (x - 1) * (4 - x), GY0: 150, GV: 150, xr: [0.5, 4.25], area: [1, 4], ytop: 40, ybot: 445, labelY: 112, gx0: 30, gux: 205,
    r1: { x: 1, col: CY, label: "a=1 (m=2)" }, r2: { x: 4, col: PK, label: "b=4 (n=1)" },
    fn: { t: "f(x) = (x − 1)²(x − 4)", x: 640, y: 95 }, sPos: [645, 395], sOpenTxt: "2 : 1 내분점", finalS: "극소 위치 c = 3", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => -0.012 * Math.pow(x - 2, 3) * (10 - x), GY0: 140, GV: 95, xr: [1.5, 10.4], area: [2, 10], ytop: 40, ybot: 445, labelY: 105, gx0: 10, gux: 86,
    r1: { x: 2, col: CY, label: "x=2 (m=3)" }, r2: { x: 10, col: PK, label: "x=k=10 (n=1)" },
    fn: { t: "f(x) = (x − 2)³(x − k) · 3 : 1 내분점 c = 8", x: 520, y: 85 }, sPos: [698, 415], sOpenTxt: "c = 8 (3 : 1)", finalS: "c = 8 → k = 10", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => {
      return {
        chips: [
          { id: "T1", tex: "f(x)=p", cls: "pl" },
          { id: "T2", tex: `(x-a)^{${cl(CY, "m")}}`, cls: "cy" },
          { id: "T3", tex: `(x-b)^{${cl(PK, "n")}}`, cls: "pk" },
          { id: "M", tex: "(c-a):(b-c)=m:n", cls: "go" },
          { id: "R", tex: "c=\\dfrac{mb+na}{m+n}", cls: "go big" }
        ],
        state(ph) {
          return {
            T1: { x: 185, y: 40, op: 1 },
            T2: { x: 455, y: 40, op: 1 },
            T3: { x: 745, y: 40, op: 1 },
            M: { x: 480, y: 215, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
            R: { x: 480, y: 395, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
          };
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T2", b: "M", col: CY }, { a: "T3", b: "M", col: PK, label: "f'(c) = 0" });
          if (ph === 2) L.push({ a: "M", b: "R", col: GO, label: "m : n 내분점" });
          return L;
        },
        fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
      };
    })(),
    ex: (() => {
      return {
        graph: G_EX,
        chips: [
          { id: "T1", tex: "f(x)=(x-1)^{2}(x-4)", cls: "cy" },
          { id: "M", tex: "m:n=2:1\\ \\Rightarrow\\ c=\\dfrac{2\\cdot 4+1\\cdot 1}{2+1}=3", cls: "go" },
          { id: "R", tex: "c=3,\\quad f(3)=-4", cls: "go big" }
        ],
        state(ph) {
          return {
            T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
            M: { x: 480, y: 175, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
            R: { x: 480, y: 345, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
          };
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
          if (ph === 2) L.push({ a: "M", b: "R", col: GO });
          return L;
        },
        fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
      };
    })(),
    exam: (() => {
      return {
        graph: G_EXAM,
        chips: [
          { id: "T1", tex: "f(x)=(x-2)^{3}(x-k),\\quad c=8", cls: "cy" },
          { id: "M", tex: "(8-2):(k-8)=3:1", cls: "pk" },
          { id: "V", tex: "6:(k-8)=3:1\\ \\Rightarrow\\ k=10", cls: "go v" }
        ],
        state(ph) {
          return {
            T1: { x: 480, y: 25, op: 1, pop: ph === 0 ? 1 : 0 },
            M: { x: 480, y: 185, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
            V: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
          };
        },
        links(ph) {
          const L = [];
          if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
          if (ph === 2) L.push({ a: "M", b: "V", col: GO });
          return L;
        },
        fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
      };
    })()
  };

  return {
    lec: 4,
    hostId: "l4ShortsHost",
    prefix: "l4s",
    title: "숏츠식 판서 미리보기 · 다항함수 비율관계 (m : n 내분점)",
    desc: "다항함수 $f(x)=p(x-a)^{m}(x-b)^{n}$ 의 극값 위치 $c$ 를 $m:n$ 내분점 공식 한 줄로 찾는 과정을 확인합니다.",
    nextLinks: [
      { lec: 37, label: "제37강 열기 (삼차 비율·높이차)" },
      { lec: 36, label: "제36강 열기 (거리곱 공식)" },
      { lec: 27, label: "제27강 열기 (인수와 대칭)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   5. 제33강 · 정적분의 본질 (넓이 vs 함숫값 변화량)
      (적분·넓이 사슬: 제1강 → 제33강 → 제38강 → 제39강)
   ================================================================== */
const L33_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "정적분의 본질 · 넓이와 높이 차", sub: "도함수 넓이 = 원시함수 변화량", parts: [
      { say: "도함수의 정적분 넓이가 왜 원시함수의 높이 변화량이 되는지 30초 만에 정리합니다.", cap: "도함수 넓이 $=$ 원시함수 높이 변화량" }
    ] },
    { id: "why", type: "list", head: "이 원리를 배우는 이유", parts: [
      { say: "도함수 그래프와 엑스축 사이의 넓이를 알면, 적분 계산 없이 원래 함수의 극댓값과 극솟값 차이를 바로 구할 수 있습니다.", cap: "도함수 둘러싸인 넓이 $S = |g(\\beta)-g(\\alpha)|$" }
    ] },
    { id: "hist", type: "list", head: "원리의 뿌리", parts: [
      { tag: "17세기", say: "순간 변화율의 합이 전체 변화량과 같다는 미적분학의 기본정리는 뉴턴과 라이프니츠가 확립했습니다.", cap: "미적분학의 기본정리 · 미분과 적분의 역연산" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기", parts: [
      { say: "지 프라임 엑스가 에프 엑스일 때, 에프 티를 에이에서 비까지 정적분합니다.", cap: "$g'(x)=f(x)$ 일 때 $\\displaystyle\\int_{a}^{b}f(t)\\,dt$" },
      { say: "미적분학의 기본정리에 의해 이 정적분 값은 지 비 빼기 지 에이, 즉 원시함수의 함숫값 변화량이 됩니다.", cap: "$\\displaystyle\\int_{a}^{b}f(t)\\,dt=g(b)-g(a)$" },
      { say: "따라서 도함수가 영이 되는 두 근 알파와 베타 사이의 넓이는 원시함수의 극댓값과 극솟값의 높이 차와 같습니다.", cap: "도함수 넓이 $S=|g(\\beta)-g(\\alpha)|$ (극대·극소 높이 차)" }
    ] },
    { id: "ex", type: "chips", head: "예제", parts: [
      { say: "예를 들어 도함수 에프 엑스가 삼 곱하기 엑스 빼기 일 곱하기 엑스 빼기 삼일 때, 일에서 삼까지 둘러싸인 넓이를 구해 봅시다.", cap: "$g'(x)=3(x-1)(x-3)$" },
      { say: "이차함수 넓이 공식 육분의 일 곱하기 삼 곱하기 이의 세제곱으로 계산하면 넓이는 사입니다.", cap: "도함수 넓이 $S=\\dfrac{3}{6}(3-1)^{3}=4$" },
      { say: "도함수가 엑스축 아래에 있으므로 원시함수 지 엑스는 일에서 삼까지 정확히 사만큼 내려갑니다.", cap: "$g(3)-g(1)=-4\\ \\Rightarrow\\ \\text{극대·극소 차 }=4$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 삼차함수 지 엑스의 도함수가 에이 엑스 곱하기 엑스 빼기 삼이고, 지 영이 십, 극솟값 지 삼이 일일 때 양수 에이는 얼마일까요?", cap: "$g'(x)=a\\,x(x-3),\\ g(0)=10,\\ g(3)=1$ 일 때 $a$ 구하기 (자작 문항)" },
      { say: "극댓값과 극솟값의 높이 차가 십 빼기 일, 구이므로 도함수가 영에서 삼까지 이루는 넓이도 구입니다.", cap: "높이 차 $g(0)-g(3)=9\\ \\Rightarrow\\ \\text{도함수 넓이 }S=9$" },
      { say: "육분의 에이 곱하기 삼의 세제곱이 구이므로 에이는 이입니다.", cap: "$\\dfrac{a}{6}\\times 27=9\\ \\Rightarrow\\ a=2$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 도함수가 양수이면 원시함수는 올라가고 음수이면 내려갑니다.", cap: "① $g'(x)\\gt 0$ 증가 · $g'(x)\\lt 0$ 감소" },
      { say: "둘째, 도함수의 정적분 넓이는 원시함수의 높이 변화량입니다.", cap: "② 도함수 넓이 $S = |\\Delta g|$ (높이 변화량)" },
      { say: "셋째, 정적분 넓이 공식과 결합하면 삼차·사차함수의 극값 차이를 한 줄로 구합니다.", cap: "③ 삼차 극값 차 $=\\dfrac{|a|}{6}(\\beta-\\alpha)^{3}$ (도함수 계수 $a$ 기준)" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "다음은 적분이 왜 직사각형의 합에서 출발하는지 리만 합의 본질을 알아봅니다.", cap: "제38강 · 적분은 왜 직사각형부터 시작할까?" },
      { tag: "연계 ②", say: "구분구적법으로 원뿔의 부피 공식 삼분의 일을 증명하는 제삼십구강도 이어서 보세요.", cap: "제39강 · 원뿔의 부피와 구분구적법 ($\\dfrac{1}{3}\\pi r^{2}h$)" },
      { tag: "이 사이트", say: "이 사이트의 제삼십팔강과 제삼십구강을 이어서 보세요.", cap: "제38강 · 리만 합과 적분의 본질  /  제39강 · 원뿔의 부피와 구분구적법" }
    ] }
  ];

  const G_EX = {
    f: x => -0.75 * (x - 1) * (3 - x), GY0: 150, GV: 150, xr: [0.3, 3.5], area: [1, 3], ytop: 40, ybot: 445, labelY: 112, gx0: 60, gux: 220,
    r1: { x: 1, col: CY, label: "x=1 (극대)" }, r2: { x: 3, col: PK, label: "x=3 (극소)" },
    fn: { t: "도함수 g'(x) = 3(x − 1)(x − 3)", x: 520, y: 80 }, sPos: [500, 310], sOpenTxt: "넓이 S = 4", finalS: "g(3) − g(1) = −4", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => -0.5 * x * (3 - x), GY0: 150, GV: 110, xr: [-0.2, 3.3], area: [0, 3], ytop: 40, ybot: 445, labelY: 112, gx0: 90, gux: 230,
    r1: { x: 0, col: CY, label: "0 · g(0)=10" }, r2: { x: 3, col: PK, label: "3 · g(3)=1" },
    fn: { t: "g'(x) = a·x(x − 3)  (넓이 S = 높이차 9)", x: 520, y: 80 }, sPos: [435, 310], sOpenTxt: "S = 9", finalS: "a = 2 (S = 9)", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => ({
      chips: [
        { id: "T1", tex: "g'(x)=f(x)", cls: "cy" },
        { id: "T2", tex: "\\displaystyle\\int_{a}^{b}f(t)\\,dt=g(b)-g(a)", cls: "go" },
        { id: "T3", tex: "\\text{도함수 넓이 }S=|g(\\beta)-g(\\alpha)|", cls: "pk v" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 55, op: 1, pop: ph === 0 ? 1 : 0 },
          T2: { x: 480, y: 225, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          T3: { x: 480, y: 415, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "T2", col: CY, label: "미적분학의 기본정리" });
        if (ph === 2) L.push({ a: "T2", b: "T3", col: GO, label: "넓이 = 높이 변화량" });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    ex: (() => ({
      graph: G_EX,
      chips: [
        { id: "T1", tex: "g'(x)=3(x-1)(x-3)", cls: "cy" },
        { id: "M", tex: "S=\\dfrac{3}{6}(3-1)^{3}=4", cls: "go" },
        { id: "R", tex: "g(3)-g(1)=-4\\ \\Rightarrow\\ |\\Delta g|=4", cls: "pk v" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 25, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 185, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          R: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "R", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    exam: (() => ({
      graph: G_EXAM,
      chips: [
        { id: "T1", tex: "g(0)-g(3)=10-1=9\\ \\Rightarrow\\ S=9", cls: "cy" },
        { id: "M", tex: "S=\\dfrac{a}{6}(3-0)^{3}=\\dfrac{9}{2}\\,a", cls: "go" },
        { id: "V", tex: "\\dfrac{9}{2}\\,a=9\\ \\Rightarrow\\ a=2", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 25, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 185, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          V: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "V", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))()
  };

  return {
    lec: 33,
    hostId: "l33ShortsHost",
    prefix: "l33s",
    title: "숏츠식 판서 미리보기 · 정적분의 본질 (넓이 vs 함숫값 변화량)",
    desc: "도함수의 부호 있는 넓이가 원시함수의 높이 변화량 $\\Delta g = g(b)-g(a)$ 이 되는 원리를 식 조각과 그래프로 확인합니다.",
    nextLinks: [
      { lec: 38, label: "제38강 열기 (리만 직사각형)" },
      { lec: 39, label: "제39강 열기 (원뿔 구분구적법)" },
      { lec: 3, label: "제3강 열기 (변곡접선)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   6. 제38강 · 적분은 왜 직사각형부터 시작할까? (리만 합과 적분의 본질)
   ================================================================== */
const L38_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "적분은 왜 직사각형으로 할까?", sub: "리만 합과 오차 소멸 30초 원리", parts: [
      { say: "곡선 넓이를 구할 때 왜 직사각형부터 시작하는지 리만 합의 본질을 30초 만에 정리합니다.", cap: "리만 합과 직사각형 적분 · 30초 원리" }
    ] },
    { id: "why", type: "list", head: "직사각형을 쓰는 이유", parts: [
      { say: "가로 곱하기 세로로 가장 쉽게 넓이를 구할 수 있고, 잘게 쪼개면 남는 삼각형 모양 오차들의 합이 영으로 사라지기 때문입니다.", cap: "가장 단순한 넓이 공식을 $n\\to\\infty$ 극한으로 확장" }
    ] },
    { id: "hist", type: "list", head: "원리의 뿌리", parts: [
      { tag: "19세기", say: "구간을 잘게 나누어 직사각형 넓이의 극한으로 정적분을 엄밀하게 정의한 사람은 리만입니다.", cap: "리만 합(Riemann Sum)과 정적분의 정의" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기 · 오차 소멸과 변환", parts: [
      { say: "구간을 엔 등분하면 한 직사각형의 가로 길이는 엔분의 피가 됩니다.", cap: "가로 폭 $\\Delta x=\\dfrac{p}{n}\\ \\longrightarrow\\ dx$" },
      { say: "케이번째 높이 에프 에이 더하기 엔분의 피 케이에 가로 폭을 곱해 모두 더합니다.", cap: "리만 합 $\\displaystyle\\sum_{k=1}^{n}f\\!\\left(a+\\dfrac{p}{n}k\\right)\\dfrac{p}{n}$" },
      { say: "엔이 한없이 커지면 오차 총합은 엔분의 일에 비례해 영이 되고, 정적분 기호로 바뀝니다.", cap: "$\\displaystyle\\lim_{n\\to\\infty}\\sum_{k=1}^{n}f\\!\\left(a+\\dfrac{p}{n}k\\right)\\dfrac{p}{n}=\\int_{a}^{a+p}f(x)\\,dx$" }
    ] },
    { id: "ex", type: "chips", head: "예제 · 급수를 정적분으로 바꾸기", parts: [
      { say: "예를 들어 엔분의 케이의 제곱에 엔분의 일을 곱해 일부터 엔까지 더한 극한을 구해 봅시다.", cap: "$\\displaystyle\\lim_{n\\to\\infty}\\sum_{k=1}^{n}\\left(\\dfrac{k}{n}\\right)^{2}\\dfrac{1}{n}$" },
      { say: "엔분의 케이를 엑스로, 엔분의 일을 디엑스로 바꾸면 구간은 영에서 일까지가 됩니다.", cap: "$\\dfrac{k}{n}\\to x,\\quad \\dfrac{1}{n}\\to dx,\\quad [0, 1]$" },
      { say: "엑스 제곱을 영에서 일까지 적분하면 넓이는 삼분의 일입니다.", cap: "$\\displaystyle\\int_{0}^{1}x^{2}\\,dx=\\dfrac{1}{3}$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 일 더하기 엔분의 이 케이의 세제곱에 엔분의 이를 곱해 더한 극한값은 얼마일까요?", cap: "$\\displaystyle\\lim_{n\\to\\infty}\\sum_{k=1}^{n}\\left(1+\\dfrac{2k}{n}\\right)^{3}\\dfrac{2}{n}$ 구하기 (자작 문항)" },
      { say: "일 더하기 엔분의 이 케이를 엑스로 두면 가로 폭 엔분의 이는 디엑스가 되고, 구간은 일에서 삼까지입니다.", cap: "$1+\\dfrac{2k}{n}\\to x,\\quad \\dfrac{2}{n}\\to dx,\\quad [1, 3]$" },
      { say: "엑스 세제곱을 일에서 삼까지 적분하면 사분의 팔십 빼기 일, 이십입니다.", cap: "$\\displaystyle\\int_{1}^{3}x^{3}\\,dx=\\left[\\dfrac{x^{4}}{4}\\right]_{1}^{3}=20$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 엔분의 케이가 들어 있는 식 전체를 엑스로 치환하면 구간이 깔끔해집니다.", cap: "① $a+\\dfrac{p}{n}k \\to x$ 로 통째로 치환하면 구간은 $[a,\\ a+p]$" },
      { say: "둘째, 케이 앞의 계수 엔분의 피가 바로 디엑스가 되는지 맞춥니다.", cap: "② $k$ 의 계수 $\\dfrac{p}{n}$ 이 $dx$ 와 일치하는지 확인" },
      { say: "셋째, 직사각형 오차 합은 엔분의 일에 비례하므로 극한에서 완전히 사라집니다.", cap: "③ 오차 총합 $\\propto \\dfrac{1}{n} \\longrightarrow 0\\ (n\\to\\infty)$" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "다음은 이 구분구적법으로 원뿔의 부피가 왜 기둥의 삼분의 일인지 직접 증명합니다.", cap: "제39강 · 원뿔의 부피와 구분구적법 ($\\dfrac{1}{3}\\pi r^{2}h$)" },
      { tag: "연계 ②", say: "이어서 미분 파트의 핵심인 삼차함수 변곡접선과 비율관계로 넘어갑니다.", cap: "제3강 · 변곡접선 정리하기  /  제4강 · 다항함수 비율관계" },
      { tag: "이 사이트", say: "이 사이트의 제삼십구강과 제삼강을 이어서 보세요.", cap: "제39강 · 원뿔의 부피와 구분구적법  /  제3강 · 변곡접선 정리하기" }
    ] }
  ];

  const G_EX = {
    f: x => x * x * 2.6, GY0: 410, GV: 115, xr: [0, 1.05], area: [0, 1], ytop: 45, ybot: 445, labelY: 448, gux: 680, boxX: 1,
    r1: { x: 0, col: CY, label: "x = 0" }, r2: { x: 1, col: PK, label: "x = 1" },
    fn: { t: "y = x²  (직사각형 리만 합 → 정적분)", x: 460, y: 75 }, sPos: [560, 340], sOpenTxt: "∑ (k/n)²(1/n)", finalS: "∫₀¹ x² dx = 1/3", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => Math.pow(x / 2, 3) * 0.85, GY0: 410, GV: 105, xr: [0, 3.05], area: [1, 3], ytop: 45, ybot: 445, labelY: 448, gux: 240,
    r1: { x: 1, col: CY, label: "a = 1" }, r2: { x: 3, col: PK, label: "a+p = 3" },
    fn: { t: "y = x³  (구간 [1, 3] 리만 합 변환)", x: 490, y: 75 }, sPos: [580, 335], sOpenTxt: "구간 [1, 3]", finalS: "∫₁³ x³ dx = 20", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => ({
      chips: [
        { id: "T1", tex: "\\Delta x=\\dfrac{p}{n}\\ \\longrightarrow\\ dx", cls: "cy" },
        { id: "T2", tex: "\\displaystyle\\sum_{k=1}^{n}f\\!\\left(a+\\dfrac{p}{n}k\\right)\\dfrac{p}{n}", cls: "pk" },
        { id: "T3", tex: "\\displaystyle\\int_{a}^{a+p}f(x)\\,dx", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 50, op: 1, pop: ph === 0 ? 1 : 0 },
          T2: { x: 480, y: 220, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          T3: { x: 480, y: 420, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "T2", col: CY });
        if (ph === 2) L.push({ a: "T2", b: "T3", col: GO, label: "n → ∞ 극한" });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    ex: (() => ({
      graph: G_EX,
      chips: [
        { id: "T1", tex: "\\displaystyle\\lim_{n\\to\\infty}\\sum_{k=1}^{n}\\left(\\dfrac{k}{n}\\right)^{2}\\dfrac{1}{n}", cls: "cy sm" },
        { id: "M", tex: "\\dfrac{k}{n}\\to x,\\quad \\dfrac{1}{n}\\to dx", cls: "pk" },
        { id: "R", tex: "\\displaystyle\\int_{0}^{1}x^{2}\\,dx=\\dfrac{1}{3}", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 15, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 185, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          R: { x: 480, y: 340, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "R", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    exam: (() => ({
      graph: G_EXAM,
      chips: [
        { id: "T1", tex: "1+\\dfrac{2k}{n}\\to x,\\quad \\dfrac{2}{n}\\to dx,\\quad x\\in[1,3]", cls: "cy sm" },
        { id: "M", tex: "\\displaystyle\\int_{1}^{3}x^{3}\\,dx=\\left[\\dfrac{x^{4}}{4}\\right]_{1}^{3}", cls: "pk" },
        { id: "V", tex: "\\dfrac{81-1}{4}=20", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          V: { x: 480, y: 355, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "V", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))()
  };

  return {
    lec: 38,
    hostId: "l38ShortsHost",
    prefix: "l38s",
    title: "숏츠식 판서 미리보기 · 적분은 왜 직사각형부터 시작할까?",
    desc: "리만 합에서 직사각형 오차가 사라지는 이유와 정적분 변환 공식을 식 조각과 그래프로 확인합니다.",
    nextLinks: [
      { lec: 39, label: "제39강 열기 (원뿔 구분구적법)" },
      { lec: 3, label: "제3강 열기 (변곡접선)" },
      { lec: 33, label: "제33강 열기 (정적분의 본질)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   7. 제39강 · 원뿔의 부피와 구분구적법 (V = 1/3 π r² h)
   ================================================================== */
const L39_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "원뿔 부피는 왜 기둥의 1/3 일까?", sub: "구분구적법 30초 증명", parts: [
      { say: "원뿔의 부피가 왜 원기둥의 삼분의 일인지 구분구적법으로 30초 만에 증명합니다.", cap: "원뿔 부피 $\\dfrac{1}{3}\\pi r^{2}h$ · 구분구적법 증명" }
    ] },
    { id: "why", type: "list", head: "이 증명을 배우는 이유", parts: [
      { say: "단면의 넓이가 높이의 제곱에 비례하는 모든 뿔의 부피가 왜 삼분의 일인지 근본 원리를 이해할 수 있습니다.", cap: "단면 넓이 $\\propto x^{2}$ 적분 $\\Rightarrow\\ \\dfrac{1}{3}$ 의 탄생" }
    ] },
    { id: "hist", type: "list", head: "증명의 뿌리", parts: [
      { tag: "고대 그리스", say: "원뿔과 구의 부피 비를 처음 발견한 사람은 에우독소스와 아르키메데스이며, 오늘날에는 구분구적법으로 증명합니다.", cap: "에우독소스·아르키메데스의 착진법과 구분구적법" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기 · 1/3 의 탄생", parts: [
      { say: "높이 에이치를 엔 등분하면 케이번째 원기둥 조각의 반지름은 닮음비에 의해 엔분의 케이 알이 됩니다.", cap: "$k$번째 반지름 $r_{k}=\\dfrac{k}{n}\\,r$, 두께 $\\Delta h=\\dfrac{h}{n}$" },
      { say: "조각들의 부피를 모두 더하면 엔 세제곱분의 파이 알 제곱 에이치 곱하기 케이 제곱의 합이 됩니다.", cap: "$V_{n}=\\dfrac{\\pi r^{2}h}{n^{3}}\\displaystyle\\sum_{k=1}^{n}k^{2}=\\dfrac{\\pi r^{2}h}{n^{3}}\\cdot\\dfrac{n(n+1)(2n+1)}{6}$" },
      { say: "엔을 무한대로 보내면 최고차항 계수 비 육분의 이, 즉 삼분의 일 파이 알 제곱 에이치가 됩니다.", cap: "$V=\\dfrac{2}{6}\\pi r^{2}h=\\dfrac{1}{3}\\pi r^{2}h$" }
    ] },
    { id: "ex", type: "chips", head: "예제", parts: [
      { say: "밑면 반지름이 삼이고 높이가 사인 원뿔의 부피를 구해 봅시다.", cap: "반지름 $r=3$, 높이 $h=4$" },
      { say: "원기둥 부피는 파이 곱하기 삼의 제곱 곱하기 사, 삼십육 파이입니다.", cap: "원기둥 부피 $=\\pi\\times 3^{2}\\times 4=36\\pi$" },
      { say: "여기에 삼분의 일을 곱하면 원뿔의 부피는 십이 파이입니다.", cap: "원뿔 부피 $=\\dfrac{1}{3}\\times 36\\pi=12\\pi$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 높이가 육인 정사각뿔을 꼭짓점으로부터 거리가 엑스인 평면으로 자른 단면 넓이가 엑스 제곱일 때, 이 뿔의 부피는 얼마일까요?", cap: "단면 넓이 $S(x)=x^{2}$, 높이 $6$ 인 뿔의 부피 구하기 (자작 문항)" },
      { say: "단면 넓이 엑스 제곱을 영에서 육까지 정적분하면 부피가 됩니다.", cap: "$V=\\displaystyle\\int_{0}^{6}x^{2}\\,dx=\\left[\\dfrac{x^{3}}{3}\\right]_{0}^{6}$" },
      { say: "삼분의 이백십육이므로 부피는 칠십이입니다.", cap: "$V=\\dfrac{216}{3}=72$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 꼭짓점에서 거리가 엑스인 단면의 닮음비는 에이치분의 엑스입니다.", cap: "① 길이 닮음비 $=\\dfrac{x}{h}\\ \\Rightarrow\\ $ 넓이 비 $=\\left(\\dfrac{x}{h}\\right)^{2}$" },
      { say: "둘째, 엑스 제곱을 적분하면 삼분의 일 엑스 세제곱이 되므로 모든 뿔의 부피에는 삼분의 일이 붙습니다.", cap: "② $\\displaystyle\\int_{0}^{h}\\left(\\dfrac{x}{h}\\right)^{2}dx=\\dfrac{1}{3}\\,h$" },
      { say: "셋째, 케이 제곱의 합 공식에서 최고차항 계수는 육분의 이, 즉 삼분의 일입니다.", cap: "③ $\\displaystyle\\lim_{n\\to\\infty}\\dfrac{1}{n^{3}}\\sum_{k=1}^{n}k^{2}=\\dfrac{2}{6}=\\dfrac{1}{3}$" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "적분과 넓이 편을 마쳤으니, 이제 미분과 그래프 비율의 핵심인 제삼강 변곡접선으로 이어집니다.", cap: "제3강 · 변곡접선 정리하기 (삼중근과 접선 개수)" },
      { tag: "연계 ②", say: "다항함수 극값 위치를 내분점으로 구하는 제사강도 함께 이어서 보세요.", cap: "제4강 · 다항함수 비율관계 ($m:n$ 내분점 공식)" },
      { tag: "이 사이트", say: "이 사이트의 제삼강과 제사강을 이어서 보세요.", cap: "제3강 · 변곡접선 정리하기  /  제4강 · 다항함수 비율관계" }
    ] }
  ];

  const G_EX = {
    f: x => (x * x) / 3, GY0: 410, GV: 110, xr: [0, 3.05], area: [0, 3], ytop: 45, ybot: 445, labelY: 448, boxX: 3,
    r1: { x: 0, col: CY, label: "꼭짓점 x=0" }, r2: { x: 3, col: PK, label: "밑면 h (단면 πr²)" },
    fn: { t: "단면 넓이 S(x) ∝ x²  →  부피는 기둥의 1/3", x: 490, y: 72 }, sPos: [560, 335], sOpenTxt: "기둥 36π", finalS: "원뿔 V = 12π", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => (x * x) / 12, GY0: 410, GV: 110, xr: [0, 6.05], area: [0, 6], ytop: 45, ybot: 445, labelY: 448, gux: 120, boxX: 6,
    r1: { x: 0, col: CY, label: "x = 0" }, r2: { x: 6, col: PK, label: "x = 6 (단면 36)" },
    fn: { t: "S(x) = x²  (0 ≤ x ≤ 6)", x: 480, y: 72 }, sPos: [550, 335], sOpenTxt: "∫₀⁶ x² dx", finalS: "부피 V = 72", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => ({
      chips: [
        { id: "T1", tex: "r_{k}=\\dfrac{k}{n}\\,r,\\quad \\Delta h=\\dfrac{h}{n}", cls: "cy" },
        { id: "T2", tex: "V_{n}=\\dfrac{\\pi r^{2}h}{n^{3}}\\cdot\\dfrac{n(n+1)(2n+1)}{6}", cls: "pk sm" },
        { id: "T3", tex: "V=\\dfrac{2}{6}\\pi r^{2}h=\\dfrac{1}{3}\\pi r^{2}h", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 45, op: 1, pop: ph === 0 ? 1 : 0 },
          T2: { x: 480, y: 215, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          T3: { x: 480, y: 410, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "T2", col: CY });
        if (ph === 2) L.push({ a: "T2", b: "T3", col: GO, label: "최고차항 비 2/6 = 1/3" });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    ex: (() => ({
      graph: G_EX,
      chips: [
        { id: "T1", tex: "r=3,\\quad h=4", cls: "cy" },
        { id: "M", tex: "V_{\\text{기둥}}=\\pi\\times 3^{2}\\times 4=36\\pi", cls: "pk" },
        { id: "R", tex: "V_{\\text{원뿔}}=\\dfrac{1}{3}\\times 36\\pi=12\\pi", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          R: { x: 480, y: 345, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "R", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    exam: (() => ({
      graph: G_EXAM,
      chips: [
        { id: "T1", tex: "S(x)=x^{2}\\quad (0\\le x\\le 6)", cls: "cy" },
        { id: "M", tex: "V=\\displaystyle\\int_{0}^{6}x^{2}\\,dx=\\left[\\dfrac{x^{3}}{3}\\right]_{0}^{6}", cls: "pk" },
        { id: "V", tex: "V=\\dfrac{216}{3}=72", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          V: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "V", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))()
  };

  return {
    lec: 39,
    hostId: "l39ShortsHost",
    prefix: "l39s",
    title: "숏츠식 판서 미리보기 · 원뿔의 부피와 구분구적법 (1/3 증명)",
    desc: "구분구적법과 $\\sum k^{2}$ 의 최고차항 계수 비 $\\dfrac{2}{6}=\\dfrac{1}{3}$ 로부터 원뿔 부피 공식을 유도합니다.",
    nextLinks: [
      { lec: 3, label: "제3강 열기 (변곡접선)" },
      { lec: 4, label: "제4강 열기 (m:n 내분점)" },
      { lec: 38, label: "제38강 열기 (리만 직사각형)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   8. 제37강 · 삼차함수 비율관계와 극대·극소 높이차 공식
      (미분·비율 사슬: 제3강 → 제4강 → 제37강 → 제36강 → 제27강 → 제14강 → 제29강)
   ================================================================== */
const L37_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "삼차함수 비율과 극값 높이차", sub: "1:1:1 비율과 높이차 30초 공식", parts: [
      { say: "삼차함수 일 대 일 대 일 비율관계와 극대·극소 높이차 공식, 30초 만에 정리합니다.", cap: "삼차함수 비율과 극값 높이차 · 30초 공식" }
    ] },
    { id: "why", type: "list", head: "이 공식을 배우는 이유", parts: [
      { say: "삼차함수의 극점·변곡점·교점 사이의 간격과 극대·극소 높이 차이를 미분이나 적분 없이 한 줄로 계산할 수 있습니다.", cap: "가로 간격 $1:1:1$ · 세로 높이차 $H=\\dfrac{|a|}{2}L^{3}=4|a|d^{3}$" }
    ] },
    { id: "hist", type: "list", head: "공식의 뿌리", parts: [
      { tag: "미적분 결합", say: "가로 비율은 변곡점 대칭과 이 대 일 내분점에서 나오고, 세로 높이차는 도함수의 정적분 넓이 공식에서 바로 유도됩니다.", cap: "제4강 내분점 비율 + 제2강·제33강 도함수 넓이 공식의 결합" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기 · 가로 1:1:1 과 세로 높이차", parts: [
      { say: "삼차함수의 극대·변곡점·극소·다시 같은 높이가 되는 교점까지의 가로 간격은 모두 디로 같습니다.", cap: "가로 4등분 간격 $d\\ :\\ d\\ :\\ d$ ($1:1:1$)" },
      { say: "두 극점 사이의 가로 거리 엘은 이 디이고, 도함수는 삼 에이 곱하기 엑스 빼기 알파 곱하기 엑스 빼기 베타입니다.", cap: "극점 사이 거리 $L=2d$, 도함수 최고차항 $3a$" },
      { say: "도함수 넓이가 곧 극대·극소 높이차이므로 육분의 삼 에이 곱하기 엘 세제곱, 즉 이분의 에이 엘 세제곱이 됩니다.", cap: "극대·극소 높이차 $H=\\dfrac{|a|}{2}\\,L^{3}=4|a|d^{3}$" }
    ] },
    { id: "ex", type: "chips", head: "예제", parts: [
      { say: "최고차항 계수가 일인 삼차함수가 엑스는 일에서 극대, 엑스는 삼에서 극소일 때 극대·극소 높이차를 구해 봅시다.", cap: "$a=1$, 극대 $x=1$, 극소 $x=3$" },
      { say: "두 극점 사이의 거리 엘은 삼 빼기 일, 이이고 한 칸 간격 디는 일입니다.", cap: "$L=3-1=2\\quad (d=1)$" },
      { say: "공식에 넣으면 이분의 일 곱하기 이의 세제곱, 극대·극소 높이차는 사입니다.", cap: "높이차 $H=\\dfrac{1}{2}\\times 2^{3}=4$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 최고차항 계수가 양수 에이인 삼차함수가 엑스는 영에서 극대, 엑스는 이에서 극소이고 극댓값과 극솟값의 차가 십이일 때, 에이는 얼마일까요?", cap: "극점 거리 $L=2$, 극대·극소 차 $H=12$ 일 때 $a$ 구하기 (자작 문항)" },
      { say: "높이차 공식 이분의 에이 곱하기 이의 세제곱은 사 에이입니다.", cap: "$H=\\dfrac{a}{2}\\times 2^{3}=4a$" },
      { say: "사 에이가 십이이므로 에이는 삼입니다.", cap: "$4a=12\\ \\Rightarrow\\ a=3$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 극대·변곡점·극소·접선 교점의 엑스좌표 간격은 항상 일 대 일 대 일입니다.", cap: "① 접점 $\\to$ 변곡점 $\\to$ 극점 $\\to$ 교점 간격 $d:d:d$" },
      { say: "둘째, 최고차항 계수가 일이고 두 극점 거리가 이이면 극대·극소 높이차는 무조건 사입니다.", cap: "② $a=1,\\ L=2\\ (d=1)\\ \\Rightarrow\\ \\text{극값 높이차 }H=4$" },
      { say: "셋째, 한 칸 간격 디로 외울 때는 사 절댓값 에이 곱하기 디의 세제곱입니다.", cap: "③ $H=\\dfrac{|a|}{2}\\,L^{3}=4|a|d^{3}$" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "다음은 인수분해된 식에서 미분계수를 일초 만에 구하는 거리곱 공식입니다.", cap: "제36강 · 다항함수 거리곱 공식과 고속 개형 추론" },
      { tag: "연계 ②", say: "다항함수의 인수와 대칭성을 8칸 박스로 읽는 제이십칠강도 이어서 보세요.", cap: "제27강 · 다항함수를 보는 눈 (인수와 대칭성)" },
      { tag: "이 사이트", say: "이 사이트의 제삼십육강과 제이십칠강을 이어서 보세요.", cap: "제36강 · 다항함수 거리곱 공식  /  제27강 · 다항함수를 보는 눈" }
    ] }
  ];

  const G_EX = {
    f: x => 0.35 * (x * x * x - 6 * x * x + 9 * x), GY0: 360, GV: 70, xr: [-0.1, 4.1], area: [0, 4], ytop: 45, ybot: 445, labelY: 448, gx0: 70, gux: 195,
    r1: { x: 1, col: CY, label: "극대 x=1" }, r2: { x: 3, col: PK, label: "극소 x=3 (L=2)" },
    fn: { t: "f(x) = x³ − 6x² + 9x  (간격 1 : 1 : 1)", x: 490, y: 75 }, sPos: [460, 250], sOpenTxt: "L = 2, d = 1", finalS: "높이차 H = 4", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => 0.45 * (x * x * x - 3 * x * x + 4), GY0: 370, GV: 65, xr: [-1.1, 3.1], area: [-1, 3], ytop: 45, ybot: 445, labelY: 448, gx0: 270, gux: 195,
    r1: { x: 0, col: CY, label: "극대 x=0" }, r2: { x: 2, col: PK, label: "극소 x=2 (L=2)" },
    fn: { t: "f(x) = a(x³ − 3x²) + C  (높이차 H = 12)", x: 490, y: 75 }, sPos: [470, 250], sOpenTxt: "H = 4a = 12", finalS: "a = 3 (H = 12)", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => ({
      chips: [
        { id: "T1", tex: "\\text{가로 간격 } d:d:d\\ (1:1:1),\\quad L=2d", cls: "cy" },
        { id: "T2", tex: "H=\\displaystyle\\int_{\\alpha}^{\\beta}|3a(x-\\alpha)(x-\\beta)|\\,dx", cls: "pk sm" },
        { id: "T3", tex: "H=\\dfrac{|a|}{2}\\,L^{3}=4|a|d^{3}", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 45, op: 1, pop: ph === 0 ? 1 : 0 },
          T2: { x: 480, y: 215, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          T3: { x: 480, y: 410, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "T2", col: CY });
        if (ph === 2) L.push({ a: "T2", b: "T3", col: GO, label: "1/6 공식 결합" });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    ex: (() => ({
      graph: G_EX,
      chips: [
        { id: "T1", tex: "a=1,\\quad x_{\\text{극대}}=1,\\quad x_{\\text{극소}}=3", cls: "cy" },
        { id: "M", tex: "L=3-1=2,\\quad d=1", cls: "pk" },
        { id: "R", tex: "H=\\dfrac{1}{2}\\times 2^{3}=4", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          R: { x: 480, y: 345, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "R", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    exam: (() => ({
      graph: G_EXAM,
      chips: [
        { id: "T1", tex: "L=2-0=2,\\quad H=12", cls: "cy" },
        { id: "M", tex: "H=\\dfrac{a}{2}\\times 2^{3}=4a", cls: "pk" },
        { id: "V", tex: "4a=12\\ \\Rightarrow\\ a=3", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          V: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "V", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))()
  };

  return {
    lec: 37,
    hostId: "l37ShortsHost",
    prefix: "l37s",
    title: "숏츠식 판서 미리보기 · 삼차함수 비율관계와 극대·극소 높이차",
    desc: "삼차함수의 $1:1:1$ 가로 비율과 극대·극소 높이차 공식 $H=\\dfrac{|a|}{2}L^{3}=4|a|d^{3}$ 을 확인합니다.",
    nextLinks: [
      { lec: 36, label: "제36강 열기 (거리곱 공식)" },
      { lec: 27, label: "제27강 열기 (인수와 대칭)" },
      { lec: 4, label: "제4강 열기 (m:n 내분점)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   9. 제36강 · 다항함수 거리곱 공식과 고속 개형 추론
   ================================================================== */
const L36_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "다항함수 미분계수 거리곱 공식", sub: "전개 없이 접선 기울기 10초 풀이", parts: [
      { say: "인수분해된 다항함수에서 전개 없이 미분계수를 바로 구하는 거리곱 공식, 30초 만에 정리합니다.", cap: "다항함수 거리곱 공식 · 30초 정리" }
    ] },
    { id: "why", type: "list", head: "이 공식을 배우는 이유", parts: [
      { say: "인수가 여러 개인 식을 미분할 때 곱의 미분법을 길게 쓰지 않고, 나머지 근까지의 거리만 곱해 접선 기울기를 즉시 구합니다.", cap: "자신을 제외한 나머지 인수의 거리곱 $= f'(\\alpha)$" }
    ] },
    { id: "hist", type: "list", head: "공식의 뿌리", parts: [
      { tag: "곱의 미분", say: "곱의 미분법에서 대입하려는 근을 가진 인수는 모두 영이 되어 사라지고, 자기 자신이 미분된 항 하나만 남는 원리입니다.", cap: "곱의 미분법에서 나머지 항은 모두 $0$ 으로 소거" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기", parts: [
      { say: "에프 엑스가 에이 곱하기 엑스 빼기 알파 곱하기 엑스 빼기 베타 곱하기 엑스 빼기 감마일 때, 알파에서의 미분계수를 구합니다.", cap: "$f(x)=a(x-\\alpha)(x-\\beta)(x-\\gamma)$" },
      { say: "엑스 빼기 알파 인수를 가리고 남은 자리에 알파를 넣으면, 알파에서 베타와 감마까지의 차가 남습니다.", cap: "$f'(\\alpha)=a(\\alpha-\\beta)(\\alpha-\\gamma)$" },
      { say: "만약 베타가 이중근이면 베타까지의 거리를 두 번 곱해 제곱으로 계산합니다.", cap: "중근 $(x-\\beta)^{2}$ 이면 거리 제곱: $f'(\\alpha)=a(\\alpha-\\beta)^{2}$" }
    ] },
    { id: "ex", type: "chips", head: "예제", parts: [
      { say: "삼차함수 엑스 곱하기 엑스 빼기 이 곱하기 엑스 빼기 오에서 엑스는 오일 때의 접선 기울기를 구해 봅시다.", cap: "$f(x)=x(x-2)(x-5)$ 에서 $f'(5)$ 구하기" },
      { say: "오에서 나머지 두 근 영과 이까지의 거리는 각각 오와 삼입니다.", cap: "$5-0=5,\\quad 5-2=3$" },
      { say: "두 거리를 곱하면 오 곱하기 삼, 미분계수는 십오입니다.", cap: "$f'(5)=5\\times 3=15$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 삼차함수 에이 곱하기 엑스 빼기 일의 제곱 곱하기 엑스 빼기 사에서 엑스는 사일 때 접선 기울기가 십팔이면, 에이는 얼마일까요?", cap: "$f(x)=a(x-1)^{2}(x-4),\\ f'(4)=18$ 일 때 $a$ 구하기 (자작 문항)" },
      { say: "사에서 이중근 일까지의 거리는 삼이므로 거리의 제곱은 구입니다.", cap: "이중근까지의 거리 제곱 $(4-1)^{2}=9$" },
      { say: "에프 프라임 사는 구 에이이고, 이 값이 십팔이므로 에이는 이입니다.", cap: "$9a=18\\ \\Rightarrow\\ a=2$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 구하려는 근의 인수를 손으로 가리고 나머지 인수에 그 근을 대입합니다.", cap: "① $(x-\\alpha)$ 를 가리고 나머지 인수에 $x=\\alpha$ 대입" },
      { say: "둘째, 이중근까지는 거리의 제곱, 삼중근까지는 거리의 세제곱을 곱합니다.", cap: "② $m$중근 $(x-\\beta)^{m}$ 은 $(\\alpha-\\beta)^{m}$ 곱하기" },
      { say: "셋째, 극점 개형에서 부호는 그 근에서 그래프가 올라가면 양수, 내려가면 음수입니다.", cap: "③ 부호는 그래프 증감 방향($+/-$)으로 즉시 확인" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "다음은 인수정리로 다항함수 식을 단번에 세우는 제이십칠강 다항함수를 보는 눈입니다.", cap: "제27강 · 다항함수를 보는 눈 (인수와 대칭성)" },
      { tag: "연계 ②", say: "극값의 교과서 정의를 정확히 짚어 주는 제십사강도 이어서 보세요.", cap: "제14강 · 이게 극대라고?! (극값의 진짜 정의)" },
      { tag: "이 사이트", say: "이 사이트의 제이십칠강과 제십사강을 이어서 보세요.", cap: "제27강 · 다항함수를 보는 눈  /  제14강 · 극값의 정의" }
    ] }
  ];

  const G_EX = {
    f: x => 0.08 * x * (x - 2) * (x - 5), GY0: 260, GV: 70, xr: [-0.3, 5.25], area: [0, 5], ytop: 45, ybot: 445, labelY: 448, gx0: 65, gux: 155,
    r1: { x: 2, col: CY, label: "근 0, 2 (거리 5, 3)" }, r2: { x: 5, col: PK, label: "x = 5 접선" },
    fn: { t: "f(x) = x(x − 2)(x − 5)", x: 480, y: 75 }, sPos: [620, 175], sOpenTxt: "거리 5 × 3", finalS: "f'(5) = 15", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => 0.22 * (x - 1) * (x - 1) * (x - 4), GY0: 150, GV: 85, xr: [0.4, 4.25], area: [1, 4], ytop: 45, ybot: 445, labelY: 112, gx0: 30, gux: 205,
    r1: { x: 1, col: CY, label: "x=1 (이중근)" }, r2: { x: 4, col: PK, label: "x=4 (기울기 18)" },
    fn: { t: "f(x) = a(x − 1)²(x − 4)", x: 480, y: 78 }, sPos: [560, 320], sOpenTxt: "f'(4) = 9a = 18", finalS: "a = 2 (f'(4) = 18)", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => ({
      chips: [
        { id: "T1", tex: "f(x)=a(x-\\alpha)(x-\\beta)(x-\\gamma)", cls: "cy" },
        { id: "T2", tex: "f'(\\alpha)=a(\\alpha-\\beta)(\\alpha-\\gamma)", cls: "go big" },
        { id: "T3", tex: "f(x)=a(x-\\beta)^{2}(x-\\alpha)\\ \\Rightarrow\\ f'(\\alpha)=a(\\alpha-\\beta)^{2}", cls: "pk sm" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 50, op: 1, pop: ph === 0 ? 1 : 0 },
          T2: { x: 480, y: 225, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          T3: { x: 480, y: 415, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "T2", col: CY, label: "(x−α) 가리고 대입" });
        if (ph === 2) L.push({ a: "T2", b: "T3", col: PK, label: "이중근은 거리 제곱" });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    ex: (() => ({
      graph: G_EX,
      chips: [
        { id: "T1", tex: "f(x)=x(x-2)(x-5)", cls: "cy" },
        { id: "M", tex: "d_{1}=5-0=5,\\quad d_{2}=5-2=3", cls: "pk" },
        { id: "R", tex: "f'(5)=5\\times 3=15", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          R: { x: 480, y: 345, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "R", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    exam: (() => ({
      graph: G_EXAM,
      chips: [
        { id: "T1", tex: "f(x)=a(x-1)^{2}(x-4)", cls: "cy" },
        { id: "M", tex: "f'(4)=a(4-1)^{2}=9a", cls: "pk" },
        { id: "V", tex: "9a=18\\ \\Rightarrow\\ a=2", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          V: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "V", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))()
  };

  return {
    lec: 36,
    hostId: "l36ShortsHost",
    prefix: "l36s",
    title: "숏츠식 판서 미리보기 · 다항함수 거리곱 공식과 고속 개형 추론",
    desc: "인수분해된 다항함수에서 나머지 근까지의 거리곱으로 미분계수 $f'(\\alpha)$ 를 즉시 구하는 공식을 확인합니다.",
    nextLinks: [
      { lec: 27, label: "제27강 열기 (인수와 대칭)" },
      { lec: 14, label: "제14강 열기 (극값의 정의)" },
      { lec: 37, label: "제37강 열기 (삼차 비율·높이차)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   10. 제27강 · 다항함수를 보는 눈 (인수와 대칭성, 8칸 박스법)
   ================================================================== */
const L27_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "다항함수를 보는 눈 · 인수정리", sub: "전개식 대신 인수로 식 세우기", parts: [
      { say: "다항함수를 에이 엑스 세제곱처럼 전개하지 않고 인수와 대칭으로 세우는 법, 30초 만에 정리합니다.", cap: "다항함수를 보는 눈 · 인수정리 식 세우기" }
    ] },
    { id: "why", type: "list", head: "인수로 식을 세우는 이유", parts: [
      { say: "전개식으로 미정계수 네 개를 연립하면 계산이 길지만, 교점과 접점을 인수로 묶으면 미지수가 하나로 줄어듭니다.", cap: "교점은 $(x-\\alpha)$, 접점은 $(x-\\alpha)^{2}$, 변곡접점은 $(x-\\alpha)^{3}$" }
    ] },
    { id: "hist", type: "list", head: "원리의 뿌리", parts: [
      { tag: "17세기", say: "다항식의 근과 인수가 일대일로 대응한다는 인수정리는 데카르트의 기하학에서 정립되었습니다.", cap: "데카르트의 인수정리: $f(\\alpha)=k \\Longleftrightarrow (x-\\alpha)$ 인수" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기 · 차함수 인수분해", parts: [
      { say: "에프 알파와 에프 베타가 모두 케이로 같다면, 에프 엑스 빼기 케이는 알파와 베타를 근으로 가집니다.", cap: "$f(\\alpha)=f(\\beta)=k\\ \\Rightarrow\\ f(x)-k=0$ 의 근이 $\\alpha,\\ \\beta$" },
      { say: "여기에 알파에서 접한다는 조건이 있으면 엑스 빼기 알파의 제곱 인수로 바로 묶습니다.", cap: "$f(x)-k=a(x-\\alpha)^{2}(x-\\beta)$" },
      { say: "직선 엠 엑스 더하기 엔과 만날 때도 똑같이 에프 엑스 빼기 직선을 인수로 묶어 세웁니다.", cap: "$f(x)-(mx+n)=a(x-\\alpha)^{2}(x-\\beta)$" }
    ] },
    { id: "ex", type: "chips", head: "예제", parts: [
      { say: "최고차항 계수가 일인 삼차함수가 엑스는 일에서 와이는 오에 접하고, 엑스는 사에서 다시 와이는 오와 만날 때 식을 세워 봅시다.", cap: "$x=1$ 에서 $y=5$ 에 접하고 $x=4$ 에서 $y=5$ 와 교차" },
      { say: "일은 이중근, 사는 단일근이므로 에프 엑스 빼기 오는 엑스 빼기 일의 제곱 곱하기 엑스 빼기 사입니다.", cap: "$f(x)-5=(x-1)^{2}(x-4)$" },
      { say: "따라서 에프 삼은 이의 제곱 곱하기 마이너스 일 더하기 오, 일이 됩니다.", cap: "$f(3)=4\\times(-1)+5=1$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 최고차항 계수가 일인 삼차함수가 에프 영과 에프 이가 모두 삼이고, 에프 프라임 영이 영일 때 에프 사는 얼마일까요?", cap: "$f(0)=f(2)=3,\\ f'(0)=0$ 일 때 $f(4)$ 구하기 (자작 문항)" },
      { say: "영에서 함숫값이 삼이고 미분계수가 영이므로 영은 와이는 삼과의 이중근입니다.", cap: "$f(x)-3=x^{2}(x-2)$" },
      { say: "엑스에 사를 대입하면 십육 곱하기 이 더하기 삼, 정답은 삼십오입니다.", cap: "$f(4)=16\\times 2+3=35$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 같은 함숫값 케이가 보이면 무조건 에프 엑스 빼기 케이로 시작합니다.", cap: "① $f(\\alpha)=f(\\beta)=k\\ \\Rightarrow\\ f(x)-k$ 부터 쓰기" },
      { say: "둘째, 함숫값과 미분계수가 동시에 주어진 점은 접점이므로 제곱 인수로 묶습니다.", cap: "② $f(\\alpha)=k,\\ f'(\\alpha)=0\\ \\Rightarrow\\ (x-\\alpha)^{2}$ 인수" },
      { say: "셋째, 삼차함수 8칸 박스를 그리면 변곡점 대칭과 비율이 한눈에 보입니다.", cap: "③ 8칸 박스: 가로 $1:1:1$, 세로 극값 차 $4|a|d^{3}$" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "다음은 미분가능성과 상관없는 극대·극소의 진짜 정의를 다루는 제십사강입니다.", cap: "제14강 · 이게 극대라고?! (극값의 진짜 정의)" },
      { tag: "연계 ②", say: "함수의 극한 진위판정을 반례 없이 푸는 제이십구강도 이어서 보세요.", cap: "제29강 · 함수의 극한 성질 진위판정 (치환법)" },
      { tag: "이 사이트", say: "이 사이트의 제십사강과 제이십구강을 이어서 보세요.", cap: "제14강 · 극값의 정의  /  제29강 · 함수의 극한 진위판정" }
    ] }
  ];

  const G_EX = {
    f: x => -0.35 * (x - 1) * (x - 1) * (4 - x), GY0: 150, GV: 150, xr: [0.4, 4.25], area: [1, 4], ytop: 40, ybot: 445, labelY: 112, gx0: 30, gux: 205,
    r1: { x: 1, col: CY, label: "x=1 접점 (m=2)" }, r2: { x: 4, col: PK, label: "x=4 교점 (n=1)" },
    fn: { t: "f(x) − 5 = (x − 1)²(x − 4)", x: 480, y: 80 }, sPos: [645, 395], sOpenTxt: "y = 5 기준선", finalS: "f(3) = −4 + 5 = 1", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => 0.12 * x * x * (x - 2), GY0: 290, GV: 70, xr: [-0.4, 4.1], area: [0, 2], ytop: 40, ybot: 445, labelY: 448, gx0: 100, gux: 185,
    r1: { x: 0, col: CY, label: "x=0 접점 (f=3)" }, r2: { x: 2, col: PK, label: "x=2 교점 (f=3)" },
    fn: { t: "f(x) − 3 = x²(x − 2)", x: 480, y: 80 }, sPos: [560, 200], sOpenTxt: "f(x) = x²(x−2)+3", finalS: "f(4) = 32 + 3 = 35", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => ({
      chips: [
        { id: "T1", tex: "f(\\alpha)=f(\\beta)=k,\\quad f'(\\alpha)=0", cls: "cy" },
        { id: "T2", tex: "f(x)-k=a(x-\\alpha)^{2}(x-\\beta)", cls: "go big" },
        { id: "T3", tex: "f(x)-(mx+n)=a(x-\\alpha)^{2}(x-\\beta)", cls: "pk sm" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 50, op: 1, pop: ph === 0 ? 1 : 0 },
          T2: { x: 480, y: 225, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          T3: { x: 480, y: 415, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "T2", col: CY, label: "접점은 제곱 인수" });
        if (ph === 2) L.push({ a: "T2", b: "T3", col: GO, label: "직선도 차함수로" });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    ex: (() => ({
      graph: G_EX,
      chips: [
        { id: "T1", tex: "f(1)=5,\\ f'(1)=0,\\ f(4)=5", cls: "cy" },
        { id: "M", tex: "f(x)-5=(x-1)^{2}(x-4)", cls: "pk" },
        { id: "R", tex: "f(3)=(3-1)^{2}(3-4)+5=1", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          R: { x: 480, y: 345, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "R", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    exam: (() => ({
      graph: G_EXAM,
      chips: [
        { id: "T1", tex: "f(0)=f(2)=3,\\quad f'(0)=0", cls: "cy" },
        { id: "M", tex: "f(x)=x^{2}(x-2)+3", cls: "pk" },
        { id: "V", tex: "f(4)=4^{2}\\times 2+3=35", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          V: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "V", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))()
  };

  return {
    lec: 27,
    hostId: "l27ShortsHost",
    prefix: "l27s",
    title: "숏츠식 판서 미리보기 · 다항함수를 보는 눈 (인수정리와 대칭)",
    desc: "전개식 대신 교점과 접점의 차함수 인수분해 $f(x)-k=a(x-\\alpha)^{2}(x-\\beta)$ 로 식을 세우는 원리를 확인합니다.",
    nextLinks: [
      { lec: 14, label: "제14강 열기 (극값의 정의)" },
      { lec: 29, label: "제29강 열기 (극한 진위판정)" },
      { lec: 36, label: "제36강 열기 (거리곱 공식)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   11. 제14강 · 이게 극대라고?! (극값의 진짜 정의)
   ================================================================== */
const L14_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "극대·극소의 진짜 교과서 정의", sub: "미분가능성·연속성과 무관한 정의", parts: [
      { say: "뾰족한 점이나 불연속인 점도 극대가 될 수 있는지, 극값의 진짜 정의를 30초 만에 정리합니다.", cap: "극대·극소의 진짜 정의 · 30초 완성" }
    ] },
    { id: "why", type: "list", head: "정의를 정확히 알아야 하는 이유", parts: [
      { say: "미분계수가 영이고 부호가 바뀐다는 것은 미분가능할 때의 판정법일 뿐, 교과서 정의는 주변 함숫값과의 크기 비교이기 때문입니다.", cap: "극값의 정의는 미분가능·연속 조건이 없다!" }
    ] },
    { id: "hist", type: "list", head: "정의의 뿌리", parts: [
      { tag: "해석학", say: "열린구간 근방에서 가장 큰 값을 극대라 부르는 국소 최대 개념은 현대 해석학과 고교 교과서의 표준 정의입니다.", cap: "열린구간 $(a-\\delta,\\ a+\\delta)$ 근방에서의 국소 대소 비교" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기 · 교과서 정의", parts: [
      { say: "엑스는 에이를 포함하는 어떤 열린구간에서 모든 엑스에 대해 에프 엑스가 에프 에이 이하이면 에프 에이는 극댓값입니다.", cap: "열린구간 내 모든 $x$ 에 대해 $f(x)\\le f(a)\\ \\Rightarrow\\ \\text{극대}$" },
      { say: "반대로 열린구간 내 모든 엑스에 대해 에프 엑스가 에프 에이 이상이면 에프 에이는 극솟값입니다.", cap: "열린구간 내 모든 $x$ 에 대해 $f(x)\\ge f(a)\\ \\Rightarrow\\ \\text{극소}$" },
      { say: "따라서 뾰족한 절댓값 꼭짓점이나 위로 찍힌 불연속 점도 주변보다 크거나 같으면 엄연한 극대입니다.", cap: "미분불가능(뾰족점)·불연속점도 정의만 만족하면 극값 ✔" }
    ] },
    { id: "ex", type: "chips", head: "예제 · 4가지 대표 사례 판별", parts: [
      { say: "절댓값 그래프처럼 뾰족한 산봉우리는 미분계수가 없지만 주변보다 가장 높으므로 극대입니다.", cap: "사례 ① 뾰족한 봉우리 $y=-|x|$ $\\Rightarrow$ $x=0$ 에서 극대 ✔" },
      { say: "상수함수 구간은 주변 함숫값이 모두 같아 작거나 같다는 등호가 성립하므로 극대이자 극소입니다.", cap: "사례 ② 평평한 상수 구간 $\\Rightarrow$ 등호($\\le, \\ge$) 성립 ✔" },
      { say: "불연속점이라도 함숫값 점이 주변 그래프보다 위에 찍혀 있으면 극대입니다.", cap: "사례 ③ 위에 찍힌 불연속점 $f(a)\\ge f(x)$ $\\Rightarrow$ 극대 ✔" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 함수 에프 엑스가 마이너스 절댓값 엑스 빼기 이 더하기 오일 때, 엑스는 이에서의 극댓값은 얼마일까요?", cap: "$f(x)=-|x-2|+5$ 의 극댓값 구하기 (자작 문항)" },
      { say: "엑스는 이에서 뾰족하여 미분불가능하지만, 모든 엑스에서 에프 엑스가 에프 이 이하이므로 극대입니다.", cap: "모든 $x$ 에서 $f(x)\\le f(2)=5$ (열린구간 정의 만족)" },
      { say: "따라서 극댓값은 에프 이, 오입니다.", cap: "극댓값 $f(2)=5$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 극값 정의에는 연속이나 미분가능이라는 조건이 전혀 없습니다.", cap: "① 극대·극소 정의 $\\neq$ 미분가능 ($f'(a)=0$ 은 미분가능할 때만)" },
      { say: "둘째, 에프 엑스가 에프 에이 이하라는 부등호에 등호가 들어 있음을 꼭 기억하세요.", cap: "② 정의의 부등호는 등호 포함 ($f(x)\\le f(a),\\ f(x)\\ge f(a)$)" },
      { say: "셋째, 진위판정에서 미분가능한 함수라는 전제가 있는지 가장 먼저 밑줄 긋습니다.", cap: "③ ‘미분가능한 함수 $f(x)$’ 조건 유무가 ㄱ·ㄴ·ㄷ 핵심" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "연계 ①", say: "다음은 수학 투 진위판정의 양대 산맥인 제이십구강 함수의 극한 성질 진위판정입니다.", cap: "제29강 · 함수의 극한 성질 진위판정 (치환법)" },
      { tag: "연계 ②", say: "처음 제이강 정적분 넓이 만능 공식으로 돌아가 전체 사슬을 복습할 수도 있습니다.", cap: "제2강 · 정적분 넓이 만능 공식으로 순환 복습" },
      { tag: "이 사이트", say: "이 사이트의 제이십구강과 제이강을 이어서 보세요.", cap: "제29강 · 함수의 극한 진위판정  /  제2강 · 정적분 넓이 만능 공식" }
    ] }
  ];

  const G_EX = {
    f: x => 2.2 - Math.abs(x - 1.5) * 1.4, GY0: 390, GV: 115, xr: [0, 3], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
    r1: { x: 0.5, col: CY, label: "a − δ" }, r2: { x: 2.5, col: CY, label: "a + δ (근방)" },
    fn: { t: "뾰족점 f(x) = −|x − a| + c  (미분불가능이어도 극대!)", x: 480, y: 72 }, sPos: [450, 290], sOpenTxt: "f(x) ≤ f(a)", finalS: "x = a 에서 극대 ✔", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => 2.5 - Math.abs(x - 2) * 1.1, GY0: 390, GV: 110, xr: [0.2, 3.8], area: [1, 3], ytop: 45, ybot: 445, labelY: 448, gx0: 60, gux: 210,
    r1: { x: 1, col: CY, label: "2 − δ" }, r2: { x: 3, col: PK, label: "2 + δ (x=2 극대)" },
    fn: { t: "f(x) = −|x − 2| + 5", x: 480, y: 72 }, sPos: [480, 290], sOpenTxt: "f(x) ≤ f(2) = 5", finalS: "극댓값 f(2) = 5", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => ({
      chips: [
        { id: "T1", tex: "x\\in(a-\\delta,\\ a+\\delta)\\text{ 에서 }f(x)\\le f(a)\\ \\Rightarrow\\ \\text{극대}", cls: "cy sm" },
        { id: "T2", tex: "x\\in(a-\\delta,\\ a+\\delta)\\text{ 에서 }f(x)\\ge f(a)\\ \\Rightarrow\\ \\text{극소}", cls: "pk sm" },
        { id: "T3", tex: "\\text{미분불가능(뾰족점)·불연속점도 극값 가능!}", cls: "go v" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 55, op: 1, pop: ph === 0 ? 1 : 0 },
          T2: { x: 480, y: 225, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          T3: { x: 480, y: 410, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "T2", col: CY });
        if (ph === 2) L.push({ a: "T2", b: "T3", col: GO, label: "미분 조건 없음" });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    ex: (() => ({
      graph: G_EX,
      chips: [
        { id: "T1", tex: "\\text{① 뾰족한 봉우리 }y=-|x|\\ \\Rightarrow\\ \\text{극대 ✔}", cls: "cy sm" },
        { id: "M", tex: "\\text{② 상수 구간 }f(x)=c\\ \\Rightarrow\\ \\text{극대이자 극소 ✔}", cls: "pk sm" },
        { id: "R", tex: "\\text{③ 위에 찍힌 불연속점 }f(a)\\ge f(x)\\ \\Rightarrow\\ \\text{극대 ✔}", cls: "go sm" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 25, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 185, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          R: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "R", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    exam: (() => ({
      graph: G_EXAM,
      chips: [
        { id: "T1", tex: "f(x)=-|x-2|+5", cls: "cy" },
        { id: "M", tex: "\\text{모든 }x\\text{ 에 대해 }f(x)\\le 5=f(2)", cls: "pk" },
        { id: "V", tex: "\\text{극댓값 }f(2)=5", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          V: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "V", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))()
  };

  return {
    lec: 14,
    hostId: "l14ShortsHost",
    prefix: "l14s",
    title: "숏츠식 판서 미리보기 · 이게 극대라고?! (극값의 진짜 정의)",
    desc: "미분가능성·연속성과 무관한 극대·극소의 열린구간 대소 비교 정의를 4가지 사례와 그래프로 확인합니다.",
    nextLinks: [
      { lec: 29, label: "제29강 열기 (극한 진위판정)" },
      { lec: 2, label: "제2강 열기 (정적분 만능공식)" },
      { lec: 27, label: "제27강 열기 (인수와 대칭)" }
    ],
    SCENES,
    chipDefs
  };
})();

/* ==================================================================
   12. 제29강 · 함수의 극한 성질 진위판정 (반례 없는 치환법)
   ================================================================== */
const L29_DATA = (() => {
  const SCENES = [
    { id: "hook", type: "hook", title: "함수의 극한 진위판정 치환법", sub: "반례 찾지 않고 10초 만에 판별", parts: [
      { say: "함수의 극한 진위판정 문제를 반례 없이 치환법으로 푸는 공식, 30초 만에 정리합니다.", cap: "함수의 극한 진위판정 · 치환법 30초 공식" }
    ] },
    { id: "why", type: "list", head: "치환법을 쓰는 이유", parts: [
      { say: "시험장에서 복잡한 반례를 일일이 떠올리는 대신, 수렴하는 식만 모아서 사칙연산 가능 여부를 확인하면 백 퍼센트 판별됩니다.", cap: "반례 암기 대신 ‘수렴 식 치환 + 분모 $0$ 점검’ 한 줄" }
    ] },
    { id: "hist", type: "list", head: "성질의 뿌리", parts: [
      { tag: "19세기", say: "수렴하는 두 함수의 합·차·곱·몫의 극한 법칙은 코시와 바이어슈트라스의 극한 정리에서 확립되었습니다.", cap: "코시·바이어슈트라스의 극한 사칙연산 정리" }
    ] },
    { id: "formula", type: "chips", head: "공식 만들기 · 수렴 식 치환과 나눗셈 점검", parts: [
      { say: "수렴한다고 주어진 복잡한 식을 에이치 엑스로 치환하면, 에프 엑스와 에이치 엑스는 모두 수렴합니다.", cap: "수렴하는 식을 $h(x)$ 로 치환" },
      { say: "구하려는 지 엑스를 에프 엑스와 에이치 엑스의 덧셈, 뺄셈, 곱셈으로만 나타낼 수 있으면 무조건 참입니다.", cap: "합·차·곱($+,-,\\times$)만으로 표현 $\\Rightarrow\\ \\text{무조건 참(True)}$" },
      { say: "반면 나눗셈이 들어가면 분모의 극한값이 영이 아니라는 보장이 있을 때만 참이고, 없으면 거짓입니다.", cap: "나눗셈($\\div$) 포함 시 분모 극한 $\\ne 0$ 보장 없으면 거짓(False)" }
    ] },
    { id: "ex", type: "chips", head: "예제 · 참과 거짓 비교", parts: [
      { say: "에프 엑스와 에프 더하기 지가 수렴할 때, 에프 더하기 지를 에이치로 두면 지는 에이치 빼기 에프이므로 무조건 수렴합니다.", cap: "$g(x)=h(x)-f(x)$ (뺄셈) $\\Rightarrow\\ \\text{참(True)}$" },
      { say: "하지만 에프 엑스와 에프 곱하기 지가 수렴할 때는 지가 에프분의 에이치가 되어 분모로 에프가 들어갑니다.", cap: "$g(x)=\\dfrac{h(x)}{f(x)}$ (나눗셈 발생)" },
      { say: "에프 엑스의 극한이 영일 수 있으므로 이 명제는 거짓입니다.", cap: "$\\lim f(x)=0$ 가능성 존재 $\\Rightarrow\\ \\text{거짓(False)}$" }
    ] },
    { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
      { say: "수능형 문제입니다. 엑스가 일로 갈 때 에프 엑스가 삼으로 수렴하고, 에프 엑스 분의 지 엑스가 이로 수렴하면 지 엑스의 극한값은 얼마일까요?", cap: "$\\lim_{x\\to 1}f(x)=3,\\ \\lim_{x\\to 1}\\dfrac{g(x)}{f(x)}=2$ 일 때 $\\lim_{x\\to 1}g(x)$ (자작 문항)" },
      { say: "에프 분의 지를 에이치로 치환하면, 지 엑스는 에프 엑스 곱하기 에이치 엑스입니다.", cap: "$h(x)=\\dfrac{g(x)}{f(x)}\\ \\Rightarrow\\ g(x)=f(x)\\cdot h(x)$ (곱셈)" },
      { say: "나눗셈 없이 곱셈만으로 표현되므로 극한값은 삼 곱하기 이, 육으로 참입니다.", cap: "$\\lim_{x\\to 1}g(x)=3\\times 2=6\\ (\\text{참})$" }
    ] },
    { id: "tips", type: "list", head: "실전 꿀팁", parts: [
      { say: "첫째, 수렴한다고 주어진 식에 동그라미를 치고 에이치 엑스로 치환합니다.", cap: "① 수렴하는 식 $=h(x)$ 로 치환" },
      { say: "둘째, 물어보는 함수를 에이치로 정리했을 때 분모가 생기면 분모 극한이 영이 될 수 있는지 봅니다.", cap: "② 분모가 생기면 $\\lim(\\text{분모})=0$ 가능성 즉시 체크" },
      { say: "셋째, 합·차·곱으로만 정리되면 반례 고민 없이 즉시 참을 고릅니다.", cap: "③ $+,-,\\times$ 만 쓰이면 $100\\%$ 참(True)" }
    ] },
    { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
      { tag: "순환 복습", say: "이것으로 수학 투 핵심 13개 강의 숏츠 사슬이 완성되었습니다. 제이강 정적분 넓이 만능 공식부터 다시 순환 복습해 보세요.", cap: "제2강 · 정적분 넓이 만능 공식부터 전체 순환 복습" },
      { tag: "연계 복습", say: "정적분의 본질을 다루는 제삼십삼강과 비율관계의 제사강도 다시 확인해 보세요.", cap: "제33강 · 정적분의 본질  /  제4강 · 다항함수 비율관계" },
      { tag: "이 사이트", say: "이 사이트의 제이강과 제삼십삼강을 이어서 보세요.", cap: "제2강 · 정적분 넓이 만능 공식  /  제33강 · 정적분의 본질" }
    ] }
  ];

  const G_EX = {
    f: x => 0.4 * (x - 1.5) * (x - 1.5) + 0.5, GY0: 390, GV: 110, xr: [0, 3], area: [0.5, 2.5], ytop: 45, ybot: 445, labelY: 448,
    r1: { x: 0.8, col: CY, label: "합·차·곱 → 참" }, r2: { x: 2.2, col: PK, label: "나눗셈(분모 0) → 거짓" },
    fn: { t: "수렴 식 치환 h(x) · 나눗셈 분모 0 체크", x: 480, y: 75 }, sPos: [480, 275], sOpenTxt: "g = h / f ?", finalS: "분모 → 0 가능하면 거짓!", finalPh: 2, scaleTo: 1
  };
  const G_EXAM = {
    f: x => 0.35 * x * x + 1.2, GY0: 390, GV: 95, xr: [0, 2.5], area: [0.4, 2.0], ytop: 45, ybot: 445, labelY: 448, gx0: 120, gux: 280,
    r1: { x: 1, col: CY, label: "x → 1 (f → 3)" }, r2: { x: 2, col: GO, label: "g = f·h → 6" },
    fn: { t: "g(x) = f(x) · [g(x)/f(x)]  (곱셈이므로 수렴 보장)", x: 480, y: 75 }, sPos: [480, 275], sOpenTxt: "3 × 2", finalS: "lim g(x) = 6 (참)", finalPh: 2, scaleTo: 1
  };

  const chipDefs = {
    formula: (() => ({
      chips: [
        { id: "T1", tex: "\\text{수렴하는 식 }\\longrightarrow\\ h(x)\\text{ 로 치환}", cls: "cy" },
        { id: "T2", tex: "g(x)=f(x)\\pm h(x),\\ f(x)\\cdot h(x)\\ \\Rightarrow\\ \\text{무조건 참(True)}", cls: "go sm" },
        { id: "T3", tex: "g(x)=\\dfrac{h(x)}{f(x)}\\ \\Rightarrow\\ \\lim f(x)\\ne 0\\text{ 보장 없으면 거짓(False)}", cls: "pk sm" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 50, op: 1, pop: ph === 0 ? 1 : 0 },
          T2: { x: 480, y: 220, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          T3: { x: 480, y: 410, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "T2", col: CY });
        if (ph === 2) L.push({ a: "T2", b: "T3", col: PK, label: "나눗셈 주의" });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    ex: (() => ({
      graph: G_EX,
      chips: [
        { id: "T1", tex: "f+g=h\\ \\Rightarrow\\ g=h-f\\ (\\text{뺄셈}\\ \\Rightarrow\\ \\text{참})", cls: "cy sm" },
        { id: "M", tex: "f\\cdot g=h\\ \\Rightarrow\\ g=\\dfrac{h}{f}\\ (\\text{나눗셈 발생})", cls: "pk sm" },
        { id: "R", tex: "\\lim f(x)=0\\text{ 가능}\\ \\Rightarrow\\ \\text{거짓(False)}", cls: "go v" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          R: { x: 480, y: 345, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "R", col: PK });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))(),
    exam: (() => ({
      graph: G_EXAM,
      chips: [
        { id: "T1", tex: "\\lim_{x\\to 1}f(x)=3,\\quad \\lim_{x\\to 1}h(x)=\\lim_{x\\to 1}\\dfrac{g(x)}{f(x)}=2", cls: "cy sm" },
        { id: "M", tex: "g(x)=f(x)\\cdot h(x)\\ (\\text{곱셈})", cls: "pk" },
        { id: "V", tex: "\\lim_{x\\to 1}g(x)=3\\times 2=6", cls: "go big" }
      ],
      state(ph) {
        return {
          T1: { x: 480, y: 20, op: 1, pop: ph === 0 ? 1 : 0 },
          M: { x: 480, y: 180, op: ph >= 1 ? 1 : 0, pop: ph === 1 ? 1 : 0 },
          V: { x: 480, y: 350, op: ph >= 2 ? 1 : 0, pop: ph >= 2 ? 1 : 0 }
        };
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T1", b: "M", col: CY });
        if (ph === 2) L.push({ a: "M", b: "V", col: GO });
        return L;
      },
      fx: ph => ph === 2 ? "confetti" : ph === 1 ? "spark" : ""
    }))()
  };

  return {
    lec: 29,
    hostId: "l29ShortsHost",
    prefix: "l29s",
    title: "숏츠식 판서 미리보기 · 함수의 극한 성질 진위판정 (치환법)",
    desc: "수렴하는 식을 $h(x)$ 로 치환하고 나눗셈 분모의 $0$ 가능성만 점검하는 무결점 진위판정법을 확인합니다.",
    nextLinks: [
      { lec: 2, label: "제2강 열기 (처음부터 순환)" },
      { lec: 33, label: "제33강 열기 (정적분의 본질)" },
      { lec: 14, label: "제14강 열기 (극값의 정의)" }
    ],
    SCENES,
    chipDefs
  };
})();

const ALL_CONFIGS = [
  L9_DATA, L1_DATA, L33_DATA, L38_DATA, L39_DATA,
  L3_DATA, L4_DATA, L37_DATA, L36_DATA, L27_DATA, L14_DATA, L29_DATA
];
ALL_CONFIGS.forEach(cfg => {
  cfg.SCENES.forEach(s => {
    s.parts.forEach(p => { p.ms = estMs(p.say); });
    s.ms = s.parts.reduce((a, p) => a + p.ms, 0);
  });
});

/* ------------------------------------------------------------------ 공통 렌더러 생성기 */
const tf = (x, y, extra) => `translate(${x}px,${y}px) translate(-50%,0)${extra || ""}`;
const mathLen = s => (String(s).match(/\$([^$]+)\$/g) || []).reduce((a, m) => a + m.length - 2, 0);
function splitCap(cap) {
  const i = String(cap).indexOf("$");
  if (i < 0 || mathLen(cap) < 14) return { html: inline(cap) };
  return { label: cap.slice(0, i).trim(), eq: inline(cap.slice(i)) };
}

function chainNavHtml(activeLec) {
  const items = [
    { lec: 2, label: "1. 제2강 만능공식" },
    { lec: 9, label: "2. 제9강 차함수" },
    { lec: 1, label: "3. 제1강 넓이비 1:n" },
    { lec: 33, label: "4. 제33강 정적분 본질" },
    { lec: 38, label: "5. 제38강 리만 직사각형" },
    { lec: 39, label: "6. 제39강 원뿔 1/3" },
    { lec: 3, label: "7. 제3강 변곡접선" },
    { lec: 4, label: "8. 제4강 m:n 내분점" },
    { lec: 37, label: "9. 제37강 삼차 높이차" },
    { lec: 36, label: "10. 제36강 거리곱" },
    { lec: 27, label: "11. 제27강 인수·대칭" },
    { lec: 14, label: "12. 제14강 극값 정의" },
    { lec: 29, label: "13. 제29강 극한 진위" }
  ];
  return `<div class="l2s-row" style="margin-bottom:12px;padding:8px 10px;background:rgba(15,23,42,.75);border:1px solid #334155;border-radius:12px">
    <span class="l2s-note" style="margin-right:4px;font-weight:700;color:#cbd5e1">수학 II 13강 개념 연결 순서</span>
    ${items.map(it => `<button class="l2s-btn ${it.lec === activeLec ? "pri" : ""}" type="button" data-chain-lec="${it.lec}" style="padding:4px 9px;font-size:.8rem">${it.label}</button>`).join("")}
  </div>`;
}

function createShortsPlayer(cfg) {
  const pfx = cfg.prefix;
  const SCENES = cfg.SCENES;
  const chipDefs = cfg.chipDefs;
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
      const d = document.createElement("div");
      d.className = "l2s-fx";
      const sz = 10 + Math.random() * 16, c = colors[i % colors.length];
      d.style.cssText = `left:${x}px;top:${y}px;width:${sz}px;height:${sz}px;background:${c};box-shadow:0 0 18px ${c}`;
      h.appendChild(d);
      const a = Math.random() * Math.PI * 2, r = 90 + Math.random() * 150;
      d.animate(
        [{ transform: "translate(0,0) scale(1)", opacity: 1 }, { transform: `translate(${Math.cos(a) * r}px,${Math.sin(a) * r}px) scale(.2)`, opacity: 0 }],
        { duration: 700 + Math.random() * 400, easing: "cubic-bezier(.1,.8,.3,1)" }
      ).onfinish = () => d.remove();
    }
  }

  function confetti() {
    if (reduced()) return;
    playSfx("chime", sfxEnabled());
    const cs = ["#fbbf24", "#f472b6", "#38bdf8", "#34d399", "#a78bfa", "#fb7185"];
    for (let i = 0; i < 46; i++) {
      const d = document.createElement("div");
      d.className = "l2s-conf";
      d.style.cssText = `left:${Math.random() * 1040}px;background:${cs[i % cs.length]}`;
      stageEl.appendChild(d);
      d.animate(
        [{ transform: "translateY(0) rotate(0deg)", opacity: 1 }, { transform: `translate(${(Math.random() - 0.5) * 240}px,${1500 + Math.random() * 400}px) rotate(${(Math.random() - 0.5) * 1080}deg)`, opacity: 0.9 }],
        { duration: 1800 + Math.random() * 1400, delay: Math.random() * 500, easing: "cubic-bezier(.3,.1,.6,1)" }
      ).onfinish = () => d.remove();
    }
  }

  function fly(hostEl, m, n) {
    const { el, x0, y0, o, dist } = m;
    const arc = 70 + Math.min(150, dist * 0.2), mx = (x0 + o.x) / 2, my = (y0 + o.y) / 2 - arc;
    const rot = (o.x >= x0 ? 1 : -1) * (7 + Math.random() * 7), delay = n * 80 + 350;
    el.style.transform = tf(o.x, o.y);
    if (reduced()) return;
    if (n === 0) playSfx("whoosh", sfxEnabled());
    const kf = [
      { transform: tf(x0, y0, " scale(1) rotate(0deg)") },
      { transform: tf(mx, my, ` scale(1.22) rotate(${rot}deg)`), offset: 0.5 },
      { transform: tf(o.x, o.y, " scale(1) rotate(0deg)") }
    ];
    const opt = { duration: 1100, delay, easing: "cubic-bezier(.22,1,.36,1)", fill: "both" };
    const an = el.animate(kf, opt);
    an.onfinish = () => an.cancel();
    [0.11, 0.22].forEach((lag, gi) => {
      const g = el.cloneNode(true);
      g.removeAttribute("data-id");
      g.classList.add("ghost");
      g.style.opacity = 0;
      g.style.transform = tf(x0, y0);
      hostEl.appendChild(g);
      g.animate(
        kf.map((f, q) => Object.assign({}, f, { opacity: q === 1 ? 0.34 - gi * 0.12 : 0 })),
        Object.assign({}, opt, { delay: delay + lag * 1000 })
      ).onfinish = () => g.remove();
    });
  }

  function drawLinks(chipsEl, def, S, ph, animate) {
    const svg = chipsEl.querySelector(".l2s-links");
    svg.innerHTML = "";
    const NS = "http://www.w3.org/2000/svg";
    (def.links(ph) || []).forEach((lk, gi) => {
      const A = chipsEl.querySelector(`[data-id="${lk.a}"]`), B = chipsEl.querySelector(`[data-id="${lk.b}"]`);
      if (!A || !B) return;
      const a = S[lk.a], b = S[lk.b];
      const x1 = a.x, y1 = a.y + A.offsetHeight, x2 = b.x, y2 = b.y;
      const dy = Math.max(60, Math.abs(y2 - y1) * 0.5), d = `M ${x1} ${y1} C ${x1} ${y1 + dy}, ${x2} ${y2 - dy}, ${x2} ${y2}`;
      const g = document.createElementNS(NS, "g");
      g.style.color = lk.col;
      const p = document.createElementNS(NS, "path");
      p.setAttribute("d", d);
      p.setAttribute("stroke", lk.col);
      g.appendChild(p);
      [[x1, y1], [x2, y2]].forEach(pt => {
        const c = document.createElementNS(NS, "circle");
        c.setAttribute("cx", pt[0]); c.setAttribute("cy", pt[1]); c.setAttribute("r", 12); c.setAttribute("fill", lk.col);
        g.appendChild(c);
      });
      let tx = null;
      if (lk.label) {
        tx = document.createElementNS(NS, "text");
        tx.setAttribute("x", (x1 + x2) / 2);
        tx.setAttribute("y", (y1 + y2) / 2 + 10);
        tx.setAttribute("fill", GO);
        tx.textContent = lk.label;
        g.appendChild(tx);
      }
      svg.appendChild(g);
      if (animate && !reduced()) {
        const L = p.getTotalLength(), dl = gi * 200;
        p.style.strokeDasharray = L;
        p.animate([{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: 650, delay: dl, easing: "cubic-bezier(.3,.7,.3,1)", fill: "both" });
        g.querySelectorAll("circle").forEach(c => c.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 300, delay: dl + 300, fill: "both" }));
        if (tx) tx.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 350, delay: dl + 450, fill: "both" });
      }
    });
  }

  function graphHtml(c) {
    const gx0 = c.gx0 != null ? c.gx0 : 90;
    const gu = c.gux != null ? c.gux : 240;
    const px = x => gx0 + gu * x, py = x => c.GY0 - c.GV * c.f(x);
    let d = "", first = true;
    for (let x = c.xr[0]; x <= c.xr[1] + 0.001; x += 0.05) {
      d += (first ? "M" : "L") + px(x).toFixed(1) + " " + py(x).toFixed(1) + " ";
      first = false;
    }
    let a = `M ${px(c.area[0])} ${c.GY0} `;
    for (let x = c.area[0]; x <= c.area[1] + 0.001; x += 0.05) a += `L ${px(x).toFixed(1)} ${py(x).toFixed(1)} `;
    a += `L ${px(c.area[1])} ${c.GY0} Z`;
    const boxRect = c.boxX ? `<rect x="${px(0)}" y="${py(c.boxX)}" width="${(px(c.boxX) - px(0)).toFixed(1)}" height="${(c.GY0 - py(c.boxX)).toFixed(1)}" fill="rgba(56,189,248,.14)" stroke="#38bdf8" stroke-width="3" stroke-dasharray="10 8"></rect>` : "";
    const clipId = `${pfx}_gClip`;
    return `<svg class="l2s-graph" viewBox="0 0 960 480">
      <defs><clipPath id="${clipId}"><rect class="js-gClipR" x="0" y="0" width="0" height="480"></rect></clipPath></defs>
      <g stroke="rgba(255,255,255,.45)" stroke-width="3" fill="none"><line x1="20" y1="${c.GY0}" x2="900" y2="${c.GY0}"></line><line x1="${gx0}" y1="${c.ybot}" x2="${gx0}" y2="${c.ytop}"></line></g>
      <text x="925" y="${c.GY0 + 12}" fill="#cbd5e1" font-size="38">x</text><text x="${gx0 + 18}" y="${c.ytop + 8}" fill="#cbd5e1" font-size="38">y</text>
      ${boxRect}
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
    const curve = q(".js-gCurve");
    if (!curve) return;
    const L = curve.getTotalLength(), area = q(".js-gArea"), clipR = q(".js-gClipR"), roots = q(".js-gRoots"), fn = q(".js-gFn"), S = q(".js-gS"), sc = q(".js-gScale");
    if (fresh) {
      if (animate && !reduced()) {
        curve.style.strokeDasharray = L;
        curve.animate([{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: 1800, easing: "cubic-bezier(.4,.1,.3,1)", fill: "both" });
        clipR.animate([{ width: "0px" }, { width: "960px" }], { duration: 1500, delay: 1500, easing: "ease-out", fill: "both" });
        roots.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 500, delay: 900, fill: "both" });
        fn.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 600, delay: 1200, fill: "both" });
      } else {
        clipR.setAttribute("width", 960);
        roots.setAttribute("opacity", 1);
        fn.setAttribute("opacity", 1);
      }
    }
    const reach = ph >= c.finalPh;
    if (c.scaleTo && c.scaleTo !== 1) {
      const to = reach ? c.scaleTo : 1;
      if (animate && !reduced() && reach && sc.dataset.s !== "2") {
        sc.animate([{ transform: "scaleY(1)" }, { transform: `scaleY(${to})` }], { duration: 1100, easing: "cubic-bezier(.3,1.3,.4,1)", fill: "both" });
      } else {
        sc.style.transform = `scaleY(${to})`;
      }
      sc.dataset.s = reach ? "2" : "1";
    }
    if (reach) {
      S.textContent = c.finalS;
      S.setAttribute("opacity", 1);
      if (animate && !reduced()) {
        S.animate([{ opacity: 0, transform: "scale(.6)" }, { opacity: 1, transform: "scale(1)" }], { duration: 600, easing: "cubic-bezier(.2,1.4,.4,1)", fill: "both" });
        area.animate([{ fillOpacity: 1 }, { fillOpacity: 1.9 }, { fillOpacity: 1 }], { duration: 900 });
      }
    } else {
      S.textContent = c.sOpenTxt;
      S.setAttribute("opacity", fresh && animate ? 0 : 1);
      if (fresh && animate && !reduced()) S.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 500, delay: 2200, fill: "both" });
    }
  }

  function renderChips(sc, k, animate) {
    const def = chipDefs[sc.id];
    let chipsEl = stageEl.querySelector(".l2s-chips"), fresh = false;
    if (!chipsEl || curDefId !== sc.id) {
      fresh = true;
      curDefId = sc.id;
      stageEl.querySelector(".l2s-board").innerHTML =
        `<div class="l2s-head" style="margin-bottom:0">${sc.head}</div>` +
        (def.graph ? graphHtml(def.graph) : "") +
        `<div class="l2s-chips ${def.graph ? "g" : ""}"><svg class="l2s-links" viewBox="0 0 960 930"></svg>${def.chips.map(c => `<div class="l2c ${c.cls}" data-id="${c.id}"></div>`).join("")}</div>`;
      chipsEl = stageEl.querySelector(".l2s-chips");
      const S0 = def.state(0);
      def.chips.forEach(c => {
        const el = chipsEl.querySelector(`[data-id="${c.id}"]`), o = S0[c.id];
        el.innerHTML = c.tex ? K(c.tex) : "";
        el.dataset.h = c.tex;
        el.dataset.x = o.x;
        el.dataset.y = o.y;
        el.style.transform = tf(o.x, o.y);
        el.style.opacity = o.op;
        if (o.w) el.style.width = o.w + "px";
      });
    }
    const S = def.state(k), flying = [];
    def.chips.forEach(c => {
      const el = chipsEl.querySelector(`[data-id="${c.id}"]`), o = S[c.id], tex = o.tex != null ? o.tex : c.tex;
      const x0 = +el.dataset.x, y0 = +el.dataset.y, dist = Math.hypot(o.x - x0, o.y - y0);
      const seen = (+el.style.opacity || 0) > 0.05 || o.op > 0.05, changed = el.dataset.h !== tex;
      if (changed) { el.innerHTML = K(tex); el.dataset.h = tex; }
      if (o.w) el.style.width = o.w + "px";
      if (animate && dist > 8 && seen) flying.push({ el, x0, y0, o, dist });
      else el.style.transform = tf(o.x, o.y);
      el.style.opacity = o.op;
      el.dataset.x = o.x;
      el.dataset.y = o.y;
      if (animate && o.pop && !(dist > 8) && (changed || !fresh) && o.op > 0.05 && !reduced()) {
        setTimeout(() => {
          const a = el.animate(
            [{ transform: tf(o.x, o.y, " scale(1)") }, { transform: tf(o.x, o.y, " scale(1.35)"), offset: 0.4 }, { transform: tf(o.x, o.y, " scale(1)") }],
            { duration: 520, easing: "cubic-bezier(.2,1.4,.4,1)" }
          );
          a.onfinish = () => { el.style.transform = tf(o.x, o.y); };
          burst(o.x, o.y + 40, 10, [GO, "#fde68a", PK, CY]);
        }, 450);
      }
    });
    flying.sort((a, b) => a.x0 - b.x0).forEach((m, n) => fly(chipsEl, m, n));
    drawLinks(chipsEl, def, S, k, animate);
    if (def.graph) graphPhase(stageEl.querySelector(".l2s-board"), k, animate, fresh, def.graph);
    const fxk = def.fx(k);
    if (animate && fxk === "confetti") setTimeout(confetti, 700);
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
    const sc = SCENES[si];
    cur = { s: si, p: pi };
    if (!stageEl.querySelector(".l2s-board")) {
      stageEl.innerHTML = `<div class="l2s-board"></div><div class="l2s-cap"><span></span></div><div class="l2s-bar" id="${pfx}_Bar"></div>`;
    }
    let cap = sc.parts[pi].cap;
    if (sc.type === "chips") cap = renderChips(sc, pi, animate);
    else {
      curDefId = "";
      const b = stageEl.querySelector(".l2s-board");
      b.innerHTML = sc.type === "hook"
        ? `<div class="l2s-big">${sc.title}</div><div class="l2s-sub">${sc.sub}</div>`
        : listBoard(sc, pi);
    }
    const c = stageEl.querySelector(".l2s-cap span"), sp = splitCap(cap);
    c.innerHTML = sp.eq
      ? `<span class="l2s-lab">${inline(sp.label)}</span><span class="l2s-capeq l2s-fit">${sp.eq}</span>`
      : `<span class="l2s-fit" style="display:inline-block">${sp.html}</span>`;
    stageEl.querySelector(".l2s-cap").classList.add("l2s-fitbox");
    c.style.animation = "none"; c.offsetWidth; c.style.animation = "";

    let before = 0;
    for (let i = 0; i < si; i++) before += SCENES[i].ms;
    for (let j = 0; j < pi; j++) before += sc.parts[j].ms;
    const bar = qid("Bar");
    if (bar) {
      bar.style.transition = "none";
      bar.style.width = (before / total * 100) + "%";
      if (animate) {
        bar.offsetWidth;
        bar.style.transition = `width ${sc.parts[pi].ms / 1000}s linear`;
        bar.style.width = ((before + sc.parts[pi].ms) / total * 100) + "%";
      }
    }
    const st = qid("Time");
    if (st) st.textContent = `${si + 1} / ${SCENES.length} 장면 · 예상 전체 ${Math.floor(Math.round(total / 1000) / 60)}분 ${Math.round(total / 1000) % 60}초 (3분 미만)`;
    host.querySelectorAll(".l2s-sc").forEach((e, i) => e.classList.toggle("on", i === si));
    scaleStage();
    fitMath();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitMath);
    setTimeout(fitMath, 350);
  }

  /* ------------------------------------------------------------------ 음성 */
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
      const u = new SpeechSynthesisUtterance(text);
      KEEP.push(u);
      u.lang = "ko-KR";
      if (voice) u.voice = voice;
      u.rate = rate;
      u.pitch = pitch;
      let done = false, started = false, tm = 0, ts = 0;
      const fin = ok => {
        if (done) return;
        done = true;
        clearTimeout(tm);
        clearTimeout(ts);
        const k = KEEP.indexOf(u);
        if (k >= 0) KEEP.splice(k, 1);
        res(ok);
      };
      u.onstart = () => { started = true; clearTimeout(ts); setState("읽는 중…"); };
      u.onend = () => fin(true);
      u.onerror = () => fin(false);
      tm = setTimeout(() => fin(started), Math.max(7000, text.length * 360));
      ts = setTimeout(() => {
        if (!started) {
          try { speechSynthesis.cancel(); } catch (e) { /* 무시 */ }
          fin(false);
        }
      }, 3000);
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
    setState("");
    return true;
  }

  /* ------------------------------------------------------------------ 재생 */
  async function playFrom(si, pi) {
    stopAllPlayers();
    const my = ++runId;
    playing = true;
    const btn = qid("Play");
    if (btn) btn.textContent = "일시정지";
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
    runId++;
    playing = false;
    const b = qid("Play");
    if (b) b.textContent = "재생";
    if (window.speechSynthesis) { try { speechSynthesis.cancel(); } catch (e) { /* 무시 */ } }
  }
  function step(d) {
    const was = playing;
    stop();
    let { s, p } = cur;
    p += d;
    if (p < 0) { s = Math.max(0, s - 1); p = SCENES[s].parts.length - 1; }
    else if (p >= SCENES[s].parts.length) { s = Math.min(SCENES.length - 1, s + 1); p = 0; }
    render(s, p, false);
    if (was) playFrom(s, p);
  }
  function fillVoices() {
    const sel = qid("Voice");
    if (!sel || !window.speechSynthesis) return;
    const vs = speechSynthesis.getVoices().filter(v => /^ko/i.test(v.lang)).sort((a, b) => NATURAL(b) - NATURAL(a)), cur0 = sel.value;
    sel.innerHTML = vs.map(v => `<option value="${v.name}">${NATURAL(v) ? "★ " : ""}${v.name}</option>`).join("") || `<option value="">기본 음성</option>`;
    if (cur0) sel.value = cur0;
  }

  function init() {
    const mount = $(cfg.hostId);
    if (!mount || mount.dataset.ready) return;
    if (!window.katex) { setTimeout(init, 300); return; }
    mount.dataset.ready = "1";
    mount.innerHTML = `${chainNavHtml(cfg.lec)}
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

    host = mount;
    frameEl = qid("Frame");
    stageEl = qid("Stage");
    new ResizeObserver(scaleStage).observe(frameEl);

    mount.onclick = e => {
      const cb = e.target.closest("[data-chain-lec]");
      if (cb) { openLectureShorts(+cb.dataset.chainLec); return; }
      const lb = e.target.closest("[data-lec]");
      if (lb) { openLectureShorts(+lb.dataset.lec); }
    };
    qid("Play").onclick = () => { if (playing) stop(); else playFrom(cur.s, cur.p); };
    qid("Prev").onclick = () => step(-1);
    qid("Next").onclick = () => step(1);
    qid("List").onclick = e => {
      const it = e.target.closest("[data-i]");
      if (!it) return;
      const was = playing;
      stop();
      render(+it.dataset.i, 0, false);
      if (was) playFrom(+it.dataset.i, 0);
    };
    qid("Test").onclick = async () => {
      stop();
      qid("VoiceOn").checked = true;
      setState("시험 중…");
      const ok = await speak("안녕하세요. 수학 투 핵심 공식을 함께 정리해 볼까요?");
      setState(ok ? "소리가 정상입니다" : "소리가 시작되지 않았습니다");
    };
    if (window.speechSynthesis) {
      speechSynthesis.addEventListener("voiceschanged", fillVoices);
      setTimeout(fillVoices, 300);
    }
    render(0, 0, false);
  }

  const api = { init, render, stop, SCENES, scaleStage };
  PLAYERS[cfg.lec] = api;
  return api;
}

/* 제2강(#l2ShortsHost)에도 연계 숏츠 순서 바로가기 막대 연결 및 스크롤 이동 연동 */
function enhanceL2Host() {
  const m2 = $("l2ShortsHost");
  if (!m2 || m2.dataset.chainEnhanced) return;
  if (!m2.querySelector(".l2s-wrap")) { setTimeout(enhanceL2Host, 250); return; }
  m2.dataset.chainEnhanced = "1";
  const nav = document.createElement("div");
  nav.innerHTML = chainNavHtml(2);
  m2.insertBefore(nav.firstElementChild, m2.firstChild);
  m2.addEventListener("click", e => {
    const cb = e.target.closest("[data-chain-lec]");
    if (cb) { openLectureShorts(+cb.dataset.chainLec); return; }
    const lb = e.target.closest("[data-lec]");
    if (lb) {
      e.stopPropagation();
      openLectureShorts(+lb.dataset.lec);
    }
  }, true);
}

function initAll() {
  ALL_CONFIGS.forEach(cfg => {
    if (!PLAYERS[cfg.lec]) createShortsPlayer(cfg);
    PLAYERS[cfg.lec].init();
  });
  enhanceL2Host();
}

window.Math2Shorts = { PLAYERS, ALL_CONFIGS, initAll, openLectureShorts };
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initAll);
else initAll();
window.addEventListener("load", initAll);
})();

