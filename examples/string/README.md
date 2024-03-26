# Info
This examople is for the ESP32 to test the full system without any sensors but still running the ESP32.

# How to use
1. Change the code in the ```main.ino``` script for your current network and network password
2. Install ESP32 core (if not done already). More details are available is the main README
3. Install the Arduino libraries:
```
ArduinoJson.h by "Benoît Blanchon"
```
5. Upload ```main.ino``` code to ESP32
6. View the serial monitor to see the ESP32 WiFi status (connected or not) and the local IP (i.e. ```192.168.1.39```). Just to double check, you can enter the IP address into a search engine. A string of the JSON data will appear.
7. Update the IP address of the ESP32 in the loggers (view main README for details) on logging etc.