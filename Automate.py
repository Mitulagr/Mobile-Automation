from ppadb.client import Client
import time
from PIL import Image
import numpy

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

device = devices[0]

def isOff() : 
    image = device.screencap()
    with open('screen.png', 'wb') as f: f.write(image) 
    try : 
        image = Image.open('screen.png')
        image = numpy.array(image, dtype=numpy.uint8)
    except : return False    
    s = 0 
    for i in image : 
        for j in i : 
            s = s + j[0] + j[1] + j[2]
    if(s==0) : return True 
    else : return False 

def isOn() : 
    return not isOff()    

def off() : 
    device.shell(f'input keyevent 26')      

def on() : 
    device.shell(f'input keyevent 26')    

def home() : 
    device.shell(f'input keyevent 3')

def back() : 
    device.shell(f'input keyevent 4')

def left() :
    device.shell(f'input touchscreen swipe 640 1200 440 1200 100')

def right() :
    device.shell(f'input touchscreen swipe 440 1200 640 1200 100')

def up() :
    device.shell(f'input touchscreen swipe 540 1400 540 1000 100')

def down() : 
    device.shell(f'input touchscreen swipe 540 1000 540 1400 100')

def tap(x,y) : 
    device.shell(f'input touchscreen tap {x} {y}') 

def swipe(x1,y1,x2,y2,t) : 
    device.shell(f'input touchscreen swipe {x1} {y1} {x2} {y2} {t}')    

def long_press(x,y,t):     
    device.shell(f'input touchscreen swipe {x} {y} {x} {y} {t}')  

def sc() :
    image = device.screencap()
    with open('screen.png', 'wb') as f: f.write(image)

def app(r,c,p=None) :
    if p is not None : 
        home()
        home()
        for i in range (p) : left()    
    device.shell(f'input touchscreen tap {-70+c*204} {-72+r*364}')

def type (s) : 
    s2 = ''
    for i in s : s2 = s2 + '\\' + i   
    device.shell(f'input text {s2}')

def keyevent(n) : 
    device.shell(f'input keyevent {n}')

def volume_up() : 
    device.shell(f'input keyevent 24')

def volume_down() : 
    device.shell(f'input keyevent 25')

def pause() : 
    device.shell(f'input keyevent 85') 

def play() : 
    device.shell(f'input keyevent 85') 

def next() : 
    device.shell(f'input keyevent 87') 

def prev() : 
    device.shell(f'input keyevent 88')  

def enter() : 
    device.shell(f'input keyevent 66')  

def wa_send() : 
    image = device.screencap()
    with open('screen.png', 'wb') as f: f.write(image) 
    image = Image.open('screen.png')
    image = numpy.array(image, dtype=numpy.uint8)
    if(image[2303][540][1]==0) : 
        device.shell(f'input touchscreen tap 996 1487')
    else :    
        device.shell(f'input touchscreen tap 996 2330')

#============================================================================== 

def inshorts() : 
    if isOff() : on()
    app(2,1,2)
    while True : 
        image = device.screencap()
        with open('screen.png', 'wb') as f: f.write(image) 
        image = Image.open('screen.png')
        image = numpy.array(image, dtype=numpy.uint8)
        if(image[1200][13][1]==255 and image[1500][13][1]==255 and image[1800][13][1]==255 and image[2100][540][1]==255) : 
            time.sleep(15)
            up()
        else : up()

def inshorts_open() :
    if isOff() : on()
    app(2,1,2)

def inshorts_swipe() : 
    image = device.screencap()
    with open('screen.png', 'wb') as f: f.write(image) 
    image = Image.open('screen.png')
    image = numpy.array(image, dtype=numpy.uint8)
    if(image[1200][13][1]==255 and image[1500][13][1]==255 and image[1800][13][1]==255 and image[2100][540][1]==255) : return True
    else : return False

def prime_video(s) : 
    if(s=="next") : 
        tap(1870,540) 
        tap(1433,540)
        tap(1870,540) 
        return None
    if(s=="prev") : 
        tap(1870,540) 
        tap(967,540)  
        tap(1870,540) 
        return None
    if(s=="pause") : 
        tap(1870,540) 
        tap(1200,540)    
        return None 
    if(s=="play") : 
        tap(1200,540)    
        return None      
    if isOff() : on()
    app(5,1,1)

    time.sleep(0.5)
    image = device.screencap()
    with open('screen.png', 'wb') as f: f.write(image) 
    try : 
        image = Image.open('screen.png')
        image = numpy.array(image, dtype=numpy.uint8)
    except : swipe(2390,540,2000,540,100) 

    tap(408,2330)
    tap(394,292)
    type(s)
    tap(982,2189)
    tap(604,578)
    tap(560,1090)
    time.sleep(1)
    tap(2182,63) 
    time.sleep(0.1)
    tap(780,447)
    tap(1780,705)  
    tap(1870,540) 

def gaana(s) : 
    if isOff() : on()
    app(5,3,1)
    time.sleep(0.5)
    tap(480,240)
    tap(480,180)
    type(s)
    tap(995,2186)
    time.sleep(0.5)
    tap(380,524)
    time.sleep(0.5)
    home()
    off()

def spotify(s) : 
    if isOff() : on()
    app(5,4,1)
    time.sleep(1.2)
    tap(350,2300)
    tap(520,500)
    type(s)
    tap(995,2186)
    time.sleep(0.5)
    tap(540,400)
    home()
    off()    

inshorts()    

#def ball_pool () : 

    # Top of Stick : (210,350)
    # Black Line 1 : (210,380)
    # Black Line 2 : (210,500) 
    # Black Line 3 : (210,620)
    # Black Line 4 : (210,740) 
    # Black Line 5 : (210,850)

    # Center : (1260,620)
    # Height = 730
    # Width = 1460


#==============================================================================         

#spotify("Legends Never Die")
#swipe(1260,620,1990,255,1000)
#swipe(2100,200,2100,1000,621)
#swipe(210,350,210,850,5000)


