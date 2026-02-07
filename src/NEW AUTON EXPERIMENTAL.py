from vex import *

# Brain should be defined by default
brain = Brain()
inertial_1 = Inertial(Ports.PORT7)
numOfDataEntries=100
numOfDataEntries = 100
polling_delay_msec = 50
data_buffer = ""
# Add timer initialization code
brain.timer.clear()
# Commands to write the data to buffer
data_buffer += "%1.3f" % brain.timer.value() + "\n"
data_buffer += "%1.3f" % inertial_1.acceleration(XAXIS) + ","
data_buffer += "%1.3f" % inertial_1.acceleration(YAXIS) + ","
data_buffer += "%1.3f" % inertial_1.acceleration(ZAXIS) + "\n"
# Data Generation
for i in range(0, numOfDataEntries):

    # Commands to write the data to buffer
    data_buffer += "%1.3f" % brain.timer.value() + "\n"
    data_buffer += "%1.3f" %inertial_1.acceleration(XAXIS) + ","
    data_buffer += "%1.3f" %inertial_1.acceleration(YAXIS) + ","
    data_buffer += "%1.3f" %inertial_1.acceleration(ZAXIS) + "\n"

    # Data Generation
for i in range(0, numOfDataEntries):

    # Commands to write the data to buffer
    data_buffer += "%1.3f" % brain.timer.value() + "\n"
    data_buffer += "%1.3f" % inertial_1.acceleration(XAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(YAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(ZAXIS) + "\n"


    wait(polling_delay_msec, MSEC)

numOfDataEntries = 100
polling_delay_msec = 50
data_buffer = ""

# Add timer initialization code
brain.timer.clear()

# Data Generation
for i in range(0, numOfDataEntries):

    # Commands to write the data to buffer
    data_buffer += "%1.3f" % brain.timer.value() + "\n"
    data_buffer += "%1.3f" % inertial_1.acceleration(XAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(YAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(ZAXIS) + "\n"

    wait(polling_delay_msec, MSEC)

# Hold the program if the SD card is not inserted
if not brain.sdcard.is_inserted():
    brain.screen.set_cursor(1,1)
    brain.screen.print("SD Card Missing")
    while(True):
        wait(5, MSEC)

csvHeaderText = "time, x, y, z"
sd_file_name = "myDataPY.csv"

# Create CSV Header
data_buffer = csvHeaderText + "\n"

# CSV Data Generation
for i in range(0, numOfDataEntries):

    # Commands to write the data to buffer
    data_buffer += "%1.3f" % brain.timer.value() + "\n"
    data_buffer += "%1.3f" % inertial_1.acceleration(XAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(YAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(ZAXIS) + "\n"


    wait(polling_delay_msec, MSEC)
    
    # CSV Data Generation
for i in range(0, numOfDataEntries):

    # Commands to write the data to buffer
    data_buffer += "%1.3f" % brain.timer.value() + "\n"
    data_buffer += "%1.3f" % inertial_1.acceleration(XAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(YAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(ZAXIS) + "\n"

    wait(polling_delay_msec, MSEC)

# Write the data to SD Card
brain.screen.set_cursor(4,1)
if brain.sdcard.savefile(sd_file_name, bytearray(data_buffer,'utf-8')) == 0:
    brain.screen.print("SD Write Error")
else:
    brain.screen.print("Data Written")

    # Library imports
from vex import *

# Brain should be defined by default
brain = Brain()
inertial_1 = Inertial(Ports.PORT7)

csvHeaderText = "time, x, y, z"
sd_file_name = "myDataPY.csv"
polling_delay_msec = 50
numOfDataEntries = 100
data_buffer = ""

# Hold the program if the SD card is not inserted
if not brain.sdcard.is_inserted():
    brain.screen.set_cursor(1,1)
    brain.screen.print("SD Card Missing")
    while(True):
        wait(5, MSEC)

# Add any sensor & timer initialization code here
brain.timer.clear()

# Create CSV Header
data_buffer = csvHeaderText + "\n"

# CSV Data Generation
for i in range(0, numOfDataEntries):

    # Commands to write the data to buffer
    data_buffer += "%1.3f" % brain.timer.value() + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(XAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(YAXIS) + ","
    data_buffer += "%1.3f" % inertial_1.acceleration(ZAXIS) + "\n"

    wait(polling_delay_msec, MSEC)

# Write the data to SD Card
brain.screen.set_cursor(4,1)
if brain.sdcard.savefile(sd_file_name, bytearray(data_buffer,'utf-8')) == 0:
    brain.screen.print("SD Write Error")
else:
    brain.screen.print("Data Written")

