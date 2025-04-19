import { useState } from "react";
import { useEffect } from "react";
import { getExerciseOverview } from "../../services/workoutplanapi";

function ExerciseOverviewModal({ id, closeModalMethod, modalContent, setModalContent }) {

    const [loading, setLoading] = useState(false);
    const [referenceModalOpen, setReferenceModalOpen] = useState(false);
    const [abortController, setAbortController] = useState(null);
    const [references, setReferences] = useState([]);

    useEffect(() => {

        const getExerciseOverviewCall = async (id) => {

            setLoading(true);
            setModalContent('');

            const apiStateController = new AbortController();
            setAbortController(apiStateController);

            try {
                const token = localStorage.getItem('token');
                const response = await getExerciseOverview(id, token, apiStateController.signal);
                if (response.status === 200) {
                    setModalContent(response.data.response.text_tutorial);
                    setReferences(response.data.sources_used || []);
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
        if (id) {
            getExerciseOverviewCall(id);
        }
    }, [])

    const openReferencesModal = () => {
        setReferenceModalOpen(true);
    }

    const closeReferencesModal = () => {
        setReferenceModalOpen(false);
    }

    return <>

        {/* Main Modal */}
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
                    onClick={() => closeModalMethod(abortController)}
                    className="mt-4 px-4 py-2 mr-5 bg-[#009951] hover:bg-[#007A41] text-white rounded"
                >
                    Close
                </button>

                {!loading && (<button
                    onClick={openReferencesModal}
                    className="mt-4 px-4 py-2 bg-[#D732A8] hover:bg-[#B0278B] text-white rounded"
                >
                    References
                </button>)}
            </div>
        </div>

        {/* References Modal */}
        {referenceModalOpen && (
            <div className="fixed inset-0 flex items-center justify-center bg-[rgba(0,0,0,0.5)] z-50">
                <div className="bg-white p-8 rounded shadow-lg w-11/12 max-w-2xl max-h-[80vh] overflow-y-auto">
                    <h2 className="text-2xl font-bold mb-4">References</h2>
                    <p className="text-gray-500 text-base italic mb-8">
                        These are the references that were analysed during the creation of this AI generated output.
                    </p>
                    {references.length > 0 ? (
                        <ul className="list-disc list-inside space-y-2 text-gray-700 mb-10">
                            {references.map((ref, index) => (
                                <li className="mb-5" key={index}>{ref}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>No references available.</p>
                    )}

                    <div className="flex justify-end mt-6">
                        <button
                            onClick={closeReferencesModal}
                            className="px-4 py-2 bg-[#D732A8] hover:bg-[#B0278B] text-white rounded"
                        >
                            Close
                        </button>
                    </div>
                </div>
            </div>
        )
        }
    </>
}

export default ExerciseOverviewModal


