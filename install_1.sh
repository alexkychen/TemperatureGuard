#!/bin/sh
#This script has been tested under Raspbian Jessie
#Before running the script, be sure to enable I2C and 1-wire functions via raspi-config
### Honorable mention ###
#The following script related to I2C LCD display was modified based on the script that Matthew Timmons-Brown cloned and tweaked for The Raspberry Pi Guy Youtube tutorial.
#Other source related to LCD display libraries include the installer by Ryanteck LTD. 

#Update Pi packages
sudo apt-get update

#Install python-smbus package that will be used in I2C_LCD_dirver.py
sudo apt-get install python-smbus

#Check Pi GPIO I2C version, and copy the I2C_lib..py from ConfigFiles to I2C_lib.py
re = 'python -c "import RPi.GPIO as GPIO; print GPIO.RPI_REVISION"'
if [ $re = "1"]
then
cp ConfigFiles/I2C_lib_0.py ./I2C_lib.py
else
cp ConfigFiles/I2C_lib_1.py ./I2C_lib.py
fi
echo "I2C LCD disply libraries were installed."

#Test drive the LCD display by running LCD_test.py. LCD display should print out Hello World...
echo "Now test drive the LCD display..."
sudo python LCD_test.py

#Reboot the Pi
echo "Press any key to reboot the Pi. After rebooting, please run './install_2.sh' from this folder."
read -n1 -s
sudo reboot

