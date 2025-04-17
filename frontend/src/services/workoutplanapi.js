import axios from 'axios'

const base_url = "http://localhost:8000/workouts"

// Workout Plan API calls

export const createWorkoutPlan = async (workoutgeninput, token) => {
  try {

    const data = {...workoutgeninput};

    const response = await axios.post(`${base_url}/create-workout-plan`, data, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Workout plan created:', response.data);
    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail.msg || 'An error occurred while creating the workout plan');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}