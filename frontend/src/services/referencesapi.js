import axios from 'axios'

const base_url = "http://localhost:8000/references"

// References API calls

export const getReferences = async (token) => {
  try {
      const response = await axios.get(`${base_url}/get-references`, {
        headers: {
          "Authorization": `Bearer ${token}`
        }
      });

      console.log('References retrieved:', response.data);
      return response;
    } catch (error) {
        console.error('Error:', error.response.data.detail);
        throw new Error(error.response.data.detail || 'An unknown error occurred when retrieving the application references');
      }
    }