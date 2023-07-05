"""
    Request Number Sender
"""
import re
import requests
from colorama import Fore

from phone_formatter import phones_query

# from azure.cognitiveservices.search.websearch import WebSearchAPI
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials


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
# WEBSITE_URL = 'https://'+ input(
#           "Enter website for search phone number like this format 'example.com': ")
# 1c5de21b71de4a0fbca851ef70335c0f
# https://api.bing.microsoft.com/


# =-=--=-=-=-==-=-=-=-=-=-=-=-=-
def search_string_bing(search_term, API_KEY):
    # Инициализация клиента Bing Search API
    credentials = CognitiveServicesCredentials(API_KEY)
    client = WebSearchAPI(credentials)

    # Выполнение поиска
    web_data = client.web.search(query=search_term, safesearch=SafeSearch.strict)

    # Извлечение результатов поиска
    results = web_data.web_pages.value

    # Возвращение результатов
    return results


# Пример использования
search_term = "projector"
API_KEY = "1c5de21b71de4a0fbca851ef70335c0f"

results = search_string_bing(search_term, API_KEY)
print("Результаты поиска в сети интернет:")
for result in results:
    print(result.name)
    print(Fore.GREEN + result.url)
    print()
