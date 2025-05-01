from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.schema.runnable import RunnableParallel
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from models.ai_models import MUSCLE_GROUPS
from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore
from security.openai_api_key import get_openai_api_key


OPENAI_API_KEY = get_openai_api_key()

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)


def get_workout_exercises_ai(available_equipment: str):
  
  equipment_context_response = get_available_equipment_context(available_equipment)

  sources = equipment_context_response["sources"]

  content = "\n\n".join(f"**{muscle} Exercises:**\n{exercises}" for muscle, exercises in equipment_context_response['ai_response'].items())

  ai_showcase_content = (
    f"Equipment the indvidual has access to: {available_equipment}\n\n"
    + f"The content for you to display: {content}"
    )
  
  prompt = ChatPromptTemplate.from_messages([   
      ("system", "You are an formatting assistant who provides a 1 to 2 line summary on an individual and the types of exercise equipment they have access to."),
      ("system", "Once you have provided the summary, you display formatted exercise recommendations."),
      ("system", "DO NOT ALTER ANY CONTENT YOU HAVE BEEN GIVEN TO USE, ONLY DISPLAY IT."),
      ("human", f"This is the following content for you to use: {ai_showcase_content}")])
  
  chain = prompt | model | StrOutputParser()

  ai_response = chain.invoke({"ai_showcase_content": ai_showcase_content})  

  print(ai_response)

  return {
     "ai_response": ai_response,
     "sources": sources
  }


def get_available_equipment_context(available_equipment: str):

    vectorstore = get_chroma_vectorstore(db_name="workout_exercise_studies_vs", db_data="workout_exercise_studies")

    if available_equipment == "Full gym access":
      available_equipment = ""

    chains = {}
    sources = set()

    for muscle in MUSCLE_GROUPS:
      muscle_method = process_muscle(muscle, available_equipment, vectorstore)

      chains[muscle] = muscle_method["chain"]
      sources.update(muscle_method["sources"])

    parallel_chain = RunnableParallel(**chains)

    ai_response = parallel_chain.invoke({})

    print("\n\n--- Generated Response: ---\n\n")
    for k, v in ai_response.items():
     print(f"Recommended {k} exercises:" + "\n\n")
     print(f"{v}" + "\n\n")

    return {
       "ai_response": ai_response,
       "sources": sources
    }


def process_muscle(muscle: str, available_equipment: str, vectorstore: Chroma):
     
    prompt_context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n (ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER)"
    + "\n\n These are the relevant documents you must use to forumulate your answer:"
    + "\n\n {context_text}"
    )

    ai_query = (
    "\n\n This is your question to answer based on the documents:"
    + "\n\n What {available_equipment} {muscle} exercises do you recommend?\n"
    + "You must provide at least three, but an upmost of five if you have them to share. \n\n" 
    + "Provide all the exercises you recommend in a list format alongside the corresponding muscle they train and provide a one line explanation "
    + "for why you have chosen that exercise."
    )

    vs_query = f"What are the best {available_equipment} {muscle} exercises?"
    vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=5)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"]

    print(context_text)

    formatted_prompt_context = prompt_context.format(context_text=context_text)
    formatted_ai_query = ai_query.format(available_equipment=available_equipment, muscle=muscle)

    prompt = ChatPromptTemplate.from_messages([   
      ("system", "You are an assistant who provides a description on an individuals exercise equipment availability as well as advice on what exercises the individual could choose and why."),
      ("system", formatted_prompt_context),  
      ("human", formatted_ai_query)])

    chain = prompt | model | StrOutputParser()

    return {
       "chain": chain,
       "sources": sources
    }