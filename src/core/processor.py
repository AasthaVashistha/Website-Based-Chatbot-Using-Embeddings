from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def process_text(text, url, title, chunk_size=1000, chunk_overlap=100):
    # Configurable chunking [cite: 40]
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(text)
    
    # Maintain metadata [cite: 41, 42, 43]
    docs = [Document(page_content=c, metadata={"source": url, "title": title}) for c in chunks]
    return docs