# task conditions

"""Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код."""

# task solution

flag = True
while flag:
    our_string = input("Enter the data for verification: ")
    unique_characters = lambda x: sum(1 for char in x if x.count(char) == 1) > 10

    print(f"{unique_characters(our_string)}")

    print("If you want to check another string, press - Y, if not, press - N")
    choice = input('Enter your choice: ').lower()
    if choice in ['y', 'н']:
        flag = True
    else:
        flag = False

