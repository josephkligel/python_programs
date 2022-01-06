import os

def pwd():
    return os.getcwd()

if __name__ == '__main__':
    print("Current Working Directory\n-----------------")
    print(pwd())
