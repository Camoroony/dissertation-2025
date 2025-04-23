import ChatbotIcon from "./ChatbotIcon"
import ChatbotErrorIcon from "./ChatbotErrorIcon"

const ChatbotMessage = ({ chat }) => {
    return (
        <div className={`message ${chat.role === "model" ? 'bot': chat.role === "error" ? 'error' : 'user'}-message`}>
            {chat.role === "model" && <ChatbotIcon />}
            {chat.role === "error" && <ChatbotErrorIcon />}
            <p className="message-text">
                {chat.text}
            </p>
        </div>
    )
}

export default ChatbotMessage