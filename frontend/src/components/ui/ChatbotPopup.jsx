import React from 'react'
import ChatbotIcon from './ChatbotIcon'
import '../../css/chatbot.css'

const ChatbotPopup = () => {
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
                    <div className='message user-message'>
                        <p className="message-text">
                         This is the user message hello how are you doing i'm okay thank yhou woooo!
                        </p>
                    </div>
                </div>

                {/* Chat Footer */}
                <div className='chat-footer'>
                    <form action="" className="chat-form">
                        <input type="text" placeholder='Message...' className="message-input" required />
                        <button className='pi pi-angle-up' style={{ fontSize: '1rem' }}></button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default ChatbotPopup