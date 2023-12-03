import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

export async function getCSRFToken() {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/get_csrf_token/', {
      method: 'GET',
      credentials: 'include', // Include credentials such as cookies
    });

    if (response.ok) {
      const data = await response.json();
      const csrfToken = data.csrfToken; // Extract the CSRF token from the response
      return csrfToken;
    } else {
      throw new Error('Failed to fetch CSRF token');
    }
  } catch (error) {
    console.error('Error fetching CSRF token:', error);
    return null;
  }
}

