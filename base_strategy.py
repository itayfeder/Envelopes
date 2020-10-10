from strategy import Strategy


class BaseStrategy(Strategy):
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def play(self):
        print("You chose the 'choose with your gut' strategy!")
        self.perform_strategy(self.envelopes)

    def perform_strategy(self, counter):
        n = 0  # counter
        chose = False  # have the user chose an envelope
        option = None  # later, the argument of the user's input
        while n != len(counter) or chose == False:
            option = input(
                f'This envelope has {self.envelopes[n].money}$! would you send it to the wedding? (yes / no)')
            if input == "yes":
                chose = True
                print(f"You chose envelope {n + 1} which had {self.envelopes[n].money}$ to bring to the wedding.")
            elif n == len(self.envelopes):
                print(f"you checked all the envelopes! you'll take to the wedding the envelope you opened last which "
                      f"had {self.envelopes[n].money}$")
            self.envelopes.used = True
            n += 1
        return self.envelopes[n].money

    def display(self):
        print(f'the basic method -- choose your envelope with your feeling.')
