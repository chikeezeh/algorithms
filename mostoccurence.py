from re import findall
from collections import Counter
from sys import argv
"""
read in a file , return the most occuring word in the file.
constraints:
1. only alphabetical words, so nothing like a1n3
2. no symbols like '!^*'...etc
"""
#read in the files
def top_words(file_path, n=1):
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

    return sorted_word_counter[:n]

def top_words_counter(filepath, n=1):
    with open(filepath, 'r',encoding='utf-8') as text_file:
        contents = text_file.read().lower()
    contents = findall(r'\b[a-z]+\b', contents)
    word_counts = Counter(contents)
    return word_counts.most_common(n)

def top_words_cli(filepath, n=1):
    with open(filepath, 'r',encoding='utf-8') as text_file:
        contents = text_file.read().lower()
    contents = findall(r'\b[a-z]+\b', contents)
    word_counts = Counter(contents)
    return word_counts.most_common(n)

if __name__ == "__main__":
    if len(argv) < 2:
        print(f"Usage: python {argv[0]} <filename>")
    else:
        print(top_words_cli(argv[1], int(argv[2])))

# print(top_words('poem.txt',5))
# print(top_words_counter('poem.txt',5))
