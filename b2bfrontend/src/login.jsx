import React, { useState } from 'react';
import { MDBContainer, MDBCol, MDBRow, MDBBtn, MDBIcon, MDBInput, MDBCheckbox } from 'mdb-react-ui-kit';
import './login.css';
import b2blogo from './b2blogo.png';
import api from './api.jsx'; // Import the Axios instance
import { useNavigate } from 'react-router-dom'; // Correct hook for navigation in React Router v6


const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate(); // useNavigate hook for redirection

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!username || !password) {
      setError('Please enter both username and password');
      return;
    }

    try {
      const response = await api.post('/accounts/login/', { username, password });
      alert('Login successful!');
      // Handle any post-login actions here (e.g., redirect)
      navigate('/homepage'); // Redirect using navigate

    } catch (err) {
      setError(err.response?.data?.message || 'Invalid credentials');
    }
  };

  return (
    <MDBContainer fluid className="p-5 my-5 d-flex justify-content-center align-items-center h-custom">
      <MDBContainer className="shadow-lg rounded-5 login-form-container p-5 bg-white">
        <MDBRow>
          <MDBCol col='10' md='6'>
            <img src={b2blogo} className="img-fluid" alt="Sample image" />
          </MDBCol>
          <MDBCol md='6'>
            <div className="divider d-flex align-items-center my-4">
              <p className="text-center fw-bold mx-3 mb-0">Enter Username and password</p>
            </div>

            <MDBInput
              wrapperClass='mb-4 mx-3 w-70'
              label='Username'
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter your username"
              id='formControlLg'
              type='text'
              size="lg"
            />

            <MDBInput
              wrapperClass='mb-4 mx-3 w-70'
              label='Password'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter your password"
              id='formControlLg'
              type='password'
              size="lg"
            />

            {error && <p className="error-message text-danger mx-5">{error}</p>}

            <MDBBtn
              className="mb-4 px-5 mx-3 w-100"
              color='black'
              size='lg'
              onClick={handleSubmit}
            >
              Login
            </MDBBtn>
            
            <div className="d-flex justify-content-between mb-4 mx-5">
              <MDBCheckbox name='flexCheck' value='' id='flexCheckDefault' label='Remember me' />
              <a href="#!">Forgot password?</a>
            </div>

            <div className='text-center text-md-start mt-4 pt-2 mx-5'>
            <p className="small fw-bold mt-2 pt-1 mb-2">Don't have an account? <a href="/register" className="link-danger">Register</a></p>
            </div>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
    </MDBContainer>
  );
};

export default Login;
