# Photobox by LEF

Waits for a USB stick, then takes a photo with a connected camera and then saving it to the stick.

Loosely based on: http://www.instructables.com/id/Raspberry-Pi-photo-booth-controller/

## Libraries used
* [Picamera](https://picamera.readthedocs.io/en/release-1.13/index.html)
* [RPi.GPIO](https://github.com/adafruit/Adafruit_Python_GPIO)
* [Adafruit_CharLCD](https://github.com/adafruit/Adafruit_Python_CharLCD)

## Tools

### STOP ACTIVE PYTHON SCRIPT
pkill -f photobox.py

### COPY to PI
scp photobox.py pi@192.168.0.191:/home/pi

### CONNECT to PI USING SSH
ssh 192.168.0.191 -l pi