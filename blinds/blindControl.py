import argparse
import json
import requests
import urllib.request
from datetime import datetime
from time import sleep

import RPi.GPIO as GPIO
from gpiozero import LightSensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

ldr = LightSensor(4, charge_time_limit=0.1, threshold=.4)
closed = True
days = ("monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday")

parser = argparse.ArgumentParser(description='Process ip address.')
parser.add_argument('--ip', default='140.141.234.197', type=str)
ip = parser.parse_args().ip
print(ip)


def blinds_close():
    GPIO.output(20, GPIO.HIGH)
    sleep(5)
    print('close')
    GPIO.output(20, GPIO.LOW)


def blinds_open():
    GPIO.output(26, GPIO.HIGH)
    sleep(5)
    print('open')
    GPIO.output(26, GPIO.LOW)


url2 = "http://" + ip + ":8000/lights/state"
while True:
    print("Start Loop")
    print(requests.get(url2).json())
    week = requests.get(url2).json()
    # print(week['monday'])
    day = week[days[datetime.today().weekday()]]
    print(day)
    if day['automatic']:
        print("on auto")
        if ldr.light_detected and closed:
            blinds_open()
            closed = False
        elif not ldr.light_detected and not closed:
            blinds_close()
            closed = True
    else:
        now: datetime = datetime.now()
        if (day.get('start') < now) and (now < day.get('end')) and closed:
            blinds_open()
            closed = False
        if (now > day.get('end')) and (not closed):
            blinds_close()
            closed = True
    sleep(60)
