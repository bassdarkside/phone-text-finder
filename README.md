Certainly! I can help you with a Python script to find numbers on a website. Here's a basic script that utilizes the `requests` and `re` (regular expressions) modules to accomplish this:

```python
import re
import requests

def find_numbers(url):
    response = requests.get(url)
    if response.status_code == 200:
        numbers = re.findall(r'\d+', response.text)
        return numbers
    else:
        return None

# Example usage:
website_url = 'https://www.example.com'
numbers_found = find_numbers(website_url)
if numbers_found:
    print("Numbers found:", numbers_found)
else:
    print("Failed to retrieve the website or no numbers found.")
```

This script uses the `findall()` method from the `re` module to search for sequences of one or more digits (`\d+`) within the HTML content of the specified URL. It returns a list of all the numbers found on the page. If the website can't be retrieved or no numbers are found, it will return `None`.

You'll need to install the `requests` module if you haven't already by running `pip install requests` in your Python environment.


-----------------  Certainly! Here's a Python script that formats a phone number:  ---------------------------

```python
def format_phone_number(phone_number):
    # Remove all non-digit characters
    digits = ''.join(filter(str.isdigit, phone_number))

    # Check if the number has a valid length
    if len(digits) != 10:
        return "Invalid phone number"

    # Format the number as (XXX) XXX-XXXX
    formatted_number = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

    return formatted_number

# Example usage
phone = "123-456-7890"
formatted_phone = format_phone_number(phone)
print(formatted_phone)
```

This script defines a function `format_phone_number` that takes a phone number as input and returns a formatted version of it. It removes all non-digit characters, checks if the number has a valid length of 10 digits, and formats it as `(XXX) XXX-XXXX`. You can replace the `phone` variable with your desired phone number.

Let me know if you need any further assistance!
