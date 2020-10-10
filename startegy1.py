from envelope import Envelope


def strategy1():
    stop = False
    n = 0
    while (stop==False // n != 100):
        env = Envelope() #create new envelope and deleting the previous one
        print("this envelop has ", {0}, " dollars. would U take the money (type 'True' to take, 'False' to continue)", env.money)
        stop = bool(input())
        n += 1 #to end the while loop, max 100 envelopes
        env.used = stop
    if (n == 100): #if the user didn't manage to decide when to take the envelope
        print("because U couldn't decide which envelope to open, U get the last one!")
        print("U get ", {0}, " dollars", env.money)
