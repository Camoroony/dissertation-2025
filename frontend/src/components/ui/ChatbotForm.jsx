import React from 'react'
import '../../css/Chatbot.css'

const ChatbotForm = () => {
    return (
        <form action="" className="chat-form">
            <input type="text" placeholder='Message...' className="message-input" required />
            <button className='pi pi-angle-up' style={{ fontSize: '1rem' }}></button>
        </form>
    )
}

export default ChatbotForm