# Yes, I know, that this code is messy. If you want to help with formatting this, you can write me at maty-mt@protonmail.com, but I will not format this code yet.

import numpy as nm
import pytesseract
import re
import pydirectinput
import time
import cv2
import math
from PIL import ImageGrab
from PIL import ImageFilter
import sched
import sys
# import tkinter as tk
# from tkinter import ttk
from throttle import *
import requests

print("SCR-Autopilot v0.2.2-beta by MaTY (matyroblox01)")
print("Checking for updates...")
URL = "https://matyapi.matymt.repl.co/scr-autopilot/newest-version"
r = requests.get(url=URL)
data = r.json()
version = data['version']
if not version == "0.2.2":
    print("Your version is outdated! Please install the latest release on https://github.com/MaTY-MT/scr-autopilot/releases")
else:
    print("Your version is up-to-date.")
input("By using this software, you agree, that if the software makes a fault, you are always ready to take over. We are not responsible for any penalties given to your account! It is highly reccomended to use this software only on VIP servers, yet. This software is not an exploit (confirmed by the SCR staff team) and you can use it freely. Press ENTER to continue.")

# window = tk.Tk()
# window.title("SCR-Autopilot (scr-autopilot.mmaty.eu)")
# window.minsize(600, 400)
# spd_label = ttk.Label(window, text="Please check the cmd to get informations.")
# lim_label = ttk.Label(window, text="")
# signal_label = ttk.Label(window, text="")
# spd_label.grid(column=0, row=0)
# lim_label.grid(column=0, row=1)
# signal_label.grid(column=0, row=2)

resolution = input("What is the resolution? (fhd, hd) > ")
if resolution == "fhd":
    spd_pos = 884, 957, 947, 985
    lim_pos = 889, 987, 942, 1016
    green_pos = 1440, 983, 1441, 984
    yellow_pos = 1438, 1016, 1439, 1017
    double_yellow_pos = 1438, 950, 1439, 951
    red_pos = 1438, 1045, 1439, 1046
    distance_pos = 555, 1046, 605, 1070
    awsbutton_pos = 1364, 960, 1365, 961
    throttle_pos = 843, 931, 845, 1074
elif resolution == "hd":
    print("The autopilot can be a little more buggy because of the HD resolution.")
    time.sleep(1)
    spd_pos = 573, 594, 630, 630
    lim_pos = 569, 627, 618, 653
    green_pos = 1118, 624, 1119, 625
    yellow_pos = 1120, 654, 1121, 655
    double_yellow_pos = 1120, 590, 1121, 591
    red_pos = 1120, 688, 1121, 689
    distance_pos = 239, 686, 284, 708
    awsbutton_pos = 1047, 597, 1048, 598
    throttle_pos = 522, 570, 525, 713
else:
    print('Hmm, the resolution is not right... Try it again. Please type only "fhd" (without the quotation marks) if you have FHD monitor, or type "hd" (without the quotation marks) if you have HD monitor.')
    input("Press ENTER to close the program.")
    sys.exit()

max_speed = int ( input("What is the maximum speed of your train in MPH? (E.g. 100, 125, 75 etc.) > ") )


def main(lim=None):

    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract.exe'

    s = sched.scheduler(time.time, time.sleep)

    def mainrun(sc):
        im = ImageGrab.grab(bbox=(awsbutton_pos))
        pix = im.load()
        awsbutton_value = pix[0, 0]  # Set the RGBA Value of the image (tuple)
        print(awsbutton_value)
        if not awsbutton_value == (0, 0, 0):
            pydirectinput.keyDown("q")
            pydirectinput.keyUp("q")
            print("AWSBUTTON:", "clicked")

        cap = ImageGrab.grab(bbox=(845, 933, 845, 1071))
        pix = im.load()
        awsbutton_value = pix[0, 0]  # Set the RGBA Value of the image (tuple)
        print(awsbutton_value)
        cap = ImageGrab.grab(bbox=(throttle_pos))
        img = cap
        count = 0
        for y in range(img.height):
            for x in range(img.width):
                pixel = img.getpixel((x,y))
                if pixel == (0, 176, 85):
                    count+=1
        
        currentThrottle = int( math.floor( 100 * (count / 142) ) )
        speed = currentThrottle/100 * max_speed

        print("Current throttle: ",currentThrottle)

        #print(count,"pixels are green.")
        if currentThrottle == None:
            print("I can't read the throttle.")
            
        else:
            # LIMIT
            cap = ImageGrab.grab(bbox=(lim_pos))
            cap = cap.filter(ImageFilter.MedianFilter())
            cap = cv2.cvtColor(nm.array(cap), cv2.COLOR_RGB2GRAY)
            tesstr = pytesseract.image_to_string(
                cap,
                config="--psm 7")
            lim = 0
            lim = [int(s) for s in re.findall(r'\b\d+\b', tesstr)]
            if lim == []:
                print("I can't read the limit.")
            else:
                templim = lim[0]
                lim = lim[0]
                lim = int(lim)
                im = ImageGrab.grab(bbox=(red_pos))
                pix = im.load()
                # Set the RGBA Value of the image (tuple)
                red_value = pix[0, 0]
                im = ImageGrab.grab(bbox=(yellow_pos))
                pix = im.load()
                # Set the RGBA Value of the image (tuple)
                yellow_value = pix[0, 0]
                im = ImageGrab.grab(bbox=(green_pos))
                pix = im.load()
                # Set the RGBA Value of the image (tuple)
                green_value = pix[0, 0]
                im = ImageGrab.grab(bbox=(double_yellow_pos))
                pix = im.load()
                # Set the RGBA Value of the image (tuple)
                double_yellow_value = pix[0, 0]
                if red_value == (255, 0, 0):
                    print("AWS:", "red")
                    lim = 0
                if yellow_value == (255, 190, 0):
                    print("AWS:", "yellow")
                    if templim > 45:
                        lim = 45
                if double_yellow_value == (255, 190, 0):
                    print("AWS:", "double_yellow")
                    if templim > 75:
                        lim = 75
                if green_value == (0, 255, 0):
                    print("AWS:", "green")

                print("Limit: ", lim)
                limitThrottle = int( (lim / max_speed) * 100 )

                print("Limit throttle: ",limitThrottle)

                cap = ImageGrab.grab(bbox=(distance_pos))
                cap = cap.filter(ImageFilter.MedianFilter())
                cap = cv2.cvtColor(nm.array(cap), cv2.COLOR_RGB2GRAY)
                tesstr = pytesseract.image_to_string(
                    cap,
                    config="--psm 7")
                distance = 0
                distance = [int(s) for s in re.findall(r'\b\d+\b', tesstr)]
                try:
                    m_distance = distance[0]
                    distance = distance[1]
                    if distance <= 50 and distance >= 39 and m_distance == 0:
                        print(
                            "Autopilot will will be disengaged 0.2 miles before the station.")
                    elif distance <= 20 and m_distance == 0:
                        if lim >= 45:
                            print("Slowing down to 45 to prepare for station arrival.")
                            throttle(currentThrottle, int( (45 / max_speed) * 100 ))
                        else:
                            throttle(currentThrottle, limitThrottle)
                        print("Autopilot disengaged.")
                        input("Press enter to engage.")
                        print("Autopilot engaged.")
                        time.sleep(1)
                    else:
                        throttle(currentThrottle, limitThrottle)
                except IndexError:
                    print("Can't read the distance!")

        # END_LIMIT
        s.enter(1, 1, mainrun, (sc,))

    s.enter(1, 1, mainrun, (s,))
    s.run()


time.sleep(1)
# Calling the function
print("Autopilot engaged.")
main()

