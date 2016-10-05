#!/usr/bin/env python
#A Python script for reading and printing temperatures. 2016
#Author: Kuan-Yu Chen
#Last update: 2016.Sep.30
#Description: Read four temperature probes (DS18B20) and print temperatures to LCD display

import time
import LCD_driver

#Set up LCD display
display = LCD_driver.lcd()
display.lcd_clear()
display.lcd_display_string("Reading",1)
display.lcd_display_string("temperatures...",2)

#Read sensor SN file (ProbeSN.txt)
try:
	openfile = open("ProbeSN.txt","r")
except:
	print("Oops. Can't find probe serial numbers. Check if ProbeSN.txt exists.")

#Extract probe SN from ProbeSN.txt file
SensorSN_list = []
for line in openfile:
	line = line.strip()
	SensorSN_list.append(line)

#Read temperature from each sensor/probe
def readTemp():
	TempData = []
	base_dir = '/sys/bus/w1/devices/'
	for sensorSN in SensorSN_list:
		sensor_file = base_dir + sensorSN + '/w1_slave'
		try:
			sensor_open = open(sensor_file, 'r')
		except:
			temp_num = " NA "
			TempData.append(temp_num)
			continue	
		sensor_read = sensor_open.read()
		sensor_open.close()
		#check if probe is working
		check_probe = sensor_read.split('\n')[0].split(' ')[-1] #get the last element (yes/no)
		if check_probe == "NO":
			temp_num = " NA "
			TempData.append(temp_num)
		else:
			#convert temp reading to C degree
			temp_string = sensor_read.split('\n')[1].split(' ')[9]
			temp_num = float(temp_string[2:])/1000
			temp_num = round(temp_num,2)
			TempData.append(temp_num)
	row1 = "#1:"+str(TempData[0])[0:4]+" #2:"+str(TempData[1])[0:4]
	row2 = "#3:"+str(TempData[2])[0:4]+" #4:"+str(TempData[3])[0:4]
	display.lcd_clear()
	display.lcd_display_string(row1,1)
	display.lcd_display_string(row2,2)


#Print temperatures on LCD display
display.lcd_clear()
try:
	while True:
		readTemp()
		time.sleep(5)
except KeyboardInterrupt:
	display.lcd_clear()


