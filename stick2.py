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

    pixels = [list(i[:3]) for i in image[2000]]

    a = 0 
    b = 0 
    c = 0
    for i in range(1,len(pixels)) : 
        if(pixels[i]!=[0,0,0]) : 
            a = i
            break
    for i in range(a,len(pixels)) : 
        if(pixels[i]==[0,0,0]) : 
            b = i
            break
    for i in range(b,len(pixels)) : 
        if(pixels[i]!=[0,0,0]) : 
            c = i
            break        

    print(a,b,c)    

    device.shell(f'input touchscreen swipe 500 500 500 500 {int(((b+c)/2-a)*0.98)}')

    time.sleep(2.5)
