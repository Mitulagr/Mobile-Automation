from ppadb.client import Client
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

device = devices[0]

def home() : 
    device.shell(f'input touchscreen swipe 540 2380 540 2000 100')

def back() : 
    device.shell(f'input touchscreen swipe 1070 1200 850 1200 100')

def left() :
    device.shell(f'input touchscreen swipe 640 1200 440 1200 100')

def right() :
    device.shell(f'input touchscreen swipe 440 1200 640 1200 100')

def up() :
    device.shell(f'input touchscreen swipe 540 1300 540 1100 100')

def down() : 
    device.shell(f'input touchscreen swipe 4540 1100 540 1300 100')

def sc() :
    image = device.screencap()
    with open('screen.png', 'wb') as f: f.write(image)

def open(r,c,p=None) :
    if p is not None : 
        home()
        home()
        for i in range (p) : left()    
    device.shell(f'input touchscreen tap {-70+c*204} {-72+r*364}')

def inshorts() : 
    open(2,1,2)

device.shell(f'input keyevent 3')  