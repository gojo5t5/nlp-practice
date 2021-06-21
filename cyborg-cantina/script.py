from collections import Counter
from responses import responses, blank_spot
from user_functions import (
    preprocess,
    compare_overlap,
    pos_tag,
    extract_nouns,
    compute_similarity,
)
import spacy

word2vec = spacy.load("en")

exit_commands = ("quit", "goodbye", "exit", "no")


class ChatBot:

    # check if user wants to exit the program
    def make_exit(self, user_message):
        for ec in exit_commands:
            if ec in user_message:
                print("Goodbye")
                return True

    # conversation starter method
    def chat(self):
        user_message = input("What would you like to know about our menu today??")
        while not self.make_exit(user_message):
            user_message = self.respond(user_message)

    # matches user intent with predefined responses in responses.py
    def find_intent_match(self, responses, user_message):
        # create bows
        bow_user_message = Counter(preprocess(user_message))
        bow_responses = [Counter(preprocess(response)) for response in responses]
        # make similarity list with comparable values
        similarity_list = [
            compare_overlap(response, bow_user_message) for response in bow_responses
        ]
        # find the index of the response that best matches the user intent
        response_index = similarity_list.index(max(similarity_list))
        return responses[response_index]

    def find_entities(self, user_message):
        # part of speech tag the bow
        tagged_user_message = pos_tag(preprocess(user_message))
        # extract nouns from user input
        message_nouns = extract_nouns(tagged_user_message)
        tokens = word2vec(" ".join(message_nouns))
        category = word2vec(blank_spot)
        # compute similarities between the noun tokens and our category
        word2vec_result = compute_similarity(tokens, category)
        # This will sort the result list by ascending similarity score
        word2vec_result.sort(key=lambda x: x[2])
        if not word2vec_result:
            return blank_spot
        return word2vec_result[-1][0]

    def respond(self, user_message):
        # intent match
        best_response = self.find_intent_match(responses, user_message)
        # entity extraction
        entity = self.find_entities(user_message)
        print(best_response.format(entity))
        # ask for more questions from the user
        input_message = input("Another question??")
        return input_message


# initialize ChatBot instance below:
cantina = ChatBot()
# call .chat() method below:
cantina.chat()
