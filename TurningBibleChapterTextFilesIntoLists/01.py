names = []
f = open('ch01.txt')
for line in f:
    if line != '' and line != '\n':
        names.append(line.rstrip()) # rstrip() removes '\n' from end of each string.
# for i in names:
#     print(i)
