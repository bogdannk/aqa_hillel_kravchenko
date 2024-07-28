import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

'''Вирішив зробити перше та друге завдання однією командою, так як використовується один метод,
рішення нижче'''

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n"," ").replace("....", " ")
print(f"Fixed_variable adwentures_of_tom_sawer \n{adwentures_of_tom_sawer}")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer)
print("\n", adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
# Перший варіант де менше коду:
h_counter = adwentures_of_tom_sawer.count("h")
print(f"\nThe number of letters “h” in the text = {h_counter}")

# Другий варіант де більше коду(написав для тренування циклів):
h_counter_2 = 0
for letter in adwentures_of_tom_sawer:
    if letter == "h":
        h_counter_2 += 1

print(f"\nThe number of letters “h” in the text = {h_counter_2}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
title_words_count = 0

for letter in adwentures_of_tom_sawer.split():
    if letter.istitle():
        title_words_count += 1
print(f"\nThe number of words starting with a capital letter: {title_words_count}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
second_Tom_index = adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom") + 1)
print(f"\nThe position where the word “Tom” appears for the second time: {second_Tom_index}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# adwentures_of_tom_sawer_sentences = None

adwentures_of_tom_sawer_sentences = re.sub(r'\s+', ' ', adwentures_of_tom_sawer.replace("\n", " ").replace("....", " ")).split('. ')

print(f"\n{adwentures_of_tom_sawer_sentences}")
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence_l_case = adwentures_of_tom_sawer_sentences[3].lower()
print(f"\nFourth sentence in lower case: \n{fourth_sentence_l_case}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

starts_with_by_the_time = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        starts_with_by_the_time = True
        break

print(f"\nDoes any sentence begin with 'By the time': {starts_with_by_the_time}")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence_length = len(adwentures_of_tom_sawer_sentences[-1].split())
print(f"\nNumber of words in the last sentence: {last_sentence_length}")