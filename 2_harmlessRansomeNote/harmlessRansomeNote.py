noteText = 'this is a note'

magazineText ='take note this is all the magazine text in a magazine'

def harmlessRansomeNote(a,b):
    noteArr = a.split(' ') # make a list out of the strings in noteText
    magazineArr = b.split(' ') # make a list out of the strings in magazineText
    # create a dictionary using magazineArr, the key is the number of times
    # the value in the list appears.
    magazineDict ={}
    for i in magazineArr:
        if i not in magazineDict:
            magazineDict[i] = 0
        magazineDict[i] += 1

    # bolean to keep track of if we have enough words to make the ransom note.
    noteIsPossible = True
    # now we loop through the noteArr, and check if each word is in our magazineDict
    # as we loop through, we decrease the value of each word in the magazineDict

    for i in noteArr:
        if i in magazineDict:
            magazineDict[i] -=1
            if magazineDict[i] < 0:
                noteIsPossible = False
        else:
            noteIsPossible = False
    return noteIsPossible

if __name__ == '__main__': # allows the program to be run by calling the file name
    print(harmlessRansomeNote(noteText,magazineText))
