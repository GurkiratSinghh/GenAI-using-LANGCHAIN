from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Anthropic model
chatmodel=ChatAnthropic(model="claude-3.5-sonnet-20241022",temperature=0,max_completion_tokens=100)

result=chatmodel.invoke("What is the capital of India?")
print(result.content)
 