import os 
import glob
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def get_chroma_vectorstore(db_name: str, db_data: str):
 
 current_dir = os.path.dirname(os.path.abspath(__file__))
 persistent_directory = os.path.join(current_dir, "chroma_dbs", db_name)

 if not os.path.exists(persistent_directory):
     print("Chroma_db does not exist, initialising vector store...")

     current_dir = os.path.dirname(os.path.abspath(__file__))
     text_files_directory = os.path.join(current_dir, "chroma_data", db_data)
     txt_files = glob.glob(os.path.join(text_files_directory, "*.txt"))

     all_docs = []

     for txt_file in txt_files:
        print(f"Loading document: {txt_file}")

        loader = TextLoader(txt_file, "utf-8")

        document = loader.load()

        docs = custom_splitter(document[0])

        for i, chunk in enumerate(docs):  
         print(f"\nChunk {i+1}:\n{chunk}\n{'='*40}")  


        all_docs.extend(docs)
        vectorstore = Chroma.from_documents(all_docs, embeddings, persist_directory=persistent_directory)
 else:
        print("Chroma_db already exists, no need to initialise.")
        vectorstore = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

 return vectorstore 

def custom_splitter(document: Document, separator="---") -> list[Document]:
    
    chunks = document.page_content.split(separator)

    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

    documents = []
    for chunk in chunks:
        doc = Document(page_content=chunk)
        documents.append(doc)
    
    return documents