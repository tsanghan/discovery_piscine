#!/usr/bin/env python

def famous_births(param):
    sorted_param = sorted(param.items(), key=lambda item: item[1]['date_of_birth'])
    for item in sorted_param:
        print(f"{item[1]['name']} is a great scientist born in {item[1]['date_of_birth']}")


women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)