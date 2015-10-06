import random

word_file = "words.txt"
WORDS = open(word_file).read().splitlines()
word1 = 'First Choice: ' + random.choice(WORDS) + ' ' + random.choice(WORDS)
word2 = 'Second Choice: ' + random.choice(WORDS) + ' ' + random.choice(WORDS)
word3 = 'Third Choice: ' + random.choice(WORDS) + ' ' + random.choice(WORDS)
print word1
print word2
print word3
