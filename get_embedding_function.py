from langchain_community.embeddings.ollama import OllamaEmbeddings



def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    embeddings = OllamaEmbeddings(model="llama3.1")


    return embeddings
