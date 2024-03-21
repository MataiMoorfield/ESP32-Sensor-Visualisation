# Setup
1. Change network name and password in the ```main.ino``` for you current WiFi network
2. Connect ESP32 with a MPU6050 module using the wiring on the ```wiring.txt```
3. Upload ```main.ino``` code to ESP32
4. View the serial monitor to see the ESP32 WiFi status (connected or not) and the local IP
5. Update the IP address of the ESP32 in the ```log.py``` script in line ``36``
6. Make sure you have installed the requirements in the ```requirements.txt``` file

# Run
1. Connect the ESP32 to power
2. Run the ```log.py``` script:
```
cd examples/mpu6050/main/log
python log.py
```
> Use ```python3``` for macOS

3. Run the ```main.py``` script:
```
cd ..
python main.py
```
4. Click on the IP of thr local host which appears in the terminal (e.g. ```http://127.0.0.1:5000```)