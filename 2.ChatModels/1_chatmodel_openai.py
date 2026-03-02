from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI model
chatmodel=ChatOpenAI(model="gpt-4",temperature=0,max_completion_tokens=100)

result=chatmodel.invoke("What is the capital of India?")
print(result)
print(result.content)

