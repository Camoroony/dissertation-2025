import React, { use } from 'react'
import { useRef } from 'react'
import '../../css/Chatbot.css'

const ChatbotForm = () => {

    const inputRef = useRef();

    const handleChatbotSubmit = (e) => {
        e.preventDefault();
        const userMessage = inputRef.current.value.trim();
        if (!userMessage) return;
        inputRef.current.value = "";

        console.log(userMessage);
    }


    return (
        <form action="" className="chat-form" onSubmit={handleChatbotSubmit}>
            <input ref={inputRef} type="text" placeholder='Message...' className="message-input" required />
            <button className='pi pi-angle-up' style={{ fontSize: '1rem' }}></button>
        </form>
    )
}

export default ChatbotForm