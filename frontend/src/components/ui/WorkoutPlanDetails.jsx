import React from 'react';

const WorkoutPlanDetails = ({ workoutPlan }) => {

    const getExerciseOverview = () => {
        alert("clicked.")
    }

    const getSessionOverview = () => {
        alert("clicked.")
    }

    if (!workoutPlan) return <p>No workout plan data available.</p>;

    return (
        <div className="p-6">
            <div className="mb-8 flex flex-col items-center text-center">
                <h1 className="text-3xl font-bold mb-10">{workoutPlan.plan_name}</h1>
                <div className="flex gap-20 mb-5">
                    <p className='text-lg border rounded p-2 shadow-md'>Sessions:  <span className=' text-green-600 font-bold underline'>{workoutPlan.no_of_sessions}</span></p>
                    <p className='text-lg border rounded p-2 shadow-md'>Average Session Length: <span className='text-green-600 font-bold underline'>{workoutPlan.average_session_length} minutes</span></p>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {workoutPlan.workout_sessions.map((session) => (
                    <div key={session.id} className="border rounded-xl p-4 shadow-md">
                        <div className="flex justify-between items-center mb-2">
                            <h2 className="text-xl font-bold mb-2 p-3">{session.session_name}</h2>
                            <p className="text-gray-600 mb-2 p-3">
                                Day: <b>{session.day_of_week}</b> | Length: <b>{session.length_of_session} mins</b>
                            </p>
                            <p className="text-gray-600 mb-2 p-3">
                                Equipment: <b>{session.equipment_requirements || 'None'}</b>
                            </p>

                            <button className="ml-4 px-2 py-3 pi pi-question-circle text-3xl text-[#009951] hover:text-[#1FA562] cursor-pointer"
                                onClick={getSessionOverview}>
                            </button>
                        </div>

            <div className="space-y-3">
              {session.exercises.map((exercise) => (
                  <>
                      <div key={exercise.id} className="p-3 border rounded bg-gray-50 flex justify-between items-center">
                          <div>
                              <h3 className="font-semibold">{exercise.exercise_name}</h3>
                              <p>Sets: {exercise.sets}</p>
                              <p>Rep goal: {exercise.reps}</p>
                              <p>RIR (Reps in Reserve): {exercise.reps_in_reserve}</p>
                          </div>

                          <div>
                              <button className="ml-4 px-2 py-1 pi pi-question-circle text-2xl text-[#D732A8] hover:text-[#C70039] cursor-pointer" 
                              onClick={getExerciseOverview}>
                              </button>
                          </div>
                      </div>
                  </>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default WorkoutPlanDetails;
