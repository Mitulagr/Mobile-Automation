from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

while True : 
    device.shell(f'input touchscreen swipe 800 540 800 540 1000 && input touchscreen swipe 1600 340 1600 340 1000 && input touchscreen swipe 1600 740 1600 740 1000')