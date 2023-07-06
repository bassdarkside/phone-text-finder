import os
from web_search_client import WebSearchClient
from web_search_client.models import SafeSearch
from azure.core.credentials import AzureKeyCredential

SUBSCRIPTION_KEY = "1c5de21b71de4a0fbca851ef70335c0f"
ENDPOINT = "https://api.bing.microsoft.com"+  "/v7.0/"




def result_types_lookup(subscription_key):
    """WebSearchResultTypesLookup.

    This will look up a single query (Xbox) and print out name and url for first web, image, news and videos results.
    """
    client = WebSearchClient(AzureKeyCredential(SUBSCRIPTION_KEY))

    try:

        web_data = client.web.search(query="xbox")
        print("Searched for Query# \" Xbox \"")

        # WebPages
        if web_data.web_pages.value:

            print("Webpage Results#{}".format(len(web_data.web_pages.value)))

            first_web_page = web_data.web_pages.value[0]
            print("First web page name: {} ".format(first_web_page.name))
            print("First web page URL: {} ".format(first_web_page.url))

        else:
            print("Didn't see any Web data..")


    except Exception as err:
        print("Encountered exception. {}".format(err))


def web_results_with_count_and_offset(subscription_key):
    """WebResultsWithCountAndOffset.

    This will search (Best restaurants in Seattle), verify number of results and print out name and url of first result.
    """

    client = WebSearchClient(AzureKeyCredential(SUBSCRIPTION_KEY))

    try:
        web_data = client.web.search(
            query="Best restaurants in Seattle", offset=10, count=20)
        print("Searched for Query# \" Best restaurants in Seattle \"")

        if web_data.web_pages.value:

            print("Webpage Results#{}".format(len(web_data.web_pages.value)))

            first_web_page = web_data.web_pages.value[0]
            print("First web page name: {} ".format(first_web_page.name))
            print("First web page URL: {} ".format(first_web_page.url))

        else:
            print("Didn't see any Web data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))

    """WebSearchWithAnswerCountPromoteAndSafeSearch.

    This will search (Lady Gaga) with answerCount and promote parameters and print details of answers.
    """

    client = WebSearchClient(AzureKeyCredential(SUBSCRIPTION_KEY))

    try:
        web_data = client.web.search(
            query="Lady Gaga",
            answer_count=2,
            promote=["videos"],
            safe_search=SafeSearch.strict  # or directly "Strict"
        )
        print("Searched for Query# \" Lady Gaga\"")

        if web_data.web_pages.value:

            print("Webpage Results#{}".format(len(web_data.web_pages.value)))

            first_web_page = web_data.web_pages.value[0]
            print("First web page name: {} ".format(first_web_page.name))
            print("First web page URL: {} ".format(first_web_page.url))

        else:
            print("Didn't see any Web data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))

if __name__ == "__main__":
    result_types_lookup(SUBSCRIPTION_KEY)
    web_results_with_count_and_offset(SUBSCRIPTION_KEY)
