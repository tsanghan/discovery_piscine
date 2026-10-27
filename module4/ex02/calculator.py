#!/usr/bin/env python

first_number = int(input("Give me the first number: "))
second_number = int(input("Give me the second number: "))

print("Thank you!")

# print(f"{first_number} + {second_number} = {first_number + second_number}")
# print(f"{first_number} - {second_number} = {first_number - second_number}")
# print(f"{first_number} / {second_number} = {first_number // second_number}")
# print(f"{first_number} * {second_number} = {first_number * second_number}")

operations = [
    ("+", first_number + second_number),
    ("-", first_number - second_number),
    ("/", first_number // second_number),
    ("*", first_number * second_number),
]

for symbol, result in operations:
    print(f"{first_number} {symbol} {second_number} = {result}")