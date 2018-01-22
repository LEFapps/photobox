#!/usr/bin/python

import RPi.GPIO as GPIO, time, os, subprocess
import Adafruit_CharLCD as LCD
import commands

# LCD PIN CONFIGURATION
lcd_rs        = 7
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 15

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# BUTTON AND LED PIN CONFIGURATION
GPIO.setmode(GPIO.BCM)
SWITCH = 4
GPIO.setup(SWITCH, GPIO.IN)
GO_LED = 3
WAIT_LED = 2
GPIO.setup(WAIT_LED, GPIO.OUT)
GPIO.setup(GO_LED, GPIO.OUT)

# DEFINE FUNCTIONS

def setLEDs(ready):
  if (ready):
    GPIO.output(WAIT_LED, False)
    GPIO.output(GO_LED, True)
  else:
    GPIO.output(WAIT_LED, True)
    GPIO.output(GO_LED, False)

currentMessage = ""

def message(m):
  global currentMessage
  if (m != currentMessage):
    lcd.clear()
    lcd.message(m)
    currentMessage = m

def init():
  print("Initializing photobox")
  setLEDs(False)
  ip = commands.getoutput('hostname -I').split(' ')[0]
  message("Opstarten...\n"+str(ip))
  time.sleep(5)

def action():
  print("Taking photo")
  message("Foto wordt\ngenomen")
  setLEDs(False)
  # gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi/photobooth_images/photobooth%H%M%S.jpg", stderr=subprocess.STDOUT, shell=True)
  # print(gpout)
  # subprocess.call("sudo /home/pi/scripts/photobooth/assemble_and_print", shell=True)
  time.sleep(1)
  for i in range(0,100):
    message("Opslaan...\n"+str(i+1)+"%")
    time.sleep(0.05)
  time.sleep(1)
  message('Klaar!')
  time.sleep(2)
  message('Verwijder stick\nof neem nog een foto')

def checkUSB():
  partitionsFile = open("/proc/partitions")
  lines = partitionsFile.readlines()[2:] # Skips the header lines
  for line in lines:
    words = [x.strip() for x in line.split()]
    minorNumber = int(words[1])
    deviceName = words[3]
    if minorNumber % 16 == 0:
      path = "/sys/class/block/" + deviceName
      if os.path.islink(path):
        if os.path.realpath(path).find("/usb") > 0:
          return "/dev/%s" % deviceName

# PROGRAM LOOP

init()
print('initcheck')
while True:
  if (checkUSB()):
    setLEDs(True)
    message("Druk op de knop\nvoor een foto")
    if (GPIO.input(SWITCH)):
      action()
  else:
      setLEDs(False)
      message('Steek de USB\nstick in de box')
