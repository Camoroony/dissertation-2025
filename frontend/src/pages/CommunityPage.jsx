import WorkoutPlanCommunityCard from "../components/ui/WorkoutPlanCommunityCard";
import { useState, useEffect} from "react";
import { Link } from "react-router-dom";
import { getAllWorkoutPlans } from '../services/workoutplanapi';

function CommunityPage() {

    const [errorMessage, setErrorMessage] = useState('');
    const [workoutPlans, setWorkoutPlans] = useState([]);

    useEffect(() => {
        const retrieveWorkoutPlans = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await getAllWorkoutPlans(token);
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


    return <>

        <div className="flex flex-col justify-center items-center mt-20">
            <h1 className="text-6xl font-bold mb-15">Welcome to the <span className='text-[#2A955F]'>community page!</span></h1>
            <p className="text-lg mb-2">Take a look at all available workout plans by other users!</p>
            <p className="text-lg">There are currently <b>{workoutPlans.length}</b> workout plans available</p>
        </div>

        {workoutPlans.length > 0 ? (<>

            {errorMessage ? (
                <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-7 py-5 rounded shadow-lg">
                    {errorMessage}
                </div>
            ) : (<div>
                <div>
                    <div className="flex flex-col justify-center items-center mt-20">
                        {workoutPlans.map(workoutplan => (
                            <WorkoutPlanCommunityCard workoutplan={workoutplan} key={workoutplan.id} />
                        ))}
                    </div>
                </div>
            </div>)}
        </>) : (

            <div className="flex flex-col justify-center items-center mt-40">
                <p className="text-lg mb-">There are currently <b>0</b> workout plans on the community page.</p>
                <p className="text-lg">Create your first workout plan <Link to='/createworkout' className="text-[#1FA562] hover:underline">here!</Link></p>
            </div>
        )}

    </>
}

export default CommunityPage