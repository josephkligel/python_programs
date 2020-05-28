import json
import re

todolist = {}
subcatRegex = re.compile(r'^(\s\w|\s-).*$')
noteRegex = re.compile(r'^(\t)*')
regex = re.compile(r'^(\s|-|#|\t)*')

category = ''
notes = []
def main():
    with open('todo-copy.txt', 'r') as fr:
        global category
        global notes
        for line in fr:
            if line.startswith('# '):
                category = regex.sub('', line.strip()).split(':')[0]
                todolist.update({category: ''})
            #elif line.startswith(' ') or line.startswith('\t'):
            #    note = regex.sub('', line).strip()
            #    notes.append(note)
            #    todolist.update({category: notes})
            elif '\t\t' in line:
                print(line)
                note, value = regex.sub('', line.strip()).split('\t', 1)
                notes.append({note: value})
                todolist.update({category: notes})
            elif '\t' in line:
                    note = regex.sub('', line.strip())
                    notes.append(note)
                    todolist.update({category: notes})
            else:
                continue
            #notes = []

if __name__ == '__main__':
    main()
    print(todolist)
