import random as rd

def get_numbers_ticket(min:int, max:int, quantity:int):
    if min < 1:
        return None
    if max > 1000:
        return None

    full_list_of_numbers = [i for i in range (min, max)]
    sample_list = ()
    sample_list = rd.sample(full_list_of_numbers,quantity)
    return sorted(sample_list)


print (get_numbers_ticket(1,49,6))



