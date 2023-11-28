#can save things on a  clipboard, can display list and load things from the list
#commands: save, load, list
#preinstalled modules - part of Python module
import sys
import clipboard

import json

if len(sys.argv) == 2:
    command = sys.argv[1]

    if command == "save":
        print('save')
    elif command == "load":
        print('load')
    elif command == "list":
        print('list')
    else: 
        print("Unknown command")

else: 
    print("Pleae pass exactly one command")