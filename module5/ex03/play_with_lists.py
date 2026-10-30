#!/usr/bin/env python

orig_list = [2, 8, 9, 48, 8, 22, -12, 2]
modified_set = { x + 2 for x in set(orig_list) if x > 5 }

print(f"{orig_list}\n{modified_set}")