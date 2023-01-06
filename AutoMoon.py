import RPi.GPIO as GPIO
import smbus
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
# Trig=11 초음파 신호 전송핀 번호 지정 및 출력지정
# Echo=12 초음파 수신하는 수신 핀 번호 지정 및 입력지정
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
def main():
    PinTrig=16
    PinEcho=18
    duty_ratio= 0
    MaxDuty= 12
    lcd_init()
    PWMpin= 12
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(PinTrig, GPIO.OUT) 
    GPIO.setup(PinEcho, GPIO.IN)
    GPIO.setup(PWMpin, GPIO.OUT)
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)
    Servo=GPIO.PWM(MaxDuty, 50) 
    Servo.start(0)
    startTime=0
    stopTime=0
    while True:
        GPIO.output(PinTrig, False) 
        time.sleep(2)
        # trigger
        print ('Calculating Distance. 1 nanosec pulse')
        GPIO.output(PinTrig, True) 
        time.sleep(0.00001) 
        GPIO.output(PinTrig, False) 
        # echo
        while GPIO.input(PinEcho) == 0: 
            startTime = time.time()
        while GPIO.input(PinEcho) == 1: 
            stopTime = time.time()
        Time_interval= stopTime - startTime
        Distance = Time_interval * 17000
        Distance = round(Distance, 2)
        cvtnum= str(Distance)
        cm= cvtnum + ' cm'
        print ('Distance => ', Distance, 'cm')
        lcd_string(cm,LCD_LINE_1)
        if Distance < 70:
            GPIO.output(seg, fnd[11] )
            Servo.ChangeDutyCycle(10)
            lcd_string("Open the door",LCD_LINE_2)
        else:
            GPIO.output(seg, fnd[0] )
            Servo.ChangeDutyCycle(2)
            lcd_string("Close the door",LCD_LINE_2)
        if duty_ratio == MaxDuty:
            duty_ratio= 0
            Servo.ChangeDutyCycle(0)
    GPIO.cleanup()
    
if __name__ == '__main__':
    main()