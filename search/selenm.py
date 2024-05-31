import time
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def selen(query):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = Firefox(options=options)
    driver.get("https://www.google.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys(query)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    driver.quit()
    results = soup.find("div", id="search").find_all("a")  # type: ignore
    res = set()
    for item in results:
        res.add(item.get("href"))
    return res
