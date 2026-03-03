from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

document=["What is the capital of France?",
          "What is the capital of Germany?",
          "how to make a cake?"]

result=embedding.embed_documents(document)
print(str(result))