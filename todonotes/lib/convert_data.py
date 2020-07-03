import json
import os
import simple_chalk as chalk

def json_to_md(src='todo.json', clone='todo.md'):
    with open(src) as fr:
        todoData = json.load(fr)
        with open(clone, 'w') as fh:
            for note in todoData:
                fh.write(f"## {note['title']}\n")
                if type(note['body']) == list:
                    for item in note['body']:
                        fh.write(f'* {item}\n')
                    fh.write('\n')
                else:
                    fh.write(f"* {note['body']}\n\n")

def md_to_json(src='todo.md', clone='todo.json'):
    with open(src) as fr:
        notes = []
        note = {}
        for line in fr:
            if line.startswith('##'):
                title = line.strip().replace('## ', '')
                note = {'title': title, 'body': []}
            elif line.startswith('*'):
                bodyItem = line.strip().replace('* ', '')
                note['body'].append(bodyItem)
            elif line == '\n':
                notes.append(note)
        
        json.dump(notes, open(clone, 'w'), indent=4, sort_keys=False)


if __name__ == '__main__':
    print(f'Calling main. Writing file copies to {os.path.abspath(".")}')
    try:
        json_to_md(src='../todo.json', clone='todo-copy.md')
        md_to_json(src='../todo.md', clone='todo-copy.json')
    except:
        print(chalk.bgRed('Error: Call from lib folder'))

