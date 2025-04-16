import { Link } from 'react-router-dom';
import { useLocation, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import {loginToAccount} from '../services/accountapi'
import { useAuth } from '../context/AuthContext';

function LoginPage() {

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
            const response = await loginToAccount(values)
            console.log(response)
            if(response.status === 201){
                login(response.data.access_token)
                navigate('/createworkout', {
                    state: { successMessage: 'You have successfully logged in!' }
                });
            }
        } catch(err) {
            console.log(err)
            if (err.message) {
                setErrorMessage(`Error occured when creating account: ${err.message}` || 'An error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            } else {
                setErrorMessage('An unknown error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            }
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
        <h1 className="text-6xl font-bold mb-1">Welcome to</h1>
        <h1 className="text-6xl text-[#2A955F] font-bold mb-15">Hypertrophy Education!</h1>
        <p className="text-lg">Login below if you have an account.</p>
        <p className="text-lg">If you don’t, create an account <Link to='/createaccount'className="text-[#1FA562] hover:underline">here!</Link></p>
        </div>
    
    
        <div className="flex justify-center items-center mt-25">
            <div className="shadow-lg px-8 py-5 border w-96">
                <h2 className="text-lg font-bold mb-4">Log In</h2>
                <form onSubmit={handleSubmit}>
                    <div className="mb-5">
                        <label htmlFor="username" className="block text-gray-700">Username</label>
                        <input type="text" placeholder="Enter Username" className="w-full px-3 py-2 border rounded" name='username'
                        onChange={handleChanges}/>
                    </div>
                    <div className="mb-6">
                        <label htmlFor="password" className="block text-gray-700">Password</label>
                        <input type="password" placeholder="Enter Password" className="w-full px-3 py-2 border rounded" name='plain_password'
                        onChange={handleChanges}/>
                    </div>
                    <div className="mb-5">
                    <button className="w-full bg-black text-white py-2 rounded cursor-pointer">Sign In</button>
                    </div>
                </form>
            </div>
        </div>
        </>
        )
}

export default LoginPage