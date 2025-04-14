function WorkoutPlanCard({workoutplan}) {

    function viewWorkoutPlan() {
        alert("clicked.")
    }

    return <div className="workout-plan-card">
        <div className="work-plan-info">
            <h3>Name: {workoutplan.plan_name}</h3>
            <p>Number of sessions: {workoutplan.no_of_sessions}</p>
            <p>Equipment requirements: {workoutplan.equipment_requirements}</p>
        </div>
        <div className="workout-plan-view-button">
            <button className="view-button" onClick={viewWorkoutPlan}>
                View
            </button>
        </div>
    </div>

}

export default WorkoutPlanCard