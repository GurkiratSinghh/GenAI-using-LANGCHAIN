from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

# Step 1: Create endpoint
endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
)

# Step 2: Wrap into chat model
chat = ChatHuggingFace(llm=endpoint)

# Step 3: Invoke
response = chat.invoke("Continue this sentence: The capital of France is")

print(response.content)