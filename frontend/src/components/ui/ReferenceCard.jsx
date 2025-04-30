import { useState } from "react";

const ReferenceCard = ({ reference }) => {
  const [showReferences, setShowReferences] = useState(false);

  return (
    <div className="bg-white border shadow-lg rounded-2xl p-6 mb-6 w-full">
      <h2 className="text-2xl font-bold mb-4">"{reference.title}"</h2>

      <button
        onClick={() => setShowReferences(!showReferences)}
        className="bg-[#D732A8] text-white px-4 py-2 rounded hover:bg-[#B0278B] transition transition cursor-pointer"
      >
        {showReferences ? "Hide Details" : "View Details"}
      </button>

      {showReferences && (
        <div className="mt-4 space-y-2">
                  <p className="text-gray-700"><strong>Author:</strong> {reference.author}</p>
                  <p className="text-gray-700"><strong>Publication Date:</strong> {reference.publication_date}</p>
                  <p className="text-blue-500 underline">
                      <a href={reference.url} target="_blank" rel="noopener noreferrer">
                          View Original Article
                      </a>
                  </p>

                  <div className="mt-4">
                      <h3 className="text-xl font-semibold mb-2">References:</h3>
                      <ul className="list-disc list-inside space-y-1">
                          {reference.references.length > 0 ? (
                              reference.references.map((ref, idx) => (
                                  <li key={idx}>
                                      <span className="text-gray-800 font-medium">{ref.title}</span> –{"  "}
                                      <span className="text-gray-600">{ref.authors} ({ref.year})</span>
                                  </li>
                              ))
                          ) : (
                              <li>
                                  <span className="text-gray-800 font-medium">N/A</span>
                              </li>
                          )}
                      </ul>
                  </div>

                  <div className="mt-4">
                      <h3 className="text-xl font-semibold mb-2">Reviewers:</h3>
                      <ul className="list-disc list-inside space-y-1">
                          {reference.reviewers.length > 0 ? (
                              reference.reviewers.map((rev, idx) => (
                                  <li key={idx}>
                                      <span className="text-gray-800 font-medium">{rev.reviewer}</span> –{"  "}
                                      <span className="text-gray-600">{rev.qualifications}</span>
                                  </li>
                              ))
                          ) : (
                              <li>
                                  <span className="text-gray-800 font-medium">N/A</span>
                              </li>
                          )}
                      </ul>
                  </div>

              </div>
          )}
      </div>
  );
};

export default ReferenceCard;
