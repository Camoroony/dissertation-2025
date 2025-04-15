import { Link } from "react-router-dom"

function CreateAccountPage() {
    return (
    <>
    <div className="flex flex-col justify-center items-center mt-20">
    <h1 className="text-6xl font-bold mb-15">Create a <span className="text-[#2A955F]">new account!</span></h1>
    <p className="text-lg">Enter your details below to create an account!</p>
    </div>


    <div className="flex justify-center items-center mt-25">
        <div className="shadow-lg px-8 py-5 border w-96">
            <h2 className="text-lg font-bold mb-4">Create an account</h2>
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
