import React from 'react'

const ChatbotIcon = ({ type }) => {
  return (
    <>{type == 'head' ? (<i className='pi pi-comments'></i>) : (<i className='pi pi-comment'></i>)}</>
 
  )
}

export default ChatbotIcon