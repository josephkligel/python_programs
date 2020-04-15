import sys, subprocess
from pexpect import popen_spawn, spawn
import pexpect

try:
    child = pexpect.spawn("gitPushAll.py")
    child.logfile = open("./mylog", 'wb')
    child.expect("Username.+: ")
    child.sendline('zigjag')
    child.expect('Password.+: ')
    child.sendline('104Percent%')
except:
    print('Something went wrong!')
    print(str(child))

# cmd = 'echo zigjag | gitPushAll.py'.split()
# print(cmd)
# p = subprocess.Popen(cmd, shell=True)
# p.communicate(input='\nzigjag', timeout=10)
# p = subprocess.check_output('gitPushAll.py', input=b'zigjag')
