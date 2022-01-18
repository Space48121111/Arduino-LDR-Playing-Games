#pip install pyautogui
#pip install pyserial

import time
import pyautogui
import serial
import subprocess
import webbrowser

subprocess.call([r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','-new-tab','http://chromedino.com'])

#chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome %s'
#url = chrome://dino
#subprocess.Popen(['google-chrome'])
#webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("chrome_path"))
#webbrowser.get('google-chrome').open_new(chrome://)
#new=2, autoraise=True)

time.sleep(1)

usb_port = '/dev/cu.usbmodem14102'
port = serial.Serial(usb_port, 9600, timeout = 1)
#port.baudrate = '9600'
port.reset_input_buffer()
print(port.name)
print('Connected.')
# port.close()

while True:
    if port.in_waiting > 0: #data available
        data = port.readline()
        print(data) #'1\r\n'
        time.sleep(1)
        if data:
            datavalue = int(data.decode('utf-8').rstrip)
            #utf-8 to str to int
            if datavalue==1:
                print('1')
                pyautogui.press('up')
