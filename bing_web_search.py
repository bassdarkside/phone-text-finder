"""bing and num"""
from pprint import pprint
import re
import requests
from colorama import Fore

from phone_formatter import phones_query


def find_numbers(url):
    """_Find numbers from HTTPS GET request"""
    headers = {'Content-Type': 'text/html'}
    response = requests.get(url, timeout=3000, headers=headers)

    if response.status_code == 403:
        print("code 403")
        return None

    formatted_numbs = phones_query()
    num = ""

    for index, p_n in enumerate(formatted_numbs):
        if index < len(formatted_numbs):
            num = p_n

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
    target = ""
    web_url = "https://" + (target)
    # numbers = find_numbers(WEBSITE_URL)  # <--------------<
    find_numbers(web_url)
    # if numbers_found:
    # if numbers:
    #     print(Fore.GREEN + "Number found! --> ", numbers)
    # else:
    #     print(Fore.RED + "Failed to retrieve the website or no numbers found.")


def bing_search():
    """Bing search"""
    subscription_key = "1c5de21b71de4a0fbca851ef70335c0f"
    endpoint = "https://api.bing.microsoft.com" + "/v7.0/search"

    # Query term(s) to search for.
    query = "+38(097)129-9999"

    # Construct a request
    # mkt = "en-US"
    mkt = "ru-RU"
    params = {"q": query, "mkt": mkt}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}

    # Call the API
    try:
        response = requests.get(endpoint, headers=headers, params=params, timeout=500)
        response.raise_for_status()

        print("\nHeaders:\n")
        print(response.headers)

        print("\nJSON Response:\n")
        pprint(response.json())
        pprint(response.text)
    except Exception as ex:
        raise ex


# input_querys()
bing_search()
