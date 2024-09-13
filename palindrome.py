# palindrome.py
def find_palindromes(word_list):
    palindromes = []
    for word in word_list:
        # Check if the word has more than one letter and is a palindrome
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)
    return palindromes

