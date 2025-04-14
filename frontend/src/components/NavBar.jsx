import { Link } from "react-router-dom";
import "../css/Navbar.css"

function NavBar () {
    return <nav className="navbar">
        <div className="navbar-logo">
            <Link to ="/">Hypertrophy <b>Education</b></Link>
        </div>
        <div className="navbar-links">
            <Link to="/createworkout" className="navbar-link"> Create Workout</Link>
            <Link to="/myworkouts" className="navbar-link"> My Workouts</Link>
            <Link to="/" className="navbar-link"> Chatbot</Link>
            <Link to="/" className="navbar-link"> Community</Link>
            <Link to="/" className="navbar-link"> References</Link>
            <Link to="/" className="navbar-link"> Account</Link>
        </div>
    </nav>
}

export default NavBar