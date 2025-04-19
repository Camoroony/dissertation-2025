import React, { use } from 'react';
import { useState } from 'react';
import { getExerciseOverview } from '../../services/workoutplanapi';

const WorkoutPlanDetails = ({ workoutPlan }) => {

    const [modalOpen, setModalOpen] = useState(false);
    const [modalContent, setModalContent] = useState('');
    const [loading, setLoading] = useState(false);
    const [abortController, setAbortController] = useState(null);

    const openModal = async (type, id) => {
        setModalOpen(true);
        setLoading(true);
        setModalContent('');

        const apiStateController = new AbortController();
        setAbortController(apiStateController);

        try {
            const token = localStorage.getItem('token');
            let response;
            if (type === 'session') {
                response = await getSessionOverviewById(id, apiStateController.signal);
            } else if (type === 'exercise') {
                response = await getExerciseOverview(id, token, apiStateController.signal);
            }

            if (response.status === 200) {
                setModalContent(response.data.response.text_tutorial);
            } else {
                setModalContent('Failed to load overview.');
            }
        } catch (error) {
            console.error(error);
            setModalContent('An error occurred while fetching the overview.');
        } finally {
            setLoading(false);
        }
    };

    const closeModal = () => {
        if (abortController) {
            abortController.abort();
        }
        setModalOpen(false);
        setModalContent('');
    };

    if (!workoutPlan) return <p>No workout plan data available.</p>;

    return (
        <div className="p-6">

            {modalOpen && (
                <div className="fixed inset-0 flex items-center justify-center bg-[rgba(0,0,0,0.5)] z-50">
                    <div className="bg-white p-8 rounded shadow-lg w-11/12 max-w-4xl max-h-[90vh] overflow-y-auto">
                        <h2 className="text-2xl font-bold mb-4">Overview</h2>

                        {loading ? (
                            <div className="flex flex-col justify-center items-center">
                                <div className="flex flex-row justify-center items-center mb-6">
                                    <i className="pi pi-spinner pi-spin text-4xl mr-5" style={{ color: '#D732A8' }}></i>
                                    <p className="text-gray-500 text-lg">Please wait...</p>
                                </div>
                                <p className="text-gray-500 text-center text-md mb-1">The AI is retreiving information on this exercise</p>
                                <p className="text-gray-500 text-center text-md">This may take a couple of seconds...</p>
                            </div>
                        ) : (
                            <p className="mb-6 whitespace-pre-line">{modalContent}</p>
                        )}

                        <button
                            onClick={closeModal}
                            className="mt-4 px-4 py-2 bg-[#009951] hover:bg-[#1FA562] text-white rounded"
                        >
                            Close
                        </button>
                    </div>
                </div>
            )}


            <div className="mb-8 flex flex-col items-center text-center">
                <h1 className="text-3xl font-bold mb-10">{workoutPlan.plan_name}</h1>
                <div className="flex gap-20 mb-5">
                    <p className='text-lg border rounded p-2 shadow-md'>Sessions:  <span className=' text-green-600 font-bold underline'>{workoutPlan.no_of_sessions}</span></p>
                    <p className='text-lg border rounded p-2 shadow-md'>Average Session Length: <span className='text-green-600 font-bold underline'>{workoutPlan.average_session_length} minutes</span></p>
                </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {workoutPlan.workout_sessions.map((session) => (
                    <div key={session.id} className="border rounded-xl p-4 shadow-md">
                        <div className="flex justify-between items-center mb-2">
                            <h2 className="text-xl font-bold mb-2 p-3">{session.session_name}</h2>
                            <p className="text-gray-600 mb-2 p-3">
                                Day: <b>{session.day_of_week}</b> | Length: <b>{session.length_of_session} mins</b>
                            </p>
                            <p className="text-gray-600 mb-2 p-3">
                                Equipment: <b>{session.equipment_requirements || 'None'}</b>
                            </p>

                            <button className="ml-4 px-2 py-3 pi pi-question-circle text-3xl text-[#009951] hover:text-[#1FA562] cursor-pointer"
                               onClick={() => openModal('session', exercise.id)}>
                            </button>
                        </div>

                        <div className="space-y-3">
                            {session.exercises.map((exercise) => (
                                <>
                                    <div key={exercise.id} className="p-3 border rounded bg-gray-50 flex justify-between items-center">
                                        <div>
                                            <h3 className="font-semibold">{exercise.exercise_name}</h3>
                                            <p>Sets: {exercise.sets}</p>
                                            <p>Rep goal: {exercise.reps}</p>
                                            <p>RIR (Reps in Reserve): {exercise.reps_in_reserve}</p>
                                        </div>

                                        <div>
                                            <button className="ml-4 px-2 py-1 pi pi-question-circle text-2xl text-[#D732A8] hover:text-[#C70039] cursor-pointer"
                                                onClick={() => openModal('exercise', exercise.id)}>
                                            </button>
                                        </div>
                                    </div>
                                </>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default WorkoutPlanDetails;
