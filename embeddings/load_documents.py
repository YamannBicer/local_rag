from langchain_community.document_loaders import PyPDFDirectoryLoader, DirectoryLoader, TextLoader

DATA_PATH = "../data"

def load_documents(inspect=False):
    # Define the loader for PDF files
    pdf_loader = PyPDFDirectoryLoader(DATA_PATH)

    # Define the loader for TXT files
    txt_loader = DirectoryLoader(DATA_PATH, glob="*.txt", loader_cls=lambda path: TextLoader(path, encoding="utf-8"))

    # Load all documents
    documents = pdf_loader.load() + txt_loader.load()

    if inspect:
        inspect_documents(documents)

    return documents

def inspect_documents(documents):
    for doc in documents:
        print(doc.metadata.get("source"))
        # print(doc.metadata)
        # print(doc.page_content)




