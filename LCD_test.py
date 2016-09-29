#!/usr/bin/env python
#I2C 16*2 LCD display test drive

import LCD_driver
import time

display = LCD_driver.lcd()

try:
	display.lcd_display_string("Hello World", 1, 2) #write to 1st line and start at 3rd character
	display.lcd_display_string("Pi Temp Guard", 2, 1) #write to 2nd line and start at 2nd character
	print("Some text should appear on LCD display. Press any key to clear the text on LCD")
except KeyboardInterrupt:
	display.lcd_clear()
	exit(0)

