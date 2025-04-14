import { Routes } from 'react-router-dom';
import { Route } from 'react-router-dom';
import './css/App.css';

import CreateWorkout from './pages/CreateWorkout';
import MyWorkouts from './pages/MyWorkouts';

import NavBar from './components/Navbar';

function App() {

  return (
    <div>
      <NavBar />
      <main className="main-content">
        <Routes>
          <Route path="/createworkout" element={<CreateWorkout />} />
          <Route path="/myworkouts" element={<MyWorkouts />} />
        </Routes>
      </main>
    </div>
  );
}


export default App
