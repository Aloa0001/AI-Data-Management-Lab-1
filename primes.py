import math as m


# Validate prim numbers
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(m.ceil(number / 2))):
        if number % i == 0:
            return False
    return True
