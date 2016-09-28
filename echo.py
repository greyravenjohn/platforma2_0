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
            self.pulse_start = time.time()
        while( GPIO.input(self.ECHO) == 1 ):
            self.pulse_end = time.time()
        #przeliczenie pomiaru
        self.pulse_duration = self.pulse_end - self.pulse_start
        self.distance = self.pulse_duration * 17150
        self.distance = round( self.distance, 2)

        return self.distance
