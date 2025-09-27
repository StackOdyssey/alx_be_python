def perform_operation(a, b, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.
    operation (str): The operation to perform. Can be 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    float: The result of the arithmetic operation.

    Raises:
    ValueError: If an unsupported operation is provided or if division by zero is attempted.
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")