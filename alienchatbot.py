# importing regex and random libraries
import re
import random


class AlienBot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? ",
    )

    def __init__(self):
        self.alienbabble = {
            "describe_planet_intent": r".*\s* your planet.*",
            "answer_why_intent": r"^why.*\s*are.*\?$",
            "cubed_intent": r".*cube.*(\d+).*",
        }

    # greet the user
    def greet(self):
        self.name = input("Bip-Bop. What is your name? ")
        will_help = input(
            f"Hi {self.name}, I'm YODAD. I'm not from this planet. Will you help me learn about your planet? "
        )
        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return
        self.chat()

    # check if a user has used an exit command
    def make_exit(self, reply):
        for word in self.exit_commands:
            if word in reply:
                return True
        return False

    # allows user to chat with alien
    def chat(self):
        reply = input(random.choice(self.random_questions))
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    # match response pairs in alienbabble
    def match_reply(self, reply):
        for intent, regexp in self.alienbabble.items():
            found_match = re.match(regexp, reply)
            if found_match:
                if intent == "describe_planet_intent":
                    return self.describe_planet_intent()
                elif intent == "answer_why_intent()":
                    return self.answer_why_intent()
                elif intent == "cubed_intent":
                    return self.cubed_intent(found_match.groups()[0])
            else:
                return self.no_match_intent()

    # include responses about the alien's planet
    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species. ",
            "I am from Opidipus, the capital of the Wayward Galaxies. ",
        )
        return random.choice(responses)

    # include responses for why the alien is visiting
    def answer_why_intent(self):
        responses = (
            "I come in peace.",
            "I am here to collect data on your planet and its inhabitants.",
            "I heard the coffee is good. ",
        )
        return random.choice(responses)

    # returns cube of a number
    def cubed_intent(self, number):
        number = int(number)
        cubed = number ** 3
        return f"The cube of {number} is {cubed}. Isn't that cool? "

    # respond with something general
    def no_match_intent(self):
        responses = (
            "Please tell me more",
            "Tell me more!",
            "Why do you say that?",
            "I see. Can you elaborate?",
            "Interesting. Can you tell me more?",
        )
        return random.choice(responses)


# Create an instance of AlienBot below:
yodad = AlienBot()
yodad.greet()
