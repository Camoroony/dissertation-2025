import axios from 'axios'

const base_url = "http://localhost:8000/workouts"

// Workout Plan API calls

export const createWorkoutPlan = async (workoutgeninput, token) => {
  try {

    const data = { ...workoutgeninput };

    const response = await axios.post(`${base_url}/create-workout-plan`, data, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Workout plan created:', response.data);
    return response;
  } catch (error) {
    if (error.response) {
      const { status, data } = error.response;
      if (status === 422 && Array.isArray(data.detail)) {
        const messages = data.detail.map(err => {
          return `${err.msg}`;
        }).join(' | ');
        throw new Error(messages);
      }
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

export const deleteWorkoutPlan = async (id, token) => {

  try {
    const response = await axios.delete(`${base_url}/delete-workout-plan`, {
      params: { workout_plan_id: id },
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Workout plan deleted:', response.data);

    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An unknown error occurred while deleting the workout plan');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}



export const getAllWorkoutPlans = async (token) => {

  try {
    const response = await axios.get(`${base_url}/get-workout-plans`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Workout plans retrieved:', response.data);

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

export const exportWorkoutPlanAsCSV = async (id, token) => {

  try {
    const response = await axios.get(`${base_url}/export-workout-plan-csv`, {
      params: { id },
      headers: {
        Authorization: `Bearer ${token}`
      },
      responseType: 'blob',
    });

    const blob = new Blob([response.data], { type: 'text/csv' });

    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;

    link.setAttribute('download', 'workout_plan.csv')

    document.body.appendChild(link)
    link.click();

    link.remove();
    window.URL.revokeObjectURL(url);

    console.log('Workout plan exported:', response.data);

    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An error occurred while exporting the workout plan to a CSV file');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}

export const getWorkoutPlanSources = async (id, token) => {

  try {
    const response = await axios.get(`${base_url}/get-workout-plan-sources`, {
      params: { id },
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Workout plan sources retrieved:', response.data);

    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || `An error occurred while retrieving the workout plans sources for workout plan Id: ${id}`);
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}

export const getSessionOverview = async (id, token, signal) => {

  try {
    const response = await axios.get(`${base_url}/get-workoutsession-info`, {
      params: { id },
      headers: {
        Authorization: `Bearer ${token}`
      },
      signal: signal,
    });

    console.log('Exercise overview retrieved:', response.data);

    return response;
  } catch (error) {
    if (axios.isCancel(error)) {
      console.log('Request was cancelled by the user.')
      return;
    }
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An error occurred while retrieving the exercise overview');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}

export const getExerciseOverview = async (id, token, signal) => {

  try {
    const response = await axios.get(`${base_url}/get-exercise-info`, {
      params: { id },
      headers: {
        Authorization: `Bearer ${token}`
      },
      signal: signal,
    });

    console.log('Exercise overview retrieved:', response.data);

    return response;
  } catch (error) {
    if (axios.isCancel(error)) {
      console.log('Request was cancelled by the user.')
      return;
    }
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An error occurred while retrieving the exercise overview');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}