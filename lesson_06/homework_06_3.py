# task conditions

""" Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код.
"""

# task data
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

# task solution № 1
new_lst_1 = list(filter(lambda item: isinstance(item, str), lst1))

print(f"A list that contains only variables of the string type below: \n{new_lst_1}")

# task solution № 2
new_lst_2 = [item for item in lst1 if isinstance(item, str)]

print(f"\nA list that contains only variables of the string type below: \n{new_lst_2}")