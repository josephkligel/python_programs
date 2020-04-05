#/usr/bin/python3
import json
import re

filename = '/home/jkligel/Github/Programmapedia/bashref.txt'

dict = {}

with open(filename) as fh:
    try:
        for line in fh:
            if line == '\n' or line[0] == '#':
                pass
            elif line[0:2] == '\t#':
                subkey = re.sub(r"\W", '', line)
                dict[command].append({subkey: []})
            elif line[0] == '/' or line[0] == '~':
                command, description = line.strip().split(":", 1)
                dict[command] = [{'description': description.strip()}]
            elif line[0] == '\t':
                subkeyofsubkey, value = line.strip().split(":", 1)
                for i, item in enumerate(dict[command]):
                    if subkey in dict[command][i]:
                        dict[command][i][subkey].append({subkeyofsubkey: value.strip()})
                    else:
                        pass#line 22 to 26
                # dict[command][1][subkey].append({subkeyofsubkey: value.strip()})
            else:
                command, description = line.strip().split(":", 1)
                dict[command] = [{'description': description.strip()}]

    except Exception:
        print(Exception.message)
    finally:
        pass

        output_file = open("/home/jkligel/Desktop/outputbash.json", "w")
        json.dump(dict, output_file, indent=4, sort_keys=False)
        output_file.close()
