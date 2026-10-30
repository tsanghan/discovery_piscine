#!/usr/bin/env python

import sys

# if len(sys.argv) < 2:
#     print("none")
# else:
#     user_input = input("What was the parameter? ")
#     if user_input == sys.argv[1]:
#         print("Good job!")
#     else:
#         print("Nope, sorry...")

print("none") if len(sys.argv) < 2 else \
    print("Good job!") if input("What was the parameter? ") == sys.argv[1] else \
        print("Nope, sorry...")