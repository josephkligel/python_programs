import sys, subprocess
from pexpect import popen_spawn, spawn
import pexpect

try:
    child = pexpect.spawn("gitPushAll.py", encoding='utf-8')
    child.logfile = sys.stdout
    child.expect("Username.+: ")
    child.sendline('zigjag')
    child.expect('Password.+: ')
    child.sendline('wrong')
except:
    print('-----Something went wrong!----')
    print(str(child))
