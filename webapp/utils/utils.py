import time
import re

import httpx
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_page_source(query: str):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = Firefox(options=options)
    try:
        driver.get("https://www.google.com")
        search = driver.find_element(By.NAME, "q")
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        time.sleep(1)
        return driver.page_source
    finally:
        driver.quit()


def get_links(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    results = soup.find("div", id="search").find_all("a")
    return [[item.get("href"), item.h3] for item in results]


def find_number_in_site(url: str, number: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    if number.startswith("+"):
        number = f"\\{number}"
    try:
        response = httpx.get(url, timeout=50, headers=headers)
        response.raise_for_status()
        return (
            response.url if (_ := re.findall(number, response.text)) else None
        )
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
    page_source_google = get_page_source(phone_number)
    urls = get_links(page_source_google)
    if page_source_google is None:
        return
    links = []
    for i in range(len(urls)):
        result = find_number_in_site(urls[i][0], phone_number)
        if result is not None:
            links.append([result, urls[i][1]])
    return links
