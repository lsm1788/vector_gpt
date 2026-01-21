import os
os.environ["OPENAI_API_KEY"] = "MY API KEY"


from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

print("문서 읽기 시작")
docs = SimpleDirectoryReader("framework_docs").load_data()
print(f"문서 개수: {len(docs)}")

index = VectorStoreIndex.from_documents(docs)
print("인덱스 생성 완료")

index.storage_context.persist("framework_index")
print("벡터 인덱스 저장 완료")
