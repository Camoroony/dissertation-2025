import { Routes, Route, Navigate } from 'react-router-dom';
import { useAuth } from './context/AuthContext';

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
import WorkoutPlanPage from './pages/WorkoutPlanPage';


import NavBar from './components/ui/NavBar';


function App() {

  const { isAuthenticated } = useAuth(); 

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

          <Route path="/workoutplan/:id" element={<PrivateRoute><WorkoutPlanPage/></PrivateRoute>}/>

          {/* Public Only Routes  */}
          <Route path="/login" element={<PublicOnlyRoute><LoginPage/></PublicOnlyRoute>}/>
          <Route path="/createaccount" element={<PublicOnlyRoute><CreateAccountPage/></PublicOnlyRoute>}/>

          <Route
            path="*"
            element={
              isAuthenticated
                ? <Navigate to="/createworkout" replace />
                : <Navigate to="/login" replace />
            }
          />

        </Routes>
      </main>
    </div>
  );
}


export default App
