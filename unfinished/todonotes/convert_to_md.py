import json

def main():
    with open('todo.json') as fr:
        todoData = json.load(fr)
        with open('todo.md', 'w') as fh:
            for note in todoData:
                fh.write(f"## {note['title']}\n")
                fh.write(f" -{note['body']}\n\n")

main()

