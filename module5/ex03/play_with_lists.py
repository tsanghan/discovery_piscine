#!/usr/bin/env python

orig_list = [2, 8, 9, 48, 8, 22, -12, 2]
remove_dup_set = set(orig_list)
modified_list = { x + 2 for x in remove_dup_set if x > 5 }

# print(f"Original list: {orig_list}")
# print(f"New list: {modified_list}")

print(orig_list)
print(modified_list)