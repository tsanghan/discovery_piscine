#!/usr/bin/env python

# number_1 = 0

# while number_1 < 11:
#     print(f"Table of {number_1}: ", end="")
#     number_2 = 0
#     while number_2 < 11:
#         print(f"{number_1 * number_2} ", end="")
#         number_2 += 1
#     print()
#     number_1 += 1

for number_1 in range(0, 11):
    print(f"Table of {number_1}: ", end="")
    for number_2 in range(0, 11):
        print(f"{number_1 * number_2} ", end="")
    print()