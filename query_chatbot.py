from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_ollama.llms import OllamaLLM
from langchain_chroma import Chroma
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

SYSTEM_PROMPT = "You are a helpful and informative assistant that provides information and answers questions based on the context given."

CHAT_PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

Answer the question based on the above context: {input}
"""


def main():
    while True:
        query_text = input("Message ChatBot: ")
        query_chatbot(query_text)


def query_chatbot(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(collection_name="vector_database",persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=3)
    sources = [doc.metadata.get("id") for doc, _ in results]

    for i, (doc, score) in enumerate(results):
        print(f"Chunk {i + 1}:")
        print(f"{doc.page_content}")
        print(f"Chunk ID: {doc.metadata.get('id')}")
        print(f"Score: {score}\n\n")

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", CHAT_PROMPT_TEMPLATE.format(context=context_text, input=query_text))
        ]
    ).format_messages()

    chat = ChatOllama(model="llama3.1",temperature=0)
    response_text = chat.invoke(prompt)

    print(f"Query: {query_text}")
    print( f"Response: {response_text.content}")
    print("Sources: ",*sources, "\n\n\n")

    return


if __name__ == "__main__":
    main()