import WorkoutPlanCard from "../components/ui/WorkoutPlanCard"
import { getWorkoutPlansByUser, deleteWorkoutPlan } from "../services/workoutplanapi";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function MyWorkoutsPage() {

    const [errorMessage, setErrorMessage] = useState('');
    const [successMsg, setSuccessMessage] = useState('');
    const [workoutPlans, setWorkoutPlans] = useState([]);

    useEffect(() => {
        const retrieveWorkoutPlans = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await getWorkoutPlansByUser(token);
                console.log(response)
                if (response.status == 200) {
                    setWorkoutPlans(response.data);
                }
            } catch (err) {
                if (err.message) {
                    setErrorMessage(`Error occured loading workout plans: ${err.message}`);
                } else {
                    setErrorMessage('An unknown error occured when loading in your workout plans.');
                }
            }
        }
        retrieveWorkoutPlans()
    }, [])

    const handleDeleteSubmit = async (workoutplanId) => {
        try {
            const token = localStorage.getItem('token');
            const response = await deleteWorkoutPlan(workoutplanId, token);
            console.log(response)
            if (response.status === 200) {
                setWorkoutPlans(prevPlans => prevPlans.filter(plan => plan.id !== response.data));
                setSuccessMessage('Workout plan has been deleted');
                setTimeout(() => setSuccessMessage(''), 4000);
            }
        } catch (err) {
            console.log(err)
            if (err.message) {
                setErrorMessage(`Error occured when deleting account:\n ${err.message}` || 'An error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            } else {
                setErrorMessage('An unknown error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            }
        }
    }

    return <>
        <div className="flex flex-col justify-center items-center mt-20">
            <h1 className="text-6xl font-bold mb-15">Your <span className='text-[#2A955F]'>workout plans!</span></h1>
            <p className="text-lg">View your personalised workout plans here!</p>
        </div>

        <div className="relative">
            {successMsg && (
                <div className="absolute top-4 left-1/2 transform -translate-x-1/2 bg-green-100 border border-green-400 text-green-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                    {successMsg}
                </div>
            )}
        </div>

        {workoutPlans.length > 0 ? (<>

            {errorMessage ? (
                <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-7 py-5 rounded shadow-lg">
                    {errorMessage}
                </div>
            ) : (<div>
                <div>
                    <div className="grid grid-cols-[repeat(auto-fit,minmax(300px,1fr))] gap-8">
                        {workoutPlans.map(workoutplan => (
                            <WorkoutPlanCard workoutplan={workoutplan} onDelete={(planId) => handleDeleteSubmit(planId)} key={workoutplan.id} />
                        ))}
                    </div>
                </div>
            </div>)}
        </>) : (

            <div className="flex flex-col justify-center items-center mt-40">
                <p className="text-lg mb-">You currently have <b>0 workout plans</b>.</p>
                <p className="text-lg">Create your first workout plan <Link to='/createworkout' className="text-[#1FA562] hover:underline">here!</Link></p>
            </div>
        )}
    </>
}

export default MyWorkoutsPage