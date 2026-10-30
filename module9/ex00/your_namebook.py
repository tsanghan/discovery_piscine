#!/usr/bin/env python

def array_of_names(param: dict[str, str]):
    # name_list = []
    # for key, value in param.items():
    #     name_list.append(f"{key.capitalize()} {value.capitalize()}")
    # return name_list
    return [f"{key.capitalize()} {value.capitalize()}"
            for key, value in param.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
