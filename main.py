import random
import string


def get_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for __ in range(length))
    return password


password = get_password()
print(f'newly generated password --> {password}')
