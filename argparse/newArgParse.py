#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(description='A program to test the concepts of Argparse.')
parser.add_argument('-m', metavar='msg', type=str, help='a message string to be printed')
args = parser.parse_args()

print(args.m)
