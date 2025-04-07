from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore


load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

def get_exercise_video_ai(exercise: str):

    vectorstore = get_chroma_vectorstore(db_name="workout_videos_db", db_data="workout_video_studies")

    vs_query = f"{exercise} videos"
    vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=1)

    context = format_context(vs_results)

    context_text = context["documents"]

    ai_query = (f"The individuals workout plan contains the {exercise}",
                "\nRecommend a youtube tutorial video for the exercise and provide the link for it.")

    ai_context = (
    "\n\n You will be provided with an exercise and you must recommend a tutorial video most relevant to the exercise."
    "\n Documents have been provided that may assist you in your response."
    + "\n If the documents do NOT include a relevant video or you cannot confidently suggest one based on them, return the following message exactly:."
    + "\n We cannot find a video to recommend."
    + f"\nHere are the following documents for you to use: {context_text}"
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