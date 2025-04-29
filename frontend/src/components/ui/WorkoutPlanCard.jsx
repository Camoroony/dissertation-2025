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


        <div className="flex justify-center items-center mt-12">
            <div className="relative flex flex-col gap-4 shadow-xl px-8 py-6 border w-full max-w-md rounded-2xl border-[#009951] bg-white transition-all">

                <button
                    onClick={openDeleteModal}
                    className="absolute top-3 right-3 text-red-500 hover:bg-red-600 hover:text-white p-1.5 rounded-full border border-transparent hover:border-white transition-colors duration-200 cursor-pointer"
                >
                    <i className="pi pi-times text-sm flex justify-center items-center"></i>
                </button>

                <h2 className="text-2xl font-semibold text-gray-900 leading-snug">{workoutplan.plan_name}</h2>

                <div className="space-y-4 text-md text-gray-700">
                    <p><span className="font-semibold">Sessions:</span> {workoutplan.no_of_sessions}</p>
                    <p><span className="font-semibold">Average session length:</span> {workoutplan.average_session_length} minutes</p>
                    <p><span className="font-semibold">Equipment:</span> {workoutplan.equipment_requirements}</p>
                    <p><span className="font-semibold">Experience:</span> {workoutplan.experience_level}</p>
                    {workoutplan.additional_info && (
                        <p><span className="font-semibold">Additional Info:</span> {workoutplan.additional_info}</p>
                    )}
                </div>

                <div className="pt-2">
                    <button
                        onClick={viewWorkoutPlan}
                        className="w-full bg-[#009951] hover:bg-[#007a40] text-white font-medium py-2 rounded-lg transition-colors duration-200 cursor-pointer"
                    >
                        View Workout Plan
                    </button>
                </div>
            </div>
        </div>

    </>


}

export default WorkoutPlanCard