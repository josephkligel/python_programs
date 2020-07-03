#!/usr/bin/env python

import json
import sys, os, argparse
import re
import simple_chalk as chalk
from notes import loadNotes, listNotes, readNote, addNote, removeNote, updateNote, appendNote
from lib import convert_data

parser = argparse.ArgumentParser(description='Todolist app')
parser.add_argument('list', action='store_true', help='List all note titles')
parser.add_argument('read', help='Read a note\'s title and body')
parser.add_argument('add', action='store_false', help="Add a new note. Syntax is todonotes.py add --title <note title> --body <body of note>")
parser.add_argument('remove', action='store_false', help="Remove a note. Syntax is todonotes.py remove --title <note title>")
parser.add_argument('update', action='store_false', help="Update existing note. Syntax is todonotes.py update --title <note title> --body <body of note>")
parser.add_argument('append', action='store_false', help="Append to an existing note. Syntax is todonotes.py append --title <note title> --body <new item to append>")


parser.add_argument('--all', action='store_true', help='Option for list to list body of notes also.')
parser.add_argument('--title', help='todoNotes.py add --title <title of note> --body <body of note>')
parser.add_argument('--body', help='todoNotes.py add --title <title of note> --body of note')
args = parser.parse_args()

def main():
    for arg in sys.argv:
        if arg == 'list':
            listNotes(args)
        elif arg == 'read':
            readNote(args.title)
        elif arg == 'add':
            addNote(args.title, args.body)
        elif 'remove' == arg:
            removeNote(args.title)
        elif 'update' == arg:
            updateNote(args.title, args.body)
        elif 'append' == arg:
            appendNote(args.title, args.body)

    convert_data.json_to_md() #converts todo.json to todo.md

if __name__ == '__main__':
    main()

