import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Store in the data folder as required by the modular structure
CHROMA_PATH = os.path.join(os.getcwd(), "data", "vector_db")

def save_to_vector_store(documents):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    # Persist the vector database to disk
    vectorstore.persist()
    return vectorstore

def load_vector_store():
    # Only load if the directory exists and is not empty
    if os.path.exists(CHROMA_PATH) and os.listdir(CHROMA_PATH):
        return Chroma(
            persist_directory=CHROMA_PATH, 
            embedding_function=OpenAIEmbeddings()
        )
    return None