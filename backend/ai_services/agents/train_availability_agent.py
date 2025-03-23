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

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    docs = text_splitter.split_documents(document)

    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")
else:
    print("Chroma_db already exists, no need to initialise.")
    vectorstore = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

retriever = vectorstore.as_retriever(search_type= "similarity_score_threshold",
                                     search_kwargs={"k": 1, "score_threshold": 0.2})

vector_query = "Body part split disadavantages"

ai_query = "What are the disadvanatages of a body part split?"

relevant_docs = retriever.invoke(vector_query)

print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")

context = (
    "Here are some relevant documents that may help you answer the question:"
    +"\n\n Relevant Documents: \n"
    + "\n\n".join([doc.page_content for doc in relevant_docs])
    + "\n\n Some documents contain references to other sources by numbers e.g. [1], [2] etc. These numbers correspond with references that are marked with the same numbers at the end of documents e.g. [2] Example university (year), Paper title etc.."
    + "\n\n Your job is to provide an answer based on the following documents. If your answer is not from the document, state this in your answer."
    + "\n\n When generating your answer, include inline number citations to the references from the relevant documents you used to come up with your answer (e.g. [1], [2] etc.)"
    + "\n\n Provide the references used in your response at the end with the same number they have in the inline citations you generated."
    + "\n\n Number these references to match the inline references you gave in the response. e.g.:"
    + "\n\n Response: This is text response content gathered from a reference [1]"
    +"\n\n References: [1] Reference author (reference year) paper title etc."
)

model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="You are a helpful assistant who provides answers to workout split questions and provides the references for the knowledge used in your answers and at the end of the answer.\n"),
    SystemMessage(content=context),
    HumanMessage(content=f"\n\n This is your question to answer: {ai_query}")
]

llm_response = model.invoke(messages)

print("\n--- Generated Response: ---")
print("Content:")
print(llm_response.content)