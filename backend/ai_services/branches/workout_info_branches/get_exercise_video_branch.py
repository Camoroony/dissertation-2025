from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore
from security.openai_api_key import get_openai_api_key

OPENAI_API_KEY = get_openai_api_key()

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

def get_exercise_video_ai(exercise: str):

    vectorstore = get_chroma_vectorstore(db_name="workout_video_studies_vs", db_data="workout_video_studies")

    vs_query = f"{exercise} videos"
    vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=5)

    context = format_context(vs_results)

    context_text = context["documents"]

    ai_query = (f"The individuals workout plan contains the {exercise}",
                "\nRecommend a youtube tutorial video for the exercise. ",
                "ONLY PROVIDE A LINK IN YOUR RESPONSE AND NOTHING ELSE.")

    ai_context = (
    "\n\n You will be provided with an exercise and you must recommend a tutorial video most relevant to the exercise."
    "\n Documents have been provided that may assist you in your response."
    + "\n IF THE DOCUMENTS DO NOT INCLUDE A RELEVANT VIDEO TO RECOMMEND, YOU MUST DISPLAY THE FOLLOWING MESSAGE: No video can be found for this exercise. "
    + f"\n\nHere are the following documents for you to use: {context_text}"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant who recommends tutorial videos regarding specific exercises."),
    ("system", "{ai_context}"),  
    ("human", "This is your task: {ai_query}")  
    ])


    chain = prompt | model | StrOutputParser()

    ai_response = chain.invoke({"ai_context": ai_context, "ai_query": ai_query})  

    print("\n--- Generated Response: ---")
    print("\n\nContent:")
    print("\n" + ai_response)

    return {
       "ai_response": ai_response
    }