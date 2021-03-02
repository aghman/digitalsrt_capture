import serial
import time
import os
from picamera import PiCamera

saveLocation = "/mnt/photoshare/DCIM"
numDigitsInFilename = 5

def prepDirectories():
    print("Preparing DCIM directory...")
    dirExists = os.path.exists(saveLocation)
    if dirExists == False:
        # Make directory
        print("Creating DCIM directory...")
        os.mkdir(saveLocation)

    isADir = os.path.isdir(saveLocation)
    dirExists = os.path.exists(saveLocation)
    if (dirExists == False) or (isADir == False):
        #bail
        print("Failed to create DCIM directory. Exiting.")
        exit(1)

def connectSerial():
    serialPort=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
    serialPort.baudrate=9600

    ## Error handling???
    return serialPort


def getStartingImageNumber():
    return 0

def getImageName(imageNumber):
    baseImgName = "IMG_"
    imageNumberString = str(imageNumber)
    prefixLength = numDigitsInFilename - len(imageNumberString)
    imageZeroPrefix = baseImgName.join([char*prefixLength for char in '0'])
    finalName = saveLocation + "/" + baseImgName + imageZeroPrefix + imageNumberString +".jpg"
    print(finalName)
    return finalName

  

def main():
    prepDirectories()
    currentImageNumber = getStartingImageNumber()
    print("Starting Image number: " + str(currentImageNumber))

    serialPort = connectSerial()
    camera = PiCamera()
    time.sleep(2)

    #camera.start_preview()
    while True:
        currentImageName = getImageName(currentImageNumber)
        serialOutput=serialPort.readline()
        print(serialOutput)
        camera.capture(currentImageName)
        currentImageNumber += 1
    #camera.stop_preview()


if __name__ == "__main__":
    main()



