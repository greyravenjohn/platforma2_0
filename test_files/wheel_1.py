import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

m1_pwm = GPIO.PWM(18, 100)
m2_pwm = GPIO.PWM(27, 100)

GPIO.output(17, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)


m1_pwm.start(50)
m2_pwm.start(50)

time.sleep(5)

m1_pwm.ChangeDutyCycle(75)
m2_pwm.ChangeDutyCycle(75)

time.sleep(5)

m1_pwm.stop()
m2_pwm.stop()

GPIO.cleanup()
