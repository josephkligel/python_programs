import os, glob

def find_git(search_dir='/home/jkligel/Github'):
    script_file = open('/home/jkligel/bin/pushAll.sh', 'w')
    
    script_file.writelines(['#!/usr/bin/env bash\n', 'git config --global credential.helper "cache --timeout 7200"\n\n', 'cd /home/jkligel/bin; bash gitPush\n']) 
    
    for file in glob.iglob(f'{search_dir}/**/.git', recursive=True):
        script_file.write(f'cd {os.path.dirname(file)}; bash gitPush\n')
    
    script_file.close()

if __name__ == '__main__':
    find_git()
