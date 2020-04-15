import sys, subprocess
from pexpect import popen_spawn, spawn
import pexpect

# cmd = "echo 'Type yes or no: '"
# child = spawn('ls -l')
# child.expect('Type yes or no: ')
# print(child.)
# child.sendline('yes')

cmd = 'echo zigjag | gitPushAll.py'.split()
print(cmd)
p = subprocess.Popen(cmd, shell=True)
# p.communicate(input='\nzigjag', timeout=10)
# p = subprocess.check_output('gitPushAll.py', input=b'zigjag')
