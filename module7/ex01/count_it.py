#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print("none")
else:
    para_len = len(sys.argv) - 1
    print(f"parameters: {para_len}")
    for para in sys.argv[1:]:
        print(f"{para}: {len(para)}")
