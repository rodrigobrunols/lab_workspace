from decimal import Decimal, ROUND_HALF_UP


class Money:
    """
    Value-object representing monetary values with automatic rounding,
    safe arithmetic, and rich comparisons.
    """

    def __init__(self, value):
        if isinstance(value, Money):
            self.value = value.value
        else:
            self.value = Decimal(str(value))
        self._round()

    def _round(self):
        self.value = self.value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # --------------------------
    # Factories
    # --------------------------
    @staticmethod
    def zero():
        return Money("0")

    # --------------------------
    # Arithmetic
    # --------------------------
    def __add__(self, other):
        other = Money(other)
        return Money(self.value + other.value)

    def __sub__(self, other):
        other = Money(other)
        return Money(self.value - other.value)

    def __mul__(self, other):
        if isinstance(other, Money):
            return Money(self.value * other.value)

        if isinstance(other, (Decimal, int, float, str)):
            return Money(self.value * Decimal(str(other)))

        raise TypeError(f"Cannot multiply Money by {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = Money(other)
        return Money(self.value / other.value)

    def __abs__(self):
        return Money(abs(self.value))

    # --------------------------
    # Comparisons
    # --------------------------
    def _to_money(self, other):
        return other if isinstance(other, Money) else Money(other)

    def __lt__(self, other):
        other = self._to_money(other)
        return self.value < other.value

    def __le__(self, other):
        other = self._to_money(other)
        return self.value <= other.value

    def __gt__(self, other):
        other = self._to_money(other)
        return self.value > other.value

    def __ge__(self, other):
        other = self._to_money(other)
        return self.value >= other.value

    def __eq__(self, other):
        try:
            other = self._to_money(other)
            return self.value == other.value
        except Exception:
            return False

    # --------------------------
    # Helpers
    # --------------------------
    @staticmethod
    def min(a, b):
        return a if a.value <= b.value else b

    @staticmethod
    def max(a, b):
        return a if a.value >= b.value else b

    # --------------------------
    # String representations
    # --------------------------
    def __repr__(self):
        return f"{self.value:.2f}"

    def __str__(self):
        return f"{self.value:.2f}"
