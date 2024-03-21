# ESP32 Sensor WebViz
Display live data from an ESP32 on a locally hosted website running on a laptop. 

# Uses:
- Live updates of UAV stats with responsive GUI
- Weather stations with responsive web page
- Typical ESP32 web hosting projects but with the ability to add images, responsiveness, and much more

# First setup
(Install [Python](https://www.python.org) and [Arduino IDE](https://www.arduino.cc) first)
Git clone repository (or download as .ZIP):
```
git clone https://github.com/MataiMoorfield/ESP32-Sensor-WebViz
cd ESP32-Sensor-WebViz
```

# Examples
Located in the ```examples``` folder, there a few examples:
- Sending a JSON string to display on:
    - Web page (HTML, CSS)
    - GUI (Python)
- Send temperature and humidity (DHT11) to display on a Python GUI
- Example drone rotation simulator with MPU6050 and display on a web page (HTML, CSS)

## Sending a JSON string:
The first example is sending a JSON string

# Tesing
Under the ```test``` folder, there is a ```test_logger.py```. This does the same as the ESP32 in the first example above (sending a JSON string). ```test_logger.py``` can be used for tesing the ```main.py``` and ```log.py``` without having to upload any code to the ESP32. 


MUP6050 → ESP32 → (JSON data) → WiFi → ```log.py``` → ```log.csv``` 
```log.csv``` → ```main.py``` → HTML & CSS

# How it works
THe ESP32 hosts a webserver containing raw sensor data. The ```log.py``` logs this data into ```log.csv```. The ```main.py``` file hosts a webpage using ```index.html``` and ```style.css``` to display the ```log.csv``` file. Images and different features can be added to ```index.html``` and ```style.css``` which is unable to work if the HTML id directly hosted on the ESP32.

# Updates
- Two way stats (sending stats back to the ESP32 for more actions - e.g. turning on/off a light)
- Faster reload time for the webpage

# Languages:
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,cpp,arduino,html,css" />
  </a>
</p>


