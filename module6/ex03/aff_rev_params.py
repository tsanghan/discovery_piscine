#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
    print("none")
else:
    for para in reversed(sys.argv[1:]):
        print(para)
