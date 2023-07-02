'''
    Request Number Sender
'''
import re
import requests

def find_numbers(url):

    response = requests.get(url)
    if response.status_code == 200:
        numbers = re.findall(r'\d+', response.text)
        return numbers
    return None

# Example usage:
website_url = 'https://patriot.ua'
numbers_found = find_numbers(website_url)
if numbers_found:
    print("Numbers found:", numbers_found)
else:
    print("Failed to retrieve the website or no numbers found.")


def format_phone_number(phone_number):
    '''
        Phone number formater
    '''
    # Remove all non-digit characters
    digits = ''.join(filter(str.isdigit, phone_number))

    # Check if the number has a valid length
    if len(digits) != 10:
        return "Invalid phone number"

    # Format the number as (XXX) XXX-XXXX
    formatted_number = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

    return formatted_number

# Example usage
phone = "067 346-7247"
formatted_phone = format_phone_number(phone)
# print(formatted_phone)
