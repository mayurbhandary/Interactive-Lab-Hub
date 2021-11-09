import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import alsaaudio

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90


# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

m = alsaaudio.Mixer()
################################
wCam, hCam = 640, 480
################################
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
 
detector = htm.handDetector(detectionCon=0.7)
minVol = 0
maxVol = 100
vol = 0
volBar = 400
volPer = 0

sentence = []

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
 
        thumbX, thumbY = lmList[4][1], lmList[4][2] #thumb
        pointerX, pointerY = lmList[8][1], lmList[8][2] #pointer

        middleX, middleY = lmList[12][1], lmList[12][2]
        ringX, ringY = lmList[16][1], lmList[16][2]
        pinkyX, pinkyY = lmList[20][1], lmList[20][2]
        
        cx, cy = (thumbX + pointerX) // 2, (thumbY + pointerY) // 2
 
        cv2.circle(img, (thumbX, thumbY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (pointerX, pointerY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (middleX, middleY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (ringX, ringY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (pinkyX, pinkyY), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (thumbX, thumbY), (pointerX, pointerY), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        len_calc = lambda x1,y1,x2,y2: math.hypot(x2 - x1, y2 - y1)
        thumb_pointer = len_calc(thumbX,thumbY,pointerX,pointerY)
        pointer_middle = len_calc(pointerX,pointerY,middleX,middleY)
        middle_ring = len_calc(middleX, middleY, ringX, ringY)
        ring_pinky = len_calc(ringX, ringY, pinkyX, pinkyY)
        thumb_ring = len_calc(thumbX,thumbY, ringX, ringY)
        thumb_middle = len_calc(thumbX,thumbY, middleX, middleY)
        thumb_pinky = len_calc(thumbX,thumbY, pinkyX, pinkyY)

        print(pointer_middle,middle_ring,ring_pinky)

        condition_money = thumb_pointer<100 and thumb_middle>100 and thumb_ring>100 and thumb_pinky>100 and middle_ring>50 and ring_pinky>50
        
        if condition_money:
            if " money" not in sentence:
                sentence.append(" money")
            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'Money', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)

        condition_yes = thumb_pointer>100 and middle_ring<100 and ring_pinky<100 and pointer_middle>100

        if condition_yes:
            if "Yes" not in sentence:
                sentence.append("Yes")

            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'Yes', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)
        
        condition_love = thumb_pointer>100 and pointer_middle>100 and middle_ring<100 and ring_pinky>100
        if condition_love:
            if " I love you" not in sentence:
                sentence.append(" I love you")
            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'I love you', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)

        condition_i = thumb_pointer<100 and pointer_middle<100 and middle_ring<100 and thumb_pinky>100
        if condition_i:
            if " I am" not in sentence:
                sentence.append(" I am")
            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'I am', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)

        condition_fine = thumb_pointer>100 and pointer_middle<100 and middle_ring<100 and ring_pinky<100
        if condition_fine:
            if " fine" not in sentence:
                sentence.append(" fine")
            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'fine', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)

        condition_back = thumb_middle<100 and thumb_pointer < 100 and thumb_middle<100 and thumb_ring <100 and thumb_pinky <100
        if condition_back:
            if len(sentence) > 0:
                sentence.pop()

        else:
 
            vol = np.interp(thumb_pointer, [50, 300], [minVol, maxVol])
            volBar = np.interp(thumb_pointer, [50, 300], [400, 150])
            volPer = np.interp(thumb_pointer, [50, 300], [0, 100])
            m.setvolume(int(vol))

        print(int(thumb_pointer), vol)

 
        if thumb_pointer < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        
         # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
        draw.text((0, -2), "".join(sentence), font=font, fill="#FFFFFF")
        # Display image.
        disp.image(image, rotation)
 
    #cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    #cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    #cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
    #            1, (255, 0, 0), 3)
 
 
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
 
    cv2.imshow("Img", img)
    cv2.waitKey(1)