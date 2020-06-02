#!/usr/bin/env python

import json
import sys, os, argparse
import re
import simple_chalk as chalk
from lib import convert_data
from lib import convert_todo_md

parser = argparse.ArgumentParser(description='Todolist app')
parser.add_argument('read', help='Read a note\'s title and body')
parser.add_argument('list', action='store_true', help='List all note titles')
parser.add_argument('add', action='store_false', help="Add a new note. Syntax is todonotes.py add --title <note title> --body <body of note>")
parser.add_argument('remove', action='store_false', help="Remove a note. Syntax is todonotes.py remove --title <note title>")
parser.add_argument('update', action='store_false', help="Update existing note. Syntax is todonotes.py update --title <note title> --body <body of note>")
parser.add_argument('append', action='store_false', help="Append to an existing note. Syntax is todonotes.py append --title <note title> --body <new item to append>")


parser.add_argument('--all', action='store_true', help='Option for list to list body of notes also.')
parser.add_argument('--title', help='todoNotes.py add --title <title of note> --body <body of note>')
parser.add_argument('--body', help='todoNotes.py add --title <title of note> --body of note')
args = parser.parse_args()

def loadNotes():
    convert_todo_md.main() # converts todo.md to todo.json
    with open('/home/jkligel/python_programs/todonotes/todo.json') as fh:
        if fh != None:
            notes = json.load(fh)
            return notes
        else:
            notes = []
            return notes

def listNotes():
    notes = loadNotes()
    for note in notes:
        if args.all:
            print(chalk.bgBlue(f'{note["title"]}: {", ".join(note["body"])}'))
        else:
            print(chalk.bgBlue(note['title']))

def readNote(title):
    notes = loadNotes()
    try:
        found = next(note for note in notes if re.compile(title).match(note['title']))
        print(chalk.bgBlue(f'title: {found["title"]}'))
        print(chalk.bgBlue(f'body: {", ".join(found["body"])}'))
    except Exception:
        print(chalk.bgRed('Note not found'))

def addNote(title, body): # No argument, just word found in sys.argsv
    notes = loadNotes()
    found = [True for note in notes if note['title'] == title]
    if not found:
        notes.append({'title': title, 'body': body})
        print(chalk.bgGreen('Added'))
        json.dump(notes, open('todo.json', 'w'))
    else:
        print(chalk.bgRed('Note taken'))

def removeNote(title): # No argument, just word found in sys.argsv
    notes = loadNotes()
    notesToKeep = [note for note in notes if note['title'] != title]
    if len(notesToKeep) < len(notes):
        print(chalk.bgGreen(f'Removed note {title}'))
        json.dump(notesToKeep, open('todo.json', 'w'))
    else:
        print(chalk.bgRed('Note does not exist'))

def updateNote(title, body): # No argument, just word found in sys.argsv
    notes = loadNotes() # Follows the same logic as the removeNote function
    updatedNotes = [note for note in notes if note['title'] != title]
    if len(updatedNotes) < len(notes):
        print(chalk.bgGreen('Updated note'))
        updatedNotes.append({'title': title, 'body': body})
        json.dump(updatedNotes, open('todo.json', 'w'))
    else:
        print(chalk.bgRed('Note does not exist'))

def appendNote(title, body):
    notes = loadNotes()
    found = [note for note in notes if note['title'] == title]
    found[0]['body'].append(body)
    if found != []:
        updateNote(found[0]['title'], found[0]['body'])

def main():
    for arg in sys.argv:
        if 'list' == arg:
            listNotes()
        elif 'read' == arg:
            readNote(args.title)
        elif 'add' == arg:
            addNote(args.title, args.body)
        elif 'remove' == arg:
            removeNote(args.title)
        elif 'update' == arg:
            updateNote(args.title, args.body)
        elif 'append' == arg:
            appendNote(args.title, args.body)

    convert_data.md() #converts todo.json to todo.md

if __name__ == '__main__':
    main()

