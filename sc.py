#!/usr/bin/env python
import sys
import serial
import time

ser = serial.Serial('/dev/ttyUSB0',9600)

time.sleep(2)

n = sys.argv[1]
strng = str(n)
ser.write(strng)
print(strng)
