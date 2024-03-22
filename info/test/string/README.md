# Info
This examople is for the ESP32 to test the full system without any sensors.

# How to use
1. Change the code in the ```main.ino``` script for your current network and network password
2. Install ESP32 core (if not done already). More details are available is the main README
3. Install the Arduino libraries:
```
ArduinoJson.h by "Benoît Blanchon"
```
4. Upload code to the ESP32
5. View the serial monitor to see IP address
6. Change the ```log.py``` script for the ESP32's IP (line ```36```)
7. ```cd``` into the string directory:
```
cd info/test/string
```
7. Run the ```log.py``` (```python log.py``` - use ```python3``` for macOS)
8. Run the ```main.py``` (```python main.py```). Open the link of the local host which appears in the terminal.