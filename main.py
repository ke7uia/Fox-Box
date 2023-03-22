# Program to blink Morse Code on an LED based on
# user entered message.
# Inspired by Simon Monk's Programming the Pico
# Lori Pfahler
# Feb 2023
#https://github.com/lpfahler/Pico_Projects/blob/main/morse_code_blinker.py

# import libraries
from machine import Pin
import utime

# setup
boardLED = Pin(25, Pin.OUT)
redLED   = Pin(26, Pin.OUT)
blueLED  = Pin(27, Pin.OUT)
greenLED = Pin(22, Pin.OUT)
relay    = Pin(15, Pin.OUT)
buzzer   = machine.PWM(machine.Pin(2))

def tone(pin,frequency,duration):
    pin.freq(frequency)
    pin.duty_u16(3000)
    utime.sleep_ms(duration)
    #utime.sleep(.91)
    pin.duty_u16(0)

# create needed sleep times for 10 words per minute dot = 0.12 seconds
# 5 words per minute is 0.24 seconds
dot        = 0.12
dash       = 4 * dot
withinChar = dot
betChar    = 2 * dot
betWord    = 8 * dot

# make sure LED is off
redLED.off()
blueLED.off()
greenLED.on()
relay.value(0)
utime.sleep(2)


# dictionary for letters and numbers linked to the Morse code for that character
morseCode = {
    'a' : '.-',    'b' : '-...',  'c' : '-.-.',
    'd' : '-..',   'e' : '.',     'f' : '..-.',
    'g' : '--.',   'h' : '....',  'i' : '..',
    'j' : '.---',  'k' : '-.-',   'l' : '.-..',
    'm' : '--',    'n' : '-.',    'o' : '---',
    'p' : '.--.',  'q' : '--.-',  'r' : '.-.',
    's' : '...',   't' : '-',     'u' : '..-',
    'v' : '...-',  'w' : '.--',   'x' : '-..-',
    'y' : '-.--',  'z' : '--..',  '1' : '.----',
    '2' : '..---', '3' : '...--', '4' : '....-',
    '5' : '.....', '6' : '-....', '7' : '--...',
    '8' : '---..', '9' : '----.', '0' : '-----'
    }

# function for blinking the LED for a particular letter or number
def charBlinks(char, buzzer):
    # if the character is a space, sleep the between word time
    if char == ' ':
        # assuming that the space is inside the message (not the first character)
        # for a space, we need to sleep "betWord - 3*dot" since the blinking code always sleeps
        # betChar (=3*dot) at the end of each character
        print(" ")
        utime.sleep(betWord - 3*dot)
    else:
        # look up character in morseCode dictionary - make lowercase if needed
        mCode = morseCode.get(char.lower())
        # if the code is found - blink the code
        if mCode:
            print(char, mCode)
            # need to know number of dot/dashes to do the between character timing
            lenCode = len(mCode)
            # counter to know when we get to the last dot/dash in mCode
            count = 0
            for symbol in mCode:
                # tract place in mCode
                count += 1
                if symbol == '.':
                    # blink a dot
                    redLED.on()
                    tone(buzzer, 262, 250)
                    utime.sleep(dot)
                    redLED.off()
                    if count == lenCode:
                        # character blinks finished - sleep the between character time
                        utime.sleep(betChar)
                    else:
                        utime.sleep(withinChar)
                if symbol == '-':
                    # blink a dash
                    redLED.on()
                    tone(buzzer, 262, 250)                    
                    utime.sleep(dash)
                    redLED.off()
                    if count == lenCode:
                        # character blinks finished - sleep the between character time
                        utime.sleep(betChar)
                    else:
                        utime.sleep(withinChar)
        else:
            # print this if the code for the character is not found
            print('No Morse code for this character:', char)
    
while True:
#    myMessage = input('Enter Your Message (a-z, 0-9): ')
    myMessage = "de ke7uia  beacon"
    greenLED.value(0)
    relay.value(1)        #open up the PTT
    blueLED.value(1)      #show that the PTT is on
    utime.sleep(5)        #wait for the PTT to turn on
    
    tone(buzzer, 262, 2250)  #just send a tone out
    tone(buzzer, 100, 2250)
    tone(buzzer, 262, 2250)
    utime.sleep(5)
    
    for char in myMessage:
        charBlinks(char, buzzer)
        boardLED.toggle()
    greenLED.value(1)
    blueLED.value(0)
    relay.value(0)
    utime.sleep(5)

    
