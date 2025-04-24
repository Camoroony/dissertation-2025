import React from 'react'

const ChatbotTemplateMessage = ({ chat_type }) => {

    const getChatType = () => {
        console.log(chat_type);
    };

    getChatType();


    return (
        <p className="message-text">
            {chat_type == "General" ? "Hi!, i'm the general chatbot!"
            : chat_type == "Community" ? "Hi! I'm the community chatbot!"
            : "Hi!, I'm the workout plan chatbot!"}
        </p>
    )
}

export default ChatbotTemplateMessage