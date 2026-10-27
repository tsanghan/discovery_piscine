#!/usr/bin/env python

def find_the_redheads(param):
    # filtered = [ k for k, v in param.items() if v == 'red']
    filtered = list(map(lambda item: item[0],
                        filter(lambda item: item[1] == 'red', param.items())))
    return filtered



dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))