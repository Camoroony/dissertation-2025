from langchain.schema.runnable import RunnableParallel, RunnableLambda
from models.input_models import WorkoutGenInput
from ai_services.branches.workout_gen_context.workout_split_branch import get_workout_split_ai
from ai_services.branches.workout_gen_context.workout_exercises_branch import get_workout_exercises_ai
from ai_services.branches.workout_gen_context.workout_sets_branch import get_workout_sets_ai
from ai_services.branches.workout_gen_context.build_workout_plan_branch import build_workout_plan


def generate_workout_plan(workout_input: WorkoutGenInput):

    workout_split_lambda = RunnableLambda(
        lambda _: get_workout_split_ai(workout_input.training_availability))
    
    workout_exercises_lambda = RunnableLambda(
        lambda _: get_workout_exercises_ai(workout_input.available_equipment)
    )

    workout_sets_lambda = RunnableLambda(
        lambda _: get_workout_sets_ai(workout_input.experience_level, workout_input.training_focus)
    )


    context_chain = RunnableParallel(
        training_availability_context = workout_split_lambda,
        training_equipment_context = workout_exercises_lambda,
        training_experience_context = workout_sets_lambda
    )

    final_generation = RunnableLambda(lambda x: build_workout_plan(workout_input, x))

    final_chain = context_chain | final_generation

    result = final_chain.invoke(WorkoutGenInput)

    return result

