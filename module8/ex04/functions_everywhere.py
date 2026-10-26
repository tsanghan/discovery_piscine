#!/usr/bin/env python

import sys

def shrink(param: str):
    print(param[0:8])

def enlarge(param: str):
    fill_len = 8 - len(param)
    # print(f"{param}{'Z' * fill_len}")
    print(param + 'Z' * fill_len)

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        # if len(param) < 8:
        #     enlarge(param)
        # else:
        #     shrink(param)
        enlarge(param) if (len(param) < 8) else shrink(param)