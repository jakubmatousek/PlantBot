import RPi.GPIO as GPIO
import time
import argparse


PIN = 23

def water(seconds: int):
    """seconds: time in [s] to lift the servo"""
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)
    time.sleep(seconds)
    GPIO.setmode(GPIO.BCM)
    GPIO.output(PIN, False)
    GPIO.cleanup()

    print(f"[SUCCESS] plant successfuly watered for {seconds}s")


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--seconds", help="open water circut for given seconds")
    args = argParser.parse_args()
    try:
        water(int(args.seconds))
    except Exception as e:
        print(f"[ERROR] message: {e}")
        # email send



