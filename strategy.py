from abc import abstractmethod, ABC
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

    def perform_strategy(self, counter):
        '''
        chooses a random packet
        :param counter:holds envelope array
        :return: returns amount of money
        '''
        counter = self.envelope_array
        return counter[self.randnum].money

    def display(self):
        '''
        strategy description
        :return:
        '''
        print("this is the Automatic Base Strategy. a random packet is chosen and opened.")
