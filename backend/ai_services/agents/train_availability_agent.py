from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "chroma_db")

embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY, model="text-embedding-3-small")

if not os.path.exists(persistent_directory):
    print("Chroma_db does not exist, initialising vector store...")

    loader = TextLoader("gymshark.txt", encoding="utf-8")
    document = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(document)

    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")
else:
    print("Chroma_db already exists, no need to initialise.")
    vectorstore = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

retriever = vectorstore.as_retriever(search_type= "similarity_score_threshold",
                                     search_kwargs={"k": 3, "score_threshold": 0.3})

query = "What are the negatives of a Body Part split workout plan?"

relevant_docs = retriever.invoke(query)

print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")

prompt = (
    "Here are some pieces of content that may help you answer the following question:"
    + query 
    +"\n\n Relevant Document: \n"
    + "\n\n".join([doc.page_content for doc in relevant_docs])
    + "\n\n Only provide an answer based on the following documents. If your answer is not from the document, please state this in your answer."
)

model = ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    HumanMessage(content="You are a helpful muscle hypertrophy knowledge assistant who provides answers to questions."),
    SystemMessage(content=prompt)
]

llm_response = model.invoke(messages)

print("\n--- Generated Response: ---")
print("Content:")
print(llm_response.content)