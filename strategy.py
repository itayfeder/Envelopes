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


class BaseStrategy(Strategy):
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        print("You chose the 'choose with your gut' strategy!")
        self.perform_strategy(self.envelopes)

    def perform_strategy(self, counter):
        counter = self.envelopes
        n = 0  # counter
        chose = False  # have the user chose an envelope
        while n != len(counter) or chose == False:
            option = input(f'This envelope has {counter[n].money}$! would you send it to the wedding? (yes / no)')
            if option == "yes":
                chose = True
                print(f"You chose envelope {n + 1} which had {counter[n].money}$ to bring to the wedding.")
            elif n == len(counter):
                print(f"you checked all the envelopes! you'll take to the wedding the envelope you opened last which "
                      f"had {counter[n].money}$")
            counter.used = True
            n += 1
        return counter[n].money

    def display(self):
        return "the basic method -- choose your envelope with your feeling."
