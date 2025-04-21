import React, { useState } from 'react'
import ChatbotIcon from './ChatbotIcon'
import ChatbotForm from './ChatbotForm'
import ChatbotMessage from './ChatbotMessage'
import '../../css/Chatbot.css'

const ChatbotPopup = () => {

    const generateBotResponse = (history) => {

        console.log(history)

    }

    const [chatHistory, setChatHistory] = useState([]);

    return (
        <div className="container">
            <div className='chatbot-popup'>
                <div className='chat-header'>
                    <div className='header-info'>
                        <ChatbotIcon />
                        <h2 className='logo-text'>Chatbot</h2>
                    </div>
                    <button className='pi pi-angle-down' style={{ fontSize: '1rem' }}></button>
                </div>

                {/* Chat Body */}
                <div className='chat-body'>
                    <div className='message bot-message'>
                        <ChatbotIcon />
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
                    <ChatbotForm chatHistory={chatHistory} setChatHistory={setChatHistory} generateBotResponse={generateBotResponse} />
                </div>
            </div>
        </div>
    )
}

export default ChatbotPopup