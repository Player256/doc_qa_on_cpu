from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from prompts import qa_template
from llm import load_llm

def set_qa_prompt():
    prompt = PromptTemplate(template=qa_template,
                            input_variables=['context','question'])
    return prompt


def build_retrival_qa(llm,prompt,vectordb):
    llm = load_llm()
    dbqa = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type = 'stuff',
                                       retriever=vectordb.as_retriever(search_kwargs={'k':2}),
                                       return_source_documents=True,
                                       chain_type_kwargs={'prompt':prompt})
    return dbqa


def setup_dbqa():
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device':'cpu'})
    vectordb = FAISS.load_local('vectorstore/db_faiss',embeddings)
    qa_prompt = set_qa_prompt()
    llm = load_llm()
    dbqa = build_retrival_qa(llm,qa_prompt,vectordb)

    return dbqa