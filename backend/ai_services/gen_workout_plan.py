from langchain.schema.runnable import RunnableParallel, RunnableLambda
from models.input_models import WorkoutGenInput
from ai_services.branches.workout_gen_context.train_availability_branch import get_availability_context
from ai_services.branches.workout_gen_context.build_workout_plan_branch import build_workout_plan
def generate_workout_plan(workout_input: WorkoutGenInput):

    training_availability_lambda = RunnableLambda(
        lambda _: get_availability_context(workout_input.training_availability))

    context_chain = RunnableParallel(
        training_availability_context = training_availability_lambda
    )

    final_generation = RunnableLambda(lambda x: build_workout_plan(workout_input, x))

    final_chain = context_chain | final_generation

    result = final_chain.invoke(WorkoutGenInput)

    return result

