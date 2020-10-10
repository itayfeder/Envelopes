from abc import abstractmethod, ABC
class Strategy(ABC):

    @abstractmethod
    def play(self):
        '''
        abstract method, used to call the `perform_strategy` method to start the strategy.
        :return: the money that was returned by the `perform_strategy` method.
        '''
        print(f"This is abstract strategy, don't use it!")

    @abstractmethod
    def perform_strategy(self, counter):
        '''
        abstract method, starts the strategy on the given envelope array.
        :param `counter`: the envelope array that you want to do the strategy on.
        :return: the money that was in the chosen envelope from that array.
        '''
        print(f"This is abstract strategy, don't use it!")

    @abstractmethod
    def display(self):
        '''
        abstract method, displays the strategy.
        '''
        print(f"This is abstract strategy, don't use it!")