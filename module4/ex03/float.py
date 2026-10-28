#!/usr/bin/env python

# s = input("Give me a number: ")

# try:
#     int(s)
#     print("This number is an integer.")
# except ValueError:
#     if "." in s and s.replace(".", "").isdigit():
#         print("This number is an decimal.")
#     else:
#         print("This is a string.")

try:
    s = float(input("Give me a number: "))
    if s.is_integer():
        print("This number is an integer.")
    else:
        print("This number is an decimal.")
except ValueError:
    print(f"Could not convert string to float.")

