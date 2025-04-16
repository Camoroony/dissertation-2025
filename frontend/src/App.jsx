import { Routes } from 'react-router-dom';
import { Route } from 'react-router-dom';
import './css/App.css';


import PublicOnlyRoute from './components/routing/PublicOnlyRoute';
import PrivateRoute from './components/routing/PrivateRoute';


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
          <Route path="/createworkout" element={<PrivateRoute><CreateWorkoutPage/></PrivateRoute>}/>
          <Route path="/myworkouts" element={<PrivateRoute><MyWorkoutsPage/></PrivateRoute>}/>
          <Route path="/chatbot" element={<PrivateRoute><ChatbotPage/></PrivateRoute>}/>
          <Route path="/manageaccount" element={<PrivateRoute><ManageAccountPage/></PrivateRoute>}/>
          <Route path="/references" element={<PrivateRoute><ReferencesPage/></PrivateRoute>}/>
          <Route path="/community" element={<PrivateRoute><CommunityPage/></PrivateRoute>}/>

           {/* Public Only Routes  */}
          <Route path="/login" element={<PublicOnlyRoute><LoginPage/></PublicOnlyRoute>}/>
          <Route path="/createaccount" element={<PublicOnlyRoute><CreateAccountPage/></PublicOnlyRoute>}/>

          {/* Redirect all other routes */}
          <Route path="*" element={<PublicOnlyRoute><LoginPage /></PublicOnlyRoute>} />

        </Routes>
      </main>
    </div>
  );
}


export default App
