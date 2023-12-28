#!/usr/bin/env python3
# pw.py - An insecure password locker program
import randompswd
import pyperclip
print('Press y/Y to create random password. Press n/N to cancel')
generate = input()
if generate == 'y' or generate =='Y' :
    print('Password succesfully created and copied to clipboard:')
    passwd_created = randompswd.passwd_gen()
    pyperclip.copy(passwd_created )

PASSWORD = {
        'email':''
        }
