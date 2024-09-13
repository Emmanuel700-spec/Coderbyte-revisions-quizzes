# file_utils.py
import re

def load_words(filename):
    words = []
    try:
        with open(filename, "r") as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)
    except FileNotFoundError:
        print(f'Error: The file {filename} does not exist.')
    except IOError as e:
        print(f'Error reading file {filename}: {e}')
    finally:
        print("Finished trying to load words.")
    return words
