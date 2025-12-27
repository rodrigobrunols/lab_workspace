from src.domain.models.money import Money
from src.domain.models.operation import Operation
from src.domain.models.result import OperationResult
from src.domain.position.state import PositionState
from src.domain.rules.base import Rule


class BuyRule(Rule):
    """
    Implement rules for BUY Operation described in Capital Gain spec
    """

    def applies(self, operation: Operation) -> bool:
        return operation.is_buy

    def execute(self, state: PositionState, operation: Operation) -> OperationResult:
        operation_total_cost = operation.unit_cost * operation.quantity

        state.total_quantity += operation.quantity
        state.total_cost += operation_total_cost

        return OperationResult.zero()
