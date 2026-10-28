#!/usr/bin/env python

import numbers

def greetings(name="noble stranger"):
    if isinstance(name, numbers.Number):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)