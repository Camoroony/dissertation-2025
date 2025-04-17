import { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';


function WorkoutPlanPage() {
    
    const location = useLocation();
    const [successMsg, setSuccessMessage] = useState('');

    useEffect(() => {
        if (location.state?.successMessage) {
            setSuccessMessage(location.state.successMessage);
            setTimeout(() => setSuccessMessage(''), 4000);
        }
    }, [location.state]);


    return <>

        <div className="relative">
            {successMsg && (
                <div className="absolute top-4 left-1/2 transform -translate-x-1/2 bg-green-100 border border-green-400 text-green-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                    {successMsg}
                </div>
            )}
        </div>

        <div>
            <p>This is the page that will display the workout plan!</p>
        </div>
    </>

}

export default WorkoutPlanPage