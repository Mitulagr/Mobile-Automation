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

    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)

    image = Image.open('screen.png')
    image = numpy.array(image, dtype=numpy.uint8)

    if(image[1200][540][1]>200) : 
        device.shell(f'input touchscreen tap 540 1200')
        device.shell(f'input touchscreen tap 540 1200')
        #device.shell(f'input touchscreen swipe 540 1200 540 1200 1')
        #device.shell(f'input touchscreen swipe 540 1200 540 1200 1')
