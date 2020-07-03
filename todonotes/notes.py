import os
import json
import re
import simple_chalk as chalk
# from lib import convert_todo_md

def loadNotes():
    with open(os.path.join(os.path.dirname(__file__), 'todo.json'), 'r') as fh:
        if fh != None:
            notes = json.load(fh)
            return notes
        else:
            notes = []
            return notes

def listNotes(args):
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
        print(chalk.bgGreen(f'title: {found["title"]}'))
        print(chalk.bgGreen(f'body: {", ".join(found["body"])}'))
    except Exception:
        print(chalk.bgRed('Note not found'))

def addNote(title, body): # No argument, just word found in sys.argsv
    notes = loadNotes()
    found = [True for note in notes if note['title'] == title]
    if not found:
        notes.append({'title': title, 'body': [body]})
        print(chalk.bgGreen('Added'))
        json.dump(notes, open(os.path.join(os.path.dirname(__file__), 'todo.json'), 'w'), indent=4)
    else:
        print(chalk.bgRed('Note taken'))

def removeNote(title): # No argument, just word found in sys.argsv
    notes = loadNotes()
    notesToKeep = [note for note in notes if note['title'] != title]
    if len(notesToKeep) < len(notes):
        print(chalk.bgGreen(f'Removed note {title}'))
        json.dump(notesToKeep, open(os.path.join(os.path.dirname(__file__), 'todo.json'), 'w'), indent=4)
    else:
        print(chalk.bgRed('Note does not exist'))

def updateNote(title, body): # No argument, just word found in sys.argsv
    notes = loadNotes() # Follows the same logic as the removeNote function
    updatedNotes = [note for note in notes if note['title'] != title]
    if len(updatedNotes) < len(notes):
        print(chalk.bgGreen('Updated note'))
        updatedNotes.append({'title': title, 'body': body})
        json.dump(updatedNotes, open(os.path.join(
            os.path.dirname(__file__), 'todo.json'), 'w'), indent=4)
    else:
        print(chalk.bgRed('Note does not exist'))

def appendNote(title, body):
    notes = loadNotes()
    found = [note for note in notes if note['title'] == title]
    found[0]['body'].append(body)
    if found != []:
        updateNote(found[0]['title'], found[0]['body']) # writing to json with updateNote
