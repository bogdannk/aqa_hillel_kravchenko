# task conditions

"""
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код.
"""

# task data
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# task solution № 1
first_solution = sum(char for char in test_list if char % 2 == 0)

print(f"The sum of all paired numbers in the list is equal to: {first_solution}")

# task solution № 2
second_solution = sum(filter(lambda char: (char % 2 == 0), test_list))

print(f"The sum of all paired numbers in the list is equal to: {second_solution}")