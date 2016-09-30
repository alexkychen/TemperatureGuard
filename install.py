#!/usr/bin/env python
#

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

while True: #Plug one probe at a time until 4 probes are detected. If an additional probe is plugged, but the total number of probes is not correct, continue enter 1 until it is correct.
	ans2 = raw_input("Please plug one probe to device and enter 1: ")
	if ans2 == "1":
		os.system("sudo modprobe w1-gpio")
		os.system("sudo modprobe w1-therm")
		deviceFolder = os.listdir("devices")
		if len(deviceFolder) == 2:
			sensorSN_1 = deviceFolder[0]
			if sensorSN_1 in SensorSN_list:
				print("Your first probe ("+sensorSN_1+") is detected! Number of probes is 1.")
				continue
			else:			
				SensorSN_list.append(sensorSN_1)
				print("Your first probe ("+sensorSN_1+") is detected! Number of probes is 1.")
				continue
		elif len(deviceFolder) == 3:
			deviceFolder.remove(sensorSN_1)
			sensorSN_2 = deviceFolder[0]
			if sensorSN_2 in SensorSN_list:
				print("Your second probe ("+sensorSN_2+") is detected! Number of probes is 2.")
				continue
			else:
				SensorSN_list.append(sensorSN_2)
				print("Your second probe ("+sensorSN_2+") is detected! Number of probes is 2.")
				continue
		elif len(deviceFolder) == 4:
			deviceFolder.remove(sensorSN_1)
			deviceFolder.remove(sensorSN_2)
			sensorSN_3 = deviceFolder[0]
			if sensorSN_3 in SensorSN_list:
				print("Your third probe ("+sensorSN_3+") is detected! Number of probes is 3.")
				continue
			else:
				SensorSN_list.append(sensorSN_3)
				print("Your third probe ("+sensorSN_3+") is detected! Number of probes is 3.")
				continue
		elif len(deviceFolder) == 5:
			deviceFolder.remove(sensorSN_1)
			deviceFolder.remove(sensorSN_2)
			deviceFolder.remove(sensorSN_3)
			sensorSN_4 = deviceFolder[0]
			if sensorSN_4 in SensorSN_list:
				print("Your fourth probe ("+sensorSN_4+") is detected! Number of probes is 4.")
				break
			else:
				SensorSN_list.append(sensorSN_4)
				print("Your fourth probe ("+sensorSN_4+") is detected! Number of probes is 4.")
				break
		else:
			continue
	else: 
		continue
print("Great! Four temperature probes were set up!")

#Export probe serial numbers to a text file
os.chdir("..")#move up to bus folder
os.chdir("..")#move up to sys folder
os.chdir("..")#move up top 
os.chdir("home/pi/TemperatureGuard")
with open("ProbeSN.txt","w") as probeSN:
	for sn in SensorSN_list:
		probeSN.write(sn + "\n")
print("A probe serial numer file (ProbeSN.txt) was created.")






