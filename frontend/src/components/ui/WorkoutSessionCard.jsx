function WorkoutSessionCard({workoutplan}) {

    function getOverview() {
        alert("Getting overview.")
    }

    return <div className="flex justify-center items-center mt-15">
        <div className="flex flex-col justify-between shadow-lg px-8 py-5 border w-70 h-full gap-10 rounded border-[#009951]">
            <h2 className="text-xl font-bold min-h-[3.5rem]">{workoutplan.plan_name}</h2>
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
                    <button onClick={getOverview} className="w-full bg-black text-white py-2 rounded cursor-pointer">Overview</button>
                </div>
        </div>
    </div>

}

export default WorkoutSessionCard