#!/usr/bin/env python

def average(param):
    return sum([v for _, v in param.items()])/len(param)

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

class_average = [
    ('3B', average(class_3B)),
    ('3C', average(class_3C))
]

for item in class_average:
    print(f"Average for class {item[0]}: {item[1]}.")
