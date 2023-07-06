"""
    This script makes phone numbers formatting 
"""


def format_phone_number(phone_number):
    """
    Phone number formater
    """
    # Remove all non-digit characters
    digits = "".join(filter(str.isdigit, phone_number))

    # Check if the number has a valid length
    if len(digits) != 10:
        return "Invalid phone number"

    # Format the number as (XXX) XXX-XXXX
    formatted_number = f"38{digits[:3]}{digits[3:6]}{digits[6:8]}{digits[8:]}"
    # formatted_number = f"38({digits[:3]}){digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    # formatted_number1 = f"+38{digits[:3]}{digits[3:6]}{digits[6:8]}{digits[8:]}"
    # formatted_number2 = f"+38({digits[:3]}){digits[3:6]}{digits[6:8]}{digits[8:]}"
    # formatted_number3 = f"+38({digits[:3]}){digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    # formatted_number4 = f"+38({digits[:3]}){digits[3:6]}-{digits[6:8]}{digits[8:]}"
    # formatted_number5 = f"+38({digits[:3]}) {digits[3:6]}{digits[6:8]}{digits[8:]}"
    # formatted_number6 = f"+38({digits[:3]}) {digits[3:6]}-{digits[6:8]}{digits[8:]}"
    # formatted_number7 = f"+38({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    # formatted_number8 = f"+38 ({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    # formatted_number9 = f"+38 {digits[:3]} {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    # print("Formattedd numbers: ", formatted_number)
    return formatted_number

    # return formatted_number, formatted_number1, formatted_number2, \
    #         formatted_number3, formatted_number4, formatted_number5, \
    #         formatted_number6, formatted_number7, formatted_number8, \
    #             formatted_number9


def phones_query():
    phone = [
        "073 873-05-20",
        "073 148-20-44",
        "073 175-35-58",
        "073 675-56-31",
        "073 142-83-14",
        "073 641-09-38",
        "068 850-47-63",
        "068 012-97-82",
        "050 426-02-25",
        "063 537-13-86",
        "044 350-74-01",
        "044 350-74-02",
        "097 129-99-99",
        "098 759-08-23",
    ]
    fphones = []
    for i in phone:
        numbers_after_format = format_phone_number(i)
        fphones.append(numbers_after_format)

    # print(fphones)
    return fphones


# phones_query()

# PHONE = "0673467247" # test for patriot.ua
# PHONE = input("\nEnter phone number as 10-digits format\nPhone number: ")
# print(Fore.BLUE + "NON-formatted phone number -> ", PHONE)
# print(Fore.GREEN + "FORMATTED  phone number -> ", formatted_phone + Fore.RESET)
