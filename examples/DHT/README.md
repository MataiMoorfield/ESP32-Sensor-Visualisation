# Setup
1. Change network name and password in the ```main.ino``` for you current WiFi network. Change the type of DHT sensor in line ```13``` of the ```main.ino``` code for the DHT11, DHT21, or DHT22 sensor. The code defults it to 11.
2. Connect ESP32 with a DHT temperature and humidity module using the wiring below:
```
DHT11:            ESP32:
VCC         →       3.3v
GND         →       GND
Signal      →       D4 (defult, can be changed in main.ino line 12)
```

3. If you haven't already, install the core for ESP32 (details avaliable in the main README).
4. Install the libraries for the ESP32 using the build in libraries for Arduino IDE. Install
```
ArduinoJson.h by "Benoît Blanchon"
DHT.h by "Adafruit"
```
The rest of the libraries are installed automatically by installing the ESP32 core.

5. Upload ```main.ino``` code to ESP32
6. View the serial monitor to see the ESP32 WiFi status (connected or not) and the local IP (i.e. ```192.168.1.39```). Just to double check, you can enter the IP address into a search engine. A string of the JSON data will appear.
7. Update the IP address of the ESP32 in the loggers (view main README for details).


# Using exmaple weather app
After uploading the ```main.ino``` code to the ESP32, run the single logger. Infomation about loggers is avaiable inthe main README. Next, run the ```main.py``` found under the ```webpage``` folder. This sould create a local host displaying the current stats:

![weather app](<Screenshot 2024-03-31 at 14.42.40.png>)

If you just want to test the website, put example stats in the ```log.csv``` (found in the ```log``` under the ```main``` folder). For example:

```
humidity,temperature
17,28
```
Cut and copy into ```log.csv```. 

The weather app works by creating a table with the data, then retrevies certain pieces of the data under "temperature" and "humidity". It then displays this data on the webpage. 

Folder structure:
```
DHT
├── esp32
│   └── main
│       └── main.ino
└── webpage
    ├── static
    │   ├── style.css
    │   └── script.js
    └── templates
        └── index.html
```