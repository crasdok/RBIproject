import RPi.GPIO as GPIO
import time
 # 핀번호 할당법은 커넥터 핀번호로 설정

GPIO.setwarnings(False)
# GPIO pin setting
# A= 40
# B= 38
# C= 37
# D= 36
# E= 35
# F= 33
# G= 32
# DP= 31
seg = [40, 38, 37, 36, 35, 33, 32, 31] # GPIO pin
# A B C D E F G DP
fnd = [(1,1,1,1,1,1,0,0), #0
       (0,1,1,0,0,0,0,0), #1
       (1,1,0,1,1,0,1,0), #2
       (1,1,1,1,0,0,1,0), #3 
       (0,1,1,0,0,1,1,0), #4
       (1,0,1,1,0,1,1,0), #5
       (1,0,1,1,1,1,1,0), #6
       (1,1,1,0,0,0,0,0), #7
       (1,1,1,1,1,1,1,0), #8
       (1,1,1,1,0,1,1,0)] #9

GPIO.setmode(GPIO.BOARD)
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
for i in range(0, 10, 1):
       GPIO.output(seg, fnd[i] )
       time.sleep(1)
GPIO.cleanup()
