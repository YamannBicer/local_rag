from langchain_chroma import Chroma
from langchain.schema.document import Document
from get_embedding_function import get_embedding_function

CHROMA_PATH = "../chroma"


def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        collection_name="vector_database",
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )

    # reset the database and look at the number of documents
    # print(len(set(db.get()['ids'])))
    # db.reset()
    # print(len(set(db.get()['ids'])))

    # Get the list of existing document IDs from the Chroma database
    existing_ids = set(db.get()['ids'])  # Assumes db.get() returns a dict with an 'ids' key
    new_ids = set([chunk.metadata["id"] for chunk in chunks])

    # Filter out chunks that already exist in the database
    new_chunks = [chunk for chunk in chunks if chunk.metadata["id"] not in existing_ids]


    new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]

    print(f"🔍 Found {len(chunks)} documents. {len(existing_ids & new_ids)} already exist in the database. {len(new_chunks)} new documents to add.")
    if new_chunks:
        db.add_documents(new_chunks, ids=new_chunk_ids)
        print(f"✅ {len(new_chunk_ids)} new documents added.")
    else:
        print("✅ All documents already exist in the database.")


def inspect_chroma():
    db = Chroma(
        collection_name="vector_database",
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )

    print(db.get().keys())
    # print(db.get()["ids"])
    # print(db.get(ids=["data\\guide.txt:10"])) only load non existent documents