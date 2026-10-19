# [제16강] 단위원(Unit Circle)으로 완벽 정복하는 삼각함수: 정의·대칭성·그래프·부등식

> **강의 출처**: 매스프레소 MathPresso (배상면 선생님 / 철벽수학)  
> **영상 제목**: `[2분] 단위원으로 조지는 삼각함수` (YouTube Shorts 114초)  
> **핵심 키워드**: 단위원(Unit Circle), $\cos\theta$ ($x$좌표), $\sin\theta$ ($y$좌표), $\tan\theta$ (동경의 기울기), 음각 공식 ($-\theta$), 각변환 ($\pi-\theta$), 삼각함수 그래프 추적, 삼각부등식 영역 판정 ($y < x$)

---

## 1. 강의 도입 및 철학: 왜 '단위원'이어야 하는가?

고등학교 수학Ⅰ에서 수많은 학생들이 **삼각함수(Trigonometric Functions)**를 포기하거나 복잡한 공식 암기에 갇히는 가장 큰 원인은 삼각함수를 단순한 "직각삼각형의 변의 비" 또는 "$\sin(\pi-\theta)$ 같은 수십 개의 암기 공식"으로 접근하기 때문입니다.

배상면 선생님은 단 2분 만에 **단위원($x^2 + y^2 = 1$)이라는 단 하나의 기하학적 프레임** 위에:
1. 삼각함수의 정의
2. 피타고라스 기본 항등식
3. 음각 공식 ($-\theta$)
4. 각변환 공식 ($\pi - \theta$)
5. 세 함수($\sin, \cos, \tan$) 그래프의 태동 원리
6. 킬러 삼각부등식의 1초 컷 영역 판정법

을 일관된 원리로 완벽하게 꿰뚫습니다.

---

## 2. 단위원과 삼각함수의 본질적 정의

좌표평면 위에서 원점을 중심으로 하고 반지름의 길이가 $1$인 원을 **단위원(Unit Circle)**이라 하며, 그 방정식은 다음과 같습니다:
$$x^2 + y^2 = 1$$

원점 $O$에서 출발하여 단위원과 만나는 동경 $OP$가 $x$축의 양의 방향과 이루는 각을 $\theta$라 할 때, **점 $P$의 좌표는 삼각함수 그 자체**로 정의됩니다:

$$\bbox[15px,border:2px solid #38bdf8,background-color:#0f172a]{
P(\cos\theta, \sin\theta)
}$$

### 3대 삼각함수의 기하학적 의미
1. **$\cos\theta$ (코사인)**: 점 $P$의 **$x$좌표** (수평 변위)
2. **$\sin\theta$ (사인)**: 점 $P$의 **$y$좌표** (수직 높이)
3. **$\tan\theta$ (탄젠트)**: 동경 $OP$의 **기울기 (Slope)**
   $$\tan\theta = \frac{\Delta y}{\Delta x} = \frac{\sin\theta}{\cos\theta}$$

### 기본 항등식 유도 (피타고라스 정리)
점 $P(\cos\theta, \sin\theta)$는 단위원 $x^2 + y^2 = 1$ 위의 점이므로, 좌표를 그대로 대입하면:
$$(\cos\theta)^2 + (\sin\theta)^2 = 1 \iff \sin^2\theta + \cos^2\theta = 1$$
어떤 복잡한 증명도 필요 없이, 단위원 위의 점이라는 정의 자체에서 즉각 성립합니다.

---

## 3. 대칭성과 음각 공식 ($-\theta$)의 기하학적 유도

각이 음수로 바뀌었을 때($-\theta$) 삼각함수의 부호 변화를 기계적으로 외우지 않고 **$x$축 대칭이동**으로 이해합니다.

1. 동경 $\theta$를 갖는 점 $P(\cos\theta, \sin\theta)$를 **$x$축에 대하여 대칭이동**한 점을 $Q$라 합시다.
2. 점 $Q$가 이루는 동경은 아래쪽으로 회전하므로 **$-\theta$**가 되며, 좌표는:
   $$Q(\cos(-\theta), \sin(-\theta))$$
3. 그런데 $x$축 대칭이므로 $x$좌표는 그대로 유지되고, $y$좌표는 부호만 반대가 됩니다:
   $$Q(\cos\theta, -\sin\theta)$$
4. 두 좌표를 성분별로 비교하면:
   $$\begin{aligned}
   \cos(-\theta) &= \cos\theta \quad (\text{우함수, } x\text{좌표 불변}) \\
   \sin(-\theta) &= -\sin\theta \quad (\text{기함수, } y\text{좌표 반전}) \\
   \tan(-\theta) &= \frac{\sin(-\theta)}{\cos(-\theta)} = \frac{-\sin\theta}{\cos\theta} = -\tan\theta \quad (\text{기울기 반전})
   \end{aligned}$$

> **결론**: 코사인은 $x$좌표이므로 $x$축 대칭에 영향을 받지 않고 그대로 $\cos\theta$가 되며, 사인과 탄젠트는 부호가 뒤집힙니다!

---

## 4. 각변환 공식의 본질: $\pi - \theta$와 $y$축 대칭

$\sin(\pi-\theta), \cos(\pi-\theta), \tan(\pi-\theta)$ 역시 단위원에서의 **$y$축 대칭이동** 하나로 완벽히 정리됩니다.

1. 각 $\pi$($180^\circ$)는 음의 $x$축 방향입니다. 여기서 $\theta$만큼 되돌아간 동경 $\pi - \theta$는 동경 $\theta$와 **$y$축에 대하여 완벽한 대칭**을 이룹니다.
2. $y$축 대칭이므로:
   - **$y$좌표(높이)**는 그대로 동일 $\implies \sin(\pi - \theta) = \sin\theta$
   - **$x$좌표(가로 위치)**는 부호 반대 $\implies \cos(\pi - \theta) = -\cos\theta$
   - **기울기(Slope)**는 부호 반대 $\implies \tan(\pi - \theta) = -\tan\theta$

어떤 사분면 공식을 따로 외울 필요 없이, $y$축 대칭 선 하나로 세 함수의 부호와 값이 1초 만에 판정됩니다.

---

## 5. 삼각함수 그래프의 태동 원리

삼각함수 곡선($y=\sin x, y=\cos x, y=\tan x$)은 단위원 위를 회전하는 점 $P$의 궤적을 시간(각도 $\theta$) 축으로 펼친 것입니다.

1. **$y = \sin\theta$ 그래프**:
   - 점 $P$가 단위원 둘레를 반시계 방향으로 돌 때, **$y$좌표(높이)**를 오른쪽으로 $\frac{\pi}{2}$ 간격으로 펼쳐서 점을 찍어나감.
   - $0 \to 1 \to 0 \to -1 \to 0$ 주기로 파동을 형성.
2. **$y = \cos\theta$ 그래프**:
   - 점 $P$의 **$x$좌표(가로 위치)**를 읽어 오른쪽 높이로 사영하여 찍어나감.
   - $1 \to 0 \to -1 \to 0 \to 1$ 주기로 파동 형성.
3. **$y = \tan\theta$ 그래프**:
   - 동경 $OP$의 **기울기**를 찍어나감.
   - $\theta = \frac{\pi}{2}, \frac{3\pi}{2}$에서는 동경이 $y$축과 일치하여 수직선이 되므로 **기울기가 정의되지 않음(무한대)** $\implies$ **점근선 $x = \frac{\pi}{2} + n\pi$ 발생!**

---

## 6. 삼각부등식의 초고속 영역 판정법 (킬러 스킬)

수능과 내신에서 가장 많은 오답이 나오는 형태인 **두 삼각함수의 대소 비교 부등식**:
$$\sin\theta < \cos\theta \quad (0 \le \theta < 2\pi)$$

### 전통적 풀이 (그래프 2개 겹쳐 그리기)
- $y = \sin\theta$ 곡선과 $y = \cos\theta$ 곡선을 겹쳐 그리고,
- 교점 $\theta = \frac{\pi}{4}, \frac{5\pi}{4}$를 찾은 뒤,
- 사인의 곡선이 코사인의 곡선보다 아래에 있는 구간을 일일이 분할하여 확인. (작도 시간이 오래 걸리고 교점 실수 빈발)

### 배상면 선생님의 단위원 치환 풀이 (1초 컷)
1. **정의 대입**: $\sin\theta = y, \;\; \cos\theta = x$
2. 부등식 변환:
   $$\sin\theta < \cos\theta \iff y < x$$
3. **기하학적 해석**:
   "단위원 $x^2 + y^2 = 1$ 둘레 중에서 **직선 $y = x$의 아래쪽 영역($y < x$)**에 위치한 호(Arc)를 찾아라!"
4. **즉석 시각화**:
   - 직선 $y = x$는 단위원과 제1사분면($\theta = 45^\circ = \frac{\pi}{4}$)과 제3사분면($\theta = 225^\circ = \frac{5\pi}{4}$)에서 만남.
   - 직선 $y = x$의 아래쪽 영역에 해당하는 단위원의 각도 범위:
     $$0 \le \theta < \frac{\pi}{4} \quad \text{또는} \quad \frac{5\pi}{4} < \theta < 2\pi$$
     (도 단위: $0^\circ \le \theta < 45^\circ \;\cup\; 225^\circ < \theta < 360^\circ$)
5. **평가**: 단위원 하나에 $45^\circ$ 선 하나 긋는 순간 정답이 바로 눈에 보입니다!

---

## 7. 타임라인 및 영상 캡처 10단계 상세 분석

| 순번 | 파일명 | 타임코드 | 배상면 선생님 판서 및 핵심 강의 내용 |
| :---: | :--- | :---: | :--- |
| **01** | `01_unit_circle_p_definition.jpg` | 00:09 | **단위원 정의**: $x^2+y^2=1$ 위의 점 $P(\cos\theta, \sin\theta)$, $x$좌표는 $\cos$, $y$좌표는 $\sin$ |
| **02** | `02_sin_square_plus_cos_square_one.jpg` | 00:20 | **피타고라스 항등식**: 단위원 식에 대입하여 $\sin^2\theta + \cos^2\theta = 1$ 유도 |
| **03** | `03_x_axis_symmetry_negative_theta.jpg` | 00:32 | **$x$축 대칭**: 점 $P$를 $x$축 대칭이동한 점 $Q$, 동경은 $-\theta$ |
| **04** | `04_negative_angle_formulas_derived.jpg` | 00:44 | **음각 공식 완성**: $Q(\cos(-\theta), \sin(-\theta)) = (\cos\theta, -\sin\theta)$ 비교 |
| **05** | `05_pi_minus_theta_y_axis_symmetry.jpg` | 01:00 | **각변환 $\pi-\theta$**: $\pi-\theta$의 동경은 $\theta$와 $y$축 대칭 $\implies \sin$ 유지, $\cos,\tan$ 부호 반전 |
| **06** | `06_sin_curve_unfolding_y_coord.jpg` | 01:14 | **$\sin$ 그래프 생성**: 점 $P$의 $y$좌표(높이)를 $\frac{\pi}{2}$ 간격으로 펼쳐서 파동 작도 |
| **07** | `07_cos_and_tan_curve_generation.jpg` | 01:25 | **$\cos, \tan$ 그래프**: $x$좌표는 $\cos$, 동경의 기울기는 $\tan$ 곡선 생성 |
| **08** | `08_tan_asymptote_vertical_slope.jpg` | 01:32 | **$\tan$ 점근선**: $\theta = \frac{\pi}{2} + n\pi$에서 수직선 $\implies$ 기울기 없음 $\implies$ 점근선 |
| **09** | `09_trig_inequality_sin_less_cos.jpg` | 01:41 | **삼각부등식**: $\sin\theta < \cos\theta \implies y < x$, 직선 $y=x$의 아래쪽 영역 판정 |
| **10** | `10_trig_inequality_final_solution_range.jpg` | 01:48 | **최종 해**: $0 \le \theta < \frac{\pi}{4} \cup \frac{5\pi}{4} < \theta < 2\pi$ ($0^\circ \sim 45^\circ, 225^\circ \sim 360^\circ$) |
