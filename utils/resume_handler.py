import os
from langchain_community.document_loaders import Docx2txtLoader, TextLoader, PyPDFLoader


def load_document(uploaded_document):
    upload_document_extension=os.path.splitext(uploaded_document.name)[1]
    
    if upload_document_extension==".txt":
        loader=TextLoader(uploaded_document.name)
    elif upload_document_extension==".pdf":
        loader=PyPDFLoader(uploaded_document.name)
    elif upload_document_extension==".docx":
        loader=Docx2txtLoader(uploaded_document.name)
    
    if loader:
        resume_data=loader.load()
        
    return resume_data
