"""
추천 서비스 모듈

이 모듈은 LangChain과 Gemini를 사용하여 사용자 입력에서 키워드를 추출하고,
추출된 키워드를 기반으로 장소 추천을 생성하는 서비스를 제공합니다.

주요 구성요소:
    - RecommenderService: 추천 서비스의 핵심 클래스
    - get_recommendation: 키워드 추출 및 추천 생성 메서드

사용 예시:
    ```python
    service = RecommenderService()
    recommendations = await service.get_recommendation("맛있는 한식집 추천해줘")
    ```
"""

import os
from typing import List, Dict
from langchain.llms import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

class RecommenderService:
    """
    추천 서비스 클래스
    
    이 클래스는 LangChain과 Gemini를 사용하여 사용자 입력에서 키워드를 추출하고,
    추출된 키워드를 기반으로 장소 추천을 생성합니다.
    
    Attributes:
        llm (GoogleGenerativeAI): Gemini 언어 모델 인스턴스
        prompt_template (PromptTemplate): 키워드 추출을 위한 프롬프트 템플릿
        chain (LLMChain): LangChain 체인 인스턴스
    """
    
    def __init__(self):
        """
        RecommenderService 인스턴스를 초기화합니다.
        
        Raises:
            ValueError: GOOGLE_API_KEY가 환경 변수에 설정되지 않은 경우
        """
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY가 설정되지 않았습니다.")
        
        # LangChain을 사용한 Gemini 모델 초기화
        self.llm = GoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=api_key,
            temperature=0.7
        )
        
        # 프롬프트 템플릿 설정
        self.prompt_template = PromptTemplate(
            input_variables=["user_input"],
            template="""
            사용자 입력: {user_input}
            
            위 사용자 입력에서 장소 추천을 위한 핵심 키워드를 추출해주세요.
            키워드는 쉼표로 구분된 형태로 반환해주세요.
            예시: 맛집, 한식, 분위기 좋은
            
            키워드만 반환해주세요. 다른 설명은 필요하지 않습니다.
            """
        )
        
        # LangChain 체인 설정
        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt_template
        )
    
    async def get_recommendation(self, user_input: str) -> List[Dict]:
        """
        사용자 입력에서 키워드를 추출하고 추천 결과를 생성합니다.
        
        이 메서드는 다음 단계로 동작합니다:
        1. LangChain을 사용하여 사용자 입력에서 키워드 추출
        2. 추출된 키워드를 사용하여 벡터 유사도 검색 수행 (TODO)
        3. 검색 결과를 기반으로 추천 목록 생성
        
        Args:
            user_input (str): 사용자의 입력 텍스트
            
        Returns:
            List[Dict]: 추천 결과 목록. 각 항목은 id와 similarity_score를 포함
            
        Raises:
            Exception: 추천 생성 과정에서 오류가 발생한 경우
        """
        try:
            # LangChain을 사용하여 키워드 추출
            keywords = await self.chain.arun(user_input=user_input)
            
            # TODO: 추출된 키워드를 사용하여 벡터 유사도 검색 수행
            # 임시로 하드코딩된 응답 반환
            return [
                {"id": 1, "similarity_score": 0.95},
                {"id": 21, "similarity_score": 0.95},
                {"id": 32, "similarity_score": 0.95}
            ]
        except Exception as e:
            raise Exception(f"추천 생성 중 오류 발생: {str(e)}")
