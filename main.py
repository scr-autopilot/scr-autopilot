# Yes, I know, that this code is messy. If you want to help with formatting this, you can write me at maty-mt@protonmail.com, but I will not format this code yet.

import numpy as nm
import pytesseract
import re
import pydirectinput
import time
import cv2
from PIL import ImageGrab
from PIL import ImageFilter
import sched
import pyttsx3
import sys
from PIL import ImageEnhance
from PIL import Image
import tkinter as tk
from tkinter import ttk
from throttle import *
from brake import *

input("By using this software, you agree, that if the software makes a fault, you are always ready to take over. We are not responsible for any penalties given to your account! It is highly reccomended to use this software only on VIP servers, yet. This software is not an exploit (confirmed by the SCR staff team) and you can use it freely. Press ENTER to continue.")
window = tk.Tk()
engine = pyttsx3.init()
window.title("SCR-Autopilot (scr-autopilot.mmaty.eu)")
window.minsize(600,400)
spd_label = ttk.Label(window, text = "Please check the cmd to get informations.")
lim_label = ttk.Label(window, text = "")
signal_label = ttk.Label(window, text = "")
spd_label.grid(column = 0, row = 0)
lim_label.grid(column = 0, row = 1)
signal_label.grid(column = 0, row = 2)
safemode = input("Enable safe mode? (0 = no; 1 = yes) > ")
resolution = input("What is the resolution? (fhd, hd) > ")
if resolution == "fhd":
    spd_pos = 884,957,947,985
    lim_pos = 889, 987, 942, 1016
    green_pos = 1440,983,1441,984
    yellow_pos = 1438,1016,1439,1017
    double_yellow_pos = 1438,950,1439,951
    red_pos = 1438,1045,1439,1046
    distance_pos = 555,1046,605,1070
    awsbutton_pos = 1364,960,1365,961
elif resolution == "hd":
    print("The autopilot can be a little more buggy because of the HD resolution.")
    time.sleep(1)
    spd_pos = 573,594,630,630
    lim_pos = 569,627,618,653
    green_pos = 1118,624,1119,625
    yellow_pos = 1120,654,1121,655
    double_yellow_pos = 1120,590,1121,591
    red_pos = 1120,688,1121,689
    distance_pos = 239,686,284,708
    awsbutton_pos = 1047,597,1048,598
else:
    print('Hmm, the resolution is not right... Try it again. Please type only "fhd" (without the quotation marks) if you have FHD monitor, or type "hd" (without the quotation marks) if you have HD monitor.')
    input("Press ENTER to close the program.")
    sys.exit()


def main(lim=None):
    
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract.exe'

    s = sched.scheduler(time.time, time.sleep)

    def mainrun(sc):
        im = ImageGrab.grab(bbox=(awsbutton_pos))
        pix = im.load()
        awsbutton_value = pix[0,0]  # Set the RGBA Value of the image (tuple)
        print(awsbutton_value)
        if not awsbutton_value == (0, 0, 0):
            pydirectinput.keyDown("q")
            pydirectinput.keyUp("q")
            print("AWSBUTTON:", "clicked")
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
                engine.say("Autopilot will will be disengaged 0.2 miles before the station.")
                engine.runAndWait()
            if distance <= 20 and m_distance == 0:
                engine.say("Autopilot disengaged.")
                engine.runAndWait()
                input("Press enter to engage.")
                engine.say("Autopilot engaged.")
                engine.runAndWait()
        except:
            print("Can't read the distance!")
        cap = ImageGrab.grab(bbox=(spd_pos))
        cap = cap.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(cap)
        cap = enhancer.enhance(2)
        cap = cv2.cvtColor(nm.array(cap), cv2.COLOR_RGB2HSV)
        c_h,c_s,c_v = cv2.split(cap)
        cap = cv2.threshold(c_v, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        cv2.imshow("Speed", cap)
        cv2.resizeWindow("Speed", 200, 200)
        cv2.waitKey(1)
        tesstr = pytesseract.image_to_string(
            cap,
            config="--psm 6 digits")
        speed = 0
        speed = [int(s) for s in re.findall(r'\b\d+\b', tesstr)]

        if speed == []:
            spd_label.configure(text= '?')
            engine.say("I can't read the speed.")
            engine.runAndWait()
        else:
            speed = speed[0]
            speed = int(speed)
            print("Speed: ", speed)
            # END_SPEED
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
                engine.say("I can't read the limit.")
                engine.runAndWait()
            else:
                templim = lim[0]
                lim = lim[0]
                lim = int(lim)
                im = ImageGrab.grab(bbox=(red_pos))
                pix = im.load()
                red_value = pix[0,0]  # Set the RGBA Value of the image (tuple)
                im = ImageGrab.grab(bbox=(yellow_pos))
                pix = im.load()
                yellow_value = pix[0,0]  # Set the RGBA Value of the image (tuple)
                im = ImageGrab.grab(bbox=(green_pos))
                pix = im.load()
                green_value = pix[0,0]  # Set the RGBA Value of the image (tuple)
                im = ImageGrab.grab(bbox=(double_yellow_pos))
                pix = im.load()
                double_yellow_value = pix[0,0]  # Set the RGBA Value of the image (tuple)
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
                if speed < lim:
                    throttle(speed, lim, safemode)
                if lim < speed:
                    brake(speed, lim, safemode)
        # END_LIMIT
        s.enter(1, 1, mainrun, (sc,))

    s.enter(1, 1, mainrun, (s,))
    s.run()

def test():
    pass
time.sleep(1)
#test()


# Calling the function
engine.say("Autopilot engaged.")
engine.runAndWait()
main()


# TODO: POZICE SE MĚNÍ SCALE SIZEM
