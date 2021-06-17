from nltk import pos_tag

user_message = [
    "i",
    "ordered",
    "two",
    "t-shirts",
    "this",
    "past",
    "weekend",
    "when",
    "will",
    "my",
    "package",
    "be",
    "shipped",
]

tagged_user_message = pos_tag(user_message)


def extract_nouns(tagged_message):
    message_nouns = list()
    for tupl in tagged_message:
        if "NN" in tupl[1]:
            message_nouns.append(tupl[0])

    return message_nouns


user_message_nouns = extract_nouns(tagged_user_message)
print(user_message_nouns)
