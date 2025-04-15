function CreateAccountPage() {
    return (
    <div className="flex justify-center items-center h-screen">
        <div className="shadow-lg px-8 py-5 border w-96">
            <h2 className="text-lg font-bold mb-4">Create an account</h2>
            <form>
                <div className="mb-4">
                    <label htmlFor="username" className="block text-gray-700">Username</label>
                    <input type="text" placeholder="Enter Username" className="w-full px-3 py-2 border"/>
                </div>
                <div>
                    <label htmlFor="password" className="block text-gray-700">Password</label>
                    <input type="text" placeholder="Enter Password" className="w-full px-3 py-2 border"/>
                </div>
                <button className="w-full bg-green-600 text-white py-2">Create Account</button>
            </form>
            <div className="text-center">
                <p>Already have an account?</p>
                <a href="">Login</a>
            </div>
        </div>
    </div>
    )
}

export default CreateAccountPage
