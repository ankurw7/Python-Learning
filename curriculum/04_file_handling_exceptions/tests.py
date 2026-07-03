import unittest
import os
import json

# Import the exercises to test
# If exercises are not yet implemented, the NotImplementedError will cause tests to fail
from exercises import count_lines_in_file, safe_divide, save_dict_to_json

class TestFileHandlingExceptions(unittest.TestCase):

    def setUp(self):
        # Setup a temporary file for reading tests
        self.test_file = "test_data.txt"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("Line 1\nLine 2\nLine 3\n")
            
        self.json_file = "test_output.json"

    def tearDown(self):
        # Clean up temporary files
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

    def test_count_lines_in_file(self):
        try:
            # Test success case
            self.assertEqual(count_lines_in_file(self.test_file), 3)
            
            # Test failure case
            self.assertEqual(count_lines_in_file("does_not_exist.txt"), -1)
        except NotImplementedError:
            self.skipTest("Exercise 1 not implemented yet.")

    def test_safe_divide(self):
        try:
            # Test success cases
            self.assertEqual(safe_divide(10, 2), 5.0)
            self.assertEqual(safe_divide(9, 3), 3.0)
            
            # Test failure case
            self.assertEqual(safe_divide(5, 0), "Cannot divide by zero")
        except NotImplementedError:
            self.skipTest("Exercise 2 not implemented yet.")

    def test_save_dict_to_json(self):
        try:
            test_data = {"key1": "value1", "key2": 42}
            
            # Call function
            result = save_dict_to_json(test_data, self.json_file)
            self.assertTrue(result)
            
            # Verify file was created and contains correct data
            self.assertTrue(os.path.exists(self.json_file))
            with open(self.json_file, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
            self.assertEqual(loaded_data, test_data)
        except NotImplementedError:
            self.skipTest("Exercise 3 not implemented yet.")

if __name__ == "__main__":
    unittest.main()
