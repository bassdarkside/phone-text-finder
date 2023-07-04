"""
    Request Number Sender
"""
import re
import requests
from colorama import Fore

# from azure.cognitiveservices.search.websearch import WebSearchAPI
# from azure.cognitiveservices.search.websearch.models import SafeSearch
# from msrest.authentication import CognitiveServicesCredentials
from phone_formatter import phones_query


def find_numbers(url):
    """
    Find numbers from HTTPS GET request
    """
    formatted_numbs = phones_query()
    for num in formatted_numbs:
        phonenumb = num
        response = requests.get(url, timeout=500)
        if response.status_code == 200:
            numbers = re.findall(phonenumb, response.text)
            # numbers = re.findall(r'\d+', response.text)
            return numbers
    return None


WEBSITE_URL = "https://" + ("patriot.ua")
numbers_found = find_numbers(WEBSITE_URL)  # <--------------<

if numbers_found:
    print(Fore.GREEN + "Number found! --> ", Fore.RED + numbers_found[0])
else:
    print(Fore.RED + "Failed to retrieve the website or no numbers found.")
# WEBSITE_URL = 'https://'+ input(
#           "Enter website for search phone number like this format 'example.com': ")
# 1c5de21b71de4a0fbca851ef70335c0f
# https://api.bing.microsoft.com/

# =-=--=-=-=-==-=-=-=-=-=-=-=-=-
# def search_string_bing(search_term, API_KEY):
#     # Инициализация клиента Bing Search API
#     credentials = CognitiveServicesCredentials(API_KEY)
#     client = WebSearchAPI(credentials)

#     # Выполнение поиска
#     web_data = client.web.search(query=search_term, safesearch=SafeSearch.strict)

#     # Извлечение результатов поиска
#     results = web_data.web_pages.value

#     # Возвращение результатов
#     return results

# # Пример использования
# search_term = formatted_phone
# API_KEY = '1c5de21b71de4a0fbca851ef70335c0f'

# results = search_string_bing(search_term, API_KEY)
# print("Результаты поиска в сети интернет:")
# for result in results:
#     print(result.name)
#     print(Fore.GREEN + result.url)
#     print()
