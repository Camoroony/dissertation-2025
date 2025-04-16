import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { verifyToken } from '../../services/accountapi';

function PublicOnlyRoute({ element: Component }) {
  const [checked, setChecked] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const checkToken = async () => {
      try {
        const token = localStorage.getItem('token');
        if (token) {
          await verifyToken(token);
          navigate('/createworkout');
          return;
        }
      } catch {
        // Do nothing, show page
      }
      setChecked(true);
    };

    checkToken();
  }, [navigate]);

  return checked ? <Component /> : null;
}

export default PublicOnlyRoute;