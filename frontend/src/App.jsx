import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import WorkoutPlanCard from './components/WorkoutPlanCard'

function App() {

  return (
   <>
   <WorkoutPlanCard workoutplan={{plan_name: "4-day upper/lower split", no_of_sessions: "4", equipment_requirements: "Dumbbells"}}/>
   </>
  );
}

function Text({display}) {
  return (
  <div>
    <p>{display}</p>
  </div>
  );
}

export default App
