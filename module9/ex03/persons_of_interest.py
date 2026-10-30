#!/usr/bin/env python

def famous_births(param: dict[str, dict[str, str]]):
    sorted_param = sorted(param.items(), key=lambda param: param[1]['date_of_birth'])
    for _, v in sorted_param:
        print(f"{v['name']} is a great scientist born in {v['date_of_birth']}")


women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)