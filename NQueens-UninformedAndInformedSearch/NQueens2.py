from simpleai.search import breadth_first, limited_depth_first,iterative_limited_depth_first
from simpleai.search.models import SearchProblem
from simpleai.search.traditional import depth_first, uniform_cost
import NQueens as queens
import timeit


class NQueensProblems(SearchProblem):
    def __init__(self,N):
        self.queen = queens.NQueens(N)
        self.initial_state = self.queen.state

    def actions(self,state):
        actions = []
        for i in range(len(state)):
            for j in range(len(state)):
                if (int(state.__getitem__(i)) != j + 1):
                    actions.append([i + 1, j + 1])
        return actions

    def result(self,state,action):
        state = list(state)
        state[action[0] - 1] = str(action[1])
        state = ''.join(state)
        return state

    def is_goal(self,state):
        control = queens.NQueens.coutAtackNum(self.queen.N,state)
        return control==2

if __name__ == '__main__':
    problem = NQueensProblems(4)
    print(" Enter 1 for breadth_first",'\n',"Enter 2 for uniform_cost",'\n',"Enter 3 for depth_first",'\n',
          "Enter 4 for limited_depth_first",'\n',"Enter 5 for iterative_limited_depth_first")
    num = int(input("Please enter number"))

    if (num==1):
        print("breadth_first")
        start = timeit.default_timer()
        result = breadth_first(problem)
        stop = timeit.default_timer()
        print("Resulting Path :")
        print(result.path())
        for i in range(len(result.path())):
            if i < len(result.path()) - 1:
                print(result.path()[i + 1][0])
                print("{0}. Action: {1}. Queen is moved to {2}".format(i + 1, result.path()[i + 1][0][0],
                                                                       result.path()[i + 1][0][1]))
        print("Resulting State :", result.path()[len(result.path()) - 1][1])
        print('Time: ', stop - start)
        print("Total Cost : ", len(result.path()) - 1)
    elif (num==2):
        print("uniform_cost")
        start = timeit.default_timer()
        result = uniform_cost(problem)
        stop = timeit.default_timer()
        print("Resulting Path :")
        print(result.path())
        for i in range(len(result.path())):
            if i < len(result.path()) - 1:
                print(result.path()[i + 1][0])
                print("{0}. Action: {1}. Queen is moved to {2}".format(i + 1, result.path()[i + 1][0][0],
                                                                       result.path()[i + 1][0][1]))
        print("Resulting State :", result.path()[len(result.path()) - 1][1])
        print('Time: ', stop - start)
        print("Total Cost : ", len(result.path()) - 1)
    elif (num==3):
        print("depth_first")
        start = timeit.default_timer()
        result = depth_first(problem, graph_search=True)
        stop = timeit.default_timer()
        print("Resulting Path :")
        print(result.path())
        for i in range(len(result.path())):
            if i < len(result.path()) - 1:
                print(result.path()[i + 1][0])
                print("{0}. Action: {1}. Queen is moved to {2}".format(i + 1, result.path()[i + 1][0][0],
                                                                       result.path()[i + 1][0][1]))
        print("Resulting State :", result.path()[len(result.path()) - 1][1])
        print('Time: ', stop - start)
        print("Total Cost : ", len(result.path()) - 1)
    elif (num==4):
        limit = input("Enter a limit: ")
        if (limit.isdecimal()):
            num = int(limit)
        print("limited_depth_first")
        limit = None
        start = timeit.default_timer()
        result = limited_depth_first(problem ,depth_limit=num)
        methodName = f"Limited Depth First (Limit: {limit})"
        stop = timeit.default_timer()
        print("Resulting Path :")
        print(result.path())
        for i in range(len(result.path())):
            if i < len(result.path()) - 1:
                print(result.path()[i + 1][0])
                print("{0}. Action: {1}. Queen is moved to {2}".format(i + 1, result.path()[i + 1][0][0],
                                                                       result.path()[i + 1][0][1]))
        print("Resulting State :", result.path()[len(result.path()) - 1][1])
        print('Time: ', stop - start)
        print("Total Cost : ", len(result.path()) - 1)

    else :
        print("iterative_limited_depth_first")
        start = timeit.default_timer()
        result = iterative_limited_depth_first(problem)
        stop = timeit.default_timer()
        print("Resulting Path :")
        print(result.path())
        for i in range(len(result.path())):
            if i < len(result.path()) - 1:
                print(result.path()[i + 1][0])
                print("{0}. Action: {1}. Queen is moved to {2}".format(i + 1, result.path()[i + 1][0][0],
                                                                       result.path()[i + 1][0][1]))
        print("Resulting State :",result.path()[len(result.path())-1][1])
        print('Time: ', stop - start)
        print("Total Cost : ", len(result.path()) - 1)




