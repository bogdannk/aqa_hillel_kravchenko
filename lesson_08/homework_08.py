# task conditions
"""
Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
"""

# Test data
my_test_list: list[str] = ["1, 2, 3, 4", "1,2,3,4,50", "qwerty1,2,3"]

# Task solution
def sum_all_numbers_if_int(input_list: list[str]):

    sum_numbers = lambda item: sum(map(int, item.replace(" ", "").split(',')))

    for item in input_list:
        try:
            result = sum_numbers(item)
            print(result)
        except ValueError:
            print(f"Cannot sum items from list due to invalid characters in: '{item}'")


sum_all_numbers_if_int(my_test_list)

