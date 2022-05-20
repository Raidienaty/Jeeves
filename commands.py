import re
from math import *

import wolframalpha

class Commands:

    def __init__(self) -> None:
        self.called = False
        self.hru = False

    def checkCall(self, request):
        if self.lookForName(request):
            self.called = True
            return True
        else:
            self.called = False
            return False
        
    def lookForName(self, request):
        greetings = r'\b(Hey|hello|yo|hi|good morning|good evening|good afternoon)'

        # No error check with proper greetings
        if re.search(greetings + r' \bJeeves', request, re.I):
            return True
        # Mentioned name but no greeting detected
        elif re.search(r'\bJeeves', request, re.I):
            pass
        # Potential false positive with stt engine for name
        elif re.search(r'\b(dreeves|trees)', request, re.I):
            if re.search(r'\b' + greetings, request, re.I):
                return True

        # Potential false positive with stt engine for 'hey jeeves'
        elif re.search(r'\bachieve', request, re.I):
            if request.count(' ') == 0:
                return True

        return False

    def evalComplexMath(self):
        client = wolframalpha.Client('AYHKGA-L5UUEX4WT3')

        return client.query('Derivative of 20x')

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
        else:
            print('What can I do for you?')
