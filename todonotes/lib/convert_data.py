import json

todo_json_path = 'todo.json'
def md(path=todo_json_path):
    with open(path) as fr:
        todoData = json.load(fr)
        with open('todo.md', 'w') as fh:
            for note in todoData:
                fh.write(f"## {note['title']}\n")
                if type(note['body']) == list:
                    for item in note['body']:
                        fh.write(f' -{item}\n')
                    fh.write('\n')
                else:
                    fh.write(f" -{note['body']}\n\n")

if __name__ == '__main__':
    md(path='../todo.json')

