from enum import Enum


class EmployeeType(Enum):
    Respondent = 0
    Manager = 1
    Director = 2


class Call(object):

    def __init__(self):
        pass

class Employee(object):

    def __init__(self):
        self.call = None

    def __str__(self):
        return "{}: {}".format(self.etype, self.call != None)

    def assign(self, call):
        self.call = call

    def release(self):
        self.call = None


class Respondent(Employee):

    def __init__(self):
        super().__init__()
        self.etype = EmployeeType.Respondent


class Manager(Employee):

    def __init__(self):
        super().__init__()
        self.etype = EmployeeType.Manager


class Director(Employee):

    def __init__(self):
        super().__init__()
        self.etype = EmployeeType.Director


class CallCenter(object):

    def __init__(self):
        self.employees = [Respondent() for _ in range(3, 6)]
        self.managers = [Manager() for _ in range(1, 2)]
        self.directors = [Director() for _ in range(1, 2)]

    def dispatch_call(self, call):
        for egroup in [self.employees, self.managers, self.directors]:
            for e in egroup:
                if not e.call:
                    e.assign(call)
                    return e
        return None

    def __iter__(self):
        for egroup in [self.employees, self.managers, self.directors]:
            for e in egroup:
                yield e

call_center = CallCenter()
for e in call_center:
    print(e)

c = Call()
print('dispatching call')
call_center.dispatch_call(c)

for e in call_center:
    print(e)

c = Call()
print('dispatching call')
call_center.dispatch_call(c)

for e in call_center:
    print(e)

c = Call()
print('dispatching call')
call_center.dispatch_call(c)

for e in call_center:
    print(e)

c = Call()
print('dispatching call')
call_center.dispatch_call(c)

for e in call_center:
    print(e)
