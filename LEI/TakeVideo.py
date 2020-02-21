from cv2 import *
import numpy as np


def start_camera():
    cap = cv2.VideoCapture(0)
    w = 0

    while True:
        ret, frame = cap.read()
        gray = cv2.flip(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1)
        frame = cv2.flip(frame, 1)

        # x1 = (200, 100)
        # x2 = (310, 300)
        # color = (0, 255, 0)
        # cv2.rectangle(frame, x1, x2, color, 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


start_camera()
