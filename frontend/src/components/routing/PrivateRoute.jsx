import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { verifyToken } from '../../services/accountapi';

function PrivateRoute({ element: Component }) {
  const [isLoading, setIsLoading] = useState(true);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const checkAuth = async () => {
      const token = localStorage.getItem('token');
      if (!token) {
        navigate('/login');
        return;
      }

      try {
        await verifyToken(token);
        setIsAuthenticated(true);
      } catch (err) {
        console.error('Token verification failed:', err);
        navigate('/login');
      } finally {
        setIsLoading(false);
      }
    };

    checkAuth();
  }, [navigate]);

  if (isLoading) return <p>Loading...</p>;

  return isAuthenticated ? <Component /> : null;
}

export default PrivateRoute;