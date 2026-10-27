#!/usr/bin/env python

a_number = int(input("Enter a number less than 25 \n"))

if a_number > 25:
    print("Error")
else:
    count = a_number
    while count <= 25:
        print(f"Inside the loop, my variable is {count}")
        count += 1