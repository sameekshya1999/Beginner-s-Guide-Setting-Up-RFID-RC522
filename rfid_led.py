import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

# Set up the GPIO for the LED
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Set up the RFID reader
reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print(f"ID: {id}")
        print(f"Text: {text}")

        # Turn on the LED if a tag is detected
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(2)  # Keep the LED on for 2 seconds

        # Turn off the LED
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)  # Wait for 1 second before the next read

except KeyboardInterrupt:
    # Cleanup on exit
    GPIO.cleanup()
finally:
    GPIO.cleanup()
