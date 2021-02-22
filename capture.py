import serial
import time
import os
from picamera import PiCamera

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
camera = PiCamera()



while True:
  read_ser=ser.readline()
  print(read_ser)
  camera.start_preview()
  sleep(20)
  camera.stop_preview()
  

  


