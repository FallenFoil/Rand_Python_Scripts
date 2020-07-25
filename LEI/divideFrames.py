import os
import shutil
import numpy as np

folder = "data/gui-swipe2/"

archives = os.listdir(os.path.expanduser(folder))
folder_name = 0

top_folders = int(np.ceil(len(archives)/12))

for i in range(top_folders):
    os.mkdir(folder + str(i))

w = 1
for archive in archives:
    if w == 13:
        folder_name += 1
        w = 1
    shutil.move(folder + archive, folder + str(folder_name))
    w += 1

