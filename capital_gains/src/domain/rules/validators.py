from src.domain.exceptions.exceptions import ValidationError, InvalidOperationError, DomainError, CalculatorBlockedError
from src.domain.models.operation import Operation, OperationType
from src.domain.position.state import PositionState


def validate_positive_quantity(op: Operation, state: PositionState = None):
    if op.quantity <= 0:
        raise ValidationError("Quantity must be positive")


def validate_positive_cost(op: Operation, state: PositionState = None):
    if op.unit_cost <= 0:
        raise ValidationError("Unit cost must be positive")


def validate_operation_type(op: Operation, state: PositionState = None):
    if op.operation not in [OperationType.SELL, OperationType.BUY]:
        raise InvalidOperationError(f"Invalid operation type: {op.operation}")


def validate_cannot_sell_more_then_current_state(op: Operation, state: PositionState):
    if op.is_sell and op.quantity > state.total_quantity:
        state.errors += 1
        raise DomainError("Can't sell more stocks than you have")


def validate_account_blocked(op: Operation, state: PositionState):
    if state.errors >= 3:
        raise CalculatorBlockedError("Your account is blocked")


def validate(op: Operation, state: PositionState):
    validators = [
        validate_account_blocked,
        validate_positive_quantity,
        validate_positive_cost,
        validate_operation_type,
        validate_cannot_sell_more_then_current_state,
    ]

    for rule in validators:
        rule(op, state)
