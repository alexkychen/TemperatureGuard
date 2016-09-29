#!/usr/bin/env python
#A Python installer embedded shell script originated from The Raspberry Pi Guy

import os
import RPi.GPIO as GPIO
import time

os.system("sudo apt-get update")
os.system("sudo apt-get install python-smbus -y")

#Check GPIO I2C pin revision
revision = GPIO.RPI_REVISION
if revision == 1:
	os.system("cp ConfigFiles/i2c_lib_0.py ./i2c_lib.py")
else:
	os.system("cp ConfigFiles/i2c_lib_1.py ./i2c_lib.py")
print("I2C LCD libraries were installed.")

#Test drive LCD display
import LCD_driver
display = LCD_driver.lcd()
display.lcd_display_string("Hello World", 1)
display.lcd_display_string("Pi Temp Guard", 2)
print("Some text should appear on LCD display.")
while True:
	ans1 = raw_input("Enter C to clear the text on LCD display: ")
	if ans1.upper() == "C":
		display.lcd_clear()
		break
print("LCD display cleared!")

#Setup DS18B20 temperature probes
SensorSN_list = [] #Create an empty list to save sensors' serial number
os.chdir("..")#move up working directory
os.chdir("..")
os.chdir("..")
os.chdir("sys/bus/w1")#change directory path to w1 

for i in ["first","second","third","fourth"]:
	print("Now please unplug any probe and only plug your " + i + " temperature probe to the device.")
	while True:
		ans2 = raw_input("Enter 1 after the probe is secured: ")
		if ans2 == "1":
			#Retrieve temperature probe SN
			time.sleep(0.5)
			os.system("sudo modprobe w1-gpio")
			time.sleep(0.5)
			os.system("sudo modprobe w1-therm")
			time.sleep(0.5)
			listfolder = os.listdir("devices")#Get list of folder in the devices folder
			time.sleep(0.5)
			break
	SensorSN = listfolder[0]
	SensorSN_list.append(SensorSN)
	time.sleep(0.5)
	print("Your " + i + " probe serial number is " + SensorSN)

#Export probe serial numbers to a text file
os.chdir("..")#move up to bus folder
os.chdir("..")#move up to sys folder
os.chdir("..")#move up top 
os.chdir("home/pi/TemperatureGuard")
with open("ProbeSN.txt","w") as probeSN:
	for sn in SensorSN_list:
		probeSN.write(sn + "\n")







