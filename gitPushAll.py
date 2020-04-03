#!/usr/bin/python3
from os import *
from io import StringIO as sio
from sys import stdin

system("%s" % ("git add ."))
system("%s" % ("git commit -m 'generic message generated from gitPushAll python program'"))

stdin = sio("zigjag")
system("%s" % ("git push -u origin master"))
