from langchain.schema.runnable import RunnableParallel, RunnableLambda
from models.input_models import WorkoutGenInput
from ai_services.branches.workout_gen_branches.train_availability_branch import get_availability_guidance
from ai_services.branches.workout_gen_branches.build_workout_plan_branch import build_workout_plan

def generate_workout_plan(workout_input: WorkoutGenInput):

    train_availability_lambda = RunnableLambda(
        lambda _: get_availability_guidance(workout_input.training_availability))

    parallel_chain = RunnableParallel(
        training_availability_advice = train_availability_lambda
    )

    final_generation = RunnableLambda(lambda x: build_workout_plan(workout_input, x))

    final_chain = parallel_chain | final_generation

    result = final_chain.invoke(WorkoutGenInput)

    return result

