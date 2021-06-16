import os
import gensim
import spacy
import random
from president_helper import (
    read_file,
    process_speeches,
    merge_speeches,
    get_president_sentences,
    get_presidents_sentences,
    most_frequent_words,
)

# get list of all speech files
files = sorted([file for file in os.listdir() if file[-4:] == ".txt"])
print(files)

# read each speech file
speeches = [read_file(file) for file in files]

# preprocess each speech
processed_speeches = process_speeches(speeches)
print(processed_speeches[0])
print(processed_speeches[0][0])
print(processed_speeches[0][0][0])

# merge speeches
all_sentences = merge_speeches(processed_speeches)

# view most frequently used words
most_freq_words = most_frequent_words(all_sentences)
# print(most_freq_words[:10])

# create gensim model of all speeches
all_prez_embeddings = gensim.models.Word2Vec(
    all_sentences, size=96, window=5, min_count=1, workers=2, sg=1
)

# view words similar to freedom
similar_to_freedom = all_prez_embeddings.most_similar("freedom", topn=20)
print(similar_to_freedom)

# get President Roosevelt sentences
roosevelt_sentences = get_president_sentences("franklin-d-roosevelt")


# view most frequently used words of Roosevelt
roosevelt_most_freq_words = most_frequent_words(roosevelt_sentences)
# print(roosevelt_most_freq_words)

# create gensim model for Roosevelt
roosevelt_embeddings = gensim.models.Word2Vec(
    roosevelt_sentences, size=96, window=5, min_count=1, workers=2, sg=1
)

# view words similar to freedom for Roosevelt
roosevelt_similar_to_freedom = roosevelt_embeddings.most_similar("freedom", topn=20)
print(roosevelt_similar_to_freedom)


# get sentences of multiple presidents
rushmore_prez_sentences = get_presidents_sentences(
    ["washington", "jefferson", "lincoln", "theodore-roosevelt"]
)

# view most frequently used words of presidents
rushmore_most_freq_words = most_frequent_words(rushmore_prez_sentences)
# print(rushmore_most_freq_words)

# create gensim model for the presidents
rushmore_embeddings = gensim.models.Word2Vec(
    rushmore_prez_sentences, size=96, window=2, min_count=1, workers=2, sg=1
)

# view words similar to freedom for presidents
rushmore_similar_to_freedom = rushmore_embeddings.most_similar("freedom", topn=20)
