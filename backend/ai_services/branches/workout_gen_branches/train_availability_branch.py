from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os
import glob

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "..", "..", "..", "database", "chroma_dbs", "workout_split_db")
text_files_directory = os.path.join(current_dir, "..", "..", "..", "database", "chroma_data")
txt_files = glob.glob(os.path.join(text_files_directory, "*.txt"))
embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY, model="text-embedding-3-small")
model = ChatOpenAI(model="gpt-4o-mini")

def get_availability_recommendation(training_availability: int):

    if not os.path.exists(persistent_directory):
     print("Chroma_db does not exist, initialising vector store...")

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

    retriever = vectorstore.as_retriever(search_type= "similarity_score_threshold",
                                     search_kwargs={"k": 6, "score_threshold": 0.4})

    vector_query = f"{training_availability} day workout split"

    ai_query = f"The individual can only train {training_availability} days per week, what is the best workout split for them?"

    relevant_docs = retriever.invoke(vector_query)

    print("\n--- Relevant Documents ---")
    for i, doc in enumerate(relevant_docs, 1):
     print(f"Document {i}:\n{doc.page_content}\n")

    context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n\n Some documents contain references to other sources by numbers e.g. [1], [2] etc. These numbers correspond with references that are marked with the same numbers at the end of documents e.g. [2] Example university (year), Paper title etc.."
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER"
    # + "\n\n When generating your answer, include inline number citations to the references from the relevant documents you used to come up with your answer (e.g. [1], [2] etc.)"
    # + "\n\n Provide the references used in your response at the end with the same number they have in the inline citations you generated."
    # + "\n\n Number these references to match the inline references you gave in the response. e.g.:"
    # + "\n Response: This is text response content gathered from a reference [1]"
    # + "\n References: [1] Reference author (reference year) paper title etc."
    + "\n\n These are the relevant documents you must use to forumulate your answer:"
    + "\n\n Relevant Documents: \n"
    + "\n\n".join([doc.page_content for doc in relevant_docs])
    )

    messages = [
    SystemMessage(content="You are an assistant who provides concise advice on what workout split an individual should choose based on their characteristics.\n"),
    SystemMessage(content=context),
    HumanMessage(content=f"\n\n This is your question to answer based on the documents: {ai_query}")
    ]

    llm_response = model.invoke(messages)

    print("\n--- Generated Response: ---")
    print("Content:")
    print(llm_response.content)