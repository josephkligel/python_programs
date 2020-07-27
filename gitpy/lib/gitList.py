import os
import glob
import json

def find_git(search_dir='/home/jkligel/Github'):
    localRepoList = {}
    for file in glob.iglob(f'{search_dir}/**/.git', recursive=True):
        localRepoList[os.path.basename(os.path.dirname(file)).capitalize()] = os.path.dirname(file)
    return localRepoList

def write_bash_script(repoDict):
    with open('pushAll.sh', 'w') as fh:
        print('Writing pushAll.sh in cwd...')
        
        fh.writelines(['#!/usr/bin/env bash\n', 'git config --global credential.helper "cache --timeout 7200"\n\n', 'cd /home/jkligel/bin; bash gitPush\n']) 
        
        for i in repoDict.keys():
            fh.write(f'git clone http://github.com/zigjag/{i.lower()}.git\n')  

def write_local_list(repoDict):
    with open('localRepoList.json', 'w') as fh:
        print('Writing localRepoList.json in cwd...')
        json.dump(repoDict, fh, indent=4)   
    
def main():
    repoDict = find_git()
    write_bash_script(repoDict)
    write_local_list(repoDict)

if __name__ == '__main__':
    main()
