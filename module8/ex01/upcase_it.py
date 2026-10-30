#!/usr/bin/env python

def upcase_it(param: str) -> str:
    return param.upper()

# from collections.abc import Callable

# upcase_it: Callable[[str], str] = lambda param: param.upper()

print(upcase_it("hello"))


