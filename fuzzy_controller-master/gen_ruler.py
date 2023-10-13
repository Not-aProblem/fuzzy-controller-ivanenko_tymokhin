import numpy as np


import pandas as pd
import itertools

import streamlit as st
import pandas as pd
import numpy as np

# init Table

# df = pd.DataFrame(
#     {
#         "Age": [10],
#         "Height": [10],
#         "Nutrition": [10],
#         "metrick": ["cof"],
#         "Value": [5.200000000000001],
#         "term": ["medium"],
#     }
# )


# df.to_csv("data.csv", index=False)


data = {
    "Age": ["puppy", "young", "adult", "senior"],
    "Weight": ["light", "medium", "heavy"],
    "Nutrition": ["low", "medium", "high"],
}


value = {
    "Age": lambda x: 6 + x * -2,
    "Weight": lambda x: 1 + -(1 ** (x + 1)),
    "Nutrition": lambda x: x * 3 - 1 * max(0, x - 1),
}


rez = []
rez2 = []
for tupl in tuple(itertools.product(*[data[i] for i in data])):
    t = 0
    for index, param in enumerate(data):
        t += value[param](data[param].index(tupl[index]))
    rez2.append(t)
    t2 = (tupl, "low")
    if t > 3:
        t2 = (tupl, "medium")
    if t > 5:
        t2 = (tupl, "high")

    rez.append(t2)


print(rez)


number_count = {}
for num in rez2:
    if num in number_count:
        number_count[num] += 1
    else:
        number_count[num] = 1
rez = []
for i in number_count:
    rez.append(number_count[i])


chart_data = pd.DataFrame(rez, columns=["a"])


st.bar_chart(chart_data)


# from model import input_lvs


# data = {}
# for i in input_lvs:
#     data[i["name"]] = []
#     for i2 in i["terms"]:
#         data[i["name"]].append(i2)
# print(data)
