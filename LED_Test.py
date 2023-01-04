 # GPIO 라이브러리 임포트
import RPi.GPIO as GPIO
 # time 라이브러리 임포트
import time
 
 # 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

 # 사용할 핀번호 대입
LED = 11
LED2 = 12 
LED3 = 13
Led= [LED,LED2,LED3]
 
 # 11번 핀을 출력 핀으로 설정, 초기출력은 로우레벨
# GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(LED3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Led, GPIO.OUT, initial=GPIO.LOW)

        # 무한반복
while 1:
        
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED2, GPIO.LOW)
        time.sleep(1)
        GPIO.output(LED3, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED3, GPIO.LOW)
        time.sleep(1)
