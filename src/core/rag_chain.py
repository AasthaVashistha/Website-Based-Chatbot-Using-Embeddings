from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

# REMOVE: from src.core.rag_chain import get_rag_chain  <-- DELETE THIS LINE

def get_rag_chain(vectorstore):
    # Assignment requirement: Answers generated only from retrieved website content [cite: 66]
    template = """You are a helpful AI assistant. Use the following pieces of context to answer the question.
    If the answer is not available on the provided website, respond exactly with: 
    "The answer is not available on the provided website."
    
    Context: {context}
    History: {chat_history}
    Question: {question}
    Answer:"""

    QA_PROMPT = PromptTemplate(input_variables=["context", "chat_history", "question"], template=template)

    # LLM must be clearly mentioned and justified in README [cite: 63, 64]
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0) 
    
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        combine_docs_chain_kwargs={"prompt": QA_PROMPT}
    )x