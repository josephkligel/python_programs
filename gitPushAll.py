#!/usr/bin/python3
from os import *
import time

add = "git add ."
commit = "git commit -m 'generic message'"
push = "git push -u origin master"

system("%s" % ("git add ."))
system("%s" % ("git commit -m 'generic message generated from gitPushAll python program'"))
system("%s" % ("git push -u origin master"))
