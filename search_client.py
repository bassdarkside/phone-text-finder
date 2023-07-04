# Import required modules.
# from web_search_client import WebSearchClient
from azure.core.credentials import AzureKeyCredential


SUBSCRIPTION_KEY = "1c5de21b71de4a0fbca851ef70335c0f"
ENDPOINT = "https://api.bing.microsoft.com" + "/v7.0/search"  # "/v7.0/"


def web_results_with_count_and_offset(subscription_key):
    """
    Set the query, offset, and count using the SDK's search method. See:
    https://learn.microsoft.com/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.operations.weboperations?view=azure-python.
    """
    client = WebSearchClient(AzureKeyCredential(SUBSCRIPTION_KEY))

    try:
        web_data = client.web.search(
            query="380673467247",
            count=10,
            location="UA",
            accept_language=("ru-RU", "uk", "uk2"),
            text_decorations=True,
            text_format="HTML",
            set_lang="uk2",
        )
        print('\r\nSearching for "380673467247"')

        if web_data.web_pages.value:
            print("Webpage Results#{}".format(len(web_data.web_pages.value))) # If web pages are available, print the # of responses, and the first and second web pages returned.

            first_web_page = web_data.web_pages.value
            for n in first_web_page:
                print("Web page name: {} ".format(n.name))
                print("Web page URL: {} ".format(n.url))

            # second_web_page = web_data.web_pages.value[1]
            # print("Second web page1 name: {} ".format(second_web_page.name))
            # print("Second web page URL: {} ".format(second_web_page.url))

        else:
            print("Didn't find any web pages...")

    except Exception as err:
        print("Encountered exception. {}".format(err))


web_results_with_count_and_offset(SUBSCRIPTION_KEY)
