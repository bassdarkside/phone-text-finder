"""Find numbers from HTTPS GET request"""

import re
import requests
from goggle_main import goggle_src


PHONE_NUMBER = "073 175-35-58"


def format_phone_number(phone_number):
    digits = "".join(filter(str.isdigit, phone_number))
    if len(digits) != 10:
        return "Invalid phone number"
    return f"38{digits[:3]}{digits[3:6]}{digits[6:8]}{digits[8:]}"


def find_numbers(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, timeout=5, headers=headers)
        assert response.ok
        if response.status_code != 200:
            return print(response.status_code)

        phone_number = format_phone_number(PHONE_NUMBER)
        numbers = re.findall(phone_number, response.text)
        if numbers:
            print("Found! ---> ", response.url)
    except requests.exceptions.ConnectionError:
        return print(
            "Error message: Unable to establish a connection. \
            Please check your internet connection."
        )


def main():
    list_url = goggle_src(format_phone_number(PHONE_NUMBER))
    for index, item in enumerate(list_url):
        if index < len(list_url):
            link = item
        find_numbers(link)


if __name__ == "__main__":
    main()
