import requests
from rich import print

API_KEY = open("search_program/API_KEY").read()
SEARCH_ENGINE_ID = open("search_program/SEARCH_ENGINE_ID").read()

search_query = "+380 63 505 38 14"

url = "https://www.googleapis.com/customsearch/v1"

params = {
    "q": search_query,
    "key": API_KEY,
    "cx": SEARCH_ENGINE_ID,
    "lr": "lang_ua",
    "gl": "UA",
    "exactTerms": "",
}

response = requests.get(url, params=params)
results = response.json()["items"]
for items in results:
    print(items["title"], items["link"], sep="\n")
