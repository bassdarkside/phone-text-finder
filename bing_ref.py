'''WORKING!!!'''
from web_search_client import WebSearchClient
from azure.core.credentials import AzureKeyCredential

from phone_formatter import phones_query

SUBSCRIPTION_KEY = "1c5de21b71de4a0fbca851ef70335c0f"
ENDPOINT = "https://api.bing.microsoft.com"+  "/v7.0/"


def bing_search(subscription_key):
    """WebSearchResultTypesLookup.

    This will look up a single query (Xbox) and print out name and url for first web results.
    """
    client = WebSearchClient(AzureKeyCredential(subscription_key))
    ph_query = phones_query()
    num = ""
    for index, p_n in enumerate(ph_query):
        if index < len(ph_query):
            num = p_n
    input_query = num
    try:

        web_data = client.web.search(query=input_query)
        print("\nSearched for Query#", input_query)

        # WebPages
        if web_data.web_pages:

            print("\nWebpage Results#", len(web_data.web_pages.value))
            # First
            first_web_page = web_data.web_pages.value[0]
            print("\nFirst web page name: ", first_web_page.name)
            print("First web page URL: ", first_web_page.url)
            # Second
            # second_web_page = web_data.web_pages.value[1]
            # print("\nSecond web page name: ", second_web_page.name)
            # print("Second web page URL: ", second_web_page.url)
            return first_web_page.url
        else:
            print("Didn't see any Web data..")


    except Exception as err:
        print("Encountered exception. ", err)
if __name__ == "__main__":
    bing_search(SUBSCRIPTION_KEY)
