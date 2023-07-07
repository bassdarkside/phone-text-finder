'''WORKING!!!'''
from pprint import pprint
from web_search_client import WebSearchClient
from azure.core.credentials import AzureKeyCredential

from phone_formatter import phones_query

SUBSCRIPTION_KEY = "1c5de21b71de4a0fbca851ef70335c0f"
ENDPOINT = "https://api.bing.microsoft.com"+  "/v7.0/"

def counter(ph_query):
    # ph_query = phones_query()
    q_numb = ""
    for i in range(len(ph_query)):
        q_numb = ph_query[i]
        print(q_numb)
    return q_numb

def bing_search(subscription_key):
    """WebSearchResultTypesLookup.

    This will look up a single query (Xbox) and print out name and url for first web results.
    """
    client = WebSearchClient(AzureKeyCredential(subscription_key))
    # ph_query = phones_query()
    # for i in range(len(ph_query)):
    #     q_numb = ph_query[i]
    ph_query = phones_query()

    numb = counter(ph_query)
    input_query = numb
    # input_query = ph_query[0]
    web_data = client.web.search(query=input_query)
    print("\nSearched for Query#", input_query)
    pages = []
    # WebPages
    if web_data.web_pages:

        print("\nWebpage Results#", len(web_data.web_pages.value))
        data = web_data.web_pages.value
        for i in range(len(data)):
            add = web_data.web_pages.value[i]
            # pprint(add.url)
            pages.append(add.url)
        # First
        # first_web_page = web_data.web_pages.value[0]
        # print("\nFirst web page name: ", first_web_page.name)
        # print("First web page URL: ", first_web_page.url)
        # return first_web_page.url
    else:
        print("Didn't see any Web data..")
    # pprint(pages)
    return pages
    # except Exception as err:
    #     print("Encountered exception. ", err)

# if __name__ == "__main__":
#     bing_search(SUBSCRIPTION_KEY)
