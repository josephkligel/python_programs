#!/usr/bin/python3
# mclip.py - A multi-clipboard program

TEXT = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """I am busy""",
    'upsell': """Buy this now!"""
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

# def argues():
#     print(sys.argv)
#
# argues()
