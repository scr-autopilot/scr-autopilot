import playsound
import pydirectinput
import time
import pyttsx3
import sys
engine = pyttsx3.init()

def throttle(speed, to, safemode):
    if to == 125:
        to = 100
    throttlespd = to - speed
    sleeptime = 0
    print("Throttle: ", throttlespd)
    validspeeds = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 115, 120, 125]
    if throttlespd in validspeeds:
        finalto = throttlespd / 5
        finalto = int(finalto)
        print("FINALTO", finalto)
        for (i) in range(finalto):
            sleeptime += 1
            pydirectinput.keyDown("w")
            time.sleep(0.0680)
            pydirectinput.keyUp("w")
        sleeptime = sleeptime * 1.3
        time.sleep(sleeptime)
        return

    playsound.playsound("./sounds/warning.mp3")
    if safemode == "1":
        engine.say(
            "Please take over immediately and stop the autopilot. Please take over immediately and stop the autopilot.")
        engine.runAndWait()
        pydirectinput.keyDown("s")
        time.sleep(3.5)
        pydirectinput.keyUp("s")
        playsound.playsound("./sounds/beeps.mp3")
        engine.say("Autopilot unavailable.")
        engine.runAndWait()
        playsound.playsound("./sounds/AutopilotEnd.mp3")
        sys.exit()