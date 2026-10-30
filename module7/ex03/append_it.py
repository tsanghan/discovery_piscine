#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print("none")
else:
    for para in sys.argv[1:]:
        # if para.endswith("ism"):
        if para.find("ism") > 0:
            continue
        else:
            print(f"{para}ism")
