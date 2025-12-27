from src.domain.models.money import Money


class TaxCalculator:
    """
    Applies tax rules for operations.
    """

    TAX_RATE = Money("0.20")
    TAX_EXEMPT_THRESHOLD = Money("20000")

    def compute_tax(self, gross: Money, profit: Money, accumulated_loss: Money):
        # 1. Case: Loss → accumulates and no tax
        if profit < 0:
            return Money("0"), accumulated_loss + abs(profit)

        # 2. Profit with gross under exemption
        if gross <= self.TAX_EXEMPT_THRESHOLD:
            return Money("0"), accumulated_loss

        # 3. Profit + taxable + apply accumulated losses
        deducted = min(profit, accumulated_loss)
        taxable_profit = profit - deducted
        new_acc_loss = accumulated_loss - deducted

        tax = taxable_profit * self.TAX_RATE
        return tax, new_acc_loss
