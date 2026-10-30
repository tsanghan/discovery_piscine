#!/usr/bin/env python

import sys

if len(sys.argv) != 3:
    print("none")
else:
    # smaller_number = int(sys.argv[1])
    # bigger_number = int(sys.argv[2])

    # if smaller_number < bigger_number:
    #     print([x for x in range(smaller_number, bigger_number + 1)])
    # else:
    #     print("first number NOT smaller than the second one!!")
    smaller_number, bigger_number = map(int, sys.argv[1:3])
    print([x for x in range(smaller_number, bigger_number + 1)]) \
        if smaller_number < bigger_number else \
            print("first number NOT smaller than the second one!!")