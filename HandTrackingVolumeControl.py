import cv2
import numpy as np
import time
import math
import HandTrackingModule as htm
#########################
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#########################
# volume.GetMute()
# volume.GetMasterVolumeLevel()

#volume.SetMasterVolumeLevel(0, None)
#########################
wCam, hCam = 640, 480
#########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.HandsDetector(detectionCon=0.9, trackCon=0.9)
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
while True:
    success, img = cap.read()
    img = detector.FindHands(img)
    lmList = detector.FindPosition(img, draw=False)
    if len(lmList) != 0:
        # To Draw on Hands
        xThumb, yThumb = lmList[4][1], lmList[4][2]
        xIndex, yIndex = lmList[8][1], lmList[8][2]
        xMidDistance, yMidDistance = (xThumb+xIndex)//2, (yThumb+yIndex)//2
        cv2.circle(img, (xThumb, yThumb), 10, (125, 0, 255), cv2.FILLED)
        cv2.circle(img, (xIndex, yIndex), 10, (125, 0, 255), cv2.FILLED)
        cv2.line(img, (xThumb, yThumb), (xIndex, yIndex), (125, 0, 255), 3)
        cv2.circle(img, (xMidDistance, yMidDistance), 10, (125, 0, 255), cv2.FILLED)

        # To calculate length of the line which connect index to thumb
        length = math.hypot(xIndex - xThumb, yIndex - yThumb)

        # HandRange 30 - 150
        # VolumeRange -65 - 0
        # vol is the corresponding value for range [minVol-maxVol] of length in range[30-150]
        vol = np.interp(length, [30, 150], [minVol, maxVol])
        print(int(length), vol)

        volume.SetMasterVolumeLevel(vol, None)

        volBar = np.interp(length, [30, 150], [400, 150])


    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
