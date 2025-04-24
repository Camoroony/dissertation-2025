import ChatbotIcon from "./ChatbotIcon"
import ChatbotErrorIcon from "./ChatbotErrorIcon"

const ChatbotMessage = ({ chat }) => {
    return (
        <>
            <div className={`message ${chat.role === "model" ? 'bot' : chat.role === "error" ? 'error' : 'user'}-message`}>
                {chat.role === "model" && <ChatbotIcon />}
                {chat.role === "error" && <ChatbotErrorIcon />}

                {chat.role == "model" ? (<div className="message-content">
                    <p className="message-text">
                        {chat.text}
                    </p>
                    <button className="sources-button"
                        onClick={() => alert('Sources will be displayed here.')}>
                        Sources used
                    </button>

                </div>) : (<p className="message-text">
                    {chat.text}
                </p>)}

            </div>

        </>
    )
}

export default ChatbotMessage