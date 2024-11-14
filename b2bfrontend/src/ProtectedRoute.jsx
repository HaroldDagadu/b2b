import React, { useEffect, useState, useCallback } from 'react';
import { Navigate } from 'react-router-dom';
import api from './api.jsx';

const ProtectedRoute = ({ element: Element }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);



  const checkAuth = useCallback(async () => {
    try {
      const response = await api.get('accounts/auth/check/');
      setIsAuthenticated(response.data.isAuthenticated);
      if (response.data.isAuthenticated) {
      }
    } catch (error) {
      console.error('Error checking authentication:', error);
      setIsAuthenticated(false);
    } finally {
      setLoading(false);
    }
  });

  useEffect(() => {
    checkAuth();
  }, [checkAuth]);

  if (loading) {
    return <div>Loading...</div>;
  }


  if (!isAuthenticated) {
    return <Navigate to="/" />;
  }

  return isAllowed ? <Element /> : <Navigate to="/not-authorized" />;
};

export default ProtectedRoute;
