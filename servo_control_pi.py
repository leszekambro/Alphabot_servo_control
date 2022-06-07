import RPi.GPIO as GPIO
import time

servoPIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 22, PWM 50Hz
p.start(0) # Inicjalizacja
try:
  p.ChangeDutyCycle(5) #duty 2-12 dla katow 0-180
  time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
