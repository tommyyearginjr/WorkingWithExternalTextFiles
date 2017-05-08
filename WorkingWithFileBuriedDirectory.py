# Created 5/8/17 by Tommy H. Yeargin, Jr. Namaste.
from BibleBookIndex import books
ExternalFile = input('What book of the Bible do you want to read? ')
ChapterNumber = input('What chapter? ')
Target = './bible/{}'.format(books.index(str(ExternalFile)))+'/ch'+ChapterNumber+'.txt'
Target = str(Target)
f = open(Target)
VerseList = []
for line in f:
    if line != '' and line != '\n':
        VerseList.append(line.rstrip()) # rstrip() removes '\n' from end of each string.
verse = input("Which verse would you like to look at? 1-{}: ".format(len(VerseList)-1))
verse = int(verse)
if verse == 0 or verse > len(VerseList):
    print("Verse number is out of range!")
else:
    print(VerseList[verse])
f.close()
