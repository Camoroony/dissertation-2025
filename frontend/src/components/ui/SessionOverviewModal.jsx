import { useState } from "react";
import { useEffect } from "react";
import { getSessionOverview } from "../../services/workoutplanapi";

function SessionOverviewModal({ id, closeModalMethod, modalContent, setModalContent }) {

    const [loading, setLoading] = useState(false);
    const [abortController, setAbortController] = useState(null);

    useEffect(() => {

        const getSessionOverviewCall = async (id) => {

            setLoading(true);
            setModalContent('');

            const apiStateController = new AbortController();
            setAbortController(apiStateController);

            try {
                const token = localStorage.getItem('token');
                const response = await getSessionOverview(id, token, apiStateController.signal);
                if (response.status === 200) {
                    setModalContent(response.data);
                } else {
                    setModalContent('Failed to load session overview.');
                }
            } catch (error) {
                console.error(error);
                setModalContent('An error occurred while fetching the session overview.');
            } finally {
                setLoading(false);
            }
        };
        if (id) {
            getSessionOverviewCall(id);
        }
    }, [])


    return <>

        {/* Main Modal */}
        <div className="fixed inset-0 flex items-center justify-center bg-[rgba(0,0,0,0.5)] z-50">
            <div className="bg-white p-8 rounded shadow-lg w-11/12 max-w-4xl max-h-[90vh] overflow-y-auto">
                <h2 className="text-2xl font-bold mb-4">Session Overview</h2>

                {loading ? (
                    <div className="flex flex-col justify-center items-center">
                        <div className="flex flex-row justify-center items-center mb-6">
                            <i className="pi pi-spinner pi-spin text-4xl mr-5" style={{ color: '#D732A8' }}></i>
                            <p className="text-gray-500 text-lg">Please wait...</p>
                        </div>
                        <p className="text-gray-500 text-center text-md mb-1">The AI is retreiving information on this session.</p>
                        <p className="text-gray-500 text-center text-md">This may take a couple of seconds...</p>
                    </div>
                ) : (
                    <p className="mb-6 whitespace-pre-line">{modalContent}</p>
                )}

                <button
                    onClick={() => closeModalMethod(abortController)}
                    className="mt-4 px-4 py-2 mr-5 bg-[#009951] hover:bg-[#007A41] text-white rounded cursor-pointer"
                >
                    Close
                </button>
            </div>
        </div>
    </>
}

export default SessionOverviewModal