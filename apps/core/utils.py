import random
from string import ascii_lowercase


def generate_short_string():
    characters = ascii_lowercase
    random_string = ""
    for i in range(6):
        random_string += random.choice(characters)

    return random_string