from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Google Gemini model
chatmodel=ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0,max_completion_tokens=100)

result=chatmodel.invoke("What is the capital of India?")
print(result)
print(result.content)