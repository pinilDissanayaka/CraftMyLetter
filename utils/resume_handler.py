import os
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader


def load_document(uploaded_document):
    upload_document_extension=os.path.splitext(load_document)[1]
    
    if upload_document_extension==".txt":
        loader=TextLoader(uploaded_document)
    elif upload_document_extension==".pdf":
        loader=PyPDFLoader(uploaded_document)
    elif upload_document_extension==".docx":
        loader=Docx2txtLoader(uploaded_document)
    
    if loader:
        resume_data=loader.load()
        
    return resume_data
