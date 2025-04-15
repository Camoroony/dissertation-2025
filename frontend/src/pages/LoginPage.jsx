import { Link } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';

function LoginPage() {

    const location = useLocation();
    const [toast, setToast] = useState('');

    useEffect(() => {
        if (location.state?.successMessage) {
            setToast(location.state.successMessage);
            setTimeout(() => setToast(''), 4000);
        }
    }, [location.state]);




    return (
        <>
        <div className="relative">
        {toast && (
         <div className="absolute top-4 left-1/2 transform -translate-x-1/2 bg-green-100 border border-green-400 text-green-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                {toast}
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
                <form>
                    <div className="mb-5">
                        <label htmlFor="username" className="block text-gray-700">Username</label>
                        <input type="text" placeholder="Enter Username" className="w-full px-3 py-2 border rounded"/>
                    </div>
                    <div className="mb-6">
                        <label htmlFor="password" className="block text-gray-700">Password</label>
                        <input type="text" placeholder="Enter Password" className="w-full px-3 py-2 border rounded"/>
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