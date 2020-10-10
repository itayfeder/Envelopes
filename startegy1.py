from envelope import Envelope


def strategy1():
    stop = False  # when to stop the while - when user takes an envelope
    n = 0 #counter
    while stop == False // n != 100:  # when user took the envelope or after 100 envelopes
        env = Envelope()  # new envelope and deleting the previous one
        print("this envelop has ", {0}, " dollars. would U take the money (type 'True' to take, 'False' to continue)", env.money)
        stop = bool(input())
        n += 1  # to end the while loop, max 100 envelopes
        env.used = stop
    if n == 100:  # if the user didn't manage to decide when to take the envelope
        print("because U couldn't decide which envelope to open, U get the last one!")
    print("U got ", {0}, " dollars", env.money)
