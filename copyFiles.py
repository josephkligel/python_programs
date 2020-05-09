# coding: utf-8
import fnmatch, os, shutil
import argparse

parser = argparse.ArgumentParser(description='A program that copies multiple files from a source to a destination. For example, files from this folder copied to another folder.')
parser.add_argument('input', help='User types in a source and destination and those are used to copy files from one location to another.')
args = parser.parse_args()

fileList = []

for dirroot, dir, files in os.walk('/home/jkligel/Ex_Files_CertPrep_RedHat_EX200/Exercise Files/'):
    for file in files:
        if fnmatch.fnmatch(file, '*cheatsheet*'):
            fileList.append(dirroot + '/' + file)

dstDir = '/home/jkligel/Github/Programmapedia/LinuxGuides/Test/'
if not os.path.exists(dstDir):
    os.mkdir(dstDir)
for file in fileList:
    shutil.copy(src=file, dst=dstDir)
    
