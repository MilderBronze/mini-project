import os

module_dir = os.path.dirname(__file__)
WORD_LIST = os.path.join(module_dir, "sowpods.txt")
wordlist = open(WORD_LIST).readlines()

wordlist = [word.lower().strip() for word in wordlist]

