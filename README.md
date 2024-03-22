# ESP32 Sensor WebViz
Display live data from an ESP32 on a locally hosted website running on a personal computer. 

# Uses:
- Live updates of UAV stats with responsive GUI
- Weather stations with responsive web page
- Typical ESP32 web hosting projects but with the ability to add images, responsiveness, and much more

# First setup
(Install [Python](https://www.python.org) and [Arduino IDE](https://www.arduino.cc) first)
1. Git clone repository (or download as .ZIP):
```
git clone https://github.com/MataiMoorfield/ESP32-Sensor-WebViz
cd ESP32-Sensor-WebViz
```
2. Install nessacerry requirements:
```
pip install -r requirements.txt
```
3. Install the ESP32 core:
 - Open the Arduino IDE.
 - Go to File > Preferences.
 - In the "Additional Board Manager URLs" field, add the following URL: https://dl.espressif.com/dl/package_esp32_index.json
 - Click OK to close the Preferences window.
 - Go to Tools > Board > Boards Manager...
 - Search for "esp32" in the Boards Manager search bar.
 - Install "esp32" by Espressif Systems.

# Examples
Located in the ```examples``` folder, there a few examples:
- Send temperature and humidity (DHT11) to display on a Python GUI
- Rotation example with MPU6050 and display on a web page (HTML, CSS)
Infomation on these are located in ```README``` files in each folder
# Tests:
Located under the ```tests``` folder found in the ```info``` folder, there is a test for the logger called ```log test.py```. This Python script allows you to test the log system without uploading any code to it. More details are its folder.


# How the Webserver Works
THe ESP32 hosts a simple webserver containing the raw sensor data in JSON format. The ```log.py``` logs this data into ```log.csv```. The ```main.py``` file hosts a complex webpage using ```index.html``` and ```style.css``` to display the ```log.csv``` file. Images and different features can be added to ```index.html``` and ```style.css``` which is unable to work if the HTML id directly hosted on the ESP32. Check out the map located in ```info/layout```. Open ```Layout.canvas``` with Obsidian.

# Updates
- Two way stats (sending stats back to the ESP32 for more actions - e.g. turning on/off a light)
- Faster reload time for the webpage

# Languages:
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,cpp,html,css" />
  </a>
</p>

# Tools:
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=obsidian,arduino,github,vscode" />
  </a>
</p>


Email me: [Matai Moorfield](mailto:matai@moorfield.co.nz)

This repository is licenced under the **MIT licence**