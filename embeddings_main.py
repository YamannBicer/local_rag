from load_documents import load_documents
from split_documents import split_documents, split_documents_with_special_character
from add_to_chroma import add_to_chroma, inspect_chroma
from chunks import index_chunks, inspect_chunks


def main():
    documents = load_documents()
    chunks = split_documents_with_special_character(documents)
    chunks = index_chunks(chunks)
    # inspect_chunks(chunks)
    add_to_chroma(chunks)
    # inspect_chroma()


if __name__ == "__main__":
    main()









