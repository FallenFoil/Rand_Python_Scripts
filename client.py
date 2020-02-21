import socket
from cv2 import *
import pickle

def simple_client():
    s = socket.socket()
    s.connect(('127.0.0.1', 12345))

    # size = int(s.recv(512).decode())

    while True:
        frame = pickle.loads(s.recv(921764))

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    s.close()


simple_client()
