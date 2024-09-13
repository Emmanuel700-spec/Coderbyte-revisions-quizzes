# main.py
from file_utils import load_words
from palindrome import find_palindromes

def main():
    word_list = load_words('dictionary.txt')
    if word_list:  # Check if the list is not empty
        palindromes = find_palindromes(word_list)
        print(f"Palindromes found ({len(palindromes)}):")
        for word in palindromes:
            print(word)
    else:
        print("No words loaded to check for palindromes.")

if __name__ == "__main__":
    main()
