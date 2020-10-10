from abc import abstractmethod, ABC
from random import randrange


class Strategy(ABC):

    @abstractmethod
    def play(self):
        '''
        abstract method, used to call the `perform_strategy` method to start the strategy.
        :return: the money that was returned by the `perform_strategy` method.
        '''

    @abstractmethod
    def perform_strategy(self, counter):
        '''
        abstract method, starts the strategy on the given envelope array.
        :param `counter`: the envelope array that you want to do the strategy on.
        :return: the money that was in the chosen envelope from that array.
        '''

    @abstractmethod
    def display(self):
        '''
        abstract method, displays the strategy.
        '''


class Automatic_BaseStrategy(Strategy):

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
        print(self.perform_strategy(self.envelope_array))

    def perform_strategy(self, counter):
        '''
        chooses a random packet
        :param counter:holds envelope array
        :return: returns amount of money
        '''
        return counter[self.randnum].money

    def display(self):
        '''
        strategy description
        :return:none
        '''
        return "this is the Automatic Base Strategy. a random packet is chosen and opened."


class N_max_strategy(Strategy):
    def __init__(self, envelope_array, N = 3):
        '''

        :param envelope_array: array of envelopes that is recived
        :param N: number of peaks foe perform_strategy
        '''
        self.envelope_array = envelope_array
        self.N = N

    def play(self):
        '''
        promps text and runs perform_strategy
        :return: returns the function preform_strategy
        '''
        print("The N max strategy has been chosen.")
        print(self.perform_strategy(self.envelope_array))

    def perform_strategy(self, counter):
        '''
        this strategy checks for peaks, and opens the envelope on the Nth one
        :param counter: envelope array placeholder
        :return: returns packet in Nth peak
        '''
        peak_counter = 0
        max_envelope = counter[0].money

        if counter[0].money > counter[1].money:
            peak_counter += 1
        for num in range(1, len(counter) - 1):
            if peak_counter == self.N:
                return max_envelope
            if (counter[num - 1].money < counter[num].money) and (counter[num].money > counter[num + 1].money):
                peak_counter += 1
                max_envelope = counter[num].money
        return counter[-1].money

    def display(self):
        '''
        strategy description
        :return:none
        '''
        return "this is the N max strategy. it selects the Nth peak packet and opens it."
