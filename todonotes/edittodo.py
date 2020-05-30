import json

def main():
    fr = open('todo.md')
    aList = []
    aDict = {}
    for line in fr:
        if line.startswith('##'):
            aDict['body'] = []
            title = line.strip().replace('## ', '')
            aDict['title'] = title
        elif line.startswith(' -'):
            body = line.strip().replace('-', '')
            aDict['body'].append(body)
            aList.append(aDict)
    print(aList)
    fr.close()

main()
