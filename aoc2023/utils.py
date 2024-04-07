def compare_with(other_function):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_result = func(*args, **kwargs)
            other_result = other_function(*args, **kwargs)
            assert (
                original_result == other_result
            ), f"Results differ: {func.__name__} returned {original_result}, {other_function.__name__} returned {other_result}"
            return original_result

        return wrapper

    return decorator
