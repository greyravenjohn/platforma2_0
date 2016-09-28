#
import RPi.GPIO as GPIO
import time

class EchoSR04:
    """distance measurement HC-SR04"""

    def __init__( self, trig, echo ):
        
        self.TRIG = trig
        self.ECHO = echo
        #ustawienie pinow gpio trig na wyjscie, echo na wejscie
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        #wylaczenie sygnalu
        GPIO.output(self.TRIG, False)

    def measure_dist( self ):
        #impuls 1 us
        GPIO.output(self.TRIG, True)
        time.sleep( 0.00001 )
        GPIO.output(self.TRIG, False)
        #pomiar
        while( GPIO.input(self.ECHO) == 0 ):
            pulse_start = time.time()
        while( GPIO.input(self.ECHO) == 1 ):
            pulse_end = time.time()
        #przeliczenie pomiaru
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round( distance, 2)

        return distance
