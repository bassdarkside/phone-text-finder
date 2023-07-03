'''
    Request Number Sender
'''
import re
import requests
from colorama import Fore
from PhoneFormatter import phones_query

#def format_phone_number(phone_number):
    #'''
    #    Phone number formater
    #'''
    # Remove all non-digit characters
    #digits = ''.join(filter(str.isdigit, phone_number))

    # Check if the number has a valid length
    #if len(digits) != 10:
    #    return "Invalid phone number"

    #formatted_number = f"38{digits[:3]}{digits[3:6]}{digits[6:8]}{digits[8:]}"
 
    #print(Fore.GREEN + "Formattedd numbers: ", fotmatted_number + Fore.RESET)
    #return formatted_number

# PHONE = "0673467247" # test for patriot.is
#PHONE = [
#        "073 873-05-20",
#        "073 148-20-44",
#        "073 175-35-58",
#        "073 675-56-31",
#        "068 850-47-63"
#        ]
        
#for i in PHONE:
#   formatted_phone = format_phone_number(i)

def find_numbers(url):
    '''
        Find numbers from HTTPS GET request
    '''
    phonenumb = PhoneFormatter.phones_query()
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

