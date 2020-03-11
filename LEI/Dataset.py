import pandas as pd


jester_train = pd.read_csv("data/jester-v1-train.csv", sep=";").to_numpy()
jester_validation = pd.read_csv("data/jester-v1-validation.csv", sep=";").to_numpy()

f = open("dataset.csv", "w")
f.write("FileName;Gesture\n")

for row_train in jester_train:
    for row_val in jester_validation:
        if row_val[0] == row_train[0]:
            print("Found one: " + str(row_train[0]))
