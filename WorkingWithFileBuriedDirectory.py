# Created 5/8/17 by Tommy H. Yeargin, Jr. Namaste.

ExternalFile = input('What book of the Bible do you want to read? ')
ChapterNumber = input('What chapter? ')
Target = './bible/'+ExternalFile+'/ch'+ChapterNumber+'.txt'
Target = str(Target)
f = open(Target)
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
