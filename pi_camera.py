import schedule
import time
from picamera import PiCamera
from time import sleep
import datetime

#Capture a picture from the camera, annotate it with timestamp along the top
# and save it in a folder with the day/hour/minute timestamp in file name
def picCapture():
    print ("Taking picture...")
    currTime=datetime.datetime.now()
    camera.start_preview()
    timeSTR = "Time (Y-M-D H:M:S): " + str(currTime)
    fileTimeStamp = str(currTime.day)+"_"+str(currTime.hour)+"_"+ str(currTime.minute)
    print (timeSTR)
    camera.annotate_text = str(timeSTR)
    sleep(5)
    camera.capture('/home/pi/Desktop/lifetime_test/plant_capture/image_'+fileTimeStamp+'.jpg')
    camera.stop_preview()
    print ("Resume waiting...")

#Take a picture every 10 min
print ("Beginning process...")
schedule.every(10).minutes.do(picCapture)
camera = PiCamera()
while True:   
    schedule.run_pending()
    time.sleep(1)
    
