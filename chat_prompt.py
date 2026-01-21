import os
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.chat_engine import CondensePlusContextChatEngine
from llama_index.llms.openai import OpenAI
from llama_index.core.retrievers import VectorIndexRetriever
import signal

# OpenAI 키
os.environ["OPENAI_API_KEY"] = "MY API KEY"

# GPT 모델 초기화
llm = OpenAI(model="gpt-4o", temperature=0)

# 인덱스 로딩
storage_context = StorageContext.from_defaults(persist_dir="framework_index")
index = load_index_from_storage(storage_context)

# retriever 구성
retriever = VectorIndexRetriever(index=index)

# ChatEngine 설정
chat_engine = CondensePlusContextChatEngine.from_defaults(
	retriever=retriever,
	llm=llm,
	system_prompt="내가 만드는 프레임워크는 PointWeb이라고 부르고, 넌 웹개발자 전문 AI야. 항상 다음과 같은 코딩 스타일을 따라야해, -PHP는 '<?php'를 항상 왼쪽에 붙여 써. - '<?= ?>' 대신 '<?php echo ?>'를 사용.- 변수명은 언더스코어(_)로 구분하고 12자 이내로 직관적으로. - 들여쓰기는 tab으로. - HTML에서 echo할 때만 '<?php ?>' 한 줄 사용 허용.", 
	verbose=True
)

# Ctrl+C 복사시 종료 방지
def handler(sig, frame):
	print("\n복사(Ctrl+C) 감지됨 → 종료하지 않고 계속 대기합니다.")
signal.signal(signal.SIGINT, handler)

# 대화 루프
print(" GPT 대화 세션 시작 (종료하려면 'exit' 입력)\n")

while True:
	query = input("질문: ")
	if query.strip().lower() in ["exit", "종료", "quit"]:
		print("'exit' 입력됨 → 종료합니다.")
		break

	response = chat_engine.chat(query)
	print(f"\nGPT 응답:\n{response.response}\n")
