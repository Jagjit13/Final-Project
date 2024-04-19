import time
from RPLCD.i2c import CharLCD
from smbus2 import SMBus

# LCD Setup
lcd = CharLCD('PCF8574', 0x27)  # Update 0x27 to your LCD's I2C address

def display_message(message):
    lcd.clear()
    lcd.write_string(message)
    time.sleep(5)  # Display the message for 5 seconds

def main():
    try:
        while True:
            input_text = input("Enter your message: ")
            display_message(input_text)
    except KeyboardInterrupt:
        print("Program stopped manually")
        lcd.clear()

if __name__ == '__main__':
    main()
