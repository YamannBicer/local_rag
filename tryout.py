from langchain.schema import Document


def split_documents(documents: list[Document]):
    split_docs = []

    for doc in documents:
        # Split the document at the '#' symbol
        chunks = doc.page_content.split('#')
        for chunk in chunks:
            # Create a new Document for each chunk
            split_docs.append(Document(page_content=chunk.strip()))  # Use strip to remove any leading/trailing spaces

    return split_docs




# Call the function to split the text
split_result = split_documents(documents)

# Print the results
for idx, chunk in enumerate(split_result):
    print(f"Chunk {idx + 1}:")
    print(chunk.page_content)
    print("=" * 40)
