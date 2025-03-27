from langchain_openai import ChatOpenAI
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from models.ai_models import MUSCLE_GROUPS
from database.chroma.init_chroma_db import get_chroma_vectorstore
from dotenv import load_dotenv
import os

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

prompt_context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n (ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER)"
    + "\n\n These are the relevant documents you must use to forumulate your answer:"
    + "\n\n {context_text}"
    )

ai_query = (
    "\n\n This is your question to answer based on the documents:"
    + "\n\n What {available_equipment} {muscle} exercises do you recommend? Provide at least three, but an upmost of five if you have them to share. \n\n" 
    + "\n\n Please provide them all in a list format alongside the correpsonding muscle they train and provide a one line explanation for why you have chosen that exercise."
    )

def get_available_equipment_context(available_equipment: str):

    vectorstore = get_chroma_vectorstore(db_name="workout_exercises_db", db_data="workout_exercise_studies")

    vectorstore_response = []

    ai_response = []

    for muscle in MUSCLE_GROUPS:
     vs_query = f"What are the best {available_equipment} {muscle} exercises?"
     vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=5)

     context_text = "\n\n---\n\n".join([doc.page_content for doc, _score, in vs_results])

    #  print(context_text)

     vectorstore_response.append(context_text)

     formatted_prompt_context = prompt_context.format(context_text=context_text)
     formatted_ai_query = ai_query.format(available_equipment=available_equipment, muscle=muscle)

     prompt = ChatPromptTemplate.from_messages([   
      ("system", "You are an assistant who provides a description on an individuals exercise equipment availability as well as advice on what exercises the individual could choose and why."),
      ("system", formatted_prompt_context),  
      ("human", formatted_ai_query)])

     chain = prompt | model | StrOutputParser()

     chain_response = chain.invoke({"formatted_prompt_context": formatted_prompt_context, "formatted_ai_query": formatted_ai_query})  
     ai_response.append(chain_response)

    print("\n\n--- Generated Response: ---\n\n")
    for response in ai_response:
     print(response + "\n\n")

    return ai_response