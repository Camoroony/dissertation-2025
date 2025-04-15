import { Link, useNavigate } from 'react-router-dom'
import {useState} from 'react'
import { createAccount } from '../services/accountapi'

function CreateAccountPage() {
    

    const [values, setValues] = useState({
            username: '',
            plain_password: ''
    })

    const [errorMessage, setErrorMessage] = useState('')
    const navigate = useNavigate()

    const handleChanges = (e) => {
            setValues({...values, [e.target.name]:e.target.value})
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const response = await createAccount(values)
            console.log(response)
            if(response.status === 201){
                navigate('/login', {
                    state: { successMessage: 'Account created successfully! Please log in.' }
                });
            }
        } catch(err) {
            console.log(err)
            if (err.message) {
                setErrorMessage(`Error occured when creating account:\n ${err.message}` || 'An error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            } else {
                setErrorMessage('An unknown error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            }
        }

    }
    
    return (
    <>

     <div className="relative">
            {errorMessage && (
                <div className="absolute top-4 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                {errorMessage}
            </div>
            )}
     </div>

    <div className="flex flex-col justify-center items-center mt-20">
    <h1 className="text-6xl font-bold mb-15">Create a <span className="text-[#2A955F]">new account!</span></h1>
    <p className="text-lg">Enter your details below to create an account!</p>
    </div>

    <div className="flex justify-center items-center mt-25">
        <div className="shadow-lg px-8 py-5 border w-96">
            <h2 className="text-lg font-bold mb-4">Create an account</h2>
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
                <button className="w-full bg-black text-white py-2 rounded cursor-pointer">Create Account</button>
                </div>
            </form>
            <div className="text-center">
                <p>Already have an account?</p>
                <Link to='/login' className='text-[#1FA562] hover:underline'>Login</Link>
            </div>
        </div>
    </div>
    </>
    )
}

export default CreateAccountPage
