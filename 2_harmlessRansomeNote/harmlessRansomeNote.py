noteText = 'This is a secret note for you from a secret admirer'

magazineText ='''puerto rico is a great place you must hike far from town to find
a secret waterfall that I am an admirer of but note that it is not as hard as it
seems this is my advice for you'''
def harmlessRansomeNote(a,b):
    if len(a) > len(b):
        return a
        


if __name__ == '__main__': # allows the program to be run by calling the file name
    harmlessRansomeNote(noteText,magazineText)
