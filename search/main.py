from .formatter import format_number
from .finder import find_numbers
from .selenm import selen


def searching(unformatted_number):
    formatted_number = format_number(unformatted_number)
    if formatted_number is not list():
        return formatted_number
    n = set()
    urls = []
    for number in formatted_number:
        urls = selen(number)
        if urls is not None:
            for url in urls:
                u = find_numbers(url, number)
                if u is not None and "translate" not in u:
                    n.add(u)
    return n
