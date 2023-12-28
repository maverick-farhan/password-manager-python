#!/usr/bin/env python3
# randompswd.py - A random password generator
# 20 characters in a passaword ensures a long, strong and reliable password
import random
def passwd_gen():
    low_alpha = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    cap_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special = '`~!@#$%^&*()-+_:;"/.<,>|\''
    letters_length = 20
    password = ''
    all_characters = low_alpha+numbers+cap_alpha+special
    password +=low_alpha[random.randrange(len(low_alpha))]
    password +=cap_alpha[random.randrange(len(cap_alpha))]
    password +=special[random.randrange(len(special))]
    password +=numbers[random.randrange(len(numbers))]
    while letters_length>len(password):
        password+=all_characters[random.randrange(len(all_characters))]
    return password
passwd_gen()
