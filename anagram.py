# return True if two given words are anagrams
# example; is_anagram(cat,tac) returns true
# while is_anagram(cat,tic) returns false

def is_anagram(word1, word2):
    # check if they are same length
    if len(word1) != len(word2):
        return False
    # create a list of 26 characters
    results = [0] * 26 # [0,0,0,.....] > [a,b,c,d,....z]
    # make both inputs all lower case
    word1 = word1.lower()
    word2 = word2.lower()
    # loop through first word and add 1 to corresponding index in the results list
    # same time, loop through second word and subtract 1 from corresponding index
    for char1, char2 in zip(word1, word2):
        results[ord(char1) - 97] += 1
        results[ord(char2) - 97] -= 1
    # we check our results to see if there are any non-zeros

    for i in results:
        if i != 0:
            return False
    return True


print(is_anagram('cat','tic'))
    