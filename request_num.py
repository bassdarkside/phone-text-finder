'''
    Request Number Sender
'''
import re
import requests
from colorama import Fore, Back

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
    # formatted_number = f"38({digits[:3]}){digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    formatted_number = f"38{digits[:3]}{digits[3:6]}{digits[6:8]}{digits[8:]}"


    return formatted_number

# Example usage
# PHONE = "673467247"
PHONE = input("\nEnter phone number as 10-digits format\nPhone number: ")
formatted_phone = format_phone_number(PHONE)
# print(Fore.BLUE + "NON-formatted phone number -> ", PHONE)
# print(Fore.GREEN + "FORMATTED  phone number -> ", formatted_phone + Fore.RESET)

def find_numbers(url):
    '''
        Find numbers from HTTPS GET request
    '''
    phonenumb = formatted_phone
    response = requests.get(url, timeout=500)
    if response.status_code == 200:
        numbers = re.findall(phonenumb, response.text)
        # numbers = re.findall(r'\d+', response.text)
        return numbers
    return None


# Example usage:
WEBSITE_URL = 'https://'+ input("Enter website for search phone number like this format 'example.com': ")
numbers_found = find_numbers(WEBSITE_URL)
if numbers_found:
    print(Fore.GREEN + "Number found! --> ", Fore.RED + numbers_found[0])
else:
    print(Fore.RED + "Failed to retrieve the website or no numbers found.")
