#!/usr/bin/python

#####################################################
# grabs a banner image from flaming text
# and saves it to the project directory as banner.png
#####################################################

import urllib
import random

word_file = "words.txt"
WORDS = open(word_file).read().splitlines()
word1 = random.choice(WORDS) + '+' + random.choice(WORDS)
myurl = "http://www.flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=dance-logo&text="+mytext
urllib.urlretrieve(myurl, "banner.png")
