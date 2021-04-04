import pydirectinput
import time

def throttle(fromThrottle, toThrottle):
    throttleDiff = toThrottle - fromThrottle

    if toThrottle == 0:
        throttleDiff -= 5

    if throttleDiff > 0:
        key = "w"
    elif throttleDiff < -1:
        key = "s"
    else:
        return

    print("Throttle: ", throttleDiff)
    pressTime = abs( (throttleDiff / 5) * 0.16 )

    if -4 < throttleDiff < 0:
        pydirectinput.keyDown(key)
        pydirectinput.keyUp(key)
    else: 
        pydirectinput.keyDown(key)
        time.sleep(pressTime)
        pydirectinput.keyUp(key)
    return
