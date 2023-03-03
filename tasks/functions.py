def gen_number_choices(max_value: int) -> tuple:
    """Generate tuple of numbers for models numeric fields choices."""
    return tuple(enumerate(range(1, (max_value + 1)), start=1))
