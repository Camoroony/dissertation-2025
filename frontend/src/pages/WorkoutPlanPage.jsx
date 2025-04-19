import { useState, useEffect } from 'react';
import { useLocation, useParams } from 'react-router-dom';
import { getWorkoutPlan } from "../services/workoutplanapi.js"
import { Link } from 'react-router-dom';
import WorkoutPlanDetails from '../components/ui/WorkoutPlanDetails.jsx';


function WorkoutPlanPage() {
    
    const location = useLocation();
    const [successMsg, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [workoutPlan, setWorkoutPlan] = useState(null);

    const { id } = useParams()

    useEffect(() => {
        if (location.state?.successMessage) {
            setSuccessMessage(location.state.successMessage);
            setTimeout(() => setSuccessMessage(''), 4000);
        }
    }, [location.state]);


    useEffect(() => {
        const retrieveWorkoutPlan = async() => {
            if (id) {
                try {
                    const token = localStorage.getItem('token');
                    const response = await getWorkoutPlan(parseInt(id, 10), token);
                    console.log(response)
                    if (response.status == 200) {
                        setWorkoutPlan(response.data);
                    }
                } catch (err) {
                    if (err.message){
                        setErrorMessage(`Error occured loading workout plan: ${err.message}`);
                    } else {
                        setErrorMessage('An unknown error occured, please go back to the workout plan page.');
                    }
                }
            }
        }
        retrieveWorkoutPlan()
    }, [id])

    return <>

        <div className="absolute m-4">
            <Link className="flex justify-center items-center hover:text-[#1FA562] gap-2 px-4 py-2 border rounded border-[#009951]" to='/myworkouts'>
                <i className="pi pi-chevron-left"></i>
                <p>Back</p>
            </Link>
        </div>

        <div className="relative">
        {successMsg && (
         <div className="absolute top-4 left-1/2 transform -translate-x-1/2 bg-green-100 border border-green-400 text-green-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                {successMsg}
        </div>
            )}
        </div>

        {errorMessage ? (
            <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-7 py-5 rounded shadow-lg">
                {errorMessage}
            </div>
        ) : (<div>
            <div>
                <WorkoutPlanDetails workoutPlan={workoutPlan}></WorkoutPlanDetails>
            </div>
        </div>)}

    </>

}

export default WorkoutPlanPage