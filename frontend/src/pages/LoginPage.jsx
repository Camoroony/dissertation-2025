function LoginPage() {
    return (
        <>
        <div className="flex flex-col justify-center items-center mt-20">
        <h1 className="text-6xl font-bold mb-1">Welcome to</h1>
        <h1 className="text-6xl text-[#2A955F] font-bold mb-15">Hypertrophy Education!</h1>
        <p className="text-lg">Login below if you have an account.</p>
        <p className="text-lg">If you don’t, create an account <span className="text-[#1FA562]">here!</span></p>
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