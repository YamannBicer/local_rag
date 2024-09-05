from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

SYSTEM_PROMPT = "You are a helpful and informative assistant that provides information and answers questions based on the context given."

CHAT_PROMPT_TEMPLATE = """
Here is the previous conversation history:

{chat_history}

Keep the conversation history in mind when answering user's questions.
Answer the current question based only on the following context:

{context}

Answer this new question based on the above context: {input}
"""



def main():
    chat_history = ""
    while True:
        query_text = input("Message ChatBot: ")
        response, sources = query_chatbot(query_text, chat_history)
        print(f"Query: {query_text}")
        print(f"Response: {response}")
        print("Sources:\n", sources, "\n\n\n")

        chat_history += f"User: {query_text}\nAssistant: {response}\n\n"



def query_chatbot(query_text: str, chat_history: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(collection_name="vector_database",persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=3)
    sources = [doc.metadata.get("id") for doc, _ in results]

    # for i, (doc, score) in enumerate(results):
    #     print(f"Chunk {i + 1}:")
    #     print(f"{doc.page_content}")
    #     print(f"Chunk ID: {doc.metadata.get('id')}")
    #     print(f"Score: {score}\n\n")

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", CHAT_PROMPT_TEMPLATE.format(chat_history=chat_history, context=context_text, input=query_text))
        ]
    ).format_messages()

    chat = ChatOllama(model="llama3.1",temperature=0)
    response_text = chat.invoke(prompt)


    return response_text.content, "\n".join(sources)

if __name__ == "__main__":
    main()
