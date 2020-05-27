import json

ad = [
        {'title': 'Command', 'desc': 'Completes task in an automated manner', 'category': {'Examples': ['This', 'That', 'Which', 'What'], 'Methods': ['M1', 'M2', 'M3'], 'Usage': ['U1', 'U2', 'U3']}},
        {'title': 'Command', 'desc': 'Completes task in an automated manner', 'category': {'Examples': ['This', 'That', 'Which', 'What'], 'Methods': ['M1', 'M2', 'M3'], 'Usage': ['U1', 'U2', 'U3']}},
        {'title': 'Command', 'desc': 'Completes task in an automated manner', 'category': {'Examples': ['This', 'That', 'Which', 'What'], 'Methods': ['M1', 'M2', 'M3'], 'Usage': ['U1', 'U2', 'U3']}},
        {'title': 'Command', 'desc': 'Completes task in an automated manner', 'category': {'Examples': ['This', 'That', 'Which', 'What'], 'Methods': ['M1', 'M2', 'M3'], 'Usage': ['U1', 'U2', 'U3']}},
        {'title': 'Command', 'desc': 'Completes task in an automated manner', 'category': {'Examples': ['This', 'That', 'Which', 'What'], 'Methods': ['M1', 'M2', 'M3'], 'Usage': ['U1', 'U2', 'U3']}},
        ]

def main():
    print('writing text file...')
    with open('test.txt', 'w') as fh:
        for dictionary in ad:
            fh.write(f'## {dictionary["title"]}:\n')
            fh.write(f'{dictionary["desc"]}\n')
            for k,v in dictionary['category'].items():
                fh.write(f'### {k}:\n')
                for item in v:
                    fh.write(f'\t-{item}\n')
            fh.write(f"{'-'*40}\n")
    print('Done')

def to_Json():
    print('Writing json file...')
    dataJSON = {item for item in ad}
    with open('test.json', 'w') as fh:
        json.dumps(dataJSON, fh)

if __name__ == '__main__':
    main()
