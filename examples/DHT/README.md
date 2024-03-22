# Setup
1. Change network name and password in the ```main.ino``` for you current WiFi network. Change the type of DHT sensor in line ```13``` of the ```main.ino``` code for the DHT11, DHT21, or DHT22 sensor. The code defults it to 11.
2. Connect ESP32 with a DHT temperature and humidity module using the wiring in the ```wiring.txt``` file
3. If you haven't already, install the core for ESP32 (details avaliable in the main README)
 4. Install the libraries for the ESP32 using the build in libraries for Arduino IDE. Install
```
ArduinoJson.h by "Benoît Blanchon"
DHT.h by "Adafruit"
```
The rest of the libraries are installed automatically by installing the ESP32 core.

5. Upload ```main.ino``` code to ESP32
6. View the serial monitor to see the ESP32 WiFi status (connected or not) and the local IP (i.e. ```192.168.1.39```). Just to double check, you can enter the IP address into a search engine. A string of the differet rotation and acceleration data should appear.
7. Update the IP address of the ESP32 in the ```log.py``` script in line ``36``
8. Make sure you have installed the Python requirements in the ```requirements.txt``` file. If you haven't ```cd``` into the main directory and type the command ```pip install -r requirements.txt``` (use ```pip3``` for macOS)

# Run
1. Connect the ESP32 to power
2. Run the ```log.py``` script:
```
cd examples/DHT/main/log
python log.py
```
> Use ```python3``` for macOS

3. Run the ```main.py``` script:
```
cd ..
python main.py
```
4. Open the local host - click on the IP of the local host which appears in the terminal (i.e. ```http://127.0.0.1:5000```)