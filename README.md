# 📐 수학 세미나 & 인터랙티브 에듀 스튜디오 6종 통합 허브

이 워크스페이스는 깃허브(`jungyeonsu0330`)에 등록된 6개 수학 프로젝트를 모두 로컬(`d:\수학세미나-v3`)에 구축하고 실시간 로컬 서버로 가동 중인 통합 환경입니다.

---

## 🌐 6대 서비스 로컬 접속 주소 (전체 정상 가동 중: HTTP 200 OK)

| # | 프로젝트명 | 성격 및 설명 | 로컬 접속 URL | 포트 | 구동 스크립트 |
| :-: | :--- | :--- | :--- | :-: | :--- |
| **1** | **youtube-math-studio** | 수능 수학 킬러 공식 마스터 포털 (1~39강 시뮬레이션, Manim 애니메이션) | **[http://localhost:8081](http://localhost:8081)** | `8081` | `python serve.py` |
| **2** | **math-interactive-workbook** | 중·고등 대표 교재(개념원리 RPM, 고쟁이 12권 9,785문항) 인터랙티브 문제집 포털 | **[http://localhost:8082](http://localhost:8082)** | `8082` | `python math-interactive-workbook/serve_workbook.py` |
| **3** | **math-calc-lab** | 미적분Ⅰ 110~133쪽, 극한·연속 6~35쪽, 평행사변형 229~252, 전체 내레이션 대본 | **[http://localhost:8083](http://localhost:8083)** | `8083` | `python math-calc-lab/serve_calc_lab.py` |
| **4** | **claude-math-v2** | 클로드 수학 v2 (모의고사 시험 랩, 기하/미적분 랩, 쪽별 인터랙티브 학습기) | **[http://localhost:8084](http://localhost:8084)** | `8084` | `python claude-math-v2/serve_v2.py` |
| **5** | **claude-math-lab** | 클로드 수학 실험실 (고쟁이 심화, 피타고라스 랩, 함수 인터랙티브 랩) | **[http://localhost:8085](http://localhost:8085)** | `8085` | `python claude-math-lab/serve_lab.py` |
| **6** | **509-401-math--helper** | 509동 401호 수학세미나 로컬 웹 서버 (선생님/학생 쌍방향 화면 공유 & 문제 풀이) | **[http://localhost:8900](http://localhost:8900)** | `8900` | `python 509-401-math--helper/server.py` |

> 💡 **509동 401호 수학세미나 도우미 안내**:
> - **선생님 화면**: [http://localhost:8900](http://localhost:8900)
> - **학생 화면**: [http://localhost:8900/student](http://localhost:8900/student) (같은 Wi-Fi 내 다른 기기에서도 접속 가능)

---

## 📂 로컬 디렉터리 구조 (`d:\수학세미나-v3`)

- **`d:\수학세미나-v3`** (메인 루트)
  - `index.html` : 킬러 공식 마스터 메인 포털
  - `serve.py` : 포트 8081 데몬
- **`d:\수학세미나-v3\math-interactive-workbook`**
  - `index.html` : 12권 9,785문항 인터랙티브 교재 포털
  - `serve_workbook.py` : 포트 8082 데몬
- **`d:\수학세미나-v3\math-calc-lab`**
  - `index.html`, `lab.html`, `calc110.html`, `calc_lim.html`
  - `serve_calc_lab.py` : 포트 8083 데몬
- **`d:\수학세미나-v3\claude-math-v2`**
  - `index.html`, `mock_exam_lab.html`, `func_lab.html`
  - `serve_v2.py` : 포트 8084 데몬
- **`d:\수학세미나-v3\claude-math-lab`**
  - `index.html`, `lab.html`, `pyth_lab.html`
  - `serve_lab.py` : 포트 8085 데몬
- **`d:\수학세미나-v3\509-401-math--helper`**
  - `server.py` : 포트 8900 양방향 수업 서버
  - `public/` : 교재 및 문제 데이터
