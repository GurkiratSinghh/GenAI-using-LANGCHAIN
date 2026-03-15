from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="conversational"
)

# Step 2: Wrap into chat model
chat = ChatHuggingFace(llm=endpoint)
st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    result=chat.invoke(user_input)
    st.write(result.content)

