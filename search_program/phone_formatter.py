"""
    This script makes phone numbers formatting 
"""
# from colorama import Fore


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

    return formatted_number


def list_format_number(phone_number):
    """
    List phone number formater
    """
    # Remove all non-digit characters
    digits = "".join(filter(str.isdigit, phone_number))
    cntry = "+38"
    oper = digits[:3]
    begin = digits[3:6]
    mid = digits[6:8]
    end = digits[8:]
    # List formats
    format_list_number = [
        f"{oper}{begin}{mid}{end}",  #    0443507401
        f"{oper} {begin}{mid}{end}",  #    044 3507401
        f"38{oper}{begin}{mid}{end}",  # 380443507401
        f"38({oper}){begin}-{mid}-{end}",  # 38(044)350-74-01
        f"{cntry}{oper}{begin}{mid}{end}",  # +380443507401
        f"{cntry}({oper}){begin}{mid}{end}",  # +38(044)3507401
        f"{cntry}({oper}) {begin}{mid}{end}",  # +38(044) 3507401
        f"{cntry}({oper}){begin}-{mid}{end}",  # +38(044)350-7401
        f"{cntry}({oper}) {begin}-{mid}{end}",  # +38(044) 350-7401
        f"{cntry} {oper} {begin}-{mid}-{end}",  # +38 044 350-74-01
        f"{cntry}({oper}){begin}-{mid}-{end}",  # +38(044)350-74-01
        f"{cntry}({oper}) {begin}-{mid}-{end}",  # +38(044) 350-74-01
        f"{cntry} ({oper}) {begin}{mid} {end}",  # +38 (044) 3507401
        f"{cntry} ({oper}) {begin}-{mid}-{end}",  # +38 (044) 350-74-01
        f"{cntry} ({oper}) {begin} {mid} {end}",  # +38 (044) 350 74 01
    ]
    return format_list_number


def phones_query():
    '''phones list'''
    # phone = [
    phone = "063 942 95-70"
    #   "063 537-13-86",

    #   "068 012-97-82",
    #   "068 850-47-63",

    #     "073 142-83-14",
    #     "073 148-20-44",
    #     "073 175-35-58",
    #     "073 641-09-38",
    #     "073 675-56-31",
    #     "073 873-05-20",
    # ]
    # fphones = []
    # # f_list = []
    # for i in phone:
    #     numbers_after_format = format_phone_number(i)
    #     fphones.append(numbers_after_format)

        # list_after_format = list_format_number(i)
        # f_list.append(list_after_format)
    # return fphones
    fphone = format_phone_number(phone)
    return fphone


# phones_query()

# PHONE = "067 346 7247" # test for patriot.ua
# PHONE = input("\nEnter phone number as 10-digits format\nPhone number: ")
# print(Fore.BLUE + "NON-formatted phone number -> ", PHONE)
# print(Fore.GREEN + "FORMATTED  phone number -> ", formatted_phone + Fore.RESET)
