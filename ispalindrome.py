from re import sub
"""
Write a function that returns  True/False if a string is a palindrome or not
A Palindrome is a word that can be spelt both forward and backwards
Examples
MADAM
ADA
RACECAR
A man, a plan, a canal – Panama
"""
def is_palindrome(input_str: str) -> bool:
    """
    Returns True if the input string is a palindrome, False otherwise.
    Ignores non-alphanumeric characters and is case-insensitive.
    """
    # remove spaces and none alphabets, and make lower case
    clean_str = remove_non_alphanumeric(input_str).lower()
    # create a left and right pointer
    left = 0
    right = len(clean_str) - 1
    # loop till left pointer overtakes right pointer
    while left <= right:
        if clean_str[left] != clean_str[right]:
            return False
        left += 1
        right -= 1
    return True

def remove_non_alphanumeric(text: str) -> str:
    """
    Removes all non-alphanumeric characters from the input string.
    """
    return sub(r'[^a-zA-Z0-9]','',text)

print(is_palindrome('MADAM'))
print(is_palindrome('ADA'))
print(is_palindrome('RACECAR'))
print(is_palindrome('A man, a plan, a canal – Panama'))
print(is_palindrome('ICE'))
