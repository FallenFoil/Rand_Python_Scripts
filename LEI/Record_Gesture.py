import time
from cv2 import *


def delete_all_pictures():
    archives = os.listdir(os.path.expanduser("Fotos"))
    for archive in archives:
        os.remove("Fotos/" + archive)


def take_pictures():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    start = time.time()
    i = 0
    w = 0

    while i <= 1:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if w < 10:
            imwrite("Fotos/0" + str(w) + ".jpg", cv2.flip(gray, 1))
        else:
            imwrite("Fotos/" + str(w) + ".jpg", cv2.flip(gray, 1))
        w += 1
        i = time.time() - start

    cap.release()
    cv2.destroyAllWindows()


def delete_odd_picture():
    archives = os.listdir(os.path.expanduser("Fotos"))
    odd = False

    for archive in archives:
        print(archive)
        if odd:
            odd = False
            os.remove("Fotos/" + archive)
        else:
            odd = True


delete_all_pictures()
take_pictures()
# delete_odd_picture()
