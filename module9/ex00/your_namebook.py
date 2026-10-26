#!/usr/bin/env python

def array_of_names(param: dict[str, str]):
    name_list: list[str]=[]
    for key, value in param.items():
        name_list.append(f"{key.capitalize()} {value.capitalize()}")
    print(name_list)

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
