import unittest
from src.domain.models.money import Money
from src.domain.models.operation import Operation, OperationType
from src.domain.services.calculator import CapitalGainsCalculator


class TestCalculator(unittest.TestCase):

    def test_calculator_processes_sequence(self):
        calc = CapitalGainsCalculator()

        ops = [
            Operation(OperationType.BUY.value, Money("10"), 100),
            Operation(OperationType.SELL.value, Money("15"), 50),
            Operation(OperationType.SELL.value, Money("15"), 50),
        ]

        taxes = [calc.process(op).tax for op in ops]

        self.assertEqual(taxes, [Money("0"), Money("0"), Money("0")])
