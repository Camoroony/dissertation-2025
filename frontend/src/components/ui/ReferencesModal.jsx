import React from 'react'

const ReferencesModal = ({ references, closeReferencesModal }) => {
  return (
      <div className="fixed inset-0 flex items-center justify-center bg-[rgba(0,0,0,0.5)] z-50">
          <div className="bg-white p-8 rounded shadow-lg w-11/12 max-w-2xl max-h-[80vh] overflow-y-auto">
              <h2 className="text-2xl font-bold mb-4">References</h2>
              <p className="text-gray-500 text-base italic mb-8">
                  These are the references that were analysed during the creation of this AI generated output.
              </p>
              {references.length > 0 ? (
                  <ul className="list-disc list-inside space-y-2 text-gray-700 mb-10">
                      {references.map((ref, index) => (
                          <li className="mb-5" key={index}>{ref}</li>
                      ))}
                  </ul>
              ) : (
                  <p>No references available.</p>
              )}

              <div className="flex justify-end mt-6">
                  <button
                      onClick={closeReferencesModal}
                      className="px-4 py-2 bg-[#D732A8] hover:bg-[#B0278B] text-white rounded cursor-pointer"
                  >
                      Close
                  </button>
              </div>
          </div>
      </div>
  )
}

export default ReferencesModal