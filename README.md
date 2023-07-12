Here's an example test script for the provided Python code that covers functional testing:
```
import unittest
from your_module import format_phone_number

class PhoneFormattingTestCase(unittest.TestCase):
    def test_valid_phone_number_formatting(self):
        phone_number = "063 942 95-70"
        expected_result = "380639429570"
        actual_result = format_phone_number(phone_number)
        self.assertEqual(actual_result, expected_result)

    def test_invalid_phone_number_length(self):
        phone_number = "063 942 95-7"
        expected_result = "Invalid phone number"
        actual_result = format_phone_number(phone_number)
        self.assertEqual(actual_result, expected_result)

    def test_invalid_phone_number_format(self):
        phone_number = "063a9429570"
        expected_result = "Invalid phone number"
        actual_result = format_phone_number(phone_number)
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()
```

This script utilizes the `unittest` framework to define test cases. It includes three test cases:
1. `test_valid_phone_number_formatting` verifies that a valid phone number is correctly formatted.
2. `test_invalid_phone_number_length` checks if an invalid phone number with an incorrect length returns the expected error message.
3. `test_invalid_phone_number_format` tests if an invalid phone number with non-digit characters returns the expected error message.

You can run this script to perform functional testing on the `format_phone_number` function. Make sure to replace `your_module` with the appropriate module name where the function is defined.
