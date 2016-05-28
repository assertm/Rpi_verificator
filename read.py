import MFRC522
import signal
import cv
import time
import os
 
continue_reading = True
MIFAREReader = MFRC522.MFRC522()

cardA = [136,52,192,118,10]
cardB = [136,52,254,238,172]
cardC = [20,38,121,207,132]

def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  print "Ctrl+C captured, ending read."
  MIFAREReader.GPIO_CLEEN()

signal.signal(signal.SIGINT, end_read)

while continue_reading:
  (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
  if status == MIFAREReader.MI_OK:
    print "Card detected"
  (status,backData) = MIFAREReader.MFRC522_Anticoll()
  if status == MIFAREReader.MI_OK:
    print "Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
    if (( backData == cardA ) or ( backData == cardB ) or ( backData == cardC )):
      print "welcome"
      capture = cv.CaptureFromCAM(0)
      frame = cv.QueryFrame(capture)
      cv.SaveImage("../../../Camera/telegram/image/ny.jpg", frame)
      del(capture)
      f1 = open("../../../Camera/telegram/text1.txt", 'wb')
      f1.write("The")
      if ( backData == cardB ):
          f1.write("User with cardB is comming")
      elif ( backData == cardA ):
          f1.write("User whith cardA is comming")
      #time.sleep(5)
      os.system('python3 telegram.py')
    else:
      print "wrong Card"

