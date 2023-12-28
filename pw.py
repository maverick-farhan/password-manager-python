#!/usr/bin/env python3
# pw.py - An insecure password locker program
import randompswd
import sys
import pyperclip
PASSWORD = {
        'gmail':'iO;2C-dx@UTXm;XP>bvu',
        'apple':'mB_5$2\'Ku0ez,":!J<^o',
        'linux':'fJ<7i!~OwyRTmg+//oeo'
        }
if len(sys.argv)<2:
    print('Usage: py pw.py [accout] - copy account password')
    sys.exit()
account = sys.argv[1]
print('Press y/Y to create random password. Press n/N to cancel')
generate = input()
if generate == 'y' or generate =='Y' :
    print('Password succesfully created and copied to clipboard:')
    passwd_created = randompswd.passwd_gen()
    pyperclip.copy(passwd_created )

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Your Password for '+ account + 'copied to clipboard')
else:
    print('There is no account '+ account)

