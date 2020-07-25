# Brute forces for the best combination of points to buy in Valorant

points = {
    500: 5.49,
    1150: 11.99,
    2150: 21.99,
    4400: 43.99,
    5500: 53.99,
    10500: 99.99,
}

pontos = 7100
res = []

for key1, value1 in points.items():
    if key1 >= pontos:
        res.append(f"{key1} for {round(value1, 2)} €")

for key1, value1 in points.items():
    for key2, value2 in points.items():
        if key1 + key2 >= pontos:
            res.append(f"{key1} + {key2} = {key1 + key2} for {round(value1 + value2, 2)} €")


for key1, value1 in points.items():
    for key2, value2 in points.items():
        for key3, value3 in points.items():
            if key1 + key2 + key3 >= pontos:
                res.append(f"{key1} + {key2} + {key3} = {key1 + key2 + key3} for {round(value1 + value2 + value3, 2)} €")


for key1, value1 in points.items():
    for key2, value2 in points.items():
        for key3, value3 in points.items():
            for key4, value4 in points.items():
                if key1 + key2 + key3 + key4 >= pontos:
                    res.append(f"{key1} + {key2} + {key3} + {key4} = {key1 + key2 + key3 + key4} for {round(value1 + value2 + value3 + value4, 2)} €")


for key1, value1 in points.items():
    for key2, value2 in points.items():
        for key3, value3 in points.items():
            for key4, value4 in points.items():
                for key5, value5 in points.items():
                    if key1 + key2 + key3 + key4 + key5 >= pontos:
                        res.append(f"{key1} + {key2} + {key3} + {key4} + {key5} = {key1 + key2 + key3 + key4 + key5} for {round(value1 + value2 + value3 + value4 + value5, 2)} €")


for key1, value1 in points.items():
    for key2, value2 in points.items():
        for key3, value3 in points.items():
            for key4, value4 in points.items():
                for key5, value5 in points.items():
                    for key6, value6 in points.items():
                        if key1 + key2 + key3 + key4 + key5 + key6 >= pontos:
                            res.append(f"{key1} + {key2} + {key3} + {key4} + {key5} + {key6} = {key1 + key2 + key3 + key4 + key5 + key6} for {round(value1 + value2 + value3 + value4 + value5 + value6, 2)} €")


min = 10000
str_res = ""
for str in res:
    print(str)
    args = str.split(" ")
    if float(args[-2]) < min:
        min = float(args[-2])
        str_res = str

print(str_res)
