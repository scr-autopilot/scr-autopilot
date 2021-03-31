import pydirectinput
import time
import pyttsx3
engine = pyttsx3.init()

def throttle(fromThrottle, toThrottle):
    throttleDiff = toThrottle - fromThrottle

    if toThrottle == 0:
        throttleDiff -= 5

    if throttleDiff > 0:
        key = "w"
    elif throttleDiff < -3:
        key = "s"
    else:
        return

    print("Throttle: ", throttleDiff)
    pressTime = abs( (throttleDiff / 5) * 0.16 )

    pydirectinput.keyDown(key)
    time.sleep(pressTime)
    pydirectinput.keyUp(key)
    return