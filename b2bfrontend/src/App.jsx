import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Import Routes instead of Switch
import Login from './login';
import Register from './register';
import Homepage from './homepage';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} /> {/* Use element with JSX */}
        <Route path="/register" element={<Register />} /> {/* Use element with JSX */}
        <Route path="/homepage" element={<Homepage />} /> {/* Use element with JSX */}

        {/* Add other routes here */}
      </Routes>
    </Router>
  );
}

export default App;
