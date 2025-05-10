"""
Given a sentence convert it to goat latin using the rules below

1. If a word starts with a consonant, move the first letter to the end and add ma.
    so Goat --> oatGma
2. If a word starts with a vowel, add ma at the end
    so ankle --> anklema
3. Add 'a' to the end of each word, with 1st word having a, 2nd word aa, 3rd word aaa ....
    so I am a duck --> Ia amaa aaaa duckaaaa
Combining all the rules:

goat_latin('I speak Goat Latin') --> 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'

"""
def consonant_word(word):
    word = word[1:] + word[0] + 'ma'
    return word

def vowel_word(word):
    word = word + 'ma'
    return word
def add_a(word: str, n:int):
    word = word + 'a'*n
    return word

def main(sentence):
    # result list
    result = []
    vowel = {'a','e','i','o','u','A','E','I','O','U'}
    # apply our helper fnx depending on if vowel or consonant.
    # loop through each word in sentence
    for index, word in enumerate(sentence.split()):
        if word[0] in vowel:
            result.append(add_a(vowel_word(word), index+1))
        else:
            result.append(add_a(consonant_word(word), index+1))
    print(' '.join(result))

main('I am a duck g')
main('I am understand goat latin')