import glob
import sys, os
import json
import simple_chalk as chalk

found_json = open('found_files.json')
found_dict = json.load(found_json)
found_json.close()

def find(file, startDir='/home/jkligel'):
    for i in glob.iglob(f'{startDir}/**/{file}', recursive=True):
        found_dict[os.path.basename(i).split('.')[0].lower()] = i
        print(chalk.bgGreen(f'Found file {os.path.basename(i)}'))
        break

    print('Writing to json file...')
    json.dump(found_dict, open('found_files.json', 'w'), indent=4)
    print('Done')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find(sys.argv[1])
    elif len(sys.argv) == 3:
        find(sys.argv[1], sys.argv[2])
