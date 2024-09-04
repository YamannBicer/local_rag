from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document


def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
        separators=["\n\n", "\n"],
        keep_separator=False,
        is_separator_regex=False,
    )

    chunks = text_splitter.split_documents(documents)

    return chunks

def split_documents_with_special_character(documents: list[Document]):
    chunks = []

    for doc in documents:
        # Split the document at the '#' symbol
        split_docs = doc.page_content.split('#')
        for split_doc in split_docs:
            # Create a new Document for each chunk
            metadata = doc.metadata.copy()
            chunks.append(Document(page_content=split_doc.strip(), metadata=metadata))  # Use strip to remove any leading/trailing spaces

    return chunks





