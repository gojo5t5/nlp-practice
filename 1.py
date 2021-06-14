import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.corpus import gutenberg

url = "https://www.technologyreview.com/2021/06/11/1026135/ai-synthetic-data/"
# save text from the website to a variable
html = request.urlopen(url).read().decode("utf8")
# get rid of html syntax
raw = BeautifulSoup(html, "html.parser").get_text()
# split the text into words
tokens = word_tokenize(raw)
# get rid of unwanted tokens
tokens = tokens[100:-50]
text = nltk.Text(tokens)
# print(text.concordance("AI"))

raw = gutenberg.raw("melville-moby_dick.txt")
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
print(fdist.most_common(5))
