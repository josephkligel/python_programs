import sys, subprocess
from pexpect import popen_spawn, spawn
import pexpect

try:
    child = pexpect.spawn("gitPushAll.py")
    child.expect(".+")
    child.sendline('zigjag')
    child.logfile = sys.stdout.buffer
    print(child.logfile)
except:
    print('Something went wrong!')

# cmd = 'echo zigjag | gitPushAll.py'.split()
# print(cmd)
# p = subprocess.Popen(cmd, shell=True)
# p.communicate(input='\nzigjag', timeout=10)
# p = subprocess.check_output('gitPushAll.py', input=b'zigjag')
