#!/usr/bin/env python

import sys

# if len(sys.argv) < 2:
#     print("none")
# else:
#     count = sys.argv[1].count('z')
#     if count:
#         print('z' * count)
#     else:
#         print("none")


print("none") if len(sys.argv) < 2 else \
    print('z' * count) if bool(count := sys.argv[1].count('z')) else \
        print("none")