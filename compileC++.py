#!/usr/bin/env python
import os, sys

print(f'Compiling...\n')
os.system(f'g++ -Wall {sys.argv[1]} -o {sys.argv[2]}')

print('Running...\n\n')
os.system(f'./{sys.argv[2]}')
