import ReferenceCard from "../components/ui/ReferenceCard";
import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import { getReferences } from "../services/referencesapi";

function ReferencesPage() {

    const [errorMessage, setErrorMessage] = useState('');
    const [references, setReferences] = useState([]);

    useEffect(() => {
            const retrieveReferences = async() => {
                    try {
                        const token = localStorage.getItem('token');
                        const response = await getReferences(token);
                        console.log(response)
                        if (response.status == 200) {
                            setReferences(response.data);
                        }
                    } catch (err) {
                        if (err.message){
                            setErrorMessage(`Error occured loading reference library: ${err.message}`);
                        } else {
                            setErrorMessage('An unknown error occured when loading in the reference library.');
                        }
                    }
            }
            retrieveReferences()
        }, [])

    return <>

        {errorMessage ? (
            <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 bg-red-100 border border-red-400 text-red-700 px-7 py-5 rounded shadow-lg">
                {errorMessage}
            </div>
        ) : (<><div className="flex flex-col justify-center items-center mt-20">
            <h1 className="text-6xl font-bold mb-15">App <span className='text-[#2A955F]'>reference library.</span></h1>
            <p className="text-lg"><b className="underline">All AI content</b> created in this application uses the following sources.</p>
        </div>
            <div className="flex flex-col justify-center items-center mt-20">
                {references.map((reference, index) => (
                    <ReferenceCard key={index} reference={reference}></ReferenceCard>
                ))}
            </div></>)}

    </>
}

export default ReferencesPage