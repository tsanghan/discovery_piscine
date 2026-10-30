#!/usr/bin/env python

##########################################################
# import sys
#
# if len(sys.argv) != 3:
#     print("none")
# else:
#     result = sys.argv[2].count(sys.argv[1])
#     if result > 0:
#        print("none")
#     else:
#         print(result)
##########################################################

##########################################################
# import sys
# import re
#
# if len(sys.argv) != 3:
#     print("none")
# else:
#     result = len(re.findall(sys.argv[1], sys.argv[2]))
#     if result == 0:
#        print("none")
#     else:
#         print(result)
##########################################################

##########################################################
# import sys
# import re
#
# print("none") if len(sys.argv) != 3 else \
#     print("none") if (result := len(re.findall(sys.argv[1], sys.argv[2]))) < 1 \
#         else print(result)
##########################################################

import sys

print("none") if len(sys.argv) != 3 else \
    print("none") if (result := sys.argv[2].count(sys.argv[1])) < 1 \
        else print(result)