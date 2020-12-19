import subprocess
#tablet screen size = 1920x1200
while True:
    subprocess.run('adb shell input touchscreen swipe 238 753 238 740 300')
    subprocess.run('adb shell input touchscreen swipe 891 838 891 838 1')