ExternalFile = 'TurningBibleChapterTextFilesIntoLists/ch01.txt'
f = open(ExternalFile)
names = []
for line in f:
    if line != '' and line != '\n':
        names.append(line.rstrip()) # rstrip() removes '\n' from end of each string.
# print(f.read())

verse = input("Which verse would you like to look at? 1-{}: ".format(len(names)-1))
f.close()
