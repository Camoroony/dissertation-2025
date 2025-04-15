import { Routes } from 'react-router-dom';
import { Route } from 'react-router-dom';
import './css/App.css';

import HomePage from './pages/HomePage';
import CreateWorkoutPage from './pages/CreateWorkoutPage';
import MyWorkoutsPage from './pages/MyWorkoutsPage';
import ChatbotPage from './pages/ChatbotPage';
import LoginPage from './pages/LoginPage';
import ManageAccountPage from './pages/ManageAccountPage';
import CreateAccountPage from './pages/CreateAccountPage';
import ReferencesPage from './pages/ReferencesPage';
import CommunityPage from './pages/CommunityPage';


import NavBar from './components/Navbar';

function App() {

  return (
    <div>
      <NavBar />
      <main className="main-content">
        <Routes>
          <Route path="/createworkout" element={<CreateWorkoutPage/>}/>
          <Route path="/home" element={<HomePage/>}/>
          {/* {<Route path="/myworkouts" element={<MyWorkoutsPage/>} />} */}
          {/* <Route path="/chatbot" element={<ChatbotPage/>} /> */}
          <Route path="/login" element={<LoginPage/>} />
          {/* <Route path="/manageaccount" element={<ManageAccountPage/>} /> */}
          <Route path="/createaccount" element={<CreateAccountPage/>} />
          {/* <Route path="/references" element={<ReferencesPage/>} />
          <Route path="/community" element={<CommunityPage/>} /> */}
        </Routes>
      </main>
    </div>
  );
}


export default App
