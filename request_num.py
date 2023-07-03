'''
    Request Number Sender
'''
import re
import requests
from colorama import Fore

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
    #formatted_number1 = f"+38{digits[:3]}{digits[3:6]}{digits[6:8]}{digits[8:]}"
    #formatted_number2 = f"+38({digits[:3]}){digits[3:6]}{digits[6:8]}{digits[8:]}"
    #formatted_number3 = f"+38({digits[:3]}){digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    #formatted_number4 = f"+38({digits[:3]}){digits[3:6]}-{digits[6:8]}{digits[8:]}"
    #formatted_number5 = f"+38({digits[:3]}) {digits[3:6]}{digits[6:8]}{digits[8:]}"
    #formatted_number6 = f"+38({digits[:3]}) {digits[3:6]}-{digits[6:8]}{digits[8:]}"
    #formatted_number7 = f"+38({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    #formatted_number8 = f"+38 ({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    #formatted_number9 = f"+38 {digits[:3]} {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    print(Fore.GREEN + "Formattedd numbers: ", fotmatted_number + Fore.RESET)
    return formatted_number

    # return formatted_number, formatted_number1, formatted_number2, \
    #         formatted_number3, formatted_number4, formatted_number5, \
    #         formatted_number6, formatted_number7, formatted_number8, \
    #             formatted_number9

# PHONE = "0673467247" # test for patriot.is
PHONE = [
        "073 873-05-20",
        "073 148-20-44",
        "073 175-35-58",
        "073 675-56-31",
        "068 850-47-63"
        ]
# PHONE = input("\nEnter phone number as 10-digits format\nPhone number: ")
for i in PHONE:
    formatted_phone = format_phone_number(i)
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


# WEBSITE_URL = 'https://'+ input("Enter website for search phone number like this format 'example.com': ")
# numbers_found = find_numbers(WEBSITE_URL)
# if numbers_found:
    # print(Fore.GREEN + "Number found! --> ", Fore.RED + numbers_found[0])
# else:
    # print(Fore.RED + "Failed to retrieve the website or no numbers found.")
# 1c5de21b71de4a0fbca851ef70335c0f
# https://api.bing.microsoft.com/

from azure.cognitiveservices.search.websearch import WebSearchAPI
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

def search_string_bing(search_term, api_key):
    # Инициализация клиента Bing Search API
    credentials = CognitiveServicesCredentials(api_key)
    client = WebSearchAPI(credentials)

    # Выполнение поиска
    web_data = client.web.search(query=search_term, safesearch=SafeSearch.strict)

    # Извлечение результатов поиска
    results = web_data.web_pages.value

    # Возвращение результатов
    return results

# Пример использования
search_term = formatted_phone   # Замените на нужную вам строку для поиска
api_key = '1c5de21b71de4a0fbca851ef70335c0f'  # Замените на ваш ключ API Bing Search

results = search_string_bing(search_term, api_key)
print(f"Результаты поиска в сети интернет:")
for result in results:
    print(result.name)
    print(result.url)
    print()

