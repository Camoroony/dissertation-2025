import React, { useState } from 'react'
import ChatbotIcon from './ChatbotIcon'
import ChatbotForm from './ChatbotForm'
import ChatbotMessage from './ChatbotMessage'
import '../../css/Chatbot.css'

const ChatbotPopup = () => {

    const [showChatbotPopup, setShowChatbotPopup] = useState(false);

    const generateChatResponse = async (history) => {

        history.map(({role, text}) => ({role, parts: [{text}]}))

        console.log(history)

    }

    const [chatHistory, setChatHistory] = useState([]);

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
                        <ChatbotIcon type={'response'}/>
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
                    <ChatbotForm chatHistory={chatHistory} setChatHistory={setChatHistory} generateChatResponse={generateChatResponse} />
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