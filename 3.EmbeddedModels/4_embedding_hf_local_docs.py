from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
document=["What is the capital of France?",
          "What is the capital of Germany?"]

result=embedding.embed_documents(document)
print(str(result))