import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
LED = 12 # PWM pin

# 듀티비 목록 작성

# 출력 핀으로 설정, 초기출력은 로우레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
# PWM 객체 인스턴스 작성ls

PWM_led = GPIO.PWM(LED, 100 )
# PWM 신호 출력
PWM_led.start(100)

while 1:
    duty_str = input('Change duty cycle:')
    duty= int(duty_str)
    if duty > 100:
        print('wrong input value. ')
    else:
        PWM_led.ChangeDutyCycle(duty) 
# 키보드 예외 검출
    end_key = input("- Stop to Blink LED, Please Enter the 'end' :")
    if end_key == "end":
        break
# 아무 것도 안함

GPIO.cleanup()