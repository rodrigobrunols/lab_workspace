from src.domain.models.money import Money
from src.domain.models.operation import Operation
from src.domain.models.result import OperationResult
from src.domain.position.state import PositionState
from src.domain.rules.base import Rule
from src.domain.services.tax_calculator import TaxCalculator


class SellRule(Rule):
    """
    Apply SellRule for an operation executed in current state.
    Delegates tax logic to a calculator,
    """

    def __init__(self, tax_calculator: TaxCalculator = None):
        self.tax_calculator = tax_calculator or TaxCalculator()

    def applies(self, operation: Operation) -> bool:
        return operation.is_sell

    def execute(self, state: PositionState, operation: Operation) -> OperationResult:
        average_cost = state.average_cost

        gross = operation.unit_cost * operation.quantity
        profit = (operation.unit_cost - average_cost) * operation.quantity

        # --------------------------
        # Delegate tax computation
        # --------------------------
        tax, state.accumulated_loss = self.tax_calculator.compute_tax(
            gross=gross,
            profit=profit,
            accumulated_loss=state.accumulated_loss
        )

        # ---------------------------------------------------
        # Update position after the sale
        # ---------------------------------------------------
        state.total_quantity -= operation.quantity
        state.total_cost = state.total_quantity * average_cost

        return OperationResult(tax)
