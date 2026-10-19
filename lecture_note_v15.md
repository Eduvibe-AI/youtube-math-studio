# [제15강] 자연수 $N$의 모든 약수의 총곱(Product of Divisors)과 기하평균의 원리

> **강의 출처**: 매스프레소 MathPresso (배상면 선생님 / 철벽수학)  
> **영상 제목**: `[기하평균] 약수의 총 곱!` (YouTube Shorts 33초)  
> **핵심 키워드**: 약수의 총곱, 기하평균(Geometric Mean), 약수의 대칭 쌍(Pairing Principle), 가우스 곱셈 대칭성, 완전제곱수

---

## 1. 강의 도입 및 문제 제기

중·고등학교 수학(수학(상), 확률과 통계, 정수론)에서 자연수 $N$이 소인수분해 $N = p_1^{a_1} p_2^{a_2} \cdots p_r^{a_r}$로 주어졌을 때:
1. **약수의 개수**: $d(N) = (a_1 + 1)(a_2 + 1)\cdots(a_r + 1)$
2. **약수의 총합**: $\sigma(N) = \left(\frac{p_1^{a_1+1}-1}{p_1-1}\right) \cdots \left(\frac{p_r^{a_r+1}-1}{p_r-1}\right)$

은 교과서와 문제집에서 매우 익숙하게 다루어집니다.  
그러나 **"약수의 총곱(Product of all positive divisors)"** 은 공식 교과서에 명시적인 공식이 실려 있지 않아 많은 학생들이 생소하게 느끼거나, 일일이 약수를 나열해 곱하다가 계산 실수에 빠지기 쉽습니다.

배상면 선생님은 이 질문에 대해 단 33초 만에 **기하평균(Geometric Mean)** 과 **대칭 쌍(Pairing)** 이라는 본질적 시각을 통해 어떤 자연수에도 즉시 적용되는 가장 우아한 공식을 증명합니다.

---

## 2. 약수의 총곱 핵심 공식

자연수 $N$의 모든 양의 약수의 개수를 $k = d(N)$이라 할 때, $N$의 모든 양의 약수의 총곱 $P(N)$은 다음과 같습니다.

$$\bbox[15px,border:2px solid #eab308,background-color:#1e1e2e]{
P(N) = \prod_{d \mid N} d = \left(\sqrt{N}\right)^{d(N)} = N^{\frac{d(N)}{2}}
}$$

> **"자연수 $N$의 모든 약수의 곱은 $\sqrt{N}$의 '약수의 개수' 제곱이다!"**

---

## 3. 엄밀한 수학적 증명 2가지

### 증명 1: 약수의 대칭 쌍(Pairing)과 가우스 곱셈법

가우스가 $1$부터 $100$까지의 합을 구할 때 $1+100 = 2+99 = \cdots = 101$로 대칭 쌍을 묶어 덧셈을 곱셈으로 바꾼 것처럼, **약수의 곱은 곱셈 세계에서의 대칭 쌍**을 이룹니다.

$N$의 임의의 양의 약수를 $d$라 하면, $N$을 $d$로 나눈 몫 $\frac{N}{d}$ 역시 반드시 $N$의 약수가 됩니다.  
이 두 약수를 곱하면 항상 본래의 수 $N$이 됩니다:
$$d \times \frac{N}{d} = N$$

이제 $N$의 모든 양의 약수를 작은 것부터 순서대로 나열한 집합을 $\{d_1, d_2, \dots, d_k\}$라 합시다.
약수의 총곱 $P(N)$을 정방향과 역방향으로 두 번 적어 곱합니다:

$$\begin{aligned}
P(N) &= d_1 \times d_2 \times \cdots \times d_k \\
P(N) &= \frac{N}{d_1} \times \frac{N}{d_2} \times \cdots \times \frac{N}{d_k}
\end{aligned}$$

변끼리 곱하면:
$$\begin{aligned}
P(N)^2 &= \left(d_1 \times \frac{N}{d_1}\right) \times \left(d_2 \times \frac{N}{d_2}\right) \times \cdots \times \left(d_k \times \frac{N}{d_k}\right) \\
&= \underbrace{N \times N \times \cdots \times N}_{k\text{개}} = N^k
\end{aligned}$$

양변에 제곱근을 취하면 (모든 약수는 양수이므로):
$$P(N) = \sqrt{N^k} = \left(\sqrt{N}\right)^k = N^{\frac{k}{2}}$$
$\blacksquare$

---

### 증명 2: 기하평균(Geometric Mean)과 곱셈 기대치 (배상면 선생님의 직관)

배상면 선생님의 설명은 통계학과 해석학의 **기하평균(Geometric Mean)** 개념을 접목하여 곱셈의 본질을 꿰뚫습니다.

1. **곱셈의 기대치(기하평균)**:
   - 두 수 $A, B$의 덧셈 세계에서의 평균은 산술평균 $\frac{A+B}{2}$ (더할 때의 회당 기대치).
   - 곱셈 세계에서의 1회당 평균적인 크기(기대치)는 **기하평균 $\sqrt{A \times B}$** 입니다.

2. **약수 한 쌍의 기하평균**:
   - 약수 $d$와 짝꿍 $\frac{N}{d}$을 곱하면 $N$이므로:
     $$d \times \frac{N}{d} = N = (\sqrt{N})^2$$
   - 따라서 두 약수 $d, \frac{N}{d}$의 기하평균은:
     $$\text{G.M.} = \sqrt{d \times \frac{N}{d}} = \sqrt{N}$$
   - 즉, **"모든 약수 1개가 가지는 곱셈적 대표값(기하평균)은 정확히 $\sqrt{N}$이다!"**

3. **약수의 총곱 도출**:
   - $k$개의 약수가 존재할 때, 약수 1개당 평균 크기가 $\sqrt{N}$이므로,
   - $k$개의 약수를 모두 곱한 총곱은 대표값 $\sqrt{N}$을 $k$번 거듭제곱한 것과 완벽히 같습니다:
     $$P(N) = \underbrace{\sqrt{N} \times \sqrt{N} \times \cdots \times \sqrt{N}}_{k\text{개}} = (\sqrt{N})^k$$
$\blacksquare$

---

## 4. 완전제곱수(Square Number)에서도 공식이 성립하는가?

학생들이 가장 많이 의문을 품는 지점은 **"약수의 개수가 홀수인 완전제곱수($N=m^2$)"** 입니다.

### 구체적 반례 검증: $N = 36$
$36$의 모든 양의 약수는 $\{1, 2, 3, 4, 6, 9, 12, 18, 36\}$으로 총 $k = 9$개(홀수 개)입니다.
- 양끝 대칭 쌍:
  - $1 \times 36 = 36$
  - $2 \times 18 = 36$
  - $3 \times 12 = 36$
  - $4 \times 9 = 36$
- 가운데 홀로 남은 약수: $6$ (왜냐하면 $6 = \sqrt{36}$)

직접 계산한 총곱:
$$P(36) = (1 \times 36) \times (2 \times 18) \times (3 \times 12) \times (4 \times 9) \times 6 = 36^4 \times 6 = (6^2)^4 \times 6 = 6^8 \times 6^1 = 6^9$$

공식 적용:
$$P(36) = (\sqrt{36})^{d(36)} = 6^9 = 10,077,696$$

두 결과가 **완벽하게 일치**합니다!  
홀로 남은 가운데 약수 $6$은 자기 자신과의 기하평균이 $\sqrt{6 \times 6} = 6 = \sqrt{36}$이므로, 기하평균 관점에서는 홀수 개이든 짝수 개이든 아무런 예외 없이 공식이 항상 정확하게 성립합니다.

---

## 5. 소인수분해를 이용한 대수적 증명

자연수 $N$의 소인수분해가 다음과 같다고 합시다:
$$N = p_1^{a_1} p_2^{a_2} \cdots p_r^{a_r}$$
약수의 개수는 $k = (a_1+1)(a_2+1)\cdots(a_r+1)$입니다.

임의의 약수 $d$는 다음과 같이 표현됩니다:
$$d = p_1^{x_1} p_2^{x_2} \cdots p_r^{x_r} \quad (0 \le x_i \le a_i)$$

모든 약수를 다 곱했을 때, 소인수 $p_1$의 총 지수 $S_1$을 구해봅시다.  
$x_1$이 $0, 1, 2, \dots, a_1$의 각 값을 취할 때, 나머지 지수 $(x_2, \dots, x_r)$를 선택하는 경우의 수는 $\frac{k}{a_1+1}$가지입니다.
따라서 $x_1$의 총합은:
$$S_1 = \left(\sum_{x_1=0}^{a_1} x_1\right) \times \frac{k}{a_1+1} = \frac{a_1(a_1+1)}{2} \times \frac{k}{a_1+1} = a_1 \times \frac{k}{2}$$

마찬가지로 모든 소인수 $p_i$에 대해 총 지수는 $a_i \times \frac{k}{2}$가 됩니다.  
따라서 모든 약수의 총곱 $P(N)$은:
$$P(N) = p_1^{S_1} p_2^{S_2} \cdots p_r^{S_r} = p_1^{a_1 \frac{k}{2}} p_2^{a_2 \frac{k}{2}} \cdots p_r^{a_r \frac{k}{2}} = \left(p_1^{a_1} p_2^{a_2} \cdots p_r^{a_r}\right)^{\frac{k}{2}} = N^{\frac{k}{2}} = (\sqrt{N})^k$$
소인수분해 지수 합 계산으로도 완벽하게 동일한 결과가 도출됩니다!

---

## 6. 실전 대표 예제 3선

### 예제 1: 12의 모든 약수의 곱
- $N = 12 = 2^2 \times 3^1$
- 약수의 개수 $k = (2+1)(1+1) = 6$개 ($\{1, 2, 3, 4, 6, 12\}$)
- 공식 적용:
  $$P(12) = (\sqrt{12})^6 = (12^{1/2})^6 = 12^3 = 1,728$$
- 직접 확인: $1 \times 2 \times 3 \times 4 \times 6 \times 12 = (1 \times 12) \times (2 \times 6) \times (3 \times 4) = 12^3 = 1,728$ (일치!)

### 예제 2: 100의 모든 약수의 곱
- $N = 100 = 10^2 = 2^2 \times 5^2$
- 약수의 개수 $k = (2+1)(2+1) = 9$개
- 공식 적용:
  $$P(100) = (\sqrt{100})^9 = 10^9 = 1,000,000,000$$

### 예제 3: 72의 모든 약수의 곱을 $2^a \cdot 3^b$ 꼴로 나타내기
- $N = 72 = 2^3 \times 3^2$
- 약수의 개수 $k = (3+1)(2+1) = 12$개
- 공식 적용:
  $$P(72) = 72^{\frac{12}{2}} = 72^6 = (2^3 \times 3^2)^6 = 2^{18} \times 3^{12}$$

---

## 7. 영상 타임라인 및 화면 캡처 분석

| 번호 | 파일명 | 타임코드 | 배상면 선생님 판서 및 강의 내용 |
| :---: | :--- | :---: | :--- |
| **01** | `01_intro_question_product_of_divisors.jpg` | 00:02 | **도입**: 약수의 개수, 약수의 총합은 익숙하지만 약수의 곱은 생소하다 |
| **02** | `02_formula_root_n_power_k.jpg` | 00:06 | **공식 선언**: 자연수 $N$의 모든 (양의) 약수의 곱 = $\sqrt{N}^{\text{약수의 개수}}$ |
| **03** | `03_question_why_proof_starts.jpg` | 00:08 | **Why?**: 공식이 왜 성립하는지 원리 탐구 시작 |
| **04** | `04_divisors_appear_in_pairs.jpg` | 00:10 | **핵심 원리 1**: 약수는 항상 짝(Pair)으로 나타난다 |
| **05** | `05_example_12_divisors_pairing.jpg` | 00:13 | **예시 12**: $3 \times 4 = 12$, 3과 4가 짝을 이루어 12의 약수가 됨 |
| **06** | `06_general_pairing_d_and_n_over_d.jpg` | 00:16 | **일반화**: $N$의 임의의 약수를 $d$라 하면 $d$와 $\frac{N}{d}$이 짝 |
| **07** | `07_product_of_pair_equals_n.jpg` | 00:20 | **한 쌍의 곱**: $d \times \frac{N}{d} = N = (\sqrt{N})^2$ |
| **08** | `08_geometric_mean_is_root_n.jpg` | 00:23 | **기하평균**: 약수 하나의 기하평균 [곱셈의 회당 기대치] = $\sqrt{N}$ |
| **09** | `09_total_product_root_n_times_k.jpg` | 00:27 | **총곱 유도**: 약수의 총곱은 기하평균 $\sqrt{N}$을 약수의 개수만큼 곱하는 것 |
| **10** | `10_final_conclusion_formula_box.jpg` | 00:30 | **최종 정리**: 약수의 총 곱 = $\sqrt{N}^{\text{약수의 개수}}$ 완벽 결론 |
