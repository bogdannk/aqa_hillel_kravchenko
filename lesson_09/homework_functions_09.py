
class MyFunctionsForTest:

    def reverse_string(input_string: str) -> str:
        return ''.join(reversed(input_string))


    def longest_word(words: list[str]) -> str:
        if not words:
            return ""
        return max(words, key=len)


    def filter_string_from_list(input_list: list[object]) -> list[str]:
        return list(filter(lambda item: isinstance(item, str), input_list))


    def sum_of_paired_numbers(input_list: list[int]) -> int:
        return sum(filter(lambda item: (item % 2 == 0), input_list))







