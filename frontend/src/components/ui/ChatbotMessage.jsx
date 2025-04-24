import ChatbotIcon from "./ChatbotIcon"
import ChatbotErrorIcon from "./ChatbotErrorIcon"
import { useState } from "react";
import ReferencesModal from "./ReferencesModal";

const ChatbotMessage = ({ chat }) => {

    const [referenceModalOpen, setReferenceModalOpen] = useState(false);

    const openReferencesModal = () => {
        setReferenceModalOpen(true);
    };

    const closeReferencesModal = () => {
        setReferenceModalOpen(false);
    };



    return (
        <>

        {referenceModalOpen && (
            <ReferencesModal references={chat.sources} closeReferencesModal={closeReferencesModal} />
        )}

            <div className={`message ${(chat.role === "model" || chat.role === "pending") ? 'bot' : chat.role === "error" ? 'error' : 'user'}-message`}>
                {(chat.role === "model" || chat.role === "pending") && <ChatbotIcon />}
                {chat.role === "error" && <ChatbotErrorIcon />}

                {chat.sources ? (<div className="message-content">
                    <p className="message-text">
                        {chat.text}
                    </p>
                    <button className="sources-button"
                        onClick={openReferencesModal}>
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