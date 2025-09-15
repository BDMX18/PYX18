'''
7. Filter dictionary to keep items where key is uppercase

Question:
From a dictionary with mixed-case keys, return only the entries with all-uppercase keys.

Sample Data:

'''

env_vars = {
    "PATH": "/usr/bin",
    "home": "/home/user",
    "SHELL": "/bin/bash",
    "lang": "en_US.UTF-8"
}

print(dict(filter(lambda item: item[0].isupper(), env_vars.items())))