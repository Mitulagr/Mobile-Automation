from ppadb.client import Client
from PIL import Image
import numpy
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

while True : 

    device.shell(f'input touchscreen swipe 540 1200 540 1200 10')

    time.sleep(1.7)
