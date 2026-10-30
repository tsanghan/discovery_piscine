#!/usr/bin/env python

def find_the_redheads(param: dict[str, str]):
    # filtered = [ k for k, v in param.items() if v == 'red']
    return list(filter(lambda name: param[name] == "red", param.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))