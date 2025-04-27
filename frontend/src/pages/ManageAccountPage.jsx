import { Link, useNavigate } from 'react-router-dom'
import { useState } from 'react'
import { createAccount } from '../services/accountapi'

function ManageAccountPage() {


    const [values, setValues] = useState({
        username: '',
        plain_password: ''
    })

    const [showPassword, setShowPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();

    const handleChanges = (e) => {
        setValues({ ...values, [e.target.name]: e.target.value })
    }

    const handleUpdateSubmit = async (e) => {
        e.preventDefault();
        alert('Account updated.')
        // try {
        //     const response = await createAccount(values);
        //     console.log(response)
        //     if (response.status === 201) {
        //         navigate('/login', {
        //             state: { successMessage: 'Account created successfully! Please log in.' }
        //         });
        //     }
        // } catch (err) {
        //     console.log(err)
        //     if (err.message) {
        //         setErrorMessage(`Error occured when creating account:\n ${err.message}` || 'An error occurred, please try again.')
        //         setTimeout(() => setErrorMessage(''), 4000);
        //     } else {
        //         setErrorMessage('An unknown error occurred, please try again.')
        //         setTimeout(() => setErrorMessage(''), 4000);
        //     }
        // }

    }

    const handleDeleteSubmit = async (e) => {
        e.preventDefault();
        alert('Account deleted.')
        // try {
        //     const response = await createAccount(values);
        //     console.log(response)
        //     if (response.status === 201) {
        //         navigate('/login', {
        //             state: { successMessage: 'Account created successfully! Please log in.' }
        //         });
        //     }
        // } catch (err) {
        //     console.log(err)
        //     if (err.message) {
        //         setErrorMessage(`Error occured when creating account:\n ${err.message}` || 'An error occurred, please try again.')
        //         setTimeout(() => setErrorMessage(''), 4000);
        //     } else {
        //         setErrorMessage('An unknown error occurred, please try again.')
        //         setTimeout(() => setErrorMessage(''), 4000);
        //     }
        // }

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
                <h1 className="text-6xl font-bold mb-15">
                    Update Your <span className="text-[#2A955F]">Account</span></h1>
                <p className="text-lg">Need to make changes to your account information?</p>
                <p className="text-lg">Easily update your details below.</p>
            </div>

            <div className="flex justify-center items-center mt-25">
                <div className="shadow-lg px-8 py-5 border w-150">
                    <h2 className="text-lg font-bold mb-4">Account details</h2>
                    <form>
                        <div className="mb-2">
                            <label htmlFor="new_username" className="block text-gray-700 mb-1">New Username</label>
                            <input type="text" placeholder="Enter your new username..." className="w-full px-3 py-2 border rounded" name='new_username'
                                onChange={handleChanges} />
                        </div>
                        <div className="mb-8">
                            <label htmlFor="confirm_username" className="block text-gray-700 mb-1">Confirm Username</label>
                            <input type="text" placeholder="Confirm your new username..." className="w-full px-3 py-2 border rounded" name='confirm_username'
                                onChange={handleChanges} />
                        </div>

                        <div className="mb-2 relative">
                            <label htmlFor="new_password" className="block text-gray-700 mb-1">
                                New Password
                            </label>
                            <input
                                type={showPassword ? "text" : "password"}
                                placeholder="Enter your new password..."
                                className="w-full px-3 py-2 border rounded pr-10" // pr-10 gives space for button
                                name="new_password"
                                onChange={handleChanges}
                            />
                            <button
                                type="button"
                                className="absolute right-3 top-9.5 text-md text-gray-600"
                                onClick={() => setShowPassword(!showPassword)}
                            >
                                {showPassword ? <i className='pi pi-eye-slash' /> : <i className='pi pi-eye' />}
                            </button>
                        </div>


                        <div className="mb-7 relative">
                            <label htmlFor="confirm_password" className="block text-gray-700 mb-1">
                                Confirm Password
                            </label>
                            <input
                                type={showPassword ? "text" : "password"}
                                placeholder="Confirm your new password..."
                                className="w-full px-3 py-2 border rounded pr-10"
                                name="confirm_password"
                                onChange={handleChanges}
                            />
                            <button
                                type="button"
                                className="absolute right-3 top-9.5 text-md text-gray-600"
                                onClick={() => setShowPassword(!showPassword)}
                            >
                                {showPassword ? <i className='text-l pi pi-eye-slash' /> : <i className='pi pi-eye' />}
                            </button>
                        </div>

                        <div className="mb-7">
                            <label htmlFor="current_password" className="block text-gray-700 mb-1">Current Password</label>
                            <input type="password" placeholder="Confirm your current password..." className="w-full px-3 py-2 border rounded" name='current_password'
                                onChange={handleChanges} />
                            <p className='text-sm'>(Please confirm your account changes by entering your current password.)</p>
                        </div>

                        <div className='flex flex-row w-full'>
                            <div className="mb-5">
                                <button onClick={handleUpdateSubmit} className="bg-black text-white p-2 rounded cursor-pointer">Update Details</button>
                            </div>
                            <div className="mb-5 ml-auto">
                                <button onClick={handleDeleteSubmit} className="bg-red-700 hover:bg-red-600 text-white p-2 rounded cursor-pointer">Delete Account</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </>
    )
}

export default ManageAccountPage
