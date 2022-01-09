#!/usr/bin/python3
from websites import *
from os import *

print("What website would you like to go to?")
url = str(input("Type here: ")).lower()

result = returnUrl(url)

try:
	gotoUrl = "google-chrome " + result
	system(gotoUrl)
except:
	print("No website of that name is listed in the dictionary.")
