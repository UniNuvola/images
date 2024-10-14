import os
import json


fixed = [
    'unihubsingle',
    'unihub',
    'ldapproxy/docker',
    'ldapsyncservice/docker',
    'web/docker',
]
folders = []

# walks inside `base` folder and finds all dir
# names with a `Makefile` inside
for root, dirs, files in os.walk('./base'):
    if 'Makefile' in files:
        folders.append(root)

folders = [*fixed[:2], *folders, *fixed[2:]]

print(f'dirs={json.dumps(folders)}')
