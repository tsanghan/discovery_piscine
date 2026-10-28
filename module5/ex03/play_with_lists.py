#!/usr/bin/env python

orig_list = [2, 8, 9, 48, 8, 22, -12, 2]
remove_dup_set = set(orig_list)
modified_set = { x + 2 for x in remove_dup_set if x > 5 }

print(f"{orig_list}\n{modified_set}")