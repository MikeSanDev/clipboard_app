#can save things on a  clipboard, can display list and load things from the list
#commands: save, load, list
#preinstalled modules - part of Python module
import sys
import clipboard
import json

# function to create/read json file for us
def save_items(filepath, data):
    with open(filepath, "w") as f: #w = write
        json.dump(data, f) #write python dictionary as a json object

save_items("test.json", {"key": "value"})

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
    print("Please pass exactly one command")