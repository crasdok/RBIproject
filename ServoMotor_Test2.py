import RPi.GPIO as GPIO 
import time 
GPIO.setwarnings(False)
seg = [40, 38, 37, 36, 35, 33, 32, 31]
fnd = [(1,1,1,1,1,1,0,0), #0
       (0,1,1,0,0,0,0,0), #1
       (1,1,0,1,1,0,1,0), #2
       (1,1,1,1,0,0,1,0), #3 
       (0,1,1,0,0,1,1,0), #4
       (1,0,1,1,0,1,1,0), #5
       (1,0,1,1,1,1,1,0), #6
       (1,1,1,0,0,0,0,0), #7
       (1,1,1,1,1,1,1,0), #8
       (1,1,1,1,0,1,1,0), #9
       (1,1,1,0,1,1,1,0), #A
       (0,0,1,1,1,1,1,0), #B
       (1,0,0,1,1,1,0,0)] #C 
def main():
    duty_ratio= 0
    MaxDuty= 12
    
    PWMpin= 12
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PWMpin, GPIO.OUT)
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
    Servo=GPIO.PWM(MaxDuty, 50) 
    Servo.start(0)
    while 1: 
        duty_ratio = int(input('Change duty cycle:'))

        Servo.ChangeDutyCycle(duty_ratio)
        GPIO.output(seg, fnd[duty_ratio] )
        time.sleep(1)
        if duty_ratio == MaxDuty:
            duty_ratio= 0
            Servo.ChangeDutyCycle(duty_ratio)

    Servo.stop()
    GPIO.cleanup()
    print('Everythings cleanup')

if __name__ == '__main__':
    main()