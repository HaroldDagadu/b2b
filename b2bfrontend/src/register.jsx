import React, { useState } from 'react';
import { MDBContainer, MDBCol, MDBRow, MDBBtn, MDBInput } from 'mdb-react-ui-kit';
import { useNavigate } from 'react-router-dom'; // Correct hook for navigation in React Router v6
import './login.css';
import b2blogo from './b2blogo.png';
import api from './api.jsx'; // Import the Axios instance

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [email, setEmail] = useState('');
  const [birth_date, setbirth_date] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate(); // useNavigate hook for redirection

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    // Check if passwords match
    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    if (!username || !password || !email || !birth_date) {
      setError('Please fill in all fields');
      return;
    }

    try {
      const response = await api.post('/accounts/register/', { username, password, email, birth_date });
      alert('Registration successful!');
      // Redirect to login page after successful registration
      navigate('/'); // Redirect using navigate
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed');
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
              <p className="text-center fw-bold mx-3 mb-0">Create an Account</p>
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
              label='Email'
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              id='formControlLg'
              type='email'
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

            <MDBInput
              wrapperClass='mb-4 mx-3 w-70'
              label='Confirm Password'
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="Confirm your password"
              id='formControlLg'
              type='password'
              size="lg"
            />

            <MDBInput
              wrapperClass='mb-4 mx-3 w-70'
              label='Date of Birth'
              value={birth_date}
              onChange={(e) => setbirth_date(e.target.value)}
              placeholder="Enter your date of birth"
              id='formControlLg'
              type='date'
              size="lg"
            />

            {error && <p className="error-message text-danger mx-5">{error}</p>}

            <MDBBtn
              className="mb-4 px-5 mx-3 w-100"
              color='black'
              size='lg'
              onClick={handleSubmit}
            >
              Register
            </MDBBtn>

            <div className='text-center text-md-start mt-4 pt-2 mx-5'>
              <p className="small fw-bold mt-2 pt-1 mb-2">Already have an account? <a href="/login" className="link-danger">Login</a></p>
            </div>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
    </MDBContainer>
  );
};

export default Register;
