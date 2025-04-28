import { useState } from 'react'
import { updateAccount, deleteAccount } from '../services/accountapi'
import { useNavigate } from 'react-router-dom'

function ManageAccountPage() {

    const navigate = useNavigate();

    const [values, setValues] = useState({
        new_username: '',
        confirm_username: '',
        new_password: '',
        confirm_password: '',
        current_password: '',
    })

    const [showPassword, setShowPassword] = useState('');
    const [successMsg, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [deleteModalOpen, setDeleteModalOpen] = useState(false);

    const handleChanges = (e) => {
        setValues({ ...values, [e.target.name]: e.target.value })
    }

    const handleUpdateSubmit = async (e) => {
        e.preventDefault();
        try {
            const token = localStorage.getItem('token');
            const response = await updateAccount(values, token);
            console.log(response)
            if (response.status === 200) {
                setValues({
                    new_username: '',
                    confirm_username: '',
                    new_password: '',
                    confirm_password: '',
                    current_password: '',
                });
                setSuccessMessage('Your account details were updated successfully!');
                setTimeout(() => setSuccessMessage(''), 4000);
            }
        } catch (err) {
            console.log(err)
            if (err.message) {
                setErrorMessage(`Error occured when updating account:\n ${err.message}` || 'An error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            } else {
                setErrorMessage('An unknown error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            }
        }

    }

    const handleDeleteSubmit = async (e) => {
        e.preventDefault();
        try {
            const token = localStorage.getItem('token');
            const response = await deleteAccount(token);
            console.log(response)
            if (response.status === 200) {
                localStorage.removeItem('token');
                window.location.reload();
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

    const openDeleteAccountModal = () => {
        setDeleteModalOpen(true);
    }

    const closeDeleteAccountModal = () => {
        setDeleteModalOpen(false);
    }

    return (
        <>

            <div className="relative">
                {successMsg && (
                    <div className="absolute top-70 left-1/2 transform -translate-x-1/2 bg-green-100 border border-green-400 text-green-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                        {successMsg}
                    </div>
                )}
            </div>

            <div className="relative">
                {errorMessage && (
                    <div className="absolute top-70 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                        {errorMessage}
                    </div>
                )}
            </div>

            {/* Delete account modal  */}
            {deleteModalOpen && (
                <div className="fixed inset-0 flex items-center justify-center bg-[rgba(0,0,0,0.5)] z-50">
                    <div className="bg-white p-8 rounded shadow-lg w-120 max-w-2xl max-h-[80vh] overflow-y-auto">
                        <h2 className="text-2xl font-bold mb-6">Are you sure you want to delete your account?</h2>
                        <p className="text-gray-500 text-base mb-8">
                            All your personal details and workout plans will be deleted.
                        </p>
                        <div className='flex justify-between w-full'>
        
                                <button
                                    onClick={handleDeleteSubmit}
                                    className="px-6 py-2 bg-green-700 hover:bg-green-600 text-white rounded cursor-pointer mt-6"
                                >
                                    Yes
                                </button>
    

                                <button
                                    onClick={closeDeleteAccountModal}
                                    className="px-6 py-2 bg-red-700 hover:bg-red-600 text-white rounded cursor-pointer mt-6"
                                >
                                    No
                                </button>
  
                        </div>
                    </div>
                </div>
            )}

            <div className="flex flex-col justify-center items-center mt-20">
                <h1 className="text-6xl font-bold mb-15">
                    Update Your <span className="text-[#2A955F]">Account</span></h1>
                <p className="text-lg">Need to make changes to your account information?</p>
                <p className="text-lg">Easily update your details below.</p>
            </div>

            <div className="flex justify-center items-center mt-25">
                <div className="shadow-lg px-8 py-5 border w-150">
                    <h2 className="text-lg font-bold mb-4">Account details</h2>
                        <div className="mb-2">
                            <label htmlFor="new_username" className="block text-gray-700 mb-1">New Username</label>
                            <input type="text" placeholder="Enter your new username..." className="w-full px-3 py-2 border rounded" name='new_username'
                                value={values.new_username} onChange={handleChanges} />
                        </div>
                        <div className="mb-8">
                            <label htmlFor="confirm_username" className="block text-gray-700 mb-1">Confirm Username</label>
                            <input type="text" placeholder="Confirm your new username..." className="w-full px-3 py-2 border rounded" name='confirm_username'
                                value={values.confirm_username} onChange={handleChanges} />
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
                                value={values.new_password}
                                onChange={handleChanges}
                            />
                            <button
                                type="button"
                                className="absolute right-3 top-9.5 text-md text-gray-600"
                                onClick={() => setShowPassword(!showPassword)}
                            >
                                {showPassword ? <i className='pi pi-eye' /> : <i className='pi pi-eye-slash' />}
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
                                value={values.confirm_password}
                                onChange={handleChanges}
                            />
                            <button
                                type="button"
                                className="absolute right-3 top-9.5 text-md text-gray-600"
                                onClick={() => setShowPassword(!showPassword)}
                            >
                                {showPassword ? <i className='text-l pi pi-eye' /> : <i className='pi pi-eye-slash' />}
                            </button>
                        </div>

                        <div className="mb-7">
                            <label htmlFor="current_password" className="block text-gray-700 mb-1">Current Password</label>
                            <input type="password" placeholder="Confirm your current password..." className="w-full px-3 py-2 border rounded" name='current_password'
                                value={values.current_password} onChange={handleChanges} />
                            <p className='text-sm'>(Please confirm your account changes by entering your current password.)</p>
                        </div>

                        <div className='flex flex-row w-full'>
                            <div className="mb-5">
                                <button onClick={handleUpdateSubmit} className="bg-black text-white p-2 rounded cursor-pointer">Update Details</button>
                            </div>
                            <div className="mb-5 ml-auto">
                                <button onClick={openDeleteAccountModal} className="bg-red-700 hover:bg-red-600 text-white p-2 rounded cursor-pointer">Delete Account</button>
                            </div>
                        </div>
                </div>
            </div>
        </>
    )
}

export default ManageAccountPage
