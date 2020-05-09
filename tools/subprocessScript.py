#!/usr/bin/python
import subprocess

the_command = ['ls', '-a', '/var']

stdout, stderr = subprocess.Popen(the_command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
print(f'stdout: {stdout}', f'stderr: {stderr}', sep='\n')

# the_run = subprocess.run(the_command)
# print(the_run)
