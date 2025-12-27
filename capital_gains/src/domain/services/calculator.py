from src.domain.exceptions.exceptions import CapitalGainsError, DomainError, CalculatorBlockedError
from src.domain.models.operation import Operation
from src.domain.models.result import OperationResult
from src.domain.position.state import PositionState
from src.domain.rules.buy_rule import BuyRule
from src.domain.rules.sell_rule import SellRule
from src.domain.rules.validators import validate


class CapitalGainsCalculator:
    """
    Service that applies the set of rules at current state
    """

    def __init__(self):
        self.state = PositionState()
        self.rules = [BuyRule(), SellRule()]
        self.errors = 0
        self.blocked = False

    def process(self, op: Operation) -> OperationResult:
        validate(op, self.state)

        for rule in self.rules:
            if rule.applies(op):
                return rule.execute(self.state, op)

        raise CapitalGainsError(f"No rule found for operation: {op.operation}")
