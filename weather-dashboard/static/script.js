function getWeather() {
    const location = document.getElementById('location-input').value;

    // this will send a post request to the flask backend to get weather data
    fetch('/get_weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ location })
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('Location not found!');
            } else {

                document.getElementById('location').innerText = `Location: ${data.name}`;
                document.getElementById('temperature').innerText = `Temperature: ${data.main.temp} °C`;
                document.getElementById('description').innerText = `Description: ${data.weather[0].description}`;
            }
        })
        .catch(error => console.error('Error fetching weather:', error));
}

document.getElementById('location-input').value = '';

window.onload = function () {
    loadFavorites();
    loadWeatherHistory();
};




function saveFavorite() {
    const location = document.getElementById('location-input').value;

    // this will send post  request to save the favorite location
    fetch('/save_favorite', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ location })
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => console.error('Error saving favorite location:', error));
}

function loadFavorites() {

    fetch('/favorites')
        .then(response => response.json())
        .then(data => {
            const favoritesList = document.getElementById('favorites-list');
            favoritesList.innerHTML = '';

            data.forEach(location => {
                const listItem = document.createElement('li');
                listItem.textContent = location;
                favoritesList.appendChild(listItem);
            });
        });
}

function loadWeatherHistory() {

    fetch('/weather_history')
        .then(response => response.json())
        .then(data => {
            const historyList = document.getElementById('history-list');
            historyList.innerHTML = '';

            data.forEach(entry => {
                const listItem = document.createElement('li');
                listItem.textContent = `${entry.location} - ${entry.temperature}°C - ${entry.description} (on ${entry.timestamp})`;
                historyList.appendChild(listItem);
            });
        });
}
