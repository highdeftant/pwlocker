#!/bin/env python3

passwords = {'email': 'Ce4ijFVMfKeImcv8430PMf',
            'blog': 'Fas94dnbPOTNjrw13',
            'luggage': '493019',
            'social': 'rfkjFIJlapZEClfj37'}

import sys,pyperclip

if len(sys.argv) < 1:
    print('Usage: py pw.py [account] - copy account password')
elif len(sys.argv) > 2:
    print('This program can only copy one password at a time.')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account + '.')
