import re

from numpy import require
from requests import request

class Commands:

    def __init__(self) -> None:
        self.called = False

    def checkCall(self, request):
        if re.search(r'\b(Hey|hello|yo|hi) Jeeves', request, re.I):
            self.called = True

    def evaluateRequest(self, request):
        if re.search(r'\b[\d]+(+|*|/|-)[\d]+'):
            print('Attempt to do math')
        elif re.search(r'\bHow are you', request, re.I):
            print('I\'m doing well, how are you?')
            self.hru = True
        elif self.hru:
            print('What can I do for you?')