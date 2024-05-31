# fmt: off

def format_number(phone_number: str):
    # Remove all non-digit characters
    digits = "".join(filter(str.isdigit, phone_number))
    if len(digits) < 10:
        return "Phone number with country code is required"
    cntry = "+38"
    oper = digits[:3]
    begin = digits[3:6]
    mid = digits[6:8]
    end = digits[8:]
    full_num = f"{cntry}{oper}{begin}{mid}{end}"
    # tel = f"tel:{full_num}"
    # full_div = f"+380 {oper[1:]} {begin}-{mid}-{end}"

    return [
        full_num,           # +000XX0000000
        full_num[1:],       # 000XX00000
        full_num[3:],       # 0XX0000000
        # full_num[4:],       # XX0000000
        # full_div,           # +000 XX 000-00-00
        # tel,                # tel:+000XX0000000
    ]

# f"38({oper}){begin}-{mid}-{end}",        # 38(044)350-74-01
# f"{cntry} {oper} {begin}-{mid}-{end}",   # +38 044 350-74-01
# f"{cntry}({oper}){begin}{mid}{end}",     # +38(044)3507401
# f"{cntry}({oper}) {begin}{mid}{end}",    # +38(044) 3507401
# f"{cntry}({oper}){begin}-{mid}{end}",    # +38(044)350-7401
# f"{cntry}({oper}){begin}-{mid}-{end}",   # +38(044)350-74-01
# f"{cntry}({oper}) {begin}-{mid}{end}",   # +38(044) 350-7401
# f"{cntry}({oper}) {begin}-{mid}-{end}",  # +38(044) 350-74-01
# f"{cntry} ({oper}) {begin}{mid}{end}",   # +38 (044) 3507401
# f"{cntry} ({oper}) {begin} {mid} {end}", # +38 (044) 350 74 01
