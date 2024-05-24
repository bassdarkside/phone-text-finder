""" This script makes phone numbers formatting """


def format_phone_number(phone_number):
    """Функция `format_phone_number` принимает номер телефона в
        качестве входных данных, удаляет все нецифровые символы,
        проверяет допустимую длину номера и возвращает
        отформатированный номер телефона с префиксом "38".

    :param phone_number:    Параметр phone_number представляет собой строку,
                            представляющую номер телефона.
    :return:                отформатированный номер телефона в формате «38XXX-XXX-XX-XX».

    Если введенный номер телефона недействителен (не ровно 10 цифр),
    он возвращает строку «Неверный номер телефона».
    """
    digits = "".join(filter(str.isdigit, phone_number))
    if len(digits) != 10:
        return "Invalid phone number"
    return f"38{digits[:3]}{digits[3:6]}{digits[6:8]}{digits[8:]}"


def list_format_number(phone_number):
    """
    Функция форматирует номер телефона,
    добавляя дефисы в соответствующих местах.

    :param phone_number: Строка, представляющая номер телефона
    """
    # Remove all non-digit characters
    digits = "".join(filter(str.isdigit, phone_number))
    cntry = "+38"
    oper = digits[:3]
    begin = digits[3:6]
    mid = digits[6:8]
    end = digits[8:]
    return [
        # 0443507401
        f"{oper}{begin}{mid}{end}",
        # 044 3507401
        f"{oper} {begin}{mid}{end}",
        # 380443507401
        f"38{oper}{begin}{mid}{end}",
        # 38(044)350-74-01
        f"38({oper}){begin}-{mid}-{end}",
        # +380443507401
        f"{cntry}{oper}{begin}{mid}{end}",
        # +38(044)3507401
        f"{cntry}({oper}){begin}{mid}{end}",
        # +38(044) 3507401
        f"{cntry}({oper}) {begin}{mid}{end}",
        # +38(044)350-7401
        f"{cntry}({oper}){begin}-{mid}{end}",
        # +38(044) 350-7401
        f"{cntry}({oper}) {begin}-{mid}{end}",
        # +38 044 350-74-01
        f"{cntry} {oper} {begin}-{mid}-{end}",
        # +38(044)350-74-01
        f"{cntry}({oper}){begin}-{mid}-{end}",
        # +38(044) 350-74-01
        f"{cntry}({oper}) {begin}-{mid}-{end}",
        # +38 (044) 3507401
        f"{cntry} ({oper}) {begin}{mid} {end}",
        # +38 (044) 350-74-01
        f"{cntry} ({oper}) {begin}-{mid}-{end}",
        # +38 (044) 350 74 01
        f"{cntry} ({oper}) {begin} {mid} {end}",
    ]


def phones_query(phone_num):
    return format_phone_number(phone_num)


# fphones = []
# # f_list = []
# for i in phone:
#     numbers_after_format = format_phone_number(i)
#     fphones.append(numbers_after_format)

# list_after_format = list_format_number(i)
# f_list.append(list_after_format)
# return fphones
