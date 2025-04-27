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
          throw new Error(error.response.data.detail || 'An error occurred while creating the account');
        } else {
          console.error('Network or server error:', error.message);
          throw new Error('Network or server error');
        }
      }
}

export const loginToAccount = async (userinput) => {
  try {
      const response = await axios.post(`${base_url}/login-user`, {
        username: userinput.username,
        plain_password: userinput.plain_password,
      });
  
      console.log('User logged in, JWT token retrieved:', response.data);
      return response;
    } catch (error) {
      if (error.response) {
        console.error('Error:', error.response.data.detail);
        throw new Error(error.response.data.detail || 'An unknown error occurred when attempting to log in');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}

export const updateAccount = async (userupdateinput) => {
  try {

    const data = { ...userupdateinput };

    const response = await axios.post(`${base_url}/update-user`, data, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('User updated:', response.data);
    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An unknown error occurred while updating the account');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}

export const verifyToken = async (token) => {
  try {
      const response = await axios.get(`${base_url}/verify-token`, {
        headers: {
          "Authorization": `Bearer ${token}`
        }
      });

      console.log('User verified:', response.data);
      return response;
    } catch (error) {
        console.error('Error:', error.response.data.detail);
        throw new Error(error.response.data.detail || 'An unknown error occurred when verifiying the user JWT token');
      }
    }