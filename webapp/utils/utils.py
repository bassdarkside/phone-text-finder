import re
import httpx
from urllib.parse import quote
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4703.0 Safari/537.36"
}


def get_links(query: str):
    query = quote(query)
    google_url = f"https://www.google.com/search?q={query}"
    print("query url: ", google_url)
    try:
        r = httpx.get(google_url, headers=headers)
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
        return None
    print("responce status code is: ", r.status_code)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
        results_links = []
        for i in soup.select(".g"):
            link = i.find("a").get("href")
            if link is not None:
                results_links.append(link)

        return results_links


def find_number_in_site(url: str, number: str):
    if number.startswith("+"):
        number = f"\\{number}"
    try:
        r = httpx.get(url, timeout=3, headers=headers)
        r.raise_for_status()
        return r.url if (_ := re.findall(number, r.text)) else None
    except re.error:
        return "Error message: Invalid regular expression."
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting the URL: {exc}")
    except httpx.HTTPStatusError as exc:
        print(
            f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
        )


def main_search(country_code: str, input_number: str) -> list:
    phone_number = "".join([country_code, input_number])
    urls = get_links(phone_number)
    if urls is None:
        return
    links = []
    for link in urls:
        print("link from google: ", link)
        result = find_number_in_site(link, phone_number)
        if result is not None:
            links.append(link)
    return links
