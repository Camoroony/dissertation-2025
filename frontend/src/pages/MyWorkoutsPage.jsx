import WorkoutPlanCard from "../components/WorkoutPlanCard"

function MyWorkoutsPage() {

    const workoutplans = [
        {id: 1, plan_name: "4-day Upper/Lower Split", no_of_sessions: 4, equipment_requirements: "Dumbbells"},
        {id: 2, plan_name: "5-day UL/PPL Split", no_of_sessions: 5, equipment_requirements: "Full gym access"},
        {id: 3, plan_name: "3-day bodyweight plan", no_of_sessions: 3, equipment_requirements: "Bodyweight exercises"}
    ]

    return <div className="home">
        <div className="workoutplans-grid">
            {workoutplans.map(workoutplan => (
                <WorkoutPlanCard workoutplan={workoutplan} key={workoutplan.id}/>
            ))}
        </div>
    </div>

}

export default MyWorkoutsPage