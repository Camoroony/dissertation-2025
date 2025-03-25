import os 
import glob
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
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
        
        loader = TextLoader(txt_file, encoding="utf-8")
        document = loader.load()

        # Split the document into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
        docs = text_splitter.split_documents(document)

        # Add the split documents to the all_docs list
        all_docs.extend(docs)
        vectorstore = Chroma.from_documents(all_docs, embeddings, persist_directory=persistent_directory)
 else:
        print("Chroma_db already exists, no need to initialise.")
        vectorstore = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

 return vectorstore 