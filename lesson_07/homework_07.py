# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number: int):
    # Initialize the appropriate variable
    multiplier: int = 1

    # Complete the while loop condition.
    while multiplier <= 5:         # FIXME errors, we need to limit the number of output lines to get the expected result
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:    # FIXME errors, comparing the result with string data, we need a comparison with numeric data.
            # Enter the action to take if the result is greater than 25
            break         # FIXME errors, wrong operator to interrupt the function
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1  # FIXME errors, wrong variable

multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(a: int, b: int):
    return a + b


print(f"The sum of the numbers is: {sum_numbers(5, 5)}") # 10

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The average value of the list of numbers is: {average(numbers_list)}")


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
# Data
our_string = "This is the string to return in reverse order."

# Task solution № 1
def reverse_string(input_string: str) -> str:
    return ''.join(reversed(input_string))


print(f"The result of the first solution: {reverse_string(our_string)}")


# Task solution № 2
def reverse_strint_var2(input_string: str) -> str:
    return input_string[::-1]

print(f"Result of the second solution:    {reverse_strint_var2(our_string)}")


# Task solution № 3
result = lambda input_string: ''.join(reversed(input_string))

print(f"Result of the third solution:     {result(our_string)}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
# Data:
our_words_list: list[str] = ["Kyiv", "Lviv", "Odesa", "Kharkiv", "Dnipro"]

# Task solution № 1
def longest_word(words: list[str]) -> str:
    if not words:
        return ""
    return max(words, key=len)


print(f"The longest word is:      {longest_word(our_words_list)}")

# Task solution № 2

longest_word_var2 = lambda word: '' if not word else max(word, key=len)

print(f"The longest word var2 is: {longest_word_var2(our_words_list)}")



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


# Task solution
def find_substring(str1: str, str2: str) -> int:
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(f"The first result is:   {find_substring(str1, str2)}") # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(f"The second result is: {find_substring(str1, str2)}") # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
# Data
our_string = input(f"input your string: ")

# Task solution

def more_than_10_unique_characters(input_string: str) -> bool:
    """
    Checks if there are more than 10 unique characters in the string

    :param input_string: the string to be checked
    :return: True if the string contains more than 10 unique characters, otherwise False.
    """
    unique_characters = lambda words: sum(1 for char in words if words.count(char) == 1) > 10
    return unique_characters(input_string)

result = more_than_10_unique_characters(our_string)
print(result)

# task 8
# Data
word_for_check = input("Enter a word that includes the letter 'h': ")

# Task solution
def check_if_contains_h_letter(input_word: str) -> bool:
    """
    Checks if the word contains the letter 'h'.

    :param input_word: the string to be checked
    :return: True if the word has an “h” letter in it, otherwise False.
    """
    return "h" in input_word.lower()

print(check_if_contains_h_letter(word_for_check))

# task 9
# Data
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

# Task solution

def filter_string_from_list(input_list: list[object]) -> list[str]:
    """
    Filters the list and keeps only data of type string
    :param input_list: a list that contains different types of data
    :return: a list with only string type data
    """
    return list(filter(lambda item:  isinstance(item, str), input_list))

print(f"\nA list that contains only variables of the string type below: \n{filter_string_from_list(lst1)}")

# task 10

# Data
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Task solution
def sum_of_paired_numbers(input_list: list[int]) -> int:
    """
    Counts the sum of all paired numbers in the list.
    :param input_list: the list of integers
    :return: The sum of all paired numbers in the list.
    """
    return sum(filter(lambda item: (item % 2 == 0), input_list))

print(f"\nThe sum of all paired numbers in the list is equal to: {sum_of_paired_numbers(test_list)}")

