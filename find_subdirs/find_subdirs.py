#!/usr/bin/env python3
import pathlib
import os
import glob 

def has_nodemod(path):
    if glob.glob(f'{path}/**/*node_modules', recursive=True):
        return True

def append_gitignore(path, line=None):
    print(f'Searching for gitignore file...')
    if glob.glob(f'{path}/.gitignore'):
        with open(f'{path}/.gitignore', 'a') as fw:
            print(f'\nWriting {line} to {fw.name}')
            fw.write(line + '\n')
        os.chdir(path)
        os.system(f'git rm -r --cached .; git add .; git commit -m "Add {line} to gitignore"; git push')

def search_subdirs(paths, filter_function):
    return filter(filter_function, paths)

def main(rootname):
    root_subdirs = [pathlib.Path(i) for i in os.scandir(rootname)]
    found_nm = search_subdirs(root_subdirs, has_nodemod)
    for i in found_nm:
        append_gitignore(i, 'node_modules/')

if __name__ == '__main__':
    main('/home/jkligel/Github')
