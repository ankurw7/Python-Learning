import unittest
import math
from examples import example_dot_product, example_mean_squared_error, example_simple_tokenizer
from exercises import exercise_relu, exercise_matrix_add, exercise_euclidean_distance

class TestAIConceptsExamples(unittest.TestCase):
    def test_dot_product(self):
        self.assertEqual(example_dot_product([1, 2], [3, 4]), 11) # 1*3 + 2*4 = 3+8=11
        
    def test_mse(self):
        self.assertAlmostEqual(example_mean_squared_error([1, 2], [1, 2]), 0.0)
        self.assertAlmostEqual(example_mean_squared_error([1], [3]), 4.0) # (1-3)^2 = 4

    def test_tokenizer(self):
        self.assertEqual(example_simple_tokenizer("Hi!"), ["hi"])

class TestAIConceptsExercises(unittest.TestCase):
    def test_relu(self):
        if exercise_relu(-5) is None:
            self.skipTest("Exercise not implemented yet")
            
        self.assertEqual(exercise_relu(10), 10)
        self.assertEqual(exercise_relu(-10), 0)
        self.assertEqual(exercise_relu(0), 0)

    def test_matrix_add(self):
        if exercise_matrix_add([[1]], [[1]]) is None:
            self.skipTest("Exercise not implemented yet")
            
        m1 = [[1, 2], [3, 4]]
        m2 = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        self.assertEqual(exercise_matrix_add(m1, m2), expected)

    def test_euclidean_distance(self):
        if exercise_euclidean_distance((0,0), (0,0)) is None:
            self.skipTest("Exercise not implemented yet")
            
        # 3-4-5 triangle
        dist = exercise_euclidean_distance((0, 0), (3, 4))
        self.assertAlmostEqual(dist, 5.0)

if __name__ == "__main__":
    unittest.main()
