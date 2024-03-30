function fetchData() {
    fetch('/')
        .then(response => response.text())
        .then(html => {
            const parser = new DOMParser();
            const newDocument = parser.parseFromString(html, 'text/html');
            const newTable = newDocument.getElementById('data-table');
            const currentTable = document.getElementById('data-table');
            currentTable.innerHTML = newTable.innerHTML;

            // Extract humidity value
            const humidityIndex = Array.from(newTable.querySelectorAll('th')).findIndex(th => th.textContent.trim() === 'humidity'); 
            const currentHumidity = Array.from(newTable.querySelectorAll('td'))[humidityIndex].textContent.trim();

            // Extract temperature value
            const temperatureIndex = Array.from(newTable.querySelectorAll('th')).findIndex(th => th.textContent.trim() === 'temperature');
            const currentTemperature = Array.from(newTable.querySelectorAll('td'))[temperatureIndex].textContent.trim();

            // Update humidity info at the bottom of the page
            document.getElementById('humidity-info').textContent = `Humidity: ${currentHumidity}`;

            // Update temperature info at the bottom of the page
            document.getElementById('temperature-info').textContent = `Temperature: ${currentTemperature}`;
        });
}

fetchData();

setInterval(fetchData, 5000); // Update every 10 seconds