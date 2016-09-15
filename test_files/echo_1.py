import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
#wylaczenie sygnalu
GPIO.output(TRIG, False)

print ("...")
time.sleep(2)
#sygnal impuls 1us
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)
#pomiar
while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()
#przeliczenie pomiaru
pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)
#wyswietlenie
print ("Distance: ", distance,"cm")

GPIO.cleanup()
