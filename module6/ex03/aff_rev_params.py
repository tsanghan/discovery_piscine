#!/usr/bin/env python

import sys

# if len(sys.argv) < 3:
#     print("none")
# else:
#     for para in reversed(sys.argv[1:]):
#         print(para)

print("none") if len(sys.argv) < 3 \
    else print(*reversed(sys.argv[1:]), sep='\n')