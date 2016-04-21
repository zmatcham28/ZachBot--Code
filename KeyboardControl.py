# ZachBot Mk1 - Main Keyboard Control script
#
#
#
print ("Started Importing")
time.sleep(2)
#==========================================
#Import SYS for Exit
import sys
print ("Sys Imported!")
time.sleep(2)
#==========================================
#Import TIME for sleep
import time
print ("Time Imported!")
time.sleep(2)
#==========================================
#Import PYGAME for controlling
import pygame
print ("PyGame Imported!")
time.sleep(2)
#===========================================
#Import RPI.GPIO for IO
import RPi.GPIO as GPIO
print ("GPIO Imported!")
time.sleep(2)
#==========================================
#PyGame Initialisation for Keyboard Controls
pygame.init()
screen = pygame.display.set_mode((480,480))
print ("PyGame Initialised!")

#==============================================
#GPIO Initialisation for IO
GPIO.setmode(GPIO.BCM)
print ("GPIO Mode set to BCM")
GPIO.setwarnings(False)
print ("GPIO Warnings set to False")
time.sleep(2)
MotorAfwd = 10
MotorAbkd = 9
MotorBfwd = 8
MotorBbkd = 7
LED = 18
print ("Motor & LED Variables Initialised")
time.sleep(2)

GPIO.setup(MotorAfwd,GPIO.OUT)
GPIO.setup(MotorAbkd,GPIO.OUT)
GPIO.setup(MotorBfwd,GPIO.OUT)
GPIO.setup(MotorBbkd,GPIO.OUT)
GPIO.setup(LED,GPIO.OUT)
print ("GPIO Pins 18, 10,9 ,8 and 7 set to Output")
time.sleep(2)
print "GPIO Initialised!"




#=================================================
#Initialise Motor Controls and Functions
def Forwards():
        GPIO.output(MotorAfwd,1)
        GPIO.output(MotorAbkd,0)
        GPIO.output(MotorBfwd,1)
        GPIO.output(MotorBbkd,0)

def Backwards():
        GPIO.output(MotorAfwd,0)
        GPIO.output(MotorAbkd,1)
        GPIO.output(MotorBfwd,0)
        GPIO.output(MotorBbkd,1)

def Left():
        GPIO.output(10,0)
        GPIO.output(MotorAbkd,1)
        GPIO.output(MotorBfwd,1)
        GPIO.output(MotorBbkd,0)

def Right():
        GPIO.output(MotorAfwd,1)
        GPIO.output(MotorAbkd,0)
        GPIO.output(MotorBfwd,0)
        GPIO.output(MotorBbkd,1)

def StopMotors():
        GPIO.output(MotorAfwd,0)
        GPIO.output(MotorAbkd,0)
        GPIO.output(MotorBfwd,0)
        GPIO.output(MotorBbkd,0)

def LEDOn():
    GPIO.output(LED,1)

def LEDOff():
    GPIO.output(LED,0)

print ("Variables and Functions set!")
time.sleep(2)
print ("Starting Control Program - PyGame")
#===========================================
while True:
        LEDOn()
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_UP]:
                print "Forwards"
                Forwards()

        elif keystate[pygame.K_DOWN]:
                print "Backwards"
                Backwards()

        elif keystate[pygame.K_LEFT]:
                print "Left"
                Left()

        elif keystate[pygame.K_RIGHT]:
                print "Right"
                Right()
        else:
                StopMotors()

                
        time.sleep(0.1)
