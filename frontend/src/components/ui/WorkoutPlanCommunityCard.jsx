import { useNavigate } from "react-router-dom"
import { useState } from "react";
import { useLocation } from "react-router-dom";
import CommunityRating from "./CommunityRating";
import { createRating } from "../../services/ratingapi";

function WorkoutPlanCommunityCard({ workoutplan }) {

    const [values, setValues] = useState({
        rating: '',
        comment: '',
        workout_plan_id: '',

    })

    const navigate = useNavigate();
    const location = useLocation();

    const [ratings, setRatings] = useState(workoutplan.ratings);
    const [successMsg, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const [sentiment, setSentiment] = useState(true);
    const [rating, setRating] = useState("");


    function viewWorkoutPlan() {
        navigate(`/workoutplan/${workoutplan.id}`, {
            state: { previousPage: location.pathname }

        });
    }

    const handleReviewSubmit = async () => {
        if (rating.trim()) {

            try {

                const ratinginput = {
                    rating: sentiment,
                    comment: rating,
                    workout_plan_id: workoutplan.id
                }

                const token = localStorage.getItem('token');
                const response = await createRating(ratinginput, token);
                console.log(response);
                if (response.status === 201) {
                    setRatings([...ratings, response.data]);
                    setRating("");
                    setSuccessMessage("Your review was successfully added to the workout plan!");
                    setTimeout(() => setSuccessMessage(''), 4000);
                }
            } catch (err) {
                setLoading(false);
                console.log(err);
                if (err.message) {
                    setErrorMessage(`Error occurred when creating workout plan: ${err.message}` || 'An error occurred, please try again.');
                } else {
                    setErrorMessage('An unknown error occurred, please try again.');
                }
                setTimeout(() => setErrorMessage(''), 4000);
            }
        }
    }

    return (<>


        <div className="relative">
            {successMsg && (
                <div className="absolute top-11 left-1/2 w-100 transform -translate-x-1/2 bg-green-100 border border-green-400 text-green-700 px-2 py-2 rounded shadow-lg transition-opacity duration-300">
                    {successMsg}
                </div>
            )}
        </div>

        <div className="relative">
            {errorMessage && (
                <div className="absolute top-1 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded shadow-lg transition-opacity duration-300">
                    {errorMessage}
                </div>
            )}
        </div>


        <div className="flex justify-center items-center mt-15">
            <div className="flex flex-col justify-between shadow-lg px-8 py-5 border w-150 h-full rounded border-[#009951]">
                <h2 className="text-xl font-bold min-h-[3.5rem] pb-6">{workoutplan.plan_name}</h2>
                <div className="mb-5">
                    <p className="block text-gray-600 "><b>Recommended experience level:</b> {workoutplan.experience_level}</p>
                </div>
                <div className="mb-5">
                    <p className="block text-gray-600 "><b>Required equipment:</b> {workoutplan.equipment_requirements}</p>
                </div>
                <div className="mb-5">
                    {workoutplan.additional_info && (<p className="block text-gray-600 "><b>Additional info:</b> {workoutplan.additional_info}</p>)}
                </div>
                <div className="inline-block max-w-full mb-3 px-4 py-3 bg-white border border-gray-300 rounded-lg shadow-sm">
                    <div className="flex items-center space-x-6">
                        <div className="text-green-700 font-semibold">
                            <span className="block text-sm"><i className="pi pi-thumbs-up-fill"/> Upvotes:</span>
                            <span className="text-lg">{workoutplan.total_upvotes}</span>
                        </div>
                        <div className="text-red-700 font-semibold">
                            <span className="block text-sm"><i className="pi pi-thumbs-down-fill"/> Downvotes:</span>
                            <span className="text-lg">{workoutplan.total_downvotes}</span>
                        </div>
                        <div className="text-black font-semibold">
                            <span className="block text-sm"> Recommendation rate:</span>
                            <span
                                className={`text-lg font-semibold ${workoutplan.total_upvotes == 0 && workoutplan.total_downvotes == 0 ? 'text-black'
                                    : workoutplan.recommendation_percentage < 50
                                        ? 'text-red-600'
                                        : workoutplan.recommendation_percentage < 70
                                            ? 'text-orange-500'
                                            : 'text-green-600'
                                    }`}
                            >{workoutplan.total_upvotes == 0 && workoutplan.total_downvotes == 0
                                ? 'No reviews'
                                : `${workoutplan.recommendation_percentage}%`}</span>
                        </div>
                    </div>
                </div>

                <div className="mb-5">
                    <button onClick={viewWorkoutPlan} className="bg-black text-white py-2 px-4 rounded cursor-pointer">View Workout Plan</button>
                </div>
                {ratings.length > 0 && (
                    <div className="mb-5">
                        <h3 className="font-semibold text-sm mb-2">Reviews:</h3>
                        <ul className="list-disc list-inside text-sm text-gray-800">
                            {ratings.map((r, index) => (
                                <CommunityRating index={index} rating={r} />
                            ))}
                        </ul>
                    </div>
                )}
                <div className="mb-5">
                    <div className="flex gap-2 mb-2">
                        <button
                            onClick={() => setSentiment(true)}
                            className={`px-3 py-1 rounded text-sm ${sentiment === true
                                ? "bg-green-600 text-white"
                                : "bg-gray-200 text-gray-700 cursor-pointer"
                                }`}
                        >
                            <i className="pi pi-check text-md"></i>
                        </button>
                        <button
                            onClick={() => setSentiment(false)}
                            className={`px-3 py-1 rounded text-sm ${sentiment === false
                                ? "bg-red-600 text-white"
                                : "bg-gray-200 text-gray-700 cursor-pointer"
                                }`}
                        >
                            <i className="pi pi-times text-md"></i>
                        </button>
                    </div>
                    <textarea
                        maxLength={250}
                        className="w-full border rounded p-2 text-sm"
                        rows="2"
                        placeholder="Leave a review..."
                        value={rating}
                        onChange={(e) => setRating(e.target.value)}
                    />
                    <button
                        onClick={handleReviewSubmit}
                        disabled={!rating.trim()}
                        className="mt-2 bg-[#009951] hover:bg-[#007a40] text-white px-3 py-1 rounded text-sm transition-colors duration-200 cursor-pointer"
                    >
                        Submit Review
                    </button>
                </div>

            </div>
        </div>
    </>
    );
}

export default WorkoutPlanCommunityCard