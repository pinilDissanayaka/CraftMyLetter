import os
from tempfile import TemporaryDirectory
from langchain_community.document_loaders import Docx2txtLoader, TextLoader, PyPDFLoader


def load_document(uploaded_document):
    try:
        temp_dir=TemporaryDirectory()
        temp_file_path=os.path.join(temp_dir.name, uploaded_document.name)
        
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_document.read())
        
        upload_document_extension=os.path.splitext(uploaded_document.name)[1]
        
        if upload_document_extension==".txt":
            loader=TextLoader(temp_file_path)
        elif upload_document_extension==".pdf":
            loader=PyPDFLoader(temp_file_path)
        elif upload_document_extension==".docx":
            loader=Docx2txtLoader(temp_file_path)
        
        if loader:
            resume_data=loader.load()
            
        return resume_data
    finally:
        temp_dir.cleanup()
