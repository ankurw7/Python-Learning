import unittest
from examples import example_list_comprehension
from exercises import exercise_filter_long_strings, exercise_count_word_frequencies, exercise_unique_elements_sorted

class TestDataStructuresExamples(unittest.TestCase):
    def test_list_comprehension(self):
        self.assertEqual(example_list_comprehension([1, 2, 3]), [1, 4, 9])
        self.assertEqual(example_list_comprehension([-1, 0, 1]), [1, 0, 1])

class TestDataStructuresExercises(unittest.TestCase):
    def test_filter_long_strings(self):
        if exercise_filter_long_strings(["a"], 1) is None:
            self.skipTest("Exercise not implemented yet")
            
        data = ["apple", "bat", "cat", "dolphin"]
        result = exercise_filter_long_strings(data, 4)
        self.assertEqual(result, ["apple", "dolphin"])
        self.assertEqual(exercise_filter_long_strings(data, 10), [])

    def test_count_word_frequencies(self):
        if exercise_count_word_frequencies([]) is None:
            self.skipTest("Exercise not implemented yet")
            
        data = ["apple", "banana", "apple", "cherry", "banana", "banana"]
        expected = {"apple": 2, "banana": 3, "cherry": 1}
        self.assertEqual(exercise_count_word_frequencies(data), expected)

    def test_unique_elements_sorted(self):
        if exercise_unique_elements_sorted([]) is None:
            self.skipTest("Exercise not implemented yet")
            
        data = [3, 1, 2, 3, 1, 4]
        expected = [1, 2, 3, 4]
        self.assertEqual(exercise_unique_elements_sorted(data), expected)

if __name__ == "__main__":
    unittest.main()
