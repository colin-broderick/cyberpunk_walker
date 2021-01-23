import numpy as np
import cv2
import time
import pyscreenshot as grab
from pynput.keyboard import Key
from pynput.keyboard import Controller as ControllerK
from pynput.mouse import Controller as ControllerM
from pynput.mouse import Button

keyboard = ControllerK()
mouse = ControllerM()

def grab_region(region):
    return grab.grab(bbox=region)

def save_img(img):
    img.save("img.png")

#time.sleep(5)
#img = grab_region((1630, 50, 1850, 173))
#save_img(img)

WMIN = np.array([75, 150, 150],np.uint8)
WMAX = np.array([150, 255, 255],np.uint8)

YMIN = np.array([0, 0, 0],np.uint8)
YMAX = np.array([75, 255, 255],np.uint8)

REGION = (1650, 130, 1830, 173)

CENTRE = 90

# img = cv2.imread("im.png")#, cv2.COLOR_RGB2HSV)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img = cv2.inRange(img, MIN, MAX)

# matches = np.argwhere(img == 255)
# avg = np.mean(matches[:, 1])

# #if avg > 120, turn right
# #if avg < 120, turn left
# #if avg == 120, do nothing

# cv2.imwrite("im2.png", img)

def send_walk_key():
    keyboard.press('w')

def avg_pos(img):
    return np.mean(np.argwhere(cv2.inRange(cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2HSV), YMIN, YMAX) == 255)[:, 1])

def turn_right(by):
    mouse.move(5*by, 0)

def turn_left(by):
    mouse.move(5*by, 0)

def do_walk():
    time.sleep(5)
    send_walk_key()
    time.sleep(0.5)
    index = 0
    while index < 20:
        img = grab_region(REGION)
        avg = avg_pos(img)
        if avg > CENTRE:
            turn_right(avg-CENTRE)
            print("turning right")
        elif avg == CENTRE:
            pass
        elif avg < CENTRE:
            turn_left(avg-CENTRE)
            print("turning left")
        # index += 1

def colour_seek():
    time.sleep(5)
    img = grab_region(REGION)
    img.save("img.png")
    img = cv2.imread("img.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img = cv2.inRange(img, YMIN, YMAX)
    cv2.imwrite("img2.png", img)

    


if __name__ == "__main__":
    do_walk()
    # colour_seek()