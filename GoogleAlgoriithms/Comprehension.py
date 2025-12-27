# list comprehension [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]

# dictionary comprehension {key_expression: value_expression for item in iterable if condition}
squares_set = {x: x**2 for x in range(10)}

# set comprehension {expression for item in iterable if condition}
unique_squares = {x**2 for x in range(10)}
