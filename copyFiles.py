# coding: utf-8
import fnmatch, os, shutil
import argparse
import sys

parser = argparse.ArgumentParser(description='A program that copies a file or directory from a source to a destination. If program is called without arguments, user can use regular expressions to find files in current directory and copy them to a new directory')
parser.add_argument('-src', help='copyFiles -src <copied folder>. Warning: The source folder or files must include absolute path or relative path if within directory where they lie, and -dst must be included')
parser.add_argument('-dst', help='copyFiles -src <copied folder> -dest <dest folder>')
args = parser.parse_args()

def commandline_tool():
    try:
        if os.path.isfile(args.src):
            shutil.copy(args.src, args.dst)
        else:
            shutil.copytree(arg.src, args.dst)
    except Exception as e:
        print(e)

def main():
    filelist = []
    src = str(input('What would you like to copy? '))
    for file in os.listdir():
        if fnmatch.fnmatch(file, src):
            filelist.append(os.path.abspath(file))

    dstDir = str(input('Where would you like to copy the files? '))
    if not os.path.exists(dstDir):
        os.mkdir(dstDir)
    for file in filelist:
        shutil.copy(file, dstDir)

if len(sys.argv) < 2:
    main()
else:
    commandline_tool()
