#can save things on a  clipboard, can display list and load things from the list
#commands: save, load, list
#preinstalled modules - part of Python module
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

# function to create/read json file for us
def save_data(filepath, data):
    with open(filepath, "w") as f: #w = write
        json.dump(data, f) #write python dictionary as a json object

def load_data(filepath):
    try: #if filepath fails/ no file exists then it goes to except:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data #returns python dictionary representation of this json object
    except: 
        return {} #the exception returns an empty dictionary

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA) #loads data in json file

    if command == "save":
        key = input("Enter a key:")
        data[key] = clipboard.paste() #pastes data onto clipboard
        save_data(SAVED_DATA, data) #loaded key will be pasted to current clipboard
        print("Input saved successfully!")
    elif command == "load":
        key = input("Enter a key:")
        if key in data: #check if key exists
            clipboard.copy(data[key]) #access data by the key
            print("Data copied to the clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else: 
        print("Unknown command")
#no delete command, you can overwrite the key 
else: 
    print("Please pass exactly one command")