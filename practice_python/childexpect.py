import sys
from pexpect import spawn, EOF

username = 'zigjag'
cmd = 'gitPushAll.py'
child = spawn(cmd, timeout=10)
child.logfile_read = sys.stdout

child.expect("Username for 'https://github.com':")
child.sendline(username)
child.expect(EOF)
child.close()
sys.exit(child.status)
