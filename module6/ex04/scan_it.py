#!/usr/bin/env python

# import sys

# if len(sys.argv) != 3:
#     print("none")
# else:
#     result = sys.argv[2].count(sys.argv[1])
#     if result != 2:
#        print("none")
#     else:
#         print(result)

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    result = len(re.findall(sys.argv[1], sys.argv[2]))
    if result != 2:
       print("none")
    else:
        print(result)