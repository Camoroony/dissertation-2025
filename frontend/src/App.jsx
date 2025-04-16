import { Routes } from 'react-router-dom';
import { Route } from 'react-router-dom';
import './css/App.css';

import PublicOnlyRoute from './components/routing/PublicOnlyRoute';
import PrivateRoute from './components/routing/PrivateRoute';

import HomePage from './pages/HomePage';
import CreateWorkoutPage from './pages/CreateWorkoutPage';
import MyWorkoutsPage from './pages/MyWorkoutsPage';
import ChatbotPage from './pages/ChatbotPage';
import LoginPage from './pages/LoginPage';
import ManageAccountPage from './pages/ManageAccountPage';
import CreateAccountPage from './pages/CreateAccountPage';
import ReferencesPage from './pages/ReferencesPage';
import CommunityPage from './pages/CommunityPage';


import NavBar from './components/ui/NavBar';


function App() {

  return (
    <div>
      <NavBar />
      <main className="main-content">
        <Routes>

          {/* Private Routes */}
          <Route path="/createworkout" element={<PrivateRoute element={CreateWorkoutPage} />}/>
          <Route path="/home" element={<PrivateRoute element={HomePage} />}/>
          <Route path="/myworkouts" element={<PrivateRoute element={MyWorkoutsPage} />}/>
          <Route path="/chatbot" element={<PrivateRoute element={ChatbotPage} />}/>
          <Route path="/manageaccount" element={<PrivateRoute element={ManageAccountPage} />}/>
          <Route path="/references" element={<PrivateRoute element={ReferencesPage} />}/>
          <Route path="/community" element={<PrivateRoute element={CommunityPage} />}/>

           {/* Public Only Routes  */}
          <Route path="/login" element={<PublicOnlyRoute element={LoginPage} />}/>
          <Route path="/createaccount" element={<PublicOnlyRoute element={CreateAccountPage} />}/>

        </Routes>
      </main>
    </div>
  );
}


export default App
