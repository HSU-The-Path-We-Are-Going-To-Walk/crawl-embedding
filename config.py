# config.py (환경 설정 파일)
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 🔹 LLM 인스턴스 (업스테이지 모델 사용)
LLM = ChatOpenAI(model="gpt-4o")

# 🔹 임베딩 모델 (업스테이지 임베딩 사용)
EMBEDDING = OpenAIEmbeddings(model="text-embedding-3-large")

# 🔹 Pinecone 벡터 DB 인덱스
INDEX_NAME = "goheung-notice"
DATABASE = PineconeVectorStore.from_existing_index(index_name=INDEX_NAME, embedding=EMBEDDING)
