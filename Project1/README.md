This is the project 1 for the course ECEN 5053- embedded interface design

The Project contains:
1. User Interface(.ui) file
2. A python script which uses pyqt5 libraries to render the UI

To Interface the sensor I have used the python library for the DHD22 sensor provided by adafruit.com
The sensor is interfaced with the rpi on GPIO pin 4. read_retry method in the Adafruit_DHT module is
used to read data from the sensor.

User Interface -
I have Implemented all the mandtory requirements such as
Get Temperature, Get Humidity, Displaying Time and Date, Displaying error if sensor not connected

Extra Credit Implemented -
1. Acquiring of Data every 30 seconds using a QTimer object
2. Storing data into a CSV file for future use
2. Plotting the data acquired
3. Constantly update average reading based on timed readings.

How to Run the Code:
Clone the git repository to your Raspberrypi
Go to folder Project 1
run the project1.py script by typing in the terminal "python3 project1.py"
Then the GUI will appear.

You can Request the Temp and Humidity by pressing the "Query Temp" and "Query Humidity" buttons.
In the background readings will be taken every 30 seconds and average value will be
updated. If the sensor is not connected the GUI should display an error where the Temperature is to be displayed

You can use the Plot button to display a graph of Humidity vs time.

To close the window you can use 'x' button in the upper right corner
