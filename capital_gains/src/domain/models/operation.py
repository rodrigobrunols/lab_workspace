from dataclasses import dataclass
from enum import Enum

from src.domain.models.money import Money


class OperationType(str, Enum):
    BUY = "buy"
    SELL = "sell"

    @staticmethod
    def from_str(value: str):
        try:
            return OperationType(value)
        except ValueError:
            raise ValueError(f"Invalid operation type: {value}")


@dataclass(frozen=True)
class Operation:
    operation: OperationType
    unit_cost: Money
    quantity: int

    @property
    def is_buy(self) -> bool:
        return self.operation == OperationType.BUY.value

    @property
    def is_sell(self) -> bool:
        return self.operation == OperationType.SELL.value
