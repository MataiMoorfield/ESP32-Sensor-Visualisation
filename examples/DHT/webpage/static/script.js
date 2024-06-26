function fetchData() {
    fetch('/')
        .then(response => response.text())
        .then(html => {
            const parser = new DOMParser();
            const newDocument = parser.parseFromString(html, 'text/html');
            const newTable = newDocument.getElementById('data-table');
            const currentTable = document.getElementById('data-table');
            currentTable.innerHTML = newTable.innerHTML;
            const humidityIndex = Array.from(newTable.querySelectorAll('th')).findIndex(th => th.textContent.trim() === 'humidity'); 
            const currentHumidity = Array.from(newTable.querySelectorAll('td'))[humidityIndex].textContent.trim();
            const temperatureIndex = Array.from(newTable.querySelectorAll('th')).findIndex(th => th.textContent.trim() === 'temperature');
            const currentTemperature = Array.from(newTable.querySelectorAll('td'))[temperatureIndex].textContent.trim();
            document.getElementById('humidity-info').textContent = `Humidity: ${currentHumidity}`;
            document.getElementById('temperature-info').textContent = `Temperature: ${currentTemperature}`;
        });
}

fetchData();

setInterval(fetchData, 5000);
