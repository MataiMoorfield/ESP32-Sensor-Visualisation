# ESP32 data to local host
Receive data from an ESP32 to display on a separate HTML and CSS file locally hosted.

Send rotation and acceleration from a MUP6050 on a ESP32 to display it on a HTML page.

MUP6050 → ESP32 → (JSON data) → WiFi → ```log.py``` → ```log.csv``` 
```log.csv``` → ```main.py``` → HTML & CSS

The ```log.py``` updates the ```log.csv``` from the IP of the ESP32. This is seprate from the ```main.py``` so the logger can be running wile the ```main.py``` isn't. This keeps the log updated.
The ```log.csv``` is a log of the data from the ESP32 and is used by the ```main.py```.
