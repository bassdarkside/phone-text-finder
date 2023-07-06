"""
    Request Number Sender
"""
import re
import requests
from colorama import Fore

from phone_formatter import phones_query


def find_numbers(url):
    """_Find numbers from HTTPS GET request"""
    response = requests.get(url, timeout=3000)
    if response.status_code == 403:
        print("code 403")
        return None
    formatted_numbs = phones_query()
    num = ""
    for index, pn in enumerate(formatted_numbs):
        if index < len(formatted_numbs):
            num = pn
        phonenumb = num
        # response = requests.get(url, timeout=3000)
        if response.status_code == 200:
            numbers = re.findall(phonenumb, response.text)
            # numbers = re.findall(r'\d+', response.text)
            if numbers:
                print(Fore.GREEN + "Number found! --> ", numbers[0])
            else:
                print(Fore.RED + "Failed to retrieve the website or no numbers found.")
    print("code ", response.status_code)
    return None


def input_querys():
    """_Input"""
    target = "base.net.ua"
    WEBSITE_URL = "https://" + (target)
    # numbers = find_numbers(WEBSITE_URL)  # <--------------<
    find_numbers(WEBSITE_URL)
    # if numbers_found:
    # if numbers:
    #     print(Fore.GREEN + "Number found! --> ", numbers)
    # else:
    #     print(Fore.RED + "Failed to retrieve the website or no numbers found.")


input_querys()

# -=--=-=-=-= Bing Web Search v7 =-=-=-=-=-=-=-

# subscription_key = "1c5de21b71de4a0fbca851ef70335c0f"
# end_point = "https://api.bing.microsoft.com/" +  "/v7.0/"
