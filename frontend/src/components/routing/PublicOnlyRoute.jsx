// src/components/PublicRoute.jsx
import { Navigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const PublicOnlyRoute = ({ children }) => {
  const { isAuthenticated } = useAuth();

  if (isAuthenticated) {
    return <Navigate to="/createworkout" replace />;
  }

  return children;
};

export default PublicOnlyRoute;