import unittest
from lesson_09.homework_functions_09 import MyFunctionsForTest

class MyTests(unittest.TestCase):

    def test_reverse_string_positive(self):
        test_string = "Hello, world!"
        expected_result = "!dlrow ,olleH"
        self.assertEqual(MyFunctionsForTest.reverse_string(test_string), expected_result,
                         f"Expected '{expected_result}' but got '{MyFunctionsForTest.reverse_string(test_string)}'")

    def test_reverse_string_negative(self):
        with self.assertRaises(TypeError, msg="Expected TypeError when passing a non-string value to reverse_string"):
            MyFunctionsForTest.reverse_string(123456)



    def test_longest_word_from_list_positive(self):
        words = ["Kyiv", "Lviv", "Odesa", "Kharkiv", "Dnipro"]
        expected_result = "Kharkiv"
        self.assertEqual(MyFunctionsForTest.longest_word(words), expected_result,
                         f"Expected '{expected_result}' but got '{MyFunctionsForTest.longest_word(words)}'")

    def test_if_the_list_of_words_is_empty_positive(self):
        words = []
        expected_result = ""
        self.assertEqual(MyFunctionsForTest.longest_word(words), expected_result,
                         f"Expected '{expected_result}' but got '{MyFunctionsForTest.longest_word(words)}'")

    def test_if_non_string_elements_negative(self):
        words = ["Kyiv", 123, "Lviv", "Odesa", "Kharkiv", "Dnipro"]
        with self.assertRaises(TypeError, msg="Expected TypeError when list contains non-string elements"):
            MyFunctionsForTest.longest_word(words)



    def test_mixed_list_positive(self):
        input_list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
        result = MyFunctionsForTest.filter_string_from_list(input_list)
        self.assertIn("1", result, "Expected '1' to be in the result list")
        self.assertIn("False", result, "Expected 'False' to be in the result list")
        self.assertIn("Python", result, "Expected 'Python' to be in the result list")
        self.assertNotIn(3, result, "Expected 3 not to be in the result list")
        self.assertNotIn(True, result, "Expected True not to be in the result list")
        self.assertNotIn(0, result, "Expected 0 not to be in the result list")

    def test_all_strings_positive(self):
        input_list = ['1', '2', 'Python', 'Lorem Ipsum']
        result = MyFunctionsForTest.filter_string_from_list(input_list)
        self.assertTrue(all(isinstance(item, str) for item in result))
        self.assertEqual(result, input_list, f"Expected result to be {input_list} but got {result}")

    def test_no_strings_positive(self):
        input_list = [3, 5, True, []]
        result = MyFunctionsForTest.filter_string_from_list(input_list)
        self.assertFalse(result, f"Expected result to be an empty list")

    def test_non_list_input_negative(self):
        try:
            MyFunctionsForTest.filter_string_from_list("not a list")
        except Exception as e:
            self.assertIsInstance(e, TypeError)



    def test_oll_odd_positive(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = MyFunctionsForTest.sum_of_paired_numbers(input_list)
        self.assertEqual(result, 30, "Expected sum of paired numbers to be 30 but got {result}")

    def test_if_the_list_is_empty_positive(self):
        input_list = []
        result = MyFunctionsForTest.sum_of_paired_numbers(input_list)
        self.assertEqual(result, 0, "Expected sum to be 0 for an empty list")

    def test_if_some_data_eaqual_to_str_negative(self):
        input_list = [2, 4, "six", 8]
        try:
            MyFunctionsForTest.sum_of_paired_numbers(input_list)
        except Exception as e:
            self.assertIsInstance(e, TypeError)













if __name__ == '__main__':
    unittest.main()


