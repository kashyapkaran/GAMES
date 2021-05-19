from ppadb.client import Client

adb = Client(host = '127.0.0.1',port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device Attached')
    quit

device = devices[0]
while True:
    device.shell('input touchscreen swipe 300 930 300 300 800')
    device.shell('input touchscreen tap 984 740')