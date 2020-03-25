fh = open("example.txt", 'r+')

fh.write("Yes, sir")
print(fh.read())

fh.close()
