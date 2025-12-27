from dataclasses import dataclass
from src.domain.models.money import Money


@dataclass(frozen=True)
class OperationResult:
    tax: Money

    @staticmethod
    def zero():
        return OperationResult(tax=Money("0"))
