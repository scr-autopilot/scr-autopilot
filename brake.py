import pydirectinput
import time
import pyttsx3
import sys
engine = pyttsx3.init()

def brake(speed, to, safemode):
    brakespd = speed - to
    sleeptime = 0
    print("Brake: ", brakespd)
    validspeeds = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 115, 120, 125]
    if brakespd in validspeeds:
        finalto = brakespd / 5
        finalto = int(finalto)
        print("FINALTO", finalto)
        for (i) in range(finalto):
            sleeptime += 1
            pydirectinput.keyDown("s")
            time.sleep(0.0680)
            pydirectinput.keyUp("s")
        #sleeptime = sleeptime * 1.2
        #time.sleep(sleeptime)
        return

    engine.say("Please calibrate the speed.")
    engine.runAndWait()
    if safemode == "1":
        engine.say(
            "Please take over immediately and stop the autopilot. Please take over immediately and stop the autopilot.")
        engine.runAndWait()
        pydirectinput.keyDown("s")
        time.sleep(3.5)
        pydirectinput.keyUp("s")
        engine.say("Autopilot unavailable.")
        engine.runAndWait()
        engine.say("Autopilot disengaged.")
        engine.runAndWait()
        sys.exit()
