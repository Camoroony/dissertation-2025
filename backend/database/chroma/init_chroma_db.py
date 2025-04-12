import os 
import glob
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from database.mongodb.references_db import get_reference_url, get_reference
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def get_chroma_vectorstore(db_name: str, db_data: str):
 
 current_dir = os.path.dirname(os.path.abspath(__file__))
 persistent_directory = os.path.join(current_dir, "chroma_dbs", db_name)

 if not os.path.exists(persistent_directory):
     print("Chroma_db does not exist, initialising vector store...")

     current_dir = os.path.dirname(os.path.abspath(__file__))

     if db_data == "*":
      text_files_directory = os.path.join(current_dir, "chroma_data")
      txt_files = glob.glob(os.path.join(text_files_directory, "**", "*.txt"), recursive=True)
     else: 
      text_files_directory = os.path.join(current_dir, "chroma_data", db_data)
      txt_files = glob.glob(os.path.join(text_files_directory, "*.txt"))

     text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1300,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
        )

     chunks = []

     for txt_file in txt_files:
        print(f"Loading document: {txt_file}")

        txt_file_dir = os.path.basename(os.path.dirname(txt_file))
        
        doc_source = "N/A" if txt_file_dir == "workout_video_studies" else get_reference(os.path.basename(txt_file))

        loader = TextLoader(txt_file, "utf-8")
        document = loader.load()
        doc_chunks = text_splitter.split_documents(document)

        # Debug the chunks
        for i, chunk in enumerate(doc_chunks): 
            if doc_source != "N/A":
             chunk.metadata["full_source"] = f"[Title: {doc_source["title"]}, Author: {doc_source["author"]}, URL: {doc_source["url"]}]"
            else: chunk.metadata["full_source"] = "N/A"
            # print(f"\nChunk {i+1}:\n\n{chunk}\n\n{chunk.metadata["url"]}\n\n{'='*40}")  

        chunks.extend(doc_chunks)
        print(f"Document: {txt_file} loaded into chunks")


     vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory=persistent_directory)

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