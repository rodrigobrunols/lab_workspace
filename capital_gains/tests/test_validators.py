from unittest import TestCase

from src.domain.exceptions.exceptions import DomainError
from src.domain.models.money import Money
from src.domain.models.operation import Operation, OperationType
from src.domain.position.state import PositionState
from src.domain.rules.validators import validate


class TestValidators(TestCase):

    def test_validate_cannot_sell_more_then_current_quantity(self):
        test_operation = Operation(operation=OperationType.SELL,
                                   quantity=1,
                                   unit_cost=Money("1"))

        test_state = PositionState()

        with self.assertRaises(DomainError) as ctx:
            validate(test_operation, test_state)

        self.assertIn(str(ctx.exception), "Can't sell more stocks than you have")

    def test_validate_operation_quantity_less_then_current(self):
        test_operation = Operation(operation=OperationType.SELL,
                                   quantity=1,
                                   unit_cost=Money("1"))

        test_state = PositionState(total_quantity=10)

        self.assertIsNone(validate(test_operation, test_state))
