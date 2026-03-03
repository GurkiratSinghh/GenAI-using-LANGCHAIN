from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

document=["What is the capital of France?",
          "What is the capital of Germany?"]

result = embedding.embed_documents(document)

print(str(result))