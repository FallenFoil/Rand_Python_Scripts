import pandas as pd
import numpy as np


def get_full_path(val):
    if 1 <= val <= 10000:
        if val <= 5000:
            return "1-10000/1-5000/" + str(val)
        else:
            return "1-10000/5001-10000/" + str(val)
    elif 10001 <= val <= 20000:
        if val <= 15000:
            return "10001-20000/10001-15000/" + str(val)
        else:
            return "10001-20000/50001-20000/" + str(val)
    elif 20001 <= val <= 30000:
        if val <= 25000:
            return "20001-30000/20001-25000/" + str(val)
        else:
            return "20001-30000/25001-30000/" + str(val)
    elif 30001 <= val <= 40000:
        if val <= 35000:
            return "30001-40000/30001-35000/" + str(val)
        else:
            return "30001-40000/35001-40000/" + str(val)
    elif 40001 <= val <= 50000:
        if val <= 45000:
            return "40001-50000/40001-45000/" + str(val)
        else:
            return "40001-50000/45001-50000/" + str(val)
    elif 50001 <= val <= 60000:
        if val <= 55000:
            return "50001-60000/50001-55000/" + str(val)
        else:
            return "50001-60000/55001-60000/" + str(val)
    elif 60001 <= val <= 70000:
        if val <= 65000:
            return "60001-70000/60001-65000/" + str(val)
        else:
            return "60001-70000/65001-70000/" + str(val)
    elif 70001 <= val <= 80000:
        if val <= 75000:
            return "70001-80000/70001-75000/" + str(val)
        else:
            return "70001-80000/75001-80000/" + str(val)
    elif 80001 <= val <= 90000:
        if val <= 85000:
            return "80001-90000/80001-85000/" + str(val)
        else:
            return "80001-90000/85001-90000/" + str(val)
    elif 90001 <= val <= 100000:
        if val <= 95000:
            return "90001-100000/90001-95000/" + str(val)
        else:
            return "90001-100000/95001-100000/" + str(val)
    elif 100001 <= val <= 110000:
        if val <= 105000:
            return "100001-110000/100001-105000/" + str(val)
        else:
            return "100001-110000/105001-110000/" + str(val)
    elif 110001 <= val <= 120000:
        if val <= 115000:
            return "110001-120000/110001-115000/" + str(val)
        else:
            return "110001-120000/115001-120000/" + str(val)
    elif 120001 <= val <= 130000:
        if val <= 125000:
            return "120001-130000/120001-125000/" + str(val)
        else:
            return "120001-130000/125001-130000/" + str(val)
    elif 130001 <= val <= 140000:
        if val <= 135000:
            return "130001-140000/130001-135000/" + str(val)
        else:
            return "130001-140000/135001-140000/" + str(val)
    elif 140001 <= val <= 148092:
        return "140001-148092/" + str(val)


def write2file(file):
    f = open(file, "w")

    f.write("FileName;Gesture\n")
    for i in range(5089):
        f.write(get_full_path(desiredTrain[i]) + ";" + desiredLabels[labels[i]] + "\n")

    f.close()


Train = pd.read_csv("data/jester-v1-validation.csv", sep=";").to_numpy()

desiredLabels = np.array(["No gesture", "Doing other things", "Swiping Down", "Swiping Right", "Swiping Left", "Zooming In With Full Hand", "Zooming Out With Full Hand", "Stop Sign"])

desiredTrain = np.zeros((5089,), dtype=int)
labels = np.zeros((5089,), dtype=int)
w = 0
for row in Train:
    if np.isin(row[1], desiredLabels):
        desiredTrain[w] = row[0]

        if row[1] == desiredLabels[0]:
            labels[w] = 0
        elif row[1] == desiredLabels[1]:
            labels[w] = 1
        elif row[1] == desiredLabels[2]:
            labels[w] = 2
        elif row[1] == desiredLabels[3]:
            labels[w] = 3
        elif row[1] == desiredLabels[4]:
            labels[w] = 4
        elif row[1] == desiredLabels[5]:
            labels[w] = 5
        elif row[1] == desiredLabels[6]:
            labels[w] = 6
        elif row[1] == desiredLabels[7]:
            labels[w] = 7

        w += 1

write2file("Train.csv")
