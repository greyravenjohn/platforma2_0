#servoblaster
import time

def set_servo(servo, position):
    with open("/dev/servoblaster") as servo_blaster:
        servo_blaster.write("{}={}\n".format(servo, position))

#tests
print('start test')

set_servo('0', '50%')
time.sleep(5)

set_servo(0, '75%')
time.sleep(5)
set_servo(0, '25%')
time.sleep(5)
set_servo(0, '50%')
time.sleep(5)
set_servo(1, '50%')
time.sleep(5)
set_servo(1, '75%')
time.sleep(5)
set_servo(1, '25%')
time.sleep(5)
set_servo(1, '50%')

print('end test')
