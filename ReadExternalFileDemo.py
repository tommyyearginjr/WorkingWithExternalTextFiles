ExternalFile = 'TurningBibleChapterTextFilesIntoLists/ch01.txt'
f = open(ExternalFile)
names = []
for line in f:
    if line != '' and line != '\n':
        names.append(line.rstrip()) # rstrip() removes '\n' from end of each string.
verse = input("Which verse would you like to look at? 1-{}: ".format(len(names)-1))
verse = int(verse)
if verse == 0 or verse > len(names):
    print("Verse number is out of range!")
else:
    print(names[verse])
f.close()




# By: Tommy H. Yeargin, Jr. I bid you peace.
