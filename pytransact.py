import random
from random import randrange

def is_visa(cc):
    cc = cc.replace(' ', '').replace('-', '')

    if len(cc) == 13 or len(cc) == 16:
        if cc.startswith('4') and cc.isdigit():
            return True
        else:
            return False
    else:
        return False


def is_valid_expiration(date): #"13/23"
    if len(date)==5:
        if date[0].isdigit() and date[1].isdigit() and date[3].isdigit() and date[4].isdigit() and date[2]=="/" :
            date = date.split("/")
            date[0] = int(date[0])
            date[1] = int(date[1])
            if (date[0]>=1 and date[0]<=12) and (date[1]>=1 and date[1]<=99):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

    ...

def random_visa():
    random_len = random.choice([13, 16])
    if random_len == 13:
        return str(randrange(4000000000000, 4999999999999))
    elif random_len == 16:
        return str(randrange(4000000000000000, 4999999999999999))
    ...
