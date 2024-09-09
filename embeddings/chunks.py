def index_chunks(chunks):
    chunk_index = 1
    for chunk in chunks:
        source = chunk.metadata.get("source")

        chunk_id = f"{source}:{chunk_index}"
        chunk_index += 1
        chunk.metadata["id"] = chunk_id

    return chunks

def inspect_chunks(chunks):
    for chunk in chunks[:5]:
        print("\n\n",chunk.metadata)
        print(chunk.page_content)
