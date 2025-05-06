from re import findall

"""
read in a file , return the most occuring word in the file.
constraints:
1. only alphabetical words, so nothing like a1n3
2. no symbols like '!^*'...etc
"""
#read in the files
def top_words(file_path):
    with open(file_path, 'r',encoding='utf-8') as text_file:
        contents = text_file.read().lower()
    contents = findall(r'\b[a-z]+\b', contents) # remove non alphabetical characters
    # create a counter dictionary
    word_counter = {}
    for content in contents:
        if content in word_counter:
            word_counter[content] += 1
        else:
            word_counter[content] = 1
    # sort the dictionary based on the value of the counter
    # this will give us a list
    sorted_word_counter = sorted(word_counter.items(), key= lambda x: (-x[1]))

    return sorted_word_counter[:1]

print(top_words('poem.txt'))
