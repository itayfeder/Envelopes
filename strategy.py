from abc import abstractmethod, ABC
import random


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


class N_max_strategy(Strategy):
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        print('You chose the max number after open some envelopes strategy!')
        self.perform_strategy(self.envelopes)

    def perform_strategy(self, counter):
        counter = self.envelopes
        num_of_envelopes = len.counter * random.randint(1, 75) // 100
        max = 0
        for i in range(num_of_envelopes - 1):
            if counter[i].money > max:
                max = counter[i].money

        i = num_of_envelopes
        while max > counter[i].money or len(counter) == i:
            i += 1

        print(f"You'll bring to te wedding envelope {i} which has {counter[i].money}$ in it")

    def display(self):
        return "the num mas strategy -- the computer opens a random amount of envelopes and saves the highest. the, " \
               "he opens the rests until he find an envelope beyond the saved maximum or until the last one "
