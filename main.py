import copy
import random

COLORS = {
    "white": 1,
    "black": 2,
    "green": 3,
    "red": 4,
    "blue": 5,
    "yellow": 6
}
COLORS_LIST = [1, 2, 3, 4, 5, 6]
PEGS = {
    "black": 0,
    "white": 1
}


def getPossiblecombos():
    l = []
    for i in range(1, 7):
        for o in range(1, 7):
            for p in range(1, 7):
                for j in range(1, 7):
                    l.append([i, o, p, j])
    return l


def score(attempt: list, solution: list):
    black = 0
    white = 0
    solution = copy.copy(solution)
    attempt = copy.copy(attempt)
    for i in range(len(attempt)):
        if(attempt[i]==solution[i]):
            black+=1
            solution[i]=0
            attempt[i] = -1
    for i in range(len(attempt)):
        if(solution.__contains__(attempt[i])):
            white += 1
            index = solution.index(attempt[i])
            solution[index] = 0
            attempt[i] = 0
    return [black, white]
# attempt = [random.choice(COLORS_LIST) for i in range(4)]
# solution = [random.choice(COLORS_LIST) for i in range(4)]
# attempt = [1,2,3,4]
# solution = [1,1,1,1]
# print(score(attempt, solution))
# print(attempt, solution)
score([1,2,3,4],[3, 6, 1, 2] )

class Board:
    def __init__(self):
        self.response = []
        self.possiblecodes = getPossiblecombos()
        self.guess = []

    def getresponse(self, string: str):
        self.response = [int(i) for i in string.split(" ")]

    def checkAllBlack(self):
        return self.response[PEGS["black"]] == 4

    def removeImpossibleCodes(self):
        codescopy = copy.copy(self.possiblecodes)
        for i in self.possiblecodes:
            score = self.score(self.guess, i)
            if (score[PEGS["white"]] != self.response[PEGS["white"]]
                    or score[PEGS["black"]] != self.response[PEGS["black"]]):
                codescopy.remove(i)
        self.possiblecodes = codescopy

    def maxOptionsRemoved(self):
        self.guess= self.possiblecodes[0]
        return self.possiblecodes[0]
        pass

    @staticmethod
    def score(attempt: list, solution: list):
        black = 0
        white = 0
        solution = copy.copy(solution)
        attempt = copy.copy(attempt)
        for i in range(len(attempt)):
            if (attempt[i] == solution[i]):
                black += 1
                solution[i] = 0
                attempt[i] = -1
        for i in range(len(attempt)):
            if (solution.__contains__(attempt[i])):
                white += 1
                index = solution.index(attempt[i])
                solution[index] = 0
                attempt[i] = 0
        return [black, white]

    def convert_guess(self, l:list):
        new_l = ""
        for i in l:
            for key in COLORS.keys():
                if COLORS[key] == i:
                    new_l = new_l.__add__(str(key) + " ")
        return new_l

    # def whiteTag(self, color):
    #     color = int(color)
    #     copied = copy.deepcopy(self.possiblecodes)
    #     for i in self.possiblecodes:
    #         if (not i.__contains__(color)):
    #             copied.remove(i)
    #     self.possiblecodes = copied
    # def blackTag(self, color, position):
    #     color = int(color)
    #     position = int(position)
    #     copied = copy.deepcopy(self.possiblecodes)
    #     for i in self.possiblecodes:
    #         if (not i[position] == color):
    #             copied.remove(i)
    #     self.possiblecodes = copied


b = Board()


b.guess = [1, 2, 3, 4]
print("guess: ", b.convert_guess(b.guess))
while True:
    b.getresponse(input("\ninput response \"black space white\":"))
    if b.checkAllBlack():
        print("you win")
        break
    b.removeImpossibleCodes()
    guess = b.maxOptionsRemoved()
    # guess = b.possiblecodes
    print(b.possiblecodes)
    print("\n guess: ", b.convert_guess(guess))

# start with initial guess 1234
# guess
# repeat
# get response
# if all black you win
# remove from possible codes all that don't suit response
# guess = see which guess minimum options removed is the highest, or other scoring technique
# extra logics to add:
# if color in all 4 spots and there wasn't a black peg then there is not color
