#!/usr/bin/env python
import os, shutil

def main():
    script_file = open('pushAll.sh', 'w')
    script_file.writelines(['#!/usr/bin/env bash\n', 'git config --global credential.helper "cache --timeout 7200"\n\n', 'cd /home/jkligel/bin; bash gitPush\n'])
    for i in os.listdir('/home/jkligel/Github'):
        if os.path.isdir(i) and '.git' in os.listdir(i):
            script_file.write(f'cd {os.path.abspath(i)}; bash gitPush\n')
    
    script_file.close()
    #shutil.move('pushAll.sh', '/home/jkligel/bin')
            

if __name__ == '__main__':
    main()

