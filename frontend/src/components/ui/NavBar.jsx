import { Link } from "react-router-dom";
import "../../css/Navbar.css"

function NavBar () {
    return <nav className="navbar">
        <div className="navbar-logo">
        <p>Hypertrophy <b>Education</b></p>
        </div>
        
        <div className="navbar-links">
            <Link to="/createworkout" className="navbar-link"> Create Workout</Link>
            <Link to="/myworkouts" className="navbar-link"> My Workouts</Link>
            <Link to="/chatbot" className="navbar-link"> Chatbot</Link>
            <Link to="/community" className="navbar-link"> Community</Link>
            <Link to="/references" className="navbar-link"> References</Link>
            <Link to="/manageaccount" className="navbar-link"> Account</Link>
        </div>
    </nav>
}

export default NavBar