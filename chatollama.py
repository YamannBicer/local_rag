from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate

chat = ChatOllama(
    model="llama3.1",
    temperature=1,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a sarcastic comedian who makes fun of anything the user saysor asks.",
        ),
        (
            "human",
            "{input}"
        ),
    ]
)

chain = prompt | chat
user_input = input("Message ChatBot: ")
response = chain.invoke(
    {
        "input": user_input
    }
)


print(response.content)
