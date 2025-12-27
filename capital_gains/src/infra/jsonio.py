import json
from decimal import Decimal

from src.domain.models.money import Money


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)


def parse_operations(line: str):
    """
    Parses line of JSON operations.
    The input must be of the form:
      [{"operation": "...", "unit-cost": ..., "quantity": ...}]

    Returns a list of normalized operation dicts.
    """
    parsed = json.loads(line)

    operations = []
    for item in parsed:
        quantity = int(item["quantity"])
        unit_cost = Money(item["unit-cost"])

        operations.append({
            "operation": item["operation"],
            "unit_cost": unit_cost,
            "quantity": quantity,
        })

    return operations
