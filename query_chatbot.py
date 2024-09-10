from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from embeddings.get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

SYSTEM_PROMPT = "You are a helpful and informative assistant that provides accurate, relevant and helpful information and answers questions based on the context and instructions given."

CHAT_PROMPT_TEMPLATE = """
Here is the previous conversation history:

{chat_history}

Keep the conversation history in mind when answering user's questions.

Keep the following information in mind ONLY IF the question is about finding a specific data in a database with its destination_table and meta_id otherwise ignore i:

If you are asked about how to find certain data in the database, you can provide directions by considering the information below.

destination_table tells he table where the data is located.
meta_id tells the id of the data in the destination_table.
data names contain the information for you to relate which data the user is asking about.

data names might contain below information:
an ISO country code (NO for norway etc.) if there are none then it is about germany (DE: deutschland),
it might contain a number next to the ISO country code which represents which electrical region of the country it is about, when there are multiple data names with same names with only difference being the number next to the ISO country code keep this in mind when answering the question.
whether the data is electiricity production or electricity consumption (load) data,
if it is production then it might contain which resource is used for production (wind, solar, wind_and_solar, biomass, etc.),
whether the data is actual data or forecasted data,
some of the names might be in german language (hochrehnung for forecast etc.).

If the question is about finding a specific data in a database with its destination_table and meta_id, you can provide directions by considering the information above.

Also utilize the context below in order to provide a more accurate, helpful and relevant response:
{context}

Provide an informative and relevant answer to this new question based on the above context: {input}
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
    results = db.similarity_search_with_score(query_text, k=7)
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
            ("human", CHAT_PROMPT_TEMPLATE.format(chat_history=chat_history, context=context_text, input=query_text))
        ]
    ).format_messages()

    chat = ChatOllama(model="llama3.1",temperature=0)
    response_text = chat.invoke(prompt)


    return response_text.content, "\n".join(sources)

if __name__ == "__main__":
    main()
