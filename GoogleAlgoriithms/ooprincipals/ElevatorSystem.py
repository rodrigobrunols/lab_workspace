from enum import Enum


class Direction(Enum):

    UP = "1"
    DOWN = "2"
    IDLE = "3"


print(Direction.UP)
print(Direction.UP.name)
print(Direction.UP.value)
