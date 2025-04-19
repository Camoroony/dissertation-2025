import WorkoutPlanCard from "../components/ui/WorkoutPlanCard"
import { getWorkoutPlansByUser } from "../services/workoutplanapi";
import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";

function MyWorkoutsPage() {

    const workoutplans = [
        {id: 1, plan_name: "4-day Upper/Lower Split", no_of_sessions: 4, average_session_length: 60, equipment_requirements: "Dumbbells"},
        {id: 2, plan_name: "5-day UL/PPL Split", no_of_sessions: 5, average_session_length: 60, equipment_requirements: "Full gym access"},
        {id: 3, plan_name: "3-day bodyweight plan", no_of_sessions: 3, average_session_length: 60, equipment_requirements: "Bodyweight exercises"},
        {id: 4, plan_name: "3-day bodyweight plan", no_of_sessions: 3, average_session_length: 60, equipment_requirements: "Bodyweight exercises"},
        {id: 5, plan_name: "3-day bodyweight plan", no_of_sessions: 3, average_session_length: 60, equipment_requirements: "Bodyweight exercises"}
    ]

    const location = useLocation();
    const [errorMessage, setErrorMessage] = useState('');
    const [workoutPlans, setWorkoutPlans] = useState([]);

    useEffect(() => {
            const retrieveWorkoutPlan = async() => {
                    try {
                        const token = localStorage.getItem('token');
                        const response = await getWorkoutPlansByUser(token);
                        console.log(response)
                        if (response.status == 200) {
                            setWorkoutPlans(response.data);
                        }
                    } catch (err) {
                        if (err.message){
                            setErrorMessage(`Error occured loading workout plans: ${err.message}`);
                        } else {
                            setErrorMessage('An unknown error occured when loading in your workout plans.');
                        }
                    }
            }
            retrieveWorkoutPlan()
        }, [])

    return <>

        <div className="flex flex-col justify-center items-center mt-20">
            <h1 className="text-6xl font-bold mb-15">Your <span className='text-[#2A955F]'>workout plans!</span></h1>
            <p className="text-lg">View your personalised workout plans here!</p>
        </div>

        {errorMessage ? (
            <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-7 py-5 rounded shadow-lg">
                {errorMessage}
            </div>
        ) : (<div>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 items-stretch">
                {workoutPlans.map(workoutplan => (
                    <WorkoutPlanCard workoutplan={workoutplan} key={workoutplan.id} />
                ))}
            </div>
        </div>)}
    </>
}

export default MyWorkoutsPage