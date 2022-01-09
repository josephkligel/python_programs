#/usr/bin/python3
import json
import re

filename = '/home/jkligel/Github/Programmapedia/bashref.txt'

dict = {}
sksklist = []

def add_to_sksklist(string, lst):
    if string in lst:
        return lst
    else:
        lst.append(string.strip())
    return lst

with open(filename) as fh:
    try:
        for line in fh:
            if line == '\n' or line[0] == '#':
                pass
            elif line[0:2] == '\t#':
                subkey = re.sub(r"\W", '', line)
                dict.update({command: {subkey}})
            elif line[0] == '/' or line[0] == '~':
                command, description = line.strip().split(":", 1)
                dict.update({command: {"description": description.strip()}})
            elif line[0] == '\t':
                # sksklist = add_to_sksklist(line, sksklist)
                # for item in sksklist:
                subkeyofsubkey, value = line.strip().split(":", 1)
                dict.update({command: {subkey: {subkeyofsubkey: value.strip()}}}) #Only adds flag/example/subkeyofsubkey
            else:
                command, description = line.strip().split(":", 1)
                dict.update({command: {"description": description.strip()}})
    except Exception:
        print(Exception.message)
    finally:
        print(sksklist)

        output_file = open("/home/jkligel/Desktop/outputbash.json", "w")
        json.dump(dict, output_file, indent=4, sort_keys=False)
        output_file.close()
