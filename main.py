import random
import string


def gen_pw(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for __ in range(length))
    return password


# password = gen_pw()
# print(f'newly generated password --> {password}')
