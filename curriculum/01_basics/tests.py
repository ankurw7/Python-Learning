import unittest
from examples import example_conditionals, example_loops, example_operators, example_type_casting
from exercises import (
    exercise_check_parity,
    exercise_sum_numbers,
    exercise_validate_password,
    exercise_celsius_to_fahrenheit,
    exercise_convert_and_sum
)

class TestBasicsExamples(unittest.TestCase):
    def test_conditionals(self):
        self.assertEqual(example_conditionals(-5), "Negative")
        self.assertEqual(example_conditionals(0), "Zero")
        self.assertEqual(example_conditionals(5), "Small Positive")
        self.assertEqual(example_conditionals(20), "Large Positive")

    def test_loops(self):
        self.assertEqual(example_loops(5), [0, 2, 4])
        self.assertEqual(example_loops(10), [0, 2, 4, 6, 8])

    def test_operators_example(self):
        res = example_operators(10, 3)
        self.assertEqual(res["addition"], 13.0)
        self.assertEqual(res["floor_division"], 3.0)
        self.assertEqual(res["modulo"], 1.0)
        self.assertEqual(res["exponent"], 1000.0)
        self.assertEqual(res["logical_and"], 1.0)

    def test_type_casting_example(self):
        self.assertEqual(example_type_casting("123"), "Integer: 123")
        self.assertEqual(example_type_casting("3.14"), "Float: 3.14")
        self.assertEqual(example_type_casting("hello"), "String: hello")

class TestBasicsExercises(unittest.TestCase):
    def test_check_parity(self):
        # Note: These will fail until the user implements the exercises
        if exercise_check_parity(2) is None:
            self.skipTest("Exercise not implemented yet")
            
        self.assertEqual(exercise_check_parity(2), "Even")
        self.assertEqual(exercise_check_parity(3), "Odd")
        self.assertEqual(exercise_check_parity(0), "Even")

    def test_sum_numbers(self):
        if exercise_sum_numbers(5) is None:
            self.skipTest("Exercise not implemented yet")
            
        self.assertEqual(exercise_sum_numbers(5), 15) # 1+2+3+4+5 = 15
        self.assertEqual(exercise_sum_numbers(1), 1)

    def test_validate_password(self):
        if exercise_validate_password("short") is None:
            self.skipTest("Exercise not implemented yet")
            
        self.assertTrue(exercise_validate_password("StrongAIpass"))
        self.assertFalse(exercise_validate_password("weak"))
        self.assertFalse(exercise_validate_password("longpasswordwithoutkeyword"))

    def test_celsius_to_fahrenheit(self):
        if exercise_celsius_to_fahrenheit(0) is None:
            self.skipTest("Exercise not implemented yet")
        self.assertAlmostEqual(exercise_celsius_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(exercise_celsius_to_fahrenheit(100), 212.0)
        self.assertAlmostEqual(exercise_celsius_to_fahrenheit(-40), -40.0)

    def test_convert_and_sum(self):
        if exercise_convert_and_sum("0", "0") is None:
            self.skipTest("Exercise not implemented yet")
        self.assertEqual(exercise_convert_and_sum("10", "20"), 30)
        self.assertEqual(exercise_convert_and_sum("-5", "5"), 0)

if __name__ == "__main__":
    unittest.main()
