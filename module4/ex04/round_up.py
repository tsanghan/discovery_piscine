#!/usr/bin/env python

import math

s = input("Give me a number: ")

try:
    int(s)
    print(s)
except ValueError:
    if "." in s and s.replace(".", "").isdigit():
        s = float(s)
        print(f"{math.ceil(s)}")
    else:
        print("This is a string.")  