import requests

# from rich import print

API_KEY = open("search_program/API_KEY").read()
SEARCH_ENGINE_ID = open("search_program/SEARCH_ENGINE_ID").read()


def google_src(search_query):
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
    links = []
    for items in results:
        # title, link = items["title"], items["link"]
        links.append(items["link"])
    return links
