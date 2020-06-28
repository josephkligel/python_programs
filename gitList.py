#!/usr/bin/env python3
import os, shutil

def main():
    script_file = open('/home/jkligel/bin/pushAll.sh', 'w')
    script_file.writelines(['#!/usr/bin/env bash\n', 'git config --global credential.helper "cache --timeout 7200"\n\n', 'cd /home/jkligel/bin; bash gitPush\n'])

    print('Writing git folders to file...')
    for i in os.listdir('/home/jkligel/Github/'):
        # script_file.write(f'cd {os.path.abspath(i)}; bash gitPush\n')
        if os.path.isdir(i) and '.git' in os.listdir(i):
            script_file.write(f'cd {os.path.abspath(i)}; bash gitPush\n')

    script_file.close()


if __name__ == '__main__':
    main()
