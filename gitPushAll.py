#!/usr/bin/python3
from os import *
import time
from sys import stdout

add = "git add ."
commit = "git commit -m 'generic message'"
push = "git push -u origin master"

system("%s" % ("git add ."))
system(commit)
system(push)
