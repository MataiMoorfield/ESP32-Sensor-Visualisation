# Setup logger
Change the IP of your ESP32 or test logger in the single or constant logger (```constant``` at line ```50``` or ```single``` at line ```45```). The IP will appear in the serial monitor after you have uploaded the ESP32 code.
```cd``` into the main directory:
```
cd main
cd log
```
Navigate to the single or constant log:
```
cd Single
```
or 
```
cd Constant
```

# Run the logger
Run the logger:
```
python log.py
```
> This works for either single or constant log
> Use ```python3``` for macOS

# GUI or Webpage
Create a new terminal and run either ```webpage``` or ```GUI``` Python scripts. The webpage creates a local host which can be viewed on a search engine and the GUI creates a Python graphic user interface. Both of them display the data from the log. If you have run the single log, the table of data will be two rows, while the constant will keep on creating more rows.

```
cd ..
cd ..
cd UI/GUI
python gui.py
```
Or

```
cd ..
cd ..
cd UI/Webpage
python webpage.py
```
> ```cd ..``` is to get out of the log folder. Form the ```main``` you can ```cd UI/GUI``` or ```cd UI/Webpage```