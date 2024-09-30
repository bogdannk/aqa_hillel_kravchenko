
def generator_for_even_numbers(n: int):
    for item in range(0, n + 1, 2):
        yield item


for even_number in generator_for_even_numbers(10):
    print(f"generated number = {even_number}")



"""FIBONACCI"""

def fibonacci_numbers_generator(n: int):
    current_number, next_number = 0, 1
    while current_number <= n:
        yield current_number
        current_number, next_number = next_number, current_number + next_number

n = 25
for number in fibonacci_numbers_generator(n):
    print(number)

"""Second solution"""
def fibonacci_even_numbers_generator(n: int, log = False):
    current_number, next_number = 0, 1
    while current_number <= n:
        if current_number % 2 == 0:
            if log:
                print(f"Generating Fibonacci number: {current_number}")
            yield current_number
        current_number, next_number = next_number, current_number + next_number


n = 35
log = True

for even_number in fibonacci_even_numbers_generator(n, log):
    print(f"Received number: {even_number}")

