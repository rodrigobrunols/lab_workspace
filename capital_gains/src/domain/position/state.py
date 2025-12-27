from dataclasses import dataclass

from src.domain.models.money import Money


@dataclass
class PositionState:
    """
    Keeps current state of the system:   total_quantity, total_cost, accumulated_loss
    """
    total_quantity: int = 0
    total_cost: Money = Money("0")
    accumulated_loss: Money = Money("0")
    errors = 0

    @property
    def average_cost(self) -> Money:
        if self.total_quantity == 0:
            return Money("0")
        return self.total_cost / self.total_quantity

    def apply_buy(self, qty: int, price: Money):
        self.total_cost += price * qty
        self.total_quantity += qty
