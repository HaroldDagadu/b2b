// services/api.js
import axios from 'axios';

// Create an Axios instance with the base URL set to port 8000
const api = axios.create({
  baseURL: 'http://35.226.26.69',
  withCredentials: true, // Enable cookies for cross-site access if needed

});


export default api;
