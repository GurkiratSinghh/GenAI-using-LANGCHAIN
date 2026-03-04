from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=os.getenv("HF_TOKEN")
)

print(client.chat_completion(
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=50
))