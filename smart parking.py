import RPi.GPIO as GPIO
import time

# GPIO pins for the ultrasonic sensor
TRIG_PIN = 18
ECHO_PIN = 24

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def distance_measurement():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Speed of sound = 34300 cm/s
    distance = (pulse_duration * 34300) / 2
    return distance

try:
    while True:
        distance = distance_measurement()
        print(f"Distance: {distance:.2f} cm")

        # Set a threshold distance to detect if a car is parked
        threshold_distance = 50  # Adjust as needed

        if distance < threshold_distance:
            print("Parking space occupied")
        else:
            print("Parking space available")

        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()