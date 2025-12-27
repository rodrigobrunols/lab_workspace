import json
import sys

from src.domain.exceptions.exceptions import DomainError, CalculatorBlockedError, CapitalGainsError
from src.domain.services.calculator import CapitalGainsCalculator
from src.domain.models.operation import Operation
from src.infra.jsonio import parse_operations, DecimalEncoder


def run():
    """
    Runs main process redding input from stdin and print results to stdout
    """
    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            break

        ops_data = parse_operations(line)
        calc = CapitalGainsCalculator()  # Creates a new calculator for each line to make each line independent
        results = []

        for d in ops_data:
            try:
                op = Operation(**d)
                res = calc.process(op)
                # Convert Money → float BEFORE passing to json.dumps
                results.append({
                    "tax": float(res.tax.value)
                })
            except CapitalGainsError as e:
                results.append({
                    "error": e.message
                })

        print(json.dumps(results, cls=DecimalEncoder))
