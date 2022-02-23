import numpy
import string
import random
from math import comb


class NQueens():
    """ class constructorff
    initializes the instance attributes N and state """
    global myBoard
    global N
    global state

    def __init__(self, N):
        self.N = N
        self.myBoard = numpy.zeros((self.N, self.N))
        self.set_state()
    def __str__(self):
        return f"N: {self.N} State: {self.state}"

    def set_state(self):
        while (True):
            print("How do you want to set state?\n1. Set state manually\n2. Set state randomly")
            val = input("Enter selection: ")
            if (val == "1"):
                stateInput = input("enter state: ")
                if (self._is_valid(stateInput)):
                    for i in range(self.N):
                        self.myBoard[self.N - int(stateInput.__getitem__(i))][i] = 1
                    self.state = stateInput
                    break
                else:
                    print("invalid state! try again")
            elif (val == "2"):
                self.generate_random_state()
                break
            else:
                print("Wrong Selection")

    def generate_random_state(self):
        digit = string.digits
        state_str = ""
        for i in range(self.N):
            while (True):
                if (len(state_str) == self.N):
                    break
                else:
                    s = ''.join(random.choice(digit))
                    if (int(s) <= int(self.N) and int(s) != 0):
                        state_str = state_str + '' + s

        self.state = state_str
        for i in range(self.N):
            self.myBoard[self.N - int(state_str.__getitem__(i))][i] = 1
        return state_str

    def _is_valid(self, state_str):
        if not(self.N == len(state_str)):
            return False
        for i in range(self.N):
            if not (state_str[i].isdigit() and int(state_str[i]) <= self.N and int(state_str[i])!=0):
                return False
        return True

    def count_attacking_pairs(self):
        diags = [self.myBoard[::-1, :].diagonal(i) for i in range(-(self.N - 2), self.N - 1)]
        diags.extend(self.myBoard.diagonal(i) for i in range(self.N - 2, -(self.N - 1), -1))
        sum1 = 0
        for n in diags:
            a = n.tolist()
            c = 0
            for i in range(len(a)):
                if (a[i] == 1):
                    c = c + 1
            if (c > 1):
                sum1 = sum1 + comb(c, 2)
        sum2 = 0
        for i in range(len(self.myBoard)):
            count = 0
            for j in range(len(self.myBoard)):
                if (self.myBoard[i][j] == 1):
                    count = count + 1
            if (count > 1):
                sum2 = sum2 + comb(count, 2)
        return sum1 + sum2
    @staticmethod
    def coutAtackNum(N,state):
        myBoard = numpy.zeros((N, N))
        for i in range(N):
            myBoard[N - int(state.__getitem__(i))][i] = 1
        diags = [myBoard[::-1, :].diagonal(i) for i in range(-(N - 2), N - 1)]
        diags.extend(myBoard.diagonal(i) for i in range(N - 2, -(N - 1), -1))
        sum1 = 0
        for n in diags:
            a = n.tolist()
            c = 0
            for i in range(len(a)):
                if (a[i] == 1):
                    c = c + 1
            if (c > 1):
                sum1 = sum1 + comb(c, 2)
        sum2 = 0
        for i in range(len(myBoard)):
            count = 0
            for j in range(len(myBoard)):
                if (myBoard[i][j] == 1):
                    count = count + 1
            if (count > 1):
                sum2 = sum2 + comb(count, 2)
        return sum1 + sum2






