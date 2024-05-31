import re
import requests


def find_numbers(url, number):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, timeout=50, headers=headers)
    if "+" in number:
        number = f"\\{number}"
    try:
        if response.status_code == 200:
            result = re.findall(number, response.text)
            if result:
                return response.url
    except requests.exceptions.ConnectionError:
        return "Error message: No connection to target."
    except re.error:
        return "Error message: Invalid regular expression."
