import itertools
import string
import secrets
import math

def attack_password(real, strength,wordlist = "ressources/ech.txt"):
    if(strength == 0):
        chars = string.ascii_lowercase + string.digits
        length = 4
        use_wordlist = False
        max_count = math.inf
    if(strength == 1):
        chars = string.ascii_letters + string.digits + string.punctuation
        length = 4
        max_count = 3000000
        use_wordlist = False
    if(strength >= 2):
        chars = string.ascii_letters + string.digits + string.punctuation
        length = 4
        max_count = 8000000
        use_wordlist = True

    if use_wordlist:
        with open(wordlist, "r") as a_file:
            for line in a_file:
                guess = line.strip()
                if guess == real:
                    return 'password is {}'.format(guess)
    count = 0
    for password_length in range(1, length + 1):
        for guess in itertools.product(chars, repeat=password_length):
            guess = ''.join(guess)
            count += 1
            if guess == real:
                return 'password is {}'.format(guess)
            if count > max_count:
                return 'password not found'
    return 'password not found'

def defend_password(strength):
    if strength == 0:
        chars = string.ascii_letters + string.digits
        length = 4
    if strength == 1:
        chars = string.ascii_letters + string.digits + string.punctuation
        length = 4
    if strength >= 2:
        chars = string.ascii_letters + string.digits + string.punctuation
        length = 6
    password = ''.join(secrets.choice(chars) for i in range(length))
    return password


def simulate_attack_password(attack, defend,wordlist = "/home/kali/Documents/projet_3A/gym-idsgame/gym_idsgame/cyber/ressources/ech.txt"):
    password = defend_password(defend)
    guess = attack_password(password,attack,wordlist)
    return guess != 'password not found'