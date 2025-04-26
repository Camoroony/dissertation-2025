import axios from 'axios'

const base_url = "http://localhost:8000/ratings"

// Rating API calls

export const createRating = async (ratinginput, token) => {
  try {

    const data = { ...ratinginput };

    const response = await axios.post(`${base_url}/create-rating`, data, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Rating created:', response.data);
    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An error occurred while creating the rating');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}