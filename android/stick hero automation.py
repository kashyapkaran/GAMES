from ppadb.client import Client
# Default is "127.0.0.1" and 5037
adb = Client(host=" 192.168.1.4", port=5037)
devices = adb.devices()
if len(devices) == 0:
    print('no devices attached')
    quit()

device = devices[0]
device.shell('input touchscreen swipe 500 500 500 500 200')