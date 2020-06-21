#!/usr/bin/env python
import os
import sys
import argparse

print(f'Compiling...\n')
os.system(f'g++ -Wall {sys.argv[1]} -o {sys.argv[2]}')

for arg in sys.argv:
    if arg == '--run':
        print('Running...\n')
        os.system(f'./{sys.argv[2]}')
