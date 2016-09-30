#!/usr/bin/env python
#I2C 16*2 LCD display test drive

import LCD_driver
import time

display = LCD_driver.lcd()

try:
	print("Some text should appear on LCD display. Press ctrl+c to clear the text on LCD")
	while True:
		display.lcd_display_string("Hello World", 1) #write to 1st line
		display.lcd_display_string("Pi Temp Guard", 2) #write to 2nd line
		
except KeyboardInterrupt: #press ctrl+c to clear LCD display
	display.lcd_clear()
	print("Clearing up")


