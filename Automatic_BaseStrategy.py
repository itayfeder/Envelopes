from strategy import Strategy
from envelope import Envelope
from random import randrange
class automatic_BaseStrategy(Strategy):

    def __init__(self, envelope_array):
        '''

        :param envelope_array: array of envelopes that is recived
        '''
        self.envelope_array = envelope_array
        self.randnum = randrange(0, 100)

    def play(self):
        '''
        promps text and runs preform_strategy
        :return: returns the function preform_strategy
        '''
        print("The Automatic Base Strategy has been chosen.")
        return self.perform_strategy()

    def perform_strategy(self, counter = 0):
        '''
        chooses a random packet
        :param counter:
        :return: returns amount of money
        '''
        return self.envelope_array[self.randnum].money

    def display(self):
        '''
        strategy description
        :return:
        '''
        print("this is the Automatic Base Strategy. a random packet is chosen and opened.")
