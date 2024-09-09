from langchain_community.embeddings.ollama import OllamaEmbeddings

# embeddings = OllamaEmbeddings(model="llama3.1")

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
