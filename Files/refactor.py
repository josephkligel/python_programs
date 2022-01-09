import os

def refactor(file, newName):
    return os.rename(file.path, newName)
