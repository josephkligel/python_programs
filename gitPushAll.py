#!/bin/usr/python3
from os import *
import time

add = "git add ."
commit = "git commit -m 'generic message'"
push = "git push -u origin master"

system(add)
system(commit)
system(push)
system("zigjag")
