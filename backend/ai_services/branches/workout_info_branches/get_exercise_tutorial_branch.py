from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore


load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

def get_exercise_tutorial_ai(exercise: str):

    vectorstore = get_chroma_vectorstore(db_name="workout_exercise_studies_vs", db_data="workout_exercise_studies")

    vs_query = f"{exercise} How To"
    vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=5)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"]

    ai_query = (f"The individuals workout plan contains the {exercise}\n",
                "Create a tutorial on how to do this exercise.")

    ai_context = (
    "\n\n You will be provided with an exercise and you must make a tutorial on how to do it."
    "\n Documents have been provided that may assist you in your response."
    + "\n YOU MUST ONLY MAKE A TUTORIAL ON HOW TO DO THIS EXERCISE USING THE DOCUMENTS PROVIDED AND NOTHING ELSE."
    + "\n IF THE DOCUMENTS PROVIDED DO NOT GIVE YOU THE NECESSARY INFORMATION TO COMPLETE THE TASK, STATE THAT THIS IS THE CASE AND THAT YOU CANNOT PROVIDE A TUTORIAL."
    + "\n DO NOT MAKE UP A TUTORIAL IF YOU DO NOT HAVE THE NECESSARY DOCUMENTS TO MAKE A TUTORIAL."
    + "\n When you use any information from a source or sources, make sure to refer to the source directly in your response in this format: "
    + " ' [Source: Title: source_title, Author: source_author, URL: source_url]' to give context to the user."
    + f"\nHere are the following documents for you to use: {context_text}"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant who provides tutorials on how to do a specific exercise."),
    ("system", "{ai_context}"),  
    ("human", "This is your task: {ai_query}")  
    ])


    chain = prompt | model | StrOutputParser()

    ai_response = chain.invoke({"ai_context": ai_context, "ai_query": ai_query})  

    print("\n--- Generated Response: ---")
    print("\n\nContent:")
    print("\n" + ai_response)
    print("\nSources used:\n")
    print(sources)

    return {
       "ai_response": ai_response,
       "sources": sources
    }