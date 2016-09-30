#!/usr/bin/env python
#Read four temperature probes (DS18B20) and print temperature to LCD display

import time
import LCD_driver

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

print(SensorSN_list)



#def readTemp