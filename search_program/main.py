"""Find numbers from HTTPS GET request"""
from pprint import pprint
import re
import requests
from colorama import Fore

from web_search_client import WebSearchClient
from azure.core.credentials import AzureKeyCredential


SUBSCRIPTION_KEY = "1c5de21b71de4a0fbca851ef70335c0f"
ENDPOINT = "https://api.bing.microsoft.com" + "/v7.0"

PHONE_NUMBER = "073 175-35-58"
# QUERY = "063 537-13-86"
# QUERY = "068 012-97-82"
# QUERY = "068 850-47-63"
# QUERY = "073 641-09-38"
# QUERY = "073 675-56-31"
# QUERY = "073 873-05-20"

""" Numbers:
    "050 426-02-25" Агенти з нерухомості https://ktozvonit.com.ua/050/19/4260000-4269999
    "097 129-99-99" Vilcov.com +380 (63) 363-44-44
    "063 942 95-70" Шваб А.В.
    "098 759-08-23"
    "073 142-83-14" негативні відгуки, реклама / нав'язування
    "073 148-20-44" негативні відгуки, реклама / нав'язування
"""


def main():
    list_url = bing_search(SUBSCRIPTION_KEY)
    num = ""
    for index, item in enumerate(list_url):
        if index < len(list_url):
            link = item
        #link = num
        find_numbers(link)


def format_phone_number(phone_number):

    digits = "".join(filter(str.isdigit, phone_number))
    if len(digits) != 10:
        return "Invalid phone number"
    return f"38{digits[:3]}{digits[3:6]}{digits[6:8]}{digits[8:]}"


def find_numbers(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, timeout=500, headers=headers)
        if response.status_code != 200:
            return print(response.status_code)
    
        phone_number = format_phone_number(PHONE_NUMBER)
        numbers = re.findall(phone_number, response.text)
        if numbers:
            print(
                f"{Fore.GREEN}Found! >---> ",
                numbers[0],
                " in >---> ",
                response.url,
            )
        if numbers is None:
            print(
                f"{Fore.RED}Failed to retrieve the website or no numbers found."
            )
    except requests.exceptions.ConnectionError:
        return print(
            "Custom error message: Unable to establish a connection. Please check your internet connection."
        )


def bing_search(subscription_key):
    client = WebSearchClient(AzureKeyCredential(subscription_key))
    
    input_query = format_phone_number(PHONE_NUMBER)
    
    web_data = client.web.search(query=input_query, set_lang="ru-RU")
    print("\nSearched for Query#", input_query)
    pages = []
    if web_data.web_pages:
        print("\nWebpage Results#", len(web_data.web_pages.value))
        data = web_data.web_pages.value
        for i in range(len(data)):
            add = web_data.web_pages.value[i]
            pages.append(add.url)
    else:
        print("Didn't see any Web data...")
    pprint(pages)
    return pages


if __name__ == "__main__":
    main()
