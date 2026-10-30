#!/usr/bin/env python

password = "Python is awesome"

# input_password = input()

# if input_password == password:
#     print("ACCESS GRANTED")
# else:
#     print("ACCESS DENIED")

print("ACCESS GRANTED") if (input_password := input()) == password else \
    print("ACCESS DENIED")