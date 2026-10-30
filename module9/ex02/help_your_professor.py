#!/usr/bin/env python

def average(param: dict[str, int]):
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

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")

# class_average = [
#     ('3B', average(class_3B)),
#     ('3C', average(class_3C))
# ]

# for class_name, average in class_average:
#     print(f"Average for class {class_name}: {average}.")