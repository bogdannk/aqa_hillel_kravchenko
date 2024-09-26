"""Solution decorator"""

def function_for_log(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


@function_for_log
def add(a, b):
    return a + b

add(3, 5)


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error was appeared: {e}")
    return wrapper


@exception_handler
def divide(a, b):
    return a / b

divide(4, 0)