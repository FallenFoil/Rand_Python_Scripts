import os
import cv2
import numpy as np


def join_frame(path):
    if os.path.isfile("data/remove.txt"):
        f = open("data/remove.txt", "w")
    else:
        f = open("data/remove.txt", "xw")

    folder = os.listdir(os.path.expanduser(path))

    first = 0
    first_window = -1
    first_set = []
    second_set = []

    is_first = True

    for i in range(len(folder)):
        for img in os.listdir(os.path.expanduser(f"{path}/{i}/")):
            image = cv2.imread(f"{path}/{i}/{img}")
            image = cv2.resize(image, (0, 0), None, .3, .3)

            if is_first:
                first_set.append(image)
            else:
                second_set.append(image)

        if is_first:
            is_first = False
            cv2.imshow(f"{i}", np.concatenate(first_set, axis=1))
        else:
            cv2.imshow(f"{i}", np.concatenate(second_set, axis=1))
            k = cv2.waitKey(0) & 0xFF
            cv2.destroyWindow(f"{first_window}")
            if k == ord('m'):
                f.write(f"{path}/{i}\n")
                for img in os.listdir(os.path.expanduser(f"{path}/{i}/")):
                    os.replace(f"{path}/{i}/{img}", f"{path}/{first}/{img}")
            else:
                first = i

            is_first = False
            first_set = second_set
            second_set = []

        first_window += 1

    f.close()


def operate_folder(od, path, param_no_gesture_folder, param_gesture_folder):
    folder = os.listdir(os.path.expanduser(path))
    no_gesture_folder = param_no_gesture_folder
    gesture_folder = param_gesture_folder

    for aux in folder:
        inner_folder = os.listdir(os.path.expanduser(f"{path}/{aux}"))

        for image in inner_folder:
            img = cv2.imread(f"{path}/{aux}/{image}", 1)
            cv2.imshow(image, img)

            k = cv2.waitKey(0) & 0xFF

            if k == ord('g'):
                if not os.path.isdir(f"data/{od}/{aux}"):
                    os.mkdir(f"data/{od}/{aux}")
                os.replace(f"{path}/{aux}/{image}", f"data/{od}/{aux}/{image}")
            elif k == ord('n'):
                if not os.path.isdir(f"data/no_gesture/{no_gesture_folder}"):
                    os.mkdir(f"data/no_gesture/{no_gesture_folder}")
                os.replace(f"{path}/{aux}/{image}", f"data/no_gesture/{no_gesture_folder}/{image}")

            cv2.destroyAllWindows()

        no_gesture_folder += 1
        gesture_folder += 1

    print(no_gesture_folder)


def delete_empty_folders(path, func_type=1):
    if func_type == 0:
        file = open(path, 'r')
        lines = file.readlines()
        path_complement = ""
    else:
        lines = os.listdir(os.path.expanduser(path))
        path_complement = path + "/"

    for line in lines:
        try:
            os.rmdir(path_complement + line.strip())
        except:
            print(f"{path} doesn't exist or is not empty")


def clean_folders(path, max_folder):
    name = 0
    for i in range(max_folder + 1):
        if os.path.isdir(f"{path}/{i}"):
            os.rename(f"{path}/{i}", f"{path}/{name}")
            name += 1


# operate_folder("swipe", "data/gui-swipe1", 92, 0)

# operate_folder("minimize", "data/gui-minimize2", 146, 15)
# operate_folder("scale", "data/gui-scale2", , 18)
# operate_folder("swipe", "data/gui-swipe2", , )

# delete_empty_folders("data/gui-swipe1")
clean_folders("data/swipe", 53)

