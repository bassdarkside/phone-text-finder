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
    input_query = ph_query[0]
    web_data = client.web.search(query=input_query)
    print("\nSearched for Query#", input_query)
    first_page = []
    names = []
    # WebPages
    if web_data.web_pages:

        print("\nWebpage Results#", len(web_data.web_pages.value))
        # First
        first_web_page = web_data.web_pages.value[0]
        first_page.append(first_web_page.url)
        names.append(first_web_page.name)
        sec = web_data.web_pages.value[1]
        first_page.append(sec.url)
        names.append(sec.name)
        thi = web_data.web_pages.value[2]
        first_page.append(thi.url)
        names.append(thi.name)
        print("\nFirst web page name: ", first_web_page.name)
        print("First web page URL: ", first_web_page.url)
        # Second
        # second_web_page = web_data.web_pages.value[1]
        # print("\nSecond web page name: ", second_web_page.name)
        # print("Second web page URL: ", second_web_page.url)

        # return first_web_page.url
    else:
        print("Didn't see any Web data..")
    
    print(names)
    return first_page
    # except Exception as err:
    #     print("Encountered exception. ", err)

# if __name__ == "__main__":
#     bing_search(SUBSCRIPTION_KEY)
