from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()

# Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Prompt template
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

file_path = r"D:\Langchain\LangChain_Prompts\Chatbots\chat_history.txt"

chat_history = []

# Load chat history from txt
if os.path.exists(file_path):

    with open(file_path, "r") as f:

        for line in f:

            line = line.strip()

            if line.startswith("HumanMessage"):
                content = re.search(r'content="(.*)"', line)
                if content:
                    chat_history.append(HumanMessage(content=content.group(1)))

            elif line.startswith("AIMessage"):
                content = re.search(r'content="(.*)"', line)
                if content:
                    chat_history.append(AIMessage(content=content.group(1)))

# Chat loop
while True:

    query = input("You: ")

    if query.lower() == "exit":
        print("Chat ended.")
        break

    # Generate prompt
    prompt = chat_template.invoke({
        "chat_history": chat_history,
        "query": query
    })

    # Call Gemini
    response = model.invoke(prompt)

    print("AI:", response.content)

    # Update chat history
    chat_history.append(HumanMessage(content=query))
    chat_history.append(AIMessage(content=response.content))

    # Save to txt
    with open(file_path, "a") as f:
        f.write(f'HumanMessage(content="{query}")\n')
        f.write(f'AIMessage(content="{response.content}")\n')