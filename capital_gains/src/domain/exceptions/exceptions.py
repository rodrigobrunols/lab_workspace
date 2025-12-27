class CapitalGainsError(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__()

    pass


class InvalidOperationError(CapitalGainsError):
    """Raised when the operation is unrecognized or unsupported."""
    pass


class ValidationError(CapitalGainsError):
    """Raised when input data is invalid."""
    pass


class DomainError(CapitalGainsError):
    def __init__(self, message):
        super().__init__(message)


class CalculatorBlockedError(CapitalGainsError):
    def __init__(self, message):
        super().__init__(message)
