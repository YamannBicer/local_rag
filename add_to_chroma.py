from langchain_chroma import Chroma
from langchain.schema.document import Document
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"


def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        collection_name="vector_database",
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )

    db.reset_collection()  # Clears all documents from the database.
    print("🗑️ Cleared all documents from the database")


    chunk_ids = [chunk.metadata["id"] for chunk in chunks]
    db.add_documents(chunks, ids=chunk_ids)

    print(f"✅ {len(chunk_ids)} documents reloaded.")


def inspect_chroma():
    db = Chroma(
        collection_name="vector_database",
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )

    print(db.get().keys())
    # print(db.get()["ids"])
    # print(db.get(ids=["data\\guide.txt:10"]))