import random
from math import comb
import NQueens as queens
from simpleai.search.models import SearchProblem
from simpleai.search import hill_climbing,hill_climbing_random_restarts,genetic
import timeit

class NQueensProblem(SearchProblem):

    def __init__(self, N):
        self.queen = queens.NQueens(N)
        self.initial_state = self.queen.state

    def actions(self,state):
        actions = []
        for i in range(len(state)):
            for j in range(len(state)):
                if (int(state.__getitem__(i)) != j + 1):
                    actions.append([i + 1, j + 1])
        return actions

    def is_goal(self,state):
        control = queens.NQueens.coutAtackNum(self.queen.N,state)
        return control==0

    def result(self,state,action):
        state = list(state)
        state[action[0] - 1] = str(action[1])
        state = ''.join(state)
        return state

    def heuristic(self, state):
        control = queens.NQueens(self.queen.N, state)
        return control.count_attacking_pairs()

    def value(self, state):
        control = queens.NQueens.coutAtackNum(self.queen.N, state)
        non_attack = comb(self.queen.N,2)-control
        return non_attack

    def generate_random_state(self):
        control= queens.NQueens.generate_random_state2(self.queen.N);
        return control

    def crossover(self, state1, state2):
        crossoverpoint = random.randint(1, self.queen.N)
        newStateLeft = state1[0:crossoverpoint]
        newStateRight = state2[crossoverpoint: self.queen.N]
        newState = newStateLeft + newStateRight
        return newState

    def mutate(self, state):
        randomlocation = random.randint(1, self.queen.N)
        randomnewvalue = str(random.randint(1, self.queen.N))
        temp = list(state)
        temp[randomlocation - 1] = randomnewvalue
        newState = "".join(temp)
        return newState
if __name__ == '__main__':

    problem = NQueensProblem(4)
    print("********")
    print("hill_climbing")
    start = timeit.default_timer()
    result = hill_climbing(problem,iterations_limit=1000)
    stop = timeit.default_timer()
    print("Resulting Path :")
    print(result.path())
    print("Resulting State :", result.path()[len(result.path()) - 1][1])
    print("coutAtackNum : ", queens.NQueens.coutAtackNum(4, result.path()[len(result.path()) - 1][1]))
    print('Time: ', stop - start)
    print("********")
    print("hill_climbing_random_restarts")
    start = timeit.default_timer()
    result = hill_climbing_random_restarts(problem, restarts_limit=100)
    stop = timeit.default_timer()
    print("Resulting Path :")
    print(result.path())
    print("Resulting State :", result.path()[len(result.path()) - 1][1])
    print("coutAtackNum : ",queens.NQueens.coutAtackNum(4,result.path()[len(result.path()) - 1][1]))
    print('Time: ', stop - start)
    print("********")
    print("genetic")
    start = timeit.default_timer()
    result = genetic(problem)
    stop = timeit.default_timer()
    print("Resulting Path :")
    print(result.path())
    print("Resulting State :", result.path()[len(result.path()) - 1][1])
    print("coutAtackNum : ",queens.NQueens.coutAtackNum(4,result.path()[len(result.path()) - 1][1]))
    print('Time: ', stop - start)


# while(True):
#     n = input("Enter N: ")
#     if(n.isdecimal()):
#         nInt = int(n)
#         problem = NQueensProblem(nInt)
#         start_time = time.time()
#         result = greedy(problem)
#         paths = result.path()
#         totalTime = (time.time() - start_time)
#         cost = -1
#         print(f"Applying Method greedy")
#         for path in paths:
#             cost += 1
#             print(f"({path[0]}, {path[1]})")
#         print(f"Total Cost: {cost}")
#         print(f"Total Time: {totalTime}")
#         break
#     else:
#         print("This part need int value")




