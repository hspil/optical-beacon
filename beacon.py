#Morse durations for "KL4LJ/B"
#kludgy, but it works
callsign = [3, 1, 3, 0, 1, 3, 1, 1, 0, 1, 1, 1, 1, 3, 0, 1, 3, 1, 1, 0, 1, 3, 3, 3, 0, 3, 1, 1, 3, 1, 0, 3, 1, 1, 1]

wpm = 10

tone_freq = 500 #Hz

#pin number (software, not physical) for IR led
output_pin = 15


from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep

#convert from wpm to seconds
dit_length = 60/(50*wpm)


#PIO state machine routine
@asm_pio(set_init=PIO.OUT_LOW)
def square():                    #50% duty cycle squarewave is fine for a low power beacon
                                 #with a lower duty cycle the LEDs could be run harder for higher peak brightness
    wrap_target()
    set(pins, 1) [1]             #super weird, but the [1] is a 1 clock cycle NOP
    set(pins, 0) [1]
    wrap()

#initialize state machine 0 with routine and state machine clock frequency, and connect to output pin
squarewave = rp2.StateMachine(0, square, freq=4*tone_freq, set_base=Pin(output_pin))




def send(morse_sequence):
    for element in morse_sequence:
        if element:                       #actual element
            squarewave.active(1)
            sleep(dit_length * element)
            squarewave.active(0)
            sleep(dit_length)
        else:
            sleep(3*dit_length)          #space

while(True):
                        #long constant tone
    send(callsign + [0, 30, 0, 0, 0])
