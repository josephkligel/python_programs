#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(description="Demonstration")
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
