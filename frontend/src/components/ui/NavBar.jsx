import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import "../../css/Navbar.css"

function NavBar () {

    const logout = () => {
        localStorage.removeItem('token');
        console.log(`Authenticated : ${isAuthenticated}`)
        window.location.reload();
    }

    const { isAuthenticated } = useAuth(); 

    return <nav className="navbar">
        <div className="navbar-logo">
            <p>Hypertrophy <b>Education</b></p>
        </div>

        {isAuthenticated && (<div className="navbar-links">
            <Link to="/createworkout" className="navbar-link"> Create Workout</Link>
            <Link to="/myworkouts" className="navbar-link"> My Workouts</Link>
            <Link to="/community" className="navbar-link"> Community</Link>
            <Link to="/references" className="navbar-link"> References</Link>
            <Link to="/manageaccount" className="navbar-link"> Account</Link>
            <Link onClick={logout} className="navbar-link">Log out</Link>
        </div>)}
    </nav>
}

export default NavBar