import json
import re

noteList = []
def main():
    titleRegex = re.compile(r'^(\s[A-Za-z])')
    bodyRegex = re.compile(r'^(\t)*')
    dashcolon = re.compile(r'(-|:)*')
    fr = open('todolist-copy.md')

    title = ''
    tbDict = {}
    bodyList = []
    global noteList
    for line in fr:
        if titleRegex.match(line):
            title, body = line.split('\t', 1)
            a_dict = {'title': title.strip(), 'body': body.strip()}
            noteList.append(a_dict)
        elif line.startswith(' -'):
            bodyList = []
            title = dashcolon.sub('', line).strip()
            tbDict = {'title': title, 'body': title}
            noteList.append(tbDict)
        elif line.startswith('\t'):
            noteList = [note for note in noteList if note != tbDict]
            body = dashcolon.sub('', line).strip()
            bodyList.append(body)


            tbDict.update({'title': title, "body": bodyList})
            noteList.append(tbDict)

    json.dump(noteList, open('todo-copy.json', 'w'), indent=4, sort_keys=True)
    fr.close()

main()
            
