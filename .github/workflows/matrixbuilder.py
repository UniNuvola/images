import os
import json


fixed = [
    'ldapproxy/docker',
    'ldapsyncservice/docker',
    'web/docker',
    'unihub',
    'unihubsingle',
]
folders = []

# walks inside `base` folder and finds all dir
# names with a `Makefile` inside
for root, dirs, files in os.walk('./base'):
    if 'Makefile' in files:
        folders.append(root)

folders += fixed

print(f'dirs={json.dumps(folders)}')
