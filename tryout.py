from langchain.schema import Document


def split_documents(documents: list[Document]):
    split_docs = []

    for doc in documents:
        # Split the document at the '#' symbol
        chunks = doc.page_content.split('###')
        for chunk in chunks:
            # Create a new Document for each chunk
            split_docs.append(Document(page_content=chunk.strip()))  # Use strip to remove any leading/trailing spaces

    return split_docs


# Example text to be split
text_content = """
Contents

Section 1: Who Should Use This Guide?
Section 2: How to Log into the Application?
Section 3: Overview of the Application
Section 3.1: Main Menu
Section 3.1.1: Reports
###
Section 3.1.2: Trade Management
Section 3.1.3: Workflow Monitoring Management
Section 3.1.4: Data Entry
Section 3.1.5: View Logs
Section 3.1.6: Invoice Management
Section 3.1.7: Contract Management
Section 3.1.8: Power Plant Management
###
Section 3.2: My Screens
###
Section 3.3: Research
Section 3.4: Market & News
Section 3.5: Today
Section 3.6: Profile
Section 3.7: Notifications
"""

# Create a list of documents (using the Langchain Document class)
documents = [Document(page_content=text_content)]

# Call the function to split the text
split_result = split_documents(documents)

# Print the results
for idx, chunk in enumerate(split_result):
    print(f"Chunk {idx + 1}:")
    print(chunk.page_content)
    print("=" * 40)
