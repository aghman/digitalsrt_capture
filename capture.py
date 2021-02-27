import serial
import time
import os
from picamera import PiCamera

saveLocation = "/mnt/photoshare/DCIM"

def prepDirectories():
    print("Preparing DCIM directory...")
    dirExists = os.path.exists(dirExists)
    if dirExists == False:
        # Make directory
        print("Creating DCIM directory...")
        os.mkdir(saveLocation)

    isADir = os.path.isdir(saveLocation)
    dirExists = os.path.exists(dirExists)
    if dirExists == False || isADir == False:
        #bail
        print("Failed to create DCIM directory. Exiting.")
        exit(1)

def connectSerial():
    serialPort=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
    serialPort.baudrate=9600

    ## Error handling???
    return serialPort


  

def main():
    prepDirectories()
    serialPort = connectSerial()
    camera = PiCamera()

    camera.start_preview()
    while True:
        serialOutput=serialPort.readline()
        print(serialOutput)
        camera.capture()
    camera.stop_preview()


if __name__ == "__main__":
    main()



