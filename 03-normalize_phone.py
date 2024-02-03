
import re

def add_prefix (numers):
    match len(numers):
        case 10:
            stnum = "+38"+numers
        case 11:
            stnum = "+3"+numers
        case 12:
            stnum = "+"+numers
        case _:
            stnum = ""
    return stnum
   
def normalize_phone(phone_number):
    if type(phone_number) == str:
        phone_number_list = []
        phone_number_list.append(phone_number)
    else:
        phone_number_list = phone_number
    st_nr = []
    for i in phone_number_list:
        patern = r"\d+"
        matches = re.findall(patern,i)
        only_number = "".join(matches)
        
        st_nr.append("".join(add_prefix(only_number)))
    return f"Stundurtized numbers for sms sending: {st_nr}"




raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    
    ]
print (normalize_phone("+123456789012"))
print (normalize_phone("432 11 222 22 22"))
print (normalize_phone(raw_numbers))