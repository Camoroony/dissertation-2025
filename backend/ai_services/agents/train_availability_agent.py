from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



loader = TextLoader("gymshark.txt", encoding="utf-8")
document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(document)

embedding_function = OpenAIEmbeddings(api_key=OPENAI_API_KEY, model="text-embedding-3-small")

vectorstore = Chroma.from_documents(docs, embedding_function, persist_directory="./chroma_db")

retriever = vectorstore.as_retriever(search_type= "similarity_score_threshold",
                                     search_kwargs={"k": 3, "score_threshold": 0.3})

query = "What is the best 4 day workout split?"

relevant_docs = retriever.invoke(query)

print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")

