import React from 'react'

const ChatbotTemplateMessage = ({ chat_type }) => {

    const getChatType = () => {
        console.log(chat_type);
    };

    getChatType();


    return (
        <p className="message-text">
            {chat_type === "General" ?
                "Hi! I'm the General Chatbot. I'm here to answer your questions about weightlifting and hypertrophy training!" :
                chat_type === "Community" ?
                    "Hi! I'm the Community Chatbot. I can help you with anything related to the community page like posts or recommendations!" :
                    "Hi! I'm the Workout Plan Chatbot. I'm here to answer any questions you have about your personalised workout plan."}
        </p>
    )
}

export default ChatbotTemplateMessage