import subprocess
#tablet screen size = 1920x1200
while True:
    subprocess.call('adb shell input touchscreen swipe 1736 873 1736 873 200')
    subprocess.call('adb shell input touchscreen swipe 891 838 891 838 1')
