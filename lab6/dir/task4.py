def countLine(f):
    c = 0
    for i in f:
        c += 1
    return c

file = open("file.txt", "r")
print(countLine(file))
file.close()
