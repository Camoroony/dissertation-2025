import axios from 'axios'

const base_url = "http://localhost:8000/users"

// Account management API calls

export const createAccount = async (userinput) => {
    try {
        const response = await axios.post(`${base_url}/create-user`, {
          username: userinput.username,
          plain_password: userinput.plain_password,
        });
    
        console.log('User created:', response.data);
        return response;
      } catch (error) {
        if (error.response) {
          console.error('Error:', error.response.data.detail);
        } else {
          console.error('Network or server error:', error.message);
        }
      }
}