#!/usr/bin/env python
import sys, os
import argparse
import re

parser = argparse.ArgumentParser(description='Generate templates for html, python, bash, or C. Example: "python templates.py --html template.html"')
parser.add_argument('--html', help='Create an html file template')
parser.add_argument('-p', '--python', help='Create a python file template')
parser.add_argument('-c', '--cpro', help='Create a C programming template')
parser.add_argument('-c++', '--cpp', help='Create a C++ program template')
parser.add_argument('-b', '--bash', help='Create a bash template')
args = parser.parse_args()

def main():
    if sys.argv[2] != True:
        sys.argv[2] == 'generated_template'
    if args.html:
        with open(sys.argv[2] + '.html', 'w') as fh:
            fh.write("""<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    
  </body>
</html>""")
    elif args.python:
        with open(sys.argv[2] + '.py', 'w') as fh:
            fh.write('#!/usr/bin/env python')
    elif args.cpro:
        with open(sys.argv[2] + '.c', 'w') as fh:
            fh.write("""#include <stdio.h>

int main(int argc, int *argv[]){


\treturn(0);
}""")
    elif args.cpp:
        with open(sys.argv[2] + '.cpp', 'w') as fh:
            fh.write("""#include <iostream>

using namespace std;

int main(int argc, char *argv[]){


\treturn 0;
}""")
    elif args.bash:
        with open(sys.argv[2] + '.sh', 'w') as fh:
            fh.write("""#!/usr/bin/env bash""")

if len(sys.argv) > 2:
    main()
else:
    os.system(f'python {__file__} --help') 
