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
    t1 = time.time()
    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)

    image = Image.open('screen.png')

    image = numpy.array(image, dtype=numpy.uint8)

    hor = 10
    ver = 20
    c = (540,1010)
    le = (300,1200)
    ri = (780,1200)
    step = 10

    hor = hor//2
    ver = ver//2

    brk = False
    for i in range (-hor*step,hor*step,step) : 
        for j in range (-ver*step,ver*step,step) : 
            r = image[c[1]+j][c[0]+i][0]
            g = image[c[1]+j][c[0]+i][1]
            b = image[c[1]+j][c[0]+i][2]
            if(r>130 and r<140 and g>200 and g<210 and b>60 and b<80) :
                device.shell(f'input touchscreen tap 540 1200')
                brk = True
            if(brk) : break   
            r = image[le[1]+i][le[0]+j][0]
            g = image[le[1]+i][le[0]+j][1]
            b = image[le[1]+i][le[0]+j][2]
            if(r>130 and r<140 and g>200 and g<210 and b>60 and b<80) :
                device.shell(f'input touchscreen tap 540 1200')
                brk = True
            if(brk) : break  
            r = image[ri[1]+i][ri[0]+j][0]
            g = image[ri[1]+i][ri[0]+j][1]
            b = image[ri[1]+i][ri[0]+j][2]
            if(r>130 and r<140 and g>200 and g<210 and b>60 and b<80) :
                device.shell(f'input touchscreen tap 540 1200')
                brk = True
            if(brk) : break   
        if(brk) : break   
    print(time.time()-t1)
        
