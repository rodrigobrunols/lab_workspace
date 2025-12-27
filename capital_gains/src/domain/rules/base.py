from abc import ABC, abstractmethod

from src.domain.models.operation import Operation
from src.domain.models.result import OperationResult
from src.domain.position.state import PositionState


class Rule(ABC):
    """
    Base class for rules
    """

    @abstractmethod
    def applies(self, operation: Operation):
        pass

    @abstractmethod
    def execute(self, state: PositionState, operation: Operation) -> OperationResult:
        pass
