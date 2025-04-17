function WorkoutPlanCard({workoutplan}) {

    function viewWorkoutPlan() {
        alert("clicked.")
    }

    return <div className="flex justify-center items-center mt-25">
        <div className="flex flex-col justify-center shadow-lg px-8 py-5 border w-96 h-full rounded border-[#009951]">
            <h2 className="text-xl font-bold mb-6">{workoutplan.plan_name}</h2>
                <div className="mb-5">
                    <p className="block text-gray-700"><b>Number of sessions:</b> {workoutplan.no_of_sessions}</p>
                </div>
                <div className="mb-5">
                    <p className="block text-gray-700"><b>Average session length:</b> {workoutplan.average_session_length} minutes</p>
                </div>
                <div className="mb-5">
                    <p className="block text-gray-700"><b>Equipment requirements:</b> {workoutplan.equipment_requirements}</p>
                </div>
                <div className="mb-1">
                    <button onClick={viewWorkoutPlan} className="w-full bg-black text-white py-2 rounded cursor-pointer">View Workout Plan</button>
                </div>
        </div>
    </div>

}

export default WorkoutPlanCard