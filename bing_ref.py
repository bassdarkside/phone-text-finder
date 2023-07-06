'''WORKING!!!'''
from pprint import pprint
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
    input_query = ph_query[0]
    web_data = client.web.search(query=input_query)
    print("\nSearched for Query#", input_query)
    pages = []
    # names = []
    # WebPages
    if web_data.web_pages:

        print("\nWebpage Results#", len(web_data.web_pages.value))
        data = web_data.web_pages.value
        for i in range(len(data)):
            add = web_data.web_pages.value[i]
            pages.append(add.url)
        # First
        # first_web_page = web_data.web_pages.value[0]
        # sec = web_data.web_pages.value[1]
        # thi = web_data.web_pages.value[2]
        # four = web_data.web_pages.value[3]
        # five = web_data.web_pages.value[4]
        # pages.append(first_web_page.url)
        # pages.append(sec.url)
        # pages.append(thi.url)
        # pages.append(four.url)
        # pages.append(five.url)
        # names.append(first_web_page.name)
        # names.append(sec.name)
        # names.append(thi.name)
        # print("\nFirst web page name: ", first_web_page.name)
        # print("First web page URL: ", first_web_page.url)
        # Second
        # second_web_page = web_data.web_pages.value[1]
        # print("\nSecond web page name: ", second_web_page.name)
        # print("Second web page URL: ", second_web_page.url)

        # return first_web_page.url
    else:
        print("Didn't see any Web data..")
    
    pprint(pages)
    return pages
    # except Exception as err:
    #     print("Encountered exception. ", err)

# if __name__ == "__main__":
#     bing_search(SUBSCRIPTION_KEY)
