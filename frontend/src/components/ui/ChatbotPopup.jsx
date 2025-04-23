import React, { useEffect, useState, useRef } from 'react'
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
    const [chatbotOptions, setChatbotOptions] = useState([]);
    const [selectedBot, setSelectedBot] = useState(null);

    const chatBodyRef = useRef(null);

    const updateChatbot = async (chatbotId) => {

        const chatbot = chatbotOptions.find(option => option.id == chatbotId);

        setChatHistoryId(chatbot.id);
        const newHistory = chatbot.chats.flatMap(chat => [
            { role: "user", text: chat.user_message },
            { role: "model", text: chat.ai_message }
        ]);
        setChatHistory(newHistory);

        setSelectedBot(chatbot)
    };


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
                setChatHistory((history) => [...history.filter(message => message.text !== "Thinking..."), {role: "error", text: `An error occured when generating the chat response: ${err.message}`}]);
            } else {
                setChatHistory((history) => [...history.filter(message => message.text !== "Thinking..."), {role: "error", text: 'An unknown error occured when generating this response.'}]);
            }
        }

        console.log(history)

    };


    useEffect(() => {
        const fetchChats = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await getUserChatHistory(token);
                console.log(response)
                if (response.status === 200) {

                    const options = response.data.map(bot => ({
                        label: bot.workout_plan_name ? `'${bot.workout_plan_name}' chatbot` : `${bot.chat_type} chatbot`,
                        id: bot._id,
                        chats: bot.chats
                    }));

                    setChatbotOptions(options);
                }
            } catch (err) {
                console.log(err)
                if (err.message) {
                    setErrorMessage(`Error occured when retrieving chat details: ${err.message}` || 'An error occurred, please try again.')
                    setTimeout(() => setErrorMessage(''), 4000);
                } else {
                    setErrorMessage('An unknown error occurred, please try again.')
                    setTimeout(() => setErrorMessage(''), 4000);
                }
            }
        };

        fetchChats();
    }, []);


    useEffect(() => {
        if (chatbotOptions.length > 0 && selectedBot === null) {
            updateChatbot(chatbotOptions[0].id);
        }
    }, [chatbotOptions]); 

    
    useEffect(() => {
        if (chatBodyRef.current) {
            chatBodyRef.current.scrollTop = chatBodyRef.current.scrollHeight;
        }
    }, [chatHistory]);

    return (
        <div>
            {showChatbotPopup ? (
                <div className='chatbot-popup'>
                    <div className='chat-header'>
                        <div className='header-info'>
                            <ChatbotIcon type={'head'} />
                            <div className='relative flex items-center border border-white rounded-md px-2 py-1'>
                                <select
                                    className='chatbot-select bg-transparent text-white appearance-none pr-6'
                                    value={selectedBot.id}
                                    onChange={(e) => updateChatbot(e.target.value)}
                                >
                                    {chatbotOptions.map((bot) => (
                                        <option key={bot.id} value={bot.id}>
                                            {bot.label}
                                        </option>
                                    ))}
                                </select>
                                <i className="pi pi-angle-down" id='chatbot-select-icon'></i>
                            </div>
                        </div>
                        <button className='pi pi-angle-down' style={{ fontSize: '20px' }} onClick={() => setShowChatbotPopup(false)}></button>
                    </div>

                    {/* Chat Body */}
                    <div className='chat-body' ref={chatBodyRef}>
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