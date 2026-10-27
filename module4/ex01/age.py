#!/usr/bin/env python

user_age = int(input("Please tell me your age: "))

print(f"You are currently {user_age} years old.")
for i in range(10,40,10):
    print(f"In {i} years, you'll be {user_age + i} years old")