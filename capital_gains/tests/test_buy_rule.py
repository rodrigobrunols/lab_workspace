from unittest import TestCase

from src.domain.models.money import Money
from src.domain.models.operation import Operation, OperationType
from src.domain.position.state import PositionState
from src.domain.rules.buy_rule import BuyRule


class TestBuyRule(TestCase):

    def test_buy_increases_position_without_tax(self):
        state = PositionState()
        rule = BuyRule()
        operation = Operation(OperationType.BUY.value, Money("10"), 100)

        result = rule.execute(state, operation)
        print(result.tax)
        self.assertEqual(result.tax, Money("0"))
        self.assertEqual(state.total_quantity, 100)
        self.assertEqual(state.total_cost, Money("1000"))
        self.assertEqual(state.average_cost, Money("10"))
