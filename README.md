# Photobox by LEF

Waits for a USB stick, then takes a photo with a connected camera and then saving it to the stick.

Loosely based on: http://www.instructables.com/id/Raspberry-Pi-photo-booth-controller/

## Libraries used
* [gPhoto2](http://www.gphoto.org/)
* RPi.GPIO
* Adafruit_CharLCD

## Tools

---STOP ACTIVE PYTHON SCRIPT---
pkill -f photobox.py

---COPY to PI---
scp photobox.py pi@192.168.0.191:/home/pi

---CONNECT to PI USING SSH---
ssh 192.168.0.191 -l pi