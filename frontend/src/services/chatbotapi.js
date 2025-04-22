import axios from 'axios'

const base_url = "http://localhost:8000/chatbot"

// Workout Plan API calls

export const generateChatResponse = async (user_prompt, chat_history_id, token) => {
  try {

    const data = {
      user_prompt: user_prompt,
      chat_history_id: chat_history_id
    };

    const response = await axios.post(`${base_url}/chat`, data, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Chat response generated:', response.data);
    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An error occurred while generating a chat response');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}

export const getUserChatHistory = async (token) => {
  try {

    const response = await axios.get(`${base_url}/get-chat-history`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    console.log('Chat history retrieved:', response.data);
    return response;
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.detail);
      throw new Error(error.response.data.detail || 'An error occurred while retrieving chat history');
    } else {
      console.error('Network or server error:', error.message);
      throw new Error('Network or server error');
    }
  }
}