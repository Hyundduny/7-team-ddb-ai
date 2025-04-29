def run_inference(prompt: str) -> str:
    return f"모델 응답: {prompt[::-1]}"

# 키워드 추출 함수 (실제 LLM 연동 필요)
def extract_keywords(text: str) -> list[str]:
    # 실제로는 로컬 LLM을 사용해야 함 (여기선 예시로 단어 분리)
    return text.replace("추천해줘", "").replace("추천", "").split()

# 임베딩 생성 함수 (실제 임베딩 모델 연동 필요)
def get_embedding(keywords: list[str]) -> list[float]:
    # 실제로는 임베딩 모델을 사용해야 함 (여기선 예시로 길이 기반 임베딩)
    return [float(len(k)) for k in keywords]
