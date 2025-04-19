import React, { use } from 'react';
import { useState, useEffect } from 'react';
import ExerciseOverviewModal from './ExerciseOverviewModal';
import { getWorkoutPlanSources } from '../../services/workoutplanapi';

const WorkoutPlanDetails = ({ workoutPlan }) => {

    const [errorMessage, setErrorMessage] = useState('');

    const [exerciseModalOpen, setExerciseModalOpen] = useState(false);
    const [sourcesUsedModalOpen, setSourcesUsedModalOpen] = useState(false);

    const [exerciseId, setExerciseId] = useState(null);
    const [modalContent, setModalContent] = useState('');
    const [sources, setSources] = useState('');

    useEffect(() => {
        const retrieveWorkoutPlanSources = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await getWorkoutPlanSources(workoutPlan.id, token);
                console.log(response)
                if (response.status == 200) {
                    setSources(response.data);
                }
            } catch (err) {
                if (err.message) {
                    setErrorMessage(`Error occured loading workout plan sources: ${err.message}`);
                    setTimeout(() => setErrorMessage(''), 4000);
                } else {
                    setErrorMessage('An unknown error occured when loading in your workout plan sources.');
                    setTimeout(() => setErrorMessage(''), 4000);
                }
            }
        }
        retrieveWorkoutPlanSources()
    }, [workoutPlan])

    const openExerciseModal = async (id) => {
        setExerciseId(id);
        setExerciseModalOpen(true);
    };

    const closeModal = (abortController) => {
        if (abortController) {
            abortController.abort();
        }
        setExerciseModalOpen(false);
        setModalContent('');
    };

    const openSourcesUsedModal = () => {
        setSourcesUsedModalOpen(true);
    }

    const closeSourcesUsedModal = () => {
        setSourcesUsedModalOpen(false);
    }

    if (!workoutPlan) return <p>No workout plan data available.</p>;

    return (
        <div className="p-6">

            {exerciseModalOpen && (
                <ExerciseOverviewModal
                    id={exerciseId}
                    closeModalMethod={closeModal}
                    modalContent={modalContent}
                    setModalContent={setModalContent}
                ></ExerciseOverviewModal>
            )}

            {/* Sources Used modal */}
            {sourcesUsedModalOpen && (
                errorMessage ? (<div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-7 py-5 rounded shadow-lg">
                    {errorMessage} </div>) : (<div className="fixed inset-0 flex items-center justify-center bg-[rgba(0,0,0,0.5)] z-50">
                        <div className="bg-white p-8 rounded shadow-lg w-11/12 max-w-2xl max-h-[80vh] overflow-y-auto">
                            <h2 className="text-2xl font-bold mb-4">Sources Used</h2>
                            <p className="text-gray-500 text-base italic mb-8">
                                These are the sources that were analysed during the creation of this AI generated workout plan. Only these sources were used for information when creating this plan.
                            </p>
                            {sources.length > 0 ? (
                                <ul className="list-disc list-inside space-y-2 text-gray-700 mb-10">
                                    {sources.map((ref, index) => (
                                        <li className="mb-5" key={index}>{ref}</li>
                                    ))}
                                </ul>
                            ) : (
                                <p>No references available.</p>
                            )}

                            <div className="flex justify-end mt-6">
                                <button
                                    onClick={closeSourcesUsedModal}
                                    className="px-4 py-2 bg-[#D732A8] hover:bg-[#B0278B] text-white rounded"
                                >
                                    Close
                                </button>
                            </div>
                        </div>
                    </div>)

            )
            }


            <div className="mb-8 flex flex-col items-center text-center">
                <h1 className="text-3xl font-bold mb-10">{workoutPlan.plan_name}</h1>
                <div className="flex gap-20 mb-5">
                    <p className='text-lg border rounded p-2 shadow-md'>Sessions:  <span className=' text-green-600 font-bold underline'>{workoutPlan.no_of_sessions}</span></p>
                    <p className='text-lg border rounded p-2 shadow-md'>Average Session Length: <span className='text-green-600 font-bold underline'>{workoutPlan.average_session_length} minutes</span></p>
                    <button
                        onClick={openSourcesUsedModal}
                        className="px-4 py-2 bg-[#D732A8] hover:bg-[#B0278B] text-white rounded shadow-md cursor-pointer"
                    >
                        Sources Used
                    </button>
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
                                                onClick={() => openExerciseModal(exercise.id)}>
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
