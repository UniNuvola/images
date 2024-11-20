import os
import json


UNIHUB = [
    'unihubsingle',
    'unihub',
    'unihubbackup',]
SERVICES = [
    'ldapproxy/docker',
    'ldapsyncservice/docker',
    'web/docker',]

folders = []

# walks inside `base` folder and finds all dir
# names with a `Makefile` inside
for root, dirs, files in os.walk('./base'):
    if 'Makefile' in files:
        folders.append(root)

folders = [*UNIHUB, *folders, *SERVICES]

print(f'dirs={json.dumps(folders)}')
