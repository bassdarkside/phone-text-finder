from pprint import pprint
import requests

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
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
    response = requests.get(endpoint, headers=headers, params=params, timeout=500)
    response.raise_for_status()

    print("\nHeaders:\n")
    print(response.headers)

    print("\nJSON Response:\n")
    pprint(response.json())
except Exception as ex:
    raise ex
