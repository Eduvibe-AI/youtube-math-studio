/* 제2강 · 정적분 넓이 만능 공식 — 숏츠식 판서 샘플 (대본·그림·움직임 모두 직접 만든 것)
   9:16 세로 화면에서 식 조각이 연결선을 따라 움직이며 공식이 조립된다. 음성은 브라우저 내장 음성(한국어)을 쓴다.
   ∫_α^β (x−α)^m (β−x)^n dx = m!·n!/(m+n+1)! · (β−α)^(m+n+1) */
(function () {
"use strict";
const $ = id => document.getElementById(id);
const K = (tex, disp) => { try { return window.katex.renderToString(tex, { displayMode: !!disp, throwOnError: false }); } catch (e) { return String(tex); } };
const inline = s => String(s || "").replace(/\$([^$]+)\$/g, (m, t) => K(t));
const reduced = () => matchMedia("(prefers-reduced-motion: reduce)").matches;
const sleep = ms => new Promise(r => setTimeout(r, ms));
const CY = "#38bdf8", PK = "#f472b6", GO = "#fbbf24";
const cl = (c, t) => `\\textcolor{${c}}{${t}}`;

/* ------------------------------------------------------------------ 대본 */
const SCENES = [
  { id: "hook", type: "hook", title: "정적분 넓이 만능 공식", sub: "30초 풀이", parts: [{ say: "정적분 넓이 만능 공식, 30초 만에 정리합니다.", cap: "정적분 넓이 만능 공식 · 30초 풀이" }] },
  { id: "why", type: "list", head: "이 공식을 배우는 이유", parts: [
    { say: "곡선과 엑스축 사이의 넓이, 매번 적분하면 길지만 이 공식은 한 줄입니다.", cap: "매번 적분하면 길다 → 이 공식 한 줄로" }
  ] },
  { id: "hist", type: "list", head: "공식의 뿌리", parts: [
    { tag: "18세기", say: "이 적분은 오일러가 연구한 베타 적분이고, 지금 보는 것은 그 정수 꼴입니다.", cap: "오일러의 베타 적분의 정수 꼴" }
  ] },
  { id: "formula", type: "chips", head: "공식 만들기", parts: [
    { say: "공식은 이렇습니다. 엑스 빼기 알파의 엠 제곱, 베타 빼기 엑스의 엔 제곱을 알파에서 베타까지 적분합니다.", cap: "알파에서 베타까지, 두 근을 가진 식" },
    { say: "엠과 엔이 분자로 내려와 엠 팩토리얼, 엔 팩토리얼이 됩니다.", cap: "지수 $m$, $n$ 이 분자로 내려온다" },
    { say: "분모에는 엠 더하기 엔 더하기 일의 팩토리얼이 들어갑니다.", cap: "분모 $(m+n+1)!$" },
    { say: "마지막으로 구간의 길이 베타 빼기 알파를, 엠 더하기 엔 더하기 일 제곱 해서 곱합니다.", cap: "길이 $(\\beta-\\alpha)^{m+n+1}$" },
    { say: "이것이 정적분 넓이 만능 공식입니다.", cap: "정적분 넓이 만능 공식" }
  ] },
  { id: "ex", type: "chips", head: "예제", parts: [
    { say: "예를 들어 엑스 제곱 곱하기 삼 빼기 엑스의, 영에서 삼까지 넓이입니다. 영은 이중근이라 엠은 이, 삼은 단일근이라 엔은 일입니다.", cap: "$m=2,\\ n=1$ · 영에서 삼까지의 넓이" },
    { say: "지수 이와 일이 분자의 이 팩토리얼, 일 팩토리얼로 내려옵니다.", cap: "분자 $2!\\cdot 1!$" },
    { say: "분모는 이 더하기 일 더하기 일, 사 팩토리얼입니다.", cap: "분모 $4!$" },
    { say: "구간의 길이는 삼이니까 삼의 사 제곱을 곱합니다.", cap: "길이 $3^{4}$" },
    { say: "계산하면 분자는 이, 분모는 이십사, 삼의 사 제곱은 팔십일입니다.", cap: "$2,\\ 24,\\ 81$" },
    { say: "십이분의 일 곱하기 팔십일, 넓이는 사분의 이십칠입니다.", cap: "넓이 $=\\dfrac{27}{4}$" }
  ] },
  { id: "exam", type: "chips", head: "수능·모의고사 적용", parts: [
    { say: "수능형 문제입니다. 곡선 에이 엑스 제곱 곱하기 엑스 빼기 삼과 엑스축이 이루는 넓이가 이분의 이십칠일 때, 에이는?", cap: "넓이가 $\\dfrac{27}{2}$ 일 때 $a$ 의 값은?  (수능형 · 직접 만든 문항)" },
    { say: "엠은 이, 엔은 일. 그래프가 엑스축 아래여도 넓이는 절댓값으로 계산합니다.", cap: "$m=2,\\ n=1$ · 그래프가 아래여도 넓이는 양수" },
    { say: "공식에 넣으면, 절댓값 에이 곱하기 이 팩토리얼 일 팩토리얼 나누기 사 팩토리얼 곱하기 삼의 사 제곱입니다.", cap: "$|a|\\times\\dfrac{2!\\,1!}{4!}\\times 3^{4}$" },
    { say: "계산하면 십이분의 일 곱하기 팔십일, 사분의 이십칠 에이입니다.", cap: "$\\dfrac{27}{4}\\,|a|$" },
    { say: "이분의 이십칠과 같으니, 에이는 이입니다. 여러 줄이던 계산이 한 줄로 끝납니다.", cap: "$a=2$ · 직접 적분하면 여러 줄 → 공식으로 한 줄" }
  ] },
  { id: "tips", type: "list", head: "실전 꿀팁", parts: [
    { say: "꿀팁 하나, 엠과 엔부터 읽습니다.", cap: "① $m$, $n$ 먼저 읽기" },
    { say: "둘, 거듭제곱은 엠 더하기 엔 더하기 일이고, 길이는 베타 빼기 알파입니다.", cap: "② 길이 $(\\beta-\\alpha)^{m+n+1}$" },
    { say: "셋, 곡선 앞의 계수는 절댓값으로 곱합니다.", cap: "③ 넓이 $S=|a|\\cdot\\dfrac{m!\\,n!}{(m+n+1)!}(\\beta-\\alpha)^{m+n+1}$" }
  ] }
,
  { id: "next", type: "list", head: "다음에 이어서 볼 내용", parts: [
    { tag: "적용 ①", say: "다음은 두 곡선 사이의 넓이입니다. 두 함수의 차를 한 식으로 묶으면 오늘 공식이 적용됩니다.", cap: "두 곡선 사이의 넓이 · 차를 한 식으로 묶기: $f(x)-g(x)=a(x-\\alpha)^{m}(x-\\beta)^{n}$" },
    { tag: "적용 ②", say: "곡선과 접선 사이의 넓이도 자주 나오고, 접점은 이중근입니다.", cap: "곡선과 접선 사이의 넓이 · 접점은 이중근이라 $m=2$" },
    { tag: "이 사이트", say: "이 사이트의 제구강과 제일강을 이어서 보세요.", cap: "제9강 · 정적분과 넓이 & 차함수의 마법  /  제1강 · 다항함수 넓이의 비" }
  ] }
];
const estMs = t => Math.max(1800, Math.round(Array.from(t || "").length * 165) + 600);
SCENES.forEach(s => { s.parts.forEach(p => { p.ms = estMs(p.say); }); s.ms = s.parts.reduce((a, p) => a + p.ms, 0); });

/* ---- 그래프 설정: 예제(a=1) 곡선은 x²(3−x), 수능형 문제는 a x²(x−3) (a=1에서 시작해 a=2로 늘어난다) ---- */
const GRAPH_EX = { f: x => x * x * (3 - x), GY0: 400, GV: 70, xr: [-0.3, 3.1], area: [0, 3], ytop: 40, ybot: 450, labelY: 454,
  r1: { x: 0, col: CY, label: "0 · 이중근 (m=2)" }, r2: { x: 3, col: PK, label: "3 · 단일근 (n=1)" }, fn: { t: "y = x²(3 − x)", x: 640, y: 110 }, sPos: [450, 308], sOpenTxt: "S", finalS: "S = 27/4", finalPh: 5, scaleTo: 1 };
const GRAPH_EXAM = { f: x => x * x * (x - 3), GY0: 110, GV: 42, xr: [-0.3, 3.1], area: [0, 3], ytop: 30, ybot: 470, labelY: 72,
  r1: { x: 0, col: CY, label: "0 · 이중근 (m=2)" }, r2: { x: 3, col: PK, label: "3 · 단일근 (n=1)" }, fn: { t: "y = a·x²(x − 3)", x: 690, y: 440 }, sPos: [450, 205], sOpenTxt: "S", finalS: "a = 2 · S = 27/2", finalPh: 4, scaleTo: 2 };

/* ------------------------------------------------------------------ 식 조각 장면 정의 */
const chipDefs = {
  formula: (() => {
    const src = { Fm: [360, 60], Fn: [640, 60], Fd: [500, 60], Fp: [335, 530] };
    const fin = { Fm: [250, 380], Fn: [440, 380], Fd: [345, 520], Fp: [760, 455] };
    return {
      chips: [
        { id: "T1", tex: "\\displaystyle\\int_{\\alpha}^{\\beta}", cls: "pl" }, { id: "T2", tex: `(x-\\alpha)^{${cl(CY, "m")}}`, cls: "cy" }, { id: "T3", tex: `(\\beta-x)^{${cl(PK, "n")}}`, cls: "pk" }, { id: "T4", tex: "dx", cls: "pl" },
        { id: "E", tex: "=", cls: "pl" }, { id: "Fm", tex: "m!", cls: "cy" }, { id: "Fn", tex: "n!", cls: "pk" }, { id: "bar", tex: "", cls: "bar" },
        { id: "Fd", tex: "(m+n+1)!", cls: "go" }, { id: "Fp", tex: "(\\beta-\\alpha)^{m+n+1}", cls: "go sm" }
      ],
      state(ph) {
        const S = { T1: { x: 110, y: 60, op: 1 }, T2: { x: 360, y: 60, op: 1 }, T3: { x: 640, y: 60, op: 1 }, T4: { x: 840, y: 60, op: 1 } };
        const show = (id, minPh) => ({ x: ph >= minPh ? fin[id][0] : src[id][0], y: ph >= minPh ? fin[id][1] : src[id][1], op: ph >= minPh ? 1 : 0 });
        S.E = { x: 70, y: 450, op: ph >= 1 ? 1 : 0 }; S.bar = { x: 345, y: 500, op: ph >= 1 ? 1 : 0, w: 400 };
        S.Fm = show("Fm", 1); S.Fn = show("Fn", 1); S.Fd = show("Fd", 2); S.Fp = show("Fp", 3);
        if (ph >= 4) Object.keys(S).forEach(k => { if (k !== "bar") S[k].pop = 1; });
        return S;
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T2", b: "Fm", col: CY }, { a: "T3", b: "Fn", col: PK });
        if (ph === 2) L.push({ a: "T2", b: "Fd", col: CY }, { a: "T3", b: "Fd", col: PK, label: "m + n + 1" });
        if (ph === 3) L.push({ a: "Fd", b: "Fp", col: GO });
        return L;
      },
      fx: ph => ph === 4 ? "spark" : ""
    };
  })(),
  ex: (() => {
    const src = { Fm: [340, 10], Fn: [600, 10], Fd: [470, 10], Fp: [335, 335] };
    const fin = { Fm: [250, 190], Fn: [440, 190], Fd: [345, 335], Fp: [740, 255] };
    return {
      graph: GRAPH_EX,
      chips: [
        { id: "T1", tex: "\\displaystyle\\int_{0}^{3}", cls: "pl" }, { id: "T2", tex: `x^{${cl(CY, "2")}}`, cls: "cy" }, { id: "T3", tex: `(3-x)^{${cl(PK, "1")}}`, cls: "pk" }, { id: "T4", tex: "dx", cls: "pl" },
        { id: "E", tex: "=", cls: "pl" }, { id: "Fm", tex: "2!", cls: "cy" }, { id: "Fn", tex: "1!", cls: "pk" }, { id: "bar", tex: "", cls: "bar" },
        { id: "Fd", tex: "(2+1+1)!", cls: "go" }, { id: "Fp", tex: "\\times 3^{4}", cls: "go" }, { id: "R", tex: "\\dfrac{1}{12}\\times 81=\\dfrac{27}{4}", cls: "go big" }
      ],
      state(ph) {
        const S = { T1: { x: 110, y: 10, op: 1 }, T2: { x: 340, y: 10, op: 1 }, T3: { x: 600, y: 10, op: 1 }, T4: { x: 830, y: 10, op: 1 } };
        const show = (id, minPh) => ({ x: ph >= minPh ? fin[id][0] : src[id][0], y: ph >= minPh ? fin[id][1] : src[id][1], op: ph >= minPh ? 1 : 0 });
        S.E = { x: 70, y: 255, op: ph >= 1 ? 1 : 0 }; S.bar = { x: 345, y: 300, op: ph >= 1 ? 1 : 0, w: 400 };
        S.Fm = show("Fm", 1); S.Fn = show("Fn", 1); S.Fd = show("Fd", 2); S.Fp = show("Fp", 3);
        if (ph >= 4) { S.Fm.tex = "2"; S.Fn = { x: 250, y: 190, op: 0 }; S.Fd.tex = "24"; S.Fp.tex = "\\times 81"; S.Fm.pop = 1; S.Fd.pop = 1; S.Fp.pop = 1; }
        if (ph >= 5) { ["Fm", "Fn", "Fd", "Fp", "E"].forEach(k => { S[k].op = S[k].op ? 0.25 : 0; }); S.bar.op = 0.25; }
        S.R = { x: 480, y: 392, op: ph >= 5 ? 1 : 0, pop: ph >= 5 ? 1 : 0 };
        return S;
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T2", b: "Fm", col: CY }, { a: "T3", b: "Fn", col: PK });
        if (ph === 2) L.push({ a: "T2", b: "Fd", col: CY }, { a: "T3", b: "Fd", col: PK, label: "2 + 1 + 1" });
        if (ph === 3) L.push({ a: "Fd", b: "Fp", col: GO });
        return L;
      },
      fx: ph => ph === 5 ? "confetti" : ph === 4 ? "spark" : ""
    };
  })()  ,
  exam: (() => {
    const src = { M: [330, 0], N: [560, 0], Wa: [160, 112], X1: [270, 112], Wb: [400, 112], X2: [540, 112], Wc: [660, 112] };
    return {
      graph: GRAPH_EXAM,
      chips: [
        { id: "T1", tex: "f(x)=a", cls: "pl" }, { id: "T2", tex: `x^{${cl(CY, "2")}}`, cls: "cy" }, { id: "T3", tex: `(x-3)^{${cl(PK, "1")}}`, cls: "pk" }, { id: "T4", tex: "S=\\dfrac{27}{2}", cls: "go" },
        { id: "M", tex: "m=2", cls: "cy" }, { id: "N", tex: "n=1", cls: "pk" },
        { id: "Wa", tex: "|a|", cls: "pl" }, { id: "X1", tex: "\\times", cls: "pl" }, { id: "Wb", tex: "\\dfrac{2!\\,1!}{4!}", cls: "go" }, { id: "X2", tex: "\\times", cls: "pl" }, { id: "Wc", tex: "3^{4}", cls: "go" },
        { id: "Z", tex: "\\dfrac{27}{4}\\,|a|", cls: "go" }, { id: "V", tex: "\\dfrac{27}{4}\\,a=\\dfrac{27}{2}\\ \\Rightarrow\\ a=2", cls: "go v" }
      ],
      state(ph) {
        const S = { T1: { x: 120, y: 0, op: 1 }, T2: { x: 330, y: 0, op: 1 }, T3: { x: 560, y: 0, op: 1 }, T4: { x: 815, y: 0, op: 1 } };
        const at = (id, minPh, fin) => ({ x: ph >= minPh ? fin[0] : src[id][0], y: ph >= minPh ? fin[1] : src[id][1], op: ph >= minPh ? 1 : 0 });
        S.M = at("M", 1, [330, 112]); S.N = at("N", 1, [560, 112]);
        const row = (id, fin) => Object.assign(at(id, 2, fin), { op: ph >= 2 ? (ph >= 3 ? 0.25 : 1) : 0 });
        S.Wa = row("Wa", [130, 228]); S.X1 = row("X1", [245, 228]); S.Wb = row("Wb", [400, 228]); S.X2 = row("X2", [560, 228]); S.Wc = row("Wc", [690, 228]);
        if (ph >= 2) { ["Wa", "X1", "Wb", "X2", "Wc"].forEach(k => { S[k].x = { Wa: 130, X1: 245, Wb: 400, X2: 560, Wc: 690 }[k]; S[k].y = 228; }); }
        S.M.op = ph >= 1 ? (ph >= 2 ? 0.45 : 1) : 0; S.N.op = ph >= 1 ? (ph >= 2 ? 0.45 : 1) : 0;
        S.Z = { x: 480, y: 325, op: ph >= 3 ? 1 : 0, pop: ph === 3 ? 1 : 0 };
        S.V = { x: 480, y: 405, op: ph >= 4 ? 1 : 0, pop: ph >= 4 ? 1 : 0 };
        return S;
      },
      links(ph) {
        const L = [];
        if (ph === 1) L.push({ a: "T2", b: "M", col: CY }, { a: "T3", b: "N", col: PK });
        if (ph === 2) L.push({ a: "M", b: "Wb", col: CY }, { a: "N", b: "Wb", col: PK, label: "2! · 1! / 4!" });
        return L;
      },
      fx: ph => ph === 4 ? "confetti" : ph === 3 ? "spark" : ""
    };
  })()

};

/* ------------------------------------------------------------------ 화면 */
const CSS = `
/* 부드러운 글씨체: 고운돋움(Gowun Dodum, SIL OFL). 수식(KaTeX)은 자체 글꼴을 그대로 쓴다 */
@font-face{font-family:"GowunDodumL2";font-display:swap;src:url(fonts_l2/gowun-dodum-korean-400.woff2) format("woff2");unicode-range:U+AC00-D7A3,U+3131-318E,U+1100-11FF,U+00B7,U+2018-201D,U+2026,U+203B,U+2192}
@font-face{font-family:"GowunDodumL2";font-display:swap;src:url(fonts_l2/gowun-dodum-latin-400.woff2) format("woff2");unicode-range:U+0000-00FF,U+2000-206F}
.l2s-wrap{display:flex;gap:26px;flex-wrap:wrap;align-items:flex-start}
.l2s-frame{width:360px;max-width:100%;aspect-ratio:9/16;position:relative;border-radius:18px;overflow:hidden;background:#0a0f1f;box-shadow:0 14px 38px rgba(0,0,0,.55);flex:none}
.l2s-stage{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:0 0;overflow:hidden;color:#f1f5f9;--serif:"GowunDodumL2","Noto Sans KR","Malgun Gothic","Apple SD Gothic Neo",sans-serif;font-family:var(--serif);
  background:radial-gradient(circle at 18% 12%,rgba(56,189,248,.34),transparent 46%),radial-gradient(circle at 86% 82%,rgba(244,114,182,.30),transparent 46%),radial-gradient(circle at 70% 30%,rgba(251,191,36,.14),transparent 40%),linear-gradient(180deg,#0a0f1f,#121b38);background-size:150% 150%,150% 150%,150% 150%,100% 100%;animation:l2sBg 11s ease-in-out infinite alternate}
@keyframes l2sBg{from{background-position:0% 0%,100% 100%,60% 20%,0 0}to{background-position:100% 60%,0% 20%,20% 80%,0 0}}
.l2s-board{position:absolute;left:60px;right:60px;top:330px;height:1130px}
.l2s-cap{position:absolute;left:60px;right:60px;bottom:110px;height:300px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:54px;line-height:1.5;font-weight:700}
.l2s-cap>span{background:rgba(0,0,0,.62);padding:10px 26px;border-radius:10px;animation:l2sCap .5s cubic-bezier(.2,1.2,.3,1) both}
@keyframes l2sCap{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
.l2s-bar{position:absolute;left:0;bottom:0;height:12px;background:#38bdf8;width:0}
.l2s-big{font-size:92px;word-break:keep-all;font-weight:800;color:#fff;text-align:center;line-height:1.5;margin-top:240px;text-decoration:underline;text-decoration-color:#fbbf24;text-decoration-thickness:8px;text-underline-offset:24px;animation:l2sZoom .6s ease both}
@keyframes l2sZoom{from{opacity:0;transform:scale(.7)}to{opacity:1;transform:none}}
.l2s-sub{text-align:center;color:#cbd5e1;font-size:56px;margin-top:40px}
.l2s-head{text-align:left;color:#fff;font-size:72px;font-weight:800;border-left:16px solid #fbbf24;padding-left:28px;margin:8px 0 40px;line-height:1.3}
.l2s-item{display:flex;align-items:center;gap:22px;border-bottom:2px solid rgba(255,255,255,.28);padding:30px 8px;margin:4px 0;font-size:56px;line-height:1.55;font-weight:600;animation:l2sIn .55s ease-out both}
.l2s-item.cur{border-bottom-color:#fbbf24}
.l2s-item em{font-style:normal;color:#fbbf24;border:3px solid #fbbf24;border-radius:8px;font-size:38px;font-weight:800;padding:4px 18px;white-space:nowrap}
@keyframes l2sIn{from{opacity:0;transform:translateY(80px) scale(.94)}to{opacity:1;transform:none}}
.l2s-stage .katex{font-family:KaTeX_Main,"Times New Roman",serif}
.l2s-stage .katex-html{white-space:nowrap}
.l2s-stage .katex .base{width:max-content}
.l2s-itbody{display:flex;flex-direction:column;gap:8px;min-width:0;flex:1}
.l2s-lab{display:block}
.l2s-itbody.txt{display:block}
.l2s-eq,.l2s-capeq{display:block;white-space:nowrap;text-align:center}
.l2s-cap>span{max-width:100%;box-sizing:border-box}
.l2s-chips{position:absolute;left:0;top:150px;width:960px;height:930px}
.l2s-chips.g{top:618px;height:700px}
.l2s-graph{position:absolute;left:0;top:110px;width:960px;height:480px;overflow:visible}
.l2s-graph text{font-family:var(--serif);paint-order:stroke;stroke:#0b1020;stroke-width:6px}
.l2s-links{position:absolute;left:0;top:0;width:960px;height:930px;overflow:visible;pointer-events:none}
.l2s-links path{fill:none;stroke-width:9;stroke-linecap:round;filter:drop-shadow(0 0 10px currentColor)}
.l2s-links text{font-size:40px;font-weight:800;text-anchor:middle;paint-order:stroke;stroke:#0b1020;stroke-width:7px}
.l2c{position:absolute;left:0;top:0;width:max-content;text-align:center;font-size:56px;line-height:1.25;padding:12px 24px;border-radius:18px;white-space:nowrap;will-change:transform,opacity;transition:opacity .5s,box-shadow .4s}
.l2c.pl{background:none}
.l2c.cy,.l2c.pk,.l2c.go{background:linear-gradient(180deg,rgba(51,65,85,.96),rgba(15,23,42,.96));border:3px solid #475569;box-shadow:0 12px 30px rgba(0,0,0,.45)}
.l2c.cy{border-color:${CY};box-shadow:0 0 30px rgba(56,189,248,.42),0 12px 30px rgba(0,0,0,.4)}
.l2c.pk{border-color:${PK};box-shadow:0 0 30px rgba(244,114,182,.42),0 12px 30px rgba(0,0,0,.4)}
.l2c.go{border-color:${GO};box-shadow:0 0 36px rgba(251,191,36,.5),0 12px 30px rgba(0,0,0,.4)}
.l2c.big{font-size:78px;padding:22px 40px}
.l2c.sm{font-size:44px;padding:10px 20px}
.l2c.v{font-size:58px;padding:14px 28px}
.l2c.bar{height:7px;padding:0;border-radius:6px;background:${GO};box-shadow:0 0 18px rgba(251,191,36,.6)}
.l2c.ghost{pointer-events:none;filter:blur(3px);box-shadow:none}
.l2s-fx{position:absolute;pointer-events:none;border-radius:50%}
.l2s-conf{position:absolute;top:-60px;width:22px;height:34px;border-radius:5px;pointer-events:none}
.l2s-ctl{display:flex;flex-direction:column;gap:12px;min-width:260px;flex:1}
.l2s-row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.l2s-btn{border:1.5px solid #334155;background:#1e293b;color:#e2e8f0;border-radius:10px;padding:8px 16px;font:inherit;font-weight:700;cursor:pointer}
.l2s-btn.pri{background:#2563eb;border-color:#2563eb;color:#fff}
.l2s-opt{display:flex;gap:14px;flex-wrap:wrap;align-items:center;font-size:.9rem;color:var(--text-dim,#94a3b8)}
.l2s-opt select{background:#0f172a;color:#e2e8f0;border:1px solid #334155;border-radius:8px;padding:5px 8px}
.l2s-state{font-size:.9rem;font-weight:700;min-height:1.4em;color:#fbbf24}
.l2s-list{display:flex;flex-direction:column;gap:6px;max-height:340px;overflow:auto}
.l2s-sc{border:1px solid #334155;border-radius:10px;padding:8px 12px;cursor:pointer;font-size:.9rem;color:#cbd5e1}
.l2s-sc.on{border-color:#38bdf8;background:rgba(56,189,248,.1)}
.l2s-note{font-size:.85rem;color:var(--text-dim,#94a3b8);line-height:1.6}
`;

let host, stageEl, frameEl, cur = { s: 0, p: 0 }, runId = 0, playing = false, curDef = null, curDefId = "";
const KEEP = [];
const total = SCENES.reduce((a, s) => a + s.ms, 0);

function scaleStage() { if (frameEl && stageEl) stageEl.style.transform = `scale(${frameEl.clientWidth / 1080})`; }

function burst(x, y, n, colors) {
  const h = stageEl.querySelector(".l2s-chips"); if (!h || reduced()) return;
  for (let i = 0; i < n; i++) {
    const d = document.createElement("div"); d.className = "l2s-fx"; const sz = 10 + Math.random() * 16, c = colors[i % colors.length];
    d.style.cssText = `left:${x}px;top:${y}px;width:${sz}px;height:${sz}px;background:${c};box-shadow:0 0 18px ${c}`; h.appendChild(d);
    const a = Math.random() * Math.PI * 2, r = 90 + Math.random() * 150;
    d.animate([{ transform: "translate(0,0) scale(1)", opacity: 1 }, { transform: `translate(${Math.cos(a) * r}px,${Math.sin(a) * r}px) scale(.2)`, opacity: 0 }], { duration: 700 + Math.random() * 400, easing: "cubic-bezier(.1,.8,.3,1)" }).onfinish = () => d.remove();
  }
}
function confetti() {
  if (reduced()) return; const cs = ["#fbbf24", "#f472b6", "#38bdf8", "#34d399", "#a78bfa", "#fb7185"];
  for (let i = 0; i < 46; i++) {
    const d = document.createElement("div"); d.className = "l2s-conf"; d.style.cssText = `left:${Math.random() * 1040}px;background:${cs[i % cs.length]}`; stageEl.appendChild(d);
    d.animate([{ transform: "translateY(0) rotate(0deg)", opacity: 1 }, { transform: `translate(${(Math.random() - 0.5) * 240}px,${1500 + Math.random() * 400}px) rotate(${(Math.random() - 0.5) * 1080}deg)`, opacity: 0.9 }], { duration: 1800 + Math.random() * 1400, delay: Math.random() * 500, easing: "cubic-bezier(.3,.1,.6,1)" }).onfinish = () => d.remove();
  }
}
const tf = (x, y, extra) => `translate(${x}px,${y}px) translate(-50%,0)${extra || ""}`;
function fly(hostEl, m, n) {
  const { el, x0, y0, o, dist } = m, arc = 70 + Math.min(150, dist * 0.2), mx = (x0 + o.x) / 2, my = (y0 + o.y) / 2 - arc, rot = (o.x >= x0 ? 1 : -1) * (7 + Math.random() * 7), delay = n * 80 + 350;
  el.style.transform = tf(o.x, o.y);
  if (reduced()) return;
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
/* ---------- 그래프: 곡선 · 영역 · 근 표시 (설정값 cfg 로 예제·수능형 문제가 함께 쓴다) ---------- */
const GX0 = 90, GU = 240;
function graphHtml(c) {
  const px = x => GX0 + GU * x, py = x => c.GY0 - c.GV * c.f(x);
  let d = "", first = true; for (let x = c.xr[0]; x <= c.xr[1] + 0.001; x += 0.05) { d += (first ? "M" : "L") + px(x).toFixed(1) + " " + py(x).toFixed(1) + " "; first = false; }
  let a = `M ${px(c.area[0])} ${c.GY0} `; for (let x = c.area[0]; x <= c.area[1] + 0.001; x += 0.05) a += `L ${px(x).toFixed(1)} ${py(x).toFixed(1)} `; a += `L ${px(c.area[1])} ${c.GY0} Z`;
  return `<svg class="l2s-graph" viewBox="0 0 960 480">
    <defs><clipPath id="l2gClip"><rect id="l2gClipR" x="0" y="0" width="0" height="480"></rect></clipPath></defs>
    <g stroke="rgba(255,255,255,.45)" stroke-width="3" fill="none"><line x1="20" y1="${c.GY0}" x2="900" y2="${c.GY0}"></line><line x1="${GX0}" y1="${c.ybot}" x2="${GX0}" y2="${c.ytop}"></line></g>
    <text x="925" y="${c.GY0 + 12}" fill="#cbd5e1" font-size="38">x</text><text x="${GX0 + 18}" y="${c.ytop + 8}" fill="#cbd5e1" font-size="38">y</text>
    <g id="l2gScale" style="transform-origin:0 ${c.GY0}px">
      <path id="l2gArea" d="${a}" fill="rgba(251,191,36,.38)" clip-path="url(#l2gClip)"></path>
      <path id="l2gCurve" d="${d}" fill="none" stroke="#e2e8f0" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke" style="filter:drop-shadow(0 0 8px rgba(226,232,240,.5))"></path>
    </g>
    <g id="l2gRoots" opacity="0"><circle cx="${px(c.r1.x)}" cy="${c.GY0}" r="15" fill="${c.r1.col}"></circle><circle cx="${px(c.r2.x)}" cy="${c.GY0}" r="15" fill="${c.r2.col}"></circle>
      <text x="${px(c.r1.x)}" y="${c.labelY}" fill="${c.r1.col}" font-size="36" text-anchor="middle">${c.r1.label}</text><text x="${px(c.r2.x)}" y="${c.labelY}" fill="${c.r2.col}" font-size="36" text-anchor="middle">${c.r2.label}</text></g>
    <text id="l2gFn" x="${c.fn.x}" y="${c.fn.y}" fill="#e2e8f0" font-size="40" opacity="0">${c.fn.t}</text>
    <text id="l2gS" x="${c.sPos[0]}" y="${c.sPos[1]}" fill="${GO}" font-size="62" font-weight="800" text-anchor="middle" opacity="0">${c.sOpenTxt}</text>
  </svg>`;
}
function graphPhase(host, ph, animate, fresh, c) {
  const q = id => host.querySelector("#" + id); if (!q("l2gCurve")) return;
  const curve = q("l2gCurve"), L = curve.getTotalLength(), area = q("l2gArea"), clipR = q("l2gClipR"), roots = q("l2gRoots"), fn = q("l2gFn"), S = q("l2gS"), sc = q("l2gScale");
  if (fresh) {
    if (animate && !reduced()) {
      curve.style.strokeDasharray = L; curve.animate([{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: 1800, easing: "cubic-bezier(.4,.1,.3,1)", fill: "both" });
      clipR.animate([{ width: "0px" }, { width: "960px" }], { duration: 1500, delay: 1500, easing: "ease-out", fill: "both" });
      roots.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 500, delay: 900, fill: "both" });
      fn.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 600, delay: 1200, fill: "both" });
    } else { clipR.setAttribute("width", 960); roots.setAttribute("opacity", 1); fn.setAttribute("opacity", 1); }
  }
  const reach = ph >= c.finalPh;
  if (c.scaleTo !== 1) {   // 수능형: 계수 a 가 1에서 2로 커지며 곡선이 아래로 늘어난다
    const to = reach ? c.scaleTo : 1;
    if (animate && !reduced() && reach && sc.dataset.s !== "2") { sc.animate([{ transform: "scaleY(1)" }, { transform: `scaleY(${to})` }], { duration: 1100, easing: "cubic-bezier(.3,1.3,.4,1)", fill: "both" }); }
    else sc.style.transform = `scaleY(${to})`;
    sc.dataset.s = reach ? "2" : "1";
  }
  if (reach) {
    S.textContent = c.finalS; S.setAttribute("opacity", 1); S.setAttribute("font-size", 62);
    if (animate && !reduced()) { S.animate([{ opacity: 0, transform: "scale(.6)" }, { opacity: 1, transform: "scale(1)" }], { duration: 600, easing: "cubic-bezier(.2,1.4,.4,1)", fill: "both" }); area.animate([{ fillOpacity: 1 }, { fillOpacity: 1.9 }, { fillOpacity: 1 }], { duration: 900 }); }
  } else { S.textContent = c.sOpenTxt; S.setAttribute("opacity", fresh && animate ? 0 : 1); if (fresh && animate && !reduced()) S.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 500, delay: 2600, fill: "both" }); }
}
function renderChips(sc, k, animate) {
  const def = chipDefs[sc.id]; let chipsEl = stageEl.querySelector(".l2s-chips"), fresh = false;
  if (!chipsEl || curDefId !== sc.id) {
    fresh = true; curDefId = sc.id; curDef = def;
    stageEl.querySelector(".l2s-board").innerHTML = `<div class="l2s-head" style="margin-bottom:0">${sc.head}</div>${def.graph ? graphHtml(def.graph) : ""}<div class="l2s-chips ${def.graph ? "g" : ""}"><svg class="l2s-links" viewBox="0 0 960 930"></svg>${def.chips.map(c => `<div class="l2c ${c.cls}" data-id="${c.id}"></div>`).join("")}</div>`;
    chipsEl = stageEl.querySelector(".l2s-chips");
    const S0 = def.state(0);
    def.chips.forEach(c => { const el = chipsEl.querySelector(`[data-id="${c.id}"]`), o = S0[c.id]; el.innerHTML = c.tex ? K(c.tex) : ""; el.dataset.h = c.tex; el.dataset.x = o.x; el.dataset.y = o.y; el.style.transform = tf(o.x, o.y); el.style.opacity = o.op; if (o.w) el.style.width = o.w + "px"; });
  }
  const S = def.state(k), flying = [];
  def.chips.forEach(c => {
    const el = chipsEl.querySelector(`[data-id="${c.id}"]`), o = S[c.id], tex = o.tex != null ? o.tex : c.tex;
    const x0 = +el.dataset.x, y0 = +el.dataset.y, dist = Math.hypot(o.x - x0, o.y - y0), seen = (+el.style.opacity || 0) > 0.05 || o.op > 0.05, changed = el.dataset.h !== tex;
    if (changed) { el.innerHTML = K(tex); el.dataset.h = tex; }
    if (o.w) el.style.width = o.w + "px";
    if (animate && dist > 8 && seen) flying.push({ el, x0, y0, o, dist }); else el.style.transform = tf(o.x, o.y);
    el.style.opacity = o.op; el.dataset.x = o.x; el.dataset.y = o.y;
    if (animate && o.pop && !(dist > 8) && (changed || !fresh) && o.op > 0.05 && !reduced()) {
      setTimeout(() => { const a = el.animate([{ transform: tf(o.x, o.y, " scale(1)") }, { transform: tf(o.x, o.y, " scale(1.35)"), offset: 0.4 }, { transform: tf(o.x, o.y, " scale(1)") }], { duration: 520, easing: "cubic-bezier(.2,1.4,.4,1)" }); a.onfinish = () => { el.style.transform = tf(o.x, o.y); }; burst(o.x, o.y + 40, 10, [GO, "#fde68a", PK, CY]); }, 450);
    }
  });
  flying.sort((a, b) => a.x0 - b.x0).forEach((m, n) => fly(chipsEl, m, n));
  drawLinks(chipsEl, def, S, k, animate);
  if (def.graph) graphPhase(stageEl.querySelector(".l2s-board"), k, animate, fresh, def.graph);
  const fxk = def.fx(k); if (animate && fxk === "confetti") setTimeout(confetti, 700);
  return sc.parts[k].cap;
}
/* 긴 수식은 글자 아래 한 줄로 내리고, 칸을 넘으면 글자 크기를 줄여 중간에 잘리지 않게 한다 */
const mathLen = s => (String(s).match(/\$([^$]+)\$/g) || []).reduce((a, m) => a + m.length - 2, 0);
function splitCap(cap) {
  const i = String(cap).indexOf("$");
  if (i < 0 || mathLen(cap) < 14) return { html: inline(cap) };
  return { label: cap.slice(0, i).trim(), eq: inline(cap.slice(i)) };
}
function fitMath() {
  if (!stageEl) return;
  stageEl.querySelectorAll(".l2s-fit").forEach(el => {
    el.style.fontSize = "";
    const box = el.closest(".l2s-fitbox") || el.parentElement, avail = box.clientWidth - 16, w = el.scrollWidth;
    if (w > avail && avail > 100) el.style.fontSize = (parseFloat(getComputedStyle(el).fontSize) * avail / w * 0.97) + "px";
  });
  stageEl.querySelectorAll(".l2c").forEach(el => { el.style.fontSize = ""; if (el.offsetWidth > 880) el.style.fontSize = (parseFloat(getComputedStyle(el).fontSize) * 880 / el.offsetWidth) + "px"; });
}
function listBoard(sc, k) {
  const its = sc.parts.map(p => ({ tag: p.tag || "", cap: p.cap })), upto = k >= 0 ? k + 1 : its.length;
  return `<div class="l2s-head">${sc.head}</div>` + its.slice(0, upto).map((x, n) => {
    const s = splitCap(x.cap);
    const body = s.eq ? `<span class="l2s-itbody l2s-fitbox"><span class="l2s-lab">${inline(s.label)}</span><span class="l2s-eq l2s-fit">${s.eq}</span></span>` : `<span class="l2s-itbody txt">${s.html}</span>`;
    return `<div class="l2s-item ${n === upto - 1 ? "cur" : ""}">${x.tag ? `<em>${x.tag}</em>` : ""}${body}</div>`;
  }).join("");
}
function render(si, pi, animate) {
  const sc = SCENES[si]; cur = { s: si, p: pi };
  if (!stageEl.querySelector(".l2s-board")) stageEl.innerHTML = `<div class="l2s-board"></div><div class="l2s-cap"><span></span></div><div class="l2s-bar" id="l2sBar"></div>`;
  let cap = sc.parts[pi].cap;
  if (sc.type === "chips") cap = renderChips(sc, pi, animate);
  else {
    curDefId = "";
    const b = stageEl.querySelector(".l2s-board");
    b.innerHTML = sc.type === "hook" ? `<div class="l2s-big">${sc.title}</div><div class="l2s-sub">${sc.sub}</div>` : listBoard(sc, pi);
  }
  const c = stageEl.querySelector(".l2s-cap span"), sp = splitCap(cap);
  c.innerHTML = sp.eq ? `<span class="l2s-lab">${inline(sp.label)}</span><span class="l2s-capeq l2s-fit">${sp.eq}</span>` : sp.html;
  stageEl.querySelector(".l2s-cap").classList.add("l2s-fitbox");
  c.style.animation = "none"; c.offsetWidth; c.style.animation = "";
  let before = 0; for (let i = 0; i < si; i++) before += SCENES[i].ms; for (let j = 0; j < pi; j++) before += sc.parts[j].ms;
  const bar = $("l2sBar"); if (bar) { bar.style.transition = "none"; bar.style.width = (before / total * 100) + "%"; if (animate) { bar.offsetWidth; bar.style.transition = `width ${sc.parts[pi].ms / 1000}s linear`; bar.style.width = ((before + sc.parts[pi].ms) / total * 100) + "%"; } }
  const st = $("l2sTime"); if (st) st.textContent = `${si + 1} / ${SCENES.length} 장면 · 예상 전체 ${Math.floor(Math.round(total / 1000) / 60)}분 ${Math.round(total / 1000) % 60}초`;
  host.querySelectorAll(".l2s-sc").forEach((e, i) => e.classList.toggle("on", i === si));
  scaleStage();
  fitMath(); if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitMath); setTimeout(fitMath, 350);
}

/* ------------------------------------------------------------------ 음성 */
const NATURAL = v => /natural|neural|online|google/i.test(v.name);
const voicesReady = () => new Promise(res => { if (!window.speechSynthesis || speechSynthesis.getVoices().length) return res(); const t = setTimeout(res, 1500); speechSynthesis.addEventListener("voiceschanged", () => { clearTimeout(t); res(); }, { once: true }); });
function pickVoice() { const vs = window.speechSynthesis ? speechSynthesis.getVoices() : [], sel = $("l2sVoice") && $("l2sVoice").value; return vs.find(v => v.name === sel) || vs.filter(v => /^ko/i.test(v.lang)).sort((a, b) => NATURAL(b) - NATURAL(a))[0] || null; }
function setState(m) { const e = $("l2sState"); if (e) e.textContent = m; }
function say1(text, voice, rate, pitch) {
  return new Promise(res => {
    const u = new SpeechSynthesisUtterance(text); KEEP.push(u); u.lang = "ko-KR"; if (voice) u.voice = voice; u.rate = rate; u.pitch = pitch;
    let done = false, started = false, tm = 0, ts = 0;
    const fin = ok => { if (done) return; done = true; clearTimeout(tm); clearTimeout(ts); const k = KEEP.indexOf(u); if (k >= 0) KEEP.splice(k, 1); res(ok); };
    u.onstart = () => { started = true; clearTimeout(ts); setState("🔊 읽는 중"); }; u.onend = () => fin(true); u.onerror = () => fin(false);
    tm = setTimeout(() => fin(started), Math.max(7000, text.length * 360));
    ts = setTimeout(() => { if (!started) { try { speechSynthesis.cancel(); } catch (e) { /* 무시 */ } fin(false); } }, 3000);
    try { speechSynthesis.speak(u); } catch (e) { fin(false); }
  });
}
async function speak(text) {
  if (!$("l2sVoiceOn").checked || !window.speechSynthesis || !text) return true;
  await voicesReady();
  try { speechSynthesis.cancel(); speechSynthesis.resume(); } catch (e) { /* 무시 */ }
  await sleep(90);
  const rate = +$("l2sRate").value; let voice = pickVoice(), retried = false;
  const parts = String(text).split(/(?<=[.!?])\s+/).filter(Boolean);
  for (const s of parts) {
    let ok = await say1(s, voice, rate, 1);
    if (!ok && !retried) { retried = true; voice = null; ok = await say1(s, null, 1, 1); }
    if (!ok) { setState("🔇 소리가 시작되지 않았습니다. 볼륨·탭 음소거를 확인하세요."); return false; }
    await sleep(130);
  }
  setState(""); return true;
}

/* ------------------------------------------------------------------ 재생 */
async function playFrom(si, pi) {
  const my = ++runId; playing = true; $("l2sPlay").textContent = "⏸ 일시정지";
  for (let i = si; i < SCENES.length; i++) {
    for (let j = (i === si ? pi : 0); j < SCENES[i].parts.length; j++) {
      if (my !== runId) return;
      render(i, j, true);
      const p = SCENES[i].parts[j], rate = +$("l2sRate").value || 1;
      await Promise.all([sleep(p.ms / rate), speak(p.say)]);
    }
  }
  if (my === runId) { stop(); render(0, 0, false); }
}
function stop() { runId++; playing = false; const b = $("l2sPlay"); if (b) b.textContent = "▶ 재생"; if (window.speechSynthesis) speechSynthesis.cancel(); }
function step(d) {
  const was = playing; stop(); let { s, p } = cur; p += d;
  if (p < 0) { s = Math.max(0, s - 1); p = SCENES[s].parts.length - 1; } else if (p >= SCENES[s].parts.length) { s = Math.min(SCENES.length - 1, s + 1); p = 0; }
  render(s, p, false); if (was) playFrom(s, p);
}

/* ------------------------------------------------------------------ 시작 */
function fillVoices() {
  const sel = $("l2sVoice"); if (!sel || !window.speechSynthesis) return;
  const vs = speechSynthesis.getVoices().filter(v => /^ko/i.test(v.lang)).sort((a, b) => NATURAL(b) - NATURAL(a)), cur0 = sel.value;
  sel.innerHTML = vs.map(v => `<option value="${v.name}">${NATURAL(v) ? "★ " : ""}${v.name}</option>`).join("") || `<option value="">기본 음성</option>`;
  if (cur0) sel.value = cur0;
}
function init() {
  const mount = $("l2ShortsHost"); if (!mount || mount.dataset.ready) return;
  if (!window.katex) { setTimeout(init, 300); return; }
  mount.dataset.ready = "1";
  const st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);
  mount.innerHTML = `<h2 style="font-size:1.25rem;margin-bottom:6px">🎬 숏츠식 판서 미리보기 · 정적분 넓이 만능 공식</h2>
    <p class="l2s-note" style="margin-bottom:14px">식 조각이 연결선을 따라 움직이며 공식 $\\dfrac{m!\\,n!}{(m+n+1)!}$ 이 조립되고, 예제로 확인합니다. 이 장면의 대본과 그림은 직접 만든 것입니다.</p>
    <div class="l2s-wrap"><div class="l2s-frame" id="l2sFrame"><div class="l2s-stage" id="l2sStage"></div></div>
      <div class="l2s-ctl">
        <div class="l2s-row"><button class="l2s-btn" id="l2sPrev" type="button">‹ 이전</button><button class="l2s-btn pri" id="l2sPlay" type="button">▶ 재생</button><button class="l2s-btn" id="l2sNext" type="button">다음 ›</button></div>
        <div class="l2s-opt"><label><input type="checkbox" id="l2sVoiceOn" checked> 음성</label><label>속도 <input type="range" id="l2sRate" min="0.8" max="1.4" step="0.05" value="1" style="width:100px"></label>
          <label>목소리 <select id="l2sVoice"></select></label><button class="l2s-btn" id="l2sTest" type="button" style="padding:4px 10px">음성 시험</button></div>
        <div class="l2s-state" id="l2sState"></div><div class="l2s-note" id="l2sTime"></div>
        <div class="l2s-list" id="l2sList">${SCENES.map((s, i) => `<div class="l2s-sc" data-i="${i}">${i + 1}. ${s.head || s.title}</div>`).join("")}</div>
        <div class="l2s-row" id="l2sLinks"><span class="l2s-note" style="margin:0">이어서 볼 강의</span><button class="l2s-btn" type="button" data-lec="9">제9강 열기</button><button class="l2s-btn" type="button" data-lec="1">제1강 열기</button></div>
        <p class="l2s-note">★ 표시는 더 자연스러운 목소리입니다. Edge 브라우저에서 열면 ‘Natural’ 한국어 목소리가 나오며, 이 목소리는 글이 Microsoft 서버로 전송됩니다.</p>
      </div></div>`;
  try { window.renderMathInElement && renderMathInElement(mount.querySelector(".l2s-note"), { delimiters: [{ left: "$", right: "$", display: false }] }); } catch (e) { /* 무시 */ }
  host = mount; frameEl = $("l2sFrame"); stageEl = $("l2sStage");
  new ResizeObserver(scaleStage).observe(frameEl);
  $("l2sPlay").onclick = () => { if (playing) stop(); else playFrom(cur.s, cur.p); };
  $("l2sLinks").onclick = e => { const b = e.target.closest("[data-lec]"); if (b && typeof window.setLecture === "function") window.setLecture(+b.dataset.lec); };
  $("l2sPrev").onclick = () => step(-1); $("l2sNext").onclick = () => step(1);
  $("l2sList").onclick = e => { const it = e.target.closest("[data-i]"); if (!it) return; const was = playing; stop(); render(+it.dataset.i, 0, false); if (was) playFrom(+it.dataset.i, 0); };
  $("l2sTest").onclick = async () => { stop(); $("l2sVoiceOn").checked = true; setState("🔊 시험 중…"); const ok = await speak("안녕하세요. 정적분 넓이 만능 공식, 같이 볼까요?"); setState(ok ? "✅ 소리가 정상입니다" : "🔇 소리가 시작되지 않았습니다"); };
  if (window.speechSynthesis) { speechSynthesis.onvoiceschanged = fillVoices; setTimeout(fillVoices, 300); }
  render(0, 0, false);
}
window.L2Shorts = { init, render, SCENES };
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
window.addEventListener("load", init);
})();
