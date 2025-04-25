import { useNavigate } from "react-router-dom"
import { useState } from "react";
import CommunityRating from "./CommunityRating";

function WorkoutPlanCommunityCard({workoutplan}) {

    const navigate = useNavigate();

    const [rating, setRating] = useState("");
    const [ratings, setRatings] = useState(workoutplan.ratings);


    function viewWorkoutPlan() {
        navigate(`/workoutplan/${workoutplan.id}`)
    }

    function handleReviewSubmit() {
        if (rating.trim()) {
            setRatings([...ratings, rating.trim()]);
            setRating("");
        }
    }

    return (
        <div className="flex justify-center items-center mt-15">
            <div className="flex flex-col justify-between shadow-lg px-8 py-5 border w-150 h-full rounded border-[#009951]">
                <h2 className="text-xl font-bold min-h-[3.5rem] pb-6">{workoutplan.plan_name}</h2>
                <div className="mb-5">
                    <p className="block text-gray-700 italic break-words"><b>Summary</b></p>
                </div>
                <div className="mb-5">
                    <p className="block text-green-600 "><b>Upvotes: {workoutplan.total_upvotes}</b></p>
                </div>
                <div className="mb-5">
                    <p className="block text-red-600"><b>Downvotes: {workoutplan.total_downvotes}</b></p>
                </div>
                <div className="mb-5">
                    <p className="block text-gray-700"><b>Recommendation Percentage:</b> {workoutplan.recommendation_percentage}%</p>
                </div>
                <div className="mb-5">
                    <button onClick={viewWorkoutPlan} className="bg-black text-white py-2 px-4 rounded cursor-pointer">View Workout Plan</button>
                </div>
                {ratings.length > 0 && (
                    <div className="mb-5">
                        <h3 className="font-semibold text-sm mb-2">Reviews:</h3>
                        <ul className="list-disc list-inside text-sm text-gray-800">
                            {ratings.map((r, index) => (
                                <CommunityRating index={index} rating={r}/>
                            ))}
                        </ul>
                    </div>
                )}
                <div className="mb-5">
                    <textarea
                        className="w-full border rounded p-2 text-sm"
                        rows="2"
                        placeholder="Leave a review..."
                        value={rating}
                        onChange={(e) => setRating(e.target.value)}
                    />
                    <button
                        onClick={handleReviewSubmit}
                        className="mt-2 bg-[#009951] text-white px-3 py-1 rounded text-sm"
                    >
                        Submit Comment
                    </button>
                </div>
                
            </div>
        </div>
    );

}

export default WorkoutPlanCommunityCard