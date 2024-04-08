from machine import Pin
from servo import Servo
import time

motor = Servo(15)

while True:
    motor.move(0)
    time.sleep(1)
    motor.move(180)
    time.sleep(1)

 