import { useNavigate } from "react-router-dom"
import { useState } from "react";

function WorkoutPlanCard({ workoutplan, onDelete }) {

    const navigate = useNavigate();

    const [deleteModalOpen, setDeleteModalOpen] = useState(false);


    function viewWorkoutPlan() {
        navigate(`/workoutplan/${workoutplan.id}`)
    }

    function handleDelete(e) {
        e.stopPropagation(); // Prevent triggering card clicks if you add that later
        if (onDelete) {
            onDelete(workoutplan.id);
        }
        closeDeleteModal();
    }


    const openDeleteModal = () => {
        setDeleteModalOpen(true);
    }


    const closeDeleteModal = () => {
        setDeleteModalOpen(false);
    }

    return <>

        {/* Delete workout plan modal  */}
        {deleteModalOpen && (
            <div className="fixed inset-0 flex items-center justify-center bg-[rgba(0,0,0,0.5)] z-50">
                <div className="bg-white p-8 rounded shadow-lg w-120 max-w-2xl max-h-[80vh] overflow-y-auto">
                    <h2 className="text-2xl font-bold mb-6">Are you sure you want to delete this workout plan?</h2>
                    <p className="text-gray-500 text-base mb-8">
                        All the workout plan sessions, exercises and community ratings will be removed.
                    </p>
                    <div className='flex justify-between w-full'>

                        <button
                            onClick={handleDelete}
                            className="px-6 py-2 bg-green-700 hover:bg-green-600 text-white rounded cursor-pointer mt-6"
                        >
                            Yes
                        </button>


                        <button
                            onClick={closeDeleteModal}
                            className="px-6 py-2 bg-red-700 hover:bg-red-600 text-white rounded cursor-pointer mt-6"
                        >
                            No
                        </button>

                    </div>
                </div>
            </div>
        )}


        <div className="flex justify-center items-center mt-15">
            <div className="relative flex flex-col justify-between shadow-lg px-10 py-8 border w-96 h-full rounded border-[#009951]">


                <button
                    onClick={openDeleteModal}
                    className="absolute top-2.5 right-3.5 text-red-500 hover:bg-red-600 hover:text-white text-xl font-bold border px-2 rounded cursor-pointer"
                >
                    <i className="pi pi-times text-sm flex justify-center"></i>
                </button>


                <h2 className="text-xl font-bold min-h-[3.5rem] pb-6">{workoutplan.plan_name}</h2>
                <div className="mb-5">
                    <p className="block text-gray-700"><b>Number of sessions:</b> {workoutplan.no_of_sessions}</p>
                </div>
                <div className="mb-5">
                    <p className="block text-gray-700"><b>Average session length:</b> {workoutplan.average_session_length} minutes</p>
                </div>
                <div className="mb-5">
                    <p className="block text-gray-700"><b>Equipment requirements:</b> {workoutplan.equipment_requirements}</p>
                </div>
                <div className="mb-5">
                    <p className="block text-gray-700"><b>Recommended experience level:</b> {workoutplan.experience_level}</p>
                </div>
                <div className="mb-1">
                    <button onClick={viewWorkoutPlan} className="w-full bg-black text-white py-2 rounded cursor-pointer">View Workout Plan</button>
                </div>
            </div>
        </div>
    </>


}

export default WorkoutPlanCard