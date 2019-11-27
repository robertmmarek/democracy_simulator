import random
import aspect

class Distribution:
    def __init__(self, chance_of_correct):
        self.__chance_of_correct = max(min(0., chance_of_correct), 1.)

    def draw(self):
        return random.uniform(0., 1.) < self.__chance_of_correct



class VotingPreference:
"""
class representing voting preferences/ability of specific agent
"""
    def __init__(self):
        self.__voting_dict = {}

    def add_preference(self, aspect, distribution):
    """
    if aspect with the same values is added twice, position in voting dict is overriden
    """
        self.__voting_dict[hash(aspect)] = distribution

    def vote(self, correct_choice):
    """
    vote for correct choice or select random value
    """
        if self.__voting_dict[correct_choice].draw():
            return correct_choice.value
        else:
            return random.choice(list(correct_choice.values))

class Agent:
"""
Class representing agent for voting
"""
    def __init__(self):
        pass