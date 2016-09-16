# DRV8835
# v1
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
 
class EnginesDriver:
    """class for engines driver"""

    def __init__(self, m1_gpio_pwm, m1_gpio_dir, m2_gpio_pwm, m2_gpio_dir):
#        GPIO.setup(m1_gpio_pwm, GPIO.OUT)
#        GPIO.setup(m1_gpio_dir, GPIO.OUT)
#        GPIO.setup(m2_gpio_pwm, GPIO.OUT)
#        GPIO.setup(m2_gpio_dir, GPIO.OUT)
        self.m1_pwm = GPIO.PWM(m1_gpio_pwm, 100)
        self.m1_direct = m1_gpio_dir
        self.m2_pwm = GPIO.PWM(m2_gpio_pwm, 100)
        self.m2_direct = m2_gpio_dir


    def forward(self):
        GPIO.output(self.m1_direct, GPIO.HIGH)
        GPIO.output(self.m2_direct, GPIO.HIGH)
        self.m1_pwm.start(50)
        self.m2_pwm.start(50)

    def stop(self):
        self.m1_pwm.stop
        self.m1_pwm.stop

    def backward(self):
        GPIO.output(self.m1_direct, GPIO.LOW)
        GPIO.output(self.m2_direct, GPIO.LOW)
        self.m1_pwm.start(50)
        self.m2_pwm.start(50)

    def left(self):
        GPIO.output(self.m1_direct, GPIO.HIGH)
        GPIO.output(self.m2_direct, GPIO.LOW)
        self.m1_pwm.start(50)
        self.m2_pwm.start(50)

    def right(self):
        GPIO.output(self.m1_direct, GPIO.LOW)
        GPIO.output(self.m2_direct, GPIO.HIGH)
        self.m1_pwm.start(50)
        self.m2_pwm.start(50)

    def accelerate(self, acc):
        self.m1_pwm.ChangeDutyCycle(acc)
        self.m2_pwm.ChangeDutyCycle(acc)

#tests
d1 = EnginesDriver(18, 17, 27, 22)

d1.forward()
time.sleep(5)
d1.left()
time.sleep(1)
d1.forward()
time.sleep(2)
d1.right()
time.sleep(1)
d1.backward()
time.sleep(3)
d1.forward()
time.sleep(1)
d1.accelerate(75)
time.sleep(2)
d1.stop()

GPIO.cleanup()
