import unittest

from src.domain.models.money import Money
from src.domain.models.operation import Operation
from src.domain.position.state import PositionState
from src.domain.rules.sell_rule import SellRule


class TestSellRule(unittest.TestCase):

    def setUp(self):
        self.state = PositionState()
        self.rule = SellRule()

    def test_sell_with_loss_accumulates_loss(self):
        self.state.apply_buy(100, Money("10"))

        op = Operation("sell", Money("5"), 50)
        res = self.rule.execute(self.state, op)

        self.assertEqual(res.tax, Money("0"))
        self.assertEqual(self.state.accumulated_loss, Money("250"))

    def test_tax_exempt_when_gross_below_threshold(self):
        self.state.apply_buy(100, Money("10"))

        op = Operation("sell", Money("15"), 10)  # gross = 150 < 20k
        res = self.rule.execute(self.state, op)

        self.assertEqual(res.tax, Money("0"))
        self.assertEqual(self.state.accumulated_loss, Money("0"))  # untouched

    def test_taxable_profit_after_deducting_loss(self):
        self.state.apply_buy(3000, Money("10"))  # total_cost = 30000
        self.state.accumulated_loss = Money("200")

        op = Operation("sell", Money("30.0"), 2000)  # profit = 40000
        res = self.rule.execute(self.state, op)

        # taxable profit = 40000 - 200 = 39800 → 20% = 60
        self.assertEqual(res.tax, Money("7960"))
        self.assertEqual(self.state.accumulated_loss, Money("0"))

    def test_tax_rounding_down(self):
        # Preço médio: 10.00
        self.state.apply_buy(1, Money("1.00"))

        # Venda por 21.015 → lucro = 21.015
        # Taxa (20%): 0.003 → arredonda para 0.00
        op = Operation("sell", Money("21000.015"), 1)
        res = self.rule.execute(self.state, op)

        self.assertEqual(res.tax, Money("4199.80"))

    def test_tax_rounding_up(self):
        # Preço médio: 0.00
        self.state.apply_buy(1, Money("0.00"))

        # Venda por 10.129 → lucro = 10.129
        # Taxa (20%): 2.0258 → arredondado para 2.03
        op = Operation("sell", Money("21000.132"), 1)
        res = self.rule.execute(self.state, op)

        self.assertEqual(res.tax, Money("4200.03"))
