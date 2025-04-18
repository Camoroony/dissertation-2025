import WorkoutPlanCard from "../components/ui/WorkoutPlanCard"

function MyWorkoutsPage() {

    const workoutplans = [
        {id: 1, plan_name: "4-day Upper/Lower Split", no_of_sessions: 4, average_session_length: 60, equipment_requirements: "Dumbbells"},
        {id: 2, plan_name: "5-day UL/PPL Split", no_of_sessions: 5, average_session_length: 60, equipment_requirements: "Full gym access"},
        {id: 3, plan_name: "3-day bodyweight plan", no_of_sessions: 3, average_session_length: 60, equipment_requirements: "Bodyweight exercises"},
        {id: 4, plan_name: "3-day bodyweight plan", no_of_sessions: 3, average_session_length: 60, equipment_requirements: "Bodyweight exercises"},
        {id: 5, plan_name: "3-day bodyweight plan", no_of_sessions: 3, average_session_length: 60, equipment_requirements: "Bodyweight exercises"}
    ]

    return <>

        <div className="flex flex-col justify-center items-center mt-20">
            <h1 className="text-6xl font-bold mb-15">Your <span className='text-[#2A955F]'>workout plans!</span></h1>
            <p className="text-lg">View your personalised workout plans here!</p>
        </div>


        <div>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 items-stretch">
                {workoutplans.map(workoutplan => (
                    <WorkoutPlanCard workoutplan={workoutplan} key={workoutplan.id} />
                ))}
            </div>
        </div>
    </>
}

export default MyWorkoutsPage