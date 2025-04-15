import { useEffect } from 'react'
import { verifyToken }  from '../services/accountapi'
import { useNavigate} from 'react-router-dom'

function HomePage() {

    const navigate = useNavigate()

    useEffect(() => {
        const fetchUser = async () => {
            const token = localStorage.getItem('token')

            if (!token) {
                navigate('/login')
                return
            }

            try {
                const response = await verifyToken(token)

                console.log("Token is valid:", response)
            } catch (error) {
                console.error("Token validation failed:", error)
                navigate('/login')
            }
        }

        fetchUser()
    }, [navigate])

    return <>
    <p>Home</p>
    </>
}

export default HomePage