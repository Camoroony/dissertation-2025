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
      throw new Error(error.response.data.detail || 'An error occurred while creating the workout plan');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}

export const getWorkoutPlan = async (id, token) => {

  try {
    const response = await axios.get(`${base_url}/get-workout-plan`, {
      params: { id },
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Workout plan retrieved:', response.data);

    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An error occurred while retrieving the workout plan');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}

export const getWorkoutPlansByUser = async (token) => {

  try {
    const response = await axios.get(`${base_url}/get-workout-plans-by-user`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Workout plans retrieved:', response.data);

    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An error occurred while retrieving the workout plans for the workout plans page');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}