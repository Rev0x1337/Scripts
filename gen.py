import random
import string

def generate_key(length):
    characters = string.ascii_letters + string.digits
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

key_length = 20
random_key = generate_key(key_length)
print(random_key)
