# ESP32 data to local host
Receive data from an ESP32 to display on a separate HTML and CSS file locally hosted.

# First setup
(Install [Python](https://www.python.org) and [Arduino IDE](https://www.arduino.cc) first)
Git clone repository (or download as .ZIP):
```
git clone https://github.com/MataiMoorfield/ESP32-to-HTML-Webserver
cd ESP32-to-HTML-Webserver
```

# Uses:
- Live updates of UAV stats with responsive GUI
- Weather stationswith responsive web page

# Examples
Located in the ```examples``` folder, there a few examples:
- Sending a JSON string to display on:
    - Web page (HTML, CSS)
    - GUI (Python)
- Send temperature and humidity (DHT11) to display on a Python GUI
- Example drone rotation simulator with MPU6050 and display on a web page (HTML, CSS)

## Sending a JSON string:

MUP6050 → ESP32 → (JSON data) → WiFi → ```log.py``` → ```log.csv``` 
```log.csv``` → ```main.py``` → HTML & CSS

The ```log.py``` updates the ```log.csv``` from the IP of the ESP32. This is seprate from the ```main.py``` so the logger can be running wile the ```main.py``` isn't. This keeps the log updated.
The ```log.csv``` is a log of the data from the ESP32 and is used by the ```main.py```.


Languages:
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,cpp,arduino,html,css" />
  </a>
</p>
