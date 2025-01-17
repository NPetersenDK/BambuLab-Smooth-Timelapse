# BambuLab-Smooth-Timelapse
Make beautiful Timelapses on your Bambu Lab printer using the build in Timelapse support in Bambu Studio. Using a external camera.

The idea can be used on all Bambu Lab printers, but the designs i have made is for the Bambu Lab A1.

Using this design i made on MakerWorld: https://makerworld.com/en/models/540403#profileId-457794

Watch it in action here:

[![A1BenchyTimelapse](https://img.youtube.com/vi/zzbIBHHvKSc/0.jpg)](https://www.youtube.com/watch?v=zzbIBHHvKSc)

## Requirements
A door sensor connected to your Raspberry Pi, that is placed on the printer where it can detect when it goes to for taking a picture internally. 

This way we do not change anything regarding GCODE or other stuff in Bambu Studio, only using already existing features.

I used a simple magnetic door sensor that I connected to the GPIO pins on the Raspberry Pi. Which can be found here: https://www.aliexpress.com/item/1005006027619189.html

Connected to ground and PIN 26.

You also need to have a camera that is supported by gphoto2. I used a Sony A6000 with a dummy camera and USB connected to my Raspberry Pi. You can see all compatible cameras here: http://www.gphoto.org/proj/libgphoto2/support.php 
The commands we run when taking a picture can be found and modified in the run.sh file.

You can also use another camera, all the python script does is running the run.sh file when the door sensor is triggered. It could be a USB Webcam, a script calling OBS to take a picture fx or other things. Get creative 😄

## Installation on the Bambu Lab A1
1. Print this design: https://makerworld.com/en/models/540403#profileId-457794
2. Connect the door sensor to your Raspberry Pi
3. Install the door sensor to the design you printed and install on the A1.
4. Install the magnet on the printing head of the A1.
5. You might wanna run a full calibration of the printer again, just to be safe. As you have changed the weight on the printing head.

![A1 Door Sensor](pictures/A1-DoorSensor.png)

## Installation on Raspberry Pi
1. Git clone or download the repository to your Raspberry Pi
2. chmod +x run.sh
3. python3 run.py
4. Test that it takes a picture by moving the magnet to the door sensor.

## Usage
1. Make sure to run the python script before starting a print. You can run it in the background, or in a screen session.
2. Start a print in Bambu Studio as you normally would, but with the following parameters:
3. Go under Others -> Special Mode -> Timelapse -> Smooth
4. When starting the print enable the timelapse feature.
5. It will now go to the poop position for each layer and take a picture. The pictures will be saved in the folder you specify in the run.sh file.