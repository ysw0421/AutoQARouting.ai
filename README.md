# Multi-Agent Workflow Optimization System

## 🚀 프로젝트 개요

이 프로젝트는 입력된 Task Description에 따라 최적화된 멀티 에이전트 워크플로우를 자동 생성하고, 에이전트 간의 상호작용 및 역할을 명확히 설계하는 시스템입니다. 기술 문서 처리, 법률 문서 분석, 고객 지원 문서 라우팅 등 다양한 업무 자동화를 지원합니다.

---

## 📌 주요 기능

- 입력된 작업 설명에 따라 멀티 에이전트 워크플로우 자동 설계 및 최적화
- 에이전트별 최적화된 프롬프트 자동 생성
- 에이전트 간 커뮤니케이션 토폴로지 및 워크플로우 시각화
- 자동화된 성능 평가 지표(metrics) 및 테스트 케이스 제공
- FastAPI 기반 API 엔드포인트 제공 (선택 사항)
- 웹 기반 시스템 시각화 데모 (선택 사항)

---

## 📂 저장소 구조

```
.
├── agents/              # 에이전트 구현 코드 및 프롬프트
├── data/                # 평가 데이터셋 및 테스트 케이스
├── eval/                # 성능 평가 및 벤치마크 코드
├── api/                 # FastAPI API 엔드포인트 (선택 사항)
├── frontend/            # 웹 시각화 데모 (선택 사항)
├── docs/                # 기술 문서 및 아키텍처 다이어그램
├── logs/                # 로그 파일
├── scripts/             # 실행 및 환경 설정 스크립트
├── README.md            # 본 문서
└── requirements.txt     # 패키지 의존성 목록
```

---

## ⚙️ 설치 방법

```bash
# 프로젝트 클론
git clone <your-repo-url>
cd <your-repo-name>

# 가상 환경 설정
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

---

## 🚦 사용 방법

### 시스템 실행

```bash
python scripts/run_workflow.py --task "Document QA & Routing" --input "./data/sample.pdf"
```

### (선택 사항) FastAPI 서버 실행

```bash
uvicorn api.main:app --reload
```

### (선택 사항) 웹 애플리케이션 실행

```bash
streamlit run frontend/app.py
```

---

## 🧪 테스트 및 평가

```bash
python eval/run_evaluation.py --scenario "Technical Documentation QA"
```

### 평가 결과 예시

| Test Scenario                      | Accuracy | Avg. Response Time |
| ---------------------------------- | -------- | ------------------ |
| Technical Documentation QA         | 92.5%    | 1.8s               |
| Legal Document Processing          | 90.3%    | 2.1s               |
| Customer Support Document Routing  | 94.7%    | 1.5s               |
| Edge Case: Multi-Language Document | 89.5%    | 2.4s               |

---

## 🎨 데모 및 시각화

웹 기반 데모는 아래 링크에서 확인할 수 있습니다:

```
http://localhost:8501
```

---

## 📚 기술 문서

- [API Documentation](./docs/API.md)
- [시스템 아키텍처](./docs/Architecture.md)
- [에이전트 역할 및 커뮤니케이션 패턴](./docs/Agent_Roles_and_Communication.md)

---

## 🚧 알려진 한계점 및 개선 사항

- 특정 도메인 용어 처리 정확도 개선 필요
- 추가적인 에이전트 유형 도입 및 확장성 향상 필요
- 실시간 응답 속도 최적화 가능

---

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. [LICENSE](./LICENSE) 파일을 참고하세요.