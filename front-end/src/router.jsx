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

export async function fetchData(setData) {
    try {
        const csrftoken = await getCSRFToken();
        const response = await fetch('http://localhost:8000/api/get_data/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            credentials: 'include'
        });

        if (response.ok) {
            const jsonData = await response.json();
            setData(jsonData); // Set the received data to state
        } else {
            console.error('Failed to fetch data');
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

export async function fetchRegionOptions(setRegionOptions) {
    try {
      const response = await fetch('http://localhost:8000/api/get_regions/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
      });
  
      if (response.ok) {
        const jsonData = await response.json();
        setRegionOptions(jsonData.regions);
      } else {
        console.error('Failed to fetch region options');
      }
    } catch (error) {
      console.error('Error fetching region options:', error);
    }
}

export async function fetchCategoryOptions(setRegionOptions) {
    try {
      const response = await fetch('http://localhost:8000/api/get_categories/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
      });
      if (response.ok) {
        const jsonData = await response.json();
        setRegionOptions(jsonData.categories);
      } else {
        console.error('Failed to fetch region options');
      }
    } catch (error) {
      console.error('Error fetching region options:', error);
    }
  }