from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="conversational"
)

# Step 2: Wrap into chat model
chat = ChatHuggingFace(llm=endpoint)
st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    result=chat.invoke(user_input)
    st.write(result.content)

