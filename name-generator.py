import random

word_file = "words.txt"
WORDS = open(word_file).read().splitlines()
word1 = 'Choice 1: ' + random.choice(WORDS) + ' ' + random.choice(WORDS)
word2 = 'Choice 2: ' + random.choice(WORDS) + ' ' + random.choice(WORDS)
word3 = 'Choice 3: ' + random.choice(WORDS) + ' ' + random.choice(WORDS)
print word1
print word2
print word3
