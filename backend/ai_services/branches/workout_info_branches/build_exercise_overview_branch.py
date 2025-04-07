from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from models.ai_models import ExerciseOverviewResponse


load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini").with_structured_output(schema=ExerciseOverviewResponse)

def build_exercise_overview_ai(context):

    prompt_template = ChatPromptTemplate.from_messages([

        ("system", "You are an exercise tutorial generator who generates text explanations and video links to tutorials for an individual."),

        ("system", "You will be provided with pre-generated guides and video links for the exercise in question. "
                   + "Use these to generate a final formatted response."),     

        ("human", "Generate me an **Exercise Tutorial** for an individual with the following context:\n"
                  + "- **Exercise information**: {exercise_info}\n\n"
                  + "- **Tutorial video**: {tutorial_video}\n\n")
    ])

   
    formatted_input = {
        "exercise_info": context["exercise_tutorial_context"]["ai_response"],
        "tutorial_video": context["exercise_video_context"]["ai_response"]
    }

    # final_prompt = prompt_template.format(**formatted_input)

    sources = context["exercise_tutorial_context"]["sources"]
    
    chain = prompt_template | model

    
    response = chain.invoke(formatted_input)

    return {
        "sources_used": sources,
        "response": response
    }

