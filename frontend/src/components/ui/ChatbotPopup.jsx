import React, { useEffect, useState } from 'react'
import ChatbotIcon from './ChatbotIcon'
import ChatbotForm from './ChatbotForm'
import ChatbotMessage from './ChatbotMessage'
import '../../css/Chatbot.css'


import { chat } from '../../services/chatbotapi'
import { getUserChatHistory } from '../../services/chatbotapi'

const ChatbotPopup = () => {

    const [showChatbotPopup, setShowChatbotPopup] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');
    const [chatHistory, setChatHistory] = useState([]);
    const [chatHistoryId, setChatHistoryId] = useState(null);

    useEffect(() => {
        const fetchChatHistory = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await getUserChatHistory(token);
                console.log(response)
                if (response.status === 200) {
                    setChatHistoryId(response.data[0]._id);
                    const newHistory = response.data[0].chats.flatMap(chat => [
                        { role: "user", text: chat.user_message },
                        { role: "model", text: chat.ai_message }
                    ]);
                    setChatHistory(newHistory);
                }
            } catch (err) {
                console.log(err)
                if (err.message) {
                    setErrorMessage(`Error occured when retrieving chat history: ${err.message}` || 'An error occurred, please try again.')
                    setTimeout(() => setErrorMessage(''), 4000);
                } else {
                    setErrorMessage('An unknown error occurred, please try again.')
                    setTimeout(() => setErrorMessage(''), 4000);
                }
            }
        };

        fetchChatHistory();
    }, []);

    const generateChatResponse = async (userMessage) => {

        if (!chatHistoryId) { return; }

        try {
            const token = localStorage.getItem('token');
            const response = await chat(userMessage, chatHistoryId, token);
            console.log(response)
            if (response.status === 200) {
                const aiResponse = response.data.ai_response;
                setChatHistory(history => [...history.filter(message => message.text !== "Thinking..."), {role: "model", text: aiResponse}]);
            }
        } catch (err) {
            console.log(err)
            if (err.message) {
                setErrorMessage(`Error occured when generating the a chat message response: ${err.message}` || 'An error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            } else {
                setErrorMessage('An unknown error occurred, please try again.')
                setTimeout(() => setErrorMessage(''), 4000);
            }
        }

        console.log(history)

    }

    return (
        <div>
            {showChatbotPopup ? (
                <div className='chatbot-popup'>
                    <div className='chat-header'>
                        <div className='header-info'>
                            <ChatbotIcon type={'head'} />
                            <h2 className='logo-text'>Chatbot</h2>
                        </div>
                        <button className='pi pi-angle-down' style={{ fontSize: '1rem' }} onClick={() => setShowChatbotPopup(false)}></button>
                    </div>

                    {/* Chat Body */}
                    <div className='chat-body'>
                        <div className='message bot-message'>
                            <ChatbotIcon type={'response'} />
                            <p className="message-text">
                                Hi! <br /> How can I help you today?
                            </p>
                        </div>

                        {chatHistory.map((chat, index) => (
                            <ChatbotMessage key={index} chat={chat} />
                        ))}
                    </div>

                    {/* Chat Footer */}
                    <div className='chat-footer'>
                        <ChatbotForm setChatHistory={setChatHistory} generateChatResponse={generateChatResponse} />
                    </div>
                </div>
            ) : (
                <button id="chatbot-toggler" onClick={() => setShowChatbotPopup(true)}>
                    <ChatbotIcon type={'head'} />
                </button>
            )}
        </div>
    )
}

export default ChatbotPopup