## Tests from chatgpt.
I use this promt example:
```
Write a test script for the python code that covers functional testing: [code]
```
## Functional testing
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

## Non-functional testing
Non-functional testing typically focuses on aspects such as performance, security, usability, and reliability. Since the given code doesn't have explicit non-functional requirements, let's assume we will cover usability and performance testing in our test script. Here's an example test script that covers non-functional testing aspects:

```
import time
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

    def test_execution_time(self):
        phone_number = "063 942 95-70"
        start_time = time.time()
        format_phone_number(phone_number)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLess(execution_time, 0.001)  # Adjust the threshold as per your requirements

if __name__ == "__main__":
    unittest.main()
```

In this script, we have added an additional test case `test_execution_time` to cover performance testing. It measures the execution time of the `format_phone_number` function for a valid phone number and asserts that it should be less than a certain threshold (in this case, 0.001 seconds). You can adjust the threshold based on your desired performance requirements.

Note that this is just an example, and you may need to modify the test cases based on your specific non-functional requirements and constraints.
