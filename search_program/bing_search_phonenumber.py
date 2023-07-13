""" WORKING??? 
"""
from pprint import pprint
import requests


def bing_to_search():
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
        _extracted_from_bing_to_search_17(endpoint, headers, params)
    except Exception as ex:
        raise ex


# TODO Rename this here and in `bing_to_search`
def _extracted_from_bing_to_search_17(endpoint, headers, params):
    response = requests.get(
        endpoint, headers=headers, params=params, timeout=500
    )
    response.raise_for_status()

    print("\nHeaders:\n")
    print(response.headers)

    print("\nJSON Response:\n")
    pprint(response.json())
    pprint(response.text)
