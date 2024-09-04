from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate

chat = ChatOllama(
    model="llama3.1",
    temperature=0,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a sarcastic and fun companion who makes a joke of anything the user says or asks.",
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
