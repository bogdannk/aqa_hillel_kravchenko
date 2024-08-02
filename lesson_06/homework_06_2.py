# task conditions

"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
(враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код."""

# task solution

includes_h = lambda word: 'h' in word.lower()

while True:
    word = input("Enter a word that includes the letter 'h': ")
    if includes_h(word):
        print(f"The word '{word}' includes the letter 'h'.")
        break
    else:
        print("The word doesn't contain the letter 'h'. Please? try one more time.")