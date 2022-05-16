import re

class Commands:

    def __init__(self) -> None:
        self.called = False
        pass

    def checkCall(self, request):
        if re.search(r'\b(Hey|hello|yo|hi) Jeeves', request, re.I):
            self.called = True

    def evaluateRequest(self, request):
        pass