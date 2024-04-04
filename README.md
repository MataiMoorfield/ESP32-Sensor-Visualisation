# ESP32 Sensor WebViz
Display live data from an ESP32 on a locally hosted website or graphic user interface. Video on examples and how to use will be up soon [here](https://youtube.com/@Bot-Frenzy) 

# Uses
- Live updates of UAV stats with responsive GUI
- Weather stations with responsive web page
- Typical ESP32 web hosting projects but with the ability to add images, responsiveness, and much more

# First setup
(Install [Python](https://www.python.org) and [Arduino IDE](https://www.arduino.cc) first)
1. Git clone repository (or download as .ZIP):
```
git clone https://github.com/MataiMoorfield/ESP32-Sensor-Visualisation
cd ESP32-Sensor-Visualisation
```
2. Install nessacerry requirements:
```
pip install -r requirements.txt
```
3. Install the ESP32 core if not done so already:
 - Open the Arduino IDE.
 - Go to File > Preferences.
 - In the "Additional Board Manager URLs" field, add the following URL: https://dl.espressif.com/dl/package_esp32_index.json
 - Click OK to close the Preferences window.
 - Go to Tools > Board > Boards Manager...
 - Search for "esp32" in the Boards Manager search bar.
 - Install "esp32" by Espressif Systems.
 More info about getting started with the ESP32 [here](https://randomnerdtutorials.com/getting-started-with-esp32/)

# Examples
Located in the ```examples``` folder, there a few examples:
- Send temperature and humidity from a DHT11 (or similar sensor)
- Rotation example with MPU6050
- Sending a basic string
Infomation on these are located in ```README``` files in each folder

# How to use
1. Upload one of the examples to your ESP32. Make sure to modify the network name and passoword. In the serial monitor, view the IP. 
2. There are two types of logs: single and constant. The single only has one line of data which is updated. The constant log continuously creates a new line with the new data, allowing to see old/previous data. Enter the ESP32's IP into either log (```constant.py``` at line ```50``` or ```single.py``` at line ```42```). Run either log: ```python constant.py``` or ```python single.py``` (use ```python3``` for macOS etc.)
3. Create a new terminal and run either ```webpage``` or ```GUI``` Python scripts. You could also run the weather app example in the ```DHT``` folder. All of the webpage examples create a local host which can be viewed on a search engine and the GUI creates a Python graphic user interface. Both of them display the data from the log. If you have run the single log, the table of data will be two rows, while the constant will keep on creating more rows. The weather app example will display certain stats which are presented by the ESP32 when the DHT code is uploaded to it. The app will not work it random data in the log. A screenshot of the weather app is under the ```DHT``` folder.

# Tests
Located under the ```tests``` folder (found in the ```info``` folder), there is a test for the logger called ```log test.py```. This Python script allows you to test the log system without uploading any code to it. Be sure to update the ESP32's IP with the local host of the test in the loggers. More details are its folder.

# How it works
## Webpage
The ESP32 hosts a simple webserver containing the raw sensor data in JSON format. Both of the ```log.py``` logs this data into ```log.csv```. The ```webpage.py``` file hosts a complex webpage using ```index.html``` and ```style.css``` to display the ```log.csv``` file. Images and different features can be added to ```index.html``` and ```style.css``` which is unable to work if the HTML is directly hosted on the ESP32. Check out the map located in ```info/layout```. Open ```layout.canvas``` with [Obsidian](https://obsidian.md).

## GUI
Much like the webpage but with a Python GUI. The ESP32 hosts a simple webserver containing the raw sensor data in JSON format. Both of the ```log.py``` logs this data into ```log.csv```. The ```gui.py``` file creates a Python GUI and displays teh data in the ```log.csv```.

# Notes
Always run the logger first and keep it running behind the GUI or webpage. To do this, create a new terminal and run them separately. This allows data to enter the log, then the ```gui.py``` or ```webpage.py``` file can use that data. If there is no data, nothing will be presented and will result in an error. 

There is a reason the logger is seprate from the main. For example, let's say you are using this repository for a weather app. You will be able to be logging behind the app, which allows you to turn on/off the front end and still have a log.

The log of the mpu6050 example deletes and clears the log every second. This allows for it to be constantly updated. In the DHT exmaple, it stores the history of the log so you could, for exmaple, make a weather app which has history of the past weather. 

# Updates
- Two way stats (sending stats back to the ESP32 for more actions - e.g. turning on/off a light)
- Faster reload time for the webpage

# Debugging
ESP32 prints this in the serial monitor:
```
Connecting...
Connecting...
Connecting...
```
Solution: be sure to enter the correct network name and passowrd for it to be able to connect to the WiFi.

```
UndefinedError
jinja2.exceptions.UndefinedError: list object has no element 0
```
Make sure the logger is running first or you have put an example CSV file as the ```log.csv```. This error is caused beacuse of the log being empty. You could put this in for example:
```
humidity,temperature
17,28
```
# Folder structure:
The folder structure is avaliable in the ```layout``` folder under ```info```.

# Languages
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,cpp,html,css" />
  </a>
</p>

# Tools
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=obsidian,arduino,github,vscode" />
  </a>
</p>


Email me: [Matai Moorfield](mailto:matai@moorfield.co.nz)

This repository is licenced under the **MIT licence**
