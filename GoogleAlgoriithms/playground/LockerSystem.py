from collections import defaultdict, deque
from enum import Enum
import unittest


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Package:

    def __init__(self, id :str, size:Size):
        self.id = id
        self.size = size

    def __str__(self):
        return f"Package({self.id})"

class Locker:

    def __init__(self, id : str, size:Size):
        self.id = id
        self.package = None
        self.available = True
        self.size = size

    def assign(self, package:Package):
        self.package = package
        self.available = False

    def release(self):
        self.package = None
        self.available = True

    def __str__(self):
        status = f"Available" if self.available else f"In use by package: {self.package.id}"
        return f"Locker({self.id}, {status})"

class LockerSystem:

    def __init__(self):
        self.lockers = defaultdict()
        self.availableLockers = defaultdict(deque)

    def assign(self, package : Package):
        pass
        for size in Size:
            if size.value >= package.size.value:
                if self.availableLockers[size]:
                    locker = self.availableLockers[size].popleft()
                    locker.assign(package)
                    print(f"Locker= {locker.id} assigned for package= {package}")
                    return locker

            print(f"No locker available for package= {package}")

    def release(self, lockerId):
        locker = self.lockers.get(lockerId)
        if locker and locker.available:
            locker.release()
            print(f"Locker= {locker.id} released form package= {locker.package}")
            return True
        print(f"Locker= {locker.id} already free or does not exists")
        return False

    def add(self, locker:Locker):
        self.availableLockers[locker.size].append(locker)
        self.lockers[locker.id] = locker

    def status(self):
        print("System Status:")
        for l in self.lockers:
            print(l)



# class TestPackage(unittest.TestCase):
#
#     def setUp(self):
#         self.package = Package("1", Size.MEDIUM)
#
#     def testGetSize(self):
#         self.assertEquals(self.package.size, Size.MEDIUM)
#
# if __name__ == "__main__":
#     unittest.main()


# system = LockerSystem()
#
# # Initialize lockers
# lockers = [
#     Locker("L1", Size.SMALL),
#     Locker("L2", Size.SMALL),
#     Locker("L3", Size.MEDIUM),
#     Locker("L4", Size.LARGE),
#     Locker("L5", Size.LARGE),
# ]
#
# for locker in lockers:
#     system.add(locker)
#
# # Packages arriving at the locker
# packages = [
#     Package("PCKG001", Size.SMALL),
#     Package("PCKG002", Size.LARGE),
#     Package("PCKG003", Size.MEDIUM),
#     Package("PCKG004", Size.SMALL),
#     Package("PCKG005", Size.LARGE),
#     Package("PCKG006", Size.SMALL),
# ]
#
# # Assign lockers to packages
# for pkg in packages:
#     system.assign(pkg)
#
# # Check locker status
# system.status()
#
# # Release a locker
# system.release("L2")
# system.release("L4")
#
# # Check locker status after release
# system.status()
