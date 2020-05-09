import os, re, zipfile
import argparse

parser = argparse.ArgumentParser(description='Count the number of slides in .pptx decks and return a count')
parser.add_argument('-s', '--summary', help='Generate a summary of all decks processed', action='store_true')
parser.add_argument('-f', '--files', help='A list of files to process', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

decks = {}

if(args.files):
    for file in args.files:
        if os.path.abspath(file.name).endswith('.pptx'):
            decks[os.path.abspath(file.name)] = 0
        else:
            print(f'The file {file.name} is not a .pptx file and will be ignored.')

for deck, count in decks.items():
    try:
        archive = zipfile.ZipFile(deck, 'r')
        contents = archive.namelist()
    except Exception as e:
        print(f'Error reading {os.path.basename(deck)} ({e}). Count will be 0')
    else:
        for fileEntry in contents:
            if(re.findall('ppt/slides/slide', fileEntry)):
                decks[deck] += 1
print('Slides\tDeck')

for deck, count in sorted(decks.items()):
    print(f'{count}\t{os.path.basename(deck)}')
