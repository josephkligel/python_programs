import os, platform

print('-'*10 + 'System Info' + '-'*10)
print('Architecture:', platform.architecture(), platform.processor())
print('OS:', platform.platform())
print('Kernel Version:', platform.release())

print()

print('-'*10 + 'Python Info' + '-'*10)
print('Python Version:', platform.python_version())
print('Python Implementation:', platform.python_implementation())
print('Python Compiler:', platform.python_compiler())

print()

print('-'*10 + 'Session Info' + '-'*10)
print('Home Directory:', os.environ.get('HOME'))
print('Shell Directory:', os.environ.get('SHELL'))
print('Logname, Username:', os.environ.get('USERNAME') + ', ' + os.environ.get('LOGNAME'))
print('Hostname:', os.environ.get('HOSTNAME'))
print('Desktop Session:', os.environ.get('DESKTOP_SESSION'))
