alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f'\nThe total area is: {total_area}.')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291
first_second_goods = 250449
second_third_goods = 222950
second_goods = first_second_goods + second_third_goods - total_goods
first_goods = first_second_goods - second_goods
third_goods = second_third_goods - second_goods
print(f"\nGoods in the first warehouse - {first_goods},\ngoods in the second warehouse - {second_goods},\n"
      f"goods in the third warehouse - {third_goods}.")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
total_payment_period = int(1.5 * 12)
total_price = monthly_payment * total_payment_period
print(f"\nThe total price of the computer is - {total_price}.")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

remainders = {
    "8019 % 8": 8019 % 8,
    "9907 % 9": 9907 % 9,
    "2789 % 5": 2789 % 5,
    "7248 % 6": 7248 % 6,
    "7128 % 5": 7128 % 5,
    "19224 % 9": 19224 % 9
}
print(f"\nResult: {remainders}") # {'8019 % 8': 3, '9907 % 9': 7, '2789 % 5': 4, '7248 % 6': 0, '7128 % 5': 3, '19224 % 9': 0}


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

"""Маленьке пояснення"""
"""Спочатку думав зробити через словник, але там повторюються ключі, і через словник в мене 
   не вистачило знань, тому спробував використати здобуті знання на минулій лекції і щоб не 
   перемножати все окреме створив 2 списки і через індекси перемножив.
   """


quantities = [4, 2, 4, 1, 3]
prices = [274, 218, 35, 350, 21]

total_cost = 0

for i in range(len(quantities)):
    total_cost += quantities[i] * prices[i]

print(f"\nTotal price: {total_cost} грн")



# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8

presumed_quantities_of_pages = total_photos / photos_per_page

if total_photos % photos_per_page == 0:
    print(f"\nThe number of pages that Igor will need is - {int(presumed_quantities_of_pages)}")
else:
    print(f"\nThe number of pages that Igor will need is - {int(presumed_quantities_of_pages) + 1}")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

total_distance = 1600
tank_capacity = 48
consumption_per_100_km = 9

fuel_needed = (total_distance / 100) * consumption_per_100_km
print(f"\nIt will take {fuel_needed} liters for the trip.")

presumed_stops_needed = fuel_needed / tank_capacity

if fuel_needed % tank_capacity == 0:
    print(f"It will take {int(presumed_stops_needed)} stops.")
else:
    print(f"It will take {int(presumed_stops_needed) + 1} stops.")

