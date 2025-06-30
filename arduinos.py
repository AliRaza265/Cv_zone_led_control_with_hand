from cvzone.SerialModule  import SerialObject
import time

Arduno = SerialObject("COM4")

while True:
    Arduno.sendData([1])
    # time.sleep(3)
    # Arduno.sendData([1])
    # time.sleep(1)
