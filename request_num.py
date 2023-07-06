"""
    Request Number Sender
"""
# import re
# import requests
# from colorama import Fore

# from phone_formatter import phones_query


# def find_numbers(url):
#     """_Find numbers from HTTPS GET request"""
#     response = requests.get(url, timeout=3000)
#     if response.status_code == 403:
#         print("code 403")
#         return None
#     formatted_numbs = phones_query()
#     num = ""
#     for index, p_n in enumerate(formatted_numbs):
#         if index < len(formatted_numbs):
#             num = p_n
#         phonenumb = num
#         # response = requests.get(url, timeout=3000)
#         if response.status_code == 200:
#             numbers = re.findall(phonenumb, response.text)
#             # numbers = re.findall(r'\d+', response.text)
#             if numbers:
#                 print(Fore.GREEN + "Number found! --> ", numbers[0])
#             else:
#                 print(Fore.RED + "Failed to retrieve the website or no numbers found.")
#     print("code ", response.status_code)
#     return None


# def input_querys():
#     """_Input"""
#     target = "patriot.ua"
#     web_url = "https://" + (target)
#     # numbers = find_numbers(WEBSITE_URL)  # <--------------<
#     find_numbers(web_url)
#     # if numbers_found:
#     # if numbers:
#     #     print(Fore.GREEN + "Number found! --> ", numbers)
#     # else:
#     #     print(Fore.RED + "Failed to retrieve the website or no numbers found.")


# input_querys()

# -=--=-=-=-= Bing Web Search v7 =-=-=-=-=-=-=-

# subscription_key = "1c5de21b71de4a0fbca851ef70335c0f"
# end_point = "https://api.bing.microsoft.com/" +  "/v7.0/"
import requests
from IPython.core.display import HTML

def bing_search():
    subscription_key = "1c5de21b71de4a0fbca851ef70335c0f"
    assert subscription_key

    search_url = "https://api.bing.microsoft.com/v7.0/search"
    search_term = "Microsoft Bing Search Services"

    # Make request
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    # Format and view response

    rows = "\n".join(["""<tr>
                        <td><a href=\"{0}\">{1}</a></td>
                        <td>{2}</td>
                        </tr>""".format(v["url"], v["name"], v["snippet"])
                    for v in search_results["webPages"]["value"]])
    HTML("<table>{0}</table>".format(rows))
