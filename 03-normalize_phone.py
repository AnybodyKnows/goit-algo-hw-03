
import re

def add_prefix (numers):
    if len(numers)<7:
        return(f"incorect number {numers} not inough digits")
    if re.search(r"^0",numers):
        num_with_prefix = "+38"+numers
    if re.search(r"^8",numers):
        num_with_prefix = "+3"+numers
    if re.search(r"^3",numers):
        num_with_prefix = "+"+numers
    return num_with_prefix
   
def normalize_phone(phone_number):
    st_nr = []
    for i in phone_number:
        patern = r"\d+"
        matches = re.findall(patern,i)
        only_number = "".join(matches)
        
        st_nr.append("".join(add_prefix(only_number)))
    return f"Stundurtized numbers for sms sending: {st_nr}"




raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "123456"
]
print (normalize_phone(raw_numbers))