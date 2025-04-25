import React from 'react'

const CommunityRating = ({ index, rating }) => {
  return (
    <li className="w-full break-words flex items-start gap-2" key={index}>
      <i className='pi pi-check text-green-600 pt-1'></i>
      <span className='p-1'>{rating.comment} <b className='italic'>({rating.user.username})</b></span>
    </li>)

}

export default CommunityRating