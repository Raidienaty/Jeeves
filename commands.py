import re
from math import *

class Commands:

    def __init__(self) -> None:
        self.called = False
        self.hru = False

    def checkCall(self, request):
        if re.search(r'\b(Hey|hello|yo|hi) Jeeves', request, re.I):
            self.called = True
            return True
        elif self.called:
            return True
        else:
            self.called = False
            return False

    def evaluate_expression(self, equation):
        evaleq = compile(equation, "<string>", "eval")
        return eval(evaleq)

    def evaluateRequest(self, request):
        if re.search(r'\b[\d]+[\ ]?(\+|\*|\/|\-)[\ ]?[\d]+', request, re.I):
            math = re.split(r'\b([\d]+[\ ]?[\+|\*|\/|\-][\ ]?[\d]+)', request)[1]
            print("The answer to your question is " + str(self.evaluate_expression(str(math))))
        elif re.search(r'\bHow are you', request, re.I):
            print('I\'m doing well, how are you?')
            self.hru = True
        elif self.hru:
            print('What can I do for you?')