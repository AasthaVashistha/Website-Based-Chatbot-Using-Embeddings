import streamlit as st
from core.crawler import extract_content
from core.processor import process_text
from utils.vector_store import save_to_vector_store, load_vector_store
from core.rag_chain import get_rag_chain

from core.rag_chain import get_rag_chain

st.set_page_config(page_title="Humanli.ai Website Chatbot")
st.title("Website Chatbot 🤖")

# Initialize Session Memory [cite: 73, 76]
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

url = st.text_input("Enter a website URL:") 

if st.button("Index Website"): 
    with st.spinner("Crawling and indexing..."):
        text, title = extract_content(url)
        if text:
            docs = process_text(text, url, title)
            save_to_vector_store(docs)
            st.success("Indexing complete!")
        else:
            st.error(f"Error: {title}") # Handles unreachable/invalid URLs [cite: 24]

# Chat Interface [cite: 82]
query = st.chat_input("Ask a question about the website:")
if query:
    vectorstore = load_vector_store()
    if vectorstore:
        chain = get_rag_chain(vectorstore)
        response = chain({"question": query, "chat_history": st.session_state.chat_history})
        
        st.session_state.chat_history.append((query, response["answer"]))
        for q, a in st.session_state.chat_history:
            st.chat_message("user").write(q)
            st.chat_message("assistant").write(a)
    else:
        st.warning("Please index a website first.")