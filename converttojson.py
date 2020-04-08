#/usr/bin/python3

import json

filename = input('Paste link of file here, include file location: ')

dict = {}
tabbed_line = ''

with open(filename) as fh:
    for line in fh:
        if line == '\n' or line[0] == '#':
            print("Nothing on this line")
        elif line[0] == '\t':
            tabbed_line = line.stip()
        elif line[0] == '/' or '~':
            print(line.strip(), tabbed_line)
        else:
            command, description = line.strip().split(":", 1)
            dict[command] = description.strip()

out_file = open("/home/jkligel/Desktop/test1.json", "w")
json.dump(dict, out_file, indent=4, sort_keys=False)
out_file.close()
