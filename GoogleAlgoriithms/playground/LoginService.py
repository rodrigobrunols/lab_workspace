# Millions of customers visit our website every day.
# For, for each customer we have a unique identifier that is the same every time they visit.
# We have 2 kinds of customers:.
# Recurrent Visitors that visit more than once and
# OneTime Visitors, who so far have visited the website only #once.
# We want to implement a class that has 2 functionalities:

# - logVisitor(int id)
# - getFirstOneTimeVisitor()

import unittest

from collections import defaultdict, OrderedDict
class LoginService:

    def __init__(self):
        self.loginFrequency = defaultdict(int)
        self.oneTimers = OrderedDict()

    def logVisitor(self, id):
        self.loginFrequency[id] += 1

        if id not in self.oneTimers:
            self.oneTimers[id] = True
        else:
            del self.oneTimers[id]

    def getFirstOneTimeVisitor(self):
        if self.oneTimers:
            return next(iter(self.oneTimers))
        return -1

    def __str__(self):
        return ",".join(f"{k}={v}" for k,v in self.loginFrequency.items()) + f" {self.oneTimers.keys()}"


# service = LoginService()
# service.logVisitor(1)
# service.logVisitor(2)
# service.logVisitor(1)
# service.logVisitor(3)
# service.oneTimers.popitem(2)
#
# print(service.getFirstOneTimeVisitor())
# service.logVisitor(1)
# print(service)
dd = defaultdict(int)
dd[1] = 1
dd[2] = 2
dd.popitem()
# del dd[2]
print(dd)

# print
# # service.logVisitor(2)
# service.logVisitor(3)
# service.removeVisitor(2)
#
# print(service.loginFrequency)
# print(service.oneTimers)




