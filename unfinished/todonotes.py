import sys
import argparse
import re

parser = argparse.ArgumentParser(description='Add and edit notes to todolist')
parser.add_argument('add', help='todonotes add <new note>')
parser.add_argument('edit', help='todonotes edit <note>')
parser.add_argument('-b', '--body', help='todonotes edit <note> --body <content>')
args = parser.parse_args()

if args.edit:
    note = re.compile(r'\t.*')
    todolist = open('/home/jkligel/Github/Programmapedia/todolist.md', 'r+')
    for line in todolist:
        if args.edit in line:
            todolist.write(line.replace(note, args.body))

todolist.close()
