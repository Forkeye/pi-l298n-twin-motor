import RPi.GPIO as GPIO          
from time import sleep

in1c = 24 #motor 1 clockwise input
in1ac = 23 #motor 1 anticlockwise input
en1 = 25 #motor 1 enable
temp1=1

in2c = 27 # motor 2 clockwise input
in2ac = 17 #motor 2 anticlockwise input
en2 = 22 #motor 2 enable

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1c,GPIO.OUT)
GPIO.setup(in1ac,GPIO.OUT)
GPIO.setup(in2c,GPIO.OUT)
GPIO.setup(in2ac,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in1c,GPIO.LOW)
GPIO.output(in1ac,GPIO.LOW)
GPIO.output(in2c,GPIO.LOW)
GPIO.output(in2ac,GPIO.LOW)
p=GPIO.PWM(en1,1000)
p.start(25)
q=GPIO.PWM(en2,1000)
q.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=raw_input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1c,GPIO.HIGH)
         GPIO.output(in2c,GPIO.HIGH)
         GPIO.output(in1ac,GPIO.LOW)
         GPIO.output(in2ac,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1c,GPIO.LOW)
         GPIO.output(in2c,GPIO.LOW)
         GPIO.output(in1ac,GPIO.HIGH)
         GPIO.output(in2ac,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1c,GPIO.LOW)
        GPIO.output(in2c,GPIO.LOW)
        GPIO.output(in1ac,GPIO.LOW)
        GPIO.output(in2ac,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1c,GPIO.HIGH)
        GPIO.output(in2c,GPIO.HIGH)
        GPIO.output(in1ac,GPIO.LOW)
        GPIO.output(in2ac,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1c,GPIO.LOW)
        GPIO.output(in2c,GPIO.LOW)
        GPIO.output(in1ac,GPIO.HIGH)
        GPIO.output(in2ac,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
