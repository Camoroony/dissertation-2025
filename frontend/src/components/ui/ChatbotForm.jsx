import React, { use } from 'react'
import { useRef } from 'react'
import '../../css/Chatbot.css'

const ChatbotForm = ({ setChatHistory, generateChatResponse }) => {

    const inputRef = useRef();

    const handleChatbotSubmit = (e) => {
        e.preventDefault();
        const userMessage = inputRef.current.value.trim();
        if (!userMessage) return;
        inputRef.current.value = "";

        console.log(userMessage);

        setChatHistory((history) => [...history, {role: "user", text: userMessage}]);

        setTimeout(() => {

            setChatHistory((history) => [...history, {role: "pending", text: "Thinking..."}]);

            generateChatResponse(userMessage);
        }, 600);
        
    }


    return (
        <form action="" className="chat-form" onSubmit={handleChatbotSubmit}>
            <input ref={inputRef} type="text" placeholder='Message...' className="message-input" required />
            <button className='pi pi-angle-up' style={{ fontSize: '1rem' }}></button>
        </form>
    )
}

export default ChatbotForm