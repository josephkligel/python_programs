import pyinputplus as pyip
import re

def ceasar_encode(aString):
    return ''.join([chr(ord(letter)+7) for letter in aString])

def ceasar_decode(aString):
    return ''.join([chr(ord(letter)-7) for letter in aString])

if __name__ == '__main__':
    inputstring = str(input('Enter a string of characters to encode: '))
    print(ceasar_encode(inputstring))
