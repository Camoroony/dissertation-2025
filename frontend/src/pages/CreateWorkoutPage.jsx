import { Link } from 'react-router-dom';
import { useLocation, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import {loginToAccount} from '../services/accountapi'
import { useAuth } from '../context/AuthContext';

function CreateWorkoutPage() {

    const { login } = useAuth()

    const [values, setValues] = useState({
        username: '',
        plain_password: ''
    })

    const location = useLocation();
    const [successMsg, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('')
    const navigate = useNavigate()

    const handleChanges = (e) => {
            setValues({...values, [e.target.name]:e.target.value})
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
        // This needs to call the create workout plan API endpoint
        } catch(err) {
        //   This needs to handle the erros fro mthe api endpoint
        }

    }

    useEffect(() => {
        if (location.state?.successMessage) {
            setSuccessMessage(location.state.successMessage);
            setTimeout(() => setSuccessMessage(''), 4000);
        }
    }, [location.state]);




    return (
        <>
        <div className="relative">
        {successMsg && (
         <div className="absolute top-4 left-1/2 transform -translate-x-1/2 bg-green-100 border border-green-400 text-green-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                {successMsg}
        </div>
            )}
        </div>

        <div className="relative">
            {errorMessage && (
                <div className="absolute top-4 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                {errorMessage}
            </div>
            )}
     </div>   


        <div className="flex flex-col justify-center items-center mt-20">
        <h1 className="text-6xl font-bold mb-15">Looking for a <span className='text-[#2A955F]'>new plan?</span></h1>
        <p className="text-lg">Fill out your details below to generate a new workout plan </p>
        <p className="text-lg">with provided explanations and references!</p>
        </div>
    

            <div className="flex justify-center items-center mt-25">
                <div className="shadow-lg px-8 py-5 border w-150">
                    <h2 className="text-lg font-bold mb-4">Create your workout plan</h2>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-5">
                            <label htmlFor="training_experience" className="block text-gray-700 mb-2">Training Experience (Select below)</label>
                            <div className="relative w-full mb-5">
                                <select
                                    name="training_experience"
                                    className="appearance-none w-full px-3 py-2 border rounded pr-10"
                                    onChange={handleChanges}
                                >
                                    <option value="">Select a training experience level</option>
                                    <option value="Beginner (less than 12 months of consistent, proper training experience)">
                                        Beginner (less than 12 months of consistent, proper training experience)
                                    </option>
                                    <option value="Intermediate (1 to 4 years of consistent, proper training experience)">
                                        Intermediate (1 to 4 years of consistent, proper training experience)
                                    </option>
                                    <option value="Advanced (more than 4 years of consistent, proper training experience)">
                                        Advanced (more than 4 years of consistent, proper training experience)
                                    </option>
                                </select>
                                <i className="pi pi-chevron-down absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none"></i>
                            </div>
                        </div>
                        <div className="mb-5">
                            <label htmlFor="training_availability" className="block text-gray-700 mb-2">Training Availability (Select below)</label>
                            <div className="relative w-full mb-5">
                                <select
                                    name="training_availability"
                                    className="appearance-none w-full px-3 py-2 border rounded pr-10"
                                    onChange={handleChanges}
                                >
                                    <option value="">Select a training availability level</option>
                                    <option value="1 day a week">
                                        1 day a week
                                    </option>
                                    <option value="2 days a week">
                                        2 days a week
                                    </option>
                                    <option value="3 days a week">
                                        3 days a week
                                    </option>
                                    <option value="4 days a week">
                                        4 days a week
                                    </option>
                                    <option value="5 days a week">
                                        5 days a week
                                    </option>
                                    <option value="6 days a week">
                                        6 days a week
                                    </option>
                                </select>
                                <i className="pi pi-chevron-down absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none"></i>
                            </div>
                        </div>
                        <div className="mb-5">
                            <label htmlFor="training_focus" className="block text-gray-700 mb-2">Training Focus (Select below)</label>
                            <div className="relative w-full mb-5">
                                <select
                                    name="training_focus"
                                    className="appearance-none w-full px-3 py-2 border rounded pr-10"
                                    onChange={handleChanges}
                                >
                                    <option value="">Select a training focus</option>
                                    <option value="Full-Body">
                                        Full-Body
                                    </option>
                                    <option value="Upper-Body">
                                        Upper-Body
                                    </option>
                                    <option value="Lower-Body">
                                        Lower-Body
                                    </option>
                                    <option value="Arms">
                                        Arms
                                    </option>
                                    <option value="Shoulders">
                                        Shoulders
                                    </option>
                                    <option value="Chest">
                                        Chest
                                    </option>
                                    <option value="Back">
                                        Back
                                    </option>
                                </select>
                                <i className="pi pi-chevron-down absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none"></i>
                            </div>
                        </div>
                        <div className="mb-5">
                            <label htmlFor="available_equipment" className="block text-gray-700 mb-2">Available Equipment (Select below)</label>
                            <div className="relative w-full mb-5">
                                <select
                                    name="available_equipment"
                                    className="appearance-none w-full px-3 py-2 border rounded pr-10"
                                    onChange={handleChanges}
                                >
                                    <option value="">Select your available equipment</option>
                                    <option value="Full gym access">
                                        Full gym access
                                    </option>
                                    <option value="Dumbbells">
                                        Dumbbells only
                                    </option>
                                    <option value="Bodyweight">
                                        Bodyweight only
                                    </option>
                                </select>
                                <i className="pi pi-chevron-down absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none"></i>
                            </div>
                        </div>
                        <div className="mb-6">
                            <label htmlFor="additional_info" className="block text-gray-700 mb-2">Any additional info you would like to mention?</label>
                            <textarea type="text" placeholder="Enter Additional Info" className="w-full px-3 py-2 border rounded h-20 resize-none" name='plain_password'
                                onChange={handleChanges} />
                        </div>
                        <div className="mb-5">
                            <button className="w-full bg-black text-white py-2 rounded cursor-pointer">Generate Plan</button>
                        </div>
                    </form>
                </div>
            </div>
        </>
        )
}

export default CreateWorkoutPage