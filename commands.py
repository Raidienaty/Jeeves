import re
from math import *

import wolframalpha

class Commands:

    def __init__(self) -> None:
        self.called = False
        self.complexMath = False

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
        elif re.search(r'\b(achieve|Patriots)', request, re.I):
            if request.count(' ') == 0:
                return True

        return False

    def evalComplexMath(self, request):
        client = wolframalpha.Client('')

        return next(client.query(request).results).text

    def evaluate_expression(self, equation):
        evaleq = compile(equation, "<string>", "eval")
        return eval(evaleq)

    def evaluateRequest(self, request):
        if re.search(r'\b[\d]+[\ ]?(\+|\*|\/|\-)[\ ]?[\d]+', request, re.I):
            math = re.split(r'\b([\d]+[\ ]?[\+|\*|\/|\-][\ ]?[\d]+)', request)[1]
            print("The answer to your question is " + str(self.evaluate_expression(str(math))))
        elif re.search(r'\bHow are you', request, re.I):
            print('I\'m doing well, what can I do for you?')
        elif re.search(r'\bmath', request, re.I):
            print('Asking wolframalpha to come help...')
            self.complexMath = True
        elif self.complexMath:
            print('The answer to your complex math question is: ' + self.evalComplexMath(request))
            self.complexMath = False
        else:
            print('What can I do for you?')
