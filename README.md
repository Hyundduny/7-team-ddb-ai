# Dolpin AI - 장소 추천 시스템

## 프로젝트 개요
Dolpin AI는 사용자의 자연어 입력을 기반으로 장소를 추천하는 AI 시스템입니다. LLM을 활용하여 키워드를 추출하고, 벡터 데이터베이스를 통해 유사한 장소를 찾아 추천합니다.

## 주요 기능
- 자연어 기반 장소 추천
- LLM을 활용한 키워드 추출
- 벡터 데이터베이스 기반 유사도 검색
- 실시간 추천 처리

## 기술 스택
- FastAPI: 백엔드 프레임워크
- LangChain: LLM 통합
- FAISS/Chroma: 벡터 데이터베이스
- Celery: 비동기 작업 처리
- Redis: 캐싱
- Docker: 컨테이너화
- Prometheus/Grafana: 모니터링

## 프로젝트 구조
```
dolpin_ai/
├── app/
│   ├── main.py                      # FastAPI 진입점
│   ├── api/                         # 엔드포인트 정의
│   │   ├── deps.py                  # Depends 의존성
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   └── recommend.py     # 추천 요청 엔드포인트
│   │       └── router.py            # v1 router 통합
│   ├── services/                    # 서비스 로직
│   │   ├── recommender.py           # 추천 알고리즘
│   │   ├── rag_engine.py            # RAG 체인
│   │   ├── prompt_manager.py        # 프롬프트 관리
│   │   └── vector_store.py          # 벡터DB 연동
│   ├── ml/                          # 모델 로딩 및 추론
│   │   ├── model_loader.py          # 모델 로딩
│   │   └── inference.py             # 추론 엔진
│   ├── schemas/                     # Pydantic 모델
│   │   └── recommend_schema.py      # 입력/출력 스키마
│   ├── core/                        # 설정, 보안, CORS 등
│   │   ├── config.py                # 기본 설정
│   │   └── init_app.py              # 앱 부트스트랩
│   │
│   ├── 🔵 models/                   # [NEW] DB 모델 정의
│   │   ├── base.py                  # 기본 모델
│   │   └── place.py                 # 장소 모델
│   │
│   ├── 🔵 database/                 # [NEW] DB 설정
│   │   ├── session.py               # DB 세션 관리
│   │   └── migrations/              # Alembic 마이그레이션
│   │
│   ├── 🔵 security/                 # [NEW] 보안 관련
│   │   ├── auth.py                  # 인증 로직
│   │   └── oauth.py                 # OAuth 설정
│   │
│   ├── 🔵 cache/                    # [NEW] 캐싱
│   │   ├── redis.py                 # Redis 설정
│   │   └── decorators.py            # 캐시 데코레이터
│   │
│   ├── 🔵 tasks/                    # [NEW] 비동기 작업
│   │   ├── celery.py                # Celery 설정
│   │   └── workers/                 # 워커 정의
│   │
│   ├── 🔵 exceptions/               # [NEW] 예외 처리
│   │   ├── handlers.py              # 예외 핸들러
│   │   └── custom.py                # 커스텀 예외
│   │
│   ├── 🔵 logging/                  # [NEW] 로깅
│   │   ├── config.py                # 로깅 설정
│   │   └── middleware.py            # 로깅 미들웨어
│   │
│   └── 🔵 utils/                    # [NEW] 보조 유틸 함수
│       ├── logger.py                # loguru/structlog 기반 로거
│       ├── text_cleaner.py          # 텍스트 전처리 유틸
│       └── timer.py                 # 성능 측정 데코레이터
│
├── 🔵 tests/                        # [NEW] 테스트
│   ├── unit/                        # 단위 테스트
│   ├── integration/                 # 통합 테스트
│   └── e2e/                         # E2E 테스트
│
├── 🔵 docs/                         # [NEW] 문서화
│   ├── api/                         # API 문서
│   └── architecture/                # 아키텍처 문서
│
├── 🔵 scripts/                      # [NEW] 유틸리티
│   ├── setup.sh                     # 환경 설정
│   └── deploy.sh                    # 배포 스크립트
│
├── 🔵 monitoring/                   # [NEW] 모니터링
│   ├── prometheus/                  # Prometheus 설정
│   └── grafana/                     # Grafana 대시보드
│
├── 🔵 config/                       # [NEW] 환경 설정
│   ├── development.py               # 개발 환경
│   ├── testing.py                   # 테스트 환경
│   └── production.py                # 운영 환경
│
├── 🔵 Dockerfile                    # [NEW] 컨테이너 설정
├── 🔵 docker-compose.yml           # [NEW] 컨테이너 구성
├── 🔵 requirements.txt             # [NEW] 의존성
└── 🔵 README.md                    # [NEW] 프로젝트 문서
```

1. **데이터베이스 관리**
    - `models/`: SQLAlchemy 기반 DB 모델 정의
    - `database/`: DB 세션 관리 및 마이그레이션
    - `vector_store.py`: FAISS/Chroma 벡터 DB 연동

2. **보안 (security/)**
    - `auth.py`: JWT/OAuth 기반 인증 로직
    - `oauth.py`: OAuth2.0 설정 및 구현
    - `core/config.py`: 보안 관련 설정

3. **캐싱 (cache/)**
    - `redis.py`: Redis 연결 및 설정
    - `decorators.py`: 캐시 데코레이터 구현
    - 성능 최적화를 위한 캐싱 전략

4. **비동기 작업**
    - `tasks/`: Celery 기반 비동기 작업 관리
    - `workers/`: 임베딩 생성 등 백그라운드 작업
    - `celery_app.py`: Celery 설정 및 워커 정의

5. **예외 처리 (exceptions/)**
    - `handlers.py`: 전역 예외 핸들러
    - `custom.py`: 커스텀 예외 클래스
    - 에러 응답 표준화

6. **로깅 (logging/)**
    - `config.py`: 로깅 설정
    - `middleware.py`: 요청/응답 로깅
    - `utils/logger.py`: 구조화된 로깅

7. **유틸리티 (utils/)**
    - `text_cleaner.py`: 텍스트 전처리
    - `timer.py`: 성능 측정
    - `logger.py`: 로깅 유틸리티

8. **테스트 (tests/)**
    - `unit/`: 단위 테스트
    - `integration/`: 통합 테스트
    - `e2e/`: End-to-End 테스트

9. **문서화 (docs/)**
    - `api/`: API 문서
    - `architecture/`: 시스템 아키텍처 문서
    - `README.md`: 프로젝트 개요

10. **모니터링 (monitoring/)**
    - `prometheus/`: 메트릭 수집
    - `grafana/`: 대시보드 및 시각화
    - 성능 모니터링

11. **환경 설정 (config/)**
    - `development.py`: 개발 환경
    - `testing.py`: 테스트 환경
    - `production.py`: 운영 환경

12. **배포 관련**
    - `Dockerfile`: 컨테이너 이미지 정의
    - `docker-compose.yml`: 서비스 구성
    - `requirements.txt`: 의존성 관리

13. **API 엔드포인트 (api/)**
    - `v1/endpoints/`: API 버전 1 엔드포인트
    - `deps.py`: 의존성 주입
    - `router.py`: 라우터 통합

14. **서비스 로직 (services/)**
    - `recommender.py`: 추천 알고리즘
    - `rag_engine.py`: RAG 체인
    - `prompt_manager.py`: 프롬프트 관리

15. **ML 모델 (ml/)**
    - `model_loader.py`: 모델 로딩
    - `inference.py`: 추론 엔진
    - LLM 및 임베딩 모델 관리

16. **데이터 스키마 (schemas/)**
    - `recommend_schema.py`: 추천 관련 스키마
    - Pydantic 기반 데이터 검증

17. **핵심 설정 (core/)**
    - `config.py`: 기본 설정
    - `init_app.py`: 앱 초기화
    - CORS, 미들웨어 등 설정

이 구조는:
- 모듈화된 설계
- 확장 가능한 아키텍처
- 유지보수 용이성
- 테스트 용이성
- 배포 자동화
- 모니터링 용이성

을 제공합니다.

## 설치 및 실행

### 요구사항
- Python 3.8+
- Docker
- Redis
- FAISS/Chroma

### 설치
```bash
# 1. 저장소 클론
git clone [repository-url]

# 2. 의존성 설치
pip install -r requirements.txt

# 3. 환경 설정
cp config/development.py config/local.py
# config/local.py 수정

# 4. 데이터베이스 마이그레이션
alembic upgrade head
```

### 실행
```bash
# 개발 환경
uvicorn app.main:app --reload

# Docker 환경
docker-compose up -d
```

## API 사용법

### 추천 API
```http
POST /api/v1/recommend
Content-Type: application/json

{
    "text": "맛있는 한식집 추천해줘"
}
```

응답:
```json
{
    "recommendations": [
        {
            "id": 1,
            "similarity_score": 0.95
        }
    ]
}
```

## 모니터링
- Prometheus: 메트릭 수집
- Grafana: 대시보드 및 시각화
- 로깅: 구조화된 로그 수집

## 테스트
```bash
# 단위 테스트
pytest tests/unit

# 통합 테스트
pytest tests/integration

# E2E 테스트
pytest tests/e2e
```

## contribution
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 라이선스
MIT License