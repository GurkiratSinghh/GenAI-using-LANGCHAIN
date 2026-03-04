from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Prompt Template
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}")
])

# Chat history
chat_history = []

domain = "cricket"

while True:

    user_input = input("You: ")

    if user_input == "exit":
        break

    # Create prompt dynamically
    prompt = chat_template.invoke({
        "domain": domain,
        "user_input": user_input,
        "chat_history": chat_history
    })

    # Model response
    result = model.invoke(prompt)

    print("AI:", result.content)

    # Update history
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=result.content))

print(chat_history)