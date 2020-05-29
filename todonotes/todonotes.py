#!/usr/bin/env python

import json
import sys, argparse
#sys.path.insert(1, '/home/jkligel/python_programs/todonotes/')
from lib import convert_to_md
from lib import *

parser = argparse.ArgumentParser(description='Todolist app')
parser.add_argument('read', help='Read a note\'s title and body')
parser.add_argument('list', action='store_true', help='List all note titles')
parser.add_argument('--all', action='store_true', help='Option for list to list body of notes also.')
parser.add_argument('--title', help='todoNotes.py add --title <title of note> --body <body of note>')
parser.add_argument('--body', help='todoNotes.py add --title <title of note> --body of note')
args = parser.parse_args()

def loadNotes():
    with open('/home/jkligel/python_programs/todonotes/lib/todo.json') as fh:
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
            print(note['title'], note['body'], sep=': ')
        else:
            print(note['title'])

def readNote(title):
    notes = loadNotes()
    try:
        found = next(note for note in notes if note['title'] == title)
        print(f'title: {found["title"]}')
        print(f'body: {found["body"]}')
    except Exception:
        print('Note not found')

def addNote(title, body): # No argument, just word found in sys.argsv
    notes = loadNotes()
    found = [True for note in notes if note['title'] == title]
    if not found:
        notes.append({'title': title, 'body': body})
        print('Added')
        json.dump(notes, open('todo.json', 'w'))
    else:
        print('Note taken')

def removeNote(title): # No argument, just word found in sys.argsv
    notes = loadNotes()
    notesToKeep = [note for note in notes if note['title'] != title]
    if len(notesToKeep) < len(notes):
        print('Removed note', title)
        json.dump(notesToKeep, open('todo.json', 'w'))
    else:
        print('Note does not exist')

def updateNote(title, body): # No argument, just word found in sys.argsv
    notes = loadNotes() # Follows the same logic as the removeNote function
    updatedNotes = [note for note in notes if note['title'] != title]
    if len(updatedNotes) < len(notes):
        print('Updated note')
        updatedNotes.append({'title': title, 'body': body})
        json.dump(updatedNotes, open('todo.json', 'w'))
    else:
        print('Note does not exist')

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
            convert_to_md.md()
        elif 'update' == arg:
            updateNote(args.title, args.body)

main()
