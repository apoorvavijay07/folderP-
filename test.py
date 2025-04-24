import RPi.GPIO as GPIO
from time import sleep

Motor1A = 02 
Motor1B = 03 

Motor2A = 17 
Motor2B = 27 

Motor3A = 9 
Motor3B = 10 

Motor4A = 19 
Motor4B = 26

water = 5
seed = 6


#Set up all as outputs
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)
GPIO.setup(water,GPIO.OUT)
GPIO.setup(seed,GPIO.OUT)


def forward():
	print("Going Forwards")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

	sleep(0.1)



def backward():
	print("Going Backwards")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

	sleep(0.1)

def turnRight():
	print("Going Right")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

	sleep(0.1)

def turnLeft():
	print("Going Left")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

	sleep(0.1)

def stop():
	print("Stopping")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor3B,GPIO.LOW)
	GPIO.output(Motor4A,GPIO.LOW)
	GPIO.output(Motor4B,GPIO.LOW)

def up():
	print("Going up")
	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor3B,GPIO.HIGH)
	sleep(0.4)
	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor3B,GPIO.LOW)

def down():
	print("Going down")
	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.LOW)
	sleep(0.4)
	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor3B,GPIO.LOW)

def aopen():
	print("Going arm open")
	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)
	sleep(0.4)
	GPIO.output(Motor4A,GPIO.LOW)
	GPIO.output(Motor4B,GPIO.LOW)

def aclose():
	print("Going arm close")
	GPIO.output(Motor4A,GPIO.LOW)
	GPIO.output(Motor4B,GPIO.HIGH)
	sleep(0.4)
	GPIO.output(Motor4A,GPIO.LOW)
	GPIO.output(Motor4B,GPIO.LOW)
	
def won():
	print("Going water ON")
	GPIO.output(water,GPIO.HIGH)
	
def woff():
	print("Going water OFF")
	GPIO.output(water,GPIO.LOW)
	
def son():
	print("Going seed ON")
	GPIO.output(seed,GPIO.HIGH)
	
def soff():
	print("Going seed OFF")
	GPIO.output(seed,GPIO.LOW)